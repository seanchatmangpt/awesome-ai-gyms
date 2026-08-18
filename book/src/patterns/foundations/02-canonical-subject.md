# P02 · Canonical Subject { #p02 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P02`

## Context

A registry, planner, runner, and verifier refer to the thing being tested.

## Problem

Names such as `main`, `latest`, package aliases, or mutable URLs allow different components to believe they are operating on the same subject when they are not.

## Forces

- Human-friendly names are mutable.
- Execution requires concrete bytes or identities.
- Evidence must remain meaningful after upstream changes.

## Resolution

**Resolve every admitted subject to a stable identity before execution: repository plus exact commit/tree, package plus digest, image plus digest, model plus revision, dataset plus version, or equivalent immutable identifier.**

## Consequences

Receipts can bind to a durable subject. Resolution becomes an explicit transition rather than an invisible convenience.

## Falsifier

Two purported replays resolve the same friendly name to different underlying subjects.

## Evidence contract

- [ ] friendly identifier
- [ ] resolved immutable identifier
- [ ] resolver provenance
- [ ] identity included in receipt

## Pattern graph

- [P10 · Provenance Lock](../discovery-composition/10-provenance-lock.md)
- [P44 · Exact Subject Binding](../evidence-learning/44-exact-subject-binding.md)
- [P51 · Exact Runtime Pin](../enterprise-operations/51-exact-runtime-pin.md)
