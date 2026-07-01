# Baseline: bge-m3 vs qwen3-embedding:8b (MRL-1024) — 2026-07-01

First candidate evaluated under this methodology. Recorded so the next candidate has a
comparable prior and so the verdict is auditable.

**VERDICT: KEEP INCUMBENT (bge-m3). Both promotion gates FAIL.**

## Setup

- **Incumbent:** bge-m3, 1024-dim native.
- **Candidate:** qwen3-embedding:8b, native 4096-dim, truncated to 1024-dim via
  Matryoshka (MRL) with L2 normalization. Both indexes: 10 862 vectors, dim 1024.
- **top-k:** 6 (the wiki Q&A default).
- **Probes:** 20 locked queries (`probes_v1.txt`).
- **Gold set:** `gold/embed_gold_20probes_labeled_v1.csv` — 198 rows / 20 queries,
  151 relevant / 47 not-relevant. A page is relevant (1) only if it is an on-topic real
  content page; scaffolding/definition pages and off-topic hits are 0.

## Result

| Metric | Incumbent (bge-m3) | Candidate (qwen MRL-1024) |
|---|---:|---:|
| Recall@6 | 0.685 | 0.586 |
| MRR@6 (context only) | 0.912 | 0.875 |
| Mean Jaccard(top-6), context | 0.237 | — |

### Promotion gate (locked)

- **Gate A — aggregate Recall@6 margin:** delta = −0.100 vs a +0.050 hurdle → **FAIL**.
  The candidate is worse in aggregate, not marginally better.
- **Gate B — per-query no-regression floor** (candidate may lose at most one relevant
  hit on any single query) → **FAIL**. Four regressions:
  | Probe | inc hits | cand hits | delta |
  |---|---:|---:|---:|
  | short-horizon prescience verdicts, late-1990s | 5 | 0 | −5 |
  | studies scored high on 3-year prescience verdicts | 2 | 0 | −2 |
  | shift to web-based enterprise software | 4 | 2 | −2 |
  | vendors expected to lose share to open-source | 4 | 2 | −2 |

Both gates must pass to promote. Both failed → keep the incumbent (status quo wins ties).

## What the gate caught

The two prescience probes are the failure mode the per-query floor exists to catch. On
both, the candidate's top-6 collapsed to scaffolding/definition pages (matching on the
token "prescient" and on decade-number strings) rather than the dated study and quote
pages the incumbent surfaced. The candidate did win a handful of other queries and
posted higher raw top-1 similarity across the board — a similarity-magnitude signal, not
a quality signal — but the prescience regressions are disqualifying under the locked
rule. The methodology worked as designed: it blocked a swap that would have quietly
degraded a category the corpus depends on.
