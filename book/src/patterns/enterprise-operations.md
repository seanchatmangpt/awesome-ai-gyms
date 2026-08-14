# Enterprise and Operations

How gyms advance from experimental worlds to governed enterprise capability.

## 49. Five-by-Seven Maturity ★★★

**Context.** A gym needs a roadmap from idea to enterprise-grade operation.

**Problem.** One-dimensional maturity labels let strong documentation or runtime polish hide missing evidence, semantics, or operations.

**Forces.**

- Different teams advance different capabilities first.
- Executives need a compact view.
- Maturity must remain cumulative.

**Therefore:** **Score the gym independently across five planes—semantics/world model, tasks/evaluation, runtime/boundaries, evidence/replay, operations/ecosystem—over seven cumulative levels M0 through M6.**

**Consequences.** Progress becomes multidimensional and hard gaps remain visible.

**Falsifier.** A gym is called enterprise-ready without separately assessing all five planes.

**Evidence.**

- [ ] plane scores
- [ ] evidence for each level
- [ ] cumulative lower-level checks
- [ ] dated assessment

**Connects to.** Minimum Plane Governs, Capability Certification, Release Crown.

---

## 50. Minimum Plane Governs ★★★

**Context.** A gym has uneven maturity across its five capability planes.

**Problem.** Averaging maturity rewards overinvestment in visible strengths while critical weak planes remain below the system's claimed level.

**Forces.**

- Teams prefer composite scores.
- The weakest plane often controls real risk.
- Some experiments intentionally tolerate low maturity.

**Therefore:** **Define overall maturity as the minimum of the five plane scores. Advance the overall label only when every plane satisfies the cumulative requirements.**

**Consequences.** The maturity label becomes a defensible floor rather than an average aspiration.

**Falsifier.** An M6 label is possible while any plane remains at M2 or M3.

**Evidence.**

- [ ] five plane scores
- [ ] minimum calculation
- [ ] evidence per plane
- [ ] promotion receipt/review

**Connects to.** Five-by-Seven Maturity, Release Crown, Standing Ladder.

---

## 51. Exact Runtime Pin ★★★

**Context.** A gym depends on compilers, containers, models, packages, system libraries, or remote providers.

**Problem.** Mutable toolchains create replays that appear identical at the source level but execute different machinery.

**Forces.**

- Security updates require movement.
- Fully hermetic environments are costly.
- Hosted services may not expose immutable identities.

**Therefore:** **Pin every runtime dependency that materially affects behavior to an exact version or digest; record unavoidable remote uncertainty as an external dependency rather than pretending it is pinned.**

**Consequences.** Local Capsule ALIVE evidence can be reused when identities actually match.

**Falsifier.** A replay or release claim depends on 'latest', floating branches, or unrecorded hosted model revisions.

**Evidence.**

- [ ] toolchain manifest
- [ ] digests/versions
- [ ] external dependency declarations
- [ ] runtime identity in receipt

**Connects to.** Canonical Subject, Replay, Capability Certification.

---

## 52. Capability Certification ★★☆

**Context.** A gym or provider needs to advertise which capabilities have actually been demonstrated.

**Problem.** Feature lists mix declared, implemented, runnable, and verified states.

**Forces.**

- Certification can become bureaucracy.
- Capabilities vary by mode and environment.
- Evidence expires as versions move.

**Therefore:** **Publish a machine-readable capability matrix whose cells bind exact subject + mode + environment + standing + receipt. Treat unsupported and untested cells explicitly.**

**Consequences.** Consumers can select providers from evidence rather than marketing claims.

**Falsifier.** A capability is advertised as supported without a scoped execution receipt or explicit UNKNOWN/UNSUPPORTED status.

**Evidence.**

- [ ] capability IDs
- [ ] subject/mode/environment
- [ ] standing
- [ ] receipt
- [ ] validity/supersession

**Connects to.** Standing Ladder, Cross-World Comparison, Marketplace Qualification.

---

## 53. Cost-Time-Attention Budget ★★☆

**Context.** Autonomous planning and gym execution can explore very large spaces.

**Problem.** Optimization for success alone can consume unbounded money, wall-clock time, tokens, compute, or human review.

**Forces.**

- Cheap exploration is valuable.
- Budgets differ by phase.
- Evidence quality must not be sacrificed merely to be fast.

**Therefore:** **Make cost, wall-clock, compute, token, and human-attention budgets explicit admission constraints and receipt dimensions. Optimize verified consequences per bounded resource.**

**Consequences.** Autonomy scales without hidden resource debt.

**Falsifier.** A planner or gym can exceed agreed resource limits without refusal or evidence that the limit changed.

**Evidence.**

- [ ] budget envelope
- [ ] resource counters
- [ ] admission/refusal behavior
- [ ] receipt metrics

**Connects to.** Constraint Fence, Combinatorial Maximalism, Autonomic Curriculum.

---

## 54. Governance Graph ★★☆

**Context.** Enterprise gyms involve owners, policies, data classifications, jurisdictions, approvals, and release rules.

**Problem.** Governance embedded in prose or CI conditionals becomes invisible to planners and impossible to compose formally.

**Forces.**

- Policies change over time.
- Legal and organizational rules overlap.
- Not every governance rule is executable.

**Therefore:** **Represent governance relationships, authorities, obligations, prohibitions, ownership, and evidence requirements in a versioned graph linked to the same subjects and capabilities used by execution.**

**Consequences.** Planning can reason about governance before proposing impossible actions.

**Falsifier.** A release-critical policy exists only in undocumented human knowledge or an opaque pipeline branch.

**Evidence.**

- [ ] policy identities
- [ ] subjects and authorities
- [ ] effective versions
- [ ] admission mappings
- [ ] audit references

**Connects to.** Authority Boundary, Release Crown, Federated Gym Graph.

---

## 55. Release Crown ★★★

**Context.** Many lower-level verifiers must compose into a release decision.

**Problem.** Green unit tests or one successful scenario are routinely overpromoted into claims about the whole system.

**Forces.**

- Release evidence spans repositories and runtimes.
- Some checks are reusable.
- The crown must fail closed on missing required evidence.

**Therefore:** **Define a named release-crown DAG of required capabilities and receipts. The crown is ALIVE only when every required node resolves to valid scoped evidence for the exact release identities.**

**Consequences.** Release status becomes a proof composition problem rather than a dashboard impression.

**Falsifier.** A required capability is missing or stale but the release still reports complete standing.

**Evidence.**

- [ ] release identity
- [ ] required capability DAG
- [ ] receipt references
- [ ] falsifiers
- [ ] final crown receipt

**Connects to.** Receipt DAG, Minimum Plane Governs, Federated Gym Graph.

---

## 56. Federated Gym Graph ★☆☆

**Context.** An enterprise operates many gyms, providers, planners, datasets, and release processes.

**Problem.** A central monolith cannot own every domain, while isolated registries prevent cross-domain planning and evidence reuse.

**Forces.**

- Domains need autonomy.
- Canonical identity must cross boundaries.
- Trust and authority are not uniform.

**Therefore:** **Federate gym graphs through stable public semantics, signed or otherwise attributable evidence, explicit trust boundaries, and local authority. Share claims and receipts without exporting ambient execution rights.**

**Consequences.** The ecosystem can reason globally while actuating locally.

**Falsifier.** Federation requires one system to inherit another system's execution authority merely to consume its evidence.

**Evidence.**

- [ ] federated identifiers
- [ ] trust relationships
- [ ] evidence exchange
- [ ] local authority checks
- [ ] mapping provenance

**Connects to.** Governance Graph, Release Crown, Gym of Gyms.

---
