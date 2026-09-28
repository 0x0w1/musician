# Contributing

Edit `skills/` and `references/`, not the generated bundle. The canonical package metadata is `.claude-plugin/plugin.json`. Codex metadata and the Antigravity marker are generated from it by `scripts/build_plugin.py`. Both marketplace catalogs resolve the same checked-in bundle.

```bash
python3 scripts/build_plugin.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

The tests use temporary directories and have no production or Suno access. Rebuild after changing a packaged reference or helper. Commit the generated bundle with its sources. Native Claude Code validation is `claude plugin validate plugins/suno-music-skills`; when available, also run the official Codex plugin-creator validator and skill-creator validators.

Follow [the repository workflow](../AGENTS.md) and keep [both READMEs](../.jig/readme.md) aligned. Ordinary changes are local until landing is authorized. Releases use jig's develop-first path and fast-forward promotion to main.

A permanent version rubric has not yet been adopted. For v0.3.0 the requested version is explicit and the release uses jig's missing-policy fallback; this does not silently adopt a lasting policy. Source and output contract changes must be described in migration documentation even during 0.x.
