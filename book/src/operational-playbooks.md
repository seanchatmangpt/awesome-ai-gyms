# Operational Playbooks

Patterns become operational when recurring situations have a bounded sequence, explicit stopping conditions, and evidence. These playbooks are default routes through the pattern graph; they are not privileged alternatives to the underlying admission, authority, or receipt rules.

## A. Integrate an external gym or benchmark

1. Preserve the candidate with provenance and default UNKNOWN standing.
2. Resolve the exact upstream subject.
3. Define the local world contract and consequence boundary.
4. Build a thin [World Adapter](patterns/discovery-composition/15-world-adapter.md) without forking upstream behavior unnecessarily.
5. Declare observation/action mappings and reset semantics.
6. Run compatibility tests for each intended planner/runtime edge.
7. Execute only inside the admitted gym boundary.
8. Verify benchmark/world postconditions independently where possible.
9. Emit receipts and promote only the exact qualified edge.

Stop if provider identity, licensing/policy, world reset, or consequence semantics cannot be bounded. Record UNSUPPORTED or BLOCKED rather than weakening the contract silently.

## B. Qualify a ggen pack

1. Pin pack source and dependencies.
2. Validate pack ontology and input contract.
3. Start from an empty/minimal controlled consumer.
4. Run the real deterministic manufacture path.
5. Build the generated consumer under a pinned toolchain.
6. Execute the consumer’s project gym.
7. Delete/regenerate or sync twice to detect drift.
8. Bind the qualification receipt to exact pack and toolchain identities.
9. Publish qualification metadata to the marketplace.

The crown fails if manual glue is required after generation to make the promised capability work.

## C. Introduce or replace a planner/model

1. Register it as a candidate provider with exact identity/provenance.
2. Define which planner/policy capability it may provide.
3. Keep the existing provider edge intact.
4. Project the same admitted problem into compatible formulations.
5. Compare quality, latency, cost, refusal behavior, and evidence.
6. Treat all output as powerless selection/intent.
7. Run the same downstream admission and authority path.
8. Update selector policy only after comparative evidence.

Do not grant new consequence authority merely because the new provider supports tool calls.

## D. Add a new consequential action

1. Name the exact consequence class.
2. Inventory all paths that could cause it.
3. Define the normalized intent schema.
4. Define preconditions and admission rules.
5. Define authority capability and issuer.
6. Add the effectful adapter only behind BRCE.
7. Define idempotency, timeout, and partial-consequence semantics.
8. Build an independent postcondition.
9. Add negative/refusal tests proving bypass is impossible.
10. Add receipt and replay fields.
11. Add the capability to the relevant release crown.

The action is not ready because the API call works; it is ready when the causal contract closes.

## E. Repair a failed capability

1. Preserve the failed receipt, world, subject, and exact hypothesis.
2. Classify failure: semantic, build, authority, runtime, verifier, replay, resource, or external dependency.
3. Attach failure to the narrowest topology edge supported by evidence.
4. Form a new repair hypothesis.
5. Change one causally relevant mechanism where practical.
6. Encode a durable guard, refusal, fixture, schema, theorem, or regression scenario.
7. Rerun the failed boundary first.
8. Expand verification only after that boundary succeeds.
9. Update standing and supersession links.

Never rerun an unchanged failure repeatedly without a new hypothesis.

## F. Replace a third-party provider

1. Preserve existing provider standing and receipts.
2. Resolve alternate provider identity.
3. Map through the existing capability seam.
4. Compare semantic gaps explicitly.
5. Qualify required world/mode/runtime edges.
6. Run production-like verifier scenarios.
7. Verify data export/migration and authority scopes.
8. Promote the new edge through a release crown.
9. Revoke or narrow old provider authority when cutover completes.

Do not make supplier substitution a schema rewrite for every consumer.

## G. Crown a release

1. Resolve exact release subject and dependency closure.
2. Load the release-crown DAG.
3. Reject stale or wrong-subject evidence.
4. Verify required policy/authority versions.
5. Verify required capability receipts.
6. Verify negative/refusal evidence where mandatory.
7. Verify replay requirements.
8. Verify maturity floor.
9. Produce the crown receipt.
10. Publish release standing as a projection of that receipt.

No dashboard override can manufacture a missing crown node.

## H. Grant a policy exception

1. Identify the exact governing policy.
2. Prove the normal path would refuse or block.
3. Define the minimal subject/action scope.
4. Name issuer and holder.
5. Set validity/expiry.
6. Define compensating controls and enhanced evidence.
7. Issue the exception capability.
8. Bind its use into receipts.
9. Revoke automatically or explicitly when the validity period closes.
10. Review recurring exceptions for conversion into durable policy.

An exception is a scoped object, never “ignore the rule.”

## I. Emergency recovery

1. Preserve current evidence before mutation when feasible.
2. Revoke compromised or uncertain authority.
3. Establish incident world/subject scope.
4. Issue break-glass capability if normal authority cannot satisfy recovery time.
5. Perform recovery through BRCE.
6. Independently verify recovered postconditions.
7. Emit enhanced recovery receipts.
8. Downgrade affected standing until replay/requalification closes.
9. Convert root cause into durable law.

Emergency execution remains receipted execution.

## J. Retire a capability

1. Enumerate consumers, authorities, crown dependencies, and historical evidence.
2. Confirm replacement or deliberate removal of each obligation.
3. Revoke new-use authority.
4. Drain or resolve in-flight intents.
5. Retain historical receipts under policy.
6. Remove provider edges and generated projections safely.
7. Verify no release crown still depends on the retired capability.
8. Record retirement/supersession in the canonical graph.

## Playbook invariant

Every playbook follows the same deeper path:

```text
observe → resolve → admit/refuse → select/construct → authorize → DO → verify → receipt → replay/standing → learn
```

A specialized playbook may skip a step only when the step is genuinely not applicable or a valid prior receipt can be reused under an explicit equivalence relation. The playbook is falsified when its convenience path creates weaker authority, evidence, or identity semantics than the canonical lifecycle.
