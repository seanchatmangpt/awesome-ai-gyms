# Governance and Policy

Governance is most effective when it constrains the possibility graph before expensive work begins and produces machine-visible evidence when it permits or refuses a transition. DFCM therefore treats governance as executable structure, not a review meeting added after implementation.

## Governance graph

The governance graph links subjects, owners, authorities, obligations, prohibitions, jurisdictions, data classifications, retention rules, policy versions, exceptions, evidence requirements, and release criteria. A policy should be able to name the subjects and actions it governs. A subject should be able to enumerate the policies that currently apply to it.

This graph is not itself execution authority. It is the canonical source from which admission and authority projections can be manufactured.

## Policy lifecycle

Every policy has a lifecycle:

```text
proposed
  ↓
reviewed
  ↓
admitted
  ↓
effective
  ↓
superseded | revoked
```

Historical receipts retain the effective policy identity that governed execution at the time. Rewriting the current policy does not rewrite history.

## Policy as constraint, not prompt

A policy that matters at the consequence boundary should not exist only as natural-language instructions to a model. Natural language can be the human authoring surface. The enforceable portion must project into one or more of schema constraints, admission rules, authority scopes, resource budgets, required postconditions, required receipts, release-crown dependencies, and typed refusal reasons.

Some obligations cannot be fully automated. Those remain explicit human-authority requirements rather than invisible prose assumptions.

## Policy classes

### Semantic integrity

Defines canonical identity, required fields, valid relationships, versioning, and source provenance.

### Authority

Defines which actors or brokers may perform which actions over which subjects.

### Data use

Defines permitted data classes, purposes, transfer boundaries, retention, and access conditions.

### Resource

Defines compute, cost, time, token, rate, concurrency, storage, or human-attention budgets.

### Release

Defines evidence required to promote a capability or release.

### Safety and consequence

Defines prohibited effect classes, mandatory sandboxes, approvals, reversible staging, and emergency rules.

### Evidence

Defines retention, integrity, replay, audit, and supersession obligations.

## Policy precedence

At enterprise scale, multiple policies will apply to the same candidate action. Precedence must be deterministic enough to audit. A practical baseline is:

1. physical and legal impossibility cannot be overridden by local preference;
2. explicit prohibition outranks optional optimization;
3. narrower valid authority does not inherit broader privilege from a caller;
4. stronger evidence obligations accumulate unless a policy explicitly supersedes them;
5. exceptions require their own authority and expiry.

The concrete precedence graph belongs to the organization and should be versioned.

## Exception management

An exception is not the deletion of a rule. It is a scoped policy object containing an exception ID, the policy being excepted, exact subjects/actions, issuer, business reason, validity interval, compensating controls, required evidence, and revocation condition. The receipt binds the exception used. This prevents a temporary decision from becoming permanent ambient practice.

## Governance before optimization

Hard constraints should prune candidates before the planner optimizes. Examples include a provider that cannot satisfy data-location constraints, an action that exceeds delegated spend authority, a model version that lacks required provenance, a deployment target outside the admitted environment class, or an evidence-retention obligation that cannot be met.

For candidate graph \(G\) and constraint set \(B\):

\[
G_{admitted} = \{g \in G \mid g \models B\}
\]

The rejected region remains typed evidence where useful. Policy can change; a candidate refused today may become admissible under a later policy without being rediscovered from scratch.

## Ownership and accountability

Every policy should have a semantic owner, authority issuer where applicable, effective version, machine-readable enforcement mapping, human-readable rationale, falsifier, and review/supersession mechanism. “Security requires it” is not sufficient provenance for a permanent fence.

## Policy verification

Policy implementation is tested through positive tests, negative tests, boundary tests, drift tests, and replay tests. Known admissible intents must pass with expected authority. Known prohibited intents must prove typed refusal before mutation. Boundary values must resolve correctly. Generated enforcement must remain equivalent to policy source. Historical receipts must reconstruct the effective policy context.

## Governance metrics

Useful measures include the proportion of consequence paths with explicit authority objects, policy-to-enforcement projection coverage, number and age of active exceptions, refused actions by typed reason, unresolved policy conflicts, stale policy versions in deployed runtimes, release-crown blocks attributable to governance, and replay success for historical policy decisions.

The objective is not fewer refusals. A refusal may be correct. The objective is predictable, bounded, explainable governance.

## Falsifier

The governance design is falsified if a release-critical obligation exists only in undocumented human knowledge, a hidden pipeline branch, or a prompt instruction that the consequence broker does not independently enforce. Governance has standing when policy identity, enforcement, authority, consequence, and evidence remain connected end to end.
