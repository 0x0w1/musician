# Composition Rules

Use for a new song or a substantive arrangement change. For small revisions, use [state and revisions](state-and-revisions.md) without redesigning the track.

## Intent and musical decisions

Preserve the user's explicit choices before profile preferences, then infer what is missing. Lyric language is independent of genre: Korean J-pop is valid. Use the profile language unless the user specifies another; with no preference, infer from the request and state that choice briefly.

Keep addressable decisions for genre, mood/energy, instrumentation, vocal character, groove, production, BPM, sections, and target duration. These are internal composition data, not claims that Suno has a control for each one. BPM and duration are requests rather than guarantees.

Start with a recognizable musical direction. Two to four instruments and one dominant genre are useful defaults for a simple request, not caps. Preserve a requested orchestra, solo instrument, or multi-genre arrangement. Name instrument roles when that clarifies the result. Consult [genre presets](genre-presets.md) and [tempo examples](bpm-by-use-case.md) only when useful; they are untested starting points.

## Prompt rendering

- **Custom:** put global musical character in Styles, sung words and restrained section cues in Lyrics, unwanted elements in Exclude when the UI exposes it.
- **Simple:** write a natural-language prompt describing the song, voice or absence of voice, language, arrangement, and useful references. Do not assume a separate Lyrics or Exclude control exists in that mode.
- **Editing:** express a bounded change to identified source material, using [editing and inputs](editing-and-inputs.md).

Put the most important requirement early for readability. Slot order is not a proven weighting mechanism. Use concise prose or descriptors according to the task; do not force all v6 requests into comma tags. Remove redundant descriptors without deleting necessary detail to reach an arbitrary count. A 350-character style prompt is a useful starting size, not a hard limit. Read the actual field counter before claiming a maximum; [model capabilities](suno-reference.md) records what has and has not been established.

Keep production notes out of sung lines. Section-specific cues may be bracketed, but are instructions Suno may ignore or sing, not a formal programming language. Describe a key change or instrumental gesture in ordinary language when appropriate; no special tag is the only way to request it.

## Exclusions

Prefer the user's exclusions. Add a profile preference only when it does not conflict with this request. Leave Exclude empty when unnecessary. Use clear noun phrases in a dedicated field; in Simple mode or without that field, include a concise constraint in the main prompt. Negative wording is not a reliable filter.

A positive alternative can clarify the arrangement, but do not add instruments merely because something was removed. `Remove drums` can mean silence in that role. Do not infer choir contamination as a universal Suno behavior. Evaluate the actual result before adding habitual exclusions.

## Controls

Normalize numeric slider values to **0–100 percent**, including stored snapshots. Choose controls independently and only when they exist in the chosen UI. The official creative-slider description names 50% Weirdness as a normal result; it does not establish a collapse threshold at 70%.

For an ordinary Custom request with visible controls, a starting suggestion is Weirdness 50% and Style Influence 70%; these are heuristics. Follow explicit settings and refine one variable at a time. Do not derive a slider setting solely from the model name.

For v6, suggest Variety 0 when preserving authored style tags; exploration may use the user's existing setting. Keep Max Mode OFF unless requested or selected after explaining its additional credit cost. Voices, Style Personas, Custom Models, My Taste/Personalize, and Audio Influence depend on available account state. Record actual selections or `none`/`unknown`; do not invent identifiers or slider values for hidden controls.

## References and output

Translate artist references into musical characteristics useful for an original composition; show the translation briefly if helpful. Do not copy lyrics from a named song. User-supplied lyrics may be edited as requested. Do not assert unverified account-strike policies.

Use the [complete output template](output-templates.md). Put explanations, translations, and uncertainty outside paste blocks. Saving a prompt does not mean the user generated it.
