# Procurement and Enterprise Evaluation

Procurement for AI, automation, workflow, model, data, and platform suppliers should test whether the supplier can participate in the enterprise causal contract. Feature counts and benchmark scores remain useful, but they are downstream of identity, authority, consequence, evidence, and exit requirements.

## Hard admission questions

Before weighted scoring, define hard fences. A supplier that fails a non-negotiable boundary remains UNSUPPORTED for that capability even if its aggregate score is excellent.

### Identity and versioning

- Can exact code, model, dataset, container, or service revisions be identified?
- Which components remain mutable or opaque?
- How are breaking changes announced?
- Can the enterprise pin or at least observe the version used in a transaction?

### Authority

- Can credentials be scoped to action, subject, tenant, environment, region, or resource class?
- Are short-lived credentials or delegated capabilities supported?
- Can read, plan, construct, and effectful permissions be separated?
- Can emergency access be time bounded and audited?

### Consequence semantics

- Which APIs create persistent, external, billable, published, access-changing, or irreversible effects?
- What idempotency guarantees exist?
- What happens on timeout after server acceptance?
- How are partial consequences exposed?

### Verification and evidence

- Can the result be independently observed?
- What request, event, audit, or transaction identifiers are returned?
- Can evidence be exported without relying on the supplier UI?
- Are historical records stable and versioned?

### Data and knowledge governance

- What data is retained, trained on, transferred, or cached?
- Can geographic and tenant boundaries be constrained?
- What provenance exists for retrieved or generated material?
- Can enterprise policy be enforced outside model prompts?

### Reliability

- What are timeout, retry, rate-limit, and outage semantics?
- What recovery mechanisms exist?
- Can the enterprise test failure modes?
- Which dependencies or regions create concentration risk?

### Supply chain

- What transitive components materially affect the service?
- Which artifacts have immutable digests?
- What vulnerability and change notification exists?
- Can qualification evidence be tied to exact versions?

### Exit

- Can data, configuration, evidence, prompts, policies, and audit records be exported?
- Which semantics are proprietary?
- Can an alternate provider implement the same capability seam?
- What transition assistance and deletion proof exist?

## Evidence package before scale

A serious evaluation should request a proof package, not only questionnaire answers. Depending on product class, the package can include exact version metadata, architecture boundaries, permission model, audit-event examples, API specifications, failure semantics, data-flow documentation, portability artifacts, independent assessment, and a controlled enterprise proof in a bounded world.

Marketing documentation is candidate evidence. Local execution remains the strongest proof for the enterprise’s actual environment.

## Weighted evaluation

After hard fences, use a multidimensional vector rather than one universal supplier score. Example dimensions:

| Dimension | Example measures |
|---|---|
| Capability | verified task/postcondition coverage |
| Identity | precision and immutability of subject resolution |
| Authority | least-privilege and delegation support |
| Evidence | exportability, integrity, replay value |
| Reliability | failure semantics and recovery quality |
| Economics | cost per verified consequence |
| Portability | seam quality and migration effort |
| Governance | policy/data boundary fit |
| Operations | incident/change/release integration |

Different capabilities can weight dimensions differently. A payment provider and a read-only research service should not share one risk weighting.

## Challenger test

Do not ask only whether the vendor supports the incumbent workflow. Ask whether the vendor removes work while preserving the underlying obligation.

A supplier that requires the enterprise to keep unnecessary manual translation, approval theater, or duplicated state may be automating the old mechanism instead of improving the capability architecture.

The enterprise owns the business semantics. Vendor products compete to satisfy those semantics behind capability seams.

## Commercial alignment

Commercial terms can affect architecture. Pay attention to:

- pricing dimensions that encourage uncontrolled exploration,
- minimum commits that create lock-in,
- data-egress cost,
- API quotas and burst behavior,
- evidence/audit export availability by tier,
- regional availability,
- support-response obligations,
- termination and deletion terms.

Put material commercial constraints into the same resource/governance graph used for admission where practical.

## Proof before production scale

Qualification should progress from isolated construction to bounded integration to production-like consequence. The supplier does not receive broad credentials or unrestricted data before the narrower evidence closes.

A useful proof sequence is:

```text
identity/provenance
→ contract/schema
→ sandbox integration
→ negative/refusal tests
→ production-like scenario
→ independent verifier
→ receipt/replay
→ capability standing
```

Only the proven edge is promoted.

## Renewal and requalification

Renewal should consider evidence since the original purchase: reliability incidents, revision churn, cost per verified consequence, data/governance changes, replay health, concentration, and success of portability tests.

A supplier may remain commercially attractive while one capability edge is downgraded. DFCM permits selective requalification rather than forcing an all-or-nothing vendor label.

## Concentration and optionality

The possibility graph should reveal which enterprise capabilities depend on the same model family, cloud, supplier, region, package ecosystem, or proprietary schema. Concentration can be accepted deliberately, but it should not be discovered only during an outage or negotiation.

Where the cost is justified, qualify alternate edges while the primary supplier is healthy.

## Procurement crown

A procurement decision closes when the required hard constraints are satisfied, the exact supplier capability is demonstrated in the intended environment, authority and evidence surfaces are understood, economic bounds are measurable, and an exit/substitution path is explicit enough for the risk class.

The falsifier is a critical supplier selected primarily from brand, demo, questionnaire score, or benchmark rank when the enterprise cannot identify its effectful boundaries, exact participating subject, independent verification path, or exit semantics.
