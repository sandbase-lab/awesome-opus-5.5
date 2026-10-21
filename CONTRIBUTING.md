# Contributing

English · [简体中文](#简体中文)

This list mirrors the [Claude Opus 5.5 collection on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/opus-5-5). A GitHub Action pulls it every day, so do not edit `data/` or the READMEs by hand; changes are overwritten on the next sync.

To suggest a video, [open a submission](https://github.com/sandbase-lab/awesome-opus-5.5/issues/new?template=submit-video.yml) with the creator's original X post. It should be a finished piece the creator says was made with Claude Opus 5.5. Lab maintainers review it, add it to the Lab collection, and it appears here after the next sync.

Changes to the scripts or the README layout are welcome as pull requests. Model-specific names, links and README copy live in `scripts/config.py`. Check locally with:

```bash
python3 scripts/sync_lab.py      # pull the current Lab list
python3 scripts/make_previews.py # animated previews for new posts (needs ffmpeg)
python3 scripts/build_readme.py  # READMEs and docs/prompts.md
python3 scripts/make_banner.py   # only when the banner should change (assets/banner-ids.txt)
python3 scripts/validate.py
```

## 简体中文

本列表镜像 [SandBase Lab 上的 Claude Opus 5.5 合集](https://www.sandbase.ai/lab/ai-videos/opus-5-5?lang=zh-CN)，由 GitHub Action 每天自动同步。请不要手动修改 `data/` 或 README，下次同步时会被覆盖。

推荐作品请 [提交表单](https://github.com/sandbase-lab/awesome-opus-5.5/issues/new?template=submit-video.yml) 并附上作者的 X 原帖。作品应是作者说明使用 Claude Opus 5.5 完成的成品。Lab 维护者审核后会加入 Lab 合集，下次同步时出现在这里。

欢迎通过 Pull Request 改进脚本或 README 排版。模型相关的名称、链接和 README 文案都在 `scripts/config.py` 里，本地用上面的命令检查。
