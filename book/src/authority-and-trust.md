# Authority and Trust Model

Enterprise AI risk becomes tractable when trust is decomposed. DFCM does not ask whether a component is “trusted.” It asks **trusted for what transformation, over which subject, in which world, under which authority, for how long, with which evidence**.

## Trust is typed

A component may be trusted to parse a schema but not to authorize a deployment. A model may be trusted to propose candidate classifications but not to write the system of record. A registry may be trusted for discovery provenance but not for runtime compatibility.

\[
Trust = (subject, capability, scope, evidence, validity)
\]

Global trust labels are operationally weak because they invite transitive authority.

## Authority capabilities

A consequence capability is represented as:

\[
K = (issuer, holder, subject, action, world, constraints, validFrom, validTo)
\]

Constraints can include resource ceilings, target scopes, data classifications, required approvers, geographic boundaries, rate limits, or evidence obligations.

A capability should be narrowly scoped, revocable, time bounded when practical, attributable to an issuer, inspectable before use, and bound into the execution receipt.

Possession of credentials is not sufficient semantic authority. Credentials are implementation material for an already-defined capability.

## No ambient authority

The following objects have no execution authority by default:

- prompts,
- model output,
- planner output,
- generated code,
- generated configuration,
- tool schemas,
- hooks,
- event subscriptions,
- workflow definitions,
- registry entries,
- CI status,
- documentation.

They can manufacture intents.

An execution architecture fails the authority model if adding a new tool definition silently expands what a model can cause.

## Delegation

Delegation must be explicit and non-expansive.

If capability \(K_1\) delegates \(K_2\):

\[
scope(K_2) \subseteq scope(K_1)
\]

unless a separately authorized issuer grants the expanded scope.

Delegation should retain the causal chain from issuer to current holder. A receipt should be able to answer which authority lineage permitted the action.

## Admission versus authorization

Admission asks whether a transition is structurally and policy-valid enough to consider for execution.

Authorization asks whether this actor possesses a valid capability to cause this exact consequence now.

They are different checks. A semantically valid deployment can still lack deployment authority. An authorized operator can still propose a semantically invalid deployment.

## Trust boundaries

### External inputs

Treat external text, APIs, package metadata, model responses, webhook payloads, and human free-form input as observations or proposals. Normalize before admission.

### Canonical graph

The graph may contain authoritative enterprise semantics, but graph write authority and consequence authority remain separate.

### Manufacturer

A deterministic manufacturer is trusted to reproduce artifacts from admitted inputs. Its output still requires separate authority to actuate.

### BRCE

The consequence broker is trusted with narrow execution capabilities and therefore deserves the strongest isolation, testing, credential hygiene, observability, and change control.

### Verifier

The verifier is trusted to evaluate postconditions. It should not depend solely on the executor’s own success signal.

### Evidence store

The evidence plane is trusted for retained receipts and replay material. Integrity, retention, access, and supersession rules matter because later standing derives from these objects.

## Secret and credential handling

Secrets should never be part of the possibility graph as ordinary values. The graph may reference a credential requirement or capability handle.

The consequence broker resolves the actual secret at the narrowest execution boundary. Receipts record the authority identity and credential class, not secret material.

Credential lifecycle includes issuance, scope, rotation, revocation, use evidence, and orphan detection.

## Prompt injection and semantic injection

A model-facing system should assume that observed content can attempt to redefine system policy, tool semantics, or authority.

The defense is architectural rather than purely linguistic:

1. content remains observation,
2. model output remains intent,
3. admission uses machine-visible policy outside the content channel,
4. authority is checked independently,
5. BRCE owns the only effectful path,
6. the postcondition is verified independently.

An injected instruction can influence proposal quality without acquiring ambient authority.

## Policy conflict

Policies may conflict. DFCM does not hide this behind “the model decides.”

Policy resolution should identify applicable policies, compute obligations/prohibitions, preserve source and effective version, apply precedence rules, produce an admission decision, and record any exception authority.

If the conflict cannot be resolved under known law, the correct standing is BLOCKED or a typed REFUSED outcome.

## Break-glass authority

Emergency authority is a real capability class, not a bypass around the architecture.

A break-glass path should define eligible issuer and holder, narrow consequence scope, expiry, mandatory reason, enhanced receipt obligations, post-event review, and automatic revocation.

Emergency action can be faster without becoming unreceipted.

## Trust review

Walk the causal path and ask at each edge:

1. what object crosses the boundary?
2. what claim is made about it?
3. who admits that claim?
4. what authority is required?
5. can this edge cause consequence?
6. what evidence proves the edge ran?
7. what state results if evidence is missing?

Any “it is trusted” answer should be decomposed until those questions are explicit.

## Crown condition

The authority model closes when every consequential path satisfies:

\[
DO \Rightarrow admitted \land authorized \land brokered \land receipted
\]

and there is no alternate effectful path with weaker semantics.

The falsifier is one consequential route that bypasses the declared authority broker.
