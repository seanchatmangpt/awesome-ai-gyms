# Adoption and Migration

Enterprise adoption should preserve obligations while replacing mechanisms. DFCM therefore migrates one bounded capability at a time and keeps the old path until the new path proves the same or stronger causal contract.

The objective is not a long coexistence period. It is a controlled way to establish equivalence before an irreversible cutover.

## Maturity path

A useful adoption sequence is:

### M0 — Observed

The current process is known only through people, documents, tickets, code, and runtime traces. No canonical capability contract exists.

### M1 — Modeled

Exact subjects, world boundary, observations, consequences, policies, and actors are represented explicitly. Existing controls are fenced until their obligation is understood.

### M2 — Admitted

Candidate intents and data inputs pass formal admission. Typed refusal exists. No new autonomous consequence authority is required yet.

### M3 — Constructed

Deterministic projections manufacture artifacts, plans, configuration, verifiers, or runbooks from admitted semantics. Construction remains separate from DO.

### M4 — Receipted execution

The capability executes through a bounded consequence broker with explicit authority, independent verification, and receipts.

### M5 — Replayable operation

Exact subject/runtime identities, replay manifests, equivalence predicates, incident handling, and release crowns are operational.

### M6 — Autonomic improvement

Process intelligence can select bounded experiments from uncertainty/failure evidence; successful experiments update durable law and are reverified before changing standing.

The overall maturity label remains the minimum of the required control planes, not an average.

## Migration from agent-first automation

An agent-first system often looks like:

```text
prompt → model → tool call → side effect
```

Do not rewrite the entire product first. Insert boundaries in order:

1. inventory effectful tools;
2. classify every tool call as intent;
3. normalize intent outside the model;
4. add admission and typed refusal;
5. externalize authority;
6. route effectful calls through BRCE;
7. add independent postconditions;
8. emit receipts;
9. bind standing to exact execution evidence;
10. only then broaden planner/model freedom.

This preserves product behavior while shrinking ambient authority.

## Migration from workflow/RPA

Workflow systems usually have better explicit sequencing but can hide authority in service accounts and success in task completion states.

Refactor by extracting:

- canonical business objects,
- partial-order dependencies,
- effectful transitions,
- credential/authority scopes,
- independent business postconditions,
- event-object relationships,
- replay obligations.

Then remove unnecessary total ordering. Deterministic steps remain deterministic; planners are introduced only where actual search or ambiguity exists.

## Migration from manual work

Do not encode every inherited human action. First identify the outcome obligation and the fences around it.

For each human step ask:

1. What state does the person observe?
2. What transformation do they perform?
3. What decision right do they exercise?
4. What consequence can they cause?
5. What evidence proves success?
6. Which part exists only because surrounding systems are weak?

Preserve obligations, authority, relationships, and necessary judgment. Eliminate accidental handoffs and manual translation when deterministic manufacture can replace them.

## Parallel run

Parallel run is useful only when it has a declared comparison predicate. Compare exact same subject/world inputs where possible and state how differences will be evaluated.

A human process is not automatically ground truth. It is an incumbent implementation whose outputs and consequences can themselves be measured against the business postcondition.

## Cutover

Cutover is a release-crown decision. Required evidence typically includes:

- exact new subject identity,
- current policy and authority mappings,
- successful behavioral scenarios,
- negative/refusal tests,
- production-like consequence proof,
- independent verifier evidence,
- replay proof,
- rollback/recovery capability,
- operator and incident playbooks,
- current supplier qualification.

When the crown closes, the old mechanism can be retired if no remaining obligation depends on it.

## Rollback and reversibility

Before cutover, classify which effects are reversible, compensatable, reconstructable, or irreversible. A rollback plan that simply redeploys old code may be insufficient if data or external state has changed.

Rollback itself is DO and needs authority, verification, and receipts.

## Change saturation

Do not migrate more capabilities than the enterprise can verify. If security review, authority modeling, production verification, or incident response is the bottleneck, launching more pilots increases WIP rather than throughput.

Use the process-intelligence spine to expose the queue and invest at the constraint.

## Adoption anti-patterns

- **Pilot accumulation:** many demos, few release crowns.
- **Prompt governance:** policy exists only inside instructions to models.
- **Shadow authority:** inherited service accounts give new components broader rights than intended.
- **Human-loop theater:** approval steps exist without a unique decision or evidence contract.
- **Green by construction:** successful build or workflow execution is treated as business standing.
- **Big-bang replacement:** incumbent obligations are removed before equivalence is proven.
- **Vendor-first ontology:** enterprise semantics are defined in one supplier’s schema.
- **Exception permanence:** temporary bypasses become normal operation.

## Adoption crown

Migration closes when the replacement capability has exact-subject ALIVE evidence for its declared scope, the release crown is satisfied, rollback/recovery is bounded, and the incumbent mechanism can be removed without deleting an unresolved obligation.

The falsifier is a cutover that relies on narrative confidence, unbounded authority, or a demo path that never exercised the real consequence and verifier boundary.
