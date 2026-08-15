# P26 · One Pack, One Manufacturing Boundary { #p26 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P26`

## Context

ggen needs reusable knowledge for manufacturing a coherent architecture or product capability.

## Problem

Tiny packs create dependency explosion; giant packs hide unrelated authority and make reuse impossible.

## Forces

- Reusable boundaries are larger than code snippets.
- Projects need local specialization.
- Pack composition must remain understandable.

## Resolution

**Define a pack around one cohesive, independently meaningful manufacturing boundary: ontology, admission rules, deterministic selection, templates/projections, fixtures, and qualification evidence. Depend on other packs for truly independent boundaries.**

## Consequences

Pack graphs remain composable without degenerating into either monoliths or feature confetti.

## Falsifier

A pack cannot explain its reusable semantic boundary without listing one specific consumer project or dozens of unrelated capabilities.

## Evidence contract

- [ ] pack ontology
- [ ] declared dependencies
- [ ] owned projections
- [ ] qualification gym
- [ ] versioned evidence

## Pattern graph

- [P16 · Local Bridge](../discovery-composition/16-local-bridge.md)
- [P28 · Pack Gym](28-pack-gym.md)
- [P29 · Marketplace Qualification](29-marketplace-qualification.md)
