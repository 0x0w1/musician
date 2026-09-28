# Editing and Reference Inputs

Use when a recording exists, the request supplies media, or the user reports a result. The output remains a Suno handoff unless a separate, authorized Suno execution tool is actually available.

## Select the operation

| Request | Handoff |
|---|---|
| Change saved prompt before generating | Change only affected fields; no source recording required |
| Change a word in an existing take | Identify source and lyric occurrence; provide replacement and preserve instruction |
| Change the chorus or one passage | Identify source, section or time range, requested change, and preserved material |
| Longer ending or additional section | Extend request with continuation point and musical direction |
| Same song, new style | Cover/remix request with source and intended changes |
| Combine own tracks | List each source and contribution; write one combined request |
| Build from a riff/sample | Identify source and interval, desired extracted element, and new arrangement |
| Work from photo/video/audio | Inspect accessible input; describe musical interpretation and input roles |
| Buried vocal, artifacts, or mix imbalance | Consider remaster, stems, or editor adjustment; do not assert a prompt fault |

For editing existing audio, ask for a source only if none is available. A lyric-only draft can still be prepared while a source is missing, but label it as a draft and do not claim it is ready to execute. Use source IDs or filenames the user supplied; do not invent song links, timestamps, voice IDs, or inaccessible media content.

## Preservation and controls

Write the smallest complete instruction that expresses the edit. Record `source_model`, current `target_model`, the targeted region, changed words/arrangement, and the elements to preserve. Keep known settings unless asked to change them. Old audio stays associated with its original model even when its next iteration uses v6.

Voices, Style Personas, Custom Models, and My Taste/Personalize are optional account state. Use an actual selected resource when supplied or visible; otherwise record `none` or `unknown`. Do not claim identical voices can be reconstructed with descriptive text alone. An uploaded reference may expose Audio Influence; report a percentage only when the setting is known or explicitly presented as a conditional suggestion.

The v6 Simple workflow can route natural-language requests to editing tools. Describe the operation without assuming an undocumented button sequence. Tool and plan access must be verified in the user's interface. No automatic uploads, paid generations, or retry loop is part of this plugin.

## Diagnose with evidence

First append the user's exact feedback and known model/settings/source to the outcome log, even when no change is needed. Separate observation from hypothesis. One failed take does not prove causality.

- Wrong language: inspect actual lyrics, translation leakage, language direction, and source material.
- Wrong voice: inspect selectors, Styles, selected Voice/Persona, and source recording before changing a coherent prompt.
- Unwanted instruments/choir: compare positive instructions and exclusions with what was heard; do not replace the arrangement by habit.
- Too short/long: compare requested structure, lyric density, tempo, and actual duration; an Extend or Crop operation may preserve more than regeneration.
- Flat dynamics or distracting climax: check the intended use and section plan before changing genre.
- Artifacts or a buried voice: a mix/editor operation may help. If the prompt itself asks for distortion or dense masking, removing that request may also be relevant.

Choose one plausible change, log the hypothesis, and compare subsequent results. Repeated corrections may indicate preference, model bias, or the same source conflict. Offer a profile update only when the user confirms the preference; do not infer it from a fixed number of failures.
