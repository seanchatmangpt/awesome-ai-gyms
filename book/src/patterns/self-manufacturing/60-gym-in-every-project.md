# P60 · Gym in Every Project { #p60 }

> **Family:** [VIII · Self-Manufacturing Ecosystem](../self-manufacturing.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P60`

## Context

Projects across the ecosystem need a consistent place for executable examples, playgrounds, acceptance worlds, and capability proof.

## Problem

Each repository invents a different layout and tooling convention, making discovery and automation expensive.

## Forces

- Not every library needs heavy end-to-end tests.
- Uniformity can become dogma.
- A common convention unlocks tooling.

## Resolution

**Adopt `gym/` as the canonical behavioral proof surface for executable projects and packs. Permit lightweight gyms, but standardize the semantic roles of worlds, scenarios, fixtures, assertions, and receipts.**

## Consequences

Tooling can locate and execute capability proofs without repository-specific archaeology.

## Falsifier

A major executable project has no discoverable behavioral proof surface or requires bespoke knowledge to find its acceptance scenarios.

## Evidence contract

- [ ] gym manifest or discoverable convention
- [ ] world/scenario locations
- [ ] runner contract
- [ ] receipt references

## Pattern graph

- [P32 · Project Gym](../manufacture/32-project-gym.md)
- [P28 · Pack Gym](../manufacture/28-pack-gym.md)
- [P61 · Gym of Gyms](61-gym-of-gyms.md)
