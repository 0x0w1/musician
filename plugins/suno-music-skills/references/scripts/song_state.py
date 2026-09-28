#!/usr/bin/env python3
"""Save full song snapshots, feedback, and exact restorations. Python 3.9+."""

import argparse
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile

FIELDS = (
    "requested_model source_model target_model availability mode vocal_state title "
    "prompt lyrics styles exclude_styles instrumental vocal_gender weirdness "
    "style_influence audio_influence variety max_mode voice style_persona "
    "custom_model personalize reference_inputs edit_target preserve sections "
    "target_duration translation"
).split()
STATUSES = {"set", "empty", "not_applicable", "unavailable", "unverified"}
SLIDERS = {"weirdness", "style_influence", "audio_influence", "variety"}


def now():
    return datetime.now(timezone.utc).isoformat()


def validate_data(data):
    if not isinstance(data, dict):
        raise ValueError("Song data must be an object")
    required = {"title", "skill", "concept", "source_model", "target_model", "mode",
                "vocal_state", "slots", "sections", "target_duration", "fields",
                "lyrics", "translation", "references", "assumptions"}
    if required - data.keys():
        raise ValueError("Missing song keys: " + ", ".join(sorted(required - data.keys())))
    if data["skill"] not in {"suno-vocal-song", "suno-instrumental"}:
        raise ValueError("Unknown skill")
    if data["mode"] not in {"custom", "simple", "edit"}:
        raise ValueError("Mode must be custom, simple, or edit")
    if data["vocal_state"] not in {"lyrics", "instrumental", "wordless"}:
        raise ValueError("Unknown vocal state")
    for key in ("title", "concept", "target_model", "lyrics", "translation"):
        if not isinstance(data[key], str):
            raise ValueError(key + " must be a string")
    for key in ("sections", "references", "assumptions"):
        if not isinstance(data[key], list):
            raise ValueError(key + " must be an array")
    if not isinstance(data["slots"], dict):
        raise ValueError("slots must be an object")
    fields = data["fields"]
    if not isinstance(fields, dict) or set(fields) != set(FIELDS):
        raise ValueError("fields must contain exactly the universal field ledger")
    for key, field in fields.items():
        if not isinstance(field, dict) or field.get("status") not in STATUSES:
            raise ValueError("Invalid status for " + key)
        if "value" not in field or not isinstance(field.get("note", ""), str):
            raise ValueError("Invalid field value/note for " + key)
        value = field["value"]
        if field["status"] in {"empty", "not_applicable", "unavailable"} and value is not None:
            raise ValueError("Inactive field must have null value: " + key)
        if field["status"] == "set" and value is None:
            raise ValueError("Set field needs a value: " + key)
        if key in SLIDERS and value is not None:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 100:
                raise ValueError(key + " must be 0–100 percent")
    for key in ("title", "source_model", "target_model", "mode", "vocal_state", "sections", "target_duration"):
        value = fields[key]["value"]
        if value is not None and value != data[key]:
            raise ValueError("Ledger disagrees with song data: " + key)
    for key in ("lyrics", "translation"):
        value = fields[key]["value"]
        if value is not None and value != data[key]:
            raise ValueError("Ledger disagrees with song text: " + key)
    if data["vocal_state"] == "instrumental" and fields["instrumental"]["value"] == "OFF":
        raise ValueError("Voice-free instrumental contradicts OFF")
    if data["vocal_state"] in {"lyrics", "wordless"} and fields["instrumental"]["value"] == "ON":
        raise ValueError("Vocal state contradicts Instrumental ON")


def read_record(path, slug):
    if path.is_symlink():
        raise ValueError("Refusing a symlink song record")
    if not path.exists():
        return {"schema_version": 1, "slug": slug, "snapshots": [], "outcomes": []}
    record = json.loads(path.read_text(encoding="utf-8"))
    if record.get("schema_version") != 1 or record.get("slug") != slug:
        raise ValueError("Unsupported or mismatched song record")
    if not isinstance(record.get("snapshots"), list) or not isinstance(record.get("outcomes"), list):
        raise ValueError("Malformed history")
    for i, snapshot in enumerate(record["snapshots"], 1):
        if snapshot.get("revision") != i:
            raise ValueError("Malformed revision sequence")
        validate_data(snapshot["data"])
    return record


@contextmanager
def lock(path):
    lock_path = path.with_suffix(".lock")
    fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.close(fd)
        yield
    finally:
        lock_path.unlink()


def atomic_write(path, record):
    fd, temporary = tempfile.mkstemp(prefix="." + path.stem + "-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(record, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def run(args):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        raise ValueError("Use a lowercase, hyphen-separated slug")
    root = Path(args.root).expanduser().resolve()
    plugin_root = next(parent for parent in Path(__file__).resolve().parents
                       if (parent / ".claude-plugin/plugin.json").is_file())
    if root == plugin_root or plugin_root in root.parents:
        raise ValueError("State must live outside the plugin directory")
    songs = root / "songs"
    if songs.is_symlink():
        raise ValueError("Refusing a symlink songs directory")
    path = songs / (args.slug + ".json")
    if args.command == "show":
        record = read_record(path, args.slug)
        if not record["snapshots"]:
            raise ValueError("No saved song")
        return record["snapshots"][-1]["data"]
    songs.mkdir(parents=True, exist_ok=True)
    with lock(path):
        record = read_record(path, args.slug)
        history = record["snapshots"]
        if args.command == "save":
            data = json.loads(Path(args.input).read_text(encoding="utf-8"))
            validate_data(data)
            history.append({"revision": len(history) + 1, "at": now(), "request": args.request, "data": data})
        elif args.command == "restore":
            if not 1 <= args.revision <= len(history):
                raise ValueError("Revision does not exist")
            data = deepcopy(history[args.revision - 1]["data"])
            history.append({"revision": len(history) + 1, "at": now(), "request": args.request,
                            "restored_from": args.revision, "data": data})
        else:
            revision = args.revision if args.revision is not None else len(history)
            if not 1 <= revision <= len(history):
                raise ValueError("Feedback needs an existing revision")
            record["outcomes"].append({"at": now(), "revision": revision, "text": args.text,
                                       "source": args.source})
        atomic_write(path, record)
    return {"path": str(path), "revision": len(history), "outcomes": len(record["outcomes"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Resolved user state root, outside the plugin")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("save", "show", "outcome", "restore"):
        command = commands.add_parser(name)
        command.add_argument("slug")
        if name == "save":
            command.add_argument("--input", required=True)
        if name in {"save", "restore"}:
            command.add_argument("--request", required=True)
        if name in {"restore", "outcome"}:
            command.add_argument("--revision", type=int, required=name == "restore")
        if name == "outcome":
            command.add_argument("--text", required=True)
            command.add_argument("--source")
    try:
        print(json.dumps(run(parser.parse_args()), ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, "song_state: " + str(error) + "\n")


if __name__ == "__main__":
    main()
