# P52 · Capability Certification { #p52 }

> **Family:** [VII · Enterprise and Operations](../enterprise-operations.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P52`

## Context

A gym or provider needs to advertise which capabilities have actually been demonstrated.

## Problem

Feature lists mix declared, implemented, runnable, and verified states.

## Forces

- Certification can become bureaucracy.
- Capabilities vary by mode and environment.
- Evidence expires as versions move.

## Resolution

**Publish a machine-readable capability matrix whose cells bind exact subject + mode + environment + standing + receipt. Treat unsupported and untested cells explicitly.**

## Consequences

Consumers can select providers from evidence rather than marketing claims.

## Falsifier

A capability is advertised as supported without a scoped execution receipt or explicit UNKNOWN/UNSUPPORTED status.

## Evidence contract

- [ ] capability IDs
- [ ] subject/mode/environment
- [ ] standing
- [ ] receipt
- [ ] validity/supersession

## Pattern graph

- [P43 · Standing Ladder](../evidence-learning/43-standing-ladder.md)
- [P48 · Cross-World Comparison](../evidence-learning/48-cross-world-comparison.md)
- [P29 · Marketplace Qualification](../manufacture/29-marketplace-qualification.md)
