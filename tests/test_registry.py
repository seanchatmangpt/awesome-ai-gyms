from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATE = load_module("validate_registry", ROOT / "scripts" / "validate_registry.py")
RENDER = load_module("render_readme", ROOT / "scripts" / "render_readme.py")


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = VALIDATE.load_registry()
        cls.contract = json.loads((ROOT / "registry" / "contract.json").read_text())
        cls.sources = json.loads((ROOT / "registry" / "sources.lock.json").read_text())

    def test_registry_validates(self):
        self.assertEqual(
            [], VALIDATE.validate(self.entries, self.contract, self.sources)
        )

    def test_dfcm_preserves_large_candidate_surface(self):
        self.assertGreaterEqual(len(self.entries), 180)
        self.assertGreaterEqual(len({entry["category"] for entry in self.entries}), 15)

    def test_catalog_never_manufactures_authority(self):
        defaults = self.contract["entry_defaults"]
        self.assertEqual("UNKNOWN", defaults["standing"])
        self.assertEqual("NONE", defaults["dfcm"]["authority"])
        self.assertEqual("FORBIDDEN_FROM_CATALOG", defaults["dfcm"]["actuation"])
        self.assertEqual("SELECT_ONLY", defaults["autofde_lab"]["authority"])
        self.assertEqual("candidate", defaults["gymact"]["stage"])

    def test_every_entry_has_pinned_provenance(self):
        known = {source["code"] for source in self.sources["sources"]}
        for entry in self.entries:
            self.assertTrue(entry["provenance"])
            self.assertTrue(set(entry["provenance"]).issubset(known))

    def test_readme_is_deterministic(self):
        self.assertEqual((ROOT / "README.md").read_text(), RENDER.render(ROOT))

    def test_readme_credits_every_source_near_top(self):
        head = (ROOT / "README.md").read_text()[:8000]
        for source in self.sources["sources"]:
            self.assertIn(source["url"], head)


if __name__ == "__main__":
    unittest.main()
