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

## Evaluation checklist

Score every result against all nine. A failure on 1, 5, or 7 is a design bug, not a taste disagreement.

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

---

## Known unverified assumptions

Two behaviors are owner-confirmed but not independently verified (`skills/_shared/suno-reference.md` §10). If output quality drops unexpectedly, re-test these first:

1. `Instrumental: ON` still honors structure tags in the Lyrics box
2. `Instrumental: OFF` with no sung text produces wordless voice without Suno inventing lyrics
