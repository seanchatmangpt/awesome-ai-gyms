from __future__ import annotations

import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REF = (
    "seanchatmangpt/autofde-lab@"
    "a1da4d0a3b666f03d45f003647fa2df0146ff9f9:.gitmodules"
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class AutoFDEVendorInboxTests(unittest.TestCase):
    def test_vendor_graph_is_preserved_as_inert_discovery_evidence(self) -> None:
        catalog = read_tsv(ROOT / "registry" / "gyms.tsv")
        inbox = read_tsv(ROOT / "registry" / "inbox" / "autofde-lab-vendor.tsv")
        catalog_urls = {row["canonical_url"].rstrip("/") for row in catalog}

        self.assertEqual(52, len(inbox))
        self.assertEqual(52, len({row["canonical_url"] for row in inbox}))
        self.assertEqual(20, sum(row["catalog_relation"] == "MATCHED" for row in inbox))
        self.assertEqual(32, sum(row["catalog_relation"] == "NEW" for row in inbox))

        for row in inbox:
            expected = (
                "MATCHED"
                if row["canonical_url"].rstrip("/") in catalog_urls
                else "NEW"
            )
            self.assertEqual(expected, row["catalog_relation"])
            self.assertEqual("UNKNOWN", row["standing"])
            self.assertEqual("NONE", row["authority"])
            self.assertEqual(SOURCE_REF, row["source_ref"])


if __name__ == "__main__":
    unittest.main()
