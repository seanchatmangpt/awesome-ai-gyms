# P41 · OCEL Event Spine { #p41 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P41`

## Context

A gym produces many episodes, transitions, tool calls, plans, receipts, and objects.

## Problem

Ad hoc logs make cross-run process analysis and causal comparison difficult.

## Forces

- Events involve multiple objects.
- Runtime logs are provider-specific.
- Process mining needs stable event/object semantics.

## Resolution

**Project execution evidence onto an object-centric event log with stable event types, object identities, relationships, timestamps, and receipt links. Keep raw evidence available behind the projection.**

## Consequences

Process mining, conformance analysis, and cross-world learning can operate on a common behavioral spine.

## Falsifier

A claimed process metric cannot be traced back to concrete execution events and subject objects.

## Evidence contract

- [ ] event schema
- [ ] object identities
- [ ] event-object relations
- [ ] receipt links
- [ ] raw evidence references

## Pattern graph

- [P03 · Explicit Observation](../foundations/03-explicit-observation.md)
- [P45 · Receipt DAG](45-receipt-dag.md)
- [P48 · Cross-World Comparison](48-cross-world-comparison.md)
