# P20 · Multiple Formulations { #p20 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P20`

## Context

One operational problem can be modeled as planning, scheduling, constraint satisfaction, optimization, search, or workflow.

## Problem

Selecting a formulation by habit can make a tractable problem look impossible or overfit the system to one solver ecosystem.

## Forces

- Formulation changes performance dramatically.
- Equivalent formulations may not preserve every semantic detail.
- Maintaining alternatives by hand is expensive.

## Resolution

**Preserve several formally related projections of the same admitted problem where equivalence or refinement can be stated. Let evidence select among them by context.**

## Consequences

The ecosystem can discover that a `new` planning problem is structurally equivalent to an older solved class.

## Falsifier

Alternative formulations introduce undeclared semantics or cannot map outcomes back to the same world-level objective.

## Evidence contract

- [ ] shared canonical problem
- [ ] projection mappings
- [ ] equivalence/refinement claims
- [ ] comparative evidence

## Pattern graph

- [P19 · Planning Projection](19-planning-projection.md)
- [P17 · Planner League](17-planner-league.md)
- [P63 · Combinatorial Maximalism](../self-manufacturing/63-combinatorial-maximalism.md)
