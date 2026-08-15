# Audit and Evidence Dossier

Audit should not require reconstructing system behavior from screenshots, ticket narratives, or interviews. A DFCM system produces an evidence dossier from the same receipts and identities that establish standing during normal operation.

The dossier is therefore a projection of causal truth, not a parallel compliance database.

## Dossier structure

For a scoped capability, release, incident, or policy decision, the dossier should be able to expose:

### Identity

- exact subject and friendly selectors,
- source revision or digest,
- dependency/runtime identities,
- world/environment identity,
- relevant model/data/policy revisions.

### Admission

- normalized input or intent,
- applicable policy identities,
- precondition evaluation,
- resource bounds,
- admission/refusal result and reason.

### Authority

- authority capability identity,
- issuer and holder,
- subject/action/world scope,
- validity interval,
- exception or break-glass lineage if used.

### Execution

- executor identity,
- attempted consequence,
- timestamps/sequence,
- idempotency or request identity,
- external provider references,
- partial/failure result where applicable.

### Verification

- declared postcondition,
- verifier identity,
- independent observation,
- observed result,
- verifier configuration/version.

### Receipt

- receipt identifier/digest,
- causal parent receipts,
- consequence references,
- integrity metadata,
- supersession relations.

### Replay

- replay manifest,
- required source/runtime material,
- equivalence predicate,
- replay result and receipt.

### Standing

- standing derivation,
- scope,
- promotion/downgrade history,
- release-crown membership,
- known residual UNKNOWNs.

## Evidence minimization

Auditability does not require copying sensitive payloads into every receipt. Store references, hashes, classifications, bounded excerpts, or encrypted evidence according to policy. The receipt needs enough identity to establish causal linkage while the raw evidence can remain in a more restricted store.

The same principle applies to credentials: retain authority identity and scope, never secret values.

## Integrity

Evidence integrity should survive dashboard and application changes. Common mechanisms include content addressing, append-oriented or versioned storage, signed attestations where needed, immutable object IDs, and explicit supersession rather than destructive overwrite.

The architecture should detect a receipt whose content no longer matches its identifier or whose referenced subject has been substituted.

## Retention

Retention is policy-specific. Different evidence classes can have different horizons:

- operational debug detail,
- financial transaction evidence,
- policy/authority decisions,
- release crowns,
- security incidents,
- replay bundles,
- supplier qualification.

Deletion is itself a governed lifecycle event. If retention expiry makes a claim no longer replayable, standing and audit expectations must reflect that policy rather than pretend evidence still exists.

## Supersession

A corrected policy, new release, requalification, or incident review does not erase prior evidence. Link old and new claims through supersession or invalidation relations.

This permits audit questions such as:

- What did the system believe at the time?
- Which policy authorized the action then?
- When was the claim later invalidated?
- Which releases depended on the affected receipt?

History remains causal rather than rewritten.

## Audit queries

The evidence model should answer queries directly:

- show every production consequence caused by subject S;
- show actions using break-glass authority during interval T;
- show ALIVE claims whose verifier has been superseded;
- show releases depending on supplier revision X;
- show refused actions by policy reason;
- show receipts that cannot currently replay;
- show standing downgrades caused by incident I;
- show all consequence paths lacking an independent verifier;
- show active exceptions nearing expiry;
- show the exact evidence behind an executive process metric.

If each query requires a manual data-integration project, the evidence spine is too fragmented.

## Sampling

Audit can sample from the receipt population rather than asking teams to stage demonstrations. A useful sampling procedure selects receipts across consequence classes, authorities, providers, environments, and time periods, then attempts reconstruction.

A random receipt should answer:

1. what exact subject ran?
2. what was admitted?
3. under whose authority?
4. what consequence occurred?
5. how was it independently verified?
6. what standing resulted?
7. can the required evidence be replayed or reconstructed?

The percentage of sampled receipts that close this chain is a powerful control metric.

## Access

Evidence access is itself authorized. Auditors may need broad read access without consequence authority. Operators may need raw evidence for one domain without access to unrelated sensitive data. Use capability-scoped access and log evidence reads where policy requires it.

## External audit package

For external review, generate a bounded export containing claim definitions, exact identities, policy/authority lineage, receipt indexes, verifier descriptions, selected evidence, integrity metadata, replay instructions where allowed, and explicit exclusions.

The package should be reproducible from canonical evidence and carry its own generation identity.

## Audit crown

The audit surface is complete when a material standing claim can be reconstructed from identity through admission, authority, consequence, verification, receipt, and replay without relying on undocumented operator memory.

The falsifier is a production claim whose audit evidence exists only as screenshots, narrative status, or logs that cannot be tied to the exact subject and authority that caused the consequence.
