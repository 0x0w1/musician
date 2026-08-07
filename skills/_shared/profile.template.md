# Suno Profile

Copied to `~/.claude/suno/profile.md` on first run. Edit freely — the skills read this every time.

This file is the one place personal taste lives. Everything else in the plugin is neutral rules, so handing the skills to someone else means handing them a different copy of this file.

```yaml
# Which Suno version to target. Supported: v4.5 | v5 | v5.5
version: v5.5

# Suno plan. Determines whether the Exclude Styles field exists.
# pro | premier  -> dedicated Exclude field
# free | basic   -> falls back to inline "no X" in Styles
plan: pro

# Default lyric language, as an English name (Korean, Japanese, English, ...).
# A genre that implies a language overrides this — J-Pop wins over a Korean default.
default_lyric_language: Korean

# Append an English translation under non-English lyrics, for proofreading.
translate_non_english: true

paths:
  profile: ~/.claude/suno/profile.md
  songs: ~/.claude/suno/songs
```

## Taste defaults

Free text. The skills read this as soft preference — an explicit request in the prompt always outranks it. Leave a line blank to express no preference.

- **Preferred genres:**
- **Genres to avoid:**
- **Default vocal character:**
- **Instruments you gravitate toward:**
- **Instruments you dislike:**
- **Production character:** _(e.g. warm analog, dry and close, wide and spacious)_
- **Typical BPM range:**
- **Always exclude:** _(goes into Exclude Styles priority 1 on every song)_
- **Lyrical themes to avoid:**
