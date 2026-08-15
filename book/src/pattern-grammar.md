# Pattern Grammar

A pattern is not a feature request and not a slogan. It is a reusable resolution to a recurring system tension under explicit boundaries.

## Canonical pattern form

Each pattern in this book can be represented as:

\[
P = (C, Q, F, S, K, X, E, N)
\]

where:

- \(C\) = context,
- \(Q\) = recurring problem,
- \(F\) = forces,
- \(S\) = bounded solution,
- \(K\) = consequences,
- \(X\) = falsifier,
- \(E\) = required evidence,
- \(N\) = neighboring patterns.

The falsifier and evidence fields are mandatory. Without them, a pattern can become architectural theater.

## Pattern scale

Patterns operate at several scales:

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

The following distinctions recur throughout the book and must remain explicit:

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

Most false confidence in AI infrastructure comes from collapsing one of these boundaries.

## Pattern sequences, not checklists

A pattern language is a graph. The sequence suggested by this book is:

```text
Preserve
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
```

You can enter later in the chain only if the earlier obligations are already satisfied and evidenced.
