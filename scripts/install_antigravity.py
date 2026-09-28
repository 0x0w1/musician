#!/usr/bin/env python3
"""Install the bundled plugin for Antigravity IDE/2.0 with ownership checks."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

NAME = "suno-music-skills"
MARKER = ".musician-installation.json"
SOURCE = Path(__file__).resolve().parents[1] / "plugins" / NAME


def inventory(root):
    result = {}
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError("Refusing symlink: " + str(path))
        if path.is_file() and path.name != MARKER:
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def install(parent, source=SOURCE):
    if not (source / "plugin.json").is_file():
        raise ValueError("Build the plugin first")
    parent = Path(parent).expanduser()
    if parent.is_symlink() or parent.parent.is_symlink():
        raise ValueError("Refusing symlink installation path")
    parent = parent.resolve()
    parent.mkdir(parents=True, exist_ok=True)
    target = parent / NAME
    if target.is_symlink():
        raise ValueError("Refusing symlink installation")
    incoming = inventory(source)
    extras = {}
    if target.exists():
        marker = target / MARKER
        if not marker.is_file() or marker.is_symlink():
            raise ValueError("Existing directory is not owned by this installer")
        saved = json.loads(marker.read_text())
        if saved.get("name") != NAME or saved.get("schema_version") != 1:
            raise ValueError("Invalid installation marker")
        actual = inventory(target)
        owned = saved.get("files")
        if not isinstance(owned, dict):
            raise ValueError("Invalid installation file inventory")
        for relative, digest in owned.items():
            if actual.get(relative) != digest:
                raise ValueError("Locally modified or missing plugin file: " + relative)
        extras = {p: digest for p, digest in actual.items() if p not in owned}
        if extras.keys() & incoming.keys():
            raise ValueError("Update conflicts with user-added plugin files")
        if owned == incoming:
            return {"status": "unchanged", "path": str(target)}
    stage = Path(tempfile.mkdtemp(prefix=".musician-stage-", dir=parent))
    backup = None
    try:
        shutil.copytree(source, stage, dirs_exist_ok=True)
        for relative in extras:
            dest = stage / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target / relative, dest)
        (stage / MARKER).write_text(json.dumps({"schema_version": 1, "name": NAME,
            "version": (source / "VERSION").read_text().strip(), "files": incoming}, indent=2) + "\n")
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup_root = parent.parent / ".musician-backups"
            if backup_root.is_symlink():
                raise ValueError("Refusing symlink backup directory")
            backup_root.mkdir(exist_ok=True)
            backup = backup_root / (NAME + ".bak-" + stamp)
            target.rename(backup)
        try:
            stage.rename(target)
        except OSError:
            if backup is not None:
                backup.rename(target)
            raise
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return {"status": "installed", "path": str(target), "backup": str(backup) if backup else None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=["project", "global"], default="project")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    args = parser.parse_args()
    parent = args.project / ".agents/plugins" if args.scope == "project" else Path.home() / ".gemini/config/plugins"
    try:
        print(json.dumps(install(parent), indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, "install_antigravity: " + str(error) + "\n")
