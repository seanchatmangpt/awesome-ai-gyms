# P25 · Ontology First { #p25 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P25`

## Context

A project or pack has semantics that will be projected into code, configuration, tests, documentation, planning models, or gym scenarios.

## Problem

When those artifacts are authored independently, their definitions diverge and every change requires synchronized manual editing.

## Forces

- Ontologies require discipline.
- Not every implementation detail belongs in semantics.
- Generated projections must remain understandable.

## Resolution

**Author the stable domain relationships, constraints, identities, and capability contracts in a canonical graph first. Manufacture downstream artifacts as deterministic projections wherever practical.**

## Consequences

Semantic change becomes one graph change followed by regeneration instead of a documentation/API synchronization campaign.

## Falsifier

Two canonical artifacts disagree because their shared semantics were manually duplicated rather than projected from one admitted source.

## Evidence contract

- [ ] canonical graph
- [ ] validation shapes
- [ ] projection ownership
- [ ] generated artifact provenance

## Pattern graph

- [P30 · Deterministic Projection](30-deterministic-projection.md)
- [P31 · Generated Is Canonical](31-generated-is-canonical.md)
- [P19 · Planning Projection](../planning-selection/19-planning-projection.md)
