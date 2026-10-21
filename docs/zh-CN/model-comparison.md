# Claude Opus 5.5 对比 GPT-6 Astra、Fable 5.1、Gemini 4 Argon 和 DeepSeek V4.1 Flash

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开写：

1. **我们测的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 数据；Lab [Pelican Test][pelican]
   用同一个固定提示词跑每个模型并打分。样本小，但所有人条件相同。
2. **创作者报告的。** X 上用各自提示词做的对比，附带成本和耗时。有参考价值，但我们没有复核。

本合集最早的作品发布于 2026-09-22，所以实测数据有一个月时间补齐——在通用榜上确实补齐了。
编码和 agentic 榜是另一回事，而这个缺口在有人说"最强模型"时很关键。

## 我们测的：Lab Evals 榜单

Artificial Analysis 2026-10-19 快照。排名是各榜内部的名次，不跨榜比较。

| 模型（榜上的行） | [智能指数][b-intel] | [编码][b-coding] | [Agentic][b-agentic] | [输出速度][b-speed] | [单任务成本][b-cost] |
|---|---|---|---|---|---|
| **Claude Opus 5.5 (Max)** | **57.6（695 个中第 1）** | **榜上暂无** | **榜上暂无** | 97.79 tok/s（371 个中第 187） | $5.982（190 个中第 188） |
| Claude Fable 5.1 (Max) | 53.4（第 6） | 81.6（258 个中第 1） | 57.9（167 个中第 1） | 68.22 tok/s（第 261） | $7.630（第 189） |
| GPT-6 Astra (Max) | 52.7（第 8） | 76.9（第 11） | 51.0（第 14） | 69.29 tok/s（第 260） | $3.258（第 174） |
| Gemini 4 Argon (High) | 52.6（第 9） | — | — | 榜上暂无 | $1.990（第 158） |
| GPT-6.1 Sol (Max) | 51.8（第 13） | — | — | 59.81 tok/s（第 281） | $0.724（第 112） |
| Kimi K3 (Max) | 43.6（第 45） | 76.2（第 20） | 50.0（第 22） | 42.29 tok/s（第 337） | $2.000（第 159） |
| DeepSeek V4.1 Flash 1017 (Max) | 39.5（第 68） | — | — | 231.23 tok/s（第 32） | $0.486（第 96） |

这说明什么：

- **在这份快照上，Opus 5.5 是最强的通用模型。** 57.6 比第二名 Fable 5.1（53.4）高 4 分，比
  DeepSeek V4.1 Flash 高 18 分。如果任务是"想清楚再写好"，实测第一就是它。
- **它没有编码和 agentic 行，这两榜的第一是 Fable 5.1。** 编码 81.6、agentic 57.9 都是榜首。
  拿 Opus 和 Fable 比仓库级工作时，应该说"编码榜还没有 Opus 5.5 的测量"，而不是"Opus 输了"。
- **它贵，速度中游。** 单任务 $5.982 在 190 个模型中排第 188，是 GPT-6.1 Sol 和 DeepSeek
  V4.1 Flash 的十二倍；97.79 token/秒排第 187，落后于 DeepSeek（231）、Gemini 3.8 Flash（158）
  和一众小模型。
- **下面的创作者账单和这个标价对得上。** 10 秒 Blender 镜头 $13.3，5600 万 token 的片子 $68，
  1.3 亿 token 的片子 $60——这不是评测口径的偏差，就是第一名智能的价格。

## 我们测的：Lab Pelican Test

[Pelican Test][pelican] 让每个模型画一只骑自行车的鹈鹕，一次静态、一次动画（轮子转、腿蹬、
只用 CSS/SMIL）。页面渲染成 PNG，由 LLM 评委按四个问题打 0–5 分：认得出、真在骑、车能用、好看。
成本是 SandBase 上的实际计费。

[实时榜单][pelican] 2026-10-21 的排名（22 个模型）：

| 排名 | 模型 | 结果数 | 得分 | 渲染成功 | 动起来 | 平均成本 |
|---|---|---|---|---|---|---|
| 1 | google/gemini-4-argon | 4 | 3.81 | 100% | 100% | $0.120 |
| 2 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.027 |
| 3 | google/gemini-3.7-flash | 6 | 3.63 | 100% | 100% | $0.085 |
| 4 | **anthropic/claude-opus-5.5** | **6** | **3.46** | **100%** | **100%** | **$0.199** |
| 5 | deepseek/deepseek-v4.1-flash | 8 | 3.44 | 100% | 100% | $0.017 |
| 6 | anthropic/claude-sonnet-5.5 | 4 | 3.25 | 100% | 100% | $0.045 |
| 6 | anthropic/claude-haiku-5.5 | 2 | 3.25 | 100% | 100% | $0.008 |
| 6 | minimax/minimax-m3.1-flash | 4 | 3.25 | 100% | 100% | $0.006 |

这说明什么：

- **质量中上，前五里最贵。** 3.46 落后于 Gemini 4 Argon（3.81）和 GPT-6.1 Sol（3.79），略高于
  DeepSeek V4.1 Flash（3.44），但每张图 $0.199——是 DeepSeek 的 7 倍、GPT-6.1 Sol 的 7.4 倍。
  在单个固定提示词上，Opus 的品味优势没有变成分数优势。
- **它很稳。** 6 个结果来自 3 位测试者，全部渲染成功、全部动起来；评委的评语都关于自行车结构，
  不是输出坏了。
- **样本量。** 6 张图、3 个账号。想加样本可以[自己跑一次][pelican-run]。

## 创作者报告的

X 上的同提示词对比。数字按创作者自己的说法：工具不同（Remotion、Blender、Claude Code）、推理
强度不同、往往只跑一次。点进去可以看两边的结果。3D 和游戏对比里最常见的对手是 GPT-6 Astra；
Fable 5.1 更多是作为"比上一代强"的参照出现。

| 创作者 | 任务 | Claude Opus 5.5 | 对手 | 创作者结论 |
|---|---|---|---|---|
| [@Stefan_3D_AI][stefan] | 一句提示词，10 秒程序化 Blender 镜头 | 35 分钟，19.96 万输出 token，约 $13.3 | GPT-6 Astra：28 分钟，5.66 万，约 $14.5 | "配得上的对手"；Opus 同时处理的东西更多，Astra 也不错 |
| [@Bhavani_00007][eiffel] | Three.js 埃菲尔铁塔，一句提示词 | $8.95，10 分钟 | Astra $7.45/8 分钟 · Sol $3.90/5 分钟 · Kimi $4.04/6 分钟 | 前端和 3D 细节更偏好 Opus；Kimi 性价比高 |
| [@Bhavani_00007][whale] | 3D 鲸鱼跃出水面，四个模型 | — | Argon 写实度第一；Opus 和 Kimi 比 Astra 更真实 | Argon 领先，Opus 写实第二 |
| [@shneural][shneural] | 15 秒动效，同一提示词 | — | GPT-6 Astra | "根本不在一个级别"；"GPT 在这里很糟" |
| [@vib3coded][pirate] | 单个 HTML 里的海盗船 | — | GPT-6 Astra | Astra 的甲板细节更好，Opus 整体更亮 |
| [@vib3coded][gummy] | 软糖，同一提示词 | — | GPT-6 Astra | 更喜欢 Astra 的果冻拉伸感，Opus 更亮更光滑 |
| [@bridgemindai][mario] | 一次成型的马里奥赛车 | — | Fable 5.1 | "比 Fable 5.1 好太多"；真的做出了可玩角色 |
| [@bridgemindai][merch] | 用 Remotion 做周边发布片 | — | Fable 5.1、GPT-6 Astra | "比我从 Fable 5.1 或 GPT-6 Astra 拿到的都好" |
| [@rubenssoto_ai][motor] | 特斯拉电机讲解，3D | — | Gemini 4 Argon | 让观众投票 |
| [@rubenssoto_ai][motor-ds] | 同一提示词、同一任务 | — | DeepSeek V4.1 Flash 1017 | "Opus 有麻烦了吗？" |
| [@dhruvalgolakiya][dhruval] | 带声音的长片，3 个提示词 | 2 小时，约 5600 万 token，约 $68 | — | — |
| [@songkeys][songkeys] | 人类起源短片，2 个提示词，max | 3 小时，约 1.3 亿 token，约 $60 | — | — |
| [@deedydas][deedydas] | 教学类发布视频 | 1 分钟，约 $2 | — | "过去要几周……成本高 1000 倍" |
| [@N01ennn][n01] | 同一位 Anthropic 设计师、三个提示词、三个模型 | 手绘故事，53 秒 | Sonnet 5.5：文字动效 15 秒 · Haiku 5.5：配方 30 秒 | 同一份要求三种味道，叙事那条给了 Opus |

单独作品与质量评价：

- [@Stefan_3D_AI][wow] 花 36 小时、约 $2,400 的 API 费用做了一个 WoW 风格游戏：六个种族、
  角色创建、战斗、一个区域和一座石头城。
- [@BubuStd][dynasty] 用 "ultracode" 做了《真·三国无双》风格游戏，然后放手让它跑。
- [@everestchris6][floor] 把户型图加照片变成可以走进去的 Three.js 房子；同类服务地产商每个户型
  要付 $5,000–$10,000。
- [@robinebers][canvas] 要了一块"可以缩放移动的画布"来看 App 架构，结果连步骤和关系图都画出来了。
- [@0xCodila][tv] 靠一张照片、一句提示词和五分钟，反向工程了电视的开发者菜单。

两类证据合起来看：**品味和动效**上，创作者把 Opus 放在第一梯队，好几位说它明显强于 Fable 5.1。
对 **GPT-6 Astra** 则是真正的互有胜负——有的测试 Opus 构图和细节更好，有的 Astra 的材质和甲板
细节更好，成本也接近。对 **Gemini 4 Argon**，写实度上 Argon 占优。没人说 Opus 便宜：实测单任务
成本是前沿模型里最高的，创作者的账单（$13.3、$60、$68）也对得上。

## 重跑一次再决定信不信

结果会随设置变化：推理强度、是否走工具链、要的是单文件还是完整工程、对手有没有拿到同样素材。
实测这边是一份快照和六只鹈鹕，创作者那边每条帖子只跑了一次。自己跑一遍：把提示词贴进
[Lab 文本竞技场][arena]，选两三个模型；步骤见[教程](tutorial.md)。

## 更多实测

- [Lab Evals 榜单][evals]——Artificial Analysis 数据，2026-10-19 快照。先在智能榜搜 "Opus 5.5"，
  再去编码榜确认那个缺口。
- [Lab Pelican Test][pelican]——同一个提示词跑所有模型，同一套标准打分，图都在页面上。
- [SandBase Lab 全部 AI 视频合集][collections]——其他模型的同类列表，包括
  [DeepSeek V4.1 Flash 1017][ds-repo] 和 [Gemini 4 Argon][gemini-repo]。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-19 快照）和 [Pelican Test][pelican]
（2026-10-21 读取）。创作者数据：各自的帖子，已链接，未经我们独立核实。

[evals]: https://www.sandbase.ai/lab/evals?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[b-coding]: https://www.sandbase.ai/lab/evals/llm-coding?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[b-agentic]: https://www.sandbase.ai/lab/evals/llm-agentic?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5&utm_content=run
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=anthropic%2Fclaude-opus-5.5&utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[ds-repo]: https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash
[gemini-repo]: https://github.com/sandbase-lab/awesome-gemini4-argon
[stefan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102471841046786153?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[eiffel]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102795814355763277?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[whale]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2110078803297055212?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[shneural]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103151003272962130?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[pirate]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102533729746882985?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[gummy]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103062348168618280?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[mario]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102451997395866021?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[merch]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102462889160286423?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[motor]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2110065587279798719?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[motor-ds]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2111513156589629941?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[dhruval]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102733714845491558?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[songkeys]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102743212922384673?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[deedydas]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102787937482252537?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[n01]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2108520767092597182?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[wow]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2104109918894580091?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[dynasty]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2102991290568954264?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[floor]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2110036224320884998?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[canvas]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2105309987983745060?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[tv]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2111826236586570101?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
