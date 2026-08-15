# Pattern Grammar

A pattern is not a feature request and not a slogan. It is a reusable resolution to a recurring system tension under explicit boundaries.

## Canonical pattern object

Each pattern is a first-class node:

\[
P = (I, F, \kappa, C, Q, \Phi, S, K, X, E, N)
\]

where:

- \(I\) = stable canonical identity (`P01` … `P64`),
- \(F\) = family,
- \(\kappa\) = confidence,
- \(C\) = context,
- \(Q\) = recurring problem,
- \(\Phi\) = forces,
- \(S\) = bounded resolution,
- \(K\) = consequences,
- \(X\) = falsifier,
- \(E\) = evidence contract,
- \(N\) = neighboring pattern graph.

Identity, falsifier, evidence, and graph edges are mandatory. Without them, a pattern can become architectural theater or a paragraph trapped inside a chapter.

## Physical structure is part of the contract

Each pattern is one Markdown source file and therefore one mdBook chapter and one stable URL. Family pages are composition maps; they do not own the pattern bodies.

```text
patterns/
├── foundations.md
├── foundations/
│   ├── 01-bounded-world.md
│   ├── 02-canonical-subject.md
│   └── ...
├── discovery-composition.md
├── discovery-composition/
│   └── ...
└── ...
```

A leaf pattern uses the same page grammar:

```text
# Pxx · Name { #pxx }
metadata: family, confidence, canonical ID
## Context
## Problem
## Forces
## Resolution
## Consequences
## Falsifier
## Evidence contract
## Pattern graph
```

The explicit `{ #pxx }` heading ID makes the canonical anchor independent of future wording changes.

## `SUMMARY.md` is a projection, not the graph

The pattern language is a graph. mdBook requires a navigational hierarchy and total reading order, so `SUMMARY.md` is deterministically manufactured from the canonical leaf chapters by `scripts/generate_book_nav.py`.

That distinction is deliberate:

```text
canonical pattern nodes + family membership
                |
                v
      deterministic projection
                |
        +-------+-------+
        |               |
        v               v
    SUMMARY.md     pattern-index.md
```

Changing sidebar order cannot silently change a pattern's identity. Adding a pattern requires adding a first-class node, not hiding another section inside a family mega-page.

## Pattern scale

| Scale | Primary concern | Typical examples |
|---|---|---|
| Ecosystem | separation of responsibilities | discovery vs selection vs actuation |
| World | bounded state and transition semantics | reset, observation, consequence |
| Planning | reversible exploration | planner leagues, alternate formulations |
| Manufacture | deterministic projection | ontology-first generation, pack qualification |
| Actuation | authority and consequence | BRCE, typed refusal, sandboxing |
| Evidence | defensible claims | exact-subject receipts, replay equivalence |
| Operations | lifecycle governance | maturity floors, release crowns, federation |

A system is healthy when patterns at these scales compose without silently moving authority.

## The non-equivalences

```text
discovered != compatible
compatible != admitted
admitted != selected
selected != authorized
authorized != executed
executed != verified
verified != replayable
logged != receipted
workflow exists != workflow succeeded
candidate != capability
inspection != execution
```

## DFCM reading semantics

The sidebar is only one lawful linearization. DFCM preserves the neighboring-pattern graph and delays irreversible narrowing:

```text
Preserve
  -> Fence
  -> Model
  -> Admit
  -> Explore
  -> Select
  -> Manufacture
  -> Actuate
  -> Observe
  -> Verify
  -> Receipt
  -> Replay
  -> Learn
  -> Release
  -> Regenerate
```

Enter later only when the earlier obligations are already satisfied and evidenced. A failed edge narrows topology; it does not invalidate adjacent patterns or erase unrelated routes.
