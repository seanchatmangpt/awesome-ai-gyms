# Manufacture and Packs

How ontology, ggen-create, ggen packs, marketplaces, and project gyms form a manufacturing lifecycle.

## 25. Ontology First ★★★

**Context.** A project or pack has semantics that will be projected into code, configuration, tests, documentation, planning models, or gym scenarios.

**Problem.** When those artifacts are authored independently, their definitions diverge and every change requires synchronized manual editing.

**Forces.**

- Ontologies require discipline.
- Not every implementation detail belongs in semantics.
- Generated projections must remain understandable.

**Therefore:** **Author the stable domain relationships, constraints, identities, and capability contracts in a canonical graph first. Manufacture downstream artifacts as deterministic projections wherever practical.**

**Consequences.** Semantic change becomes one graph change followed by regeneration instead of a documentation/API synchronization campaign.

**Falsifier.** Two canonical artifacts disagree because their shared semantics were manually duplicated rather than projected from one admitted source.

**Evidence.**

- [ ] canonical graph
- [ ] validation shapes
- [ ] projection ownership
- [ ] generated artifact provenance

**Connects to.** Deterministic Projection, Generated Is Canonical, Planning Projection.

---

## 26. One Pack, One Manufacturing Boundary ★★★

**Context.** ggen needs reusable knowledge for manufacturing a coherent architecture or product capability.

**Problem.** Tiny packs create dependency explosion; giant packs hide unrelated authority and make reuse impossible.

**Forces.**

- Reusable boundaries are larger than code snippets.
- Projects need local specialization.
- Pack composition must remain understandable.

**Therefore:** **Define a pack around one cohesive, independently meaningful manufacturing boundary: ontology, admission rules, deterministic selection, templates/projections, fixtures, and qualification evidence. Depend on other packs for truly independent boundaries.**

**Consequences.** Pack graphs remain composable without degenerating into either monoliths or feature confetti.

**Falsifier.** A pack cannot explain its reusable semantic boundary without listing one specific consumer project or dozens of unrelated capabilities.

**Evidence.**

- [ ] pack ontology
- [ ] declared dependencies
- [ ] owned projections
- [ ] qualification gym
- [ ] versioned evidence

**Connects to.** Local Bridge, Pack Gym, Marketplace Qualification.

---

## 27. ggen-create Discovers Pack Law ★★☆

**Context.** A mature exemplar or external architecture exists and its reusable manufacturing law is not yet encoded as a ggen pack.

**Problem.** Manual template authoring captures surface files but misses the deeper variables, invariants, and semantic relationships that make the exemplar reusable.

**Forces.**

- Exemplars contain accidental details.
- Several examples reveal variation better than one.
- Reverse engineering must not silently grant execution authority.

**Therefore:** **Use ggen-create as the pack-authoring and reverse-compilation process: ingest exemplars, identify variables and invariants, derive candidate ontology/projections, and emit a candidate pack for qualification. It does not generate consumer projects.**

**Consequences.** Existing systems become raw material for reusable manufacturing knowledge while preserving the separation between pack creation and ggen execution.

**Falsifier.** The ggen-create output is treated as a finished consumer application or bypasses pack qualification.

**Evidence.**

- [ ] exemplar identities
- [ ] derived variables/invariants
- [ ] candidate pack
- [ ] qualification obligations

**Connects to.** One Pack, One Manufacturing Boundary, Pack Gym, Marketplace Qualification.

---

## 28. Pack Gym ★★★

**Context.** A ggen pack claims it can manufacture a reusable capability.

**Problem.** Template unit tests do not prove that the complete pack can manufacture, build, run, and reproduce a real consumer.

**Forces.**

- Pack qualification should be cheap enough for every release.
- Some consumers need local bridges.
- Generation success is weaker than behavior success.

**Therefore:** **Place a gym with the pack that starts from controlled consumer worlds, runs the real ggen path, and verifies the manufactured capability through behavioral scenarios.**

**Consequences.** The pack becomes an executable manufacturing contract rather than a bag of templates.

**Falsifier.** A pack can be published as qualified even though no gym has manufactured and exercised an exact consumer instance.

**Evidence.**

- [ ] empty/minimal consumer world
- [ ] generation receipt
- [ ] consumer verifier
- [ ] repeat-sync or regeneration check

**Connects to.** Marketplace Qualification, Project Gym, Empty Repo Crown.

---

## 29. Marketplace Qualification ★★★

**Context.** Reusable packs must be distributed across projects.

**Problem.** A package registry can easily become an app store where publication is mistaken for behavioral trust.

**Forces.**

- Fast publishing encourages experimentation.
- Consumers need provenance and dependency closure.
- Qualification evidence can expire as dependencies move.

**Therefore:** **Treat the marketplace as a governed supply plane: publish pack identity, dependencies, provenance, compatibility claims, and qualification receipts. Installation grants no execution authority.**

**Consequences.** Consumers can resolve trusted manufacturing inputs without collapsing distribution and execution.

**Falsifier.** A published or downloaded pack is automatically considered ALIVE in the consuming environment.

**Evidence.**

- [ ] pack digest/version
- [ ] dependency lock
- [ ] qualification state
- [ ] receipt references
- [ ] revocation/supersession metadata

**Connects to.** Pack Gym, Candidate Is Not Capability, Exact Runtime Pin.

---

## 30. Deterministic Projection ★★★

**Context.** Canonical semantics must become files, models, tests, configs, or documentation.

**Problem.** Probabilistic generation in the canonical path makes drift detection and replay ambiguous.

**Forces.**

- LLMs are useful at novelty boundaries.
- Canonical builds need reproducibility.
- Template engines can still hide nondeterministic ordering.

**Therefore:** **Make canonical projection a deterministic function of admitted graph, pack version, template/projection version, and declared environment. Use probabilistic systems only to propose candidate semantic changes upstream.**

**Consequences.** Regeneration becomes a verifier: unchanged inputs should produce unchanged outputs.

**Falsifier.** Two runs with identical admitted inputs and toolchain identities produce different canonical artifacts without a declared nondeterministic field.

**Evidence.**

- [ ] input graph digest
- [ ] pack/toolchain versions
- [ ] output digest
- [ ] sync-twice equality

**Connects to.** Ontology First, Generated Is Canonical, Delete and Regenerate.

---

## 31. Generated Is Canonical ★★★

**Context.** A deterministic manufacturer writes source, config, tests, or docs into a consumer project.

**Problem.** Separating generated output into a second-class directory encourages manual shadows, wrapper layers, and confusion about which artifact is authoritative.

**Forces.**

- Developers are used to 'do not edit generated' trees.
- Some artifacts are genuinely transient.
- Canonical ownership must be explicit.

**Therefore:** **Where ggen owns an artifact, write it directly to its canonical project location and make ownership/provenance machine-visible. Regeneration, not a parallel handwritten copy, repairs drift.**

**Consequences.** Generated source participates in normal builds and interfaces without architectural stigma.

**Falsifier.** The project maintains a handwritten canonical file plus a generated near-duplicate because generated artifacts are not trusted as first-class outputs.

**Evidence.**

- [ ] artifact owner
- [ ] projection provenance
- [ ] drift detector
- [ ] regeneration path

**Connects to.** Deterministic Projection, Ontology First, Project Gym.

---

## 32. Project Gym ★★★

**Context.** A manufactured or manually integrated project needs to demonstrate its own behavior.

**Problem.** Examples, playgrounds, smoke tests, integration tests, and demos often scatter the most important executable knowledge across unrelated directories.

**Forces.**

- Unit tests are narrower than capability proof.
- Examples are readable but frequently stale.
- A project needs one place to answer 'what can this actually do?'

**Therefore:** **Give each executable project a `gym/` proof surface containing bounded worlds, scenarios, fixtures, assertions, and receipt references. Run it through GymAct or the project's admitted gym runner.**

**Consequences.** Examples and playground behavior gain executable standing and can be used as acceptance surfaces.

**Falsifier.** The only proof of a major capability is an unexecuted example, README snippet, or bespoke CI workflow outside the project gym.

**Evidence.**

- [ ] gym manifest
- [ ] worlds
- [ ] scenarios
- [ ] assertions/verifiers
- [ ] receipt locations

**Connects to.** Pack Gym, Gym in Every Project, Independent Postcondition.

---
