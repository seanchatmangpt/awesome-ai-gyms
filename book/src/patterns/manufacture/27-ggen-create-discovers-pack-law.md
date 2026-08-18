# P27 · ggen-create Discovers Pack Law { #p27 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P27`

## Context

A mature exemplar or external architecture exists and its reusable manufacturing law is not yet encoded as a ggen pack.

## Problem

Manual template authoring captures surface files but misses the deeper variables, invariants, and semantic relationships that make the exemplar reusable.

## Forces

- Exemplars contain accidental details.
- Several examples reveal variation better than one.
- Reverse engineering must not silently grant execution authority.

## Resolution

**Use ggen-create as the pack-authoring and reverse-compilation process: ingest exemplars, identify variables and invariants, derive candidate ontology/projections, and emit a candidate pack for qualification. It does not generate consumer projects.**

## Consequences

Existing systems become raw material for reusable manufacturing knowledge while preserving the separation between pack creation and ggen execution.

## Falsifier

The ggen-create output is treated as a finished consumer application or bypasses pack qualification.

## Evidence contract

- [ ] exemplar identities
- [ ] derived variables/invariants
- [ ] candidate pack
- [ ] qualification obligations

## Pattern graph

- [P26 · One Pack, One Manufacturing Boundary](26-one-pack-one-manufacturing-boundary.md)
- [P28 · Pack Gym](28-pack-gym.md)
- [P29 · Marketplace Qualification](29-marketplace-qualification.md)
