# P22 · Constraint Fence { #p22 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P22`

## Context

Search or planning occurs inside a large possibility space.

## Problem

Unbounded combinatorics can consume arbitrary resources or generate candidates that are illegal by construction.

## Forces

- Broad exploration improves novelty.
- Hard constraints prune aggressively.
- Some constraints are policy, others are physics.

## Resolution

**Encode non-negotiable ontology, authority, safety, cost, and evidence constraints as fences before optimization. Optimize freely inside the admitted region.**

## Consequences

Search becomes both more efficient and more defensible.

## Falsifier

The planner spends resources exploring candidates that violate known hard constraints or treats policy constraints as soft preferences.

## Evidence contract

- [ ] constraint classes
- [ ] admission tests
- [ ] resource bounds
- [ ] refusal evidence

## Pattern graph

- [P23 · Falsifier First](23-falsifier-first.md)
- [P04 · Admission Before Action](../foundations/04-admission-before-action.md)
- [P63 · Combinatorial Maximalism](../self-manufacturing/63-combinatorial-maximalism.md)
