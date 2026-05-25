# Model Selection Finding — Bucket A Prescience Scoring

**Document ID**: model_prescience_scoring_finding_v1
**Date**: 2026-05-25
**Author**: Pete Kastner (Adoptex LLC, BlueBridge Group) with Computer
**Archive**: Kastner Aberdeen Archive v1.4
**Status**: Decision locked
**Decision**: **Qwen 3.5 27B-MLX, run locally on M4 Pro Mac mini, is the production scorer for Bucket A Pass C prescience scoring.**

---

## TL;DR for the curious researcher

We needed to pick a local LLM to score ~124 Aberdeen Group studies (Bucket A: Benchmark Reports) for prescience — how well each historical claim aged from publication through 2026. We considered three candidates: **Qwen 3.5 27B-MLX**, **Qwen 3.5 35B-MLX**, and a **cloud reference (Claude Sonnet 4.6)**. We picked 27B after a two-phase evaluation:

1. **Phase 1 — Speeds and feeds**: web research to confirm both Qwen MLX variants would run on a 48 GB M4 Pro Mac mini, what their throughput should look like, and how they were rated for reasoning/grounded-judgment tasks.
2. **Phase 2 — Three-way calibration**: one full study (`ra_warehouseautomation_3867`, 93 observations, 68 scoreable) scored by all three models against the same rubric, with pairwise agreement and Cohen's kappa reported.

**Result**: 27B agreed with the cloud at kappa **0.853** (near-perfect), 100% within-1 agreement. 35B agreed with the cloud at kappa **0.515** (moderate) and **inflated four non-claims as scoreable**, a discipline failure that would corrupt prescience rankings at scale. 27B was chosen.

---

## 1. Background

The Kastner Aberdeen Archive is a forever-archive of ~2,300 Aberdeen Group industry-analyst studies (1998–2007 era). Bucket A is the heaviest research surface — full benchmark reports with structured claims, predictions, and Best-in-Class frameworks. Pass C of the archive ingest workflow attaches a prescience score (0–5) and confidence (1–3) to each scoreable observation, asking: *did this 2007-era claim age well through 2026?*

This requires an LLM with strong grounding in 20+ years of enterprise IT history, willingness to assign **0** to non-claims (figure captions, methodology framing, author bios), and consistent rubric adherence across hundreds of studies. We wanted a model that could run **locally** — for cost, reproducibility, and forever-archive durability — provided the quality met a cloud-anchored calibration target.

---

## 2. Phase 1 — Speeds and Feeds

Before spending compute on side-by-side runs, we did web research to confirm the candidate stack was viable on the available hardware (48 GB M4 Pro Mac mini, MLX runtime via Ollama).

Key findings from the research pass:

- **Qwen 3.5 MLX variants** were the highest-rated open weights for grounded-judgment tasks on Apple Silicon at the time of the study, with MLX-specific quantizations giving usable throughput on 48 GB unified memory.
- **27B-MLX**: ~19 GB on disk, fits comfortably in memory with headroom for context windows up to 8K–32K, projected ~13 tokens/sec on M4 Pro.
- **35B-MLX**: ~21 GB on disk, just larger but still fits; projected slightly slower per-token throughput but with reasoning depth comparable to top-tier open weights.
- **Cloud reference**: Claude Sonnet 4.6 — used as ground-truth anchor, not as production scorer (cost and forever-archive principle both push against cloud-dependent production paths).

The speeds-and-feeds research said both Qwen variants were viable. No basis at that stage to pick between them — that's what Phase 2 was for.

---

## 3. Phase 2 — Three-Way Calibration

### 3.1 Calibration study

- **Study**: `ra-warehouseautomation-3867-89c99f` — *Warehouse Automation* (Aberdeen Group, January 2007, Ian Hobkirk and Jeff O'Neill)
- **Why this study**: medium-sized (93 observations / ~17K source tokens), rich claim mix (analytical claims, viability predictions, market metrics), broad technology coverage (barcoding, voice-directed picking, pick-to-light, AS/RS, parcel sortation, AGV/AMR precursors). Domain history is well-documented through 2026, so cloud scoring has solid ground.

### 3.2 Filter for scoreable observations

The ingest pipeline produces 93 observations per study, but not all are scoreable claims. A pre-pass excluded:

- Markdown headers (`## **Figure 4: ...**`)
- Pure figure references with no claim text
- Author bios
- Methodology framing
- Fragments under 40 characters

Result: **25 non-claim observations skipped, 68 scoreable observations sent to each model.**

### 3.3 Rubric (identical for all three models)

System prompt: "You are a technology industry historian specializing in enterprise IT trends from 1998-2026."

Scoring scale:
- **5** = Remarkably prescient (specific prediction played out essentially as stated)
- **4** = Largely prescient (direction correct, magnitudes/timing off)
- **3** = Partially right (mixed)
- **2** = Mostly wrong
- **1** = Wrong (contradicted by history)
- **0** = Cannot assess (too vague, too narrow, or no claim to test)

Confidence: 1 (low) / 2 (medium) / 3 (high).

Output: strict JSON per observation, parsed and concatenated into a CSV.

### 3.4 Generation parameters (locked)

```json
{
  "think": false,
  "keep_alive": "30m",
  "stream": false,
  "options": {"temperature": 0.2, "num_ctx": 8192, "num_predict": 400}
}
```

`think: false` was critical — Qwen 3.5 defaults to chain-of-thought, which produced 95% wasted tokens at ~190 s/obs in early testing. Disabling think dropped 27B to ~15 s/obs and 35B to ~3 s/obs.

`num_ctx: 8192` overrides Ollama's default 262,144 context window (which silently allocates massive KV cache and hangs the first request). This was the single biggest lesson from the calibration build — documented in `ollama_qwen_install_runbook_v1.md`.

### 3.5 Execution

All three model runs used the same prompt file (`prescience_score_prompt_v2.md`) and the same 68-row scoreable subset.

| Model | Throughput | Total wall clock | Parse success |
|---|---|---|---|
| Qwen 3.5 27B-MLX (local) | 15.35 s/obs | ~17.5 min | 68/68 (100%) |
| Qwen 3.5 35B-MLX (local) | 2.94 s/obs | ~3.3 min | 68/68 (100%) |
| Claude Sonnet 4.6 (cloud) | n/a (single batch) | n/a | 68/68 (100%) |

35B was 5.2× faster than 27B — counterintuitive at first, but explained by 35B's more efficient MLX kernel layout on M4 Pro plus the disabled thinking traces.

---

## 4. Results

### 4.1 Per-model statistics

| Metric | 27B-local | 35B-local | Cloud |
|---|---|---|---|
| n parsed | 68 | 68 | 68 |
| Mean score | 3.34 | 3.53 | 3.35 |
| Median score | 4 | 4 | 4 |
| **Zeros assigned** | **12** | **8** | **12** |
| Mean confidence | 2.37 | 2.43 | 2.49 |
| Mean rationale length (words) | 63 | 61 | 36 |
| Elapsed mean (s/obs) | 15.35 | 2.94 | n/a |

The zero count is the most important row. The cloud and 27B independently identified the same 12 observations as non-claim / unassessable. 35B inflated four of those — OBS-057 (demographic snapshot), OBS-074 (methodology framing), OBS-087 (tautological truism), OBS-091 (sample composition) — assigning them scores between 2 and 5. That's a discipline failure, not a quality win.

### 4.2 Pairwise agreement

| Pair | Exact agreement | Within-1 agreement | Mean abs diff | Max abs diff | Cohen's kappa |
|---|---|---|---|---|---|
| **27B-local vs Cloud** | **89.4%** | **100.0%** | **0.11** | **1** | **0.853** |
| 35B-local vs Cloud | 64.5% | 87.1% | 0.61 | 5 | 0.515 |
| 27B-local vs 35B-local | 70.0% | 85.0% | 0.60 | 5 | 0.579 |

Reading the kappa column:
- **0.853** — near-perfect agreement (>0.80 threshold)
- **0.515** — moderate agreement (0.41–0.60 band)
- **0.579** — moderate agreement

Within-1 agreement of **100%** between 27B and cloud means across all 66 comparable observations, the two passes never differed by more than one point on the 0–5 scale. The "max abs diff = 1" confirms it.

35B vs cloud has max abs diff = 5 — meaning at least one observation where the two scorers gave 0 and 5. Those were the inflated non-claims.

### 4.3 The decisive evidence

The cloud pass is the gold-standard human-historian anchor for this study. **27B tracks it at kappa 0.853 and never disagrees by more than 1 point.** 35B tracks it at kappa 0.515 and produces wild divergences on non-claims that would corrupt aggregated prescience rankings across 124 studies.

Speed alone is not enough to overcome that. If 35B were used in production:
- ~17.5 hours of compute saved across 124 studies (vs 27B's ~45 hours)
- But: ~500+ inflated non-claim scores corrupting the master prescience table
- And: a lower agreement floor with any future human-validation pass

The trade is unfavorable.

---

## 5. Decision

**Production model for Bucket A Pass C: Qwen 3.5 27B-MLX.**

Operational plan:
1. **27B as primary scorer** for all 124 Bucket A studies (~45 hours sequential at observed cadence)
2. **35B dropped from production.** Retained on disk as a reference for future calibration runs only.
3. **Cloud (Claude Sonnet 4.6) as low-confidence reviewer.** For any 27B output where `confidence == 1`, automatically send to cloud for a second-pass score. From the calibration set, this is rare (~2 obs out of 68) so cost is bounded.
4. **No cloud-as-primary.** Kappa 0.853 with 27B makes paying cloud rates for full Pass C redundant for the forever-archive use case.

This decision is recorded in `bucket_a_model_decision_template_v1.md` (Option D / Hybrid, refined).

---

## 6. Reproducibility

Anyone returning to this archive in 2027, 2030, or beyond can reproduce the calibration:

- **Install guide**: `ollama_qwen_install_runbook_v1.md` (8 hard-won lessons, full November 2026 refresh checklist)
- **Calibration runbook**: `CALIBRATION_README_v1.md` (7-step procedure)
- **Production scorer**: `run_prescience_calibration_v3.py` (locks the critical `think: false`, `keep_alive: 30m`, `num_ctx: 8192`, `num_predict: 400` parameters)
- **Comparison harness**: `compare_prescience_models_v1.py` (kappa, score histograms, pairwise agreement)
- **Decision template**: `bucket_a_model_decision_template_v1.md`

Calibration outputs preserved at `prepared/ra-warehouseautomation-3867-89c99f/working/`:
- `prescience_scores_qwen3_5_27b-mlx_v1.csv`
- `prescience_scores_qwen3_5_35b-mlx_v1.csv`
- `prescience_scores_cloud_v1.csv`
- `comparison_summary_v1.md`
- `comparison_table_v1.csv`
- `calibration_log_v1.jsonl`

---

## 7. Caveats and open questions

- **One-study calibration**: this finding is based on a single benchmark report. A second-study calibration on a different domain (e.g., a 2003 CRM or ERP study) would strengthen the conclusion. Recorded in `v1_5_backlog.md`.
- **OBS-007 obs_id typo in 27B output**: the model rendered the study suffix as `89c9f` instead of `89c99f` on one row — single-row glitch, not data corruption. Logged in v1.5 backlog.
- **35B's speed advantage may scale better on larger studies** (lower per-obs overhead), but unless its non-claim discipline can be improved via prompt engineering, that doesn't change the production decision.
- **Cloud model versions drift**. Claude Sonnet 4.6 was the reference in May 2026; future reruns should pin the model version explicitly. Generic "cloud" labeling in CSVs is a known weakness to fix in v1.5.
- **The 68/93 scoreable filter is pre-LLM**. If the upstream filter changes, calibration must be rerun.

---

## 8. Stewardship

This memo is a forever-archive document. It explains *why* the production scorer is what it is, so future researchers (including future Pete) do not need to re-derive the decision from first principles. If 27B is later replaced, the replacement should be justified by a similar three-way calibration — preserve the existing CSVs and add new ones alongside, never overwrite.

— *Memo prepared 2026-05-25 in support of Kastner Aberdeen Archive v1.4 release.*
