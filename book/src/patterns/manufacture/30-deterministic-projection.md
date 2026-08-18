# P30 · Deterministic Projection { #p30 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P30`

## Context

Canonical semantics must become files, models, tests, configs, or documentation.

## Problem

Probabilistic generation in the canonical path makes drift detection and replay ambiguous.

## Forces

- LLMs are useful at novelty boundaries.
- Canonical builds need reproducibility.
- Template engines can still hide nondeterministic ordering.

## Resolution

**Make canonical projection a deterministic function of admitted graph, pack version, template/projection version, and declared environment. Use probabilistic systems only to propose candidate semantic changes upstream.**

## Consequences

Regeneration becomes a verifier: unchanged inputs should produce unchanged outputs.

## Falsifier

Two runs with identical admitted inputs and toolchain identities produce different canonical artifacts without a declared nondeterministic field.

## Evidence contract

- [ ] input graph digest
- [ ] pack/toolchain versions
- [ ] output digest
- [ ] sync-twice equality

## Pattern graph

- [P25 · Ontology First](25-ontology-first.md)
- [P31 · Generated Is Canonical](31-generated-is-canonical.md)
- [P58 · Delete and Regenerate](../self-manufacturing/58-delete-and-regenerate.md)
