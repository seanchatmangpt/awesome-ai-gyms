# DFCM Calculus

DFCM is not a preference for “more options.” It is a bounded calculus for preserving reversible lawful structure while concentrating irreversible consequence behind the smallest admissible authority boundary.

## Objects

Let the enterprise system contain the following typed objects:

\[
\mathcal{O} = \{S,W,O,O^\star,G,P,I,K,A,C,V,R,E,\Sigma\}
\]

where:

| Symbol | Object |
|---|---|
| \(S\) | exact subject: code, model, dataset, policy, pack, workflow, or service revision |
| \(W\) | bounded world in which behavior is observed |
| \(O\) | raw observation |
| \(O^\star\) | admitted, aligned, grounded, bounded observation |
| \(G\) | reversible possibility graph |
| \(P\) | plan or formulation |
| \(I\) | powerless intent |
| \(K\) | scoped authority capability |
| \(A\) | manufactured artifact |
| \(C\) | observed consequence |
| \(V\) | independent verifier result |
| \(R\) | deterministic receipt |
| \(E\) | replay/evidence material |
| \(\Sigma\) | scoped standing |

Identity is part of the object. `main`, `latest`, “the current policy,” and “the model” are selectors, not sufficient subject identities.

## Morphisms

The lawful lifecycle is a composition of typed morphisms:

\[
W \xrightarrow{observe} O \xrightarrow{admit} O^\star \xrightarrow{preserve} G \xrightarrow{select} P \xrightarrow{intent} I
\]

Construction is separate:

\[
(O^\star, Pack, Toolchain) \xrightarrow{\mu} A
\]

Authority is separate:

\[
(I,K,W,S) \xrightarrow{authorize} I^\star
\]

Only then may consequence occur:

\[
I^\star \xrightarrow{BRCE} C \xrightarrow{verify} V \xrightarrow{receipt} R \xrightarrow{standing} \Sigma
\]

Replay is not a duplicate execution command. It is a morphism constrained by an equivalence relation:

\[
R \xrightarrow{reconstruct(E,\sim)} R'
\]

where \(R' \sim R\) must be evaluated using a predeclared equivalence predicate.

## Partial morphisms and refusal

Not every input admits a lawful output. `admit`, `authorize`, `materialize`, and `execute` are partial morphisms. A missing morphism does not collapse into a generic exception.

For a requested transition \(x\):

\[
f(x) \in \{y,\ REFUSED_t,\ BLOCKED_t,\ UNSUPPORTED_t,\ BUILD\_BROKEN_t\}
\]

A typed refusal is a valid terminal outcome. It proves that the system recognized a candidate and deliberately prevented consequence under declared law.

## SELECT, CONSTRUCT, DO

The three modes are intentionally non-equivalent.

### SELECT

SELECT explores or chooses among reversible candidates. It may rank, optimize, schedule, search, formulate, or compare. It has no ambient consequence authority.

### CONSTRUCT

CONSTRUCT manufactures artifacts—plans, code, configuration, graphs, policies, templates, reports, or executable bundles. Construction may be deterministic and may produce powerful objects, but the existence of an executable artifact does not confer permission to execute it.

### DO

DO crosses the consequence boundary. It may mutate durable state, publish, spend, grant access, deploy, send, delete, approve, transact, or otherwise alter the world. DO is brokered and receipted.

The fundamental non-equivalences are:

```text
representable != admitted
admitted != selected
selected != authorized
authorized != executed
executed != verified
verified != replayable
constructed != permitted
logged != receipted
```

## Admission

Admission transforms raw possibility into bounded possibility.

An admission decision is a function of at least:

\[
admit(S,W,I,Policy,Authority,Resources,EvidenceRequirements)
\]

Admission validates semantic shape, subject identity, preconditions, exclusions, authority requirements, resource bounds, and required evidence. It does not need to prove that execution will succeed; it proves that attempting the transition is lawful within the declared envelope.

The complement of the admitted region must remain visible. A rejected candidate should carry a typed reason rather than disappearing from history.

## DFCM objective

Let \(G_r\) be the reversible candidate graph and \(B\) the set of hard bounds induced by ontology, authority, physics, policy, cost, and evidence.

DFCM seeks:

\[
G^\star = \max_{\subseteq}\{g \subseteq G_r \mid g \models B\}
\]

until an irreversible decision must be made.

The objective is **not** to actuate all lawful possibilities. It is to preserve them long enough that selection can use more information. One failed edge removes or penalizes that edge; it does not justify deleting unrelated nodes.

## Closure

A capability claim closes only when the causal chain is complete.

For a scoped claim \(q\):

\[
close(q) = subject(q) \land admission(q) \land authority(q) \land execution(q) \land independentVerification(q) \land receipt(q)
\]

For claims requiring replay:

\[
close_{replay}(q) = close(q) \land replay(q)
\]

For a release crown, closure is a DAG condition: every required node resolves to valid, non-superseded evidence for the exact release identities.

## Standing as a derived value

Standing is not manually assigned decoration. It is a derivation over evidence.

```text
UNKNOWN
  ├─ BLOCKED
  ├─ UNSUPPORTED
  ├─ BUILD_BROKEN
  ├─ REFUSED(type)
  └─ PARTIAL_ALIVE
          └─ ALIVE
```

The side states represent distinct causal outcomes. A secure refusal can be the correct behavior and should not be coerced into a failure.

## Authority calculus

Authority is a capability \(K\), not a property of the calling component.

\[
K = (issuer, subject, actor, action, world, constraints, validity)
\]

Authorization succeeds only when the requested intent lies inside that scope. Authority does not transitively flow from a parent object unless the delegation relation explicitly says it does.

Thus:

```text
model output → no authority
planner output → no authority
generated code → no authority
hook output → no authority
workflow definition → no authority
```

Each may produce an intent that a separately authorized broker can admit and execute.

## Receipt calculus

A receipt is a causal binding, not an after-action note.

\[
R = H(S,O^\star,I,K,Executor,C,V,Runtime,Time,ReplayRefs)
\]

where \(H\) is a deterministic content-addressing function or equivalent stable identity construction.

Receipts compose into a DAG. A downstream receipt should reference the exact upstream receipts on which its standing depends.

## Chesterton fence

Before deleting a control, edge, role, compatibility path, or evidence requirement, establish the obligation it currently preserves. If the obligation is obsolete, remove it explicitly. If the obligation remains, replace the mechanism before removing the old one.

In DFCM terms, a fence is a constraint edge with unknown or partially known rationale. UNKNOWN does not grant deletion authority.

## Falsification

Every architectural claim should name an observation that would narrow or defeat it. Falsifiers are first-class because they prevent architecture from becoming self-confirming prose.

A pattern with no falsifier is guidance. A pattern with a falsifier, evidence contract, and operational boundary can participate in a release crown.

## The enterprise theorem

> Broad machine exploration is compatible with conservative enterprise consequence when reversible search, semantic manufacture, authority, actuation, verification, and evidence remain typed and non-transitive.

The rest of the book operationalizes that theorem.
