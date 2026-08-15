# P47 · Failure Becomes Law { #p47 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P47`

## Context

A scenario reveals a defect, unsafe edge, ambiguity, or unsupported assumption.

## Problem

Fixing only the immediate instance allows the same class of failure to recur elsewhere.

## Forces

- Permanent guards add maintenance.
- Not every failure generalizes.
- Overgeneralization can remove valid possibilities.

## Resolution

**After root-cause localization, encode the narrowest reusable prevention as ontology constraint, admission rule, typed refusal, fixture, schema, theorem, regression scenario, or verifier condition.**

## Consequences

The ecosystem compounds learning: defects shrink the invalid region of future search.

## Falsifier

The same failure class recurs because the repair changed implementation behavior but added no durable guard or regression evidence.

## Evidence contract

- [ ] root cause
- [ ] scope
- [ ] new guard/law
- [ ] regression scenario
- [ ] passing receipt

## Pattern graph

- [P39 · Failure Is Topology](../execution-safety/39-failure-is-topology.md)
- [P23 · Falsifier First](../planning-selection/23-falsifier-first.md)
- [P62 · Autonomic Curriculum](../self-manufacturing/62-autonomic-curriculum.md)
