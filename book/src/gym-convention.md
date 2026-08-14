# The `gym/` Convention

A repository usually has obvious places for implementation and narrow verification:

```text
src/
tests/
```

What is often missing is one canonical place for the executable answer to:

> What can this project actually do?

This language proposes:

```text
gym/
```

as that proof surface.

## Semantic roles

The exact physical layout may vary, but a gym should make these roles discoverable:

```text
gym/
├── manifest.*          # gym identity, runner, world/scenario catalog
├── worlds/             # resettable execution environments
├── scenarios/          # admitted behavioral objectives
├── fixtures/           # controlled observations and inputs
├── assertions/         # postconditions and independent verifiers
└── receipts/           # references or retained local evidence
```

A `gym/` directory is **not** simply another test directory.

- `tests/` primarily answers whether implementation units and interfaces behave correctly.
- `examples/` primarily communicates how a capability is used.
- `playground/` primarily permits experimentation.
- `gym/` answers whether an admitted capability can be exercised end to end against a bounded world and produce defensible evidence.

A gym can contain readable examples and exploratory scenarios, but they acquire stronger meaning when the same scenario can run through an evidence-producing lifecycle.

## Three distinct gym levels

### Pack gym

A pack gym proves:

> Can this manufacturing process produce what it claims?

Typical world: an empty or minimal consumer.

Typical crown: generate, build, run, verify, regenerate.

### Project gym

A project gym proves:

> Does this exact manufactured project instance actually behave as claimed?

Typical world: the project's admitted sandbox or external provider.

Typical crown: exact-subject behavior + independent postcondition + receipt.

### GgenGym

GgenGym proves:

> Does the manufacturer itself behave correctly across pack resolution, ontology admission, deterministic projection, drift, composition, and refusal?

Typical worlds include empty consumers, existing consumers, multi-pack consumers, invalid graphs, projection ownership collisions, repeat-sync, and intentionally broken toolchains.

These are separate standing claims:

\[
PACK\_ALIVE \neq INSTANCE\_ALIVE \neq MANUFACTURER\_ALIVE
\]

Evidence may compose, but none of these statuses should be silently inherited.
