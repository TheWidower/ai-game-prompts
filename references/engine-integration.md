# Game engine integration workflows

Use this when the user named an engine, asked how generated assets get into a project, or when the Next Prompt should be an import / MCP / editor-agent request — not another pretty picture.

Three integration layers exist in 2026. Do not mix them in one prompt.

1. **File import** — generate outside, drop into Assets / res:// / Content
2. **In-editor generators** — Unity AI Generators, Unreal MetaHuman / EDA, Godot Image Studio style addons
3. **Live editor agents (MCP)** — chat client drives the open editor (scenes, components, screenshots)

Default recommendation
- Shipping / commercial / known engine → layer 1 + 3 (generate assets outside or in-editor, wire with MCP)
- Solo prototype / no engine loyalty → AI-native builder, export Godot or web later
- AAA look / digital humans / cinematics → Unreal + MetaHuman + (optional) NVIDIA ACE

## Shared pipeline (any engine)

```
Style Bible + one-job prompt
        ↓
generate still / mesh / clip / script
        ↓
cleanup (alpha, grid, remesh, maps, loop)
        ↓
import with engine-correct settings
        ↓
collision / pivot / PPU or pixels-per-meter / animator
        ↓
placeholder in a blockout, then playtest
        ↓
only then batch the set
```

Name files for pipelines, not for moods
`char_courier_idle_01_32.png` not `coolFoxFinalv7.png`

Always tell the user what still has to happen after generate — AI output is not engine-ready by default.

## Unity (Unity 6 / 6.x, 2026)

### In-editor AI

- **Sprite Generator** — Project right-click Create > 2D > Generate Sprite, or AI > Generate New > Sprite. Prompt + optional reference + seed. Post tabs — Remove BG, Upscale, Pixelate, Recolor, Inpaint. Promote out of `/GeneratedAssets`.
- **Spritesheet** — source sprite → Remove BG → spritesheet tab (e.g. turntable) → 4×4 sheet + mp4 → drag sheet into scene to make a `.anim`.
- **Texture / UI / 3D Object Generators** — same Generators window. 3D Object Generator returns a static mesh prefab; good for single-part props, not heroes.
- **AI Assistant** can call generators from Agent mode.
- Treat generator output as prototype unless the team has a license/review path to ship it.

### Official agent stack

- Unity MCP Server ships with the in-editor AI Assistant package (Unity 6+). Connects Claude Code, Cursor, Copilot, Windsurf to the live Editor (hierarchy, console, scene edits).
- Official **Unity plugin for Claude Code** (Sep 2026) installs engineering skills (~29), Unity CLI, and MCP. Skills include `/new-unity-project` and `/unity-cli`.
- Community Unity-MCP still exists; prefer official when the user is on Unity 6+.

### File import notes

2D
- Consistent PPU across the set
- Sprite Mode Single vs Multiple; slice sheets
- Filter Mode Point for pixel art; disable mipmaps
- Compression — None or low for pixel; normal maps marked as Normal Map

3D (Meshy / Tripo / 3D AI Studio / Neural4D class)
- Prefer **FBX** for materials; GLB needs GLTFast / UnityGLTF
- Extract materials; assign albedo / normal / roughness-as-smoothness / metallic
- Remesh high-poly AI meshes; add collider on a simple hull, not the render mesh
- Characters — Humanoid rig + Animator; do not expect AI meshes to skin cleanly

Video
- Drop mp4 into Assets; use as Movie Texture / Video Player on a title screen or Timeline track
- Looping gameplay FX often better as a spritesheet or VFX Graph than a movie

### MCP / assistant request shape

```
In the current scene, create [thing] named [Name], set [one property], then take a screenshot.
```

Verify Ready (green) before asking. One object per first request.

## Godot 4.x

### Agent / MCP

- **Godot AI** (dlight / Asset Library, Godot 4.5+) — MCP to Claude Code, Codex, Cursor, etc. Scenes, scripts, UI, materials, particles.
- **godot-ai** (PyPI) — MCP server + editor plugin, 100+ operations.
- **Ziva**, **Golem-AI**, **Godot MCP Studio** — in-dock agents; some add image studio + playtest + screenshot.
- Asset-generation plugins that call Meshy/SD and land a configured resource are still rough. Plan a manual import pass.

### File import notes

2D / pixel
- Drag PNG to FileSystem → Import dock
- Filter Off / Nearest, mipmaps Off
- Repeat Disabled except true tiling textures
- Sprite2D or AnimatedSprite2D; SpriteFrames for anim
- Project stretch mode + viewport size must match the pixel grid
- TileMap / TileSet — keep iso angle and tile size identical to the prompt lock

3D
- **glTF 2.0 (.glb / .gltf) is the recommended format**
- `.blend` works if Blender is installed (Godot calls Blender to export glTF)
- Extract textures when you need to tweak import; add collision separately

Video
- VideoStreamPlayer; keep trailer files out of gameplay loops

### Agent request shape

```
In the active scene, add a CharacterBody2D named Player under the World node, attach a script with move_and_slide only, then run and screenshot.
```

## Unreal Engine 5.7–5.8 (road to UE6)

### First-party character / cinematic path

- **MetaHuman Creator is in-engine** (no browser export hop). Play the character immediately.
- **From Custom Mesh** — fit AI meshes (Meshy, Tripo, scans, sculpts) to MetaHuman rig.
- Collections + pipelines — modular wardrobe slots, build vs assemble.
- Crowds (experimental) — card hair, LOD, Mass spawning.
- MetaHuman DevKit / DNA + Open Rig Logic — take the rig outside Unreal if needed.
- NVIDIA ACE (speech, Audio2Face) + Kimodo motion — on-device companions and promptable animation, refined in-editor.

### Agent / MCP

- UE 5.8 experimental **built-in MCP server** (localhost toolset registry).
- Community **ue-mcp** — large action surface + YAML flows.
- Epic Developer Assistant is being wired to character assembly.

### File import notes

- FBX or glTF into Content. Nanite for static high-poly; do not Nanite skinned heroes by default.
- Pivot, forward axis, unit scale (cm) before you generate a batch.
- Movies → Media Framework / Sequencer, not as gameplay sprites.
- AI textures — Virtual Texturing / streamed; do not ship uncompressed 4K on every prop.

### Agent request shape

```
Under the World folder, spawn an actor named Crate at (0, 100, 0), add a box collision, then screenshot the viewport.
```

## AI-native engines / vibe-coding

Summer Engine and similar sit on Godot 4. Chat builds the scene tree; you still own `.tscn` / `.gd`. Use the text-design-code skill file — one mechanic per prompt, press play, then import art.

Web makers (Rosebud, SEELE-class) are for demos. If the user says "Steam page", steer to Unity / Godot / Unreal / Godot-based AI-native.

## Cross-engine MCP pattern (ai-game.dev family and others)

```
MCP client (Claude Code, Cursor, Copilot, Grok)
    → MCP server
    → editor plugin (live Unity / Godot / Unreal)
```

Rules that do not change by vendor
- Editor must be open and Ready
- Outcome language, not API names
- Name every created object
- Screenshot or compile after each step
- Do not start with "build the whole game"

## What to emit from this skill

When engine is known, append to Next Prompt

1. Cleanup command (remove bg, downsample to grid, remesh, pack ORM)
2. Exact import settings for that engine
3. One MCP / assistant request that places the asset and screenshots
4. Playtest check (PPU mismatch, filter blur, missing collider, wrong scale)

Do not write a 40-step engine tutorial in the chat reply. Link the user to this file's relevant section and give the next 3 actions.

MCP client JSON, ports, and approval flows live in `references/mcp-config.md`.
