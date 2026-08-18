# P51 · Exact Runtime Pin { #p51 }

> **Family:** [VII · Enterprise and Operations](../enterprise-operations.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P51`

## Context

A gym depends on compilers, containers, models, packages, system libraries, or remote providers.

## Problem

Mutable toolchains create replays that appear identical at the source level but execute different machinery.

## Forces

- Security updates require movement.
- Fully hermetic environments are costly.
- Hosted services may not expose immutable identities.

## Resolution

**Pin every runtime dependency that materially affects behavior to an exact version or digest; record unavoidable remote uncertainty as an external dependency rather than pretending it is pinned.**

## Consequences

Local Capsule ALIVE evidence can be reused when identities actually match.

## Falsifier

A replay or release claim depends on `latest`, floating branches, or unrecorded hosted model revisions.

## Evidence contract

- [ ] toolchain manifest
- [ ] digests/versions
- [ ] external dependency declarations
- [ ] runtime identity in receipt

## Pattern graph

- [P02 · Canonical Subject](../foundations/02-canonical-subject.md)
- [P08 · Replay](../foundations/08-replay.md)
- [P52 · Capability Certification](52-capability-certification.md)
