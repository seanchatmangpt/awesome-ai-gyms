# Execution and Safety

How a system crosses the consequence boundary without ambient execution authority.

## 33. BRCE Is the Only DO ★★★

**Context.** A system contains models, planners, hooks, generators, tools, runtimes, and plugins that can propose actions.

**Problem.** Multiple actuation paths make it impossible to prove that every consequence was admitted, authorized, and receipted.

**Forces.**

- Direct tool execution is convenient.
- Hooks want to automate reactions.
- Distributed providers hide their side-effect boundaries.

**Therefore:** **Route every state-changing transition through the Brokered Receipted Consequence Executor (BRCE) or equivalent single consequence broker. All other components may manufacture intents but cannot actuate.**

**Consequences.** Execution authority becomes small enough to audit and harden.

**Falsifier.** Any component can mutate world or external state without entering the broker.

**Evidence.**

- [ ] enumerated DO operations
- [ ] call graph showing exclusive broker path
- [ ] authority checks
- [ ] receipts

**Connects to.** Zero Unreceipted Actuation, Tool Call Is Intent, Consequence Boundary.

---

## 34. Zero Unreceipted Actuation ★★★

**Context.** The consequence broker is about to perform an admitted state change.

**Problem.** Allowing 'fire and forget' transitions creates gaps where consequential actions exist without durable evidence.

**Forces.**

- Receipts add latency and storage.
- External systems can fail after accepting a request.
- Some consequences are only eventually observable.

**Therefore:** **Make receipt production part of the actuation contract. A DO transition is incomplete until its execution and observed consequence are bound into a receipt or an explicit partial/failure receipt.**

**Consequences.** Every attempted consequence leaves an auditable causal artifact.

**Falsifier.** A state change can be observed in the world but no corresponding execution or failure receipt exists.

**Evidence.**

- [ ] pre-actuation intent receipt
- [ ] executor result
- [ ] postcondition evidence
- [ ] final or partial receipt

**Connects to.** Receipt, BRCE Is the Only DO, Receipt DAG.

---

## 35. Tool Call Is Intent ★★★

**Context.** A model or planner emits a structured tool invocation.

**Problem.** Tool-call syntax is often wired directly to execution, giving generated text ambient machine authority.

**Forces.**

- Tool ecosystems are designed for convenience.
- Models hallucinate arguments.
- Policy enforcement needs stable objects.

**Therefore:** **Treat every model-facing tool call as an intent object. Normalize, validate, admit, authorize, and only then route it to DO. The tool schema defines a proposal surface, not an execution capability.**

**Consequences.** Model innovation and tool richness can increase without expanding the trusted computing base.

**Falsifier.** Emitting a syntactically valid tool call is sufficient to cause the side effect.

**Evidence.**

- [ ] raw call
- [ ] normalized intent
- [ ] admission decision
- [ ] authority decision
- [ ] execution receipt

**Connects to.** Selection Is Not Authorization, Admission Before Action, BRCE Is the Only DO.

---

## 36. Sandbox Boundary ★★★

**Context.** A gym needs shell, filesystem, browser, network, process, or device capabilities.

**Problem.** A nominally bounded task can escape through shared host state and invalidate both safety and reproducibility.

**Forces.**

- Strong isolation can be expensive.
- Network access is often necessary.
- Filesystem and subprocess capabilities share hidden state.

**Therefore:** **Declare one execution world for coupled capabilities and confine them with the strongest practical isolation boundary. Expose network, mounts, credentials, devices, and host bridges explicitly as admitted capabilities.**

**Consequences.** Tool behavior becomes attributable to a concrete environment.

**Falsifier.** A scenario depends on undeclared host files, credentials, processes, or network routes.

**Evidence.**

- [ ] sandbox identity
- [ ] mount/network/device policy
- [ ] resource limits
- [ ] escape tests

**Connects to.** Bounded World, Idempotent Reset, Exact Runtime Pin.

---

## 37. Idempotent Reset ★★★

**Context.** Many scenarios must run against the same world type.

**Problem.** Residual state from prior episodes creates order-dependent results and false capability claims.

**Forces.**

- Full reconstruction may be slow.
- Caches improve performance.
- Some external systems cannot be perfectly reset.

**Therefore:** **Define reset as a verified transition to a named baseline. Prefer reconstructable ephemeral worlds; where reset is approximate, specify and test the equivalence class.**

**Consequences.** Scenario order stops affecting standing and parallel execution becomes safer.

**Falsifier.** Running scenario B after scenario A changes B's result compared with running B from a fresh baseline without a declared dependency.

**Evidence.**

- [ ] baseline identity
- [ ] reset procedure
- [ ] post-reset verifier
- [ ] leakage test

**Connects to.** Bounded World, Replay, Reversible Composition.

---

## 38. Typed Refusal ★★★

**Context.** Admission, authority, materialization, or execution can legitimately decline a transition.

**Problem.** Generic exceptions blur policy refusal, unsupported capability, missing evidence, infrastructure failure, and software defects.

**Forces.**

- Callers want simple success/failure APIs.
- Operators need actionable diagnosis.
- Refusal must not be confused with capability absence.

**Therefore:** **Use typed outcomes such as REFUSED, BLOCKED, UNSUPPORTED, BUILD_BROKEN, UNKNOWN, and PARTIAL_ALIVE with domain-specific reason codes. Preserve the failed transition and evidence.**

**Consequences.** Automation can choose the correct recovery path without pretending every failure is the same.

**Falsifier.** A policy denial and a missing compiler produce the same undifferentiated error state.

**Evidence.**

- [ ] typed status
- [ ] reason code
- [ ] failed transition
- [ ] supporting evidence
- [ ] retry/repair semantics

**Connects to.** Failure Is Topology, Standing Ladder, Admission Before Action.

---

## 39. Failure Is Topology ★★★

**Context.** One attempted path through a composition or compatibility graph fails.

**Problem.** Global failure labels erase other reversible paths and turn local defects into ecosystem-wide conclusions.

**Forces.**

- Humans generalize from vivid failures.
- Retry storms waste resources.
- Some failures really are shared root causes.

**Therefore:** **Attach failure to the exact edge, subject, world, and hypothesis that failed. Remove or penalize that path while preserving unrelated nodes and edges until separately falsified.**

**Consequences.** The system learns structure instead of merely accumulating red states.

**Falsifier.** One failed provider/planner/world combination causes unrelated combinations to be marked failed without execution.

**Evidence.**

- [ ] failed edge identity
- [ ] failure class
- [ ] scope
- [ ] alternative edges preserved
- [ ] repair hypothesis

**Connects to.** Compatibility Edge, Typed Refusal, Failure Becomes Law.

---

## 40. Independent Postcondition ★★★

**Context.** An executor reports that a requested action succeeded.

**Problem.** The component that performed the action is not independent evidence that the intended consequence actually holds.

**Forces.**

- External APIs can acknowledge before convergence.
- Executors may contain correlated bugs.
- Verification may be expensive.

**Therefore:** **After DO, run a verifier that observes the world independently of the executor's success return and evaluates the declared postcondition.**

**Consequences.** Standing is based on consequence, not optimism from the execution path.

**Falsifier.** The only evidence for success is the executor's own return value or log message.

**Evidence.**

- [ ] declared postcondition
- [ ] independent observation path
- [ ] verifier identity
- [ ] verifier result in receipt

**Connects to.** Falsifier First, Receipt, Exact Subject Binding.

---
