---
name: suno-instrumental
description: Write or revise Suno instrumental prompts, arrangements, and wordless vocal textures.
---

# Suno Instrumental

Turn a scene, purpose, or musical idea into a complete Suno handoff without sung words. Wordless humming and choir textures belong here when requested. For lyrics, continue through the sibling `suno-vocal-song` skill when available without making the user repeat the request.

## Choose the work

- **New track:** use [composition rules](../../references/compiler-rules.md) and [arrangement guidance](references/instrumentation-and-performance.md).
- **Change a prompt or resume a track:** use [state and revisions](../../references/state-and-revisions.md). Save arrangement sections as well as prompt text.
- **Edit existing audio, use a reference, or diagnose a result:** use [editing and inputs](../../references/editing-and-inputs.md).

For every Suno handoff, consult the selected model row in [model capabilities](../../references/suno-reference.md) and render the matching [output template](../../references/output-templates.md). Load the profile using [state paths](../../references/state-and-revisions.md#paths); save the result unless the user requests text only.

## Voice and arrangement

Use Instrumental ON for a track without voices. For explicitly requested humming or wordless choir, use OFF and describe the wordless voice as an instrument. Empty lyrics may still lead Suno to invent words; treat the result as an experiment, not a guarantee. Do not exclude a voice texture the user requested.

Keep a section plan in the song record. Use a Lyrics box containing only section cues if the current UI accepts it with Instrumental ON. Otherwise leave Lyrics empty and express the arrangement in Styles or the Simple prompt. Do not claim those cues guarantee section timing or a seamless loop.

## Completion

Deliver the prompts, exclusions, complete settings ledger, and saved arrangement. Shape dynamics for the intended listening use; a short logo, long ambient piece, and concert track need different structures. These skills prepare text and instructions, not audio. Report only meaningful uncertainty.
