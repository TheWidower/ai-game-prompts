---
name: ai-game-prompts
description: Craft production-ready AI prompts and engine-integration packs for game development from text, images, or video. Use when a user wants game prompts, asset prompts, tileset or sprite prompts, trailer or cutscene prompts, GDD or vibe-coding prompts, Midjourney Flux Veo Kling Runway game prompts, Unity Godot Unreal import workflows, MCP server config for Claude Code Cursor or Copilot, Style Bible lock sheets, or a reusable pipeline from idea to in-engine asset.
metadata:
  type: workflow
  version: "2.0"
  domain: game-development
---

# AI Game Prompts

Reusable production pack for AI game work. One skill covers prompt craft, style locks, engine import, and MCP wiring.

Do not re-research this domain from scratch. Read the matching reference and emit copy-paste artifacts.

## Task router

Pick one primary job. Load only the files that job needs.

| User intent | Primary job | Read |
|---|---|---|
| prompts, Midjourney, Flux, sprite, tileset, concept, key art | image pack | `references/image-assets.md`, `references/tool-adaptations.md`, `assets/style-bible-template.md` |
| trailer, cutscene, I2V, ability FX, loop | video pack | `references/video-cinematics.md`, `references/tool-adaptations.md`, `assets/style-bible-template.md` |
| GDD, mechanic, level, dialogue, vibe-coding, AI engine builder | text pack | `references/text-design-code.md` |
| import, PPU, glTF, FBX, filter off, generator window | engine import | `references/engine-integration.md`, `assets/engine-import-cheatsheet.md` |
| MCP, Claude Code, Cursor, `.mcp.json`, ports, relay | MCP config | `references/mcp-config.md`, `assets/mcp-client-templates.md` |
| whole pipeline, "reusable", "from idea to engine" | full pack | `references/playbook.md` plus the rows above that apply |

If they want an image generated in this chat, write the prompt with this skill first, then generate.

## Intake — at most 4 questions

Infer the rest. Guess, then lock.

1. Job — prompt pack / engine import / MCP / full pipeline, plus the exact deliverable.
2. Game frame — genre, camera, platform, engine (Unity, Godot, Unreal, AI-native, none).
3. Style lock — render, palette, light. Draft a Bible if missing (`assets/style-bible-template.md`).
4. Target tool or client — image/video model, or MCP client + OS.

Attached text, images, or video are source of truth. Extract camera, palette, verbs, and shot grammar before writing anything new.

## Core rules

1. One prompt, one job.
2. Production first, pretty second. Asset type, camera, in-game use, technical target — then style.
3. Reuse lock language verbatim. Never "in the same style" as the only lock.
4. Original worlds unless they own the IP. No real-person likeness. Genre feel is allowed.
5. Change one variable per iteration.
6. Readability beats detail.
7. Always ship constraints — grid, background, aspect, view, no text / watermark / logo.
8. Vendor flags stay in the tool-specific variant.
9. Do not mix MCP stacks or ports. Official Unity relay is not community Unity-MCP. Godot `:8000` raw HTTP is not `godot-ai attach`.
10. AI output is not engine-ready. Next step is always cleanup + import settings + one place-and-screenshot request.

## Output shapes

### A — Prompt pack (default)

1. Style Bible
2. Primary prompt (fenced, no commentary inside)
3. Negatives
4. Tool variants (2–3)
5. Batch plan (one-variable deltas)
6. Next prompt (cleanup, turnaround, frame, I2V, or engine/MCP)
7. Sanity check (five questions from the matching reference)

### B — Engine import pack

1. Cleanup steps
2. Exact import settings for the named engine (`assets/engine-import-cheatsheet.md`)
3. One MCP / assistant request that places the asset and screenshots
4. Playtest checks (PPU, filter, collider, scale)

### C — MCP config pack

1. Named stack (official vs community) — never mixed
2. Client file path for their OS
3. One JSON or TOML block with absolute-path placeholders
4. Four live checks — editor open, plugin on, client restarted, tools visible
5. First agent prompt after connect (ping / list tools / screenshot)

Prefer generating the JSON with `scripts/emit-mcp-config.py` when engine, client, and OS are known.

### D — Full pipeline pack

Follow `references/playbook.md`. Emit Bible + first asset prompt + import settings + MCP snippet + first in-engine request. Stop after the first playable slice.

## Prompt anatomy (short)

Image — asset type + job, genre, locked subject, camera, materials, light + palette, technical constraints. Details in `references/image-assets.md`.

Video — shot + lens, subject + one trait, one present-continuous motion, light + atmosphere, duration + audio. Details in `references/video-cinematics.md`.

Text — where + concrete outcome + one behavior + observable success. Details in `references/text-design-code.md`.

## Consistency

Character — turnaround first, then 5–9 frozen trait words, then cref / sref / seed.
Tiles / props — freeze angle and light. Only the noun changes.

## Iteration

Name what worked. Bible + winner traits + one delta. Pretty-but-unusable means a missing production constraint, not more adjectives.

## Guardrails

- No living-person clones, no protected-franchise look-alikes, no sexual content involving minors.
- Flag fuzzy commercial licenses.
- 3D images are concept or texture bases unless they are on a mesh generator. Include scale, pivot, map-set notes.
- Official Unreal MCP has no auth and is loopback-only. Say that when emitting its URL.

## Resource map

- `references/playbook.md` — end-to-end reusable pipeline
- `references/image-assets.md` — image formulas and category starters
- `references/video-cinematics.md` — trailer, cutscene, loop, I2V
- `references/text-design-code.md` — GDD, systems, vibe-coding
- `references/tool-adaptations.md` — Midjourney, Flux / SD, Veo, Kling, Runway, Grok Imagine, chat LLMs
- `references/engine-integration.md` — Unity, Godot, Unreal, AI-native, MCP request shape
- `references/mcp-config.md` — ports, files, approval, security
- `assets/style-bible-template.md` — Style / Char / Set locks
- `assets/engine-import-cheatsheet.md` — import toggles
- `assets/mcp-client-templates.md` — client JSON
- `scripts/emit-mcp-config.py` — print a client config block
