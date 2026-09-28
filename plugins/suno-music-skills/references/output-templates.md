# Complete Suno Output Templates

Use for every Suno handoff. Select **one model + one mode + one vocal state**, unless the user asks for a comparison. Fill every ledger row: do not silently drop a field because it is unavailable. A complete template does not imply every field exists in Suno's UI.

## Rendering contract

1. Start with model, availability, mode, and vocal state (`lyrics`, `instrumental`, or `wordless`). Keep source and target models distinct for old songs.
2. Render each applicable text field under its own label with a separate fenced `text` block. Fence contents contain only pasteable text, never labels, translations, commentary, or placeholders.
3. For an intentionally empty field, write **Empty — leave this field blank** outside a fence. For a hidden field write **Not applicable** or **Unavailable** and a short reason. For unknown controls use **Unverified — use the current UI/default**. Do not paste these markers into Suno.
4. Render the settings ledger below. Use percentage units for numeric sliders. Status is `set`, `empty`, `not_applicable`, `unavailable`, or `unverified`.
5. Put the saved record path, brief concept, meaningful assumptions, and optional proofreading translation after the paste fields. A translation never appears inside Lyrics.

User-facing labels may be translated; Suno field names should remain recognizable.

## Universal field ledger

All adapters account for these fields; labels are not proof of a matching UI control.

| Field | Fill with |
|---|---|
| Requested model | exact user request or `auto` |
| Source model | original recording/profile model, or none |
| Target model | selected current model, or explicitly historical target |
| Availability | current / retired / unverified |
| Mode | Custom / Simple / Edit |
| Vocal state | lyrics / instrumental / wordless |
| Title | song title; preserve for a narrow edit unless requested |
| Prompt | Simple song description or bounded edit instruction; N/A for Custom |
| Lyrics | performed text, empty, or section cues when supported |
| Styles / Style prompt | Custom style text; otherwise represented inside Prompt |
| Exclude Styles / Exclude prompt | exclusions, empty, or represented inside Prompt |
| Instrumental | ON / OFF / preserve; or unavailable in current UI |
| Vocal Gender | actual selector value if exposed; otherwise voice direction in Prompt/Styles |
| Weirdness | 0–100% or explicit status |
| Style Influence | 0–100% or explicit status |
| Audio Influence | 0–100% if applicable and known; otherwise status |
| Variety | v6 value if exposed; recommended 0 for controlled revisions |
| Max Mode | ON / OFF if available; otherwise status |
| Voice | actual selected voice name/ID, none, or unknown |
| Style Persona | actual selection, none, or unknown |
| Custom Model | actual selection/base model if known, none, or unknown |
| My Taste / Personalize | ON / OFF / unknown / unavailable |
| Reference inputs | actual files, song URLs/IDs, and their roles; or none |
| Edit target | source + section/time range + exact change; N/A for new songs |
| Preserve | musical/audio elements to keep; N/A if no edit |
| Sections | saved arrangement; label planning-only if not pasted |
| Target duration | requested length or unspecified; never a guarantee |
| Translation | separate review text, or not requested |

## v6 family: Custom

Applies separately to **v6**, **v6-wild**, and **v6-mini**, using that model's access row. Do not invent different field limits or slider personalities for the variants.

Output in this order:

- Header: target model, mode `Custom`, vocal state, source model if any.
- **Title**: separate paste block.
- **Lyrics**: separate paste block for sung lyrics. Instrumental = empty unless the UI accepts section-only cues. Wordless = empty or section-only cues, never an English translation or invented sung words.
- **Styles / Style prompt**: separate paste block with the desired sound and arrangement.
- **Exclude Styles / Exclude prompt**: separate paste block only when that field exists. Empty if no exclusions. If absent, put the constraints into Styles and state that no separate field is used.
- **Prompt**: Not applicable — Custom uses Styles and Lyrics.
- Complete ledger for all remaining fields.

For lyrics use Instrumental OFF. For voice-free music use ON. For explicitly requested wordless voice use OFF with the caveat in the instrumental skill. A duet may need a voice description instead of one misleading gender selection. If no account UI has been inspected, label advanced controls as suggestions conditional on their visibility; never claim they were set.

## v6 family: Simple

Applies to **v6**, **v6-wild**, and **v6-mini**. Use a **Prompt** paste block carrying the desired sound, vocal state, lyric language if any, arrangement, and exclusions. For references, describe what each supplied input contributes; give attachment instructions outside the prompt.

Provide a suggested Title separately. Styles and Exclude are accounted for as **Not applicable — included in Prompt**, unless the actual UI exposes separate fields. Lyrics is **Not applicable — generated from Prompt** for a song whose words the user wants Suno to write. If exact authored words must be preserved, choose Custom unless the user's Simple interface accepts exact lyrics; never promise that embedding long lyrics in a description locks them.

Complete the same settings ledger. Instrumental intent must be expressed even when the toggle is absent. All hidden sliders and identity controls receive a status rather than fabricated values.

## v6 family: Edit

Applies to **v6**, **v6-wild**, and **v6-mini** subject to actual tool access. Supply:

- **Reference inputs**: source song/file and role, with attachment instructions outside paste blocks.
- **Prompt**: `In [identified section/time], [specific change]. Keep [preserved elements].` Replace every bracketed placeholder with the user's real material or stop short of an executable handoff if the source is missing.
- **Lyrics**: only requested replacement lines in a separate block, or Not applicable.
- **Styles / Style prompt** and **Exclude prompt**: separate only when the selected editor exposes them; otherwise incorporated in Prompt.
- All remaining ledger fields, preserving known source settings rather than resetting them to defaults.

A word replacement, section replacement, extension, cover, mashup, sample-based idea, and mix repair have different targets. See [editing and inputs](editing-and-inputs.md). Text preservation is exact in the saved record; audio preservation is a request to Suno, not a guarantee.

## Legacy: v4.5, v4.5+, v4.5-all, v5, v5.5

Use the Custom or Simple layout above as a **historical handoff**, with the exact model prominently labeled **retired — not selectable for new generation**. Preserve documented settings from the source record. Variety and Max Mode are **Unavailable — v6 controls**. Identity and upload controls are unverified unless the historical record establishes them.

For Custom, fill Title, Lyrics (sung / empty / supported cues), Styles, Exclude, Instrumental, and all ledger rows. For Simple, fill Prompt and account for the other fields with their actual status. Earlier prose-vs-tag advice may be tried as a heuristic; it is not a version-specific requirement.

When the user wants to generate now, create a separate v6-family adaptation and retain the original model and prompt in history. Do not relabel a v5.5 recording as generated by v6.

## Legacy: v2, v3, v3.5, v4; unknown versions

Always retain the exact requested identifier. Use the complete ledger with known Title, Prompt/Styles, Lyrics, and Instrumental information from the source. Mark undocumented fields **Unverified**, not supported by analogy. Variety/Max Mode are unavailable on known pre-v6 models. Modern editing belongs to a new v6 target, not to a fabricated legacy editor.

Unknown future models remain **Unverified** until checked against official information or the user's UI. Never silently downgrade an explicit target.

## Filled examples

These are illustrative text fixtures, not reports of generated audio. Full ledgers for a Korean vocal track, an instrumental, a wordless track, a Simple prompt, an audio edit, and a historical track are in [examples.json](examples.json). Every fixture accounts for every field. Use them to understand field placement; do not copy their creative choices into unrelated requests.
