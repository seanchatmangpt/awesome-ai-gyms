# P01 · Bounded World { #p01 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P01`

## Context

An actor, policy, planner, or agent must interact with an environment.

## Problem

Without an explicit world boundary, observations, actions, resets, and consequences leak into ambient machine state and claims become unscoped.

## Forces

- Real systems expose more state than an experiment needs.
- Isolation adds cost, but unbounded consequence destroys reproducibility.
- A useful world must be rich enough to falsify the policy being tested.

## Resolution

**Define a world as an explicit state space, observation projection, admitted transition relation, reset semantics, resource boundary, and consequence boundary. Anything outside that definition is external and cannot silently participate.**

## Consequences

Experiments gain a named causal boundary and deterministic reset target. Some realism is intentionally excluded and must be reintroduced through explicit world extensions.

## Falsifier

A scenario can read or mutate state that is neither declared as world state nor recorded as an external dependency.

## Evidence contract

- [ ] world identity and version
- [ ] state/observation/action contract
- [ ] reset proof
- [ ] declared external dependencies

## Pattern graph

- [P02 · Canonical Subject](02-canonical-subject.md)
- [P06 · Consequence Boundary](06-consequence-boundary.md)
- [P37 · Idempotent Reset](../execution-safety/37-idempotent-reset.md)
- [P15 · World Adapter](../discovery-composition/15-world-adapter.md)
