import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install_antigravity.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "plugin.json").write_text(json.dumps({"name": installer.NAME}))
        (self.source / "VERSION").write_text("0.3.0\n")
        (self.source / "skill.txt").write_text("first version")
        self.parent = self.root / "workspace/.agents/plugins"
        self.target = self.parent / installer.NAME

    def install(self):
        return installer.install(self.parent, self.source)

    def test_repeat_install_is_idempotent(self):
        self.assertEqual(self.install()["status"], "installed")
        self.assertEqual(self.install()["status"], "unchanged")

    def test_upgrade_preserves_user_additions_and_backup(self):
        self.install()
        (self.target / "personal.txt").write_text("keep me")
        (self.source / "skill.txt").write_text("second version")
        result = self.install()
        self.assertEqual((self.target / "personal.txt").read_text(), "keep me")
        self.assertEqual((self.target / "skill.txt").read_text(), "second version")
        self.assertEqual((Path(result["backup"]) / "skill.txt").read_text(), "first version")
        self.assertNotEqual(Path(result["backup"]).parent, self.target.parent)

    def test_modified_managed_file_is_not_overwritten(self):
        self.install()
        (self.target / "skill.txt").write_text("my edit")
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual((self.target / "skill.txt").read_text(), "my edit")

    def test_unknown_directory_is_not_overwritten(self):
        self.target.mkdir(parents=True)
        (self.target / "personal.txt").write_text("not yours")
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual((self.target / "personal.txt").read_text(), "not yours")

    def test_new_payload_does_not_overwrite_user_added_path(self):
        self.install()
        (self.target / "personal.txt").write_text("mine")
        (self.source / "personal.txt").write_text("upstream")
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual((self.target / "personal.txt").read_text(), "mine")

    def test_symlink_target_is_rejected(self):
        self.parent.mkdir(parents=True)
        self.target.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.install()


if __name__ == "__main__":
    unittest.main()
