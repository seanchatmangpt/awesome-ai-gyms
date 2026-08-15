# P03 · Explicit Observation { #p03 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P03`

## Context

A world exposes state to a planner, policy, model, or verifier.

## Problem

If observations are implicit, different actors may reason from different hidden projections and a successful run cannot be reconstructed.

## Forces

- Full state may be too large or unsafe to expose.
- Partial observability is often intentional.
- Derived observations can smuggle inference into fact.

## Resolution

**Define observation objects and projections explicitly. Record what was observed, when, by whom, under which world state, and which derivations were applied.**

## Consequences

Partial observability becomes a modeled property rather than missing instrumentation. Observed and inferred facts can be separated.

## Falsifier

A later verifier cannot determine which state was actually visible to the acting policy.

## Evidence contract

- [ ] observation schema
- [ ] projection identity
- [ ] timestamp/sequence
- [ ] observed-versus-derived marker

## Pattern graph

- [P01 · Bounded World](01-bounded-world.md)
- [P42 · Observation vs Inference](../evidence-learning/42-observation-vs-inference.md)
- [P41 · OCEL Event Spine](../evidence-learning/41-ocel-event-spine.md)
