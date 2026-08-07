# Instrumentation, Performance, and Arrangement

Detail for `suno-instrumental`. Tag inventories live in `../../_shared/suno-reference.md` §5.

---

## 1. Instrumentation hierarchy

Slot 3 takes **2–4 instruments in role order**:

1. **Lead** — carries the motif. Always named.
2. **Supporting** — harmony or counter-line. Usually one.
3. **Bass** — name it when its character matters (`upright bass` vs `sub bass` are different tracks).
4. **Percussion** — name it when rhythm is part of the identity. Ambient often omits it entirely.

Beyond four, individual instruments stop registering and Suno averages them into a generic ensemble. A fifth instrument is almost always decoration — cut it, or fold its quality into slot 6 as production texture.

Texture layers (pads, drones, field recordings) count toward the four. `warm analog pad` is an instrument, not a free modifier.

## 2. Playing technique

Naming an instrument gives you the timbre. Naming the technique gives you the *gesture* — and the gesture is often what the user actually described.

```
fingerstyle      bending        long sustained notes    staccato
arpeggio         muted          syncopation             legato
tremolo          harmonics      volume swell            palm-muted
```

**Apply technique only where it is load-bearing.** `fingerpicked acoustic guitar` earns its word because picking style defines the sound. `syncopated shaker` usually does not — it spends budget on something the listener won't isolate.

Rule of thumb: technique on the lead instrument is usually worth it; technique on the third or fourth instrument almost never is.

## 3. Arrangement

With no words to carry time, the arrangement *is* the composition. Express it as structure tags in the Lyrics box — this works with `Instrumental: ON`.

**4–6 sections.** The full vocabulary is larger than what any one track needs:

```
[Short Instrumental Intro]   [Build-Up]    [Main Theme]     [Variation]
[Interlude]                  [Breakdown]   [Drop]           [Climax]
[Outro]                      [Fade Out]
```

A common shape:

```
[Short Instrumental Intro 4]
[Main Theme]
[Variation]
[Breakdown]
[Climax]
[Outro 4]
```

**Bar counts only where length matters** — intro and outro. Numbering every section is the "excessive timestamp instruction" failure: it reads as precision but Suno treats the numbers as approximate targets, so the extra specificity buys nothing and crowds the box.

**Motif discipline:** one main motif, introduced early, varied at least once. Two competing motifs in a 3-minute instrumental read as two unfinished tracks.

## 4. Dynamics

Choose one dynamic shape and let the section list express it. Stating both the shape and the sections is redundant.

| Shape | Section pattern |
|---|---|
| Restrained, no climax | Theme → Variation → Interlude → Outro |
| Slow build, single climax | Intro → Build-Up → Theme → Climax → Outro |
| Dynamic contrast | Theme → Breakdown → Climax → Breakdown → Outro |
| Steady energy | Theme → Variation → Variation → Fade Out |

**Repeat listening favors no climax.** Music for focus or background that peaks will pull attention every time it comes around — that is a failure for the stated purpose, even though it is a better standalone listen. Let the use case decide, not the drama.

Endings: `[Fade Out]` for background use, `[Outro]` for a defined close, an abrupt end only when it is the point.

## 5. Production character

Slot 6. **One or two terms**, only when they change what you'd hear.

```
dry / spacious        analog / digital       lo-fi / clean
warm / cold           close / ambient        mono / wide
reverb    delay    saturation
```

Test before including: *would removing this word change the track?* If not, it is bloat. `warm analog tape` earns its place on a lo-fi piece; `professional mixing` earns nothing anywhere.

## 6. Common exclusions

Frequent priority-2 entries for instrumentals — Suno adds these unprompted:

```
vocals    spoken word    choir    backing vocals
aggressive drums    EDM drops    orchestral strings
heavy distortion    busy arrangement
```

Group vocals are the single most common unrequested addition. On any calm or minimal instrumental, `choir, backing vocals` is close to a default priority-2 exclusion.

Remember the pairing rule: excluding `orchestral strings` from a piece that wants scale means putting something else in slot 3 to carry it — `warm analog pad`, `layered electric piano`. An exclusion without a replacement leaves a hole the model fills from habit.
