# Installation

## Requirements

Use a host version that supports its documented plugin commands. Python 3.9+ is needed for song snapshot helpers and the Antigravity IDE installer; prompt-only use needs no Python and no API key. Suno access is separate from this plugin. No third-party Suno API is required.

The shared bundle is `plugins/suno-music-skills/`. It includes `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and Antigravity's root `plugin.json`. All three use the same two skills and packaged reference files. Antigravity's manifest schema has no version field, so its bundle version is recorded in `VERSION`.

## Codex

```bash
codex plugin marketplace add 0x0w1/musician
codex plugin add suno-music-skills@musician
```

For local development, register the checkout path instead of the Git source, then use the same add command:

```bash
codex plugin marketplace add /absolute/path/to/musician
codex plugin add suno-music-skills@musician
```

The repository marketplace is `.agents/plugins/marketplace.json`; Codex resolves the bundle from the repository root. Start a new thread to load the skills. Use natural language or select the namespaced skill from the host's skill picker.

Update a Git-backed installation:

```bash
codex plugin marketplace upgrade musician
codex plugin add suno-music-skills@musician
```

## Claude Code

```bash
claude plugin marketplace add 0x0w1/musician
claude plugin install suno-music-skills@musician
```

Replace the GitHub source with `/absolute/path/to/musician` for a local checkout. Commands default to user scope. Add `--scope project` to the add/install commands for project scope. Session equivalents are `/plugin marketplace add ...` and `/plugin install suno-music-skills@musician`.

Explicit calls are `/suno-music-skills:suno-vocal-song` and `/suno-music-skills:suno-instrumental`; ordinary requests can also select the relevant skill.

To update:

```bash
claude plugin marketplace update musician
claude plugin update suno-music-skills@musician
```

Use the installed scope if it differs from the default. Run `/reload-plugins` or start a new session after updating. The plugin name is unchanged from v0.2.0.

## Antigravity CLI

From a checkout of this repository:

```bash
agy plugin install ./plugins/suno-music-skills
agy plugin list
```

The CLI stages the bundle under `~/.gemini/antigravity-cli/plugins/`. Use the host's plugin manager for subsequent updates and inspect the installed version's help rather than assuming IDE installation paths apply to the CLI. [Official plugin documentation](https://www.antigravity.google/docs/plugins?tab=ide)

## Antigravity IDE / 2.0

The IDE discovers workspace plugins in `.agents/plugins/` and global plugins in `~/.gemini/config/plugins/`. From this checkout, use the installer:

```bash
python3 scripts/install_antigravity.py --scope project --project /absolute/path/to/your-project
```

For all workspaces:

```bash
python3 scripts/install_antigravity.py --scope global
```

The installer copies the whole bundle. Re-run it from the updated checkout to update. Repeated identical installs do nothing; changed owned files are backed up under `.musician-backups/` beside the `plugins/` directory, outside plugin discovery. Locally modified managed files or conflicting user-added files cause a refusal instead of an overwrite. Nonconflicting user-added files survive updates. Backups are retained for user review.

Inspect active skills in Customizations and start a new session. The installer has been exercised in temporary directories; a live Antigravity application was not available during v0.3.0 validation.

## Shared user state

Resolve state from an explicit path or `MUSICIAN_HOME`, then an existing `~/.claude/suno/profile.md`, otherwise `~/.config/musician/`. Existing profile `paths` overrides remain usable. Every host uses this same resolution so song history is shared, not duplicated per host.

Profiles remain readable Markdown. New song histories are JSON files under `songs/`. Existing Markdown song files are preserved and imported when resumed. State is never stored in the plugin bundle. See [migration](migration.md).
