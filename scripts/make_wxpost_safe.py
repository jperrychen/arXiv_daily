from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONT_MATTER_RE = re.compile(r"\A(---\n.*?\n---\n)", re.S)
PAPER_RE = re.compile(r"^###\s+\d+\.\s+(.+)$", re.M)


def strip_markdown_link(value: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)


def clean_summary(value: str, limit: int) -> str:
    value = re.sub(r"https?://\S+", "", value)
    value = value.replace("\\%", "%")
    value = value.replace("\\textbf{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[:limit].rstrip() + "..."


def parse_papers(body: str) -> list[dict[str, str]]:
    matches = list(PAPER_RE.finditer(body))
    papers: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[start:end]
        paper: dict[str, str] = {"title": strip_markdown_link(match.group(1)).strip()}
        for key in ["方向", "作者", "日期", "分类", "关键词", "链接"]:
            item = re.search(rf"^-\s+{key}：(.+)$", block, re.M)
            if item:
                raw_value = item.group(1).strip()
                if key == "链接":
                    paper[key] = raw_value
                else:
                    paper[key] = strip_markdown_link(raw_value).strip()
        summary = re.search(r"摘要：\s*\n\s*\n>\s*(.+?)(?=\n\n|\Z)", block, re.S)
        if summary:
            paper["摘要"] = clean_summary(summary.group(1), 520)
        papers.append(paper)
    return papers


def arxiv_id(link_line: str) -> str:
    match = re.search(r"(\d{4}\.\d{4,5}v\d+)", link_line)
    return match.group(1) if match else "见 arXiv"


def render_safe(markdown: str, max_papers: int) -> str:
    front = FRONT_MATTER_RE.search(markdown)
    front_matter = front.group(1) if front else ""
    body = markdown[front.end() :] if front else markdown
    papers = parse_papers(body)[:max_papers]

    date_match = re.search(r"生成时间：(.+)", body)
    date_text = date_match.group(1).strip() if date_match else ""

    lines = [
        front_matter.rstrip(),
        "",
        "# 本周底层视觉与视频处理论文速览",
        "",
    ]
    if date_text:
        lines.append(f"生成时间：{date_text}")
        lines.append("")

    lines.extend(
        [
            f"本期选取 {len(papers)} 篇近期 arXiv cs.CV 论文，聚焦底层视觉、视频处理和 CVPR 相关方向。为适配公众号发布，正文保留摘要要点和 arXiv 编号，完整论文可按编号到 arXiv 检索。",
            "",
            "## 本期论文",
            "",
        ]
    )

    for index, paper in enumerate(papers, start=1):
        lines.extend(
            [
                f"### {index}. {paper.get('title', 'Untitled')}",
                "",
                f"- 方向：{paper.get('方向', '')}",
                f"- 作者：{paper.get('作者', '')}",
                f"- 日期：{paper.get('日期', '')}",
                f"- 关键词：{paper.get('关键词', '')}",
                f"- arXiv：{arxiv_id(paper.get('链接', ''))}",
                "",
                "摘要：",
                "",
                paper.get("摘要", ""),
                "",
            ]
        )

    lines.extend(
        [
            "## 说明",
            "",
            "本内容由自动脚本按关键词筛选生成。筛选关键词包括 image restoration、super-resolution、denoising、deblurring、video compression、frame interpolation、CVPR 等。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a WeChat-safe Markdown copy.")
    parser.add_argument("path")
    parser.add_argument("--max-papers", type=int, default=10)
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    path.write_text(render_safe(text, args.max_papers), encoding="utf-8")
    print(f"Rewrote {path} for wxpost with max_papers={args.max_papers}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
