# P08 · Replay { #p08 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P08`

## Context

A run has produced evidence and someone needs to audit, compare, or reproduce it.

## Problem

Re-running the same command is not replay if the subject, environment, observations, seeds, or verifier changed.

## Forces

- Perfect bit-for-bit reproduction may be impossible in stochastic worlds.
- Auditors need bounded equivalence criteria.
- Replay infrastructure costs storage.

## Resolution

**Define replay as reconstruction of the admitted subject, world, inputs, authority envelope, and verifier with an explicit equivalence relation for allowed nondeterminism.**

## Consequences

Evidence remains useful after the original process exits. Stochastic systems can still support rigorous replay by declaring tolerances.

## Falsifier

A `replay` depends on mutable latest dependencies or lacks a declared equivalence test.

## Evidence contract

- [ ] replay manifest
- [ ] pinned identities
- [ ] seed/randomness record
- [ ] equivalence predicate
- [ ] replay receipt

## Pattern graph

- [P07 · Receipt](07-receipt.md)
- [P46 · Replay Equivalence](../evidence-learning/46-replay-equivalence.md)
- [P58 · Delete and Regenerate](../self-manufacturing/58-delete-and-regenerate.md)
