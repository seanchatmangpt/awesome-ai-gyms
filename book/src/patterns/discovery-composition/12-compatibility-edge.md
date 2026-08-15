# P12 · Compatibility Edge { #p12 }

> **Family:** [II · Discovery and Composition](../discovery-composition.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P12`

## Context

A candidate may work with some planners, runtimes, operating systems, models, or adapters and fail with others.

## Problem

A single compatibility boolean destroys useful topology and encourages global rejection after one local failure.

## Forces

- Compatibility is relational.
- Many edges are initially unknown.
- Testing every pair is expensive.

## Resolution

**Model compatibility as typed edges between exact versions of subjects, providers, planners, worlds, and execution modes. Default each edge to UNKNOWN until evidence changes it.**

## Consequences

One failure removes one edge instead of one node. DFCM can preserve the rest of the graph.

## Falsifier

A failed integration causes the candidate to be globally marked unusable without proving failures on other edges.

## Evidence contract

- [ ] edge endpoints
- [ ] compatibility type
- [ ] evidence state
- [ ] failure/refusal reason
- [ ] receipt when executed

## Pattern graph

- [P39 · Failure Is Topology](../execution-safety/39-failure-is-topology.md)
- [P09 · Possibility Registry](09-possibility-registry.md)
- [P14 · Capability Seam](14-capability-seam.md)
