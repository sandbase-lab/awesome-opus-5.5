# Claude Opus 5.5 提示词写法：七条来自真实作品的模式

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

下面每一条都来自本合集里作者公开的提示词，并链接到对应帖子。它们不是模型强制的规则，
而是"想要一支十五秒的片子、并且真的拿到了"的写法。

一句话版本：**说清要什么文件、给一个创作标尺、按节拍编排、把素材当契约交出去、守住不变量、
禁掉偷懒的招、最后要求一条录制路径。**

## 1. 第一句就写清交付物、时长和渲染方式

这个合集里被复用最多的提示词只有一句，而且没有任何画面描述：

> "make a dynamic 15-second motion graphics video that shows what an incredible motion
> designer you are, like it's your showreel for a résumé. go all out."
> — [@stephanlivera][stephan]

它有效，是因为语言模型理解的"视频"其实是"一个能渲染出视频的网页"：模型必须自己选渲染器、
时长和画幅。与其让它猜，不如直接写出来——单个 HTML 文件、1920×1080、15 秒、Canvas/SVG/Three.js。

## 2. 给创作标尺，而不是功能清单

"go all out" 和 "like your showreel" 是有实际作用的。加了品味参照的创作者，拿到的是能和人类
作品放在一起看的动效；只列功能的提示词，拿到的往往是演示：

> "Dribbble-level UI motion. One shape, never cut…"
> — [@twoclipping][twoclipping-ui]

标尺只需要一行："像 Apple 发布会"、"像一张 Dribbble 作品"、"像你最喜欢的那部电影片头"，
选一个，放在交付物旁边。

## 3. 按节拍编排时间线，一镜到底

最强的提示词描述的是**转场**，不是场景。下面这段用一整段讲每个状态如何变成下一个：

> "An Apple-keynote launch film, 2D only, one continuous take. Every scene is made out of the
> previous one: nothing fades, blurs or cuts. Objects change shape instead: text rises out of
> a mask line, icons pop from zero on a spring, bars draw across, pages push, and a black
> shape floods the whole frame and contracts into the next scene."
> — [@twoclipping][twoclipping-launch]

如果你只说"先出现手机，再出现图表，最后出现 logo"，得到的就是硬切。描述是什么把视线从上一个
镜头带到下一个——一个形状、一个光标、一次颜色漫延——模型才会真的把它动画化。

## 4. 把素材当契约交出去

不要直接把内容粘进去，而是告诉模型它可以向你要什么，并给出跳过时的默认值，保证页面照样能跑：

> "<inputs>Ask me for: 8 to 12 UI states I want the shape to become (e.g. button, loader,
> player, slider, toggle, tabs, chart, command palette, toast) …"
> — [@twoclipping][twoclipping-ui]

> "If I skip anything, use the defaults: the food-ordering story below, food photos from
> Pexels … and Mixkit 'Cat Walk'."
> — [@ultimaxbt][ultimax]

这也是模板可复用的关键：换品牌时只换输入，不改代码。

## 5. 写清什么必须始终不变

给模型"不变量"——十五秒里一直成立的东西。它能在模型想不出下一步时，阻止它切到一个新场景：

> "One shape, never cut: every state is the same element morphing its size, radius and color
> while its content swaps with a short blur. A cursor drives every change with real clicks and
> drags."
> — [@twoclipping][twoclipping-ui]

> "120 BPM, 54 beats, something happens on every beat."
> — [@twoclipping][twoclipping-launch]

固定的节拍数、固定的色板、一条连续的运镜、一个始终在变形的物体：挑一个能让作品"像设计过"的
不变量。

## 6. 禁掉偷懒的招

最好的提示词都以一张明确的禁用清单结尾。它比事后返工便宜：

> "Banned: crossfades, blur-ins, brightness 'developing', 3D flips, particles, glows, holds
> longer than 1s, anything that looks like a template."
> — [@twoclipping][twoclipping-launch]

技术上的也一起禁：不要外部素材、不要 CDN 引入、不要视频文件、不要生成人物。有位创作者把这类
作品成立的原因说得很清楚：

> "no video model, no AI-generated people. Claude writes the animation as code, so every word,
> number and timing is yours to change."
> — [@N01ennn][n01]

## 7. 要求自检和一条录制路径

结尾加两行，能省掉一轮返工：打开页面、修掉控制台报错，并给出录制方式。固定时长循环或自动运镜
意味着成片不依赖鼠标：

> "here's a floor plan and photos for one house. build it as a three.js site…"
> — [@everestchris6][floorplan]

再接上 [`scripts/record.mjs`](../../scripts/record.mjs)（12 秒、1080p），不用录屏软件也能得到 MP4。
命令见 [教程](tutorial.md)。

## 填空模板

```text
一个独立的 HTML 文件，1920x1080，{秒数} 秒，{渲染方式}，不使用外部素材。

目标：{一句话——观众应该感受到或理解什么}。
创作标尺：{像 Apple 发布会 / 一张 Dribbble 作品 / 你的 showreel——全力以赴}。

节拍：{BPM} BPM，{n} 拍，每一拍都有事情发生。
开场：{第一帧}。然后：{转场 1 -> 2 -> 3}。收尾：{最后一帧，与第一帧呼应}。

不变量：{始终不变的一个物体 / 色板 / 运镜}。
禁用：交叉淡化、模糊入场、库存视频、生成人物、任何超过 1 秒的静止、任何像模板的东西。

输入：向我索要 {照片 / 状态 / 音乐}，否则使用这些默认值：{默认值}。

结束前：打开页面，修掉控制台报错，并让动画能干净地循环 {秒数} 秒以便录制。
```

## 这些提示词的出处

- [@stephanlivera][stephan]——十五秒 showreel 提示词，1.7 万赞。
- [@twoclipping][twoclipping-ui]——UI 状态变形模板及其 `<inputs>` 段。
- [@twoclipping][twoclipping-launch]——带节拍、禁用清单和实现步骤的发布片提示词。
- [@ultimaxbt][ultimax]——带默认值的产品发布片提示词。
- [@everestchris6][floorplan]——从户型图到可走入的 Three.js 房子。
- [@N01ennn][n01]——为什么代码动画比视频模型更可控。
- [@robinebers][canvas]——把架构画成"可以缩放移动的画布"。

[stephan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103315922098470926?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[twoclipping-ui]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103273003555402193?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[twoclipping-launch]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103835273813496100?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[ultimax]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2108210884799549714?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[floorplan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2110036224320884998?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[n01]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2108520767092597182?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[canvas]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2105309987983745060?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
