# Full pipeline playbook

Use this when the user wants a reusable path from idea (text, image, or video) to something that exists in an engine. Do the stages in order. Do not skip verification.

## Stage 0 — Project lock (once)

Fill `assets/style-bible-template.md`. Save the filled block in the reply so every later prompt can paste it.

Also freeze
- engine (or AI-native)
- camera
- pixel grid or world scale
- MCP client + OS if they want editor control

If MCP is in scope, emit config from Stage 5 before generating a hundred assets.

## Stage 1 — One-sentence game

From `references/text-design-code.md`

```
A [camera] [genre] where the player [core verb] using [one mechanic], and wins/loses when [condition]. Tone is [3 words]. Original world.
```

Then the smallest controller prompt. Play / screenshot. Do not art yet.

## Stage 2 — Hero asset only

One subject. Image formula from `references/image-assets.md`.

Order
1. Concept or idle still (Bible on top)
2. Turnaround if it is a character
3. Cleanup (alpha, grid, no watermark)
4. Import with `assets/engine-import-cheatsheet.md`
5. Place + screenshot via MCP shape in `references/engine-integration.md`

Stop. If the still cannot read at game camera, do not batch.

## Stage 3 — Set family

Same Bible. Same camera. Same light. Swap only the noun.
Tiles, props, icons — one object per prompt.
After two winners, batch 6–10 one-variable deltas.

## Stage 4 — Motion

Still-first.
- Spritesheet / frames from the locked still (`references/image-assets.md` sprite section)
- or I2V with motion-only prompt (`references/video-cinematics.md`)
Trailer beats are a shot list, not one paragraph.

## Stage 5 — Editor agent

Config from `references/mcp-config.md` / `scripts/emit-mcp-config.py`.

Live checks
1. Editor open, plugin enabled, status Ready
2. Client restarted
3. Tools listed
4. Pending connection accepted (Unity official)

First requests
```
List tools or ping the plugin.
```
```
In the current scene, assign [asset] to [NamedObject], then take a screenshot.
```

## Stage 6 — Only now expand

More verbs, more rooms, more trailer shots. Each is a new one-job prompt. Keep the Bible frozen.

## Source-media variants

From text — verbs become mechanics; implied camera becomes Bible camera.
From images — describe lock first; change only subject or pose.
From video — steal shot grammar; write I2V + one mechanic prompt if they want the feel playable.

## Reuse kit to hand the user

Always leave them with
1. Filled Style Bible
2. Char / Set lock if relevant
3. Winning prompt text (not just the picture)
4. Engine import 3-liner
5. MCP JSON if they asked
6. The next single prompt

That kit is the skill's reusable output. The conversation is not.
