# P46 · Replay Equivalence { #p46 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P46`

## Context

A replay is expected to demonstrate that prior evidence remains reproducible.

## Problem

Bit identity is too strict for many stochastic or distributed systems, while vague `similar results` is too weak.

## Forces

- Randomness can be legitimate.
- External timing varies.
- Users need domain-specific tolerances.

## Resolution

**Define an equivalence predicate before replay: exact for deterministic artifacts, state-equivalent for resets, metric-bounded for stochastic evaluation, or semantically equivalent for allowed provider differences.**

## Consequences

Replay claims become falsifiable across diverse worlds.

## Falsifier

A replay is declared successful without a predeclared equivalence predicate.

## Evidence contract

- [ ] equivalence class/predicate
- [ ] tolerances
- [ ] replay inputs
- [ ] observed result
- [ ] replay receipt

## Pattern graph

- [P08 · Replay](../foundations/08-replay.md)
- [P44 · Exact Subject Binding](44-exact-subject-binding.md)
- [P48 · Cross-World Comparison](48-cross-world-comparison.md)
