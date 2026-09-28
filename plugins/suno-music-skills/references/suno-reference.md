# Suno Models and Capabilities

Checked **2026-09-28**. These are text handoff targets, not an audio-generation API. Inspect the user's current model picker and visible controls when available; do not infer plan or mode-specific controls from a version label alone.

## Evidence

- **official:** a linked first-party document, with its check date above.
- **observed:** a recorded model, settings, generation, and result. No v6 audio trials have been performed for this package.
- **heuristic:** a compositional or prompting recommendation, not a Suno guarantee.
- **experimental:** an untested technique or older observation not reproduced on the target model.

Do not upgrade an experiment to a default because multiple blogs repeat it.

## Model selection

| Requested model | Status | Access / use | Output adapter |
|---|---|---|---|
| v6 | current | Pro/Premier; precise direction | v6 template |
| v6-wild | current | Pro/Premier; exploratory direction | v6 template, preserve model |
| v6-mini | current | all plans; quick ideas | v6 template, preserve model |
| v5.5 | retired | historical record only | legacy Custom/Simple |
| v5 | retired | historical record only | legacy Custom/Simple |
| v4.5+ | retired | historical record only | legacy Custom/Simple |
| v4.5-all | retired | historical record only | legacy Custom/Simple |
| v4.5 | retired | historical record only | legacy Custom/Simple |
| v4 | retired | historical record only | legacy Custom/Simple |
| v3.5 | retired | historical record only | legacy Custom/Simple |
| v3 | retired | historical record only | legacy / unknown controls |
| v2 | retired | historical record only | legacy / unknown controls |

The current three-model lineup and access are **official**: [Current Models](https://help.suno.com/en/articles/13924737). All three support up to eight minutes per generation: [What's new](https://help.suno.com/en/articles/13924801). This is a ceiling, not a guaranteed duration.

The retirement of all pre-v6 models and preservation of old songs are **official**: [v6 FAQ](https://help.suno.com/en/articles/13924481). Listing an older identifier here does not claim it remains selectable. For a new generation from an old profile, retain `source_model` and recommend a current `target_model`. Do not silently overwrite the profile. An explicitly requested historical prompt stays labeled historical; offer a separate current adaptation. For an unfamiliar version, keep its name and mark capabilities unverified rather than inheriting the latest settings.

Default recommendation: v6 for a known paid plan, v6-mini for free or unknown access; disclose the unknown-plan assumption. Choose v6-wild when exploration is requested, not just because a genre is unusual.

## Modes and fields

| Field / control | Custom | Simple | Existing-audio edit |
|---|---|---|---|
| Title | title field | suggested title; UI may name result | new title only if requested |
| Prompt | not a separate Custom field | natural-language song request | bounded edit request |
| Lyrics | authored sung text / empty instrumental | supply separately only if the UI accepts it | replacement words for selected region |
| Styles / Style prompt | global musical description | included in Prompt | description of requested change |
| Exclude Styles / Exclude prompt | dedicated field if exposed | constraints within Prompt | constraints within edit request unless field exposed |
| Instrumental | ON/OFF | toggle if exposed; also describe intent | preserve / change only if requested |
| Vocal Gender | only if selector exists | voice description in Prompt | preserve / describe requested change |
| Weirdness / Style Influence | only if exposed | do not assume controls | only if exposed |
| Audio Influence | audio-based flow, if exposed | do not assume controls | audio-based flow, if exposed |
| Variety / Max Mode | v6; confirm control availability | v6; confirm availability | v6; confirm availability |
| Voices / Style Persona / Custom Model | account-dependent | account-dependent | account-dependent |
| My Taste / Personalize | record actual state if exposed | record actual state if exposed | record actual state if exposed |

Custom text fields and Instrumental are described in [Custom Mode](https://help.suno.com/en/articles/3726721). That document is Android-specific and predates v6; exact cross-platform UI parity is **unverified**. Dedicated exclusion availability by plan, gender-selector options, and numeric input caps need a current UI check. Do not automatically suppress Exclude on free plans based on the old plugin assumption.

Weirdness, Style Influence, and upload-dependent Audio Influence are **officially documented** in [Creative Sliders](https://help.suno.com/en/articles/6141377), dated 2025-06-03; this does not prove every v6 mode exposes them. Variety changes style prompts; zero preserves control of those tags. Max Mode uses extra credits. These v6 features are **official** in the [FAQ](https://help.suno.com/en/articles/13924481).

## Legacy settings and limits

For v4.5/v4.5+/v4.5-all/v5/v5.5 records, preserve known Lyrics, Styles, Exclude, Instrumental, gender, and slider values. Their availability for a historical session must come from that session, not from this table. Do not add Variety or Max Mode to a pre-v6 recreation: mark unavailable. For v2/v3/v3.5/v4, modern controls are unverified unless the record establishes them.

The previous package used 5,000 Lyrics / 1,000 Styles / 100 Title characters for v4.5–v5.5 and 3,000 / 200 / 100 for v3.5–v4, based on third-party guides. Those limits have not been independently confirmed here and must not be carried into v6 as facts. The actual UI counter wins. There is no established universal 3,000-character truncation boundary or four-instrument limit.

## Arrangement experiments

Common section cues include `[Verse]`, `[Chorus]`, `[Bridge]`, `[Instrumental Break]`, and `[Outro]`. They request musical structure; they do not guarantee it. Fixed bar counts, emotion-fused tags, `~held~`, `word-`, uppercase emphasis, and `[loop-friendly]` are **experimental**. A fade-out is not evidence of a seamless loop.

On 2026-08-07 the owner reported structure cues working with Instrumental ON, and wordless voice with OFF and empty sung text. These are **historical observations**, not verified v6 behavior. Use the fallback in the instrumental entrypoint when the UI hides Lyrics.

## Further inputs

Natural-language section/lyric edits, multiple musical sources, images, video, and audio are documented in the [v6 announcement](https://suno.com/blog/introducing-v6). Consult [editing and inputs](editing-and-inputs.md) for handoff behavior; account compatibility and exact edit controls still require checking.
