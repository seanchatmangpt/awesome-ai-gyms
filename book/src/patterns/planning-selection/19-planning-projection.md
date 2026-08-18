# P19 · Planning Projection { #p19 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P19`

## Context

A rich canonical graph must be solved by a planner with a narrower input language.

## Problem

Hand-maintained planning models drift from the canonical semantics and silently change the problem.

## Forces

- Planners need specialized representations.
- Canonical ontologies favor interoperability.
- Projection can lose information.

## Resolution

**Generate planner-specific models as deterministic projections from the admitted canonical graph, and record the projection identity in the plan evidence.**

## Consequences

Many planner languages can coexist without becoming competing sources of truth.

## Falsifier

A planning model contains semantics that cannot be traced back to the admitted canonical graph or declared projection rules.

## Evidence contract

- [ ] source graph digest
- [ ] projection version
- [ ] generated planner model
- [ ] round-trip/coverage checks

## Pattern graph

- [P25 · Ontology First](../manufacture/25-ontology-first.md)
- [P20 · Multiple Formulations](20-multiple-formulations.md)
- [P30 · Deterministic Projection](../manufacture/30-deterministic-projection.md)
