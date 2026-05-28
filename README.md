# 每周底层视觉与视频处理论文自动汇总

这个仓库用于每周自动从 arXiv `cs.CV` 抓取底层视觉、视频处理相关论文，生成 Markdown，并可通过 `wxpost-cli` 创建微信公众号草稿。

目标 GitHub 仓库：[jperrychen/arXiv_daily](https://github.com/jperrychen/arXiv_daily)

## 已配置方向

- 底层视觉：image restoration、super-resolution、denoising、deblurring、low-level vision 等。
- 视频处理：video restoration、video super-resolution、video compression、frame interpolation 等。
- 顶会论文：CVPR、CVPR 2026 等标题或摘要命中项。

关键词在 `config.yaml` 中维护。

## 本地运行

```bash
python scripts/fetch_arxiv.py
```

生成文件位于 `outputs/`：

- `outputs/YYYY-MM-DD-low-level-vision-video-papers.md`
- `outputs/latest.md`

如需创建公众号草稿，先生成默认封面：

```bash
python scripts/generate_cover.py
```

## GitHub Actions 定时运行

工作流文件：`.github/workflows/weekly-papers.yml`

默认计划为北京时间每周一 09:00 运行，对应 GitHub Actions cron：

```text
0 1 * * 1
```

也可以在 GitHub 仓库的 Actions 页面手动触发 `Weekly CV Papers`。

## 公众号草稿与发布

工作流会先提交生成的 Markdown。若仓库配置了下面的 Secrets，会继续创建微信公众号草稿：

- `WXPOST_ENV_JSON`：`@rongyan/wxpost-cli` 需要的 `env-cli.json` 完整内容。
- `WXPOST_AUTO_PUBLISH`：设置为 `true` 时，创建草稿后继续发布；不设置或不是 `true` 时只创建草稿。

建议先只配置 `WXPOST_ENV_JSON`，确认草稿格式没有问题后，再决定是否开启 `WXPOST_AUTO_PUBLISH`。

## 调整抓取范围

修改 `config.yaml`：

- `max_results`：每期最多保留多少篇。
- `lookback_days`：向前回看多少天。
- `keywords`：方向分组和关键词列表。

脚本按关键词命中数量和提交时间排序。arXiv 本身不提供热度数据，所以这里的“热点”指近期且与配置关键词高匹配的候选论文。
