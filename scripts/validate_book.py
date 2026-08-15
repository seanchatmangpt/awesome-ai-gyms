#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys

repo = Path(__file__).resolve().parents[1]
book = repo / "book"
src = book / "src"
summary = src / "SUMMARY.md"
patterns_root = src / "patterns"

errors: list[str] = []

if not (book / "book.toml").is_file():
    errors.append("missing book/book.toml")
if not summary.is_file():
    errors.append("missing book/src/SUMMARY.md")

summary_text = summary.read_text(encoding="utf-8") if summary.is_file() else ""
summary_links = re.findall(r"\[[^\]]+\]\(([^)#]+\.md)(?:#[^)]+)?\)", summary_text)
for rel in summary_links:
    target = src / rel
    if not target.is_file():
        errors.append(f"SUMMARY target missing: {rel}")

for rel, count in Counter(summary_links).items():
    if count != 1:
        errors.append(f"SUMMARY target must appear exactly once: {rel} appears {count} times")

family_files = sorted(patterns_root.glob("*.md"))
if len(family_files) != 8:
    errors.append(f"expected 8 family map chapters, got {len(family_files)}")
for path in family_files:
    text = path.read_text(encoding="utf-8")
    if re.search(r"^##\s+\d+\.", text, re.MULTILINE):
        errors.append(f"{path.relative_to(repo)} still embeds pattern bodies; family files must be maps")

pattern_files = sorted(patterns_root.glob("*/*.md"))
if len(pattern_files) != 64:
    errors.append(f"expected 64 first-class pattern chapters, got {len(pattern_files)}")

required_headings = [
    "## Context",
    "## Problem",
    "## Forces",
    "## Resolution",
    "## Consequences",
    "## Falsifier",
    "## Evidence contract",
    "## Pattern graph",
]

title_re = re.compile(r"^# P(?P<num>\d{2}) · (?P<title>.+?) \{ #p(?P<anchor>\d{2}) \}$", re.MULTILINE)
confidence_re = re.compile(r"^> \*\*Confidence:\*\* (★{1,3}☆{0,2})\s*$", re.MULTILINE)
ids: list[int] = []
leaf_relpaths: list[str] = []

for path in pattern_files:
    text = path.read_text(encoding="utf-8")
    match = title_re.search(text)
    if not match:
        errors.append(f"{path.relative_to(repo)}: missing canonical Pxx title/anchor")
        continue
    number = int(match.group("num"))
    anchor = int(match.group("anchor"))
    ids.append(number)
    leaf_relpaths.append(path.relative_to(src).as_posix())
    if number != anchor:
        errors.append(f"{path.relative_to(repo)}: title ID P{number:02d} != anchor p{anchor:02d}")
    if not path.name.startswith(f"{number:02d}-"):
        errors.append(f"{path.relative_to(repo)}: filename must start with {number:02d}-")
    if f"> **Canonical ID:** `P{number:02d}`" not in text:
        errors.append(f"{path.relative_to(repo)}: canonical ID metadata mismatch")
    if not confidence_re.search(text):
        errors.append(f"{path.relative_to(repo)}: missing confidence metadata")
    for heading in required_headings:
        if text.count(heading) != 1:
            errors.append(f"{path.relative_to(repo)}: {heading} count {text.count(heading)}, expected 1")

    local_links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)", text)
    if not local_links:
        errors.append(f"{path.relative_to(repo)}: pattern graph has no links")
    for rel in local_links:
        target = (path.parent / rel).resolve()
        try:
            target.relative_to(src.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(repo)}: link escapes book source: {rel}")
            continue
        if not target.is_file():
            errors.append(f"{path.relative_to(repo)}: broken local markdown link: {rel}")

if sorted(ids) != list(range(1, 65)):
    errors.append(f"pattern IDs must be exactly P01..P64; got {sorted(ids)}")
if len(ids) != len(set(ids)):
    errors.append("pattern IDs must be unique")

summary_leaf_links = [rel for rel in summary_links if re.fullmatch(r"patterns/[^/]+/\d{2}-.+\.md", rel)]
if set(summary_leaf_links) != set(leaf_relpaths):
    missing = sorted(set(leaf_relpaths) - set(summary_leaf_links))
    extra = sorted(set(summary_leaf_links) - set(leaf_relpaths))
    if missing:
        errors.append(f"patterns missing from SUMMARY: {missing}")
    if extra:
        errors.append(f"non-canonical pattern leaves in SUMMARY: {extra}")
if len(summary_leaf_links) != 64:
    errors.append(f"SUMMARY must contain exactly 64 leaf pattern chapters; got {len(summary_leaf_links)}")

if errors:
    print("book validation FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "book validation OK: "
    f"{len(family_files)} families, {len(pattern_files)} first-class patterns, "
    f"{len(summary_links)} unique SUMMARY chapters"
)
