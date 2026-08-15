# P07 · Receipt { #p07 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P07`

## Context

An admitted transition has been attempted or completed.

## Problem

Logs prove that text was emitted, not that the exact subject executed under the claimed authority and produced the claimed consequence.

## Forces

- Evidence must be compact enough to retain.
- Distributed execution produces multiple identities.
- A verifier can fail independently of execution.

## Resolution

**Emit a deterministic receipt that binds subject identity, admitted intent, authority decision, executor identity, observed consequence, verifier result, timing, and references to replay material.**

## Consequences

Claims gain a machine-checkable evidentiary object. Receipts can form DAGs across multi-step workflows.

## Falsifier

A claimed successful action cannot be tied to one exact admitted subject and one observed verifier outcome.

## Evidence contract

- [ ] receipt identifier/hash
- [ ] subject
- [ ] intent
- [ ] authority
- [ ] executor
- [ ] consequence
- [ ] verifier
- [ ] replay references

## Pattern graph

- [P44 · Exact Subject Binding](../evidence-learning/44-exact-subject-binding.md)
- [P45 · Receipt DAG](../evidence-learning/45-receipt-dag.md)
- [P08 · Replay](08-replay.md)
