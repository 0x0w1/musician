---
name: suno-vocal-song
description: Turn a one-line idea into a complete, paste-ready Suno song with lyrics. Use when the user wants to make a song, write lyrics, or produce vocal music with Suno — including revisions to a song made earlier ("make it female vocal", "cut the chorus", "BPM 105"). For music with no sung text, use suno-instrumental instead.
---

# Suno Vocal Song

Take a short idea and return a Suno prompt set that can be pasted without editing. Then keep it revisable.

**Read first, every time:**
- `../_shared/suno-reference.md` — what Suno is
- `../_shared/compiler-rules.md` — how to compile
- `references/lyrics-and-vocals.md` — lyrics and vocal design
- The profile at `~/.claude/suno/profile.md` (create from `../_shared/profile.template.md` if missing)

**Look up when the step calls for it, not up front:**
- `../_shared/genre-presets.md` — opening slot values by genre (step 4)
- `../_shared/bpm-by-use-case.md` — opening BPM by what the track is for (step 4, slot 7)

## Boundary

This skill handles songs **with text to be sung**. If the request has no sung text — background music, a focus track, ambient — say so and point to `suno-instrumental`. **Do not redesign the request to fit this skill.** Two skills that quietly do each other's work have no boundary.

## Workflow

There are no modes. One path: produce a finished result, mark what you were unsure of, refine through conversation.

### 1. Resolve intent

From the user's line, infer: emotion, story or message, speaker's perspective, emotional movement across the song, genre, mood. Infer rather than ask — the user gave you a sentence, not a form.

If an artist or track is named, decompose it per `compiler-rules.md` §6.1 **before anything else**, and never carry the name forward.

Ask only when requirements genuinely conflict (`compiler-rules.md` §6.2). Everything else you are unsure about becomes a `⚠️` line, not a question.

### 2. Set language

Profile default, unless the genre implies otherwise — J-Pop implies Japanese regardless of the default. Native script. `singing in <language>` goes into slot 4; without it Suno drifts.

### 3. Write lyrics

Per `references/lyrics-and-vocals.md`. Structure tags on every section, delivery tags only at emotional turns, no production direction anywhere in the box.

### 4. Fill slots and compile

Seven slots in order (`compiler-rules.md` §2), rendered in the profile's version dialect (§3). Then run the redundancy pass: any two descriptors saying the same thing collapse into one.

### 5. Voice Gender

Choose it — it is a selector value, not prose, and it controls gender more reliably than any Styles wording. If the concept genuinely doesn't determine it, pick the better fit and put it in `⚠️`.

### 6. Exclude Styles

Per `compiler-rules.md` §4. Branch on the profile's `plan`. Pair every exclusion with a positive replacement.

### 7. Sliders

Per `compiler-rules.md` §5. Two axes, independently.

### 8. Title

One title. Two alternates on the same line. Not a list.

### 9. Save and output

Write the song file to `~/.claude/suno/songs/<slug>.md` using the schema in `compiler-rules.md` §8, then print the two layers below.

## Output

**Layer 1 — paste block**

```
Title
  <title>

Lyrics
  <lyrics with structure tags>
  <English translation beneath, if non-English and translate_non_english is on>

Styles
  <compiled styles string>

Exclude Styles
  <2-4 noun phrases, or empty>

Voice Gender
  male | female

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

Alternate titles go on the concept line. Nothing else is printed — rationale lives in the song file.

## Revisions

Load the song file. Change the slot named. Apply the contradiction test from `compiler-rules.md` §7: fix what would otherwise contradict and say so in one line; suggest the rest under `⚠️`. Preserve every untouched decision **verbatim**. Append to `revision_history`.

`cut the lyrics by 30%` touches Lyrics only — do not re-derive Styles.

## When the user reports back

A generation result arrives as a sentence — `보컬이 계속 남자로 나와`, `너무 산만해`. Handle it in this order (`compiler-rules.md` §10):

1. **Append it to `outcome`** in the song file, before changing anything. Record it even when nothing needs to change.
2. **Diagnose** against §10.2 — symptom to cause to slot.
3. **Revise** under the ordinary §7 contradiction test. "It came out wrong" is not a licence to redesign.

If the problem is a mix problem — artifacts, a buried vocal in an otherwise correct take — say so and stop. That is Suno-side, and recompiling a prompt that was already right makes the next take worse, not better.

When the same correction has now landed in three songs, offer to move it into the profile. Offer only.

## Do not

- Put playing technique, mixing, or production direction in the Lyrics box
- Emit an artist or track name in any field
- Reproduce existing lyrics
- Print BPM as a separate field, or restate Styles content as prose
- Auto-recommend Weirdness ≥ 0.7
- Regenerate the whole song in response to a targeted revision
- Recompile a prompt when the report describes a mix problem
- Edit the profile without being asked
