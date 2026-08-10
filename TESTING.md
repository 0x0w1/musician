# Testing

Test inputs and an evaluation checklist for both skills. Every input is a real prompt — paste it and judge the output against the pass criteria.

---

## suno-vocal-song

| # | Input | What it tests | Pass criteria |
|---|---|---|---|
| 1 | `요즘 조금씩 앞으로 나아가고 있다는 느낌을 노래하고 싶어.` | Baseline inference from a vague emotional line | Finished output with no clarifying questions. 2–3 `⚠️` lines. Genre and mood are specific, not "uplifting pop" |
| 2 | `실패했지만 다시 시작하려는 마음을 노래하고 싶어.` | Emotional movement across the song | Lyrics move somewhere — the last chorus is not the first chorus's mood. Delivery tag placed at the turn, not scattered |
| 3 | `차가운 여름 도시를 걷는 느낌의 J-Pop을 만들고 싶어.` | Genre overriding the profile's default language | Lyrics in Japanese despite a Korean default. `singing in Japanese` present in Styles. Native script, not romaji |
| 4 | `라디오헤드 같은 느낌으로 무기력함에 대한 노래.` | Artist reference guardrail | **"Radiohead" appears nowhere in any output field.** A one-line translation appears in Layer 2. Lyrics are original |
| 5 | `미니멀한 편곡에 기타 다섯 대랑 풀 오케스트라 넣어줘.` | Conflict detection | Does **not** compile. States the conflict in one sentence and asks which matters most |
| 6 | `여성 보컬 발라드인데 코러스 없이.` | Structural deviation + explicit gender | Voice Gender = female. No `[Chorus]` section. Structure still coherent without one |

**Revision tests** — run after #1, in order, against the same song:

| Input | Pass criteria |
|---|---|
| `여성 보컬로 바꿔줘.` | Voice Gender **and** slot 4 both change. One line reports the paired change. Nothing else moves |
| `BPM을 105로 바꿔줘.` | Slot 7 only. A groove suggestion may appear under `⚠️` but is **not applied** |
| `가사를 30% 줄여줘.` | Lyrics shorten. Styles string is byte-identical to before |
| `아까 걸로 되돌려줘.` | Restores from `revision_history` |

---

## suno-instrumental

| # | Input | What it tests | Pass criteria |
|---|---|---|---|
| 1 | `비 오는 새벽에 혼자 작업할 때 들을 음악을 만들고 싶어.` | Baseline; use case shaping dynamics | `Instrumental: ON`. 4–6 sections. Given the work context, no climax or a restrained one |
| 2 | `밤에 혼자 코딩하면서 들을 음악.` | Repeat-listening → dynamics | No climax section. Steady energy or fade out. Not "builds to an emotional peak" |
| 3 | `눈 내리는 숲을 걷는 느낌의 잔잔한 음악.` | Scene → instrumentation and space | 2–4 instruments. Production terms present but ≤2. `choir, backing vocals` likely excluded |
| 4 | `허밍이 들어간 앰비언트 포스트록.` | Voice texture mode | `Instrumental: OFF`. `wordless ... humming` in slot 3. `sung lyrics, spoken word` in Exclude. Lyrics box has structure tags only |
| 5 | `가사도 좀 써줘 — 여름 노래로.` | Boundary enforcement | **Refuses and points to `suno-vocal-song`.** Does not write lyrics. Does not silently produce an instrumental instead |
| 6 | `신스웨이브인데 드럼은 빼줘.` | Exclusion paired with replacement | `drums` excluded **and** slot 3 gains something to carry rhythm (arpeggiated bass, gated pad). Not just a removal |

---

## Outcome and diagnosis

Run against any finished song. These test the loop that closes after generation (`compiler-rules.md` §10).

| Input | What it tests | Pass criteria |
|---|---|---|
| `생성해보니 합창이 계속 껴.` | Record, then diagnose | `outcome` gains a line **before** anything changes. Exclusion added **and** slot 3 gains a replacement. Not just a removal |
| `보컬이 계속 남자로 나와.` | Selector-vs-prose conflict | Voice Gender **and** slot 4 change together. Diagnosed as a conflict, not treated as a new request |
| `네 번 뽑았는데 다 좋았어.` | Recording a non-event | `outcome` gains a line. **Nothing else changes.** No improvement is volunteered |
| `소리가 좀 지직거려.` | Scope boundary | Named as a mix problem, Suno-side. **Does not recompile.** Does not invent a Styles fix |
| `가사는 좋은데 곡이 너무 짧아.` | Length lever | Adds a section. Does **not** pad verses or touch Styles |
| (after three songs each excluding `choir`) | Preference detection | Offers to move it into the profile's `Always exclude`. **Offers — does not write** |

## Evaluation checklist

Score every result against all ten. A failure on 1, 5, or 7 is a design bug, not a taste disagreement.

| # | Criterion | How to judge |
|---|---|---|
| 1 | **Intent preserved** | Does the concept summary describe the song the user asked for? Read only the summary and check it against the original line |
| 2 | **Musically coherent** | Do genre, instrumentation, tempo, and dynamics describe one plausible track? Any pair that fights is a failure |
| 3 | **Styles is clear** | Under 350 chars. Genre first. **No two descriptors saying the same thing** |
| 4 | **Exclude is clear** | 2–4 plain noun phrases, no `no` (unless free-tier fallback). Every exclusion has a positive replacement in Styles |
| 5 | **Lyrics / production separated** | Scan the Lyrics box: any playing technique, mixing, or production word is a failure |
| 6 | **No repetition** | Nothing in Layer 2 restates Styles content in prose. No field appears twice |
| 7 | **Revisions preserve decisions** | Diff the song file before and after. Only the named slot and required cascades changed |
| 8 | **Paste-ready** | Can every Layer 1 block be copied into Suno without editing? Labels and prose must not be inside the copyable content |
| 9 | **Skill boundary holds** | Did the vocal skill stay out of instrumentals and vice versa? Handoffs happen instead of redesigns |
| 10 | **Outcome recorded** | After any report on a generation, does the song file have a new `outcome` line — including when the report was that nothing was wrong? |

---

## Known unverified assumptions

Two behaviors are owner-confirmed but not independently verified (`skills/_shared/suno-reference.md` §10). If output quality drops unexpectedly, re-test these first:

1. `Instrumental: ON` still honors structure tags in the Lyrics box
2. `Instrumental: OFF` with no sung text produces wordless voice without Suno inventing lyrics

### Added in v0.1.1 — untested against audio

Everything below came from an uncited third-party library and none of it has been heard. Ranked by how much breaks if it turns out to be wrong:

| # | Assumption | Where | If wrong |
|---|---|---|---|
| 3 | `~word~` holds a note, `word-` cuts off, `UPPERCASE` shouts | reference §5.5 | Ignored silently — cosmetic loss |
| 4 | `[loop-friendly]` produces a seamless loop | reference §5.6 | Background tracks keep a seam; no other harm |
| 5 | `[modulate up a key]` performs a key change | reference §5.6 | No other way to ask; feature simply absent |
| 6 | Emotion-fused section tags (`[Sad Verse]`) are honored | reference §5.1 | Falls back to a plain section tag |
| 7 | 6–12 syllables/line is the English alignment band | lyrics-and-vocals §1 | Lines crowd or stretch; the Korean and Japanese bands are inferred from this one and fall with it |
| 8 | Section count maps to duration as stated | lyrics-and-vocals §1, instrumentation §3 | Songs land long or short |
| 9 | Genre presets describe their genres accurately | genre-presets.md | Wrong opening values — but every preset is meant to be overwritten by the concept, so this degrades rather than breaks |

Test 3 is the cheapest to check and covers four claims at once: generate one song with all four notations on known lines and listen for each.
