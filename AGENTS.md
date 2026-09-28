# Repository workflow

This repository adopts jig's `develop/main` workflow. Read `.jig/readme.md` when editing the README and `.jig/versioning.md` when grading a change, once that policy has been agreed.

Ordinary implementation requests authorize local edits and verification. Commit, landing, and release stages require the user’s request or explicit standing approval. A release request authorizes completing its pending changes through the develop-first flow before publication.

When landing is explicitly authorized, start from an up-to-date `origin/develop`, use a task branch, squash into `develop`, and push `develop` through jig. A release is a separately requested promotion to `main`. Resolve any `main` commits missing from `develop` before starting that flow.

Keep the English and Korean READMEs consistent. Preserve unrelated working-tree files. Use the upstream skill-creator guidance: concise triggers, a short entrypoint, and task-specific references loaded when needed.
