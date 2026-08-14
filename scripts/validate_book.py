#!/usr/bin/env python3
from pathlib import Path
import re
import sys

repo = Path(__file__).resolve().parents[1]
book = repo / "book"
src = book / "src"
summary = src / "SUMMARY.md"

errors = []

if not (book / "book.toml").is_file():
    errors.append("missing book/book.toml")
if not summary.is_file():
    errors.append("missing book/src/SUMMARY.md")

summary_text = summary.read_text(encoding="utf-8") if summary.is_file() else ""
links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", summary_text)
for rel in links:
    target = src / rel
    if not target.is_file():
        errors.append(f"SUMMARY target missing: {rel}")

pattern_files = sorted((src / "patterns").glob("*.md"))
pattern_text = "\n".join(p.read_text(encoding="utf-8") for p in pattern_files)
headings = re.findall(r"^##\s+(\d+)\.\s+(.+)$", pattern_text, re.MULTILINE)
numbers = sorted(int(n) for n, _ in headings)

if numbers != list(range(1, 65)):
    errors.append(f"pattern numbering must be exactly 1..64; got {numbers}")

required_fields = [
    "**Context.**",
    "**Problem.**",
    "**Forces.**",
    "**Therefore:**",
    "**Consequences.**",
    "**Falsifier.**",
    "**Evidence.**",
    "**Connects to.**",
]
for path in pattern_files:
    text = path.read_text(encoding="utf-8")
    count = len(re.findall(r"^##\s+\d+\.", text, re.MULTILINE))
    for field in required_fields:
        actual = text.count(field)
        if actual != count:
            errors.append(f"{path.relative_to(repo)}: {field} count {actual}, expected {count}")

if errors:
    print("book validation FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"book validation OK: {len(pattern_files)} pattern chapters, {len(numbers)} patterns, {len(links)} SUMMARY entries")
