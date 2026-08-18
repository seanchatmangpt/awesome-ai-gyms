# P44 · Exact Subject Binding { #p44 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P44`

## Context

Evidence is used to support a capability claim.

## Problem

Evidence from a neighboring version, mock, generated substitute, or similar configuration can be mistakenly transferred to the target subject.

## Forces

- Reuse of prior evidence saves time.
- Small version changes may be behaviorally irrelevant.
- Subject equivalence is itself a claim.

## Resolution

**Bind every standing claim to the exact subject and environment identities executed. Reuse evidence only when an explicit equivalence relation proves the relevant identities and configuration are interchangeable.**

## Consequences

Evidence inheritance becomes lawful instead of anecdotal.

## Falsifier

ALIVE standing for subject X is justified only by execution of subject Y without a proven equivalence relation.

## Evidence contract

- [ ] subject digest/revision
- [ ] environment identity
- [ ] config identity
- [ ] equivalence proof if reused
- [ ] receipt

## Pattern graph

- [P02 · Canonical Subject](../foundations/02-canonical-subject.md)
- [P07 · Receipt](../foundations/07-receipt.md)
- [P46 · Replay Equivalence](46-replay-equivalence.md)
