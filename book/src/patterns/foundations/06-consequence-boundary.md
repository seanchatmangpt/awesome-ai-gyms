# P06 · Consequence Boundary { #p06 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P06`

## Context

A system transitions from reversible reasoning to machine-state change.

## Problem

Irreversible or externally visible effects are qualitatively different from graph exploration, simulation, planning, or construction.

## Forces

- Users want low latency.
- Distributed systems hide side effects behind APIs.
- Some operations appear read-only but allocate, cache, bill, or publish.

## Resolution

**Name and minimize the consequence boundary. Everything before it is SELECT or CONSTRUCT; crossing it is DO and must pass through the designated broker with explicit authority and receipt obligations.**

## Consequences

The system can optimize aggressively before DO while keeping actual consequence conservative and inspectable.

## Falsifier

A component outside the named DO path can produce externally visible or persistent state changes.

## Evidence contract

- [ ] enumerated consequence classes
- [ ] single execution path
- [ ] side-effect inventory
- [ ] receipt for every admitted transition

## Pattern graph

- [P33 · BRCE Is the Only DO](../execution-safety/33-brce-is-the-only-do.md)
- [P35 · Tool Call Is Intent](../execution-safety/35-tool-call-is-intent.md)
- [P34 · Zero Unreceipted Actuation](../execution-safety/34-zero-unreceipted-actuation.md)
