# Musician Profile

Preferences are soft defaults. Explicit requests take precedence. State path resolution and legacy aliases are described in [state-and-revisions.md](state-and-revisions.md).

```yaml
schema_version: 1
plan: unknown # free | pro | premier | unknown; retain unfamiliar plans as unknown access
model: auto # v6 | v6-wild | v6-mini, or an explicitly requested historical target
mode: auto # custom | simple | edit
lyric_language: auto
translation_language: English
translate_lyrics: false
variety: 0 # suggestion for preserving authored styles, if the control exists
max_mode: false
voice: null
style_persona: null
custom_model: null
personalize: unknown
# Optional absolute paths. Existing legacy `paths` are honored.
paths: {}
```

## Taste defaults

- Preferred genres:
- Genres to avoid:
- Default vocal character:
- Preferred instruments:
- Instruments to avoid:
- Production character:
- Typical tempo or groove:
- Preferred exclusions:
- Lyrical themes to avoid:

Legacy `version` maps to the model preference and `default_lyric_language` maps to lyric language. `translate_non_english` remains a translation preference, but translations are always separate from Suno lyrics. Legacy taste headings remain readable. Do not reset an existing profile just to adopt this template.
