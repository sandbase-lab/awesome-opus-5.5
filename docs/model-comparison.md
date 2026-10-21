# Claude Opus 5.5 vs GPT-6 Astra, Fable 5.1, Gemini 4 Argon and DeepSeek V4.1 Flash

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the
   Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result.
   Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, costs and
   times. Useful context, not verified by us.

The earliest creations in this collection were posted on 2026-09-22, so the measured side has
had a month to fill in — and for Opus 5.5 it has, on the general-purpose board. The coding and
agentic boards are a different story, and that gap matters when someone says "best model".

## What we measured: Lab Evals boards

Artificial Analysis snapshot of 2026-10-19. Ranks are within each board, not across boards.

| Model (row on the board) | [Intelligence Index][b-intel] | [Coding][b-coding] | [Agentic][b-agentic] | [Output speed][b-speed] | [Cost per task][b-cost] |
|---|---|---|---|---|---|
| **Claude Opus 5.5 (Max)** | **57.6 (#1 of 695)** | **not on the board** | **not on the board** | 97.79 tok/s (#187 of 371) | $5.982 (#188 of 190) |
| Claude Fable 5.1 (Max) | 53.4 (#6) | 81.6 (#1 of 258) | 57.9 (#1 of 167) | 68.22 tok/s (#261) | $7.630 (#189) |
| GPT-6 Astra (Max) | 52.7 (#8) | 76.9 (#11) | 51.0 (#14) | 69.29 tok/s (#260) | $3.258 (#174) |
| Gemini 4 Argon (High) | 52.6 (#9) | — | — | not on the board | $1.990 (#158) |
| GPT-6.1 Sol (Max) | 51.8 (#13) | — | — | 59.81 tok/s (#281) | $0.724 (#112) |
| Kimi K3 (Max) | 43.6 (#45) | 76.2 (#20) | 50.0 (#22) | 42.29 tok/s (#337) | $2.000 (#159) |
| DeepSeek V4.1 Flash 1017 (Max) | 39.5 (#68) | — | — | 231.23 tok/s (#32) | $0.486 (#96) |

What this says:

- **Opus 5.5 is the strongest generalist on this snapshot.** 57.6 is four points clear of the
  next row (Fable 5.1 at 53.4) and eighteen above DeepSeek V4.1 Flash. If the task is "reason
  about this and write something good", it is the measured leader.
- **It has no coding or agentic row, and Fable 5.1 owns both.** 81.6 on coding and 57.9 on
  agentic are the top of their boards. Anyone comparing Opus with Fable for repository-scale
  work should say that the coding board does not have an Opus 5.5 measurement yet — not that
  Opus lost it.
- **It is expensive and mid-pack on speed.** $5.982 per task ranks 188 of 190, twelve times
  GPT-6.1 Sol and twelve times DeepSeek V4.1 Flash; 97.79 tokens per second ranks 187 of 371,
  behind DeepSeek (231), Gemini 3.8 Flash (158) and every small model on the board.
- **The creator cost reports below are consistent with that list price.** A 10-second Blender
  shot billed $13.3, a 56M-token film $68, a 130M-token film $60 — those are not benchmark
  artefacts, they are the price of the top intelligence row.

## What we measured: Lab Pelican Test

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once
static and once animated (wheels spin, legs pedal, CSS/SMIL only). The page is rendered to PNG
and scored 0 to 5 by an LLM judge on four questions: recognizable, actually riding, a bike that
works, looks good. Cost is the real billed amount on SandBase.

Leaderboard rows from the [live leaderboard][pelican] on 2026-10-21 (22 models):

| Rank | Model | Results | Score | Renders | Animation moves | Avg cost |
|---|---|---|---|---|---|---|
| 1 | google/gemini-4-argon | 4 | 3.81 | 100% | 100% | $0.120 |
| 2 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.027 |
| 3 | google/gemini-3.7-flash | 6 | 3.63 | 100% | 100% | $0.085 |
| 4 | **anthropic/claude-opus-5.5** | **6** | **3.46** | **100%** | **100%** | **$0.199** |
| 5 | deepseek/deepseek-v4.1-flash | 8 | 3.44 | 100% | 100% | $0.017 |
| 6 | anthropic/claude-sonnet-5.5 | 4 | 3.25 | 100% | 100% | $0.045 |
| 6 | anthropic/claude-haiku-5.5 | 2 | 3.25 | 100% | 100% | $0.008 |
| 6 | minimax/minimax-m3.1-flash | 4 | 3.25 | 100% | 100% | $0.006 |

What this says:

- **Upper-middle quality, highest price in the top five.** 3.46 puts Opus behind Gemini 4
  Argon (3.81) and GPT-6.1 Sol (3.79), just ahead of DeepSeek V4.1 Flash (3.44), at $0.199 a
  drawing — 7x DeepSeek and 7.4x GPT-6.1 Sol. On a single fixed prompt, Opus's taste advantage
  does not show up as a score advantage.
- **It is consistent.** Six results from three testers, all rendering and all animating; the
  judge's notes are about bicycle geometry, not broken output.
- **Sample size.** Six drawings, three accounts. [Run it yourself][pelican-run] to add more.

## What creators reported

Same-prompt comparisons posted on X. Numbers are as the creator stated them: different tools
(Remotion, Blender, Claude Code), different reasoning settings, often one run. Click through to
watch both results. GPT-6 Astra is the rival in most of the 3D and game head-to-heads; Fable
5.1 shows up mostly as "better than the previous generation".

| Creator | Task | Claude Opus 5.5 | Rival | Creator's verdict |
|---|---|---|---|---|
| [@Stefan_3D_AI][stefan] | 10-second procedural Blender shot, one prompt | 35 min, 199.6k output, ~$13.3 | GPT-6 Astra: 28 min, 56.6k, ~$14.5 | "A worthy rival"; Opus "juggles way more at once", Astra still good |
| [@Bhavani_00007][eiffel] | Three.js Eiffel Tower, one prompt | $8.95, 10 min | Astra $7.45, 8 min · Sol $3.90, 5 min · Kimi $4.04, 6 min | Preferred Opus for frontend and 3D detail; Kimi strong for the price |
| [@Bhavani_00007][whale] | 3D whale breaching, four models | — | Argon wins photorealism; Opus and Kimi "more realistic than Astra" | Argon ahead, Opus second on realism |
| [@shneural][shneural] | 15-second motion graphics, same prompt | — | GPT-6 Astra | "Not even close"; "GPT is honestly terrible here" |
| [@vib3coded][pirate] | Pirate ships in one HTML file | — | GPT-6 Astra | Astra "nailed the deck detail"; Opus brighter overall |
| [@vib3coded][gummy] | Gummy candy, same prompt | — | GPT-6 Astra | Prefers Astra's jelly stretch; Opus glossier |
| [@bridgemindai][mario] | Mario Kart, one shot | — | Fable 5.1 | "Way better than Fable 5.1"; real playable characters |
| [@bridgemindai][merch] | Merch launch film in Remotion | — | Fable 5.1, GPT-6 Astra | "Better than anything I have gotten from Fable 5.1 or GPT 6 Astra" |
| [@rubenssoto_ai][motor] | Tesla-style motor explainer, 3D | — | Gemini 4 Argon | Asks viewers which is better |
| [@rubenssoto_ai][motor-ds] | Same prompt, same task | — | DeepSeek V4.1 Flash 1017 | "Is Opus in trouble?" |
| [@dhruvalgolakiya][dhruval] | Long film with audio, 3 prompts | 2 h, ~56M tokens, ~$68 | — | — |
| [@songkeys][songkeys] | Origin-of-humans film, 2 prompts, max effort | 3 h, ~130M tokens, ~$60 | — | — |
| [@deedydas][deedydas] | Instructional launch video | 1 min, ~$2 | — | "Used to take weeks… 1000x the costs" |
| [@N01ennn][n01] | Anthropic designer's three prompts, three models | Hand-drawn story, 53 s | Sonnet 5.5: kinetic type, 15 s · Haiku 5.5: recipe, 30 s | Same brief, three tastes; Opus got the narrative one |

Solo runs and quality notes:

- [@Stefan_3D_AI][wow] spent 36 hours and about $2,400 of API tokens on a WoW-style game — six
  races, character creation, combat, a zone and a stone city.
- [@BubuStd][dynasty] built a Dynasty Warriors-style game with "ultracode" and let it cook.
- [@everestchris6][floor] turns a floor plan plus photos into a walkable Three.js house; home
  builders pay $5k–$10k per plan for the equivalent.
- [@robinebers][canvas] asked for "a canvas I can zoom in and out and move around" to see an
  app's architecture; it came out with connected graphs and steps.
- [@0xCodila][tv] reverse-engineered a TV's developer menu from a photo, one prompt and five
  minutes.

The pattern across both sources: on **taste and motion design** creators put Opus at or near
the top, and several say it beats Fable 5.1 outright. Against **GPT-6 Astra** it is genuinely
mixed — Opus wins on composition and detail in some tests, Astra wins on material feel and deck
detail in others, and the cost is close. Against **Gemini 4 Argon** the results split on
photorealism, where Argon has the edge. Nobody argues Opus is cheap: the measured cost per task
is the highest of the frontier rows, and the creator bills ($13.3, $60, $68) match it.

## Rerun before you trust a comparison

Results move with the setup: reasoning effort, harness, whether the model was asked for a
single file or a full project, and whether the rival got the same assets. The measured side
here is one snapshot and six pelicans; the creator side is one run per post. Run the prompt
yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see
the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals] — Artificial Analysis data, snapshot 2026-10-19. Search for
  "Opus 5.5" on the intelligence board, then check the coding board for the gap.
- [Lab Pelican Test][pelican] — same prompt on every model, scored the same way, drawings on
  screen.
- [All AI video collections on SandBase Lab][collections] — the same list for other models,
  including [DeepSeek V4.1 Flash 1017][ds-repo] and [Gemini 4 Argon][gemini-repo].

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-19) and [Pelican
Test][pelican] (read 2026-10-21). Creator data: their posts, linked; not independently
verified.

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
