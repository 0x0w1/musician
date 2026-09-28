# Validation and Evaluation

## Automated checks

```bash
python3 scripts/build_plugin.py --check
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

These exercise complete field ledgers, exact snapshot restoration, preservation of feedback and instrumental sections, invalid-record rejection, legacy Markdown preservation, idempotent plugin installation, backups, and protection of locally modified files. Package checks cover generated/source parity, local links, skill discovery names, and all three manifests.

Run host validators when available. A passing static or filesystem check is not a claim that a host loaded a live skill or Suno generated the requested sound.

## Behavioral scenarios

Use the relevant skill with a disposable state root. Assess whether the request is preserved rather than matching exact wording.

| Scenario | Observable result |
|---|---|
| Free plan, new vocal song | v6-mini recommendation; no assumption of paid access |
| Unknown plan, short instrumental | usable v6-mini draft with disclosed assumption; no lyric-language interview |
| Paid plan, precise song | v6 unless the user chose another model |
| Explicit v6-wild request | retain v6-wild and do not silently substitute v6 |
| Korean lyrics in a J-pop style | Korean lyrics regardless of genre suggestion |
| User requests a translation | separate translation; none in copyable Lyrics |
| Solo piano or five-part orchestra | preserve requested instrumentation rather than force 2–4 instruments |
| Remove drums | remove drums without automatically adding a replacement |
| Voice-free instrumental, Lyrics hidden | Instrumental ON, empty Lyrics, arrangement in Styles/Prompt and saved sections |
| Wordless humming | OFF, no sung text, no exclusion contradicting humming; uncertainty acknowledged |
| Simple prompt with a photograph | reference only observed/supplied content; account for Styles/Exclude inside Prompt |
| Exact user lyrics with mode unspecified | Custom handoff; lyrics not reduced to a vague Simple description |
| Existing song, change one line | identify source and occurrence; preserve other words/settings |
| Audio edit with no source | request missing source; any preliminary text is labeled draft |
| Two-source mashup | actual input identifiers and separate contribution roles |
| Legacy v5.5 profile, generate now | retain source model; current-model adaptation clearly labeled |
| Explicit historical v4 request | retired-model label; unknown controls unverified, not invented |
| Future/unknown model | exact identifier retained; capabilities not assumed |
| Restore after restarting session | load saved snapshot and restore exact data, retaining outcome log |
| Old Markdown with field-name-only history | preserve original; do not fabricate earlier values |
| Four good takes | feedback recorded; no unsolicited prompt revision |
| Wrong voice despite consistent settings | inspect source/identity controls; do not assert a selector conflict |
| No Python available | text handoff still works; do not claim a snapshot was saved |

## Model / mode / voice coverage

For each current model (`v6`, `v6-wild`, `v6-mini`), review Custom, Simple, and Edit with sung lyrics, voice-free music, and wordless voice. All applicable values or explicit statuses must be present in the universal ledger. A missing control must not be rendered as an applied setting.

Review historical adapters for `v2`, `v3`, `v3.5`, `v4`, `v4.5`, `v4.5+`, `v4.5-all`, `v5`, and `v5.5`. Modern edits use a current target, and Variety/Max Mode are unavailable for pre-v6 recreations. See [filled fixtures](references/examples.json).

## Audio experiments — not run for v0.3.0

If generation is authorized separately, compare multiple takes with the same prompt, model, input material, identity controls, and slider settings. Change one factor at a time. Record model, mode, settings, source/take IDs, observed duration, and listening results with the relevant snapshot.

Test section-cue adherence, wordless voice without invented lyrics, lyric pronunciation, unwanted choir, edit preservation, and loop joins. Treat ratings as observations for those takes, not universal causal rules. Establish a generation/credit budget before an automated experiment; this plugin itself has no generation loop.
