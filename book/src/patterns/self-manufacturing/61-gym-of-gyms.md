# P61 · Gym of Gyms { #p61 }

> **Family:** [VIII · Self-Manufacturing Ecosystem](../self-manufacturing.md)  
> **Confidence:** ★★☆  
> **Canonical ID:** `P61`

## Context

Many gyms must be compared, composed, or exercised as one ecosystem.

## Problem

A central runner that hardcodes every domain becomes the new monolith.

## Forces

- Cross-gym experiments are valuable.
- Gyms have different lifecycles.
- Federation should preserve local semantics.

## Resolution

**Build a meta-gym that treats gyms themselves as typed subjects with adapters, maturity, capability matrices, and receipts. Compose through shared lifecycle contracts rather than importing domain internals.**

## Consequences

The ecosystem can evaluate gym infrastructure and selection policies at a higher level.

## Falsifier

Adding a new gym requires patching privileged meta-gym core logic rather than registering a compatible typed adapter.

## Evidence contract

- [ ] gym registry identities
- [ ] adapter contracts
- [ ] common lifecycle
- [ ] meta-scenarios
- [ ] cross-gym receipts

## Pattern graph

- [P56 · Federated Gym Graph](../enterprise-operations/56-federated-gym-graph.md)
- [P59 · GgenGym](59-ggengym.md)
- [P62 · Autonomic Curriculum](62-autonomic-curriculum.md)
