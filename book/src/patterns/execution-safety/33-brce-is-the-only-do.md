# P33 · BRCE Is the Only DO { #p33 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P33`

## Context

A system contains models, planners, hooks, generators, tools, runtimes, and plugins that can propose actions.

## Problem

Multiple actuation paths make it impossible to prove that every consequence was admitted, authorized, and receipted.

## Forces

- Direct tool execution is convenient.
- Hooks want to automate reactions.
- Distributed providers hide their side-effect boundaries.

## Resolution

**Route every state-changing transition through the Brokered Receipted Consequence Executor (BRCE) or equivalent single consequence broker. All other components may manufacture intents but cannot actuate.**

## Consequences

Execution authority becomes small enough to audit and harden.

## Falsifier

Any component can mutate world or external state without entering the broker.

## Evidence contract

- [ ] enumerated DO operations
- [ ] call graph showing exclusive broker path
- [ ] authority checks
- [ ] receipts

## Pattern graph

- [P34 · Zero Unreceipted Actuation](34-zero-unreceipted-actuation.md)
- [P35 · Tool Call Is Intent](35-tool-call-is-intent.md)
- [P06 · Consequence Boundary](../foundations/06-consequence-boundary.md)
