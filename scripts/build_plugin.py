#!/usr/bin/env python3
"""Build or check the shared three-host plugin payload. Python 3.9+."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "suno-music-skills"


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def payload():
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    codex = {key: value for key, value in manifest.items() if key != "skills"}
    codex["skills"] = "./skills/"
    codex["interface"] = {
        "displayName": "Musician",
        "shortDescription": "Suno songs, instrumentals, and editing prompts",
        "longDescription": "Prepare complete Suno handoffs for vocal and instrumental music, revise existing songs, and retain full prompt history. Audio generation remains in Suno.",
        "developerName": manifest["author"]["name"],
        "category": "Productivity",
        "capabilities": ["Write"],
        "websiteURL": manifest["repository"],
        "defaultPrompt": ["Write a Korean song about starting again.", "Make an instrumental for reading at dawn.", "Revise only the chorus of my Suno song."]
    }
    result = {
        ".claude-plugin/plugin.json": json_bytes(manifest),
        ".codex-plugin/plugin.json": json_bytes(codex),
        "plugin.json": json_bytes({"name": NAME, "description": manifest["description"]}),
        "VERSION": (manifest["version"] + "\n").encode(),
        "LICENSE": (ROOT / "LICENSE").read_bytes(),
    }
    for path in sorted([*(ROOT / "skills").rglob("*"), *(ROOT / "references").rglob("*")]):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            if path.is_symlink():
                raise ValueError("Unexpected source symlink: " + str(path))
            result[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    return result


def build(check=False):
    destination = ROOT / "plugins" / NAME
    expected = payload()
    actual = {p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file()}
    extras = actual - expected.keys()
    if extras:
        raise ValueError("Unexpected payload files; inspect before removal: " + ", ".join(sorted(extras)))
    changed = []
    for relative, contents in expected.items():
        target = destination / relative
        if target.is_symlink():
            raise ValueError("Unexpected payload symlink: " + relative)
        if not target.exists() or target.read_bytes() != contents:
            changed.append(relative)
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(contents)
    if check and changed:
        raise ValueError("Stale payload: " + ", ".join(changed))
    print(("Verified" if check else "Built") + " %d plugin files" % len(expected))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    try:
        build(parser.parse_args().check)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")
