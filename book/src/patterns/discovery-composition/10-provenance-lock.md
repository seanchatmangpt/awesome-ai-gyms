# P10 · Provenance Lock { #p10 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P10`

## Context

Registry data or exemplars are imported from external sources.

## Problem

Mutable upstream descriptions make it impossible to know which source observation produced a local fact.

## Forces

- Upstreams rewrite README files and branches.
- Copying descriptions creates licensing and drift concerns.
- Exact commits are noisier than friendly links.

## Resolution

**Record every imported fact with source identity and exact source revision. Preserve upstream canonical links while locking the observation to the revision actually inspected.**

## Consequences

Discovery becomes replayable and disputes can be resolved against the observed source.

## Falsifier

A registry fact cites only a mutable branch or homepage and cannot be traced to the observed revision.

## Evidence contract

- [ ] source code/identifier
- [ ] exact commit or revision
- [ ] retrieval timestamp
- [ ] field-level or row-level provenance

## Pattern graph

- [P02 · Canonical Subject](../foundations/02-canonical-subject.md)
- [P09 · Possibility Registry](09-possibility-registry.md)
- [P44 · Exact Subject Binding](../evidence-learning/44-exact-subject-binding.md)
