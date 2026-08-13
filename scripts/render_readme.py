#!/usr/bin/env python3
"""Render the public Awesome list from canonical TSV registry + pinned provenance."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from validate_registry import load_registry

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def render(root: Path = ROOT) -> str:
    entries = load_registry(root / "registry" / "gyms.tsv")
    contract = load_json(root / "registry" / "contract.json")
    sources_doc = load_json(root / "registry" / "sources.lock.json")
    source_by_code = {source["code"]: source for source in sources_doc["sources"]}

    by_category: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        by_category[entry["category"]].append(entry)
    kind_counts = Counter(entry["kind"] for entry in entries)

    lines = [
        "# Awesome AI Gyms",
        "",
        "**The discovery registry for AI gyms — feeding AutoFDE-Lab for selection/planning and GymAct for lawful execution.**",
        "",
        "## Upstream acknowledgements & provenance",
        "",
        "This project begins with the excellent community curation below. **Please star, cite, and contribute upstream.** "
        "We normalize factual metadata and canonical links rather than copying upstream descriptions. "
        "Every row in [`registry/gyms.tsv`](registry/gyms.tsv) carries source codes resolved by the exact-commit lock in [`registry/sources.lock.json`](registry/sources.lock.json).",
        "",
    ]
    for source in sources_doc["sources"]:
        commit_url = f"{source['url']}/tree/{source['commit_sha']}"
        lines.append(
            f"- [{source['name']}]({source['url']}) — "
            f"[{source['commit_sha'][:12]}]({commit_url}) — `{source['code']}`"
        )

    lines += [
        "",
        "## DFCM product topology",
        "",
        "```text",
        "upstream lists/repos",
        "        │",
        "        ▼",
        " awesome-ai-gyms",
        " DISCOVER + PRESERVE",
        " authority = NONE",
        "        │",
        "        ▼",
        "   AutoFDE-Lab",
        "   SELECT + PLAN",
        " authority = SELECT_ONLY",
        "        │",
        "        ▼",
        "      GymAct",
        " ADMIT → MATERIALIZE → OBSERVE → BRCE DO → VERIFY → RECEIPT/REPLAY",
        "```",
        "",
        "DFCM rule: preserve the maximum reversible lawful possibility graph before irreversible selection. "
        "Catalog membership is **not** installation, compatibility, admission, authority, execution, or proof. "
        "Planner compatibility starts `UNKNOWN`; one refused edge narrows topology rather than collapsing the graph.",
        "",
        "### Standing",
        "",
        f"- Registry: `{contract['standing']}`",
        f"- Candidates: **{len(entries)}** across **{len(by_category)}** categories",
        f"- Candidate default: `{contract['entry_defaults']['standing']}`",
        "- Awesome AI Gyms authority: `NONE`",
        "- AutoFDE-Lab authority from this feed: `SELECT_ONLY`",
        "- Gym execution: GymAct only, after its own admission; no catalog row auto-registers a provider",
        "",
        "### Kind coverage",
        "",
    ]
    for kind, count in sorted(kind_counts.items()):
        lines.append(f"- `{kind}`: {count}")

    lines += [
        "",
        "## Machine interface",
        "",
        "- [`registry/gyms.tsv`](registry/gyms.tsv) — canonical candidate set.",
        "- [`registry/contract.json`](registry/contract.json) — DFCM/default-standing contract.",
        "- [`schema/awesome-ai-gym.schema.json`](schema/awesome-ai-gym.schema.json) — normalized candidate record schema.",
        "- [`scripts/crawl_upstreams.py`](scripts/crawl_upstreams.py) — exact-pinned DISCOVER crawler; emits a review inbox and never mutates the canonical registry.",
        "- GymAct and AutoFDE-Lab each own a typed adapter over this registry; product semantics are not duplicated here.",
        "",
        "Verify: `python scripts/render_readme.py && python scripts/validate_registry.py && python -m unittest discover -s tests -v`.",
        "",
        "## Catalog",
        "",
    ]

    for category in sorted(by_category):
        group = sorted(by_category[category], key=lambda item: item["name"].casefold())
        lines.append(f"### {category.replace('-', ' ').title()} ({len(group)})")
        lines.append("")
        lines.append(" · ".join(
            f"[{entry['name']}]({entry['canonical_url']})" for entry in group
        ))
        lines.append("")

    lines += [
        "## Contribution law",
        "",
        "Increase the reversible lawful graph without manufacturing standing. Preserve provenance; keep unknowns unknown; "
        "do not mark a gym ALIVE from documentation, importability, CI metadata, popularity, or an upstream benchmark claim. "
        "See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    text = render(ROOT)
    (ROOT / "README.md").write_text(text, encoding="utf-8")
    print(f"README_ALIVE entries={len(load_registry(ROOT / 'registry' / 'gyms.tsv'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
