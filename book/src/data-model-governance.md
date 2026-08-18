# Data, Model, and Knowledge Governance

DFCM separates what was observed, what was inferred, what was admitted as enterprise knowledge, and what a model merely proposed. This distinction is essential at scale because data, model output, retrieved context, and generated artifacts frequently collapse into one conversational stream even though they have different authority and evidence.

## Subject classes

Every material object should have a stable class and identity. Common classes include datasets, records, documents, schemas, ontology entities, policies, prompts, model revisions, embeddings, indexes, retrieval results, generated artifacts, plans, intents, receipts, and derived analytical features.

A friendly name is a selector. Standing binds to the resolved subject actually used.

## Observation versus inference

Observed facts are recorded as observations with provenance. Inferred facts record the derivation that produced them. Admitted knowledge records the policy or proof by which an observation or inference became eligible for downstream use.

This gives three non-equivalent states:

```text
observed != inferred != admitted
```

A language model statement does not become an observed fact because it is fluent. A retrieved document does not become policy because it appears in context. A confidence score does not create execution authority.

## Data admission

Data admission checks the constraints relevant to the capability before the data enters canonical decision or manufacturing paths. Depending on domain, that can include schema, provenance, quality, classification, purpose, consent, retention, jurisdiction, freshness, and exact source identity.

Rejected data remains typed evidence where useful. Silent dropping can hide a systematic source failure.

## Model identity

A model is a subject with version, provider, configuration, surrounding system instructions, tool surface, and runtime context. “GPT,” “Claude,” “the classifier,” or “latest” is not enough identity for a material standing claim.

Where a hosted provider cannot expose immutable weights or revision, record the provider's available revision metadata and the residual uncertainty. The evidence claim must be no stronger than the identity available.

## Prompts are configuration, not governance

Prompts can shape behavior and should be versioned where they materially affect results. They do not replace admission policy, authority, consequence controls, or independent verification.

A prompt can ask a model not to publish a secret. The consequence architecture prevents a model from acquiring the publication credential in the first place unless separately authorized.

## Retrieval and RAG provenance

Retrieval systems manufacture observations for a model. Each retrieved item should preserve source identity, retrieval query or selector, revision/freshness where available, ranking provenance, and any transformations applied before presentation.

Derived summaries remain inference. If downstream policy requires exact evidence, the system must retain a path back to the source object rather than only the model's summary.

## Canonical graph authority

The enterprise knowledge graph can hold stable relationships, obligations, subject identities, capability contracts, and policy links. Graph write authority is separate from execution authority.

A generated proposal to add a fact is a candidate graph mutation. It can be admitted, verified, and then written through the graph's own consequence boundary. This prevents model-derived knowledge from silently becoming canonical.

## Derived artifacts

Embeddings, search indexes, caches, feature stores, generated documentation, code, and planner models are projections. Their provenance should identify source graph/data identities and projection/toolchain versions.

When the source changes, the enterprise can decide whether the projection is stale, regenerate it deterministically where possible, and invalidate dependent evidence when required.

## Change triggers

Material changes that can require requalification include:

- dataset revision or schema change,
- model/provider revision,
- prompt or system-policy change,
- retrieval-index rebuild,
- ontology or constraint change,
- embedding model change,
- data classification change,
- jurisdiction or retention-policy change,
- verifier change,
- discovered provenance defect.

The impact graph determines which capability receipts and crowns need to be refreshed.

## Data minimization

The possibility graph should know that a data capability exists without copying all data into every planning context. Minimize observation to what the current actor needs. Sensitive raw evidence can remain behind a stronger access boundary while upstream systems receive bounded projections.

This improves both security and causal clarity: a model cannot rely on state it was never admitted to observe.

## Model failure and abstention

Model uncertainty is not an execution state. Model abstention, invalid output, safety refusal, timeout, and low-confidence classification are provider outcomes that the surrounding system maps into typed process states.

A model can be replaced or ensembled without redefining the enterprise standing ladder. This is one reason to represent policy separately from agent/runtime identity.

## Knowledge correction

When a false canonical fact is discovered, correction should preserve provenance. Record the superseding fact, affected subjects, impacted derived artifacts, and any standing claims that depended on the old fact. Rebuild or replay only the affected closure where possible.

Historical receipts remain evidence of what the system knew and used at the time; correction does not erase history.

## Governance crown

Data/model/knowledge governance closes when every material decision input can be classified as observed, inferred, or admitted; every model and source used in a standing claim has a bounded identity; canonical graph mutations are authorized consequences; derived projections are traceable; and sensitive data exposure is explicit.

The falsifier is a material enterprise claim whose source cannot be distinguished from model inference, or a model-generated fact that becomes canonical or effectful merely by appearing in context.
