# Suno Reference — Facts

What Suno actually is: fields, limits, tag taxonomy, vocabulary. **Facts only.** How to use them lives in `compiler-rules.md`.

Every claim carries a verification status. Never promote a claim to a default without checking its tag.

| Tag | Meaning |
|---|---|
| `[verified]` | Multiple independent sources agree |
| `[user-confirmed]` | Confirmed by the repo owner on 2026-08-07, not independently verified |
| `[unverified]` | Single source or inference — document it, do not build defaults on it |

---

## 1. Input fields

Supported versions: **v4.5, v5, v5.5**. Default **v5.5**.

| Field | Type | v4.5 | v5 | v5.5 | Notes |
|---|---|---|---|---|---|
| Lyrics | textarea | ✓ | ✓ | ✓ | Disabled by the Instrumental toggle for sung content, but still accepts structure tags `[user-confirmed]` |
| Styles (Style of Music) | textarea | ✓ | ✓ | ✓ | Weighted tag list — order matters, see §3 |
| Exclude Styles | textarea | Pro/Premier | Pro/Premier | Pro/Premier | **Plan-gated, not version-gated** `[verified]` |
| Title | text | ✓ | ✓ | ✓ | |
| Voice Gender | selector | ✓ | ✓ | ✓ | male/female. **More reliable than describing gender in Styles** `[verified]` |
| Instrumental | toggle | ✓ | ✓ | ✓ | On = no vocals |
| Weirdness | slider | ✓ | ✓ | ✓ | Introduced in v4.5 `[verified]` |
| Style Influence | slider | ✓ | ✓ | ✓ | Introduced in v4.5 `[verified]` |
| Persona / Voices | selector | — | — | Pro/Premier | **Out of scope** — account-bound state, not reproducible from text |
| Audio Influence | slider | ✓ | ✓ | ✓ | Only appears when audio is uploaded. Out of scope |

**Not Suno fields.** BPM, genre, mood, instruments, vocal tone, rhythm, arrangement, dynamics, production character have **no field of their own**. They are compiled into the Styles string. Treat them as internal representation, never as output slots.

## 2. Character limits `[verified]`

| Field | v4.5 / v5 / v5.5 | v3.5 / v4 (unsupported) |
|---|---|---|
| Lyrics | 5,000 | 3,000 |
| Styles | 1,000 | 200 |
| Title | 100 | 100 |

Two practical ceilings sit well below the hard caps:

- **Lyrics: past ~3,000 chars Suno rushes or truncates the song.** A 3–4 minute song is 200–300 words / 30–40 lines.
- **Styles: keep under ~350 chars.** The 1,000 cap is reachable but not useful.

**Suno truncates silently — no warning.**

## 3. How the Styles field is read `[verified]`

A comma-separated **weighted tag list**. Earlier terms carry substantially more influence. In testing, moving `jazz noir` from position 1 to position 5 of a seven-element prompt changed the result from "a jazz noir track" to "a moody track with some jazz in it."

Consensus ordering: **genre + era → mood + energy → instrumentation → vocal → production / tempo.**

On descriptor count, sources conflict and the disagreement is resolved:

- The widely repeated "4–7 descriptors max" rule traces to a **single third-party guide and is not borne out in practice** `[verified]`.
- What actually degrades output is the **synonym-pile** — `intimate / breathy / whispery / soft` stacked together gives the model nothing new to act on.
- Rich ~10-descriptor style boxes work well **when every term does distinct work**.

**So the constraint is non-redundancy, not count.** Trim synonyms, not detail.

## 4. Version dialects `[verified]`

Fields, limits, and syntax are **identical across v4.5 / v5 / v5.5**. v5 prompts run unchanged on v5.5. What differs is how each version *listens*:

| Version | Prompt personality | Render style |
|---|---|---|
| v4.5 | Responds to descriptive, near-conversational prompts | Fuller phrasing, connective words allowed |
| v5 | Literal and clean; needs less instruction | Compressed, comma-separated, no filler |
| v5.5 | Expressive; emotion terms track closer to intent | Compressed, but finer descriptors earn their place |

Suno's CTO's top recommendation: **do not rerun v4/v4.5 prompts on v5** — v5 listens differently and needs less instruction.

## 5. Tag taxonomy — what goes where

Five distinct layers. Confusing them is the single most common failure.

| Layer | Lives in | Examples | Discipline |
|---|---|---|---|
| **Structure tags** | Lyrics | `[Verse 1]` `[Chorus]` `[Bridge]` `[Interlude]` `[Outro]` | Required on every section |
| **Delivery bracket tags** | Lyrics | `[Whispered]` `[Spoken]` `[Vulnerable]` `[Shout]` | Accent only — 1–3 per section max |
| **Performance notation** | Lyrics | `SHOUTED` `(backing)` `~held~` `cut-` | Plain text on the sung line itself — §5.5 |
| **Style descriptors** | Styles | `gravelly` `melismatic` `belting` `spacious reverb` | Comma prose, never bracketed |
| **Inline metatags** | Lyrics | `[Verse 1: raspy older female, husky contralto]` | **Escalation only**, never a default |

**The Lyrics box holds four of these five, and that is the whole reason it goes wrong.** What separates them is not the bracket — it is Axis 1 in `compiler-rules.md` §1: does a human make this sound? `[Whispered]` and `SHOUTED` describe a human making a sound, so they belong. `[Instrument: Piano]` and `[Texture: Tape-Saturated]` do not — those are slot 3 and slot 6 wearing brackets, and putting them here means the same instruction is now competing with itself across two fields.

### 5.1 Structure tags

```
[Short Instrumental Intro]  [Intro - Spoken]
[Verse]  [Verse 1]  [Verse 2]  [Catchy Verse]
[Pre-Chorus]  [Chorus]  [Hook]  [Catchy Hook]  [Post-Chorus]
[Bridge]
[Break]  [Interlude]  [Guitar Solo Interlude]  [Percussion Break]
[Instrumental]  [Instrumental Break]  [Build-Up]  [Drop]  [Breakdown]
[Outro]  [End]  [Fade Out]  [Fade to End]  [Big Finish]  [Refrain]
```

**Trap: bare `[Intro]` is notoriously unreliable** `[verified]`. Always use a specific form — `[Short Instrumental Intro]`, `[Intro - Spoken]`.

**Emotion-fused structure tags** `[unverified]` — a mood folded into the section tag itself:

```
[Sad Verse]  [Angry Verse]  [Whimsical Verse]  [Hopeful Chorus]  [Melancholic Bridge]
```

This is the same shape as `[Catchy Verse]` and `[Catchy Hook]` above: **one tag, not a stack.** It is a legitimate way to mark a section whose emotion departs from the track's overall mood — the second verse of a song that turns. It is not a licence to open every section with a mood tag; Styles already sets the track's mood, and repeating it per section spends attention on something already said.

### 5.2 Bar count targeting `[unverified]`

Numbers after section tags act as approximate bar targets:

```
[INTRO 4] [VERSE 1 8] [PRE 4] [CHORUS 8] [BRIDGE 8] [OUTRO 4]
```

Treated as targets, not guarantees. Single-source claim — use sparingly, mainly for intro/outro length.

### 5.3 Delivery bracket tags

```
[Shout] [Whispered] [Spoken] [Intimate] [Vulnerable] [Haunting]
[Melancholy] [Energetic] [Aggressive] [Triumphant] [Playful] [Whimsical]
```

### 5.4 Style descriptors — vocal (Styles field, not brackets)

**Delivery:** `staccato` `legato` `vibrato-heavy` `monotone` `melismatic` `syncopated` `operatic` `chanting` `spoken-word` `growling` `belting` `rapping` `scatting` `falsetto runs` `humming` `call-and-response`

**Texture:** `whispered` `gravelly` `velvety` `dreamy` `resonant` `nasal` `brassy` `smoky` `breathy exhale` `rough-edged` `shimmery` `glassy` `crunchy` `chilled`

**Processing:** `spacious reverb` `slapback delay` `auto-tuned` `natural pitch` `vocoded` `distorted vocals` `telephone effect`

### 5.5 Performance notation `[unverified]`

Marks applied to the sung line itself, with no bracket and no tag. This is the only per-word control available — every bracket tag is per-section and every Styles descriptor is per-track.

| Notation | Effect |
|---|---|
| `UPPERCASE` | Shouted or emphasised |
| `(text in parentheses)` | Backing vocal or harmony |
| A line repeated verbatim | Sung as a loop |
| `~word~` | Note held long |
| `word-` | Cut off abruptly |

```
This is OUR time, this is our time
(our time, our time)
I never said good-
```

`(parentheses)` is the well-attested one and is already how ad-libs are written. The other four come from a single third-party source and none has been checked against audio — use them where the effect is worth losing if it silently does nothing, and never as the only thing carrying a moment.

**Uppercase is the one to watch.** It looks free but it is not: an all-caps chorus reads as a chorus with no dynamic range. Emphasise words, not sections.

### 5.6 Other bracket tags `[unverified]`

```
[modulate up a key]    [modulate down a key]    [loop-friendly]    [crowd sings]
```

- `[modulate up a key]` before a final chorus is a real songwriting device and there is no other way to ask for it — Styles has no vocabulary for a key change.
- `[loop-friendly]` matters for background and focus tracks, where the track will run on repeat and a distinct ending becomes a defect. Pairs with `[Fade Out]`, not against it.
- `[crowd sings]` produces group vocals on purpose. Note this is the element Suno adds *unprompted* more than any other (§6) — the tag is only useful when you also want it there and nowhere else.

Single-source, all four. Worth testing before any of them becomes a default.

## 6. Exclude Styles `[verified]`

Two paths with **different grammar** — do not mix them.

| Path | When | Grammar |
|---|---|---|
| Dedicated field | Pro/Premier | Plain noun phrases, **no `no`** — `electric guitar, guitar solo` |
| Inline in Styles | Free tier fallback | `no [element]` appended — `no electric guitar` |

- **2–4 items.** Over-specifying dilutes the effect.
- **Probabilistic, not a filter.** A prompt that strongly implies the element will override the exclusion.
- **Pair every exclusion with a positive replacement in Styles**, or the model refills the gap by habit.
- Suno's most common unrequested addition is **group vocals** — `choir`, `crowd vocals`, `backing vocals`, `gang vocals`, `vocal harmonies`.

## 7. Creative sliders `[verified]`

| Slider | Range | Behavior |
|---|---|---|
| Weirdness | 0–1 (Safe → Chaos) | 50% is the conventional result. **Past 0.7 song form itself breaks down** — a feature for ambient/noise, a failure for anything with a chorus |
| Style Influence | 0–1 (Loose → Strong) | High (70–85) = tight genre focus. Low = looser fusion |

High Weirdness paired with a **specific** genre tag produces interesting results *within* the genre. High Weirdness with a vague genre produces incoherence.

## 8. Language handling `[verified]`

- Best results: English, Spanish, Portuguese, French, Japanese, Korean, Mandarin.
- Korean: v5 handles Hangul well — consistent syllable structure helps.
- **Write in the native script.** Romanization with hyphens is a *local* fix for specific mispronounced words, not a whole-lyric strategy (romanized Japanese collapses homophones).
- **`singing in <language>` must appear in Styles** or Suno drifts off the intended language. This is a behavioral requirement, not a stylistic choice.

## 9. Artist references — hard constraint `[verified]`

After Suno's late-2025 Warner Music settlement, the terms of service changed:

- **Real artist names in prompts are blocked.** `in the style of [artist]` and even `inspired by [artist]` are rejected.
- Attempting to mimic a specific artist risks an **impersonation account strike**.
- The sanctioned substitute is **era + genre + texture**.

An artist name must never reach any output field. See `compiler-rules.md` §6 for the decomposition procedure.

## 10. Instrumental toggle behavior `[user-confirmed]`

With `Instrumental: ON`, the Lyrics box **still accepts structure tags** and they take effect. This gives instrumental tracks direct control of the time axis without any sung content.

With `Instrumental: OFF` and no sung lyrics, a Styles instruction such as `wordless female humming` produces wordless voice texture as intended — Suno does not invent lyrics to fill the gap.

Both were confirmed by the repo owner on 2026-08-07 and **not independently verified**. If Suno changes behavior, these are the first two assumptions to re-test — they are the only load-bearing claims in this file that lack multi-source support.

---

## Sources

- Suno Help — [Creative Sliders](https://help.suno.com/en/articles/6141377), [Custom Mode](https://help.suno.com/en/articles/3726721)
- [Character limits by model](https://hookgenius.app/learn/suno-character-limits/) · [Prompt guide 2026](https://hookgenius.app/learn/suno-prompt-guide-2026/) · [Lyrics formatting](https://hookgenius.app/learn/suno-lyrics-formatting/)
- [Negative prompting guide](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide) · [Multilingual & pronunciation](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-v5-multilingual-english-pronunciation-guide)
- [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) — v5 best practices, structure tags, voice tags
- [schwepps/skills — suno-music-creator](https://github.com/schwepps/skills) (MIT) — source for §5.5 performance notation, §5.6 bracket tags, the emotion-fused structure tags in §5.1, `bpm-by-use-case.md`, and the 40 genres decomposed in `genre-presets.md`. Carries no citations of its own; everything taken from it is tagged `[unverified]`
- [v5 vs v4.5 vs v5.5 comparison](https://acetaggen.com/blog/suno-v5-vs-v4-complete-comparison) · [Prompt order testing](https://travisnicholson.medium.com/how-to-write-better-suno-ai-prompts-50-examples-b362d325d5ef)
- [Artist style without naming](https://roo.beehiiv.com/p/suno-artist-style-prompts) · [Content filter](https://hookgenius.app/learn/suno-content-filter-blocked-words/)
