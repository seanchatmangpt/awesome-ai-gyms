# Discovery and Composition

How to preserve a large ecosystem of candidates without converting discovery into authority.

## 9. Possibility Registry ★★★

**Context.** Many candidate gyms, benchmarks, environments, simulators, planners, or adapters exist.

**Problem.** Choosing too early collapses the option graph and turns discovery into an implicit architecture decision.

**Forces.**

- Catalogs want simple rankings.
- Compatibility is contextual.
- New candidates appear faster than they can be fully qualified.

**Therefore:** **Maintain a broad, provenance-preserving registry whose default standing is UNKNOWN and whose authority is NONE. Store facts needed for later selection without pretending discovery is qualification.**

**Consequences.** The ecosystem preserves optionality and can improve selectors independently of the catalog.

**Falsifier.** Adding an item to the catalog automatically installs, admits, ranks, or authorizes it.

**Evidence.**

- [ ] canonical reference
- [ ] provenance
- [ ] kind/category
- [ ] default UNKNOWN standing
- [ ] explicit NONE authority

**Connects to.** Candidate Is Not Capability, Provenance Lock, Compatibility Edge.

---

## 10. Provenance Lock ★★★

**Context.** Registry data or exemplars are imported from external sources.

**Problem.** Mutable upstream descriptions make it impossible to know which source observation produced a local fact.

**Forces.**

- Upstreams rewrite README files and branches.
- Copying descriptions creates licensing and drift concerns.
- Exact commits are noisier than friendly links.

**Therefore:** **Record every imported fact with source identity and exact source revision. Preserve upstream canonical links while locking the observation to the revision actually inspected.**

**Consequences.** Discovery becomes replayable and disputes can be resolved against the observed source.

**Falsifier.** A registry fact cites only a mutable branch or homepage and cannot be traced to the observed revision.

**Evidence.**

- [ ] source code/identifier
- [ ] exact commit or revision
- [ ] retrieval timestamp
- [ ] field-level or row-level provenance

**Connects to.** Canonical Subject, Possibility Registry, Exact Subject Binding.

---

## 11. Candidate Is Not Capability ★★★

**Context.** A discovered project appears to offer useful functionality.

**Problem.** Presence in a list, a README claim, import success, or a CI badge is easily mistaken for demonstrated local capability.

**Forces.**

- Humans use social proof as a shortcut.
- Documentation is cheap to produce.
- Compatibility can fail only at runtime boundaries.

**Therefore:** **Represent discovery as candidate status only. Promote to capability standing only after exact-subject execution through the relevant admitted world and verifier.**

**Consequences.** The registry can be generous while execution claims remain conservative.

**Falsifier.** A candidate receives ALIVE or capability standing without an observed exact-subject run and receipt.

**Evidence.**

- [ ] candidate standing
- [ ] separate compatibility state
- [ ] execution receipt reference for promotions

**Connects to.** Standing Ladder, Compatibility Edge, Possibility Registry.

---

## 12. Compatibility Edge ★★★

**Context.** A candidate may work with some planners, runtimes, operating systems, models, or adapters and fail with others.

**Problem.** A single compatibility boolean destroys useful topology and encourages global rejection after one local failure.

**Forces.**

- Compatibility is relational.
- Many edges are initially unknown.
- Testing every pair is expensive.

**Therefore:** **Model compatibility as typed edges between exact versions of subjects, providers, planners, worlds, and execution modes. Default each edge to UNKNOWN until evidence changes it.**

**Consequences.** One failure removes one edge instead of one node. DFCM can preserve the rest of the graph.

**Falsifier.** A failed integration causes the candidate to be globally marked unusable without proving failures on other edges.

**Evidence.**

- [ ] edge endpoints
- [ ] compatibility type
- [ ] evidence state
- [ ] failure/refusal reason
- [ ] receipt when executed

**Connects to.** Failure Is Topology, Possibility Registry, Capability Seam.

---

## 13. Reversible Composition ★★★

**Context.** A gym is assembled from providers, plugins, adapters, tools, models, or policies.

**Problem.** Composition becomes fragile when adding one capability mutates global state or requires patching a privileged core.

**Forces.**

- Plugins need lifecycle ordering.
- Shared state is convenient.
- Experiments benefit from swapping implementations.

**Therefore:** **Prefer compositions whose registrations and effects are scoped, replaceable, and unwindable. Treat configuration as a graph that can be constructed, compared, and discarded before DO.**

**Consequences.** The search space stays large while experiment teardown stays cheap.

**Falsifier.** Removing or replacing one component leaves hidden state that changes subsequent runs.

**Evidence.**

- [ ] component graph
- [ ] lifecycle hooks
- [ ] teardown/reset proof
- [ ] dependency declaration

**Connects to.** Capability Seam, Combinatorial Maximalism, Idempotent Reset.

---

## 14. Capability Seam ★★★

**Context.** Multiple providers can implement the same useful behavior.

**Problem.** Consumers coupled to concrete implementations fragment the ecosystem and make experiments incomparable.

**Forces.**

- Interfaces can be too weak or too vendor-specific.
- Provider swaps may change semantics.
- Tools often mix definition, implementation, and policy.

**Therefore:** **Define each capability as a service contract with explicit provider and consumer roles, semantic pre/postconditions, and a common evidence surface. Provider identity remains visible in receipts.**

**Consequences.** Whole classes of implementations become swappable without pretending they are behaviorally identical.

**Falsifier.** A provider swap requires modifying unrelated consumers or hides provider identity from evidence.

**Evidence.**

- [ ] service definition
- [ ] provider contract
- [ ] consumer contract
- [ ] provider identity in run evidence

**Connects to.** Compatibility Edge, World Adapter, Local Bridge.

---

## 15. World Adapter ★★★

**Context.** An external benchmark or runtime needs to participate in the gym lifecycle.

**Problem.** Forking the external system to fit local semantics destroys provenance and creates a maintenance branch.

**Forces.**

- External APIs vary wildly.
- The local lifecycle must remain stable.
- Adapters can accidentally inherit authority.

**Therefore:** **Wrap external systems with a thin adapter that maps local reset/observe/intent/execute/verify semantics to the provider without changing provider internals. Keep authority in GymAct, not in the adapter.**

**Consequences.** Upstream identity stays intact and provider upgrades remain tractable.

**Falsifier.** The adapter performs unbrokered side effects or requires a permanent fork merely to satisfy local lifecycle semantics.

**Evidence.**

- [ ] adapter boundary
- [ ] provider revision
- [ ] mapping tests
- [ ] no ambient authority

**Connects to.** Capability Seam, Local Bridge, Project Gym.

---

## 16. Local Bridge ★★★

**Context.** A project needs ecosystem-specific semantics that should not contaminate a shared upstream pack or provider.

**Problem.** Putting every local convention into global infrastructure causes coupling and pack explosion.

**Forces.**

- Local projects need flexibility.
- Shared packs need stable boundaries.
- Bridges can become dumping grounds.

**Therefore:** **Place project-specific semantic mappings in a consumer-local bridge pack or adapter. Keep the shared pack focused on the reusable manufacturing boundary and make the bridge explicitly dependent on it.**

**Consequences.** Local specialization remains possible without forking ecosystem-wide law.

**Falsifier.** A shared pack contains one-off project assumptions that cannot be justified outside a single consumer.

**Evidence.**

- [ ] bridge ownership
- [ ] explicit dependency
- [ ] local ontology mappings
- [ ] local gym scenarios

**Connects to.** One Pack, One Manufacturing Boundary, World Adapter, Project Gym.

---
