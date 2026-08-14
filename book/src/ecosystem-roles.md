# Ecosystem Roles

The pattern language assumes four distinct responsibilities. Repositories may provide adapters for one another, but the responsibilities must not collapse.

## Awesome AI Gyms — DISCOVER + PRESERVE

The registry keeps the possibility graph large.

It may know that a gym exists, what kind of system it is, which source reported it, and which exact upstream revision was observed. It does **not** install the candidate, assert planner compatibility, authorize a transition, or confer ALIVE standing.

Default authority: **NONE**.

Default candidate standing: **UNKNOWN**.

## AutoFDE-Lab — SELECT + PLAN

AutoFDE-Lab explores compatible planner and formulation spaces. It may select a candidate gym, planner, policy, plan, or intervention.

Its output is a **powerless intent or plan**. Selection is not authorization.

Default authority from the registry feed: **SELECT_ONLY**.

## ggen ecosystem — CONSTRUCT

The ggen ecosystem turns admitted semantics into deterministic artifacts.

- **ggen-create** discovers and authors reusable pack law from exemplars and requirements.
- **ggen packs** package one coherent manufacturing boundary.
- **ggen-marketplace** distributes qualified packs and their evidence.
- **ggen** resolves, composes, admits, and deterministically projects canonical artifacts.
- **pack gyms** prove manufacturing processes.
- **project gyms** prove manufactured instances.

Construction has no ambient authority to perform external DO transitions merely because it emitted executable files.

## GymAct / BRCE — OBSERVE + DO + VERIFY + RECEIPT/REPLAY

GymAct owns the world execution boundary. BRCE is the exclusive DO path.

A normal lifecycle is:

```text
parse
  -> route
  -> admit/refuse
  -> diagnose/repair
  -> construct
  -> actuate through BRCE
  -> observe consequence
  -> independently verify
  -> receipt
  -> replay/hook
  -> standing
```

Hooks manufacture intents; they do not actuate.

## The correspondence

```text
registry candidate
      |
      v
planner selection
      |
      v
admitted semantic graph
      |
      v
ggen manufacture
      |
      v
project gym scenario
      |
      v
GymAct admission
      |
      v
BRCE consequence
      |
      v
independent verifier
      |
      v
receipt + replay
      |
      v
scoped standing
```

Each boundary exists so that the layer above it can remain more generative without inheriting the authority of the layer below it.
