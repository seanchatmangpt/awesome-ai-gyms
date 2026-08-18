# Assurance Case

An assurance case explains why a scoped capability claim deserves standing. DFCM makes the case inspectable by binding claims to exact subjects, explicit falsifiers, independent evidence, and replay rather than to confidence language.

## Claim tuple

A useful assurance claim is:

\[
Q = (subject, capability, world, mode, policy, time, standing)
\]

Each dimension matters. “The system is secure” or “the agent can deploy” is too broad to audit. A defensible claim might be: exact subject S can perform deployment capability C in world W under policy P using authority mode M, with ALIVE standing as of evidence set E.

## Evidence ladder

Evidence has different strength depending on the claim.

### Inspection

Proves source/configuration contains a structure. It does not prove execution.

### Build/static verification

Proves the subject can be constructed or satisfies static constraints under a toolchain.

### Unit verification

Proves narrow implementation contracts.

### Integration verification

Proves interactions across concrete components.

### Gym/behavioral verification

Proves a bounded capability against an executable world and declared postcondition.

### Consequence verification

Proves the actual effectful transition occurred against the exact admitted subject and target.

### Replay verification

Proves the prior claim can be reconstructed under the declared equivalence predicate.

Use the lowest-cost evidence sufficient for the claim, but never substitute a weaker rung for a stronger acceptance boundary. A unit test cannot prove a real external deployment; a production consequence need not be repeated for a purely static spelling change if exact equivalence law supports reuse.

## Argument form

Every high-value claim should answer:

1. **Subject:** What exact thing is being claimed about?
2. **Context:** In which world, mode, runtime, and policy?
3. **Claim:** What capability/postcondition is asserted?
4. **Falsifier:** What observation would defeat or narrow the claim?
5. **Evidence:** Which receipts and verifier outputs support it?
6. **Independence:** Is the evidence independent enough from the component making the claim?
7. **Validity:** Are identities current and non-superseded?
8. **Replay:** What can be reconstructed and under what equivalence?
9. **Residual UNKNOWN:** What is deliberately not proven?

This format makes scope reduction a normal result rather than a rhetorical failure.

## Independence

Evidence independence is proportional to the failure mode being tested. A verifier does not always need a separate organization or technology stack, but it must not merely restate the executor’s own success signal when correlated failure would matter.

Examples:

- deployment API returns success → independently query target state;
- generator emits a file → build/run the generated consumer;
- policy engine allows an action → negative tests prove prohibited variants refuse;
- release workflow reports success → observe the public or production postcondition.

## Negative assurance

Enterprise assurance includes proof of refusal, not only proof of success.

Important negative claims include:

- an unauthorized actor cannot cross BRCE;
- a refused intent has no downstream DO event;
- a model tool call is insufficient authority;
- a wrong subject/revision cannot reuse another subject’s receipt;
- a stale policy cannot silently govern a new release;
- an over-budget search is refused;
- a tampered receipt invalidates dependent standing.

A system that only exercises happy paths cannot claim the authority boundary is closed.

## Evidence scope and inheritance

Evidence belongs to the exact identity tuple it observed. Reuse requires explicit equivalence. Valid reuse can dramatically reduce enterprise verification cost, but accidental inheritance creates false standing.

For cached verifier evidence, compare at least source identity, validator identity, toolchain, relevant configuration, environment, policy, and external dependencies. If material identity differs, prove equivalence or rerun.

## Evidence age

Evidence can expire operationally even when bytes have not changed. Reasons include supplier movement, policy revision, credential model change, vulnerability discovery, external environment movement, or verifier defect.

Validity policy should state which evidence classes have event-driven invalidation and which have time-based review horizons.

## Deterministic manufacture as assurance

When projections are deterministic, regeneration becomes a verifier. If identical admitted semantics and toolchain identities produce different canonical artifacts, the manufacturing claim is falsified.

This is especially important for policy, documentation, deployment manifests, planning models, and code generated from an ontology. Drift is evidence that an unmodeled input exists.

## Assurance graph

The assurance case should be machine-readable enough to compute dependencies:

```text
claim
 ├─ exact subject
 ├─ admission receipt
 ├─ authority receipt
 ├─ execution receipt
 ├─ independent verifier receipt
 ├─ replay receipt
 └─ dependencies / subclaims
```

A release crown is an assurance graph whose required root claim is release standing.

## Review

Human assurance review should focus on whether the claim scope, falsifier, independence, and equivalence rules are appropriate—not manually reperform every automated check. This keeps humans on semantic and authority questions that are difficult to reduce while allowing machines to verify repetitive closure.

## Anti-patterns

- **Badge assurance:** treating CI, certification, or vendor status as local execution proof.
- **Narrative substitution:** a report says success without receipt linkage.
- **Adjacent evidence:** neighboring version or environment is used without equivalence proof.
- **Executor self-attestation:** success return is the only postcondition.
- **Falsifier-free claims:** nothing could disprove the architecture statement.
- **Unknown suppression:** missing evidence is converted to a green status.
- **Scope inflation:** one scenario proves an entire product or organization.

## Assurance crown

An assurance case has standing when every material claim is exact-subject bound, falsifiable, supported by evidence at the required rung, independently verified where correlated failure matters, and connected to replay or explicit limitations.

The falsifier is a material crown claim that remains “proven” after its supporting receipt, subject identity, or verifier is removed or shown invalid.
