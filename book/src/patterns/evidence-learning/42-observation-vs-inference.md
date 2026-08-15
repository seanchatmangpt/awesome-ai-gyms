# P42 · Observation vs Inference { #p42 }

> **Family:** [VI · Evidence and Learning](../evidence-learning.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P42`

## Context

A system derives semantic conclusions from runtime evidence.

## Problem

Derived claims often become indistinguishable from directly observed facts, allowing model outputs or heuristics to masquerade as execution evidence.

## Forces

- Inference is necessary for useful summaries.
- Raw observations can be noisy.
- Multiple derivations may disagree.

## Resolution

**Store observed, admitted, executed, changed, verified, inferred, refused, blocked, and unsupported states separately. Record derivation provenance for inferred facts.**

## Consequences

Reasoning can be rich without weakening the evidentiary boundary.

## Falsifier

An inferred compatibility or success claim is stored as though it were directly observed execution.

## Evidence contract

- [ ] fact status/type
- [ ] source observation
- [ ] derivation/proof identity
- [ ] confidence where applicable

## Pattern graph

- [P03 · Explicit Observation](../foundations/03-explicit-observation.md)
- [P43 · Standing Ladder](43-standing-ladder.md)
- [P41 · OCEL Event Spine](41-ocel-event-spine.md)
