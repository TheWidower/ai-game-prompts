# Tool adaptations

Write a **universal prompt** first (no vendor flags). Then clone it into the tools the user named. If they named none, ship Midjourney + Flux/SD for images, Kling + Veo for video, and a chat-LLM version for text.

Tool flags change. Prefer durable language. Put vendor syntax only in the variant block.

## Images

### Universal (any image model)

Prose, production-first, Style Bible on top, constraints at the end. No `--` flags.

### Midjourney

- Keep the universal prose. Add parameters on one trailing line.
- Consistency — style reference on a winner (`--sref`), character reference when they have a sheet (`--cref`), seed reuse when iterating one subject.
- Isometric — say "orthographic projection, 30-degree isometric, no vanishing point" plus a square or near-square aspect.
- Pixel — say the grid size and "clean pixel edges, no smear". MJ will still need downsample + cleanup.
- Typical useful knobs — aspect, stylize mid-low for assets (assets want control, not extra flourish), no extra text in the image.

Do not dump a long parameter lecture. Give one ready command line.

### Flux / SD / Leonardo-class

- Repeat locked traits verbatim. Separate scene with a pipe or a short second clause.
- Character reference first when the tool supports it. Strength high (about 0.8–1.0) for identity, lower if they need a new pose more than a perfect face.
- Negatives matter here — paste the default avoid list.
- Game-asset LoRAs exist (iso objects, white backdrop). Only mention a trigger word if the user said they have that LoRA.
- For sprites, generate oversized and specify "will be downscaled to NxN, keep chunky shapes".

### Chat image models / Grok Imagine stills

Natural sentences. Front-load subject. No negative-prompt dialect unless the UI has a negatives box. Describe what should be there, not a paragraph of absences — then add a short avoid line.

When generating inside this chat, write the prompt to the image tool exactly as the primary prompt, compressed to 2–5 sentences.

## Video

### Universal

Five slots from `video-cinematics.md`. One motion. Duration named.

### Kling

Subject + Action + Scene + Camera/Lighting/Atmosphere.
Concrete verbs. Good default for cinematic trailer beats and action.

### Veo

Cinematic prose plus a field tail

```
camera: ...
motion: ...
lighting: ...
style: ...
audio: ...
```

Use when they want native sound or dialogue.

### Runway

Shorter than the others. Lead with camera + verb. Cut appearance words that the reference image already shows.

### Grok Imagine video / other I2V

If a still exists, describe only what moves. "Keep identity from the reference."

### Loop tools (Luma and similar)

First frame = last frame intent. Say "seamless loop" and "end pose matches start".

## Text / builders

### General LLM (Grok, Claude, GPT, etc.)

Use `text-design-code.md`. Paste project facts every few turns — camera, engine, verbs already shipped — so the model does not reinvent the game.

### AI-native game engines / vibe-coding builders

One mechanic per message. "Then I will press play." Avoid engine API names unless the user is already in that editor.

### Engine copilots (Unity / Godot / Unreal agents)

Outcome + object name + one property + screenshot/verify. Tiny first request.

## How to present variants

```
### Midjourney
[prompt]
--ar 1:1 ...

### Flux / SD
[prompt]
Negatives: [list]

### Kling
[prompt]
```

Do not claim a tool will hit a pixel grid or a perfect loop. Say what cleanup remains (alpha trim, downsample, tile test, foot-pivot align).
