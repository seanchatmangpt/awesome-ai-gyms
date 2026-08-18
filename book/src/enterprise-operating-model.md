# Enterprise Operating Model

DFCM changes operating responsibility more than it changes organization charts. The objective is not to create a new “AI team” that owns every model call. It is to establish clear ownership for semantics, authority, consequence, verification, evidence, and release across existing business capabilities.

## Organize around capability boundaries

A capability is a bounded promise with preconditions, postconditions, authority requirements, and evidence. Examples include “provision an approved development environment,” “reconcile an invoice,” “publish a catalog change,” or “promote a qualified pack.”

The operating unit should own the capability contract, not every implementation that may satisfy it.

A provider can change from human procedure to deterministic software to optimizer to model-assisted planner without changing the enterprise meaning of the capability.

## Seven accountabilities

Every consequential capability needs explicit owners for seven functions.

| Accountability | Owns | Must not silently own |
|---|---|---|
| Semantic owner | meaning, identity, constraints, business invariants | execution credentials |
| World owner | state boundary, reset, observation contract | release standing |
| Policy owner | obligations, prohibitions, admission rules | optimizer objective by implication |
| Authority issuer | scoped capability to cause consequence | semantic validity |
| Executor owner | BRCE implementation and consequence adapter | independent verification |
| Verifier owner | postconditions and acceptance observations | executor success narrative |
| Evidence/release owner | receipt retention, replay, crown composition | retroactive redefinition of success |

One person or team may hold multiple accountabilities. The distinctions must remain explicit in the artifacts.

## Decision rights

### Reversible design rights

Teams may explore ontologies, candidate providers, planners, formulations, templates, and simulations broadly within cost and information-security constraints.

### Admission rights

Policy and semantic authorities decide whether a candidate transition lies inside the allowed region. Admission is usually automatable because the rules should be machine-visible.

### Consequence rights

Authority issuers delegate narrowly scoped capabilities to BRCE or equivalent brokers. Credentials and effectful APIs live here.

The same component should not acquire consequence rights merely because it produced a good plan.

## Portfolio governance

At portfolio scale, maintain four graphs rather than one roadmap.

1. **Capability graph** — what the enterprise must be able to do.
2. **Possibility graph** — alternative providers, planners, packs, worlds, and formulations.
3. **Governance graph** — authorities, policies, obligations, prohibitions, and ownership.
4. **Evidence graph** — receipts, standing, maturity, failures, and release crowns.

A portfolio decision can then ask which capability has the highest expected verified consequence per constrained cost and attention, rather than which project has the most persuasive status deck.

## Work intake

A new automation initiative enters through an outcome contract:

```text
business outcome
exact subject class
world boundary
observation sources
allowed consequence classes
forbidden consequence classes
authority source
falsifier
independent verifier
evidence retention
resource budget
release crown
```

If the consequence boundary is unknown, the initiative remains in discovery/modeling. It does not proceed by attaching tools to a model and learning the authority model in production.

## Change management

Change is classified by the boundary it affects.

### Semantic change

Changes meaning, identity, ontology, constraints, or capability contracts. Requires compatibility analysis and regenerated projections.

### Selection change

Changes planner, model, ranking policy, objective weights, or formulation. Because selection is powerless, this can often move quickly if downstream contracts remain fixed.

### Construction change

Changes packs, templates, compiler, generator, or deterministic projection. Requires regeneration and behavioral qualification.

### Authority change

Changes who or what may cause consequences. Requires explicit policy review and capability issuance/revocation evidence.

### Consequence-adapter change

Changes the implementation that mutates external state. Requires independent postcondition verification and focused regression.

### Evidence change

Changes verifier, receipt schema, replay predicate, or standing derivation. This can invalidate historical comparability and must be versioned deliberately.

This classification avoids applying the same approval process to a harmless selector experiment and a new payment authority.

## Human participation

Humans are modeled as actors with capabilities, not as an undefined safety blanket.

A human review step should state:

- what information the reviewer observes,
- what decision they own,
- what authority they exercise,
- what evidence their decision produces,
- what happens on timeout or disagreement,
- whether the decision can be replayed or audited.

If a human simply clicks “approve” without a bounded decision contract, the system has created latency without necessarily creating control.

## Service management integration

DFCM does not require abandoning incident, change, service, or risk-management systems. Those systems become projections or interfaces around the canonical evidence.

- an incident record can reference receipt IDs and affected subject IDs;
- a change request can reference a governance-graph delta;
- a service catalog can publish capability standing;
- a risk register can reference falsifiers and unresolved UNKNOWN edges;
- an audit package can be generated from the receipt DAG.

The enterprise avoids copying causal truth into disconnected prose systems.

## Escalation policy

Escalation is triggered by typed state transitions, not by generic “AI confidence.”

- `UNKNOWN → BLOCKED`: dependency or authority unavailable; route to dependency owner.
- `PARTIAL_ALIVE → BUILD_BROKEN`: toolchain or construction regression; route to manufacturer owner.
- `ALIVE → PARTIAL_ALIVE`: evidence expired or replay failed; freeze promotion while preserving prior receipts.
- `intent → REFUSED(policy)`: route only if policy exception is legitimately requested.
- `verified consequence → postcondition failure`: open an incident against the consequence path even if the executor returned success.

## Executive cadence

The useful enterprise review is a crown review, not a demo review.

Executives should see:

- capabilities by standing,
- maturity floor by plane,
- unclosed release crowns,
- new typed refusals and their causes,
- failed compatibility edges,
- budget consumption,
- replay health,
- evidence age,
- newly learned law,
- concentration of consequence authority.

A healthy program can explain why some capabilities remain UNKNOWN. Artificially converting unknowns to green is an anti-pattern.

## Organizational end state

The end state is an organization in which semantics, authority, and evidence survive implementation changes.

Teams can adopt new planners, models, deterministic generators, or providers rapidly because those components live inside explicit capability seams. High-risk consequence remains bounded because the authority surface is small. Operating knowledge compounds because every significant failure can become machine-visible law.

That is the enterprise value of the pattern language: **fast reversible change, slow implicit authority, and durable causal evidence**.
