# P05 · Authority Boundary { #p05 }

> **Family:** [I · Foundations](../foundations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P05`

## Context

A semantically valid action may still lack permission to occur.

## Problem

Systems often conflate `can be represented`, `looks safe`, or `was selected` with authority to cause consequences.

## Forces

- Authority may differ by subject, user, world, action, and time.
- Central policy is simpler but can overgrant.
- Models and planners are untrusted producers of intent.

## Resolution

**Represent authority as an explicit capability scoped to actor, action, subject, world, and validity interval. Check it at the consequence boundary; never grant ambient execution authority to planners, hooks, prompts, or generated artifacts.**

## Consequences

Authorization becomes auditable and revocable. The design can safely host aggressive exploration upstream.

## Falsifier

A planner or tool schema can directly cause a consequence merely because it emitted a syntactically valid call.

## Evidence contract

- [ ] authority object
- [ ] scope
- [ ] issuer
- [ ] expiry/revocation semantics
- [ ] authority check in execution receipt

## Pattern graph

- [P04 · Admission Before Action](04-admission-before-action.md)
- [P35 · Tool Call Is Intent](../execution-safety/35-tool-call-is-intent.md)
- [P34 · Zero Unreceipted Actuation](../execution-safety/34-zero-unreceipted-actuation.md)
