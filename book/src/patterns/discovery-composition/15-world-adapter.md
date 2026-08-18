# P15 · World Adapter { #p15 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P15`

## Context

An external benchmark or runtime needs to participate in the gym lifecycle.

## Problem

Forking the external system to fit local semantics destroys provenance and creates a maintenance branch.

## Forces

- External APIs vary wildly.
- The local lifecycle must remain stable.
- Adapters can accidentally inherit authority.

## Resolution

**Wrap external systems with a thin adapter that maps local reset/observe/intent/execute/verify semantics to the provider without changing provider internals. Keep authority in GymAct, not in the adapter.**

## Consequences

Upstream identity stays intact and provider upgrades remain tractable.

## Falsifier

The adapter performs unbrokered side effects or requires a permanent fork merely to satisfy local lifecycle semantics.

## Evidence contract

- [ ] adapter boundary
- [ ] provider revision
- [ ] mapping tests
- [ ] no ambient authority

## Pattern graph

- [P14 · Capability Seam](14-capability-seam.md)
- [P16 · Local Bridge](16-local-bridge.md)
- [P32 · Project Gym](../manufacture/32-project-gym.md)
