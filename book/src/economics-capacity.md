# Economics, Capacity, and Attention

DFCM treats cost as a first-class admission boundary because autonomous systems can consume money, compute, API quota, storage, time, and human attention without ever crossing an obvious business transaction boundary. The objective is not minimum cost. It is **maximum verified consequence per bounded resource while preserving evidence and authority**.

## Resource vector

Represent resource consumption as a vector rather than one dollar amount:

\[
B = (money, compute, tokens, wallTime, storage, apiQuota, humanAttention)
\]

Different stages consume different resources. Discovery may be token-heavy but consequence-free. Verification may be compute-heavy. Human exception review may dominate calendar time. A low-dollar system can still be operationally expensive if it creates an unbounded review queue.

Budgets belong in admission and receipts. They should not exist only in monthly cloud-finance reports.

## Cost of reversibility

Reversible exploration is not free, but it is usually cheaper than irreversible correction. DFCM intentionally spends some resource before selection to preserve options and gather evidence.

The relevant comparison is:

\[
ExpectedCost = ExploreCost + SelectedExecutionCost + ExpectedFailureCost
\]

Premature selection can reduce ExploreCost while increasing failure, lock-in, rework, and incident cost. Combinatorial maximalism therefore preserves alternatives only while the information value exceeds the bounded exploration cost.

## Verified consequence as denominator

Raw task throughput is a weak economic metric. A model can emit many answers or tool calls without closing business consequences.

Prefer measures such as:

```text
cost / independently verified consequence
human minutes / ALIVE capability
compute / closed release-crown node
failed attempts / successful receipted consequence
replay cost / historical claim
```

These metrics discourage cheap but unverifiable automation.

## Little’s Law

For a stable flow:

\[
L = \lambda W
\]

Increasing local generation speed while leaving admission, authority, verification, or human review unchanged raises WIP. The enterprise then experiences more open intents, more stale artifacts, and longer time to standing even though “AI throughput” appears higher.

DFCM therefore applies WIP limits at causal boundaries. The system should not manufacture unlimited work merely because proposal generation is cheap.

## Human attention is scarce capacity

Human approval is frequently modeled as an infinite safety resource. It is not. It is a queue with service time, expertise requirements, fatigue, and opportunity cost.

For every human review edge define:

- arrival rate,
- expected review time,
- required expertise,
- information available to the reviewer,
- decision authority,
- escalation behavior,
- timeout semantics,
- evidence produced.

A review step that adds waiting but no unique evidence or authority is a candidate for elimination after its obligation is understood.

## Cost-aware planner league

Different planners and formulations can have radically different cost profiles. Selection policy should consider expected verified outcome, latency, cost, reliability, and evidence quality—not benchmark score alone.

A cheap deterministic solver may dominate a language model for a constrained scheduling subproblem. A higher-cost planner may be justified for rare, high-value ambiguity. The capability seam allows the enterprise to choose per context without rewriting the operating contract.

## Portfolio WIP

Portfolio governance should limit simultaneous initiatives that have not closed their evidence boundaries. Starting more pilots can reduce learning if each competes for the same security review, data access, verifier development, or production authority.

A useful portfolio view groups WIP into:

- discovered but unmodeled capabilities,
- modeled but not admitted,
- admitted but not constructed,
- constructed but not executed,
- executed but not verified,
- verified but not replayable,
- release-ready but not crowned.

The longest queue identifies the real organizational constraint.

## Resource evidence

Receipts should record resource dimensions material to the claim. Depending on domain that can include compute class, API usage, token count, wall-clock duration, monetary spend, storage, network transfer, retries, and human decision time.

This enables evidence-based optimization across versions and providers while preserving exact-subject identity.

## Denial of wallet

A compromised or merely pathological planner can generate an enormous lawful search space. Resource fences prevent that search from becoming an economic incident.

Controls include maximum candidate count, branch depth, parallelism, per-subject spend, global spend, provider rate, retry count, wall-clock deadline, and human-review budget. Exceeding the budget yields a typed refusal or BLOCKED state rather than hidden overrun.

## Investment decisions

A capability investment should answer:

1. What business consequence closes value?
2. What evidence proves that consequence?
3. What is the current end-to-end cost including human attention?
4. Which causal boundary is the bottleneck?
5. Which reversible alternatives remain?
6. What failure costs are reduced by stronger identity, authority, or replay?
7. What supplier concentration or exit cost is embedded?

This converts “AI ROI” from a model-cost conversation into a systems-flow conversation.

## Economic crown

The economic model is closed when resource budgets are admitted before expensive work, actual consumption is receipted, WIP is observable at causal boundaries, and optimization is based on verified consequences rather than proposal volume.

The falsifier is an autonomous path that can consume unbounded spend or human attention while remaining semantically “successful,” or a portfolio metric that rewards generated activity without evidence of closed consequence.
