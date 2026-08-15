# P32 · Project Gym { #p32 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P32`

## Context

A manufactured or manually integrated project needs to demonstrate its own behavior.

## Problem

Examples, playgrounds, smoke tests, integration tests, and demos often scatter the most important executable knowledge across unrelated directories.

## Forces

- Unit tests are narrower than capability proof.
- Examples are readable but frequently stale.
- A project needs one place to answer `what can this actually do?`

## Resolution

**Give each executable project a `gym/` proof surface containing bounded worlds, scenarios, fixtures, assertions, and receipt references. Run it through GymAct or the project's admitted gym runner.**

## Consequences

Examples and playground behavior gain executable standing and can be used as acceptance surfaces.

## Falsifier

The only proof of a major capability is an unexecuted example, README snippet, or bespoke CI workflow outside the project gym.

## Evidence contract

- [ ] gym manifest
- [ ] worlds
- [ ] scenarios
- [ ] assertions/verifiers
- [ ] receipt locations

## Pattern graph

- [P28 · Pack Gym](28-pack-gym.md)
- [P60 · Gym in Every Project](../self-manufacturing/60-gym-in-every-project.md)
- [P40 · Independent Postcondition](../execution-safety/40-independent-postcondition.md)
