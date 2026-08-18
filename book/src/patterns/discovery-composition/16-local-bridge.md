# P16 · Local Bridge { #p16 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P16`

## Context

A project needs ecosystem-specific semantics that should not contaminate a shared upstream pack or provider.

## Problem

Putting every local convention into global infrastructure causes coupling and pack explosion.

## Forces

- Local projects need flexibility.
- Shared packs need stable boundaries.
- Bridges can become dumping grounds.

## Resolution

**Place project-specific semantic mappings in a consumer-local bridge pack or adapter. Keep the shared pack focused on the reusable manufacturing boundary and make the bridge explicitly dependent on it.**

## Consequences

Local specialization remains possible without forking ecosystem-wide law.

## Falsifier

A shared pack contains one-off project assumptions that cannot be justified outside a single consumer.

## Evidence contract

- [ ] bridge ownership
- [ ] explicit dependency
- [ ] local ontology mappings
- [ ] local gym scenarios

## Pattern graph

- [P26 · One Pack, One Manufacturing Boundary](../manufacture/26-one-pack-one-manufacturing-boundary.md)
- [P15 · World Adapter](15-world-adapter.md)
- [P32 · Project Gym](../manufacture/32-project-gym.md)
