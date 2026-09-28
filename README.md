# musician

[한국어](README.ko.md) · [Installation](#installation) · [Usage](#usage) · [Documentation](docs/README.md)

Suno music skills packaged for Codex, Claude Code, and Antigravity.

## Introduction

Turn an idea into a vocal song or instrumental handoff with lyrics, prompts, exclusions, and model-aware settings. Revise a saved prompt, prepare an edit to an existing recording, and retain full snapshots for later restoration.

v0.3.0 supports handoffs for v6, v6-wild, and v6-mini, plus explicitly historical templates for earlier models. You paste the result into Suno; the plugin does not generate audio or spend credits itself.

## Installation

**Codex**

```bash
codex plugin marketplace add 0x0w1/musician
codex plugin add suno-music-skills@musician
```

**Claude Code**

```bash
claude plugin marketplace add 0x0w1/musician
claude plugin install suno-music-skills@musician
```

**Antigravity CLI** — from a checkout:

```bash
agy plugin install ./plugins/suno-music-skills
```

Antigravity IDE/2.0 uses a plugin directory installer. See [installation details](docs/installation.md) for that command, local checkout installation, updates, prerequisites, and state locations. Start a new agent session after installing.

## Usage

Ask in natural language:

```text
Make a Korean J-pop song about starting again, with a female lead.
Create a voice-free ambient instrumental for reading at dawn.
Change only the first chorus lyric in my existing Suno song.
```

Provide the source song or file for an audio edit. The handoff accounts for every field, distinguishing pasteable content from unavailable or unverified controls. Translations are separate from lyrics.

Report what you heard or request a focused change:

```text
All four takes added a choir. Keep the rest of the arrangement.
Restore the first saved version.
```

## Skills

| Skill | Purpose |
|---|---|
| `suno-vocal-song` | Songs with sung lyrics |
| `suno-instrumental` | Instrumentals and wordless textures |

## Documentation

- [Documentation home](docs/README.md)
- [Output templates and filled examples](references/output-templates.md)
- [Workflow and validation limits](docs/workflow.md)
- [Updating from v0.2.0](docs/migration.md)

## License

[Apache-2.0](LICENSE)
