# P35 · Tool Call Is Intent { #p35 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P35`

## Context

A model or planner emits a structured tool invocation.

## Problem

Tool-call syntax is often wired directly to execution, giving generated text ambient machine authority.

## Forces

- Tool ecosystems are designed for convenience.
- Models hallucinate arguments.
- Policy enforcement needs stable objects.

## Resolution

**Treat every model-facing tool call as an intent object. Normalize, validate, admit, authorize, and only then route it to DO. The tool schema defines a proposal surface, not an execution capability.**

## Consequences

Model innovation and tool richness can increase without expanding the trusted computing base.

## Falsifier

Emitting a syntactically valid tool call is sufficient to cause the side effect.

## Evidence contract

- [ ] raw call
- [ ] normalized intent
- [ ] admission decision
- [ ] authority decision
- [ ] execution receipt

## Pattern graph

- [P24 · Selection Is Not Authorization](../planning-selection/24-selection-is-not-authorization.md)
- [P04 · Admission Before Action](../foundations/04-admission-before-action.md)
- [P33 · BRCE Is the Only DO](33-brce-is-the-only-do.md)
