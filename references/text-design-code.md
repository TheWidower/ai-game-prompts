# Text prompts — design, systems, vibe-coding

These prompts are for chat models and AI-native game builders, not image models.

## Master rule

Smallest testable request. One scene or one object or one behavior. State the outcome, not the API.

Pattern
```
In [current scene / this project], [do concrete thing named X]. [One property or rule]. I will know it worked when [observable].
```

Bad — "make a fun combat system"
Good — "In the current scene, player deals 3 damage on left click to the nearest enemy in a 1.5m cone. Take a screenshot after a hit."

## Game idea (one sentence)

Name genre + one twist + player goal.

```
A [camera] [genre] where the player [core verb] using [one mechanic], and wins/loses when [condition]. Tone is [3 words]. Original world, no existing IP.
```

Then optionally expand into a one-page GDD prompt.

## One-page GDD

Ask for sections, cap length, forbid scope creep.

```
Write a one-page GDD for [idea sentence].
Sections — premise, player fantasy, camera and controls, core loop (30 seconds), 3 verbs, 1 resource, fail state, 6 content beats, art direction (5 bullets), out of scope.
Constraints — solo-dev shippable in [N] weeks, [platform], no multiplayer, no live-ops.
Do not invent extra modes.
```

## Mechanic / feel

One verb. Include the feedback the player sees and hears.

```
Design the [verb] for a [genre].
Input, response, cooldown or cost, readable telegraph, success feedback, fail feedback, how it upgrades once.
Keep it implementable in [engine or language].
```

Tuning knobs to name when relevant — TTK, i-frames, coyote time, input buffer, camera lag, enemy read time.

## Level / encounter

```
Block out [level name] for [camera] [genre].
Player enters knowing [X], learns [Y] without text, is tested on [Y] plus [old verb], exits with [reward].
Call out 1 landmark, 1 optional secret, 1 teaching room, 1 pressure room.
No new verbs.
```

## Narrative / dialogue

```
Write [N] lines of barks for [NPC lock] in [situation].
Voice — [3 traits].
Each line must be speakable in under 2 seconds.
No lore dumps. No franchise tone-cloning.
Tag each line with state (idle, spotted, hurt, death).
```

Quest prompt — goal, constraint, moral fork optional, 3 beat rooms, no fetch-for-its-own-sake.

## Vibe-coding / AI-native engine

Write many small prompts. After each, the user plays.

Order
1. Core loop sentence
2. Player controller (one verb)
3. Fail / win condition
4. One enemy or obstacle
5. Camera and feel
6. Juice (hit stop, particles, screenshake — one at a time)
7. UI that is part of the game, not a website
8. Then assets

Example first prompt
```
Make a [camera] [genre]. Player [moves how]. Press [button] to [verb] only when grounded. Falling off the bottom resets. Show a score that goes up when [action].
```

Bug-fix pattern (best follow-up shape)
```
I did [input] and [wrong thing] happened. It should [correct rule] because [reason]. Do not rewrite unrelated systems.
```

## Code-adjacent (Unity / Godot / Unreal chat)

- Name the object and the component
- One script per prompt
- Ask for comments only on non-obvious choices
- Demand the happy path plus one fail path
- "Do not replace existing input code; extend it"

```
Add a C# component DoubleJump to the existing Player body. Second jump only in air, once, resets on IsGrounded. Do not change walk speed. Include a serialized jumpForce2.
```

## From a reference video or screenshot

```
Match the feel of this clip without copying IP.
Observable rules I want — [list 3 verbs you extracted].
Implement only [verb 1] first.
Art can stay placeholder.
```

## Quality gate

1. Can this be verified in 30 seconds of play or one screenshot?
2. Did we add a system the user did not ask for?
3. Is the camera named?
4. Is the fail state named?
5. Could a teammate paste this without extra lore?
