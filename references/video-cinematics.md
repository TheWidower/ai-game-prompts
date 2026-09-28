# Video prompts for games

Use for trailers, cutscenes, ability FX, loops, and marketing stingers. Prefer image-to-video when the user already has locked concept art.

## Master formula

1. Shot type + lens feel — "low-angle close-up, 35mm, shallow depth"
2. Subject + one signature trait — "hooded lantern courier, rust-red scarf"
3. One motion, present continuous — "slamming a tin lantern into the cobbles"
4. Lighting + atmosphere — "dusk backlight, wet stone, woodsmoke"
5. Duration + audio note — "5 seconds, hear the lantern glass rattle, no dialogue"

One shot, one motion. Multi-beat trailers are a sequence of prompts, not one paragraph.

## Game jobs

### Trailer beat

Write a 4–8 shot list. Each shot is its own prompt. Label the job (hook, mechanic reveal, threat, character, title card).

Hook pattern
```
[shot], [hero with lock traits] [one verb], [world], [camera move], [grade], cinematic, [N] seconds, [audio]
```

Do not ask a 5-second model to "tell the whole story".

### Cutscene

Lock faces via first-frame image. Keep dialogue off-model unless the target tool does native speech (then write a short line and a delivery note).

```
medium shot of [character lock], [emotion], [one gesture], [location], locked camera or slow push-in, [lighting], [N] seconds
```

### Gameplay-looking loop (idle, run, cast)

Orthographic or locked side camera. Loop-friendly end pose = start pose.

```
side-view game animation of [character lock] [action], looping, constant camera, [style from Bible], no background parallax change, [N] seconds
```

### Ability / VFX

Show cause then effect. Name the element and the body part.

```
close-up game VFX, [character lock] [casts from staff], [element] erupts then collapses back, high contrast against dark ground, 4 seconds, whoosh then crackle
```

### Image-to-video from concept art

The image is the identity lock. The prompt should describe **only motion + camera**, not a new costume.

```
Keep the character, outfit, and colors from the reference frame. Slow dolly-in, cloak stirs, lantern flame flickers, fog drifts left to right, 5 seconds, no new props.
```

## Shot vocabulary (use these words)

Static, slow push-in, pull-out, dolly left/right, tracking follow, orbit, crane up, handheld, locked-off game camera, whip pan (use sparingly), aerial establish.

Avoid stacking three camera moves in one clip.

## Per-model shape (adapt, do not mix)

Details and flags live in `tool-adaptations.md`. Default shapes

- **Kling** — Subject + Action + Scene + Camera/Lighting/Atmosphere. Short concrete verbs.
- **Veo** — cinematic prose, then a field block (camera, motion, lighting, style, audio).
- **Runway** — short, motion-first, often under 40 words. How it moves beats how it looks.
- **Grok Imagine video** — reference-to-video when an image exists; otherwise the five-slot formula.
- **Luma** — keyframe first/last if they have both stills; ask for loop flag when they need idle/run cycles.

## Batch plan

Generate 3 directions before committing a trailer
- atmosphere-led (world)
- mechanic-led (verb the player does)
- character-led (face and motive)

Pick one spine, then fill shot list.

## Quality gate

1. Is there a single readable action?
2. Would this shot cut against gameplay footage without a style shock?
3. Did we ask the model to change identity (new outfit, new face)?
4. Is duration honest for the model?
5. Could this loop or cut on the last frame?

## Common failures and fixes

- Identity drift — switch to I2V; strip wardrobe words from the prompt
- Floaty motion — add weight ("boots scuff stone", "heavy staff")
- Video looks like a movie, not the game — inject Bible camera (side-view / iso) and "game animation, constant focal length"
- Morphing background — "locked environment, only subject moves"
- Unusable for engine — request transparent or solid backdrop, or a clean plate pass
