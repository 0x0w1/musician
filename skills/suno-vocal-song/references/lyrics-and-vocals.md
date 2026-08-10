# Lyrics and Vocal Design

Detail for `suno-vocal-song`. Tag inventories live in `../../_shared/suno-reference.md` §5.

---

## 1. Length

| | Target |
|---|---|
| A 3–4 minute song | 200–300 words, 30–40 lines |
| Hard ceiling | ~3,000 characters — past this Suno rushes or truncates |
| Field limit | 5,000 characters (not a target) |

Line length follows the language. Korean and Japanese carry less information per syllable than English, so a line that fits a melody in English runs short in translation — write to the *melodic* line, not the word count.

### Syllables per line `[unverified]`

Write to the melodic line, then check it against a number. Too many syllables and Suno crowds them into the bar; too few and it stretches vowels to fill.

| Language | Syllables per line | Basis |
|---|---|---|
| English | 6–12 | Third-party guide, uncited |
| Korean | 8–15 | Inferred, not measured |
| Japanese | 10–18 (mora) | Inferred, not measured |

**Only the English band has a source, and it is a weak one.** The other two are reasoned from the density difference stated above, not observed: the same melodic phrase needs more Korean syllables than English to say the same thing, and more Japanese mora again. Treat them as a sanity check on an outlier line, never as a target to write toward — a line at 20 Korean syllables is worth a second look; a line at 14 is not a problem.

The band is a **check, not a constraint.** Irregular line lengths are what make phrasing conversational (§5); a lyric where every line lands in the middle of the band reads mechanical.

### Sections and duration `[unverified]`

Section count is the main lever on length — the Lyrics box has no duration field.

| Structure | Approximate length |
|---|---|
| 2 verses + 2 choruses | 2–3 min |
| + bridge + outro | 3–4 min |
| Ceiling | 8 min per generation |

`[Instrumental]` and `[Instrumental Break]` add time without adding words, which is the tool for a song that runs short — not padding the verses. Bar counts (`[Instrumental 8]`) apply here under the §5.2 caveat: a target, not a guarantee.

## 2. Structure

Default: `Intro → Verse 1 → Chorus → Verse 2 → Chorus → Bridge → Chorus → Outro`.

Deviate when the concept asks for it. A song about circling the same thought may want no bridge; a song about a single moment may want two verses and no chorus at all.

**Rules:**

- A structure tag on **every** section. Suno's sectioning degrades without them.
- **Never bare `[Intro]`** — it is unreliable. Use `[Short Instrumental Intro]` or `[Intro - Spoken]`.
- Repetition is the chorus's job. A chorus that changes every time is a verse.
- Bar counts (`[VERSE 1 8]`) are a single-source technique — use them only when intro or outro length actually matters, never across the whole song.

## 3. Cue discipline

The Lyrics box holds **what is performed** and nothing else.

| Belongs in Lyrics | Belongs in Styles |
|---|---|
| Sung words | `melismatic`, `belting`, `gravelly` |
| `(ooh)`, `(one more time)` — ad-libs as parenthetical text | `humming` as a general tendency |
| `[Whispered]` at an emotional turn | `spacious reverb`, `auto-tuned` |
| `[Short Instrumental Intro]` | `fingerpicked acoustic`, `analog tape warmth` |
| `THIS IS OUR TIME` — one shouted phrase | `shouted` as the whole song's delivery |

**Performance notation** (`../../_shared/suno-reference.md` §5.5) is the third thing the Lyrics box holds, after the words and the tags: `UPPERCASE` for emphasis, `(parentheses)` for backing vocals, `~held~`, `cut-`. It is the only per-*word* control that exists — every bracket tag is per-section, every Styles descriptor is per-track. Spend it on the one or two words a line turns on.

It is also the easiest thing here to overdo. An all-caps chorus is a chorus with no dynamic range left to give.

**Delivery tags: 2–3 in the entire song, at most one per section.** They are the only per-section control available — Styles applies to the whole track — so spend them where the song actually turns. Stacking them causes the same attention dilution as a synonym-pile in Styles.

**Inline metatags** (`[Verse 1: raspy older female, husky contralto]`) are an escalation card, not a default. Reach for them only when a vocal identity problem survives two ordinary revisions.

## 4. Language

- Profile default, overridden by a genre that implies a language.
- **Native script.** Romanize only the specific words Suno mispronounces, with hyphens — never the whole lyric. Fully romanized Japanese collapses homophones (`kami` = 神 / 髪 / 紙).
- `singing in <language>` in slot 4 is mandatory. Suno drifts without it.
- When `translate_non_english` is on, print an English translation beneath the lyrics — it is for proofreading, not for Suno. It never goes in the paste block's Lyrics field.

## 5. Rhyme and phrasing

Rhyme is a tool, not a requirement. Dense end-rhyme reads as light or comic; sparse or slant rhyme reads as serious. Match the emotional register — a song about failure that rhymes perfectly every line undercuts itself.

Conversational singing wants short lines, plain words, and irregular line lengths. Fast phrasing wants more syllables than the beat comfortably holds. Sparse lyrics want fewer lines and more instrumental space — express the space with `[Interlude]`, not by leaving the box empty.

## 6. Vocal design

**Voice Gender is a selector, not prose.** Pick it. It controls gender more reliably than any wording in Styles. Still describe the voice in slot 4 — the selector sets gender, the text sets character.

Slot 4 assembles as: **range/identity + texture + delivery + `singing in <language>`**

```
breathy female alto, intimate delivery, singing in Korean
warm male tenor, belting on the chorus, singing in Japanese
```

Two to three vocal descriptors. `intimate` and `breathy` and `whispery` are one idea, not three.

**Harmony and backing vocals:** Suno adds group vocals unprompted more than any other element. If the track should stay a single voice, put `backing vocals, choir` in Exclude Styles — do not assume a lean prompt is enough.

**Shouting, screaming, belting:** these read as delivery, so they go in slot 4 for a whole-song character, or as a `[Shout]` delivery tag for a single section. Not both.
