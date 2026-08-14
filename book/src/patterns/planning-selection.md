# Planning and Selection

How to search, formulate, compare, and select while keeping plans powerless until admitted.

## 17. Planner League ★★★

**Context.** A problem can be expressed to multiple planning algorithms or solver families.

**Problem.** Treating one planner or one LLM as the universal decision maker hides formulation sensitivity and collapses useful diversity.

**Forces.**

- Different planners dominate different structures.
- Search cost can be high.
- Comparisons need common world semantics.

**Therefore:** **Maintain a league of planners with explicit domain contracts. Evaluate compatible planners against the same admitted world and objective, and let evidence update selection policy.**

**Consequences.** Planner diversity becomes an asset rather than integration debt.

**Falsifier.** One planner receives exclusive authority merely because it is the default implementation.

**Evidence.**

- [ ] planner registry
- [ ] domain contracts
- [ ] common objective
- [ ] comparative receipts
- [ ] selection policy

**Connects to.** Multiple Formulations, Policy Is Not Agent, Selection Is Not Authorization.

---

## 18. Policy Is Not Agent ★★★

**Context.** A runtime assigns behavior to roles in a world.

**Problem.** The words policy, planner, role, and agent are often collapsed, making it impossible to vary one dimension independently.

**Forces.**

- One process may host many roles.
- A planner can parameterize many policies.
- LLMs may compile decisions without owning rollout.

**Therefore:** **Represent policy as planner × parameters × objective × observation projection × action projection, and represent roles separately from the runtime process that hosts them.**

**Consequences.** Self-play and cross-planner experiments become compositional.

**Falsifier.** Changing the observation projection requires creating a new 'agent type' even though planner and role are unchanged.

**Evidence.**

- [ ] policy tuple
- [ ] role definition
- [ ] planner identity
- [ ] projection identities

**Connects to.** Planner League, Planning Projection, Multiple Formulations.

---

## 19. Planning Projection ★★☆

**Context.** A rich canonical graph must be solved by a planner with a narrower input language.

**Problem.** Hand-maintained planning models drift from the canonical semantics and silently change the problem.

**Forces.**

- Planners need specialized representations.
- Canonical ontologies favor interoperability.
- Projection can lose information.

**Therefore:** **Generate planner-specific models as deterministic projections from the admitted canonical graph, and record the projection identity in the plan evidence.**

**Consequences.** Many planner languages can coexist without becoming competing sources of truth.

**Falsifier.** A planning model contains semantics that cannot be traced back to the admitted canonical graph or declared projection rules.

**Evidence.**

- [ ] source graph digest
- [ ] projection version
- [ ] generated planner model
- [ ] round-trip/coverage checks

**Connects to.** Ontology First, Multiple Formulations, Deterministic Projection.

---

## 20. Multiple Formulations ★★☆

**Context.** One operational problem can be modeled as planning, scheduling, constraint satisfaction, optimization, search, or workflow.

**Problem.** Selecting a formulation by habit can make a tractable problem look impossible or overfit the system to one solver ecosystem.

**Forces.**

- Formulation changes performance dramatically.
- Equivalent formulations may not preserve every semantic detail.
- Maintaining alternatives by hand is expensive.

**Therefore:** **Preserve several formally related projections of the same admitted problem where equivalence or refinement can be stated. Let evidence select among them by context.**

**Consequences.** The ecosystem can discover that a 'new' planning problem is structurally equivalent to an older solved class.

**Falsifier.** Alternative formulations introduce undeclared semantics or cannot map outcomes back to the same world-level objective.

**Evidence.**

- [ ] shared canonical problem
- [ ] projection mappings
- [ ] equivalence/refinement claims
- [ ] comparative evidence

**Connects to.** Planning Projection, Planner League, Combinatorial Maximalism.

---

## 21. Partial Order Before Total Order ★★★

**Context.** A workflow contains dependencies but many steps are independent.

**Problem.** Prematurely imposing a single sequence destroys concurrency and creates unnecessary waiting.

**Forces.**

- Total orders are easy to visualize.
- Real authority may serialize only a few transitions.
- Parallelism complicates replay.

**Therefore:** **Represent only required precedence constraints. Preserve a partial order until execution resources or authority force a totalization, and record the chosen linearization.**

**Consequences.** Little's Law improves because independent work can proceed concurrently without semantic compromise.

**Falsifier.** A workflow serializes independent tasks without an authority, data, or resource dependency that requires ordering.

**Evidence.**

- [ ] dependency DAG
- [ ] independence proof or lack of edge
- [ ] chosen schedule
- [ ] execution timestamps

**Connects to.** Constraint Fence, Combinatorial Maximalism, Receipt DAG.

---

## 22. Constraint Fence ★★★

**Context.** Search or planning occurs inside a large possibility space.

**Problem.** Unbounded combinatorics can consume arbitrary resources or generate candidates that are illegal by construction.

**Forces.**

- Broad exploration improves novelty.
- Hard constraints prune aggressively.
- Some constraints are policy, others are physics.

**Therefore:** **Encode non-negotiable ontology, authority, safety, cost, and evidence constraints as fences before optimization. Optimize freely inside the admitted region.**

**Consequences.** Search becomes both more efficient and more defensible.

**Falsifier.** The planner spends resources exploring candidates that violate known hard constraints or treats policy constraints as soft preferences.

**Evidence.**

- [ ] constraint classes
- [ ] admission tests
- [ ] resource bounds
- [ ] refusal evidence

**Connects to.** Falsifier First, Admission Before Action, Combinatorial Maximalism.

---

## 23. Falsifier First ★★★

**Context.** A plan, capability, or architectural claim is being proposed.

**Problem.** Teams naturally collect confirming examples and postpone the test that could defeat the claim.

**Forces.**

- Positive demos are persuasive.
- Boundary failures often contain more information.
- Some falsifiers are expensive.

**Therefore:** **Before implementation, state the cheapest decisive observation that would invalidate the claim or force its scope to narrow. Build that into the gym scenario.**

**Consequences.** Development optimizes for information gain instead of demonstration theater.

**Falsifier.** A claim advances to ALIVE without a predeclared failure condition or independent acceptance boundary.

**Evidence.**

- [ ] claim
- [ ] scope
- [ ] falsifier
- [ ] test scenario
- [ ] observed result

**Connects to.** Independent Postcondition, Standing Ladder, Failure Becomes Law.

---

## 24. Selection Is Not Authorization ★★★

**Context.** A planner, optimizer, model, or human chooses a candidate action.

**Problem.** Selection is frequently treated as permission to execute, allowing decision logic to inherit consequence authority.

**Forces.**

- Low-latency systems want direct tool calls.
- Selections may be probabilistic.
- Authority belongs to governance, not optimization.

**Therefore:** **Make selection produce a powerless intent. Pass that intent to a separate admission/authority boundary before any DO transition.**

**Consequences.** Planners can be replaced, ensembled, or made more aggressive without changing the safety model.

**Falsifier.** A selected action can directly cross the consequence boundary without a separate authority decision.

**Evidence.**

- [ ] selection record
- [ ] intent object
- [ ] separate admission decision
- [ ] execution receipt linking both

**Connects to.** Tool Call Is Intent, Authority Boundary, Planner League.

---
