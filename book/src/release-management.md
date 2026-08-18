# Release Management and the Crown

A release is an exact subject plus a dependency closure and an evidence claim. It is not a branch name, a green dashboard, or a collection of successful jobs. DFCM makes release readiness a proof-composition problem through the [Release Crown](patterns/enterprise-operations/55-release-crown.md).

## Release subject

Resolve the release to immutable identities:

- source commit/tree,
- generated artifact digests,
- pack and dependency versions,
- compiler/toolchain identity,
- deployment manifests,
- model/data/policy versions where material,
- target environment identity.

A tag can name the release, but standing binds to the resolved subjects behind it.

## Crown graph

The crown is a DAG of required claims. A typical enterprise crown includes nodes for:

1. semantic/ontology validation,
2. deterministic generation drift check,
3. build and unit verification,
4. integration and project-gym behavior,
5. negative admission/refusal behavior,
6. authority-boundary verification,
7. production-like consequence proof,
8. independent postconditions,
9. supply-chain qualification,
10. security boundary tests,
11. replay/equivalence proof,
12. maturity floor,
13. required operational playbooks,
14. incident/recovery proof where required,
15. final publication/deployment observation.

Different capability classes can have different crown templates. The template itself is versioned policy.

## Evidence admission

A crown node accepts evidence only when subject, validator, toolchain, configuration, environment, and policy identities satisfy the node’s reuse rules.

Prior evidence can be reused when an explicit equivalence relation proves the relevant identities unchanged or equivalent. “The diff is small” is not an equivalence proof by itself.

Missing evidence leaves the node open. A dashboard cannot override the absence by changing the color.

## Promotion sequence

A normal release progresses through:

```text
candidate subject
   ↓
resolved dependency closure
   ↓
source/static validation
   ↓
construction/build proof
   ↓
behavioral/integration proof
   ↓
consequence + verifier proof
   ↓
replay / recovery proof
   ↓
release crown receipt
   ↓
production publication
   ↓
production postcondition
   ↓
ALIVE release standing
```

The production publication itself is DO and receives its own authority and receipt.

## Blockers

Release blockers are typed:

- **UNKNOWN:** required evidence has not been observed;
- **BLOCKED:** dependency, environment, or authority unavailable;
- **BUILD_BROKEN:** exact release cannot be constructed;
- **UNSUPPORTED:** required capability is not provided for this release scope;
- **REFUSED:** policy correctly denies promotion;
- **PARTIAL_ALIVE:** lower-level evidence exists but crown is incomplete.

This makes release triage actionable. A security refusal and a compiler failure should not appear as the same red gate.

## Continuous release

Continuous delivery is compatible with a strong crown when crown manufacture is deterministic and impact-selective. Unchanged evidence can be reused under exact identity rules; affected nodes rerun.

The objective is not to rerun every expensive test blindly. It is to recompute the smallest sufficient proof closure for the exact release.

A dependency or policy movement can invalidate evidence even when application source is unchanged.

## Rollback

Rollback is a new release decision and a new consequence. Resolve the rollback target exactly, verify that data/external state is compatible, issue rollback authority, perform the transition through BRCE, and independently verify the recovered postcondition.

A prior ALIVE receipt proves the old subject once worked in its historical environment. It does not automatically prove rollback safety against today’s state.

## Release notes

Release notes should be a projection of causal changes, not the source of truth. Useful generated content includes changed capabilities, changed authorities, changed policies, new or retired supplier edges, standing changes, new failure guards, replay-impacting changes, and open UNKNOWNs accepted by scope.

Human narrative can be layered on top of these facts.

## Emergency release

Emergency release uses a scoped break-glass capability and an emergency crown. The emergency crown may legitimately omit lower-risk checks that cannot fit the incident window, but the omission is explicit, typed, and time-bounded. Enhanced production verification and post-event replay can become mandatory compensating controls.

Emergency does not mean unreceipted.

## Production proof

A deployment workflow that succeeds proves the workflow executed. Production ALIVE standing requires the declared production postcondition.

Examples:

- public documentation URL serves the exact new edition;
- service endpoint returns the expected build identity and passes health/business verifier;
- infrastructure state matches the desired exact revision;
- policy engine reports the new policy identity and negative tests refuse prohibited action.

Inspection of CI metadata is not execution of the production subject.

## Invalidation and supersession

A release crown can be invalidated or narrowed after publication because of compromised dependency, policy change, verifier defect, security incident, or replay failure. Preserve the historical crown receipt and add a supersession/invalidation relation.

Standing reflects current defensibility while evidence preserves history.

## Release dossier

The final crown should reference a dossier containing release identity, dependency closure, crown template version, all required receipts, policy/authority versions, known exceptions, replay manifest, operational/incident playbooks, production postcondition, and supersession links.

This dossier is the interface for audit and rollback analysis.

## Release crown rule

\[
ALIVE_{release} \iff
ExactSubject
\land
\bigwedge_{n \in Crown} valid(n)
\land
ProductionConsequence
\land
ProductionPostcondition
\]

The release process is falsified when a required crown node can be stale, absent, wrong-subject, or failed while the system still reports complete release standing.
