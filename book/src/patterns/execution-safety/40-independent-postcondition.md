# P40 · Independent Postcondition { #p40 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P40`

## Context

An executor reports that a requested action succeeded.

## Problem

The component that performed the action is not independent evidence that the intended consequence actually holds.

## Forces

- External APIs can acknowledge before convergence.
- Executors may contain correlated bugs.
- Verification may be expensive.

## Resolution

**After DO, run a verifier that observes the world independently of the executor's success return and evaluates the declared postcondition.**

## Consequences

Standing is based on consequence, not optimism from the execution path.

## Falsifier

The only evidence for success is the executor's own return value or log message.

## Evidence contract

- [ ] declared postcondition
- [ ] independent observation path
- [ ] verifier identity
- [ ] verifier result in receipt

## Pattern graph

- [P23 · Falsifier First](../planning-selection/23-falsifier-first.md)
- [P07 · Receipt](../foundations/07-receipt.md)
- [P44 · Exact Subject Binding](../evidence-learning/44-exact-subject-binding.md)
