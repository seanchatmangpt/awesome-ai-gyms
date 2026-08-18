# P11 · Candidate Is Not Capability { #p11 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P11`

## Context

A discovered project appears to offer useful functionality.

## Problem

Presence in a list, a README claim, import success, or a CI badge is easily mistaken for demonstrated local capability.

## Forces

- Humans use social proof as a shortcut.
- Documentation is cheap to produce.
- Compatibility can fail only at runtime boundaries.

## Resolution

**Represent discovery as candidate status only. Promote to capability standing only after exact-subject execution through the relevant admitted world and verifier.**

## Consequences

The registry can be generous while execution claims remain conservative.

## Falsifier

A candidate receives ALIVE or capability standing without an observed exact-subject run and receipt.

## Evidence contract

- [ ] candidate standing
- [ ] separate compatibility state
- [ ] execution receipt reference for promotions

## Pattern graph

- [P43 · Standing Ladder](../evidence-learning/43-standing-ladder.md)
- [P12 · Compatibility Edge](12-compatibility-edge.md)
- [P09 · Possibility Registry](09-possibility-registry.md)
