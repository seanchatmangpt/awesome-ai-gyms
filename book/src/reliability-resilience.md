# Reliability and Resilience

Reliability in a DFCM system is not “the agent usually succeeds.” It is the ability to preserve correct standing and bounded consequence when dependencies fail, retries occur, worlds drift, partial effects happen, and evidence is incomplete.

The reliability design begins by typing failure instead of treating all failure as one exception channel.

## Failure taxonomy

A useful minimum taxonomy includes:

- **semantic failure** — subject, schema, or precondition is invalid;
- **admission refusal** — candidate is understood but outside declared law;
- **authority denial** — the intent is admissible but the actor lacks consequence capability;
- **materialization failure** — required source or dependency cannot be resolved;
- **build failure** — exact subject cannot reach runnable form;
- **runtime failure** — executor cannot complete the admitted operation;
- **partial consequence** — some effects occurred but the requested postcondition is not closed;
- **verification failure** — executor returned success but independent postcondition is false or unknown;
- **evidence failure** — the action may have occurred but required receipt/replay material is incomplete;
- **replay failure** — prior evidence cannot be reconstructed under the declared equivalence relation;
- **external dependency failure** — provider, network, credential service, region, or system of record is unavailable;
- **budget exhaustion** — bounded resources are consumed before closure.

Each failure class has different recovery semantics. Retrying an authority denial is wrong. Rebuilding a semantic refusal is waste. Treating a partial consequence as a clean failure can duplicate effects.

## Idempotency and retries

Retry safety is a property of the consequence contract, not of the HTTP status code.

For every effectful operation, define:

- idempotency key or equivalent subject identity,
- duplicate-detection semantics,
- timeout semantics,
- provider acknowledgment semantics,
- observable postcondition,
- recovery action if the prior result is UNKNOWN.

When the system cannot determine whether a consequence occurred, it should enter a typed uncertain state and observe the world before issuing a new DO transition.

## Partial consequence

Distributed operations often cross several irreversible boundaries. A deployment may update two regions and fail in the third. A payment workflow may submit to a provider but fail before local acknowledgment. A publication may be externally visible even though the caller times out.

Partial consequence must produce a partial receipt containing completed effects, unresolved effects, verifier observations, and permitted recovery intents. Recovery itself is a new admitted and receipted consequence—not an untracked cleanup script.

## Recovery through the same authority boundary

Recovery paths are often more dangerous than normal paths because they receive elevated credentials and fewer checks. DFCM applies the same BRCE rule to rollback, reconciliation, replay repair, and emergency action.

A rollback is DO. A compensating transaction is DO. A restore is DO. A forced state repair is DO.

Emergency speed changes the authority envelope; it does not remove the consequence boundary.

## Reset and reconstructability

For gyms and controlled worlds, prefer reconstructable ephemeral environments. A reset should return the world to a named baseline and run an independent reset verifier.

Where exact reset is impossible, define an equivalence class. For example, regenerated identifiers may differ while the application-level state is equivalent. The equivalence predicate must be declared before results are compared.

## Reliability objectives

Traditional availability remains important, but DFCM adds causal objectives.

Useful service-level indicators include:

- admission decision latency,
- authority-check latency,
- consequence success rate,
- independent postcondition success rate,
- percentage of attempted consequences with valid receipts,
- percentage of receipts replayable within target time,
- reset leakage rate,
- evidence freshness,
- mean time from failure to typed localization,
- mean time from localized failure to durable guard,
- recovery actions with complete receipts.

A system can have high API uptime while having low evidentiary reliability.

## Graceful degradation

Degradation should remove capability edges, not silently weaken invariants.

Examples:

- if a preferred planner is unavailable, select another compatible planner;
- if a noncritical enrichment source is unavailable, preserve the observation as missing rather than inventing it;
- if independent verification is unavailable, execution may be blocked or standing may remain PARTIAL_ALIVE according to policy;
- if authority service is unavailable, consequence fails closed unless a separately designed break-glass capability exists;
- if a supplier is degraded, route through an already qualified alternate edge rather than dynamically trusting an unknown provider.

## Capacity and backpressure

Reliability requires bounding queues. Admission should consider executor capacity, provider rate limits, verifier capacity, and human-review capacity. When the downstream consequence plane is saturated, upstream planners should not continue manufacturing unlimited intents.

Backpressure is part of lawful admission. Queue growth is evidence that the current possibility graph cannot be actuated at the requested rate.

## Chaos and fault injection

High-assurance gyms should inject failures at the boundaries that matter:

- resolver returns a moved subject,
- provider times out after accepting a request,
- credential expires between admission and DO,
- verifier disagrees with executor,
- receipt store becomes unavailable,
- reset leaves residue,
- one region fails during a multi-region operation,
- replay resolves a different dependency,
- rate limit or cost budget is exhausted.

The objective is not to demonstrate that nothing fails. It is to prove that failure produces bounded consequence, correct standing, and recoverable evidence.

## Resilience portfolio

DFCM preserves alternate lawful routes before an incident. That can include multiple planners, multiple suppliers, multiple runtime modes, offline toolchains, cached immutable dependencies, and independent verification paths.

Alternatives must still be qualified. An untested fallback is a candidate, not resilience.

## Reliability crown

A capability is resilient when failure of an admitted dependency causes one of three defensible outcomes: successful bounded substitution, typed safe refusal/blocking, or a receipted partial consequence with a lawful recovery path.

The reliability claim is falsified when a common dependency failure produces unbounded retry, duplicate consequence, silent standing promotion, unreconstructable partial state, or a recovery path that bypasses normal authority and evidence controls.
