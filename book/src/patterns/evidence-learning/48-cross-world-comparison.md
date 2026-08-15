# P48 · Cross-World Comparison { #p48 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P48`

## Context

A policy, planner, or architecture is evaluated across multiple gyms or world configurations.

## Problem

Metrics with different task semantics, observation spaces, or consequence models are compared as though they measured the same capability.

## Forces

- Leadership wants one leaderboard.
- World difficulty varies.
- Useful transfer requires shared semantics without erasing differences.

## Resolution

**Compare only through declared common dimensions and mappings. Preserve world-specific metrics alongside normalized projections, and attach every aggregate to its source receipts.**

## Consequences

Cross-gym learning becomes defensible without manufacturing a false universal score.

## Falsifier

A single aggregate score combines incomparable world metrics with no mapping or uncertainty model.

## Evidence contract

- [ ] world identities
- [ ] metric semantics
- [ ] normalization/mapping
- [ ] source receipts
- [ ] uncertainty

## Pattern graph

- [P41 · OCEL Event Spine](41-ocel-event-spine.md)
- [P20 · Multiple Formulations](../planning-selection/20-multiple-formulations.md)
- [P52 · Capability Certification](../enterprise-operations/52-capability-certification.md)
