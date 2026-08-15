# The Gym Maturity Matrix

The repository's canonical maturity model scores a gym independently on **five capability planes** and **seven cumulative levels**. Overall maturity is the minimum of the five plane scores.

| Capability plane | M0 Seed | M1 Modeled | M2 Admitted | M3 Runnable | M4 Receipted | M5 Replayable | M6 Enterprise |
|---|---|---|---|---|---|---|---|
| Semantics and world model | idea only | explicit vocabulary | machine-readable schema and validity rules | validated scenarios and state transitions | versioned provenance | mappings across scenario families | governed federated canonical graph |
| Tasks and evaluation | manual examples | documented task families | deterministic task contract, metrics and seeds | executable benchmark for the exact selected subject | broad regression and failure suites | adaptive curricula and comparative evaluation | continuous multi-policy evaluation with calibrated regression |
| Runtime and boundaries | no runtime | mock or demo | offline sandbox and typed accept/reject outcomes | exact-subject offline simulation observed end to end | bounded state transitions coupled to evidence | isolated roles and deterministic reset | federated governed runtime with explicit boundaries |
| Evidence and replay | narrative claims | logs | structured observations and identities | machine verifier emits scoped standing | deterministic receipt binds subject, inputs, outcome and verifier | replay equivalence and receipt graph | signed evidence graph with audit and independent replay |
| Operations and ecosystem | ad hoc | documented setup | pinned dependencies and deterministic bootstrap | automated local validation gate | CI retains artifacts and regression evidence | release, compatibility, security and performance gates | SLOs, governance, interoperability and certification mapping |

## Why five planes

A single maturity number is useful only if it is difficult to game.

A gym with an excellent runtime but no semantic contract cannot support reliable planner composition. A gym with beautiful schemas but no observed execution is not runnable. A gym with receipts but no replay criteria has evidence without reproducibility. A gym with all of those but no operational lifecycle cannot make an enterprise claim.

Therefore the overall maturity is:

\[
M_{\text{overall}} = \min(M_{\text{semantics}}, M_{\text{tasks}}, M_{\text{runtime}}, M_{\text{evidence}}, M_{\text{operations}})
\]

This is [Minimum Plane Governs](patterns/enterprise-operations.md).

## Promotion rules

- A plane earns a level only when all lower levels are also satisfied.
- Missing evidence does not count as admission.
- Documentation is inspection, not observed execution.
- M4 requires deterministic evidence binding subject, inputs, outcome, and verifier.
- M5 requires explicit equivalence criteria and a reproducible evidence path.
- M6 requires governance, interoperability, operational evidence, security, and lifecycle controls.

For a new gym, establish an honest **M2 floor on all five planes** before optimizing for a high score on any one plane. Then advance runtime and evidence together; runnable-but-unreceipted systems accumulate technical debt precisely at the consequence boundary.
