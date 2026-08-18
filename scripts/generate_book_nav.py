#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import re
from dataclasses import dataclass
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
src = repo / "book" / "src"

PREFIX = [
    ("Introduction", "introduction.md"),
    ("Pattern Grammar", "pattern-grammar.md"),
    ("DFCM Generative Sequence", "generative-sequence.md"),
]

FAMILIES = [
    ("I · Foundations", "foundations", "patterns/foundations.md"),
    ("II · Discovery and Composition", "discovery-composition", "patterns/discovery-composition.md"),
    ("III · Planning and Selection", "planning-selection", "patterns/planning-selection.md"),
    ("IV · Manufacture and Packs", "manufacture", "patterns/manufacture.md"),
    ("V · Execution and Safety", "execution-safety", "patterns/execution-safety.md"),
    ("VI · Evidence and Learning", "evidence-learning", "patterns/evidence-learning.md"),
    ("VII · Enterprise and Operations", "enterprise-operations", "patterns/enterprise-operations.md"),
    ("VIII · Self-Manufacturing Ecosystem", "self-manufacturing", "patterns/self-manufacturing.md"),
]

OPERATIONALIZATION = [
    ("Ecosystem Roles", "ecosystem-roles.md"),
    ("The `gym/` Convention", "gym-convention.md"),
    ("Gym Maturity Matrix", "maturity.md"),
]

SUFFIX = [
    ("Pattern Index", "pattern-index.md"),
    ("Glossary", "glossary.md"),
]

TITLE_RE = re.compile(r"^# P(?P<num>\d{2}) · (?P<title>.+?) \{ #p(?P=num) \}$", re.MULTILINE)
CONFIDENCE_RE = re.compile(r"^> \*\*Confidence:\*\* (?P<confidence>★{1,3}☆{0,2})\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Pattern:
    number: int
    title: str
    confidence: str
    relpath: str
    family: str
    family_path: str


def load_patterns() -> list[Pattern]:
    patterns: list[Pattern] = []
    for family, directory, family_path in FAMILIES:
        for path in sorted((src / "patterns" / directory).glob("*.md")):
            text = path.read_text(encoding="utf-8")
            title = TITLE_RE.search(text)
            confidence = CONFIDENCE_RE.search(text)
            if not title or not confidence:
                raise SystemExit(f"invalid pattern metadata: {path.relative_to(repo)}")
            patterns.append(
                Pattern(
                    number=int(title.group("num")),
                    title=title.group("title"),
                    confidence=confidence.group("confidence"),
                    relpath=path.relative_to(src).as_posix(),
                    family=family,
                    family_path=family_path,
                )
            )
    patterns.sort(key=lambda p: p.number)
    numbers = [p.number for p in patterns]
    if numbers != list(range(1, 65)):
        raise SystemExit(f"pattern numbering must be exactly 1..64; got {numbers}")
    return patterns


def render_summary(patterns: list[Pattern]) -> str:
    by_family = {directory: [] for _, directory, _ in FAMILIES}
    for pattern in patterns:
        directory = Path(pattern.relpath).parent.name
        by_family[directory].append(pattern)

    lines = ["# Summary", ""]
    for title, path in PREFIX:
        lines.append(f"[{title}]({path})")
    lines += ["", "# Pattern Language", ""]
    for family, directory, family_path in FAMILIES:
        lines.append(f"- [{family}]({family_path})")
        for pattern in by_family[directory]:
            lines.append(f"    - [P{pattern.number:02d} · {pattern.title}]({pattern.relpath})")
    lines += ["", "# Operationalization", ""]
    for title, path in OPERATIONALIZATION:
        lines.append(f"- [{title}]({path})")
    lines += ["", "---", ""]
    for title, path in SUFFIX:
        lines.append(f"[{title}]({path})")
    return "\n".join(lines) + "\n"


def render_index(patterns: list[Pattern]) -> str:
    lines = [
        "# Pattern Index",
        "",
        "All 64 patterns as first-class chapters. `Pxx` is the stable canonical identity; mdBook section numbers are only one navigational projection.",
        "",
        "| ID | Pattern | Confidence | Family |",
        "|:---:|---|:---:|---|",
    ]
    for pattern in patterns:
        lines.append(
            f"| P{pattern.number:02d} | [{pattern.title}]({pattern.relpath}) | {pattern.confidence} | [{pattern.family}]({pattern.family_path}) |"
        )
    return "\n".join(lines) + "\n"


def check_or_write(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return True
    if check:
        print(f"generated navigation drift: {path.relative_to(repo)}")
        print("".join(difflib.unified_diff(actual.splitlines(True), expected.splitlines(True), fromfile="actual", tofile="expected")))
        return False
    path.write_text(expected, encoding="utf-8")
    print(f"wrote {path.relative_to(repo)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate mdBook navigation projections from canonical pattern chapters.")
    parser.add_argument("--check", action="store_true", help="fail if generated navigation differs from checked-in projections")
    args = parser.parse_args()

    patterns = load_patterns()
    ok = True
    ok &= check_or_write(src / "SUMMARY.md", render_summary(patterns), args.check)
    ok &= check_or_write(src / "pattern-index.md", render_index(patterns), args.check)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
