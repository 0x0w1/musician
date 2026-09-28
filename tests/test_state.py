import argparse
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("song_state", ROOT / "references/scripts/song_state.py")
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)


class SongStateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.candidate = self.root / "candidate.json"
        self.data = json.loads((ROOT / "references/examples.json").read_text())[0]

    def run_command(self, command, **kwargs):
        args = dict(root=str(self.root / "state"), command=command, slug="test-track",
                    input=str(self.candidate), request="test", revision=None, text="heard it", source=None)
        args.update(kwargs)
        return state.run(argparse.Namespace(**args))

    def save(self, data=None):
        self.candidate.write_text(json.dumps(data or self.data, ensure_ascii=False))
        return self.run_command("save")

    def record(self):
        return json.loads((self.root / "state/songs/test-track.json").read_text())

    def test_all_examples_are_complete(self):
        for data in json.loads((ROOT / "references/examples.json").read_text()):
            state.validate_data(data)

    def test_targeted_change_restores_exact_text_and_preserves_feedback(self):
        self.save()
        self.run_command("outcome", text="합창이 계속 껴", source="take-1")
        changed = deepcopy(self.data)
        changed["slots"]["bpm"] = 105
        changed["fields"]["styles"]["value"] = changed["fields"]["styles"]["value"].replace("78 BPM", "105 BPM")
        self.save(changed)
        self.assertEqual(self.run_command("show")["lyrics"], self.data["lyrics"])
        self.run_command("restore", revision=1)
        self.assertEqual(self.run_command("show"), self.data)
        self.assertEqual(self.record()["outcomes"][0]["revision"], 1)
        self.assertEqual(self.record()["snapshots"][2]["restored_from"], 1)

    def test_feedback_does_not_create_revision(self):
        self.save()
        self.run_command("outcome", text="All four takes were good")
        self.assertEqual(len(self.record()["snapshots"]), 1)
        self.assertEqual(self.run_command("show"), self.data)

    def test_instrumental_sections_survive_restore(self):
        data = json.loads((ROOT / "references/examples.json").read_text())[1]
        self.save(data)
        changed = deepcopy(data)
        changed["sections"] = ["Theme", "Outro"]
        changed["fields"]["sections"]["value"] = changed["sections"]
        self.save(changed)
        self.run_command("restore", revision=1)
        self.assertEqual(self.run_command("show")["sections"], data["sections"])

    def test_invalid_candidate_leaves_history_unchanged(self):
        self.save()
        before = self.record()
        bad = deepcopy(self.data)
        bad["fields"]["weirdness"]["value"] = 101
        with self.assertRaises(ValueError):
            self.save(bad)
        self.assertEqual(self.record(), before)

    def test_invalid_revision_does_not_write(self):
        self.save()
        before = self.record()
        with self.assertRaises(ValueError):
            self.run_command("restore", revision=99)
        self.assertEqual(self.record(), before)

    def test_existing_lock_refuses_writer(self):
        self.save()
        lock = self.root / "state/songs/test-track.lock"
        lock.write_text("other writer")
        with self.assertRaises(FileExistsError):
            self.run_command("outcome")
        self.assertEqual(lock.read_text(), "other writer")

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            self.run_command("save", slug="../outside")

    def test_state_inside_plugin_is_rejected(self):
        with self.assertRaises(ValueError):
            self.run_command("save", root=str(ROOT / "state"))

    def test_translation_and_lyrics_are_separate(self):
        data = deepcopy(self.data)
        data["translation"] = "Slowly, I begin again."
        data["fields"]["translation"] = {"status": "set", "value": data["translation"], "note": "Review only"}
        self.save(data)
        self.assertEqual(self.run_command("show")["lyrics"], self.data["lyrics"])
        self.assertNotIn(data["translation"], self.run_command("show")["fields"]["lyrics"]["value"])

    def test_contradictory_vocal_toggle_is_rejected(self):
        data = deepcopy(self.data)
        data["fields"]["instrumental"]["value"] = "ON"
        with self.assertRaises(ValueError):
            state.validate_data(data)

    def test_legacy_markdown_is_not_overwritten(self):
        songs = self.root / "state/songs"
        songs.mkdir(parents=True)
        legacy = songs / "test-track.md"
        legacy.write_text("legacy song without recoverable earlier values")
        self.save()
        self.assertEqual(legacy.read_text(), "legacy song without recoverable earlier values")


if __name__ == "__main__":
    unittest.main()
