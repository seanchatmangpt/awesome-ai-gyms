# Foundations

The smallest invariants that make a gym a bounded, evidentiary system rather than a demo.

## 1. Bounded World ★★★

**Context.** An actor, policy, planner, or agent must interact with an environment.

**Problem.** Without an explicit world boundary, observations, actions, resets, and consequences leak into ambient machine state and claims become unscoped.

**Forces.**

- Real systems expose more state than an experiment needs.
- Isolation adds cost, but unbounded consequence destroys reproducibility.
- A useful world must be rich enough to falsify the policy being tested.

**Therefore:** **Define a world as an explicit state space, observation projection, admitted transition relation, reset semantics, resource boundary, and consequence boundary. Anything outside that definition is external and cannot silently participate.**

**Consequences.** Experiments gain a named causal boundary and deterministic reset target. Some realism is intentionally excluded and must be reintroduced through explicit world extensions.

**Falsifier.** A scenario can read or mutate state that is neither declared as world state nor recorded as an external dependency.

**Evidence.**

- [ ] world identity and version
- [ ] state/observation/action contract
- [ ] reset proof
- [ ] declared external dependencies

**Connects to.** Canonical Subject, Consequence Boundary, Idempotent Reset, World Adapter.

---

## 2. Canonical Subject ★★★

**Context.** A registry, planner, runner, and verifier refer to the thing being tested.

**Problem.** Names such as 'main', 'latest', package aliases, or mutable URLs allow different components to believe they are operating on the same subject when they are not.

**Forces.**

- Human-friendly names are mutable.
- Execution requires concrete bytes or identities.
- Evidence must remain meaningful after upstream changes.

**Therefore:** **Resolve every admitted subject to a stable identity before execution: repository plus exact commit/tree, package plus digest, image plus digest, model plus revision, dataset plus version, or equivalent immutable identifier.**

**Consequences.** Receipts can bind to a durable subject. Resolution becomes an explicit transition rather than an invisible convenience.

**Falsifier.** Two purported replays resolve the same friendly name to different underlying subjects.

**Evidence.**

- [ ] friendly identifier
- [ ] resolved immutable identifier
- [ ] resolver provenance
- [ ] identity included in receipt

**Connects to.** Provenance Lock, Exact Subject Binding, Exact Runtime Pin.

---

## 3. Explicit Observation ★★★

**Context.** A world exposes state to a planner, policy, model, or verifier.

**Problem.** If observations are implicit, different actors may reason from different hidden projections and a successful run cannot be reconstructed.

**Forces.**

- Full state may be too large or unsafe to expose.
- Partial observability is often intentional.
- Derived observations can smuggle inference into fact.

**Therefore:** **Define observation objects and projections explicitly. Record what was observed, when, by whom, under which world state, and which derivations were applied.**

**Consequences.** Partial observability becomes a modeled property rather than missing instrumentation. Observed and inferred facts can be separated.

**Falsifier.** A later verifier cannot determine which state was actually visible to the acting policy.

**Evidence.**

- [ ] observation schema
- [ ] projection identity
- [ ] timestamp/sequence
- [ ] observed-versus-derived marker

**Connects to.** Bounded World, Observation vs Inference, OCEL Event Spine.

---

## 4. Admission Before Action ★★★

**Context.** A candidate intent could cause a world transition.

**Problem.** Validation performed after actuation cannot protect the world from an invalid or unauthorized transition.

**Forces.**

- Some checks are expensive.
- Planners benefit from exploring invalid candidates cheaply.
- Authority must not be inferred from semantic validity.

**Therefore:** **Place a formal admission boundary before every consequential transition. Admission validates subject, schema, preconditions, exclusions, authority requirements, and resource bounds; refusal is a first-class outcome.**

**Consequences.** The execution path becomes fail-closed. Candidate generation remains broad because invalid candidates can be refused without being executed.

**Falsifier.** A state-changing path exists that bypasses admission or performs validation only after mutation.

**Evidence.**

- [ ] admission input
- [ ] admission decision
- [ ] typed refusal reason
- [ ] proof that DO is unreachable on refusal

**Connects to.** Authority Boundary, Typed Refusal, BRCE Is the Only DO.

---

## 5. Authority Boundary ★★★

**Context.** A semantically valid action may still lack permission to occur.

**Problem.** Systems often conflate 'can be represented', 'looks safe', or 'was selected' with authority to cause consequences.

**Forces.**

- Authority may differ by subject, user, world, action, and time.
- Central policy is simpler but can overgrant.
- Models and planners are untrusted producers of intent.

**Therefore:** **Represent authority as an explicit capability scoped to actor, action, subject, world, and validity interval. Check it at the consequence boundary; never grant ambient execution authority to planners, hooks, prompts, or generated artifacts.**

**Consequences.** Authorization becomes auditable and revocable. The design can safely host aggressive exploration upstream.

**Falsifier.** A planner or tool schema can directly cause a consequence merely because it emitted a syntactically valid call.

**Evidence.**

- [ ] authority object
- [ ] scope
- [ ] issuer
- [ ] expiry/revocation semantics
- [ ] authority check in execution receipt

**Connects to.** Admission Before Action, Tool Call Is Intent, Zero Unreceipted Actuation.

---

## 6. Consequence Boundary ★★★

**Context.** A system transitions from reversible reasoning to machine-state change.

**Problem.** Irreversible or externally visible effects are qualitatively different from graph exploration, simulation, planning, or construction.

**Forces.**

- Users want low latency.
- Distributed systems hide side effects behind APIs.
- Some operations appear read-only but allocate, cache, bill, or publish.

**Therefore:** **Name and minimize the consequence boundary. Everything before it is SELECT or CONSTRUCT; crossing it is DO and must pass through the designated broker with explicit authority and receipt obligations.**

**Consequences.** The system can optimize aggressively before DO while keeping actual consequence conservative and inspectable.

**Falsifier.** A component outside the named DO path can produce externally visible or persistent state changes.

**Evidence.**

- [ ] enumerated consequence classes
- [ ] single execution path
- [ ] side-effect inventory
- [ ] receipt for every admitted transition

**Connects to.** BRCE Is the Only DO, Tool Call Is Intent, Zero Unreceipted Actuation.

---

## 7. Receipt ★★★

**Context.** An admitted transition has been attempted or completed.

**Problem.** Logs prove that text was emitted, not that the exact subject executed under the claimed authority and produced the claimed consequence.

**Forces.**

- Evidence must be compact enough to retain.
- Distributed execution produces multiple identities.
- A verifier can fail independently of execution.

**Therefore:** **Emit a deterministic receipt that binds subject identity, admitted intent, authority decision, executor identity, observed consequence, verifier result, timing, and references to replay material.**

**Consequences.** Claims gain a machine-checkable evidentiary object. Receipts can form DAGs across multi-step workflows.

**Falsifier.** A claimed successful action cannot be tied to one exact admitted subject and one observed verifier outcome.

**Evidence.**

- [ ] receipt identifier/hash
- [ ] subject
- [ ] intent
- [ ] authority
- [ ] executor
- [ ] consequence
- [ ] verifier
- [ ] replay references

**Connects to.** Exact Subject Binding, Receipt DAG, Replay.

---

## 8. Replay ★★★

**Context.** A run has produced evidence and someone needs to audit, compare, or reproduce it.

**Problem.** Re-running the same command is not replay if the subject, environment, observations, seeds, or verifier changed.

**Forces.**

- Perfect bit-for-bit reproduction may be impossible in stochastic worlds.
- Auditors need bounded equivalence criteria.
- Replay infrastructure costs storage.

**Therefore:** **Define replay as reconstruction of the admitted subject, world, inputs, authority envelope, and verifier with an explicit equivalence relation for allowed nondeterminism.**

**Consequences.** Evidence remains useful after the original process exits. Stochastic systems can still support rigorous replay by declaring tolerances.

**Falsifier.** A 'replay' depends on mutable latest dependencies or lacks a declared equivalence test.

**Evidence.**

- [ ] replay manifest
- [ ] pinned identities
- [ ] seed/randomness record
- [ ] equivalence predicate
- [ ] replay receipt

**Connects to.** Receipt, Replay Equivalence, Delete and Regenerate.

---
