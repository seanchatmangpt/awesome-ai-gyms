# P31 · Generated Is Canonical { #p31 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P31`

## Context

A deterministic manufacturer writes source, config, tests, or docs into a consumer project.

## Problem

Separating generated output into a second-class directory encourages manual shadows, wrapper layers, and confusion about which artifact is authoritative.

## Forces

- Developers are used to `do not edit generated` trees.
- Some artifacts are genuinely transient.
- Canonical ownership must be explicit.

## Resolution

**Where ggen owns an artifact, write it directly to its canonical project location and make ownership/provenance machine-visible. Regeneration, not a parallel handwritten copy, repairs drift.**

## Consequences

Generated source participates in normal builds and interfaces without architectural stigma.

## Falsifier

The project maintains a handwritten canonical file plus a generated near-duplicate because generated artifacts are not trusted as first-class outputs.

## Evidence contract

- [ ] artifact owner
- [ ] projection provenance
- [ ] drift detector
- [ ] regeneration path

## Pattern graph

- [P30 · Deterministic Projection](30-deterministic-projection.md)
- [P25 · Ontology First](25-ontology-first.md)
- [P32 · Project Gym](32-project-gym.md)
