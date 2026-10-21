# Claude Opus 5.5 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步，从一句提示词到一条 MP4。Opus 5.5 写出一个网页，你播放它、录下来。

## 1. 从一条你喜欢的视频开始

在 [合集](../../README.zh-CN.md) 里点开任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，
以及作者公开的提示词。点 **复刻**，Lab 会打开文本竞技场，载入帖子并选中 Claude Opus 5.5。登录、
运行，就能拿回 HTML 和实时预览。

作者没公开提示词？用 [提示词写法](prompt-guide.md) 自己写，文末有填空模板。

## 2. 在同一个提示词上对比模型

在[文本竞技场][arena] 里，给 Opus 5.5 再加一两个模型（比如 `openai/gpt-6-astra`、
`anthropic/claude-fable-5.1`、`google/gemini-4-argon` 或 `deepseek/deepseek-v4.1-flash`），
运行一次。每个模型拿到同样的文字，各自显示花费和耗时。本合集里的对比视频大多就是这么做的：
同一提示词、同一素材，两个结果并排。它也是验证[对比页](model-comparison.md)结论最快的办法。

## 3. 或者直接调 API

Claude Opus 5.5 在 SandBase 上是 `anthropic/claude-opus-5.5`，兼容 OpenAI。

1. 在[控制台][keys] 创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词存成 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "anthropic/claude-opus-5.5",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > opus.html
jq '.usage' response.json
```

- `max_tokens: 128000`：这是模型的输出上限，Opus 5.5 的隐藏推理 token 也占用同一份额度。长页面
  直接给满；给得太紧，页面会被截断，token 照样计费。
- `--max-time 900`：长页面可能要跑几分钟。创作者报告：Three.js 埃菲尔铁塔 10 分钟
  （[@Bhavani_00007][eiffel]），程序化 Blender 镜头 35 分钟（[@Stefan_3D_AI][stefan]），
  长片 2 小时（[@dhruvalgolakiya][dhruval]），`max` 强度的 1.3 亿 token 作品 3 小时
  （[@songkeys][songkeys]）。
- `sed '/^```/d'` 用来去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示实际计费的 token，包括 `completion_tokens_details.reasoning_tokens`。
  输入每百万 token $4，输出每百万 token $20；价格见[模型页][model]。
- 可选：`reasoning_effort` 用思考换速度与成本。想要 showreel 的创作者都开 `max`；先出草稿时
  可以调低，构图满意后再拉高。

用浏览器打开 `opus.html`。如果是一片空白，打开开发者控制台：常见原因是文件被截断（提高上限）
或 CDN 没加载（要求全部内联）。

### 用 SandBase CLI

同样的调用也可以走 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli)，它同样读
`SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect anthropic/claude-opus-5.5   # 输入字段与价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_anthropic_claude_opus_5_5 -f input.json --timeout 900 -o result.json
```

`-o result.json` 会保存响应；页面在 assistant 消息里，和 API 一样。

## 4. 把页面变成视频

多数创作者直接录屏。要每次得到同样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs)
无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs opus.html opus.mp4 12 1920 1080   # 1080p，录 12 秒
```

它按你给的尺寸打开页面、录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的结果，就在提示词里
要求自动运镜或固定时长循环（见[提示词写法第 7 条](prompt-guide.md#7-要求自检和一条录制路径)），
让成片不依赖鼠标。

想要声音？录制只有画面，音频在剪辑里加。也有创作者把免版税音乐直接写进页面，录制时就带上了；
如果你录的是带声音的页面，抓标签页音频，不要用麦克风。

本列表里不少作品不是一次 API 调用，而是走工具链：Remotion 或 HyperFrames 做发布片
（[@bridgemindai][bridge]），Blender 做程序化 3D（[@Stefan_3D_AI][stefan]），而动效 showreel
大多是"一句提示词、一个 HTML 文件"（[@stephanlivera][stephan]）。

## 安全地运行生成的代码

HTML 是你没读过的代码。单个文件从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。
对不信任的页面，或要批量自动运行，用 [SandBase Sandbox][sandbox]：一个隔离环境，有时限，
访问不到你的文件和密钥。

## 分享

把视频发到 X，附上提示词并提到 Claude Opus 5.5。想收录到这里，请[提交作品](https://github.com/sandbase-lab/awesome-opus-5.5/issues/new?template=submit-video.yml)；
通过后会进入 Lab 合集，并在下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/opus-5-5?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=anthropic%2Fclaude-opus-5.5&utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[model]: https://www.sandbase.ai/model/anthropic/claude-opus-5.5?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[eiffel]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102795814355763277?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[stefan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102471841046786153?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[dhruval]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102733714845491558?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[songkeys]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102743212922384673?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[bridge]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102462889160286423?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[stephan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103315922098470926?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
