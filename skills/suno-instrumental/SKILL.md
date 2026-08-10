---
name: suno-instrumental
description: Turn a one-line scene or use case into a paste-ready Suno instrumental with no lyrics. Use when the user wants background music, focus/study music, ambient, BGM, or any track described by mood and setting rather than words — including revisions to one made earlier. For songs with sung lyrics, use suno-vocal-song instead.
---

# Suno Instrumental

Take a scene, a use case, or a feeling and return a Suno prompt set for a track with no sung text. Then keep it revisable.

**Read first, every time:**
- `../_shared/suno-reference.md` — what Suno is
- `../_shared/compiler-rules.md` — how to compile
- `references/instrumentation-and-performance.md` — instrumentation, technique, arrangement
- The profile at `~/.claude/suno/profile.md` (create from `../_shared/profile.template.md` if missing)

**Look up when the step calls for it, not up front:**
- `../_shared/genre-presets.md` — opening slot values by genre (step 2)
- `../_shared/bpm-by-use-case.md` — opening BPM by what the track is for (step 3)

## Boundary

This skill handles music with **no text to be sung**. If the user wants lyrics, say so and point to `suno-vocal-song` — do not write a song here.

Wordless human voice as *texture* (humming, ooh-ahh pads, choir beds) stays in this skill: it is voice, but it is not text to be sung. See "Voice texture mode" below.

## Workflow

No modes. Produce a finished result, mark what you were unsure of, refine through conversation.

### 1. Resolve intent

From the user's line, infer: purpose, scene, emotion, environment, energy, time of day, sense of motion, and whether it is meant for repeat listening. A track for background focus and a track for a single attentive listen are different tracks — repeat-listening pushes toward steadier dynamics and away from a big climax.

If an artist or track is named, decompose it per `compiler-rules.md` §6.1 first, and never carry the name forward.

### 2. Genre

One dominant genre. **Blend at most two**, and make the dominance explicit — `ambient techno with a post-rock lean`, not `ambient techno post-rock jazz`. Three or more genres average into something characterless, and the genre slot is the most heavily weighted position in the whole prompt.

### 3. Tempo and groove

BPM, plus perceived tempo when it differs — a half-time feel at 140 BPM reads slow, and saying so matters more than the number. Rhythmic density belongs here too.

### 4. Instrumentation

2–4 named instruments, lead → supporting (`compiler-rules.md` §2). Add playing technique **only where it is musically load-bearing** — `fingerstyle`, `volume swell`, `muted`, `arpeggio`. Technique on a supporting instrument is usually decoration; cut it. See `references/instrumentation-and-performance.md`.

### 5. Arrangement

Instrumentals have no words to carry time, so the time axis is the main design surface. Express it with **structure tags in the Lyrics box** — this works with `Instrumental: ON`.

- **4–6 sections.** Not eight. Choose the ones this track actually needs.
- **Bar counts only where length genuinely matters** — usually intro and outro. Do not number every section.
- Dynamics — restrained, slow build, single climax, no climax, steady, fade out, abrupt end — go in slot 6 or the section choice, not in a separate instruction.

### 6. Production

Only when it changes the result. `dry / spacious`, `analog / digital`, `lo-fi / clean`, `warm / cold`, `close / ambient`. One or two terms. Production vocabulary that doesn't alter what you'd hear is bloat.

### 7. Exclude Styles and sliders

Per `compiler-rules.md` §4 and §5. For instrumentals, `vocals`, `spoken word`, and `choir` are frequent priority-2 exclusions — Suno adds group vocals unprompted more than anything else.

### 8. Save and output

Write to `~/.claude/suno/songs/<slug>.md` (`compiler-rules.md` §8), then print the two layers.

## Voice texture mode

Only when the user explicitly asks for humming, ooh-ahh pads, or a choir bed:

- `Instrumental: OFF`
- Wordless voice goes in **slot 3** as an instrument — `wordless female humming`, `ooh-ahh choir pad`
- Structure tags stay in the Lyrics box, still with no sung text
- Put `sung lyrics, spoken word` in Exclude Styles as a safety belt — the path is confirmed working, but Exclude is probabilistic and these two cost nothing

Never enter this mode by inference. Default is `Instrumental: ON` with no voice at all.

## Output

**Layer 1 — paste block**

```
Title
  <title>

Lyrics
  <structure tags only, no sung text>

Styles
  <compiled styles string>

Exclude Styles
  <2-4 noun phrases, or empty>

Instrumental
  ON | OFF

Weirdness / Style Influence
  <n> / <n>
```

**Layer 2 — max 5 lines**

```
<1-2 sentence concept summary>
<reference translation line, only if an artist or track was named>
⚠️ <decision you were least sure about>
⚠️ <second one>
```

## Revisions

Load the song file, change the named slot, apply the contradiction test (`compiler-rules.md` §7). Fix only what would otherwise contradict; suggest the rest under `⚠️`. Preserve untouched decisions verbatim. Append to `revision_history`.

## When the user reports back

A generation result arrives as a sentence — `합창이 자꾸 껴`, `집중이 안 돼`. Handle it in this order (`compiler-rules.md` §10):

1. **Append it to `outcome`** in the song file, before changing anything. Record it even when nothing needs to change.
2. **Diagnose** against §10.2 — symptom to cause to slot.
3. **Revise** under the ordinary §7 contradiction test.

`집중이 안 돼` on a focus track is a dynamics failure, not a genre failure: the track probably has a climax it should not have (`references/instrumentation-and-performance.md` §4). Check the section list before touching slot 1.

If the problem is a mix problem, say so and stop — that is Suno-side.

When the same correction has now landed in three songs, offer to move it into the profile. Offer only.

## Do not

- Write lyrics, or accept a lyrics request — hand it to `suno-vocal-song`
- Enter voice texture mode without an explicit request
- Blend three or more genres
- Number every section with bar counts
- Emit an artist or track name in any field
- Auto-recommend Weirdness ≥ 0.7
- Recompile a prompt when the report describes a mix problem
- Edit the profile without being asked
