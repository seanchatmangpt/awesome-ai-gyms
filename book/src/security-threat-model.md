# Security and Threat Model

The DFCM security model starts from one premise: **proposal surfaces will be compromised, mistaken, adversarial, stale, or merely wrong**. Security therefore does not depend on perfect model behavior. It depends on preventing proposal authority from becoming consequence authority.

## Protected assets

The threat model protects canonical semantic and governance graphs, subject identity and provenance, execution credentials, authority capabilities, consequential systems and data, verifier integrity, receipts and replay material, release standing, supply-chain identities, and resource budgets.

A threat matters when it can corrupt one of these assets or create an unreceipted consequence.

## Primary threat classes

| Threat | Attack path | Primary boundary | Required evidence |
|---|---|---|---|
| Prompt/content injection | observation attempts to redefine policy or tool authority | intent/admission | normalized intent + independent policy decision |
| Tool escalation | model selects a more powerful tool than intended | authority | scoped capability and typed denial |
| Hidden side effect | nominal read mutates, bills, publishes, or allocates | consequence inventory | effect classification + receipt |
| Subject substitution | mutable alias resolves to different code/model/data | identity | exact subject binding |
| Supply-chain drift | dependency changes after qualification | materialization | digest/version lock + qualification evidence |
| Credential leakage | secret appears in model/context/log/evidence | consequence zone | secret-boundary controls + redaction evidence |
| Verifier capture | executor controls its own success proof | evidence | independent postcondition |
| Receipt tampering | historical evidence altered or detached | evidence | content addressing and integrity controls |
| Replay poisoning | replay uses different subject/world/policy | replay | replay manifest + equivalence predicate |
| Budget exhaustion | planner explores without resource fence | admission | budget envelope + counters |
| Cross-tenant bleed | world state or cache leaks between subjects | sandbox/reset | isolation and reset proof |
| Policy downgrade | new config silently weakens admission | governance | policy version + release crown |
| Hook escalation | event callback directly actuates | BRCE | hook produces intent only |
| Inference laundering | model-derived fact stored as observed truth | evidence semantics | observation/inference typing |
| Federation trust leak | remote evidence grants local execution rights | federation | local authority check |

## Prompt and content injection

Prompt injection is a special case of semantic injection: untrusted content attempts to redefine how the system interprets authority or tools.

The DFCM defense chain is:

```text
untrusted content
     ↓
observation
     ↓
model/planner proposal
     ↓
normalized intent
     ↓
admission against external policy
     ↓
authority capability check
     ↓
BRCE
     ↓
independent verification
```

The attacker may influence the proposal. They do not acquire the capability required for DO. This architecture does not make model behavior irrelevant; bad proposals still consume resources and can exploit weak admission semantics. It prevents linguistic success from being sufficient execution authority.

## Supply-chain boundary

Every executable or policy-relevant dependency should resolve to an immutable identity where the provider allows it. Qualification binds source identity, dependency closure, toolchain identity, configuration, world, verifier, and receipt. A package name or marketplace presence is not a capability claim. Requalification is triggered when a material identity changes.

## Credential boundary

Credentials are resolved as late as possible and held by the narrowest consequence component. Controls include no secrets in prompts or canonical graph values, capability handles rather than raw credentials upstream, short-lived credentials where practical, target-scoped permissions, rotation and revocation, separate verifier credentials when independence requires it, and evidence redaction that preserves authority identity without secret material.

## Evidence boundary

Evidence can be attacked after execution. Protect receipt integrity, subject linkage, timestamps and sequence semantics, verifier identity, replay references, supersession relationships, access, and retention controls. A valid receipt should not become invalid merely because a dashboard entry was deleted.

## Denial of wallet and attention

Autonomous exploration can create economic denial of service even when no security policy is violated. Admission should constrain maximum attempts, concurrent branches, compute, external API spend, tokens, wall-clock time, storage, and human review demand. Exhausting the reviewer queue is a real consequence.

## Federation boundary

A federated enterprise should exchange claims without exchanging ambient authority. A remote domain can publish subject identity, capability claim, receipt, maturity, and provenance. The local domain decides whether to trust that evidence for a local purpose. It does not inherit the remote domain’s credentials or execution rights.

## Security testing strategy

### Structural tests

Prove that every effectful adapter is reachable only through the declared broker.

### Negative admission tests

Attempt known illegal intents and verify typed refusal before mutation.

### Confused-deputy tests

Use a low-authority caller to request a high-authority action through an intermediate component.

### Subject-substitution tests

Move aliases while pinning expected identities and verify mismatch refusal.

### Injection tests

Place adversarial instructions in observations, documents, tool results, and external metadata; verify they remain proposal content.

### Reset and isolation tests

Execute scenarios in different orders and tenants and compare post-reset state.

### Evidence-tamper tests

Alter receipt fields, verifier outputs, replay manifests, or dependency identities and verify crown invalidation.

### Break-glass tests

Exercise emergency authority, expiry, enhanced receipts, and revocation.

## Incident standing

A security event can downgrade standing without erasing history. A compromised runtime identity can reduce an affected capability to PARTIAL_ALIVE or BLOCKED pending requalification. An evidence-integrity breach can make claims depending on affected receipts UNKNOWN. A leaked authority capability is revoked and future DO blocked while historical receipts remain evidence of what occurred. Verifier capture invalidates verifier-dependent crown nodes until independent verification is restored.

## Security crown

The security architecture closes only when every known consequence path is inventoried, every consequence path crosses admission and explicit authority, every effectful path is brokered, secrets are confined to the consequence boundary, success is independently verified, receipts preserve causal integrity, replay detects identity drift, and negative tests prove refusal behavior.

The decisive falsifier is one real state-changing path that bypasses those controls.
