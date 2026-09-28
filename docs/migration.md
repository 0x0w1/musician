# Updating from v0.2.0

The package name remains `suno-music-skills` and both public skill names are unchanged. Update through the host's plugin mechanism described in [installation](installation.md). Codex and Antigravity are new installation targets.

## Preserved data

Existing `~/.claude/suno/profile.md` and Markdown song records are left in place. Profile keys `version`, `default_lyric_language`, `translate_non_english`, and `paths` remain readable. Do not copy user data into a plugin directory.

On resuming a legacy song, the agent reads its current fields and starts a JSON snapshot history next to the preserved Markdown file (or under its explicit path override). Unknown old values stay unknown. Future restores use full snapshots; changes that were never stored in v0.2.0 cannot be recovered retroactively.

## Behavior changes to review

- New generation recommendations use v6-family access. Old model names remain provenance or explicitly historical output targets.
- Explicit lyric language and then the profile take priority over genre. A Korean J-pop request stays Korean.
- Translation is always outside Lyrics. Legacy translation preferences are honored without putting the translation into the sung text.
- Sliders use 0–100 percent. Ambiguous legacy units are not guessed.
- Instrumentation, section counts, and prompt lengths are recommendations rather than universal hard caps.
- Output includes a complete field ledger with unavailable/unverified statuses. A field's presence in that ledger does not imply it exists in the current Suno mode.
- Voices, Style Personas, Custom Models, and Personalize remain optional account choices. Text descriptions do not recreate account resources.

No bulk profile rewrite or destructive migration is required. Generation behavior changes should be assessed in Suno with the desired model and settings.
