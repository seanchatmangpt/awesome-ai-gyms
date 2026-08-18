# P04 · Admission Before Action { #p04 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P04`

## Context

A candidate intent could cause a world transition.

## Problem

Validation performed after actuation cannot protect the world from an invalid or unauthorized transition.

## Forces

- Some checks are expensive.
- Planners benefit from exploring invalid candidates cheaply.
- Authority must not be inferred from semantic validity.

## Resolution

**Place a formal admission boundary before every consequential transition. Admission validates subject, schema, preconditions, exclusions, authority requirements, and resource bounds; refusal is a first-class outcome.**

## Consequences

The execution path becomes fail-closed. Candidate generation remains broad because invalid candidates can be refused without being executed.

## Falsifier

A state-changing path exists that bypasses admission or performs validation only after mutation.

## Evidence contract

- [ ] admission input
- [ ] admission decision
- [ ] typed refusal reason
- [ ] proof that DO is unreachable on refusal

## Pattern graph

- [P05 · Authority Boundary](05-authority-boundary.md)
- [P38 · Typed Refusal](../execution-safety/38-typed-refusal.md)
- [P33 · BRCE Is the Only DO](../execution-safety/33-brce-is-the-only-do.md)
