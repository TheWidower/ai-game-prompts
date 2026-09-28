# Image asset prompts

## Master formula

Write in this order. Drop a slot only if it is truly unknown.

1. Asset type + game job — "32px side-view idle sprite for a 2D platformer"
2. Genre / world — "coastal lantern-folk fantasy, original setting"
3. Subject + locked traits — "fox-eared courier, rust-red scarf, tin lantern, patched green coat"
4. Camera / layout — "orthographic side view, feet planted on a ground line, full body in frame"
5. Materials + shape language — "cloth folds simplified, metal with 2 highlight ticks, rounded silhouette"
6. Lighting + palette — "soft light from upper left, 12-color warm dusk palette, no neon"
7. Technical constraints — "transparent background, 512 square then downscale to 32, no text, no logo, no watermark"

Put the project's Style Bible above this block on every prompt.

## Default negatives

text, watermark, signature, logo, UI mockup chrome, real-person likeness, franchise mark, extra limbs, extra fingers, extra weapons, cropped weapon, unreadable silhouette, messy background clutter, photoreal skin pores (unless the Bible is realistic), inconsistent camera, perspective distortion (when ortho/iso is required), frame-in-frame, deformed face, blurry pixel edges

Add style-specific bans from the Bible (example — "no gradients" for pixel, "no thick black outline" for painterly).

## Quality gate (use in the reply sanity check)

1. Can a teammate name the asset type in three seconds?
2. Does the camera match the game camera?
3. Is subject separable from background for engine use?
4. Any protected marks, real faces, or franchise fingerprints?
5. Can this prompt be reused for the next asset by swapping only the noun?

If any answer is no, revise the prompt rather than praising the picture.

## Camera cheat sheet

- Side-view platformer — orthographic profile or 3/4; feet on a shared ground line; consistent horizon
- Top-down / twin-stick — 90° or slight 3/4 top; head and weapon readable from above; no tall perspective
- Isometric / city-builder — "orthographic projection, 2:1 iso, 30-degree game iso, no vanishing point"
- Third-person action — 3/4 hero shot or turnaround; readable back-mounted gear
- First-person — hands + weapon viewmodel; no face; barrel and iron sights aligned
- UI / icons — orthographic, centered, padding on all sides, no scene
- Key art / store page — cinematic perspective allowed; leave negative space for logo and badges

## Specs by asset class

### Character / NPC concept

Lead with role and silhouette. Lock 5–9 traits.

Starter
```
[BIBLE]
character concept for an original [genre] game, [role] [species], [3 body traits], [outfit], [signature prop], full-body, [camera], readable silhouette, [lighting], [palette], plain backdrop, no text, no logo, no franchise references
```

Always follow a winner with a **turnaround** prompt — front, 3/4, side, back, same height, same light.

### Creature / boss

Demand readable weak points and scale cues (human-height mark, arena floor).

Starter
```
[BIBLE]
boss concept for an original [genre], [creature], towering but readable weak points on [location], [materials], arena-scale floor, [camera], dramatic rim light, no text, no logos
```

### Sprite (idle, walk, attack)

Author on a pixel grid. Ask for one frame or one strip, not a novel.

Starter
```
[BIBLE]
[N]x[N] pixel art [action] sprite of [character lock], [view], limited [N]-color palette, feet planted, full body, transparent background, clean pixel edges, no anti-alias smear, no text
```

Animation follow-up — same seed language, only the pose verb changes (idle → walk 1 of 4 → walk 2 of 4). Call out onion-skin consistency — same proportions, same pivot at the feet.

### Tileset / isometric tile

Freeze angle and light. One object per prompt. Mention seam behavior.

Starter
```
[BIBLE]
[N]x[N] 2:1 isometric [object] terrain tile, flat playable top, visible [side material], soft north-west light, seamless edges, transparent background, no characters, no props sitting on the tile unless requested, no text
```

Test language to include — "tileable, no obvious repeating landmark".

### Prop / weapon / item icon

Treat as a family. Same angle, same light, same outline weight.

Starter
```
[BIBLE]
game-ready [prop] icon, [material notes], consistent 3/4 view, centered, padding around silhouette, transparent background, rarity accent in [color], no text, no drop shadow unless Bible allows
```

Weapon sheets — side view plus silhouette comparison. No embedded labels in the image (add labels in engine or a separate overlay).

### Texture / material

Starter
```
[BIBLE]
tileable [surface] game texture, [material], even lighting, no large unique landmark, no text, power-of-two friendly, PBR albedo only
```

If they need a full PBR set, emit four sibling prompts — albedo, normal, roughness, AO — each stating the same surface and "matching the albedo layout".

### UI / HUD

Judge by hierarchy and tap targets, not ornament.

Starter
```
[BIBLE]
[mobile/desktop] game HUD, [genre], health + resource + objective + menu button, high contrast, large touch targets, diegetic-adjacent [theme], empty center for gameplay, no brand marks, no unreadable script
```

### Environment / biome / loading screen

Call out traversal, landmarks, and player-safe floor.

Starter
```
[BIBLE]
biome concept, [place], readable path through [foreground], landmark [mid], atmosphere [back], [palette], gameplay-readable silhouettes, space at [top/bottom] for UI, original world, no text
```

### Key art / store capsule

Cinematic camera allowed. Leave title-safe negative space.

## Batch plan pattern

Ask for 6–10 variations. After the user picks two winners, emit deltas that change only one of
- pose / action
- time of day
- material wear
- rarity tier
- facing direction
- crop (bust vs full body)

## 3D concept extras (when they will model later)

Add to the prompt or as a sibling spec
- real-world scale (character 1.7 m, door 2.1 m)
- pivot hint (weapon at grip, door at hinge, modular wall at snap corner)
- expected maps (base color, normal, packed ORM)
- "concept sheet, not final mesh" so the image model does not fake topology

## Category starter pack (swap nouns, keep structure)

- Fantasy boss — towering silhouette, weak points, layered armor, arena floor, crimson rim
- Roguelike dungeon map — top-down, looping corridors, encounter rooms, treasure pockets, parchment, readable symbols
- Pixel platformer tileset — modular ground, cliff edges, hazards, limited palette, 16-bit readability
- Cozy village map — warm afternoon, shops, wells, winding paths, painterly map
- Cyberpunk NPC portrait — invented medic, neon rain, faction accent, dialogue crop, no real likeness
- Inventory icon set — consistent angle, rarity colors, transparent-ready
- Sci-fi corridor — depth lines, cover spots, emergency lights, playable hallway
- Low-poly prop pack — orthographic, coherent palette, modular dressing
- Companion creature — animation-ready limbs, scale next to a crate, friendly posture
- Viewmodel gun — first-person hands, original firearm design, iron sights aligned
