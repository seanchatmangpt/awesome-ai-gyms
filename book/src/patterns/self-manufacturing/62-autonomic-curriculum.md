# P62 · Autonomic Curriculum { #p62 }

> **Family:** [VIII · Self-Manufacturing Ecosystem](../self-manufacturing.md)  
> **Confidence:** ★☆☆  
> **Canonical ID:** `P62`

## Context

A gym ecosystem accumulates failures, capability evidence, planner performance, and changing worlds.

## Problem

Static scenario suites stop targeting the most informative uncertainty and repeatedly spend resources on already-settled behavior.

## Forces

- Adaptive testing risks moving goalposts.
- Exploration needs reproducible seeds.
- Regression coverage must remain stable.

## Resolution

**Maintain a stable regression core plus an autonomically selected curriculum drawn from UNKNOWN edges, recent failures, boundary conditions, and high-value uncertainty. Record why each scenario was selected.**

## Consequences

Evaluation effort follows information value while preserving historical comparability.

## Falsifier

Adaptive selection can silently drop required regressions or choose scenarios without a recorded objective/evidence rationale.

## Evidence contract

- [ ] fixed regression set
- [ ] adaptive candidate pool
- [ ] selection rationale
- [ ] budgets
- [ ] curriculum receipts

## Pattern graph

- [P17 · Planner League](../planning-selection/17-planner-league.md)
- [P47 · Failure Becomes Law](../evidence-learning/47-failure-becomes-law.md)
- [P53 · Cost-Time-Attention Budget](../enterprise-operations/53-cost-time-attention-budget.md)
