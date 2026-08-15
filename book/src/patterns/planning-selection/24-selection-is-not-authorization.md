# P24 · Selection Is Not Authorization { #p24 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P24`

## Context

A planner, optimizer, model, or human chooses a candidate action.

## Problem

Selection is frequently treated as permission to execute, allowing decision logic to inherit consequence authority.

## Forces

- Low-latency systems want direct tool calls.
- Selections may be probabilistic.
- Authority belongs to governance, not optimization.

## Resolution

**Make selection produce a powerless intent. Pass that intent to a separate admission/authority boundary before any DO transition.**

## Consequences

Planners can be replaced, ensembled, or made more aggressive without changing the safety model.

## Falsifier

A selected action can directly cross the consequence boundary without a separate authority decision.

## Evidence contract

- [ ] selection record
- [ ] intent object
- [ ] separate admission decision
- [ ] execution receipt linking both

## Pattern graph

- [P35 · Tool Call Is Intent](../execution-safety/35-tool-call-is-intent.md)
- [P05 · Authority Boundary](../foundations/05-authority-boundary.md)
- [P17 · Planner League](17-planner-league.md)
