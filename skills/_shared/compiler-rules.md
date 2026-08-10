# Compiler Rules

How to turn intent into Suno fields. Shared by `suno-vocal-song` and `suno-instrumental`.

Facts live in `suno-reference.md`. This file is rules — when a rule and a fact disagree, the fact wins and the rule is wrong.

---

## 1. Two classification axes

Every ambiguity about "where does this belong" is answered by one of these. They are orthogonal, so nothing falls between them.

**Axis 1 — "Does a human make this sound?"** → splits Lyrics from Styles.
`(ooh, ooh)` is a sound a human makes → Lyrics. `melismatic` is a *way* of making sound → Styles.

**Axis 2 — "Is there text to be sung?"** → splits the two skills.
Text to sing → `suno-vocal-song`. No text to sing → `suno-instrumental`. Structure tags are not text to be sung, so an instrumental using `[Build-Up]` does not cross the boundary.

**Three fields, three responsibilities:**

| Field | Owns |
|---|---|
| Lyrics | What is actually performed, plus the minimum cues |
| Styles | The music you want |
| Exclude Styles | The music you don't want |

Production notes, playing technique, and mixing direction never appear in Lyrics.

## 2. The slot compiler

Styles is assembled from fixed slots in fixed order. **Never free-write the Styles string** — order is weight (`suno-reference.md` §3), and free-writing gambles the most valuable position in the prompt.

| # | Slot | Vocal | Instrumental |
|---|---|---|---|
| 1 | genre + subgenre / era | required | required |
| 2 | mood + energy | required | required |
| 3 | instrumentation (2–4 instruments) | required | required |
| 4 | vocal identity + delivery + `singing in <language>` | required | absent |
| 5 | rhythm / groove | optional | optional |
| 6 | production character | optional | optional |
| 7 | BPM | optional, always last | optional, always last |

### Starting values

`genre-presets.md` holds opening slot values for 44 genres. Load the nearest one, then replace whatever the concept determines — a preset that survives untouched means the concept was never resolved. The redundancy pass still runs afterwards: preset descriptors meeting concept descriptors is exactly how a synonym-pile forms.

Presets are a shortcut through slot *assembly*, never a shortcut around it. A preset string is not an output string.

### Choosing the BPM

Slot 7 is a number, and a number picked from nothing is worse than no number at all. Take the opening value from `bpm-by-use-case.md` — indexed by what the track is *for*, which is what the user actually told you — then let the genre preset and the concept move it.

When the perceived tempo differs from the stated one, put the feel in slot 5 and leave slot 7 honest: `half-time feel, 140 BPM`. Do not average the two into a number that describes neither.

### Budget

- **≤ 350 characters.**
- **~10 descriptors as a reference line, not a cap.**
- **Zero synonyms.** This is the real constraint. Before emitting, scan the assembled string: if two descriptors point at the same idea, collapse them into the stronger one.
- One concept → one strong descriptor.

### Instrumentation discipline

Slot 3 takes **2–4 named instruments**, ordered lead → supporting. More than four and the individual instruments stop registering; the model averages them into a generic band. If the concept seems to need five, the fifth is almost always decoration — cut it, or move its character into slot 6 as production texture.

### Never

- Do not put `no X` in Styles when the Exclude field is available (see §4).
- Do not restate a Styles descriptor in prose elsewhere in the output. It is already said.
- Do not emit BPM as a separate output field. It is slot 7, inside Styles.

## 3. Version dialect rendering

Same slots, different surface. Read the target version from the profile.

**v4.5** — descriptive, connective words permitted:
```
warm 70s soft rock with a folk edge, wistful and unhurried, fingerpicked acoustic
guitar with brushed drums and upright bass, breathy male tenor singing in English,
loose behind-the-beat feel, warm analog tape, 88 BPM
```

**v5 / v5.5** — compressed, comma-separated, no filler:
```
70s soft rock, folk edge, wistful, fingerpicked acoustic, brushed drums, upright bass,
breathy male tenor, singing in English, behind-the-beat, analog tape warmth, 88 BPM
```

v5.5 permits finer descriptors than v5 (`slightly detuned vintage keys`) because it tracks nuance better — but the same non-redundancy rule applies.

## 4. Exclude Styles

Read `plan` from the profile and branch:

- **Pro / Premier** → dedicated field, plain noun phrases, no `no`.
- **Otherwise** → append `no [element]` to the end of Styles, and count it against the 350-char budget.

**Fill priority**, capped at 4 items:

1. What the user explicitly said they don't want
2. What Suno habitually contaminates this genre with
3. What directly contradicts the concept

Priority 1 always outranks 2 and 3. The skill's guess never displaces the user's stated wish.

**Every exclusion must be paired with a positive replacement in Styles.** Excluding `electric guitar` without putting `upright bass, brushed drums` in slot 3 leaves a hole the model fills from habit. Exclusion is probabilistic; replacement is what actually moves the result.

**Leave it empty when there is nothing to exclude.** Filler exclusions dilute the real ones.

## 5. Slider mapping

Two independent properties of the concept drive two sliders. Do not couple them to a single axis — "a clearly defined city pop track with an unconventional structure" is a real and common combination.

| Concept property | Slider | Value |
|---|---|---|
| Single clear genre | Style Influence | 70–85 |
| Genre blend | Style Influence | 40–60 |
| Conventional, chorus-driven | Weirdness | 20–40 |
| Texture / ambient / experimental | Weirdness | 50–65 |

**Never auto-recommend Weirdness ≥ 0.7.** Song form breaks down past that point. Emit it only on explicit request, with the consequence stated.

**Coupling rule:** when raising Weirdness, raise Style Influence with it. Experimentation needs a genre fence or it produces something that is merely strange and stylistically shapeless.

## 6. Guardrails

### 6.1 Artist and track references

Artist names are blocked by Suno and risk account strikes (`suno-reference.md` §9). When the user names an artist or track:

1. **Never let the name reach any output field.** No exceptions.
2. Decompose into five components: **era / genre + subgenre / texture / instrumentation / vocal character.** Feed them into the slots.
3. **Show the translation in one line of Layer 2**, e.g. `"Radiohead" → 90s alternative, dissonant guitar texture, falsetto male vocal`. Without this line the user cannot tell a good generalization from a bad one until after generating.
4. **Never reproduce existing lyrics.** A reference applies to sound only; lyrics are always original.
5. Generalizing a song's *section layout* is fine. Attempting to reproduce its melody or hook is not.

### 6.2 Conflict detection

Before compiling, check the requirements against each other. `minimal arrangement` + `five guitars` + `full orchestra` cannot all be satisfied.

When requirements conflict: **do not silently pick one.** State the conflict in one sentence, ask which one matters most, and wait. This is the one case where the no-friction flow yields — compiling a self-contradicting prompt wastes a generation and teaches the user nothing.

### 6.3 Bloat

The enemy is repetition, not length. Before emitting Styles, run one pass: for each descriptor, ask *what does this add that nothing else here already says?* If the answer is nothing, delete it. Do not delete a specific instrument, vocal, or production detail merely to hit a number.

## 7. Revision rules

The user's revision request changes the slot it names. The question is only how far the change is allowed to spread.

**Test: does leaving it produce a contradiction?**

- **Contradiction → fix it automatically, and report in one line.**
  Changing Voice Gender to female while slot 4 still reads `male baritone` sends Suno two fighting signals. Fix both.
- **No contradiction → do not touch it. Raise it under `⚠️` as a suggestion.**
  Dropping BPM to 105 might pair well with a looser groove, but the current groove still works. Suggest, don't apply.

The test is deliberately "is it contradictory," **not** "would it be better." *Better* is unbounded and turns every revision into a redesign — exactly what these skills must not do.

**Additional constraints:**

- **Cascade depth 1.** A required fix does not trigger further fixes. Two levels deep is a redesign.
- **Lyrics are a text block, not a slot.** `cut the lyrics by 30%` touches Lyrics only. Styles is not re-derived.
- **Append to `revision_history` on every change**, as `request → slots changed`. This is what makes `revert to the previous version` possible.
- Everything not named in the request is preserved **verbatim**, not regenerated.

## 8. State

### Paths

| What | Where |
|---|---|
| Profile | `~/.claude/suno/profile.md` |
| Songs | `~/.claude/suno/songs/<slug>.md` |

Both are overridable via `paths` in the profile. **Never write state inside the plugin directory** — it is a versioned cache and is replaced on update.

On first run, if the profile does not exist, create it from `profile.template.md`, ask for the two values that cannot be inferred (**Suno plan** and **default lyric language**), and save.

### Song file schema

```yaml
---
slug: cold-summer-city
title: Cold Summer City
skill: suno-vocal-song
version: v5.5
created: 2026-08-07
---

## concept
One or two sentences of intent.

## outcome            # what came back from Suno — see §10
- 2026-08-10 — 4 takes, every one added a choir on the last chorus
  → choir, backing vocals added to exclude; layered synth pad added to slot 3

## slots
genre: ...
mood: ...
instrumentation: ...
vocal: ...          # vocal skill only
rhythm: ...
production: ...
bpm: ...

## lyrics            # vocal skill only
...

## compiled
styles: ...
exclude_styles: ...
voice_gender: ...    # vocal skill only
instrumental: ...    # instrumental skill only
weirdness: ...
style_influence: ...

## uncertain
- ...

## revision_history
- 2026-08-07 — "make it female vocal" → voice_gender, slots.vocal
```

Load this file to resume a song. Everything needed for a partial recompile is in it.

## 9. Output shape

Two layers. Layer 1 is for pasting, Layer 2 is for reading. Nothing else.

**Layer 1 — paste block**, in Suno's own field order, each field on its own labeled block so it can be copied without editing.

**Layer 2 — at most 5 lines:**
- Concept summary, 1–2 sentences (lets the user confirm intent survived)
- `⚠️` 2–3 decisions the skill was least confident about
- Reference translation line, if an artist or track was named

**Everything else goes in the song file, not on screen.** Rationale, instrument reasoning, arrangement intent are all recorded — they are simply not printed. Printing them buries the six fields the user actually needs to copy.

Do not print: BPM as its own field, vocal direction prose, arrangement explanation prose, a list of title candidates beyond one line.

## 10. Outcome and diagnosis

Everything above this section compiles intent into a prompt. Nothing above it can tell whether the prompt worked — that information exists only in the user's ears, and it arrives as an offhand sentence: *"보컬이 계속 남자로 나와"*, *"너무 산만해"*, *"괜찮은데 후렴이 안 살아"*.

**Record it before acting on it.** A sentence like that is the only evidence this system ever gets, and without the `outcome` log the song file is a record of intentions that were never checked.

### 10.1 Recording

When the user reports back on a generation, append one line to `outcome` in the song file: **what was asked for → what came back → what changed in response.** Then handle the report as an ordinary revision under §7 — the contradiction test still applies, and "it came out wrong" does not license a redesign any more than "make it female vocal" does.

Record the report even when nothing changes. "Three takes, all fine" is the only kind of evidence that a rule is working, and it is the kind that never gets written down.

### 10.2 Diagnosis

Symptom to cause to slot. Prompt-side only — everything here is something the compiler can act on.

| Symptom | Likely cause | Fix |
|---|---|---|
| Drifted to English, or mixed languages | `singing in <language>` missing or buried | Slot 4, exactly as written (`suno-reference.md` §8) |
| Vocal gender came out wrong | Voice Gender selector and slot 4 disagree | Both, together — one is a selector and beats prose (§7) |
| Unrequested choir or group vocals | Suno's most common unprompted addition | Exclude **and** put something in slot 3 to carry the weight (§4) |
| An exclusion was ignored | Exclusion is probabilistic, and the prompt still implies the element | Find what implies it in slots 1–3 and change that instead |
| Genre came out vague — "a bit jazzy" not "jazz noir" | Genre not in position 1, or Style Influence too low | Slot 1 first; Style Influence 70–85 (§5) |
| Strange but shapeless | Weirdness raised without a genre fence | Raise Style Influence with it (§5 coupling rule) |
| Individual instruments not audible | More than four in slot 3; Suno averaged them | Cut to 2–4, fold the rest into slot 6 as texture |
| Song rushed or cut off | Lyrics past ~3,000 characters — truncation is silent | Cut lyrics, not Styles (`suno-reference.md` §2) |
| Sections ignored | Bare `[Intro]`, or a section without a tag | Specific forms, tag every section (§5.1) |
| Descriptors seem ignored | Synonym pile — the model had nothing new to act on | Redundancy pass, collapse to the stronger term (§2) |
| Track came out longer or shorter than wanted | Section count, not word count, is the lever | Add or cut a section |

Two failures are **not** in this table because they are not the prompt's fault: audio artifacts and a buried vocal in an otherwise correct take. Those are mix problems, and the fix is Suno-side — regenerate, or use Remaster and stems. Say so and stop; do not recompile a prompt that was right.

### 10.3 When a correction repeats

The same correction landing in three different songs is not three revisions — it is a preference that was never written down.

When it happens, say so in one line and offer to move it into the profile: a habitual exclusion belongs in `Always exclude`, a habitual instrument in `Instruments you gravitate toward`. **Offer, do not write.** The profile is the user's file, and a skill that edits it silently makes every future output harder to explain.

This is the only path by which the profile's taste section ever fills in. Left alone it stays blank, and a blank taste section means the profile is doing nothing but holding a version number and a language.
