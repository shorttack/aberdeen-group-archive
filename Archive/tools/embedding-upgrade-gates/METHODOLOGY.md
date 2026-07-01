# Embedding-Model Upgrade Gates — Methodology

**Lane:** embedding models only (the retrieval embedder behind `kw_ask`, currently
bge-m3 → candidate). This is deliberately SEPARATE from the *generative* LLM upgrade
process, which governs the model that writes answers and follows a different
cost/quality calculus. This document covers only the embedder that decides *what gets
retrieved*.

**Core bias: status quo wins ties.** Every gate is biased toward "keep the incumbent
embedder". A candidate must earn its way through all gates in order. Failing any one
stops the process.

Why the bias: the cost asymmetry is real and worse for embeddings than for the
generative model.
- Cost of skipping an embedding upgrade we should have made: slightly weaker `kw_ask`
  retrieval, easily revisited next month.
- Cost of promoting an embedding upgrade we shouldn't have: a full re-embed of the
  entire corpus (~10,900 pages, ~3 h wall-clock on a mid-range Apple-Silicon machine),
  plus every downstream
  `kw_ask` answer silently shifts, plus a rollback re-embed to undo it. The blast
  radius is the whole retrieval surface, not one Phase-3 run.

---

## What makes the embedding lane different from the generative-model lane

1. **The dimension contract is a hard blocker, not a quality question.** The live
   index, the query-time embed call, and every stored vector must agree on
   dimensionality. bge-m3 is 1024-dim. Any candidate must land at 1024-dim too —
   either natively or via Matryoshka (MRL) truncation — or the whole schema breaks.
   qwen3-embedding:8b is natively 4096-dim; we use MRL-1024 truncation to preserve
   the bge-m3 schema. **Gate 0 verifies this before anything else.**

2. **There is no "thinking mode" to worry about**, but there IS a
   normalization + endpoint trap: Ollama's `/api/embeddings` ignores the
   `dimensions` parameter; only `/v1/embeddings` (OpenAI-compat) honors MRL
   truncation. And truncated MRL vectors must be L2-normalized before cosine.
   Both are documented below and re-checked in Gate 0.

3. **Quality can't be read off a public benchmark alone.** MTEB retrieval scores
   tell you the candidate is plausibly better *in general*, but they say nothing
   about THIS corpus (1970s–2000s IT-analyst prose, heavy on entity/tech tag stubs
   and short quote pages). The only trustworthy signal is a human-judged gold set
   over real archive probe queries. That's Gate 3.

---

## The Gates (sequential — each is a STOP point)

### Gate 0 — Contract + gotchas (cost: ~5 min)

1. Review the known embedding-backend landmines before touching a candidate. The
   load-bearing one for Ollama: the native `/api/embeddings` endpoint silently
   ignores the `dimensions` parameter, so MRL truncation appears to "work" but
   returns native-dim vectors. Use the OpenAI-compatible `/v1/embeddings` endpoint
   with `dimensions: N`, and L2-normalize truncated vectors before cosine similarity.
   (If you keep an append-only landmine ledger for your setup, read it here.)
2. **Preflight dimension probe on real hardware:** embed one short string via
   `/v1/embeddings` with `dimensions: 1024` and confirm the returned vector length
   is exactly 1024. Also confirm the native length (no `dimensions` param) so we know
   the MRL headroom. This is a 2-request probe, not a corpus run.

**Stop-conditions (any one aborts):**
- Candidate can't produce 1024-dim vectors (no native match, no working MRL). Hard stop.
- A gotcha entry says "do not use this embedder for <workload>". Respect it.

**Verified for qwen3-embedding:8b (2026-07-01):** native = 4096, `/v1/embeddings` +
`dimensions:1024` → 1024. MRL truncation confirmed working on the target Ollama
build. PASS.

### Gate 1 — Public benchmark sniff (cost: ~5 min, 1–2 fetches)

Read one or two credible MTEB / retrieval comparisons of incumbent vs candidate.
This is a *sniff test*, not a promotion signal — it only tells us whether the
candidate is worth the cost of building a candidate index at all.

- MTEB retrieval subscore is the relevant column (not overall average).
- Storage / latency deltas are context, never gates ("Latency is not a concern.
  Quality is a concern.").

**Recorded for this evaluation (MTEB table, 2026-06-30):**
bge-m3 = 63.2 overall / ~52.0 retrieval / ~0.6 GB;
qwen3-embedding:8b = 70.6 overall / 57.8 retrieval / ~5 GB.
Candidate is plausibly stronger on retrieval → proceed to Gate 2.

**Stop-condition:** candidate is *worse* on MTEB retrieval than incumbent → stop;
not worth a candidate-index build.

### Gate 2 — Build candidate index on a SIDE PATH (cost: ~3 h wall-clock, 1 re-embed)

Build the candidate index to a **separate parquet** — never overwrite the live
`data/embeddings.parquet`. Snapshot the incumbent first.

- Live incumbent: `data/embeddings.parquet` (bge-m3) — UNTOUCHED during evaluation.
- Incumbent snapshot: `data/embeddings_bgem3.parquet`.
- Candidate: `data/embeddings_qwen1024.parquet`.

Use the corpus embedding builder with the candidate model and
`--dimensions 1024 --out data/embeddings_candidate.parquet`. The schema (6-col:
`page_path,page_type,slug,title,vector,dim`) MUST match the incumbent so both load
under the identical harness.

**Stop-condition:** the candidate index fails to load at the expected dim, or has
all-zero / NaN vectors → the contract is broken; fix before any eval.

**Done for this evaluation (2026-07-01):** candidate index built, 10 862 rows,
~2 h 56 m, zero failures. Both indexes load clean at dim=1024. PASS.

### Gate 3 — Gold-set quality with the LOCKED two-part gate (cost: labeling time)

This is the ONLY gate that yields a promotion verdict.

1. **Agreement A/B (context, not a gate):** run `embed_ab_harness_v2.py` on the
   LOCKED probe set (`probes_v1.txt`, 20 queries) with no `--gold`. It reports
   mean Jaccard(top-6) between the two indexes. High agreement = low-risk swap;
   low agreement = the swap materially changes what `kw_ask` sees, so a gold set
   is REQUIRED before promoting.
2. **Emit the gold template:** `--emit-gold-template gold.csv` writes one row per
   (query, slug) for the UNION of both models' top-6 hits, with a blank `relevant`
   column. Union (not incumbent-only) so a slug only the candidate surfaces is still
   offered for labeling — otherwise recall is biased toward the incumbent's picks.
3. **A human labels** the `relevant` column 1/0 by hand — this is the irreducible
   judgment step; no automated proxy substitutes for it.
4. **Rerun with `--gold gold.csv`** for the verdict.

#### The LOCKED promotion gate (established 2026-07-01)

The candidate PROMOTES only if **both** gates pass:

- **Gate A — aggregate Recall@6 margin.** Candidate mean Recall@6 must beat
  incumbent by **≥ +0.05**. A win inside the noise band (< 0.05) is a tie, and
  status quo wins ties.
- **Gate B — per-query no-regression floor.** On **no single labeled query** may
  the candidate lose more than **1** relevant hit vs the incumbent. This guards
  signature query *types* (e.g. prescience/horizon queries) from category collapse
  even when the aggregate looks like a win.

**MRR@6 and mean-Jaccard are reported as CONTEXT ONLY. They are never gates.**

Rationale for the two-part shape (why not a single aggregate number):
`kw_ask` consumes the top-k as a *bundle* fed to the generative model. A candidate
that wins on average but tanks one query type would silently degrade that whole
class of answers. The A/B agreement run for this candidate already flagged exactly
this failure mode — the short-horizon-prescience probe drifted to scaffolding
pages (`_prescient`, `2030s`, `code-pre-00x`) instead of study pages. Gate B exists
to catch that pattern with human labels behind it, not just Jaccard.

Why Recall@6 (not Recall@10, not nDCG): k=6 is the `kw_ask` default top-k, so the
metric measures exactly the slice the generative model actually sees. nDCG rewards
ranking finesse that doesn't change which 6 pages get fed in; recall of the right
pages into the top-6 is what matters here.

**Stop-condition:** either gate fails → KEEP INCUMBENT. Archive the candidate index
+ the gold-labeled report for the next candidate's baseline; do NOT promote.

### Gate 4 — Promote + rollback plan (only if Gate 3 PASSES both parts)

Promotion = point the live pipeline at the candidate:
1. `data/embeddings_qwen1024.parquet` → `data/embeddings.parquet` (the live index).
2. Query side already patched (`kw_ask_v7_1_qwen3emb.py`, `reembed_v1_1_qwen3emb.py`)
   — cut them over.
3. Phase 5 canonical → v4.

**One-line rollback (write it down BEFORE promoting):**
```
cp data/embeddings_bgem3.parquet data/embeddings.parquet   # revert live index
# + revert kw_ask.py / reembed.py / Phase 5 to their bge-m3 versions
```
If the rollback isn't trivially one copy + a script revert, the promotion pack is wrong.

---

## LOCKED artifacts (never edit between candidates)

- `probes_v1.txt` — 20 probe queries. LOCKED so agreement/recall numbers are
  comparable candidate-to-candidate. Add only with a version bump + re-baseline.
- The gate thresholds: Recall@6 margin **0.05**, per-query floor **1**. Changing
  either re-opens every prior verdict — treat as a methodology version bump.

## Anti-patterns

- **Don't overwrite the live index during evaluation.** Side-path parquets only.
- **Don't trust MTEB as a promotion signal.** It's a Gate-1 sniff test. This corpus
  is weird (tag stubs, short quotes); only the gold set decides.
- **Don't promote on aggregate alone.** Gate B is the whole point.
- **Don't skip the preflight dimension probe.** A dim mismatch discovered after a
  3-hour re-embed is a wasted afternoon.
- **Don't change probes or thresholds mid-stream.** Locked means locked.

## Quick reference

| Gate | Cost | What | Output |
|---|---|---|---|
| 0 | 5 min | Read gotchas + 2-request dim probe | Contract confirmed at 1024-dim |
| 1 | 5 min | MTEB retrieval sniff | Worth a candidate build? |
| 2 | ~3 h | Side-path candidate index build | Candidate parquet, both load clean |
| 3 | labeling | Agreement A/B → gold template → label → `--gold` | PROMOTE / KEEP verdict |
| 4 | ~3 h | Cut over live index + scripts | Live swap + one-line rollback |
