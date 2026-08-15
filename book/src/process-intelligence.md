# Process Intelligence and the Evidence Spine

Process intelligence closes the loop between what the enterprise intended to happen and what actually happened. In DFCM, process data is not a reporting exhaust stream. It is a projection of the same identities, receipts, consequences, and standing transitions used by execution.

## Object-centric event model

A consequential workflow rarely involves one case ID. A deployment can involve repository, commit, environment, policy, authority, artifact, region, verifier, and release. A payment can involve invoice, supplier, purchase order, account, approval, transaction, and reconciliation.

The event spine therefore uses object-centric semantics. Events reference one or more stable objects and typed relationships instead of flattening the world into one process instance.

A minimum event envelope contains:

```text
event identity
event type
time / sequence
subject identities
world identity
actor / executor
related intents and authorities
related receipt
observed attributes
inferred attributes with derivation provenance
```

The receipt remains the causal evidence object. The event log is a process-intelligence projection over those receipts and observations.

## No shadow truth store

A common architecture writes operational state into one system, process-mining state into another, and management status into a third. Over time the stores disagree.

DFCM prefers a single causal correspondence:

```text
admitted subject
   ↓
execution events
   ↓
receipts
   ↓
object-centric projection
   ↓
process analysis
```

Process intelligence can maintain indexes and analytical projections, but it should be able to trace a metric back to concrete execution evidence. The analytical projection does not acquire authority to rewrite standing.

## Conformance

The canonical graph can express required process constraints without imposing an unnecessary total order. Conformance evaluates observed event relationships against those constraints.

Examples:

- authority must precede consequence;
- verifier observation must follow the relevant consequence;
- release crown must reference non-superseded receipts;
- a typed refusal must have no downstream DO edge;
- a policy exception must be effective at the time of execution;
- a reset must precede an independent scenario when isolation is required.

Conformance violations are evidence, not automatically root cause. They generate hypotheses for diagnosis.

## Little’s Law and flow

For stable systems:

\[
L = \lambda W
\]

where \(L\) is work in process, \(\lambda\) throughput, and \(W\) flow time. Enterprise automation often increases local processing speed while allowing WIP to explode because admission, review, verification, or release remains serialized.

The event spine makes WIP visible at each causal boundary:

- candidates awaiting admission,
- intents awaiting authority,
- artifacts awaiting consequence capacity,
- executions awaiting independent verification,
- receipts awaiting crown composition,
- failures awaiting durable law.

This reveals whether the bottleneck is computation, authority, verification, or human attention.

## Variant discovery

Variant discovery should preserve topology rather than rank one “happy path.” Useful questions include:

- which compatible provider/planner pairs close fastest?
- which refusal types dominate a capability?
- where do partial consequences occur?
- which families of subjects fail replay?
- which policy exceptions recur and should become explicit law?
- which human approvals add evidence and which merely add waiting?

Variants are compared against common objectives and scopes. A faster path is not superior if it weakens evidence or authority boundaries.

## Prediction is inference

Predictive process intelligence may estimate likely breach, failure, delay, or resource exhaustion. Those predictions are inferred facts and remain distinct from observed process state.

A prediction can create a candidate intervention. It cannot silently become a consequence. The intervention passes through the same admission and authority path as any other intent.

This preserves a clean loop:

```text
observation
  ↓
analysis / prediction
  ↓
hypothesis
  ↓
candidate intervention
  ↓
admission + authority
  ↓
bounded experiment or DO
  ↓
new evidence
```

## Autonomic process improvement

Process intelligence becomes autonomic when it selects new experiments from uncertainty and failure evidence while preserving a stable regression core.

Candidate curriculum sources include UNKNOWN compatibility edges, recent failure classes, high-cost variants, repeated policy exceptions, queue growth, replay failures, and capability gaps. Selection rationale is recorded, bounded by resource budgets, and remains powerless until admitted.

A successful experiment should change a durable artifact: selector policy, ontology, constraint, pack, verifier, capability edge, or operating playbook. Otherwise the loop produced insight without institutional learning.

## Executive measures

Useful enterprise process measures include:

- verified consequences per unit time,
- verified consequence per dollar or compute unit,
- WIP by causal boundary,
- admission/refusal latency,
- authority wait time,
- verification latency,
- replay success rate,
- percentage of failures converted into durable guards,
- evidence age,
- variance by provider/world/formulation,
- manual attention per closed capability,
- percentage of process metrics traceable to exact receipts.

## Privacy and minimization

Process data can expose sensitive operational behavior. The event projection should carry only attributes needed for declared analytical purposes. Raw evidence can remain behind stricter access boundaries while the analytical layer retains stable object references.

Derived process features should record provenance so a later audit can distinguish direct observation from a classifier or heuristic.

## Process-intelligence crown

Process intelligence has standing when a management claim can be traced from aggregate metric to object-centric events to exact receipts to the underlying subject and consequence. The design is falsified when a dashboard reports process success or breach that cannot be reconstructed from execution evidence, or when an analytical prediction directly actuates without entering the normal authority path.
