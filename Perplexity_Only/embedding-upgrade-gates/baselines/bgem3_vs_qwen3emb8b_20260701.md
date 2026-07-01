# Baseline: bge-m3 vs qwen3-embedding:8b (MRL-1024) — 2026-07-01

First candidate evaluated under the embedding-upgrade-gates methodology. Recorded so
the next candidate has a comparable prior, and so this verdict is auditable.

**FINAL VERDICT: KEEP INCUMBENT (bge-m3). Both promotion gates FAIL.**

## Setup (frozen)

- **Incumbent:** bge-m3, 1024-dim native, live index `data/embeddings.parquet`
  (snapshot `data/embeddings_bgem3.parquet`).
- **Candidate:** qwen3-embedding:8b, native 4096-dim, truncated to **1024-dim via
  MRL** through `/v1/embeddings` + `dimensions:1024`, L2-normalized. Candidate index
  `data/embeddings_qwen1024.parquet`, **10 862 rows**, built ~2 h 56 m, zero failures.
- **Query-side contract:** both query embeddings go through the same `/v1/embeddings`
  path the patched `kw_ask.py` uses, so the harness exercises the real contract.
- **top-k:** 6 (kw_ask default).
- **Probes:** 20 LOCKED probes (`probes_v1.txt`).
- **Gold set:** `gold/embed_gold_20probes_labeled_v1.csv` — 198 rows / 20 queries,
  **151 relevant / 47 not-relevant, 0 blanks**. Rubric: 1 = on-topic real content page;
  0 = scaffolding/definition page (`code-pre-00x`, `code-prescience-assessment`,
  `_prescient`, bare decade tags) OR off-topic. Aggressive 0-labeling concentrated on
  the two prescience probes (Q11 5/12, Q14 2/11) — the category-collapse guard. Labels
  are Pete's judgment call, reviewed and confirmed (incl. Q6 `linux-server`=1, Q14
  decade tags=0).

## Gate 0 — contract: PASS
Preflight probe on the Mac confirmed native=4096, `dimensions:1024`→1024. MRL works.

## Gate 1 — MTEB sniff: PASS (proceed)
Pete's table: bge-m3 63.2/~52.0-retr/~0.6 GB vs qwen3-emb-8b 70.6/57.8-retr/~5 GB.
Candidate plausibly stronger on retrieval — enough to justify the full eval.

## Gate 2 — side-path index: PASS
Both indexes load clean at dim=1024, 10 862 vecs each. No all-zero/NaN vectors.

## Gate 3 — agreement + gold-set A/B: **FAIL (both promotion gates)**

### Agreement (context/risk signal, NOT a gate)
**Mean Jaccard(top-6) = 0.237** → in the "<0.3, swap changes retrieval substantially,
do NOT promote without a gold-set eval" band. Baseline-to-beat for future candidates'
agreement runs.

### Quality vs gold set (20 labeled queries)

| Metric | Incumbent (bge-m3) | Candidate (qwen MRL-1024) |
|---|---:|---:|
| Recall@6 | 0.685 | 0.586 |
| MRR@6 (context only) | 0.912 | 0.875 |

### Promotion gate (LOCKED) — result

- **Gate A — aggregate Recall@6 margin:** delta = **−0.100**, hurdle = **+0.050** → **FAIL**
  (candidate is worse, not marginally better).
- **Gate B — per-query no-regression floor** (candidate may lose ≤1 relevant hit on any
  single query) → **FAIL**. Four regressions, two severe:
  | Probe | inc hits | cand hits | delta |
  |---|---:|---:|---:|
  | Q11 — short-horizon prescience verdicts, late-1990s | 5 | 0 | **−5** |
  | Q14 — studies scored high on 3-year prescience verdicts | 2 | 0 | −2 |
  | Q5 — shift to web-based enterprise software | 4 | 2 | −2 |
  | Q6 — vendors expected to lose share to open-source | 4 | 2 | −2 |

**Both gates must pass to promote. Gate A: FAIL, Gate B: FAIL → KEEP INCUMBENT
(status quo wins ties).**

### The category-collapse finding (the point of the gates)

Q11 and Q14 are exactly the qwen failure mode the per-query floor exists to catch. On
both prescience probes the candidate's top-6 collapsed to **scaffolding/definition
pages only** — matching on the tokens "prescient" / decade-number strings rather than
study content:

- Q11 cand top-6: `_prescient`, `2030s`, `code-pre-001`, `code-pre-002`, `1900s`,
  `code-pre-003` (Recall 0.0, hits 0/5). Incumbent returned dated study + quote pages
  (`1990s`, `quote-893`, `study-1991-apple-c-s-e9ffd7`, …), Recall 1.0.
- Q14 cand top-6: `2030s`, `code-pre-001`, `_prescient`, `code-pre-002`,
  `code-prescience-assessment`, `code-pre-003` (Recall 0.0, hits 0/2). Incumbent
  returned real dated study pages, Recall 1.0.

The candidate DID win some queries (NT-vs-Unix TCO +2, TCO debate +1, minicomputer +1,
data-warehousing +1, Microsoft +1, middleware +1) and posted higher top-1 similarity on
every probe — a similarity-magnitude signal, not a quality signal. Those wins are real
but the prescience regressions are disqualifying under the locked rule. **The gate did
its job: it blocked a swap that would have quietly gutted prescience retrieval.**

## Rollback (pre-written; unused — candidate NOT promoted)
```
cp data/embeddings_bgem3.parquet data/embeddings.parquet
# revert kw_ask.py / reembed.py / Phase 5 to bge-m3 versions
```
Not exercised: the live index `data/embeddings.parquet` was never touched. Candidate
index `data/embeddings_qwen1024.parquet` stays on disk as the recorded artifact.
