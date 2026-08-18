# P45 · Receipt DAG { #p45 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P45`

## Context

A workflow contains multiple manufactured artifacts, plans, admissions, executions, and verifications.

## Problem

One flat final log cannot preserve the causal structure needed to audit or replay the workflow.

## Forces

- Evidence comes from different subsystems.
- Some branches are parallel.
- Failures may occur after partial success.

## Resolution

**Link receipts into a DAG whose edges represent derivation, admission, execution, verification, replay, or dependency relationships. Each node remains independently inspectable.**

## Consequences

Complex workflows retain causal history without forcing a total order.

## Falsifier

A final success receipt cannot identify which exact upstream plan, artifact, authority decision, and verifier results it depended on.

## Evidence contract

- [ ] receipt identifiers
- [ ] typed edges
- [ ] subject lineage
- [ ] partial/failure nodes
- [ ] root release/crown node

## Pattern graph

- [P07 · Receipt](../foundations/07-receipt.md)
- [P21 · Partial Order Before Total Order](../planning-selection/21-partial-order-before-total-order.md)
- [P55 · Release Crown](../enterprise-operations/55-release-crown.md)
