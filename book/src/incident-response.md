# Incident Response and Standing Downgrade

Incident response in a DFCM system has two simultaneous objectives: contain consequence and preserve enough causal evidence to determine what actually happened. Fast containment must not destroy the receipt, subject, policy, or world information needed to repair the system lawfully.

## Incident triggers

An incident can be triggered by security compromise, unverified consequence, replay failure, evidence-integrity defect, policy bypass, credential leakage, repeated partial consequence, cross-tenant leakage, supplier drift, material cost overrun, release-crown inconsistency, or any discovery of an effectful path outside the declared broker.

Not every BUILD_BROKEN state is an incident. Not every REFUSED action is an incident. Typed status prevents ordinary safe refusal from flooding incident management.

## 1. Preserve

Capture the exact subject and runtime identities, active policy versions, relevant authority capabilities, observation sequence, intents, executor results, verifier results, receipts, external provider references, and current world state where feasible.

Do not begin by rewriting logs or deleting evidence to “clean up” the system. Evidence preservation is itself bounded by privacy and security policy.

## 2. Contain authority

Contain the narrowest authority that can stop further harmful consequence:

- revoke or suspend compromised capabilities,
- disable affected BRCE adapter paths,
- narrow target scopes,
- freeze release promotion,
- isolate affected worlds,
- block a specific supplier/subject edge.

Avoid global shutdown when the evidence supports a smaller boundary. One failed edge is topology.

## 3. Downgrade standing

Standing must reflect evidence, not reputation. Examples:

- an affected ALIVE capability becomes PARTIAL_ALIVE if the exact consequence still works but required evidence is compromised;
- a capability becomes BLOCKED if authority is intentionally revoked pending investigation;
- a claim becomes UNKNOWN if its supporting receipt integrity cannot be trusted;
- a supplier edge becomes UNSUPPORTED if a required capability is no longer available;
- a build regression becomes BUILD_BROKEN without implying the prior release never worked.

Historical receipts remain historical facts unless their integrity is specifically falsified.

## 4. Localize the failed transition

Trace the lifecycle:

```text
parse
→ route
→ resolve
→ admit/refuse
→ select
→ construct
→ authorize
→ DO
→ observe
→ verify
→ receipt
→ replay
→ standing
```

Identify the first transition whose observed output violates its contract. Distinguish root cause from later symptoms.

If an executor succeeded but postcondition failed, the failure boundary is not “the model.” If a mutable subject changed, the failure may be identity resolution. If policy was correct but an alternate API path bypassed BRCE, the failure is consequence topology.

## 5. Form a repair hypothesis

State what should change and what observation would disprove the hypothesis. Make the smallest coherent repair that restores the violated contract.

Do not repeatedly rerun the unchanged failing path. A rerun is justified by a new hypothesis, changed dependency state, or evidence that the failure was transient under a declared retry policy.

## 6. Convert failure into law

A durable repair should add the narrowest reusable guard:

- ontology constraint,
- schema rule,
- admission/refusal condition,
- authority restriction,
- fixture,
- regression scenario,
- independent verifier,
- theorem or invariant,
- dependency pin,
- supplier qualification rule,
- operational playbook.

The objective is to shrink the invalid region of future search without deleting unrelated valid possibilities.

## 7. Reverify the boundary

Run the cheapest high-information verifier at the failed boundary first. Then expand to upstream/downstream coverage required by impact.

For a consequential defect, include production-like consequence verification or an equivalent bounded world before restoring ALIVE standing. Unit success cannot substitute for the failed integration boundary.

## 8. Recovery and promotion

Recovery actions are new DO transitions and need authority, postconditions, and receipts. After repair:

1. close affected regression scenarios;
2. refresh invalidated qualification evidence;
3. replay representative prior receipts where required;
4. recompute affected release crowns;
5. restore standing only for exact subjects with current evidence;
6. revoke temporary break-glass authority.

## Incident evidence package

An incident package should contain incident identity, affected subjects/worlds, first known bad and last known good evidence, authority changes, standing downgrades, failure receipts, causal hypothesis, repair diff/reference, added durable law, verifier results, replay results, recovery receipts, and remaining unknowns.

The package should be generated from canonical evidence where possible rather than hand-copied into a disconnected document.

## Communication

Communicate typed facts:

- **observed:** what exact consequence/evidence was seen;
- **inferred:** current causal hypothesis;
- **changed:** authority, configuration, or standing changes made;
- **verified:** tests or postconditions that now pass;
- **unknown:** unresolved scope;
- **next gate:** evidence required for promotion.

This prevents early hypotheses from becoming organizational fact.

## Repeated incidents

Repeated exceptions or incidents in the same causal class are evidence that local repair is insufficient. Escalate from patch to ontology/policy/architecture change when failures share a common constraint that the current design cannot express.

Process intelligence should surface recurrence across subjects and worlds even when individual tickets look unrelated.

## Incident metrics

Useful metrics include time to authority containment, time to first typed localization, percentage of incidents with exact-subject evidence, percentage converted into durable guards, replay success after repair, number of standing claims invalidated per incident, and recurrence by causal class.

Mean time to “close ticket” is weaker than mean time to restore defensible standing.

## Incident crown

An incident is closed when harmful authority is contained, affected standing is accurate, root cause is localized or explicitly remains UNKNOWN, the repair is independently verified, required historical/replay evidence is preserved, durable law prevents the causal class where justified, and temporary emergency authority is retired.

The response is falsified if the organization restores green status because the symptom disappeared while the violated authority/evidence boundary remains unproven.
