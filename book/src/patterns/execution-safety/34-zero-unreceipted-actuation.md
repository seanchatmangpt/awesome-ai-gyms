# P34 · Zero Unreceipted Actuation { #p34 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P34`

## Context

The consequence broker is about to perform an admitted state change.

## Problem

Allowing `fire and forget` transitions creates gaps where consequential actions exist without durable evidence.

## Forces

- Receipts add latency and storage.
- External systems can fail after accepting a request.
- Some consequences are only eventually observable.

## Resolution

**Make receipt production part of the actuation contract. A DO transition is incomplete until its execution and observed consequence are bound into a receipt or an explicit partial/failure receipt.**

## Consequences

Every attempted consequence leaves an auditable causal artifact.

## Falsifier

A state change can be observed in the world but no corresponding execution or failure receipt exists.

## Evidence contract

- [ ] pre-actuation intent receipt
- [ ] executor result
- [ ] postcondition evidence
- [ ] final or partial receipt

## Pattern graph

- [P07 · Receipt](../foundations/07-receipt.md)
- [P33 · BRCE Is the Only DO](33-brce-is-the-only-do.md)
- [P45 · Receipt DAG](../evidence-learning/45-receipt-dag.md)
