from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import socket
import sys
import time
import urllib.parse
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = {"atom": "http://www.w3.org/2005/Atom"}


@dataclass
class Paper:
    title: str
    authors: list[str]
    summary: str
    published: dt.datetime
    updated: dt.datetime
    link: str
    pdf: str
    categories: list[str]
    groups: list[str]
    matched_keywords: list[str]
    score: int


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        text = f.read()
    if yaml is not None:
        return yaml.safe_load(text)
    return load_simple_config(text)


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.isdigit():
        return int(value)
    return value


def load_simple_config(text: str) -> dict:
    config: dict = {}
    keywords: dict[str, dict[str, list[str]]] = {}
    current_group: str | None = None
    in_filters = False

    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        if indent == 0 and stripped == "keywords:":
            config["keywords"] = keywords
            current_group = None
            in_filters = False
            continue

        if indent == 0 and ":" in stripped:
            key, value = stripped.split(":", 1)
            config[key] = parse_scalar(value)
            current_group = None
            in_filters = False
            continue

        if indent == 2 and stripped.endswith(":"):
            current_group = stripped[:-1]
            keywords[current_group] = {"filters": []}
            in_filters = False
            continue

        if indent == 4 and stripped == "filters:":
            in_filters = True
            continue

        if indent == 6 and in_filters and current_group and stripped.startswith("- "):
            keywords[current_group]["filters"].append(str(parse_scalar(stripped[2:])))
            continue

    if "keywords" not in config:
        config["keywords"] = keywords
    return config


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def keyword_query(filters: list[str]) -> str:
    terms = []
    for item in filters:
        escaped = item.replace('"', '\\"')
        terms.append(f'all:"{escaped}"')
    return " OR ".join(terms)


def build_query(config: dict) -> str:
    filters: list[str] = []
    for group in config["keywords"].values():
        filters.extend(group.get("filters", []))
    deduped = list(dict.fromkeys(filters))
    return f"cat:cs.CV AND ({keyword_query(deduped)})"


def fetch_entries(query: str, max_results: int, retries: int = 3) -> list[ET.Element]:
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "jperrychen-arxiv-daily/1.0 (https://github.com/jperrychen/arXiv_daily)",
        },
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                body = response.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == retries:
                raise
            wait_seconds = 20 * (attempt + 1)
            print(f"arXiv API returned 429, retrying in {wait_seconds}s...", file=sys.stderr)
            time.sleep(wait_seconds)
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            if attempt == retries:
                raise
            wait_seconds = 15 * (attempt + 1)
            print(f"arXiv API request failed ({exc}), retrying in {wait_seconds}s...", file=sys.stderr)
            time.sleep(wait_seconds)
    root = ET.fromstring(body)
    return root.findall("atom:entry", ATOM)


def match_groups(title: str, summary: str, config: dict) -> tuple[list[str], list[str], int]:
    haystack = f"{title}\n{summary}".lower()
    groups: list[str] = []
    matched: list[str] = []
    score = 0
    for group_name, group in config["keywords"].items():
        group_hits = []
        for keyword in group.get("filters", []):
            if keyword.lower() in haystack:
                group_hits.append(keyword)
        if group_hits:
            groups.append(group_name)
            matched.extend(group_hits)
            score += len(group_hits)
    return groups, list(dict.fromkeys(matched)), score


def entry_to_paper(entry: ET.Element, config: dict) -> Paper | None:
    title = normalize_text(entry.findtext("atom:title", default="", namespaces=ATOM))
    summary = normalize_text(entry.findtext("atom:summary", default="", namespaces=ATOM))
    groups, matched_keywords, score = match_groups(title, summary, config)
    if not groups:
        return None

    published = parse_time(entry.findtext("atom:published", default="", namespaces=ATOM))
    updated = parse_time(entry.findtext("atom:updated", default="", namespaces=ATOM))
    authors = [
        normalize_text(author.findtext("atom:name", default="", namespaces=ATOM))
        for author in entry.findall("atom:author", ATOM)
    ]
    link = normalize_text(entry.findtext("atom:id", default="", namespaces=ATOM))
    pdf = link.replace("/abs/", "/pdf/")
    categories = [
        category.attrib.get("term", "")
        for category in entry.findall("atom:category", ATOM)
        if category.attrib.get("term")
    ]
    return Paper(
        title=title,
        authors=authors,
        summary=summary,
        published=published,
        updated=updated,
        link=link,
        pdf=pdf,
        categories=categories,
        groups=groups,
        matched_keywords=matched_keywords,
        score=score,
    )


def format_authors(authors: list[str], limit: int = 6) -> str:
    if len(authors) <= limit:
        return ", ".join(authors)
    shown = ", ".join(authors[:limit])
    return f"{shown}, et al."


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def strip_urls(value: str) -> str:
    return re.sub(r"https?://\S+", "", value)


def short_summary(value: str, limit: int = 520) -> str:
    value = strip_urls(value)
    value = value.replace("\\%", "%")
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[:limit].rstrip() + "..."


def article_title_with_date(config: dict, date_text: str) -> str:
    title = config.get("article_title", "底层视觉与视频论文速览")
    return f"{date_text}｜{title}"


def render_markdown(papers: list[Paper], config: dict, now: dt.datetime, output_name: str) -> str:
    author = config.get("article_author", "AI论文助手")
    digest = config.get("article_digest", "每周自动筛选底层视觉与视频处理方向论文，汇总摘要、关键词与论文链接。")
    cover = config.get("cover", "./images/cover.jpg")
    date_text = now.strftime("%Y-%m-%d")
    title = article_title_with_date(config, date_text)

    lines = [
        "---",
        f"title: {title}",
        f"author: {author}",
        f"digest: {digest}",
        f"cover: {cover}",
        "---",
        "",
        f"# {title}",
        "",
        f"生成时间：{date_text}",
        "",
        f"本期从 arXiv cs.CV 最新论文中按关键词筛选，覆盖底层视觉、视频处理相关方向。共收录 {len(papers)} 篇，排序优先考虑关键词命中数量，其次参考提交时间。",
        "",
    ]

    if not papers:
        lines.extend(
            [
                "本期没有在时间窗口内命中配置关键词的论文。",
                "",
                "可以放宽 `config.yaml` 中的关键词，或增大 `lookback_days`。",
                "",
            ]
        )
        return "\n".join(lines)

    lines.extend(["## 快速列表", ""])
    for index, paper in enumerate(papers, start=1):
        groups = "、".join(paper.groups)
        lines.append(f"{index}. {groups}｜{paper.title}｜{paper.published.date().isoformat()}")

    lines.append("")
    lines.append("## 论文摘要")
    lines.append("")
    for index, paper in enumerate(papers, start=1):
        groups = "、".join(paper.groups)
        keywords = "、".join(paper.matched_keywords[:10])
        lines.extend(
            [
                f"### {index}. {paper.title}",
                "",
                f"- 方向：{groups}",
                f"- 作者：{format_authors(paper.authors)}",
                f"- 日期：{paper.published.date().isoformat()}",
                f"- 分类：{', '.join(paper.categories)}",
                f"- 关键词：{keywords}",
                f"- arXiv：{paper.link.rsplit('/', 1)[-1]}",
                "",
                "摘要：",
                "",
                short_summary(paper.summary),
                "",
            ]
        )

    lines.extend(
        [
            "## 关键词配置",
            "",
            "本期筛选来自仓库 `config.yaml`。如果希望增加方向，可以在 `keywords` 下新增分组和 `filters`。",
            "",
            f"Markdown 文件：`{output_name}`",
            "",
        ]
    )
    return "\n".join(lines)


def resolve_timezone(name: str) -> dt.tzinfo:
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError:
        if name == "Asia/Shanghai":
            return dt.timezone(dt.timedelta(hours=8), name="Asia/Shanghai")
        return dt.timezone.utc


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch low-level vision and video processing papers from arXiv.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    config = load_config(Path(args.config))
    timezone = resolve_timezone(config.get("timezone", "Asia/Shanghai"))
    now = dt.datetime.now(timezone)
    output_dir = Path(args.output_dir or config.get("output_dir", "outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)

    query = build_query(config)
    fetch_count = max(int(config.get("max_results", 30)) * 2, 30)
    entries = fetch_entries(query, fetch_count)
    cutoff = now.astimezone(dt.timezone.utc) - dt.timedelta(days=int(config.get("lookback_days", 8)))

    papers: list[Paper] = []
    seen: set[str] = set()
    for entry in entries:
        paper = entry_to_paper(entry, config)
        if paper is None or paper.link in seen:
            continue
        if paper.published < cutoff:
            continue
        seen.add(paper.link)
        papers.append(paper)

    papers.sort(key=lambda item: (item.score, item.published), reverse=True)
    papers = papers[: int(config.get("max_results", 30))]

    output_name = f"{now.strftime('%Y-%m-%d')}-low-level-vision-video-papers.md"
    output_path = output_dir / output_name
    output_path.write_text(render_markdown(papers, config, now, output_name), encoding="utf-8")

    latest_path = output_dir / "latest.md"
    latest_path.write_text(render_markdown(papers, config, now, "latest.md"), encoding="utf-8")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"markdown_path={output_path.as_posix()}\n")
            f.write(f"paper_count={len(papers)}\n")

    print(f"Generated {output_path} with {len(papers)} papers.")
    time.sleep(3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
