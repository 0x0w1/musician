# Genre Presets

Opening slot values for 44 genres. **Starting points, not output.**

**Status: `[unverified]`.** Forty of these are decompositions of a third-party genre library (see `suno-reference.md` Sources); four are authored here (§9). None has been checked against generated audio.

---

## 1. How to use a preset

A preset fills slots 1, 2, 3, 5, 6, 7 — and slot 4 for the vocal skill — with values that are known to describe the genre. It does not fill them with values that describe *this* track.

1. Load the preset for the nearest genre.
2. Replace whatever the concept actually determines. A preset that survives untouched means the concept was never resolved (`compiler-rules.md` §2).
3. **Run the redundancy pass anyway.** Preset descriptors plus concept descriptors is exactly how a synonym-pile forms — `warm` from the preset meeting `warm analog tape` from the concept.
4. Compile in the profile's version dialect (§3). The cells below are neutral English fragments, not finished strings.

**The source strings put BPM in second position. These tables do not, and neither does the compiler.** Order is weight (`suno-reference.md` §3), and tempo is the least discriminating thing you can say about a track. BPM is slot 7, always last. This is the single most important thing that changed in the decomposition — a pasted source string would have contradicted the rule the compiler is built on.

**The vocal column is slot 4 material for `suno-vocal-song` only.** For `suno-instrumental` it is ignored, and a `—` means the genre is ordinarily instrumental. `singing in <language>` is appended by the skill, not by the preset, except where the genre itself names a language.

**The exclusions column is priority-2 candidates only** — what Suno habitually contaminates this genre with. Priority 1 is whatever the user said they don't want, and it always outranks these (`compiler-rules.md` §4). These entries are inferred from genre convention, not observed from generations; drop any that the concept actually wants, and keep the pairing rule — every exclusion needs a positive replacement in slot 3.

---

## 2. Electronic and EDM

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| House | classic house | groovy, warm | piano chords, funky bassline, filtered pads | four-on-the-floor | — | 124 | soulful female alto | trap hi-hats, heavy distortion |
| Progressive house | progressive house | melodic, euphoric | emotional synth lead, atmospheric pads, sub bass | driving, long build | wide, glossy | 128 | airy female | acoustic guitar, spoken word |
| Techno | dark techno | hypnotic, industrial | heavy kick, atmospheric synths, sub bass | relentless, minimal | dry, cold | 135 | — | vocals, choir, melodic pop chorus |
| Trance | uplifting trance | euphoric, soaring | soaring synth lead, supersaw pads, sub bass | breakdown and lift | wide reverb | 140 | ethereal female | rap verses, lo-fi texture |
| Dubstep | heavy dubstep | aggressive, massive | wobble bass, growling synths, hard drums | half-time drop | saturated, loud | 140 | — | soft piano, orchestral strings |
| Drum and bass | liquid drum and bass | smooth, uplifting | rolling bassline, atmospheric pads, breakbeats | fast breakbeat | spacious | 174 | soulful female | screamed vocals, heavy distortion |
| Synthwave | 80s synthwave | nostalgic, dreamy | retro analog synths, arpeggiated bass, gated drums | steady, arpeggio-driven | analog warmth | 110 | dreamy male tenor | acoustic guitar, modern trap hi-hats |
| Future bass | future bass | colorful, emotional | wobbly synth chords, pitched vocal chops, sub bass | syncopated, festival drop | glossy, wide | 150 | processed, pitched | acoustic arrangement, lo-fi hiss |

## 3. Hip-hop

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Boom bap | 90s boom bap | nostalgic, confident | jazzy piano samples, upright bass, punchy drums | swung breakbeat | vinyl warmth | 90 | confident conversational male | auto-tune, EDM drops |
| Trap | trap | dark, hard-hitting | 808 bass, rolling hi-hats, sparse synth lead | half-time, triplet hats | sub-heavy, loud | 140 | aggressive male flow | acoustic guitar, orchestral strings |
| Cloud rap | cloud rap | dreamy, hazy | ethereal synth pads, muted 808, sparse drums | slow, floating | reverb-drenched | 70 | auto-tuned melodic male | punchy drums, bright production |
| French rap | French rap | street, melancholic | melancholic piano, heavy kick, sparse strings | steady, spoken cadence | dry, close | 100 | technical male flow, singing in French | sung pop chorus, EDM synths |
| Old school | old school hip-hop | funky, playful | breakbeats, brass samples, turntable scratches | swung, call-and-response | vinyl warmth | 95 | party male, call-and-response | auto-tune, 808 bass |
| Drill | UK drill | dark, menacing | sliding 808s, minor-key bell melody, sparse hats | half-time, off-grid | dry, cold | 140 | aggressive male | sung chorus, warm pads |

## 4. Rock and metal

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Classic rock | 70s classic rock | energetic, swaggering | electric guitar, Hammond organ, driving drums | straight backbeat | analog tape warmth | 120 | raspy male | synth pads, electronic drums |
| Hard rock | hard rock | powerful, defiant | distorted guitar riffs, pounding drums, electric bass | driving, riff-led | compressed, loud | 140 | belting male | acoustic ballad, orchestral strings |
| Arena rock | 80s arena rock | anthemic, triumphant | layered big guitars, stadium drums, synth pad | four-on-the-floor stomp | wide reverb | 130 | soaring male, sing-along | lo-fi texture, trap hi-hats |
| Pop rock | pop rock | catchy, bright | jangly electric guitar, upbeat drums, electric bass | steady backbeat | clean, polished | 125 | male and female harmony | growled vocals, heavy distortion |
| Punk rock | punk rock | fast, rebellious | raw distorted guitar, rapid drums, driving bass | relentless eighth notes | raw, unpolished | 180 | shouted male | polished production, synth pads |
| Metal | heavy metal | aggressive, relentless | shredding guitars, double bass drums, downtuned bass | double-time, riff-led | tight, loud | 160 | growling male | acoustic guitar, soft piano |
| Nu metal | nu metal | heavy, brooding | downtuned guitars, turntable scratches, thick bass | half-time groove | thick, compressed | 100 | rapped verse, screamed chorus | orchestral strings, clean jazz |

## 5. Pop

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Dance pop | dance pop | catchy, bright | synth hooks, four-on-the-floor drums, sub bass | four-on-the-floor | radio-ready, polished | 120 | polished female | lo-fi hiss, growled vocals |
| Electropop | electropop | glossy, upbeat | lead synth, drum machine, sub bass | steady, syncopated | glossy, processed | 118 | processed female | acoustic arrangement, orchestral strings |
| Indie pop | indie pop | dreamy, introspective | jangly guitar, soft synth pad, brushed drums | loose, laid-back | lo-fi warmth | 110 | soft close-miked male | polished pop production, EDM drops |
| K-pop | K-pop | energetic, colorful | synth hooks, electronic drums, sub bass | syncopated, dance break | wide, polished | 125 | layered polished vocals | lo-fi texture, raw production |
| Power ballad | power ballad | emotional, swelling | piano, building strings, live drums | slow, rubato into steady | wide reverb | 70 | soaring female, belting on the chorus | trap hi-hats, electronic drums |

## 6. Chill and ambient

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Lo-fi hip-hop | lo-fi hip-hop | relaxing, nostalgic | warm Rhodes piano, soft drums, upright bass | swung, laid-back | vinyl crackle, tape warmth | 75 | — | vocals, choir, bright digital production |
| Ambient | ambient electronic | atmospheric, still | evolving pads, subtle drones, field texture | no pulse | spacious, soft | 60 | — | drums, vocals, choir |
| Chillwave | chillwave | dreamy, nostalgic | reverb-drenched synths, warm bass, soft drums | hazy, mid-tempo | washed, saturated | 95 | soft distant male | punchy modern drums, spoken word |
| Downtempo | downtempo electronic | groovy, hypnotic | deep bass, organic percussion, textured pads | loose mid-tempo groove | warm, wide | 90 | — | aggressive drums, EDM drops |
| Jazz lo-fi | jazz lo-fi | smooth, late-night | saxophone, upright bass, brushed drums | swung, relaxed | vinyl warmth | 80 | — | vocals, choir, electronic drums |

## 7. Cinematic and specialized

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Epic cinematic | epic cinematic | heroic, triumphant | soaring strings, powerful brass, massive drums | building, downbeat hits | wide, cinematic | 90 | — | choir, electric guitar |
| Corporate uplifting | corporate uplifting | optimistic, warm | acoustic guitar, warm piano, light percussion | steady, gentle build | clean, bright | 120 | — | heavy distortion, dark textures |
| Children's | children's music | playful, cheerful | bright keyboard, bouncy bass, hand percussion | bouncy, simple | clean, close | 110 | cheerful female | dark textures, heavy distortion |
| Chiptune | chiptune synthwave | nostalgic, arcade | 8-bit lead, square bass, retro drums | driving, arpeggio | clean digital | 130 | — | acoustic instruments, orchestral strings |
| Christmas | Christmas pop | festive, warm | sleigh bells, warm orchestration, piano | steady, lilting | wide, warm | 115 | joyful female | heavy distortion, dark textures |
| Romantic ballad | romantic ballad | intimate, tender | fingerpicked acoustic guitar, soft strings, upright bass | slow, unhurried | close, warm | 65 | tender female or male | electronic drums, heavy production |

## 8. French

Note: the source library writes these style strings **in French** (`piano mélancolique`, `voix masculine chaude`). Whether Suno reads a non-English Styles field as well as an English one is untested and §8 of the reference does not cover it — the mandate there is only that `singing in <language>` appear. These presets are given in English; writing them in the target language is an open question worth testing, not a rule.

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| Variété française | variété française | nostalgic, melodic | acoustic piano, elegant strings, upright bass | steady, unhurried | warm, close | 100 | warm male, singing in French | trap hi-hats, heavy distortion |
| French touch | French touch | funky, sophisticated | filtered disco samples, groovy bassline, vocoder | four-on-the-floor | filtered, analog | 122 | vocoded | acoustic arrangement, growled vocals |
| Chanson française | chanson française | poetic, intimate | accordion, acoustic guitar, upright bass | rubato, conversational | dry, close | 85 | expressive voice, singing in French | electronic drums, synth pads |

## 9. Authored here — East Asian genres

**Not from the source library.** It covers EDM, rock, hip-hop and French and contains no J-pop, city pop, Korean ballad or Korean indie — which is the entire home territory of a profile whose `default_lyric_language` is Korean, and which the test suite already exercises (`TESTING.md`, vocal test #3 is a J-pop input). These four are written here from genre convention to close that gap.

They carry the same `[unverified]` status as the rest of the file and one additional caveat: they have no third-party corroboration at all.

| Genre | 1 genre / era | 2 mood | 3 instrumentation | 5 rhythm | 6 production | 7 BPM | 4 vocal | priority-2 excludes |
|---|---|---|---|---|---|---|---|---|
| J-pop | modern J-pop | bright, propulsive | bright electric guitar, synth pad, live drums | busy, syncopated | clean, wide | 135 | clear female, singing in Japanese | lo-fi texture, spoken word |
| City pop | 80s city pop | wistful, urbane | electric piano, slap bass, gated drums | laid-back funk groove | analog warmth, wide | 105 | smooth voice, singing in Japanese | trap hi-hats, heavy distortion |
| Korean ballad | Korean ballad | aching, restrained | piano, strings entering late, live drums | slow, builds to the final chorus | wide reverb | 68 | breathy female alto, belting on the last chorus, singing in Korean | electronic drums, trap hi-hats |
| Korean indie | Korean indie pop | wistful, unhurried | fingerpicked acoustic guitar, soft electric piano, brushed drums | loose, behind the beat | lo-fi warmth, close | 92 | soft close-miked male, singing in Korean | polished pop production, EDM drops |

## 10. What the presets confirm

Two rules in `compiler-rules.md` had no external support before this file existed. The source library, written independently and to a different philosophy, happens to corroborate both:

- **Instrumentation, 2–4 named instruments.** Essentially every source string names three or four. Not one names more than four.
- **One dominant genre, at most two blended.** Every source string opens with a single genre, sometimes with an era or a modifier, never with a stack.

This is corroboration, not verification — the source is uncited and may share ancestry with the material already in `suno-reference.md`. But two independently-arrived-at rules agreeing is worth more than either alone.
