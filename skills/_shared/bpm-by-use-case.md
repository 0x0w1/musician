# BPM by Use Case

Starting values for **slot 7**. Heuristics, not facts — this file holds *how to choose a number*, so it lives with the rules, not in `suno-reference.md`.

**Status: `[unverified]`.** Adapted from a third-party guide that carries no citations (see `suno-reference.md` Sources). The ranges are plausible and internally consistent, and nothing here has been checked against generated audio. Treat every number as an opening bid the concept is allowed to overrule.

---

## 1. The number is not the tempo

Perceived tempo and stated BPM diverge, and when they do, **the perception is what the listener gets**. A half-time feel at 140 BPM reads slow. A double-time hi-hat over 75 BPM reads fast.

So slot 7 is a floor, not a decision. When the feel differs from the number, say the feel in slot 5 and let slot 7 stay honest:

```
..., half-time feel, 140 BPM
..., double-time hats, 75 BPM
```

Rhythmic density belongs in slot 5 for the same reason. Two tracks at 90 BPM, one sparse and one busy, are not the same tempo to anyone listening.

## 2. Work and focus

| Context | BPM | Note |
|---|---|---|
| Deep focus | 60–80 | Minimal, ambient, no lyrics |
| Coding / technical | 70–90 | Ambient or instrumental electronic |
| Light work | 80–100 | Lo-fi, jazz, gentle electronic |
| Creative / brainstorming | 100–120 | Upbeat without pulling attention |
| Repetitive tasks | 110–130 | Steady, can carry more energy |

Repeat-listening constraint applies on top of this table — see `../suno-instrumental/references/instrumentation-and-performance.md` §4. A focus track that peaks fails at its job every time the peak comes around, whatever its BPM.

## 3. Movement and exercise

| Activity | BPM | Note |
|---|---|---|
| Meditation | 50–70 | Drones, evolving pads, no percussion |
| Yoga / stretching | 60–90 | Gentle, natural textures |
| Cool-down | 65–90 | Progressive decrease |
| Warm-up | 100–120 | Progressive build |
| Walking | 115–125 | Steady, syncs to footfall |
| Running — endurance | 120–140 | Matched to stride cadence |
| Weightlifting | 130–150 | Sustained, not rushed |
| Boxing / martial arts | 130–150 | Steady enough for combination work |
| Cycling / spinning | 130–170 | Varies by phase |
| Dance / Zumba | 130–170 | Latin rhythms, energetic pop |
| Running — tempo | 140–160 | Speed sessions |
| Tabata | 140–150 | 20s effort / 10s rest |
| CrossFit | 130–160 | Varies by workout |
| HIIT | 150–170 | Alternates with 115–120 recovery |
| Sprint / intervals | 160–180 | Maximum intensity |

## 4. Rooms and events

| Context | BPM | Note |
|---|---|---|
| Spa / wellness | 50–70 | Ultra-relaxed |
| Art gallery | 60–80 | Ambient, atmospheric |
| Dinner ambience | 70–95 | Soft, unobtrusive |
| Cocktail reception | 90–110 | Jazz, lounge |
| Retail floor | 100–120 | Pleasant, encourages movement |
| Corporate event | 100–120 | Professional, uplifting |
| Product launch | 110–130 | Energetic, modern |
| Fashion show | 115–130 | Rhythmic, stylish |

## 5. Screen and media

| Context | BPM | Note |
|---|---|---|
| Film — romance | 60–80 | Tender |
| Video game — menu | 80–100 | Atmospheric, loopable |
| Film — tension | 80–110 | Building, suspenseful |
| Podcast intro | 100–120 | Short, memorable |
| Advertisement | 110–130 | Energetic, memorable |
| YouTube intro | 110–140 | Catchy, dynamic |
| Film — action | 120–150 | Dynamic, powerful |
| Video game — action | 130–160 | Intense, driving |

## 6. What is deliberately not here

**There is no BPM-to-emotion table.** The source had one — `peaceful 50–70`, `aggressive 140–180` — and it was dropped rather than adapted.

Tempo does not carry emotion independently of genre. A 60 BPM half-time trap beat is not peaceful; a 140 BPM shoegaze wash is not aggressive. Mood is slot 2's job and instrumentation is slot 3's, and both outrank the number. A table that suggests otherwise would push the compiler toward picking a tempo from a feeling, which is backwards: **the use case and the genre pick the tempo, and the mood is stated separately.**

When no use case is given and the concept is purely emotional, take the BPM from the genre preset (`genre-presets.md`) and adjust from there.

## 7. Parked — playlist energy curves

Both skills currently produce **one track at a time**, so these are unused. Kept because they are the part of the source that is hardest to reconstruct, and they become directly usable the day a playlist or album mode exists.

```
Workout, 30 min
  warm-up 5m 110-120 → build 3m 130-140 → peak 8m 150-160
  → active recovery 2m 120 → peak 8m 155-165 → cool-down 4m 90-100 → 70

Running, 45 min
  warm-up 5m 110-120 → cruise 15m 130-140 → intervals 15m alternating 150/120
  → return 5m 130 → cool-down 5m 100 → 80

Focus, 2 h
  30m 70-80 lo-fi → 30m 60-70 ambient → 30m 110-115 minimal techno
  → 30m 75-85 jazz lo-fi

Event, 3 h
  arrival 90-100 → main 100-115 → peak 115-125
```
