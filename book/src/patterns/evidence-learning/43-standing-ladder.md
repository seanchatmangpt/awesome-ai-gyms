# P43 · Standing Ladder { #p43 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P43`

## Context

Stakeholders need a compact status for a capability or subject.

## Problem

Binary pass/fail collapses important differences between unknown, unsupported, blocked, broken, partially demonstrated, and fully demonstrated behavior.

## Forces

- Status must remain understandable.
- Granularity can explode.
- Standing must be scoped to evidence.

## Resolution

**Use a small typed ladder such as UNKNOWN, PARTIAL_ALIVE, ALIVE, BLOCKED, BUILD_BROKEN, UNSUPPORTED, plus typed REFUSED. ALIVE requires observed execution against the exact admitted subject.**

## Consequences

Status becomes actionable and evidence-bounded.

## Falsifier

A documentation inspection, successful build, or workflow definition alone can produce ALIVE.

## Evidence contract

- [ ] status
- [ ] scope
- [ ] subject identity
- [ ] evidence/receipt
- [ ] falsifier for promotion

## Pattern graph

- [P11 · Candidate Is Not Capability](../discovery-composition/11-candidate-is-not-capability.md)
- [P38 · Typed Refusal](../execution-safety/38-typed-refusal.md)
- [P44 · Exact Subject Binding](44-exact-subject-binding.md)
