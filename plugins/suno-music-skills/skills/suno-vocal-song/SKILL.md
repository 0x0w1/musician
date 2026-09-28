---
name: suno-vocal-song
description: Write or revise Suno songs with lyrics, including prompts for editing an existing vocal track.
---

# Suno Vocal Song

Turn the user's idea into a complete Suno handoff with original or user-supplied lyrics. Preserve explicit language, structure, and musical choices. For a request with no sung words, continue through the sibling `suno-instrumental` skill when available; do not make the user repeat the request.

## Choose the work

- **New song:** use [composition rules](../../references/compiler-rules.md) and [lyric guidance](references/lyrics-and-vocals.md). Infer ordinary creative choices; ask only when a missing answer materially changes the requested song.
- **Change a prompt or resume a song:** use [state and revisions](../../references/state-and-revisions.md). Preserve unaffected text exactly.
- **Edit existing audio, use a reference, or diagnose a result:** use [editing and inputs](../../references/editing-and-inputs.md). Distinguish editing a saved prompt from editing a generated recording.

For every Suno handoff, consult the selected model row in [model capabilities](../../references/suno-reference.md) and render the matching [output template](../../references/output-templates.md). Load the profile using [state paths](../../references/state-and-revisions.md#paths); save the result there unless the user requests text only.

## Completion

Deliver usable lyrics, prompts, exclusions, and the complete settings ledger for the selected model and mode. Keep translations outside the copyable lyrics. State meaningful assumptions briefly; do not manufacture a fixed number of warnings. These skills prepare text and instructions, not audio. Do not claim a generation, upload, edit, or listening test occurred without evidence.
