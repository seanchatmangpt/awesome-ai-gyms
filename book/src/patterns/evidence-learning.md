# Evidence and Learning

How execution becomes defensible evidence, replay, process knowledge, and durable law.

## 41. OCEL Event Spine ★★☆

**Context.** A gym produces many episodes, transitions, tool calls, plans, receipts, and objects.

**Problem.** Ad hoc logs make cross-run process analysis and causal comparison difficult.

**Forces.**

- Events involve multiple objects.
- Runtime logs are provider-specific.
- Process mining needs stable event/object semantics.

**Therefore:** **Project execution evidence onto an object-centric event log with stable event types, object identities, relationships, timestamps, and receipt links. Keep raw evidence available behind the projection.**

**Consequences.** Process mining, conformance analysis, and cross-world learning can operate on a common behavioral spine.

**Falsifier.** A claimed process metric cannot be traced back to concrete execution events and subject objects.

**Evidence.**

- [ ] event schema
- [ ] object identities
- [ ] event-object relations
- [ ] receipt links
- [ ] raw evidence references

**Connects to.** Explicit Observation, Receipt DAG, Cross-World Comparison.

---

## 42. Observation vs Inference ★★★

**Context.** A system derives semantic conclusions from runtime evidence.

**Problem.** Derived claims often become indistinguishable from directly observed facts, allowing model outputs or heuristics to masquerade as execution evidence.

**Forces.**

- Inference is necessary for useful summaries.
- Raw observations can be noisy.
- Multiple derivations may disagree.

**Therefore:** **Store observed, admitted, executed, changed, verified, inferred, refused, blocked, and unsupported states separately. Record derivation provenance for inferred facts.**

**Consequences.** Reasoning can be rich without weakening the evidentiary boundary.

**Falsifier.** An inferred compatibility or success claim is stored as though it were directly observed execution.

**Evidence.**

- [ ] fact status/type
- [ ] source observation
- [ ] derivation/proof identity
- [ ] confidence where applicable

**Connects to.** Explicit Observation, Standing Ladder, OCEL Event Spine.

---

## 43. Standing Ladder ★★★

**Context.** Stakeholders need a compact status for a capability or subject.

**Problem.** Binary pass/fail collapses important differences between unknown, unsupported, blocked, broken, partially demonstrated, and fully demonstrated behavior.

**Forces.**

- Status must remain understandable.
- Granularity can explode.
- Standing must be scoped to evidence.

**Therefore:** **Use a small typed ladder such as UNKNOWN, PARTIAL_ALIVE, ALIVE, BLOCKED, BUILD_BROKEN, UNSUPPORTED, plus typed REFUSED. ALIVE requires observed execution against the exact admitted subject.**

**Consequences.** Status becomes actionable and evidence-bounded.

**Falsifier.** A documentation inspection, successful build, or workflow definition alone can produce ALIVE.

**Evidence.**

- [ ] status
- [ ] scope
- [ ] subject identity
- [ ] evidence/receipt
- [ ] falsifier for promotion

**Connects to.** Candidate Is Not Capability, Typed Refusal, Exact Subject Binding.

---

## 44. Exact Subject Binding ★★★

**Context.** Evidence is used to support a capability claim.

**Problem.** Evidence from a neighboring version, mock, generated substitute, or similar configuration can be mistakenly transferred to the target subject.

**Forces.**

- Reuse of prior evidence saves time.
- Small version changes may be behaviorally irrelevant.
- Subject equivalence is itself a claim.

**Therefore:** **Bind every standing claim to the exact subject and environment identities executed. Reuse evidence only when an explicit equivalence relation proves the relevant identities and configuration are interchangeable.**

**Consequences.** Evidence inheritance becomes lawful instead of anecdotal.

**Falsifier.** ALIVE standing for subject X is justified only by execution of subject Y without a proven equivalence relation.

**Evidence.**

- [ ] subject digest/revision
- [ ] environment identity
- [ ] config identity
- [ ] equivalence proof if reused
- [ ] receipt

**Connects to.** Canonical Subject, Receipt, Replay Equivalence.

---

## 45. Receipt DAG ★★★

**Context.** A workflow contains multiple manufactured artifacts, plans, admissions, executions, and verifications.

**Problem.** One flat final log cannot preserve the causal structure needed to audit or replay the workflow.

**Forces.**

- Evidence comes from different subsystems.
- Some branches are parallel.
- Failures may occur after partial success.

**Therefore:** **Link receipts into a DAG whose edges represent derivation, admission, execution, verification, replay, or dependency relationships. Each node remains independently inspectable.**

**Consequences.** Complex workflows retain causal history without forcing a total order.

**Falsifier.** A final success receipt cannot identify which exact upstream plan, artifact, authority decision, and verifier results it depended on.

**Evidence.**

- [ ] receipt identifiers
- [ ] typed edges
- [ ] subject lineage
- [ ] partial/failure nodes
- [ ] root release/crown node

**Connects to.** Receipt, Partial Order Before Total Order, Release Crown.

---

## 46. Replay Equivalence ★★★

**Context.** A replay is expected to demonstrate that prior evidence remains reproducible.

**Problem.** Bit identity is too strict for many stochastic or distributed systems, while vague 'similar results' is too weak.

**Forces.**

- Randomness can be legitimate.
- External timing varies.
- Users need domain-specific tolerances.

**Therefore:** **Define an equivalence predicate before replay: exact for deterministic artifacts, state-equivalent for resets, metric-bounded for stochastic evaluation, or semantically equivalent for allowed provider differences.**

**Consequences.** Replay claims become falsifiable across diverse worlds.

**Falsifier.** A replay is declared successful without a predeclared equivalence predicate.

**Evidence.**

- [ ] equivalence class/predicate
- [ ] tolerances
- [ ] replay inputs
- [ ] observed result
- [ ] replay receipt

**Connects to.** Replay, Exact Subject Binding, Cross-World Comparison.

---

## 47. Failure Becomes Law ★★★

**Context.** A scenario reveals a defect, unsafe edge, ambiguity, or unsupported assumption.

**Problem.** Fixing only the immediate instance allows the same class of failure to recur elsewhere.

**Forces.**

- Permanent guards add maintenance.
- Not every failure generalizes.
- Overgeneralization can remove valid possibilities.

**Therefore:** **After root-cause localization, encode the narrowest reusable prevention as ontology constraint, admission rule, typed refusal, fixture, schema, theorem, regression scenario, or verifier condition.**

**Consequences.** The ecosystem compounds learning: defects shrink the invalid region of future search.

**Falsifier.** The same failure class recurs because the repair changed implementation behavior but added no durable guard or regression evidence.

**Evidence.**

- [ ] root cause
- [ ] scope
- [ ] new guard/law
- [ ] regression scenario
- [ ] passing receipt

**Connects to.** Failure Is Topology, Falsifier First, Autonomic Curriculum.

---

## 48. Cross-World Comparison ★★☆

**Context.** A policy, planner, or architecture is evaluated across multiple gyms or world configurations.

**Problem.** Metrics with different task semantics, observation spaces, or consequence models are compared as though they measured the same capability.

**Forces.**

- Leadership wants one leaderboard.
- World difficulty varies.
- Useful transfer requires shared semantics without erasing differences.

**Therefore:** **Compare only through declared common dimensions and mappings. Preserve world-specific metrics alongside normalized projections, and attach every aggregate to its source receipts.**

**Consequences.** Cross-gym learning becomes defensible without manufacturing a false universal score.

**Falsifier.** A single aggregate score combines incomparable world metrics with no mapping or uncertainty model.

**Evidence.**

- [ ] world identities
- [ ] metric semantics
- [ ] normalization/mapping
- [ ] source receipts
- [ ] uncertainty

**Connects to.** OCEL Event Spine, Multiple Formulations, Capability Certification.

---
