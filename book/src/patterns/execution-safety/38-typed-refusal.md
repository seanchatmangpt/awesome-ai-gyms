# P38 · Typed Refusal { #p38 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P38`

## Context

Admission, authority, materialization, or execution can legitimately decline a transition.

## Problem

Generic exceptions blur policy refusal, unsupported capability, missing evidence, infrastructure failure, and software defects.

## Forces

- Callers want simple success/failure APIs.
- Operators need actionable diagnosis.
- Refusal must not be confused with capability absence.

## Resolution

**Use typed outcomes such as REFUSED, BLOCKED, UNSUPPORTED, BUILD_BROKEN, UNKNOWN, and PARTIAL_ALIVE with domain-specific reason codes. Preserve the failed transition and evidence.**

## Consequences

Automation can choose the correct recovery path without pretending every failure is the same.

## Falsifier

A policy denial and a missing compiler produce the same undifferentiated error state.

## Evidence contract

- [ ] typed status
- [ ] reason code
- [ ] failed transition
- [ ] supporting evidence
- [ ] retry/repair semantics

## Pattern graph

- [P39 · Failure Is Topology](39-failure-is-topology.md)
- [P43 · Standing Ladder](../evidence-learning/43-standing-ladder.md)
- [P04 · Admission Before Action](../foundations/04-admission-before-action.md)
