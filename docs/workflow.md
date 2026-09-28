# Workflow

## Compose, explore, or edit

The two entrypoints distinguish sung lyrics from instrumentals and requested wordless voices. They route to the references needed for the current task rather than reading the entire library on every request.

- Custom handoffs provide exact lyrics, style text, exclusions, and a settings ledger.
- Simple handoffs express musical intent in natural language and describe supplied inputs.
- Existing-audio edits identify the source, targeted passage or lyric, requested change, and preserved material.

Model choice follows the user's request and actual access. v6 is the paid-plan starting recommendation, v6-mini works for free or unknown access, and v6-wild is for requested exploration. Historical model templates are labeled retired; they cannot make an old model selectable again. See [capabilities](../references/suno-reference.md).

The [output contract](../references/output-templates.md) accounts for all fields even when they are empty, unavailable, or unverified. Each pasteable field has its own block. Translations and explanations never go into sung lyrics. Account-dependent controls are conditional, not invented.

## Musical judgment

Slots preserve creative decisions without imposing a fixed tag order. Instrument count, genre blending, lyric length, and section count are flexible. [Presets](../references/genre-presets.md) and [tempo examples](../references/bpm-by-use-case.md) are heuristics, not tested Suno behavior. Explicit user language always outranks a genre suggestion.

## State and feedback

The [state helper](../references/scripts/song_state.py) stores full snapshots, including instrumental sections. Restoring a snapshot appends an exact copy of its data while retaining later history and feedback. It does not restore audio or undo changes inside Suno.

The agent records feedback before proposing a fix, distinguishes observations from hypotheses, and avoids changing unrelated decisions. Repeated failures do not automatically become user preferences. Old Markdown histories are preserved; missing previous values cannot be reconstructed from a list of changed field names.

## Validation limits

Automated checks verify package parity, manifests, local links, field ledgers, history restoration, and installer behavior. They do not establish audio quality, pronunciation, genre fidelity, loop continuity, or exact timing. No paid Suno generations were run for this release. Account controls and UI availability can vary; the current Suno interface takes precedence over an unverified template assumption.

The short entrypoints and conditional references follow [OpenAI's Astra skill guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): narrow discovery descriptions, progressive disclosure, and less rigid procedural scaffolding. The core skill files remain host-neutral.
