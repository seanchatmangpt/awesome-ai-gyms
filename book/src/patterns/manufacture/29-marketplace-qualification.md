# P29 · Marketplace Qualification { #p29 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P29`

## Context

Reusable packs must be distributed across projects.

## Problem

A package registry can easily become an app store where publication is mistaken for behavioral trust.

## Forces

- Fast publishing encourages experimentation.
- Consumers need provenance and dependency closure.
- Qualification evidence can expire as dependencies move.

## Resolution

**Treat the marketplace as a governed supply plane: publish pack identity, dependencies, provenance, compatibility claims, and qualification receipts. Installation grants no execution authority.**

## Consequences

Consumers can resolve trusted manufacturing inputs without collapsing distribution and execution.

## Falsifier

A published or downloaded pack is automatically considered ALIVE in the consuming environment.

## Evidence contract

- [ ] pack digest/version
- [ ] dependency lock
- [ ] qualification state
- [ ] receipt references
- [ ] revocation/supersession metadata

## Pattern graph

- [P28 · Pack Gym](28-pack-gym.md)
- [P11 · Candidate Is Not Capability](../discovery-composition/11-candidate-is-not-capability.md)
- [P51 · Exact Runtime Pin](../enterprise-operations/51-exact-runtime-pin.md)
