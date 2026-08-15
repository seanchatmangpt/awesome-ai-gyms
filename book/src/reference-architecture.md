# Reference Architecture

The DFCM reference architecture is organized around causal responsibility, not around vendor products. A concrete implementation may collapse several planes into one process or distribute one plane across many services. The semantic boundaries must remain observable even when the deployment topology changes.

## Seven planes

### 1. Knowledge and semantic plane

Owns canonical identities, ontologies, constraints, policies, capability contracts, and stable relationships.

Primary patterns: [Canonical Subject](patterns/foundations/02-canonical-subject.md), [Ontology First](patterns/manufacture/25-ontology-first.md), [Governance Graph](patterns/enterprise-operations/54-governance-graph.md).

This plane may state that an action type exists or that a subject has a relationship. It does not authorize DO.

### 2. Possibility plane

Owns discovered candidates, compatibility edges, provider alternatives, world adapters, formulations, and reversible compositions.

Primary patterns: [Possibility Registry](patterns/discovery-composition/09-possibility-registry.md), [Compatibility Edge](patterns/discovery-composition/12-compatibility-edge.md), [Combinatorial Maximalism](patterns/self-manufacturing/63-combinatorial-maximalism.md).

Default candidate standing is UNKNOWN. Discovery grants no trust and no authority.

### 3. Selection and planning plane

Owns objectives, planners, optimization, partial orders, candidate schedules, simulations, and powerless intents.

Primary patterns: [Planner League](patterns/planning-selection/17-planner-league.md), [Constraint Fence](patterns/planning-selection/22-constraint-fence.md), [Selection Is Not Authorization](patterns/planning-selection/24-selection-is-not-authorization.md).

A selected intent can still be refused at admission or authority.

### 4. Manufacture plane

Owns deterministic construction from admitted semantics: code, configuration, tests, deployment plans, policy projections, reports, and executable packages.

Primary patterns: [Deterministic Projection](patterns/manufacture/30-deterministic-projection.md), [Generated Is Canonical](patterns/manufacture/31-generated-is-canonical.md), [Pack Gym](patterns/manufacture/28-pack-gym.md).

Manufacture is reproducible construction, not consequence.

### 5. Consequence plane

Owns the transition from intent to world mutation.

Primary patterns: [Consequence Boundary](patterns/foundations/06-consequence-boundary.md), [BRCE Is the Only DO](patterns/execution-safety/33-brce-is-the-only-do.md), [Zero Unreceipted Actuation](patterns/execution-safety/34-zero-unreceipted-actuation.md).

This plane is deliberately small. It is the highest-value target for formalization, hardening, isolation, and audit because it owns actual consequence.

### 6. Evidence plane

Owns independent observation, verification, receipts, event projection, replay, and standing derivation.

Primary patterns: [Independent Postcondition](patterns/execution-safety/40-independent-postcondition.md), [Receipt DAG](patterns/evidence-learning/45-receipt-dag.md), [Replay Equivalence](patterns/evidence-learning/46-replay-equivalence.md).

The evidence plane must not simply echo executor success.

### 7. Operations and learning plane

Owns maturity, release crowns, capability certification, process intelligence, budgets, incidents, federation, and conversion of failure into durable law.

Primary patterns: [Release Crown](patterns/enterprise-operations/55-release-crown.md), [Failure Becomes Law](patterns/evidence-learning/47-failure-becomes-law.md), [Closed Causal Loop](patterns/self-manufacturing/64-closed-causal-loop.md).

## Reference flow

```text
             ┌─────────────────────────────┐
             │ Knowledge / Governance Graph│
             └──────────────┬──────────────┘
                            │
                            v
┌──────────────┐     ┌──────────────┐
│ Possibility  │────>│ Select / Plan│
│ Graph        │     │ powerless    │
└──────┬───────┘     └──────┬───────┘
       │                     │ intent
       │                     v
       │              ┌──────────────┐
       └─────────────>│ Admission +  │
                      │ Authority    │
                      └──────┬───────┘
                             │ admitted intent
                             v
                    ┌─────────────────┐
                    │ BRCE / DO       │
                    │ consequence     │
                    └────────┬────────┘
                             │
                             v
                    ┌─────────────────┐
                    │ Independent     │
                    │ Verification    │
                    └────────┬────────┘
                             │
                             v
                    ┌─────────────────┐
                    │ Receipt + Replay│
                    └────────┬────────┘
                             │
                             v
                    ┌─────────────────┐
                    │ Standing / Learn│
                    └─────────────────┘
```

Construction can occur before authority when it remains reversible. A system may manufacture a deployment package while still lacking deployment authority. The package is an artifact; deployment is a distinct DO transition.

## Trust zones

### Untrusted proposal zone

Inputs include user text, model outputs, planner outputs, external metadata, webhook payloads, generated tool calls, and third-party discovery. These inputs may enrich the possibility graph. They cannot directly mutate trusted state.

### Admitted semantic zone

Contains validated identities, schemas, policies, constraints, normalized intents, and deterministic construction inputs. Admission proves structural and policy eligibility, not execution success.

### Authorized consequence zone

Contains the minimum code and credentials required to cross the consequence boundary. This zone should have the narrowest interfaces, strongest isolation, explicit capabilities, and mandatory receipt production.

### Evidence zone

Contains observations and receipts used to establish standing. Verifiers should use an observation path independent enough to detect executor optimism or correlated failure.

## Control, data, and evidence planes

The **control plane** carries identity, admission, authority, policy, budgets, standing, and release criteria.

The **data plane** carries workload inputs, outputs, model payloads, files, messages, and domain data.

The **evidence plane** records what actually happened across both.

An enterprise can replace a model provider or storage system without changing control meaning when these planes are separated by capability seams.

## Event model

Each consequential lifecycle should project events such as:

```text
subject_resolved
observation_recorded
admission_granted | admission_refused
intent_selected
artifact_manufactured
authority_granted | authority_denied
actuation_started
actuation_result_observed
postcondition_verified | postcondition_failed
receipt_emitted
replay_started
replay_compared
standing_changed
law_updated
```

Events reference objects; they do not flatten objects into log strings. [OCEL Event Spine](patterns/evidence-learning/41-ocel-event-spine.md) provides the object-centric projection needed for process analysis.

## Deployment topology

The architecture does not require one centralized service. A global enterprise can federate local consequence brokers while sharing common semantics and evidence contracts.

A valid federation preserves:

- stable subject identity,
- attributable policy and evidence,
- local authority,
- explicit trust mappings,
- no exported ambient credentials,
- replayable cross-domain claims.

A central graph may know that a regional broker has a capability without possessing the credential to invoke it.

## Failure containment

Each plane must fail at its own boundary.

- Discovery failures change candidate topology.
- Planning failures change formulation or selector evidence.
- Construction failures produce BUILD_BROKEN or a manufacturing defect.
- Admission failures produce typed REFUSED or BLOCKED.
- Authority failures deny DO.
- Execution failures produce partial/failure receipts.
- Verification failures prevent ALIVE standing.
- Replay failures narrow the evidence claim.
- Release-crown gaps block only the affected release scope.

This prevents one red status from becoming an untyped system-wide conclusion.

## Reference deployment contract

A production capability should be able to publish the following machine-readable surfaces:

1. subject resolver,
2. world/scenario catalog,
3. capability contracts,
4. admission schema,
5. authority capability schema,
6. consequence inventory,
7. verifier catalog,
8. receipt schema,
9. replay manifest schema,
10. standing API,
11. event/object projection,
12. release-crown manifest.

The product interface can vary. The causal contract cannot.
