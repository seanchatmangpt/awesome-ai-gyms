# Contributing

Awesome AI Gyms is a discovery registry, not an execution authority.

## Admission law

A new record may enter the catalog when it has a canonical public reference and provenance. Catalog membership means **candidate only**.

Do not infer any of the following from a README, paper, package import, CI badge, star count, or upstream benchmark claim:

- runtime compatibility,
- planner compatibility,
- safe materialization,
- authority,
- successful execution,
- `ALIVE` standing.

`ALIVE` requires observed execution against the exact admitted subject and a receipt reference. If evidence is missing, use `UNKNOWN`.

## Preferred changes

1. Add or update factual metadata in `registry/gyms.tsv`.
2. Preserve every upstream source in `provenance`.
3. Keep descriptions out of the canonical registry unless independently authored and necessary.
4. Run `python scripts/render_readme.py`.
5. Run `python scripts/validate_registry.py`.
6. Run `python -m unittest discover -s tests -v`.

The generated README must not be hand-edited. Product-specific projections belong in the owning product adapters, not in this registry.

## DFCM

Preserve reversible lawful possibilities before selection. A failed compatibility edge should narrow the graph; it should not erase unrelated candidates. Awesome AI Gyms discovers, AutoFDE-Lab selects/plans, and GymAct owns admission and execution.
