# Claude Opus 5.5 tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Opus 5.5 writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the
video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab
opens the text arena with the post loaded and Claude Opus 5.5 selected. Sign in, run it, and
you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in
template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to Opus 5.5 (for example
`openai/gpt-6-astra`, `anthropic/claude-fable-5.1`, `google/gemini-4-argon` or
`deepseek/deepseek-v4.1-flash`) and run once. Every model gets the same words, and each result
shows its cost and time. That is how most of the head-to-heads in this collection were made:
the same prompt, the same assets, two results side by side. It is also the quickest way to
check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

Claude Opus 5.5 is `anthropic/claude-opus-5.5` on SandBase, OpenAI-compatible.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 128000`: that is the model's output ceiling, and Opus 5.5's hidden reasoning
  tokens come out of the same budget. Ask for the whole budget on long pages; a tight limit
  gives you a truncated page and still bills the tokens.
- `--max-time 900`: one long page can take minutes. Creators report 10 minutes for a Three.js
  Eiffel Tower ([@Bhavani_00007][eiffel]), 35 minutes for a procedural Blender shot
  ([@Stefan_3D_AI][stefan]), 2 hours for a long film ([@dhruvalgolakiya][dhruval]) and 3 hours
  at `max` effort for a 130M-token piece ([@songkeys][songkeys]).
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for, including
  `completion_tokens_details.reasoning_tokens`. Input is $4 per million tokens and output $20
  per million; prices are on the [model page][model].
- Optional: `reasoning_effort` trades thinking for speed and cost. Creators who wanted a
  showreel ran at `max`; for a quick draft, start lower and only raise it when the composition
  is right.

Open `opus.html` in a browser. If it is blank, open the developer console: the usual causes
are a truncated file (raise the limit) or a CDN that did not load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli),
which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect anthropic/claude-opus-5.5   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_anthropic_claude_opus_5_5 -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly
with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs opus.html opus.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264
MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a
fixed-length loop (see [prompt guide §7](prompt-guide.md#7-ask-for-a-self-check-and-a-recording-path)),
so nothing depends on a mouse.

Want sound? The recording is picture only, so add audio in the edit. Some creators mixed a
royalty-free track into the page itself so the recording carries it; if you record a page with
audio, capture the tab audio, not the microphone.

Many videos in this list came out of a harness rather than a single API call: Remotion or
HyperFrames for launch films ([@bridgemindai][bridge]), Blender for procedural 3D
([@Stefan_3D_AI][stefan]), and plain "one prompt, one HTML file" for the motion-design
showreels ([@stephanlivera][stephan]).

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file
page, but it can still load scripts and make network requests. For anything you don't trust,
or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment
with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Claude Opus 5.5. To have it added here,
[submit it](https://github.com/sandbase-lab/awesome-opus-5.5/issues/new?template=submit-video.yml);
accepted posts go into the Lab collection and show up in this list on the next daily sync.

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
