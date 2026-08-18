# P58 · Delete and Regenerate { #p58 }

> **Family:** [VIII · Self-Manufacturing Ecosystem](../self-manufacturing.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P58`

## Context

A generated repository or artifact tree is claimed to be a projection rather than the primary source of truth.

## Problem

Manual edits and hidden state can accumulate until regeneration is theoretically possible but practically false.

## Forces

- Deleting artifacts feels risky.
- Build caches obscure dependencies.
- Some state is intentionally persistent.

## Resolution

**Periodically delete the disposable projection and reconstruct it from the canonical graph, pack lock, and pinned toolchain; then rerun behavioral verification under declared equivalence.**

## Consequences

Regeneration becomes continuously exercised disaster recovery and drift detection.

## Falsifier

A supposedly reproducible project cannot be rebuilt after deleting generated artifacts without recovering undocumented manual state.

## Evidence contract

- [ ] canonical inputs
- [ ] deletion boundary
- [ ] rebuild receipt
- [ ] artifact equivalence
- [ ] project-gym replay

## Pattern graph

- [P30 · Deterministic Projection](../manufacture/30-deterministic-projection.md)
- [P57 · Empty Repo Crown](57-empty-repo-crown.md)
- [P46 · Replay Equivalence](../evidence-learning/46-replay-equivalence.md)
