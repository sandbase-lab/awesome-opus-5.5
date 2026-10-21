"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'opus-5-5'
REPO = 'sandbase-lab/awesome-opus-5.5'

CFG = dict(
    slug=SLUG,
    name='Claude Opus 5.5',
    short='Opus 5.5',  # how the prose refers to the model after the first mention
    vendor='Anthropic',
    model_id='anthropic/claude-opus-5.5',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-opus-5.5',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/anthropic/claude-opus-5.5',
    arena=f'{SITE}/lab/x/llm-arena?models=anthropic%2Fclaude-opus-5.5',
    evals=f'{SITE}/lab/evals',
    pelican=f'{SITE}/lab/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-opus-5-5-sync/1.0 (+https://github.com/{REPO})',
    html_out='opus.html',
    # Output limit for the curl example. `sandbase inspect anthropic/claude-opus-5.5 --json`
    # reports inputSchema.max_tokens.maximum = 128000, and reasoning tokens count toward it,
    # so the example asks for the whole budget.
    max_tokens=128000,
    max_tokens_limit=128000,
    context_length=1000000,
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Claude Opus 5.5',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or rival model names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'astra', 'gpt', 'gemini',
                 'argon', 'deepseek', 'kimi', 'fable', 'sonnet', 'haiku', 'grok', 'qwen', 'glm'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Anthropic.', 'zh-CN': '与 Anthropic 无隶属或背书关系。'},
    # No SandBase blog post on this model existed when the list shipped (blog.sandbase.ai,
    # checked 2026-10-21). build_readme.py skips the reading section while this is empty.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Facts here trace to: `sandbase inspect anthropic/claude-opus-5.5`, the Lab collection's own
# posts (linked), the Lab Evals boards (Artificial Analysis snapshot 2026-10-19) and the Lab
# Pelican Test leaderboard (2026-10-21).
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Claude Opus 5.5 examples**: videos, prompts and demos made with Anthropic\'s flagship Claude 5 model. Motion design is its signature — one prompt, fifteen seconds of code-animated type and shapes — alongside walkable Three.js architecture, playable browser games, procedural 3D and launch films. Most pieces are a single HTML page the model wrote from a prompt, credited to the creator and linked to the original post.',
        'alt': 'Awesome Claude Opus 5.5: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[Claude Opus 5.5 vs. GPT-6 Astra, Fable 5.1, Gemini 4 Argon and DeepSeek V4.1 Flash](docs/model-comparison.md)'),
            ('Try it now', '[Run Claude Opus 5.5 in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. Opus 5.5 reasons before it answers, and those hidden tokens count toward `max_tokens`, so the call above asks for 128,000. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Claude Opus 5.5?', 'Claude Opus 5.5 is Anthropic\'s flagship model in the Claude 5 family: a 1,000,000-token context window, up to 128,000 output tokens, and reasoning support, priced at $4 per million input tokens and $20 per million output tokens on SandBase. The earliest creations in this collection were posted on 2026-09-22. On SandBase it is `{model_id}`. Sources: `sandbase inspect anthropic/claude-opus-5.5` and the collection\'s own posts.'),
            ('How are these videos made?', 'The model doesn\'t render video. It writes a web page — HTML with Three.js, Canvas, SVG or WebGL — and the creator records the page playing. Some creators compose in Remotion or HyperFrames and let Opus drive the timeline. The result is resolution-independent and editable, which is why motion designers use it for showreels and launch films. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Claude Opus 5.5 prompt?', 'Ask for one self-contained HTML file, name the renderer, describe the sequence beat by beat, and set a creative bar ("like your showreel"). Supply inputs (states, photos, a BPM track) instead of pasting content, and forbid external assets so the page runs offline. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Claude Opus 5.5 API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Claude Opus 5.5 better than GPT-6 Astra, Fable 5.1, Gemini 4 Argon or DeepSeek V4.1 Flash?', 'Two evidence classes. **Measured:** on the Lab [Evals boards]({evals}) (Artificial Analysis snapshot 2026-10-19) Opus 5.5 ranks **#1 of 695** on the Intelligence Index at 57.6; the coding and agentic boards have no row for it yet; its blended cost of $5.982 per million tokens ranks #188 of 190 and its 97.79 tokens per second ranks #187 of 371. On the Lab [Pelican Test]({pelican}) it scores 3.46, rank 4 of 22, at about $0.199 a drawing — the most expensive of the top five. **Reported:** creators split against GPT-6 Astra — some prefer Opus for taste and detail, others Astra for jelly-like material or deck detail — while several say it beats Fable 5.1 outright. Details and links: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report a $2 one-minute launch video, $8.95 for a Three.js Eiffel Tower (10 minutes), $13.3 for a 35-minute Blender scene (199.6k output tokens), and $60–$68 for multi-hour pieces at 56M–130M tokens. SandBase list price is $4 per million input tokens and $20 per million output tokens; reasoning tokens bill as output.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Claude Opus 5.5 creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Claude Opus 5.5 prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Claude Opus 5.5 videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Claude Opus 5.5 案例**合集：用 Anthropic Claude 5 系列旗舰模型做出的视频、提示词和演示。最出彩的是动效设计——一句提示词、十五秒纯代码动画；也有可以走进去的 Three.js 建筑、浏览器里能玩的游戏、程序化 3D 和发布片。大多是模型按提示词写出的单个 HTML 页面，均注明作者并链接原帖。',
        'alt': 'Awesome Claude Opus 5.5：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[Claude Opus 5.5 对比 GPT-6 Astra、Fable 5.1、Gemini 4 Argon 和 DeepSeek V4.1 Flash](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Claude Opus 5.5]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。Opus 5.5 会先推理再作答，隐藏的推理 token 也占用 `max_tokens`，所以上面的示例给到 128000。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Claude Opus 5.5 是什么？', 'Claude Opus 5.5 是 Anthropic Claude 5 系列的旗舰模型：上下文窗口 100 万 token，最多输出 12.8 万 token，支持推理；在 SandBase 上每百万输入 token 收费 $4、每百万输出 token 收费 $20。本合集最早的作品发布于 2026-09-22。在 SandBase 上它是 `{model_id}`。来源：`sandbase inspect anthropic/claude-opus-5.5` 与本合集的原帖。'),
            ('这些 Claude Opus 5.5 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页（用 Three.js、Canvas、SVG 或 WebGL 的 HTML），作者再把页面播放过程录下来；也有作者用 Remotion 或 HyperFrames 组织时间线，让 Opus 驱动画面。产物与分辨率无关、还能继续改，所以动效设计师拿它做 showreel 和发布片。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Claude Opus 5.5 提示词？', '要求它输出一个独立 HTML 文件，说明用哪个渲染方式；按节拍描述整段过程，并给一个创作标尺（比如"当作你的 showreel，全力以赴"）。用输入清单（界面状态、照片、BPM 音乐）代替直接给内容，并禁止外部素材，保证页面离线可跑。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Claude Opus 5.5 API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Claude Opus 5.5 比 GPT-6 Astra、Fable 5.1、Gemini 4 Argon 或 DeepSeek V4.1 Flash 更强吗？', '分两类证据。**实测：** Lab [Evals 榜单]({evals})（Artificial Analysis，2026-10-19 快照）上，Opus 5.5 的智能指数 57.6，在 695 个模型中排 **第 1**；编码和 agentic 榜还没有它的数据；混合成本 $5.982/百万 token，在 190 个模型中排第 188，速度 97.79 token/秒，在 371 个模型中排第 187。Lab [Pelican Test]({pelican}) 得分 3.46，22 个模型中排第 4，每张图约 $0.199，是前五名里最贵的。**创作者反馈：** 与 GPT-6 Astra 各有胜负——有人更喜欢 Opus 的品味和细节，也有人觉得 Astra 的果冻质感或甲板细节更好；面对 Fable 5.1 则多位创作者认为 Opus 明显更强。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告：一分钟发布片约 $2；Three.js 埃菲尔铁塔 $8.95（10 分钟）；Blender 场景 $13.3（35 分钟，19.96 万输出 token）；多小时的长片在 $60–$68，消耗 5600 万到 1.3 亿 token。SandBase 标价为每百万输入 token $4、每百万输出 token $20，推理 token 按输出计费。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Claude Opus 5.5 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Claude Opus 5.5 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Claude Opus 5.5 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
