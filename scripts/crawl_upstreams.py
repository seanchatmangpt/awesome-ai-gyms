#!/usr/bin/env python3
"""Discover candidate GitHub repositories from exact-pinned upstream lists.

This is intentionally a DISCOVER operation. It does not edit registry/gyms.tsv,
install dependencies, import candidate packages, or grant execution authority.
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[^\s)>\]\"']*)?")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def load_sources() -> list[dict]:
    doc = json.loads((ROOT / "registry" / "sources.lock.json").read_text())
    return doc["sources"]


def raw_readme(source: dict) -> str:
    owner_repo = source["url"].removeprefix("https://github.com/").rstrip("/")
    url = f"https://raw.githubusercontent.com/{owner_repo}/{source['commit_sha']}/README.md"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "awesome-ai-gyms-dfcm-discovery/1"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def normalize_repo_url(url: str) -> str | None:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc.lower() != "github.com" or len(parts) < 2:
        return None
    if parts[0].lower() in {"sponsors", "features", "topics"}:
        return None
    return f"https://github.com/{parts[0]}/{parts[1].removesuffix('.git')}"


def discover(source: dict) -> list[dict]:
    current_heading = "unclassified"
    found: dict[str, dict] = {}
    for line in raw_readme(source).splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            current_heading = re.sub(r"\s+", " ", heading.group(2)).strip()
        for match in LINK_RE.finditer(line):
            canonical = normalize_repo_url(match.group(0))
            if canonical is None or canonical == source["url"]:
                continue
            found.setdefault(
                canonical.lower(),
                {
                    "canonical_url": canonical,
                    "source_id": source["id"],
                    "source_commit": source["commit_sha"],
                    "source_section": current_heading,
                    "standing": "UNKNOWN",
                    "authority": "NONE",
                    "admission": "REVIEW_REQUIRED",
                },
            )
    return sorted(found.values(), key=lambda item: item["canonical_url"].lower())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    allowed = set(args.source)
    sources = [s for s in load_sources() if not allowed or s["id"] in allowed]
    merged: dict[str, dict] = {}
    for source in sources:
        for candidate in discover(source):
            key = candidate["canonical_url"].lower()
            existing = merged.get(key)
            if existing is None:
                candidate["provenance"] = [{
                    "source_id": candidate.pop("source_id"),
                    "source_commit": candidate.pop("source_commit"),
                    "source_section": candidate.pop("source_section"),
                }]
                merged[key] = candidate
            else:
                existing["provenance"].append({
                    "source_id": candidate["source_id"],
                    "source_commit": candidate["source_commit"],
                    "source_section": candidate["source_section"],
                })

    document = {
        "schema": "awesome-ai-gyms/discovery-inbox@1",
        "semantics": {
            "standing": "UNKNOWN",
            "authority": "NONE",
            "canonical_registry_mutation": False,
        },
        "candidates": sorted(merged.values(), key=lambda item: item["canonical_url"].lower()),
    }
    text = json.dumps(document, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
