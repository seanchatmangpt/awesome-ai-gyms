# P37 · Idempotent Reset { #p37 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P37`

## Context

Many scenarios must run against the same world type.

## Problem

Residual state from prior episodes creates order-dependent results and false capability claims.

## Forces

- Full reconstruction may be slow.
- Caches improve performance.
- Some external systems cannot be perfectly reset.

## Resolution

**Define reset as a verified transition to a named baseline. Prefer reconstructable ephemeral worlds; where reset is approximate, specify and test the equivalence class.**

## Consequences

Scenario order stops affecting standing and parallel execution becomes safer.

## Falsifier

Running scenario B after scenario A changes B's result compared with running B from a fresh baseline without a declared dependency.

## Evidence contract

- [ ] baseline identity
- [ ] reset procedure
- [ ] post-reset verifier
- [ ] leakage test

## Pattern graph

- [P01 · Bounded World](../foundations/01-bounded-world.md)
- [P08 · Replay](../foundations/08-replay.md)
- [P13 · Reversible Composition](../discovery-composition/13-reversible-composition.md)
