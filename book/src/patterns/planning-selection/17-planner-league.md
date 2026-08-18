# P17 · Planner League { #p17 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P17`

## Context

A problem can be expressed to multiple planning algorithms or solver families.

## Problem

Treating one planner or one LLM as the universal decision maker hides formulation sensitivity and collapses useful diversity.

## Forces

- Different planners dominate different structures.
- Search cost can be high.
- Comparisons need common world semantics.

## Resolution

**Maintain a league of planners with explicit domain contracts. Evaluate compatible planners against the same admitted world and objective, and let evidence update selection policy.**

## Consequences

Planner diversity becomes an asset rather than integration debt.

## Falsifier

One planner receives exclusive authority merely because it is the default implementation.

## Evidence contract

- [ ] planner registry
- [ ] domain contracts
- [ ] common objective
- [ ] comparative receipts
- [ ] selection policy

## Pattern graph

- [P20 · Multiple Formulations](20-multiple-formulations.md)
- [P18 · Policy Is Not Agent](18-policy-is-not-agent.md)
- [P24 · Selection Is Not Authorization](24-selection-is-not-authorization.md)
