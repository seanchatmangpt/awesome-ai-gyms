# P13 · Reversible Composition { #p13 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P13`

## Context

A gym is assembled from providers, plugins, adapters, tools, models, or policies.

## Problem

Composition becomes fragile when adding one capability mutates global state or requires patching a privileged core.

## Forces

- Plugins need lifecycle ordering.
- Shared state is convenient.
- Experiments benefit from swapping implementations.

## Resolution

**Prefer compositions whose registrations and effects are scoped, replaceable, and unwindable. Treat configuration as a graph that can be constructed, compared, and discarded before DO.**

## Consequences

The search space stays large while experiment teardown stays cheap.

## Falsifier

Removing or replacing one component leaves hidden state that changes subsequent runs.

## Evidence contract

- [ ] component graph
- [ ] lifecycle hooks
- [ ] teardown/reset proof
- [ ] dependency declaration

## Pattern graph

- [P14 · Capability Seam](14-capability-seam.md)
- [P63 · Combinatorial Maximalism](../self-manufacturing/63-combinatorial-maximalism.md)
- [P37 · Idempotent Reset](../execution-safety/37-idempotent-reset.md)
