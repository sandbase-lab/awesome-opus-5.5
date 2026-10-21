# Claude Opus 5.5 prompt guide: seven patterns from real videos

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Every pattern below is lifted from a prompt a creator published with a video in this
collection, and each one links to that post. They are not rules the model enforces; they are
what worked when someone asked for a fifteen-second film and got one.

The short version: **say what file you want, set a creative bar, choreograph the beats, hand
over the inputs, protect the invariants, ban the cheap tricks, and ask for a recording path.**

## 1. Name the deliverable, the duration and the renderer in the first sentence

The most-reused prompt in this collection is one sentence, and it contains no visual
description at all:

> "make a dynamic 15-second motion graphics video that shows what an incredible motion
> designer you are, like it's your showreel for a résumé. go all out."
> — [@stephanlivera][stephan]

It works because "video" on a language model means "a page that renders a video": the model
has to pick a renderer, a duration and a frame. Say those out loud instead of leaving them to
chance — one HTML file, 1920×1080, 15 seconds, Canvas/SVG/Three.js.

## 2. Set a creative bar instead of a specification

"Go all out" and "like your showreel" are doing real work. Creators who added a taste
reference got motion design that holds up next to human work; prompts that only listed
features got demos:

> "Dribbble-level UI motion. One shape, never cut…"
> — [@twoclipping][twoclipping-ui]

A bar is one line. "Make it look like an Apple keynote", "like a Dribbble shot", "like the
title sequence of a film you admire" — pick one and put it next to the deliverable.

## 3. Choreograph the timeline beat by beat, one continuous take

The strongest prompts describe *transitions*, not scenes. This one spends a paragraph on how
each state becomes the next:

> "An Apple-keynote launch film, 2D only, one continuous take. Every scene is made out of the
> previous one: nothing fades, blurs or cuts. Objects change shape instead: text rises out of
> a mask line, icons pop from zero on a spring, bars draw across, pages push, and a black
> shape floods the whole frame and contracts into the next scene."
> — [@twoclipping][twoclipping-launch]

If you only say "show a phone, then a chart, then a logo", you get cuts. Describe what carries
the eye from one shot to the next — a shape, a cursor, a color flood — and the model animates
it.

## 4. Hand over the inputs as a contract

Instead of pasting content, give the model a list of what it may ask for, plus defaults so the
page still runs when you skip something:

> "<inputs>Ask me for: 8 to 12 UI states I want the shape to become (e.g. button, loader,
> player, slider, toggle, tabs, chart, command palette, toast) …"
> — [@twoclipping][twoclipping-ui]

> "If I skip anything, use the defaults: the food-ordering story below, food photos from
> Pexels … and Mixkit 'Cat Walk'."
> — [@ultimaxbt][ultimax]

This is also how you get a reusable template: the same prompt runs on a different brand by
changing the inputs, not the code.

## 5. State what must never change

Give the model invariants — the things that stay true for all fifteen seconds. They stop it
from escaping into a new scene when it runs out of ideas:

> "One shape, never cut: every state is the same element morphing its size, radius and color
> while its content swaps with a short blur. A cursor drives every change with real clicks and
> drags."
> — [@twoclipping][twoclipping-ui]

> "120 BPM, 54 beats, something happens on every beat."
> — [@twoclipping][twoclipping-launch]

A beat count, a fixed palette, one continuous camera move, a single morphing object: pick the
invariant that makes the piece feel designed.

## 6. Ban the escape hatches

The best prompts end with an explicit ban list. It is cheaper than fixing the result:

> "Banned: crossfades, blur-ins, brightness 'developing', 3D flips, particles, glows, holds
> longer than 1s, anything that looks like a template."
> — [@twoclipping][twoclipping-launch]

Add the technical bans too: no external assets, no CDN imports, no video files, no generated
people. One creator summarised why the whole genre works at all:

> "no video model, no AI-generated people. Claude writes the animation as code, so every word,
> number and timing is yours to change."
> — [@N01ennn][n01]

## 7. Ask for a self-check and a recording path

Two lines at the end save a round trip: ask it to open the page, fix console errors, and give
you a way to record it. A fixed-length loop or an autoplay camera tour means nothing depends
on a mouse:

> "here's a floor plan and photos for one house. build it as a three.js site…"
> — [@everestchris6][floorplan]

Pair that with [`scripts/record.mjs`](../scripts/record.mjs) (12 seconds, 1080p) and you have
an MP4 without a screen recorder. The [tutorial](tutorial.md) has the command.

## Fill-in template

```text
One self-contained HTML file, 1920x1080, {seconds} seconds, {renderer}, no external assets.

Goal: {one sentence — what the viewer should feel or understand}.
Creative bar: {like an Apple keynote / a Dribbble shot / your showreel — go all out}.

Beats: {BPM} BPM, {n} beats, something happens on every beat.
Open: {first frame}. Then: {transition 1 -> 2 -> 3}. Close: {last frame, matching the first}.

Invariants: {one object / palette / camera move that never changes}.
Bans: crossfades, blur-ins, stock footage, generated people, holds longer than 1s,
anything that looks like a template.

Inputs: ask me for {photos / states / a track}, otherwise use these defaults: {defaults}.

Before you finish: open the page, fix console errors, and make the animation loop cleanly
for a {seconds}-second recording.
```

## Where these came from

- [@stephanlivera][stephan] — the fifteen-second showreel prompt, 17k likes.
- [@twoclipping][twoclipping-ui] — the UI-state morph template and its `<inputs>` block.
- [@twoclipping][twoclipping-launch] — the launch-film prompt with beats, bans and a build plan.
- [@ultimaxbt][ultimax] — the product-launch film with defaults for skipped inputs.
- [@everestchris6][floorplan] — floor plan to walkable Three.js house.
- [@N01ennn][n01] — why code animation beats a video model for control.
- [@robinebers][canvas] — "a canvas I can zoom in and out and move around" for architecture.

[stephan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103315922098470926?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[twoclipping-ui]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103273003555402193?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[twoclipping-launch]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2103835273813496100?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[ultimax]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2108210884799549714?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[floorplan]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2110036224320884998?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[n01]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2108520767092597182?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
[canvas]: https://www.sandbase.ai/lab/ai-videos/opus-5-5/2105309987983745060?utm_source=github&utm_medium=docs&utm_campaign=awesome-opus-5.5
