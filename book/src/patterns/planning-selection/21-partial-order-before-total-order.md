# P21 · Partial Order Before Total Order { #p21 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P21`

## Context

A workflow contains dependencies but many steps are independent.

## Problem

Prematurely imposing a single sequence destroys concurrency and creates unnecessary waiting.

## Forces

- Total orders are easy to visualize.
- Real authority may serialize only a few transitions.
- Parallelism complicates replay.

## Resolution

**Represent only required precedence constraints. Preserve a partial order until execution resources or authority force a totalization, and record the chosen linearization.**

## Consequences

Little's Law improves because independent work can proceed concurrently without semantic compromise.

## Falsifier

A workflow serializes independent tasks without an authority, data, or resource dependency that requires ordering.

## Evidence contract

- [ ] dependency DAG
- [ ] independence proof or lack of edge
- [ ] chosen schedule
- [ ] execution timestamps

## Pattern graph

- [P22 · Constraint Fence](22-constraint-fence.md)
- [P63 · Combinatorial Maximalism](../self-manufacturing/63-combinatorial-maximalism.md)
- [P45 · Receipt DAG](../evidence-learning/45-receipt-dag.md)
