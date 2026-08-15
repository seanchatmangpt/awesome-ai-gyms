# P23 · Falsifier First { #p23 }

> **Family:** [III · Planning and Selection](../planning-selection.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P23`

## Context

A plan, capability, or architectural claim is being proposed.

## Problem

Teams naturally collect confirming examples and postpone the test that could defeat the claim.

## Forces

- Positive demos are persuasive.
- Boundary failures often contain more information.
- Some falsifiers are expensive.

## Resolution

**Before implementation, state the cheapest decisive observation that would invalidate the claim or force its scope to narrow. Build that into the gym scenario.**

## Consequences

Development optimizes for information gain instead of demonstration theater.

## Falsifier

A claim advances to ALIVE without a predeclared failure condition or independent acceptance boundary.

## Evidence contract

- [ ] claim
- [ ] scope
- [ ] falsifier
- [ ] test scenario
- [ ] observed result

## Pattern graph

- [P40 · Independent Postcondition](../execution-safety/40-independent-postcondition.md)
- [P43 · Standing Ladder](../evidence-learning/43-standing-ladder.md)
- [P47 · Failure Becomes Law](../evidence-learning/47-failure-becomes-law.md)
