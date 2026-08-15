# P14 · Capability Seam { #p14 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P14`

## Context

Multiple providers can implement the same useful behavior.

## Problem

Consumers coupled to concrete implementations fragment the ecosystem and make experiments incomparable.

## Forces

- Interfaces can be too weak or too vendor-specific.
- Provider swaps may change semantics.
- Tools often mix definition, implementation, and policy.

## Resolution

**Define each capability as a service contract with explicit provider and consumer roles, semantic pre/postconditions, and a common evidence surface. Provider identity remains visible in receipts.**

## Consequences

Whole classes of implementations become swappable without pretending they are behaviorally identical.

## Falsifier

A provider swap requires modifying unrelated consumers or hides provider identity from evidence.

## Evidence contract

- [ ] service definition
- [ ] provider contract
- [ ] consumer contract
- [ ] provider identity in run evidence

## Pattern graph

- [P12 · Compatibility Edge](12-compatibility-edge.md)
- [P15 · World Adapter](15-world-adapter.md)
- [P16 · Local Bridge](16-local-bridge.md)
