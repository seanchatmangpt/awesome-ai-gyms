# P28 · Pack Gym { #p28 }

> **Family:** [IV · Manufacture and Packs](../manufacture.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P28`

## Context

A ggen pack claims it can manufacture a reusable capability.

## Problem

Template unit tests do not prove that the complete pack can manufacture, build, run, and reproduce a real consumer.

## Forces

- Pack qualification should be cheap enough for every release.
- Some consumers need local bridges.
- Generation success is weaker than behavior success.

## Resolution

**Place a gym with the pack that starts from controlled consumer worlds, runs the real ggen path, and verifies the manufactured capability through behavioral scenarios.**

## Consequences

The pack becomes an executable manufacturing contract rather than a bag of templates.

## Falsifier

A pack can be published as qualified even though no gym has manufactured and exercised an exact consumer instance.

## Evidence contract

- [ ] empty/minimal consumer world
- [ ] generation receipt
- [ ] consumer verifier
- [ ] repeat-sync or regeneration check

## Pattern graph

- [P29 · Marketplace Qualification](29-marketplace-qualification.md)
- [P32 · Project Gym](32-project-gym.md)
- [P57 · Empty Repo Crown](../self-manufacturing/57-empty-repo-crown.md)
