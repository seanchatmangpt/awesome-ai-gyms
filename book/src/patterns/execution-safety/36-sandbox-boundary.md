# P36 · Sandbox Boundary { #p36 }

> **Family:** [V · Execution and Safety](../execution-safety.md)  
> **Confidence:** ★★★  
> **Canonical ID:** `P36`

## Context

A gym needs shell, filesystem, browser, network, process, or device capabilities.

## Problem

A nominally bounded task can escape through shared host state and invalidate both safety and reproducibility.

## Forces

- Strong isolation can be expensive.
- Network access is often necessary.
- Filesystem and subprocess capabilities share hidden state.

## Resolution

**Declare one execution world for coupled capabilities and confine them with the strongest practical isolation boundary. Expose network, mounts, credentials, devices, and host bridges explicitly as admitted capabilities.**

## Consequences

Tool behavior becomes attributable to a concrete environment.

## Falsifier

A scenario depends on undeclared host files, credentials, processes, or network routes.

## Evidence contract

- [ ] sandbox identity
- [ ] mount/network/device policy
- [ ] resource limits
- [ ] escape tests

## Pattern graph

- [P01 · Bounded World](../foundations/01-bounded-world.md)
- [P37 · Idempotent Reset](37-idempotent-reset.md)
- [P51 · Exact Runtime Pin](../enterprise-operations/51-exact-runtime-pin.md)
