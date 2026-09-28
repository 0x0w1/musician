#!/usr/bin/env python3
"""Check packaged links, metadata, fixtures, and source/payload parity."""

import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/build_plugin.py"), "--check"], check=True)
    bundle = ROOT / "plugins/suno-music-skills"
    manifests = [ROOT / ".claude-plugin/plugin.json", bundle / ".claude-plugin/plugin.json", bundle / ".codex-plugin/plugin.json"]
    for path in manifests:
        data = json.loads(path.read_text())
        assert data["name"] == "suno-music-skills", path
        assert data["version"] == "0.3.0", path
    assert (bundle / "VERSION").read_text().strip() == "0.3.0"
    ag = json.loads((bundle / "plugin.json").read_text())
    assert set(ag) == {"name", "description"} and ag["name"] == "suno-music-skills"
    for path in [ROOT / ".claude-plugin/marketplace.json", ROOT / ".agents/plugins/marketplace.json"]:
        catalog = json.loads(path.read_text())
        assert catalog["name"] == "musician"
        for entry in catalog["plugins"]:
            source = entry["source"]
            relative = source["path"] if isinstance(source, dict) else source
            assert (ROOT / relative).resolve() == bundle.resolve()
    docs = [ROOT / "README.md", ROOT / "README.ko.md", ROOT / "TESTING.md"]
    docs += list((ROOT / "docs").rglob("*.md")) + list((ROOT / "skills").rglob("*.md"))
    docs += list((ROOT / "references").rglob("*.md"))
    docs += list((bundle / "skills").rglob("*.md")) + list((bundle / "references").rglob("*.md"))
    for path in docs:
        for url in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" in url:
                continue
            relative, _, anchor = url.partition("#")
            target = path.parent / relative if relative else path
            assert target.exists(), (path, url)
            if anchor:
                headings = re.findall(r"^#+ (.+)$", target.read_text(), re.M)
                slugs = [re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-") for text in headings]
                assert anchor in slugs, (path, url)
    for base in [ROOT, bundle]:
        for path in (base / "skills").glob("*/SKILL.md"):
            name = re.search(r"^name: (.+)$", path.read_text(), re.M)
            assert name and name.group(1) == path.parent.name, path
    spec = importlib.util.spec_from_file_location("song_state", ROOT / "references/scripts/song_state.py")
    state = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(state)
    for data in json.loads((ROOT / "references/examples.json").read_text()):
        state.validate_data(data)
    print("Metadata, source and installed links, skill names, and full-ledger fixtures passed")


if __name__ == "__main__":
    main()
