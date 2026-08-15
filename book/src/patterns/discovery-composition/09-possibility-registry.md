# P09 · Possibility Registry { #p09 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P09`

## Context

Many candidate gyms, benchmarks, environments, simulators, planners, or adapters exist.

## Problem

Choosing too early collapses the option graph and turns discovery into an implicit architecture decision.

## Forces

- Catalogs want simple rankings.
- Compatibility is contextual.
- New candidates appear faster than they can be fully qualified.

## Resolution

**Maintain a broad, provenance-preserving registry whose default standing is UNKNOWN and whose authority is NONE. Store facts needed for later selection without pretending discovery is qualification.**

## Consequences

The ecosystem preserves optionality and can improve selectors independently of the catalog.

## Falsifier

Adding an item to the catalog automatically installs, admits, ranks, or authorizes it.

## Evidence contract

- [ ] canonical reference
- [ ] provenance
- [ ] kind/category
- [ ] default UNKNOWN standing
- [ ] explicit NONE authority

## Pattern graph

- [P11 · Candidate Is Not Capability](11-candidate-is-not-capability.md)
- [P10 · Provenance Lock](10-provenance-lock.md)
- [P12 · Compatibility Edge](12-compatibility-edge.md)
