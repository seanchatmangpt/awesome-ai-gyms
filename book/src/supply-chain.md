# Supply Chain and Third-Party Qualification

Enterprise automation depends on code, models, datasets, runtimes, APIs, planners, packs, containers, and hosted services that the enterprise does not fully control. DFCM treats every external dependency as a candidate with provenance and bounded claims, never as ambient trust.

## Candidate lifecycle

A third-party component moves through:

```text
DISCOVERED
   ↓
RESOLVED
   ↓
COMPATIBILITY_EVALUATED
   ↓
QUALIFIED_FOR_SCOPE
   ↓
ADMITTED_FOR_USE
   ↓
EXECUTED
   ↓
VERIFIED
   ↓
RECEIPTED
```

A registry entry proves only discovery. A successful import proves only a narrow construction fact. A vendor statement is evidence about vendor intent, not local capability.

## Exact identity

Prefer immutable identities: source commit/tree, package digest, container digest, model revision, dataset version, policy revision, or API version plus observed provider metadata. When a hosted provider does not expose immutable identity, record the uncertainty explicitly. Do not fabricate pinning.

## Qualification envelope

A supplier is qualified for a tuple, not globally:

\[
Q = (subject, capability, mode, environment, policy, verifier, time)
\]

Changing a material dimension may require requalification. A model qualified for document classification is not thereby qualified for tool selection. A package qualified under one runtime is not automatically qualified under another.

## Dependency closure

Qualification includes material transitive dependencies. The evidence package should identify direct dependency, resolved transitive closure where observable, toolchain, build/runtime environment, configuration, external services, generated artifacts, and licenses/policy metadata where required by the organization.

A lockfile without execution evidence is necessary but not sufficient.

## Pack and marketplace supply chain

For deterministic manufacturing, the pack itself is a supply-chain object. A qualified pack publishes canonical identity, source/provenance, dependency lock, owned projections, input schema, output ownership, qualification gym, receipts, and supersession/revocation metadata.

Marketplace installation grants no execution authority.

## Hosted service providers

Hosted providers introduce uncertainty that local pinning cannot remove. Record service/provider identity, API contract/version, region or boundary where material, model/service revision if exposed, observed behavioral contract, outage and retry semantics, data handling constraints, rate and spend limits, verifier behavior, and provider status only as external context.

If the provider cannot support an enterprise requirement, classify the edge UNSUPPORTED rather than silently weakening the requirement.

## Change detection

A material supplier change creates a new candidate edge. Triggers can include digest/revision movement, API behavior change, model revision, permission-scope change, new transitive dependency, policy or license change, changed data boundary, changed verifier result, or a new failure class.

Requalification should be impact-selected: rerun the smallest evidence set that closes the affected capability while preserving unrelated standing.

## Supplier failure

One failed supplier edge is topology. If provider A fails for world W under runtime R, the system records:

```text
(A, W, R) → failed
```

It does not conclude:

```text
A → globally unusable
```

unless evidence supports that broader claim. This allows rapid substitution across preserved capability seams.

## Procurement interface

Procurement should request evidence that can become part of the graph. Useful supplier questions include:

- How is the exact service, model, or runtime revision identified?
- Which actions are effectful?
- Can credentials be scoped to subject, action, and world?
- What deterministic or replay guarantees exist?
- What audit/evidence exports exist?
- Which data boundaries are configurable?
- What failure and rate-limit semantics are documented?
- Can the provider be independently verified?
- How are breaking changes announced and versioned?
- What constraints prevent immutable identity?

Answers should become structured qualification facts rather than remain isolated in a questionnaire.

## Exit and substitution

A capability seam is healthy when the enterprise can replace a supplier without redesigning unrelated consumers. Exit planning therefore includes canonical enterprise semantics independent of provider schema, adapter boundary, exportable evidence, configuration ownership, data migration semantics, alternate candidates in the possibility graph, and regression worlds for substitution.

Lock-in risk is measured as the number and depth of enterprise obligations that cannot be projected through another provider—not merely contract duration.

## Supplier concentration

A Fortune-scale architecture should also expose concentration risk. If many capabilities depend on one provider, runtime, model family, or region, the graph should make that dependence queryable. Where substitution is feasible, preserve alternate compatibility edges before an outage or commercial dispute forces selection under pressure.

## Evidence aging

Qualification evidence has a validity horizon. Evidence can become stale because the subject moves, the verifier changes, policy changes, environment changes, or a vulnerability invalidates assumptions. Staleness downgrades the claim; it does not erase historical evidence.

## Supply-chain crown

A supplier-dependent capability earns standing only when its exact resolved subject, dependency context, local world, admission, execution, independent verification, and receipt are bound.

The falsifier is simple: if the enterprise cannot identify which external subject actually participated in a claimed successful execution, the supply-chain claim is not closed.
