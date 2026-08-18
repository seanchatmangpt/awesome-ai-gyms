# V · Execution and Safety { #family-execution-safety }

How a system crosses the consequence boundary without ambient execution authority.

DFCM is intentionally maximal before DO and conservative at DO. This family defines the single consequence path, refusal semantics, reset boundary, and independent postcondition needed to keep exploration powerful without expanding ambient authority.

## Pattern map

33. [P33 · BRCE Is the Only DO](execution-safety/33-brce-is-the-only-do.md)
34. [P34 · Zero Unreceipted Actuation](execution-safety/34-zero-unreceipted-actuation.md)
35. [P35 · Tool Call Is Intent](execution-safety/35-tool-call-is-intent.md)
36. [P36 · Sandbox Boundary](execution-safety/36-sandbox-boundary.md)
37. [P37 · Idempotent Reset](execution-safety/37-idempotent-reset.md)
38. [P38 · Typed Refusal](execution-safety/38-typed-refusal.md)
39. [P39 · Failure Is Topology](execution-safety/39-failure-is-topology.md)
40. [P40 · Independent Postcondition](execution-safety/40-independent-postcondition.md)

## DFCM composition rule

Hooks, tools, models, planners, and generated artifacts may manufacture intents. Only the admitted consequence broker may DO, and every attempted consequence must terminate in evidence.
