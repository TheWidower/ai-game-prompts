# Engine import cheatsheet

Copy the block for the user's engine. Adjust names only.

## Unity 2D / pixel

```
PPU — same value on every sprite in the set (example 32)
Sprite Mode — Single, or Multiple + slice if it is a sheet
Filter Mode — Point (no filter) for pixel; Bilinear for painted
Mipmaps — Off for pixel
Compression — None or low for pixel
Normal maps — Texture Type = Normal Map
Pixels Per Unit mismatch is the usual "everything is huge/tiny" bug
```

## Unity 3D (FBX from Meshy / Tripo / 3D AI Studio)

```
Format — FBX preferred
Extract Materials
Albedo ← base color
Normal ← normal (mark as Normal Map)
Smoothness ← roughness with Source = Roughness if the shader allows
Metallic ← metallic
Remesh high-poly
Collider on a convex hull or box, not the render mesh
Humanoid + Animator only after the mesh actually skins
```

## Unity generators (in-editor)

```
Sprite — Create > 2D > Generate Sprite, or AI > Generate New > Sprite
Remove BG before spritesheet
Spritesheet tab → sheet + mp4 → drag sheet into scene for .anim
3D Object Generator — static single-part props only
Promote out of /GeneratedAssets
Treat as prototype until license review
```

## Godot 2D / pixel

```
Import dock — Preset 2D
Filter — Off / Nearest
Mipmaps — Off
Repeat — Disabled unless it is a tiling texture
Compression — Lossless or Uncompressed
Node — Sprite2D or AnimatedSprite2D
Anim — SpriteFrames
Match viewport + stretch mode to the prompted pixel grid
```

## Godot 3D

```
Format — glTF 2.0 (.glb)
.blend works if Blender is installed
Extract textures if you need to retouch
Add collision yourself
```

## Unreal

```
Units — centimeters
Set forward axis and pivot before a batch
Static high-poly — Nanite optional
Skinned hero — do not Nanite by default
AI mesh → MetaHuman — From Custom Mesh
Movies — Media Framework / Sequencer
Do not ship uncompressed 4K on every prop
```

## Video files (any engine)

```
Trailers / title cards — movie file is fine
Gameplay loops / attacks — spritesheet or VFX, not an mp4 on a quad
```
