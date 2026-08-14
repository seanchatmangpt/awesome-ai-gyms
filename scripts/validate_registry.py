#!/usr/bin/env python3
"""Validate the canonical DFCM gym registry without third-party dependencies."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "gyms.tsv"
CONTRACT = ROOT / "registry" / "contract.json"
SOURCES = ROOT / "registry" / "sources.lock.json"

KINDS = {"environment", "benchmark", "simulator", "framework", "infrastructure"}
MODES = {"train", "eval"}
COLUMNS = ["name", "canonical_url", "category", "kind", "modes", "tags", "provenance"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(path: Path = REGISTRY) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"REGISTRY_COLUMNS:{reader.fieldnames!r}")
        rows = []
        for raw in reader:
            row = dict(raw)
            row["modes"] = [value for value in row["modes"].split(",") if value]
            row["tags"] = [value for value in row["tags"].split(",") if value]
            row["provenance"] = [value for value in row["provenance"].split(",") if value]
            rows.append(row)
        return rows


def validate(entries: list[dict], contract: dict, sources_doc: dict) -> list[str]:
    errors: list[str] = []
    source_codes = {source.get("code") for source in sources_doc.get("sources", [])}

    for field, values in {
        "URL": [entry.get("canonical_url") for entry in entries],
        "NAME_URL": [(entry.get("name"), entry.get("canonical_url")) for entry in entries],
    }.items():
        for value, count in Counter(values).items():
            if count > 1:
                errors.append(f"DUPLICATE_{field}:{value}")

    if contract.get("entry_count") != len(entries):
        errors.append(f"ENTRY_COUNT_DRIFT:{contract.get('entry_count')}!={len(entries)}")

    defaults = contract.get("entry_defaults", {})
    dfcm = defaults.get("dfcm", {})
    if defaults.get("standing") != "UNKNOWN":
        errors.append("DEFAULT_STANDING_MUST_BE_UNKNOWN")
    if dfcm.get("authority") != "NONE":
        errors.append("CATALOG_AUTHORITY_MUST_BE_NONE")
    if dfcm.get("admission") != "CANDIDATE_ONLY":
        errors.append("CATALOG_MUST_NOT_ADMIT")
    if dfcm.get("actuation") != "FORBIDDEN_FROM_CATALOG":
        errors.append("CATALOG_MUST_NOT_ACTUATE")
    if defaults.get("autofde_lab", {}).get("authority") != "SELECT_ONLY":
        errors.append("AUTOFDE_MUST_BE_SELECT_ONLY")
    if defaults.get("gymact", {}).get("stage") != "candidate":
        errors.append("GYMACT_STAGE_MUST_BE_CANDIDATE")

    for index, entry in enumerate(entries):
        prefix = f"ENTRY[{index}]"
        if not entry["name"]:
            errors.append(f"{prefix}:EMPTY_NAME")
        parsed = urlparse(entry["canonical_url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{prefix}:BAD_URL:{entry['canonical_url']}")
        if entry["kind"] not in KINDS:
            errors.append(f"{prefix}:BAD_KIND:{entry['kind']}")
        if not set(entry["modes"]).issubset(MODES):
            errors.append(f"{prefix}:BAD_MODE")
        unknown = set(entry["provenance"]) - source_codes
        if unknown:
            errors.append(f"{prefix}:UNKNOWN_SOURCE:{','.join(sorted(unknown))}")
        if not entry["provenance"]:
            errors.append(f"{prefix}:NO_PROVENANCE")

    for source in sources_doc.get("sources", []):
        if not source.get("commit_sha") or len(source["commit_sha"]) != 40:
            errors.append(f"SOURCE_NOT_PINNED:{source.get('id')}")
        if not source.get("code"):
            errors.append(f"SOURCE_CODE_MISSING:{source.get('id')}")

    return errors


def main() -> int:
    entries = load_registry()
    contract = load_json(CONTRACT)
    sources = load_json(SOURCES)
    errors = validate(entries, contract, sources)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"REGISTRY_ALIVE entries={len(entries)} authority=NONE "
        "actuation=FORBIDDEN_FROM_CATALOG"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
