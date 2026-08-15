# P18 · Policy Is Not Agent { #p18 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P18`

## Context

A runtime assigns behavior to roles in a world.

## Problem

The words policy, planner, role, and agent are often collapsed, making it impossible to vary one dimension independently.

## Forces

- One process may host many roles.
- A planner can parameterize many policies.
- LLMs may compile decisions without owning rollout.

## Resolution

**Represent policy as planner × parameters × objective × observation projection × action projection, and represent roles separately from the runtime process that hosts them.**

## Consequences

Self-play and cross-planner experiments become compositional.

## Falsifier

Changing the observation projection requires creating a new `agent type` even though planner and role are unchanged.

## Evidence contract

- [ ] policy tuple
- [ ] role definition
- [ ] planner identity
- [ ] projection identities

## Pattern graph

- [P17 · Planner League](17-planner-league.md)
- [P19 · Planning Projection](19-planning-projection.md)
- [P20 · Multiple Formulations](20-multiple-formulations.md)
