# P55 · Release Crown { #p55 }

> **Family:** [VII · Enterprise and Operations](../enterprise-operations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P55`

## Context

Many lower-level verifiers must compose into a release decision.

## Problem

Green unit tests or one successful scenario are routinely overpromoted into claims about the whole system.

## Forces

- Release evidence spans repositories and runtimes.
- Some checks are reusable.
- The crown must fail closed on missing required evidence.

## Resolution

**Define a named release-crown DAG of required capabilities and receipts. The crown is ALIVE only when every required node resolves to valid scoped evidence for the exact release identities.**

## Consequences

Release status becomes a proof composition problem rather than a dashboard impression.

## Falsifier

A required capability is missing or stale but the release still reports complete standing.

## Evidence contract

- [ ] release identity
- [ ] required capability DAG
- [ ] receipt references
- [ ] falsifiers
- [ ] final crown receipt

## Pattern graph

- [P45 · Receipt DAG](../evidence-learning/45-receipt-dag.md)
- [P50 · Minimum Plane Governs](50-minimum-plane-governs.md)
- [P56 · Federated Gym Graph](56-federated-gym-graph.md)
