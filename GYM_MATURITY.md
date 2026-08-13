# Canonical Gym Maturity Matrix (5x7)

A gym is scored independently on five capability planes and seven cumulative levels. Overall maturity is the minimum of the five plane scores.

| Capability plane | M0 Seed | M1 Modeled | M2 Admitted | M3 Runnable | M4 Receipted | M5 Replayable | M6 Enterprise |
|---|---|---|---|---|---|---|---|
| Semantics and world model | idea only | explicit vocabulary | machine-readable schema and validity rules | validated scenarios and state transitions | versioned provenance | mappings across scenario families | governed federated canonical graph |
| Tasks and evaluation | manual examples | documented task families | deterministic task contract, metrics and seeds | executable benchmark for the exact selected subject | broad regression and failure suites | adaptive curricula and comparative evaluation | continuous multi-policy evaluation with calibrated regression |
| Runtime and boundaries | no runtime | mock or demo | offline sandbox and typed accept/reject outcomes | exact-subject offline simulation observed end to end | bounded state transitions coupled to evidence | isolated roles and deterministic reset | federated governed runtime with explicit boundaries |
| Evidence and replay | narrative claims | logs | structured observations and identities | machine verifier emits scoped standing | deterministic receipt binds subject, inputs, outcome and verifier | replay equivalence and receipt graph | signed evidence graph with audit and independent replay |
| Operations and ecosystem | ad hoc | documented setup | pinned dependencies and deterministic bootstrap | automated local validation gate | CI retains artifacts and regression evidence | release, compatibility, security and performance gates | SLOs, governance, interoperability and certification mapping |

## Standing rules

- A plane earns a level only when its lower levels are also satisfied.
- Overall maturity is the minimum plane score.
- Missing evidence does not count as admission.
- Documentation is inspection, not observed execution.
- M4 requires deterministic evidence that binds subject, inputs, outcome and verifier.
- M5 requires equivalence criteria and a reproducible evidence path.
- M6 requires governance, interoperability, operational evidence, security and lifecycle controls.

New gyms should first establish an honest M2 floor on all five planes, then advance Runtime and Evidence through deterministic offline evaluation.
