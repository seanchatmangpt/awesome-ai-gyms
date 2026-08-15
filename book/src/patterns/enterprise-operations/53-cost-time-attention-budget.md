# P53 · Cost-Time-Attention Budget { #p53 }

> **Family:** [VII · Enterprise and Operations](../enterprise-operations.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P53`

## Context

Autonomous planning and gym execution can explore very large spaces.

## Problem

Optimization for success alone can consume unbounded money, wall-clock time, tokens, compute, or human review.

## Forces

- Cheap exploration is valuable.
- Budgets differ by phase.
- Evidence quality must not be sacrificed merely to be fast.

## Resolution

**Make cost, wall-clock, compute, token, and human-attention budgets explicit admission constraints and receipt dimensions. Optimize verified consequences per bounded resource.**

## Consequences

Autonomy scales without hidden resource debt.

## Falsifier

A planner or gym can exceed agreed resource limits without refusal or evidence that the limit changed.

## Evidence contract

- [ ] budget envelope
- [ ] resource counters
- [ ] admission/refusal behavior
- [ ] receipt metrics

## Pattern graph

- [P22 · Constraint Fence](../planning-selection/22-constraint-fence.md)
- [P63 · Combinatorial Maximalism](../self-manufacturing/63-combinatorial-maximalism.md)
- [P62 · Autonomic Curriculum](../self-manufacturing/62-autonomic-curriculum.md)
