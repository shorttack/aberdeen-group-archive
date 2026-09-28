# Workload 4 Fixture — Kastner-voice Narrative Bakeoff (Databases)

**Governing skill:** `local-model-upgrade-gates` v1.3 (workload 4, Gate 6).
**Fixture status:** LOCKED once Pete signs off on this README, the dossier, and the gold reference. After lock, no edits to fixture inputs — any change requires re-running all prior contestants against the new inputs so cross-model comparability is preserved.

---

## 1. Purpose

Decide which runtime writes **Phase 3 Kastner-voice longitudinal narrative** for `kastner-longitudinal-study-builder` Mode A. This is the last cloud-dependent workload in the archive pipeline; if a local runtime wins, the archive becomes end-to-end local-runnable on the M4 today.

**Method:** three contestants receive an identical dossier and an identical prompt, produce a narrative + machine-readable sidecar under identical output rules, get pre-filtered on structural criteria, and the survivors are ranked blind by Pete on voice + factual fidelity.

**Not in scope for this fixture:** Phase 3 wiki generation, `kw_ask` synthesis, Pass C prescience scoring. Those are workloads 1, 2, 3 with their own (still-unmaterialized) fixtures.

---

## 2. Fixture inputs (LOCKED after sign-off)

| Role | Path | Size | Notes |
|---|---|---|---|
| Dossier (Phase 2 output) | `DB_LONGITUDINAL_DOSSIER_v2.md` | 35,609 bytes (321 lines) | Alias-consolidated vendor evidence, 1970–2005 window, prescience scores, verbatim observation text |
| Gold reference (Phase 3, target) | `RDBMS_NARRATIVE_KASTNER_v1.md` | TBD | Not yet produced. See §7. |
| Voice prompt | `Perplexity_Only/kastner_voice_prompt_v1.md` | (on Mac, referenced from the skill's workload-4 table) | Not duplicated here — canonical location is the archive |

**Minimum-source-size floor:** the 35 KB dossier is well above the "tens of KB" threshold Requirement 1 of the workload-4 fixture note requires. Any future re-run against a smaller dossier is a different fixture and requires re-baselining.

---

## 3. Contestants

Five contestants are supported. Default M4 baseline enables three (marked *default*); the two Qwen 3.6 Ollama variants are one env-var flip away for whenever the Gate 6 question is refined into "runtime effect vs. model effect" (same base model, PPLX runtime vs. Ollama runtime).

| ID | Runtime | Model | Invocation surface | Enabled by default |
|---|---|---|---|:-:|
| `cloud` | Cloud (Perplexity Computer) | Frontier default | This thread or a fresh cloud session | ✓ |
| `ollama` | Ollama on Mac | `qwen3.5:27b-mlx` (`_llm_helper_v4.py` incumbent) | Direct `curl` to `http://localhost:11434/api/generate` from `run_bakeoff.sh` | ✓ |
| `ollama-q36-a3b` | Ollama on Mac | `qwen3.6:35b-a3b` | Same as `ollama`, different model tag | – |
| `ollama-q36-mlx` | Ollama on Mac | `qwen3.6:35b-mlx` (same base as `pplx`, different runtime) | Same as `ollama`, different model tag | – |
| `pplx` | Hybrid (PPLX local) | `pplx-computer-qwen-3-6-35b-a3b-mlx-20260709` (4-bit, on-device) | `run_local_subagent` from an orchestrating cloud session, or a fresh Hybrid thread with the model selector set explicitly | ✓ |

**Why the two extra Ollama contestants exist.** The `pplx` and `ollama-q36-mlx` contestants share the same base model (Qwen 3.6 35B) but differ in runtime. If both make it through the pre-filter and Pete ranks one clearly above the other, the delta is a runtime effect (PPLX app vs. Ollama server), not a model-quality effect. That distinction changes which knob to turn at the M5 Pro cutover — upgrade the model, or switch the runtime, or both.

See `MODEL_INVENTORY.md` in this folder for what's actually installed on disk and where the two model stores currently live.

**Discipline:** each contestant runs end-to-end on its own runtime — no mixing (per skill §Gate 6 rule 4). Cloud does not touch the local model even if Hybrid is available in the session; Ollama does not fall back to cloud even if a step is slow; PPLX does not delegate long-tail synthesis to a cloud call.

---

## 4. Prompt template (LOCKED)

Every contestant receives the same prompt, verbatim, with only the `{{DOSSIER}}` placeholder replaced by the full text of `DB_LONGITUDINAL_DOSSIER_v2.md`.

```
You are drafting Chapter 1 of "The Database Decade," Peter S. Kastner's
Phase 3 longitudinal narrative on relational database management systems,
1970–2005. Use the evidence dossier below as your ONLY source of facts.
Do not introduce any Aberdeen study, benchmark, vendor claim, prescience
score, quotation, or historical event that is not present in the dossier.

Voice: follow the specification in Perplexity_Only/kastner_voice_prompt_v1.md
(first-person where Kastner is the actor, first-person-plural where Aberdeen
is the actor, thesis-first paragraphs, the eight Kastner rhetorical moves
used only where they earn their place, honest reckoning where Kastner got
something wrong).

Output TWO artifacts, in this order, separated by a line containing only
`---SIDECAR---`:

1. The narrative itself, in Markdown. Target 2,000–3,500 words. Every
   factual claim that maps to a specific study, observation, vendor
   evidence row, or prescience value in the dossier must carry an inline
   anchor in one of these forms:
     - `[study-<study_id>]` for a claim citing a study as a whole
     - `[obs-<obs_id>]` for a claim citing a specific observation
     - `[ps=<0-5>]` for a claim referencing a prescience value
   Anchors go inline, immediately after the claim, before punctuation.

2. A YAML block containing the sidecar fields defined in §5. The YAML
   must parse cleanly; any content not in the schema is dropped.

Do not write a preamble, an outline, or a "Here is the narrative:" header.
Start the narrative with its first paragraph. End the narrative with its
last paragraph. Emit `---SIDECAR---` on its own line. Emit the YAML.
Nothing else.
```

**Rationale for the LOCK:** the smoke test on 2026-09-06 showed that unprompted, the local model produces clean prose with zero anchors and no sidecar. Requirements 2 and 3 of the workload-4 fixture note are enforced through this prompt, not through post-hoc reformatting.

---

## 5. Sidecar schema (LOCKED)

Each contestant emits a YAML block with these keys. Missing keys count as sidecar failures.

```yaml
study_id: 2026-kastner-database-decade-rdbms
title: "The Database Decade: How Relational Databases, and the Stopwatch I Held to Them, Became the Best Work of My Aberdeen Years"
subject_domain: commercial-benchmarks
methodology: longitudinal-archival-synthesis
pub_year_range: [1970, 2005]
entity_cluster: [Oracle, Informix, Sybase, Ingres, CA, NCR, "Software AG", DB2, CCA]
prescience_anchors:
  - {obs_id: <string>, ps_value: <int 0-5>}
  - ...
```

**Field derivation rules:**
- `study_id`, `title`, `subject_domain`, `methodology`, `pub_year_range` are given — a contestant that changes them is failing the extraction test, not showing initiative.
- `entity_cluster` must be the vendor list from Dossier §0 (consolidated vendor volume table), in that order. Alias variants collapsed. Contestants that add out-of-dossier vendors fail.
- `prescience_anchors` must be populated only from the "Prescience layer (scored)" tables in the dossier. Contestants that invent `obs_id` values or `ps_value` integers not present in the dossier fail.

---

## 6. Pre-filter (before Pete sees any narrative)

For each contestant output, mechanical pre-filter checks in this order. Failure at any step disqualifies that contestant from voice ranking.

| # | Check | Pass criterion |
|---|---|---|
| 1 | Narrative length | 2,000 ≤ words ≤ 3,500 (soft ±10% grace) |
| 2 | Sidecar parses | Valid YAML, all §5 keys present |
| 3 | Sidecar fidelity | `study_id`, `title`, `subject_domain`, `methodology`, `pub_year_range` match §5 exactly; `entity_cluster` is a subset of the dossier §0 list; every `prescience_anchors` row exists in the dossier's prescience-layer tables |
| 4 | Anchor coverage | `(anchored_factual_claims / total_factual_claims) ≥ 0.90` — measured by the coverage script (§8) |
| 5 | No out-of-dossier facts | Manual spot-check on 10 random anchored claims — every claim traces back to the cited artifact in the dossier |

Pete never sees which contestant produced which output. Filenames on disk are `narrative_<contestant>.md` and `sidecar_<contestant>.yaml`; a wrapper script produces the blind-ranking bundle by copying them to `blind/A.md`, `blind/B.md`, `blind/C.md` with a `blind/key.json` mapping stored outside Pete's view until after ranking.

---

## 7. Gold reference — SETTLED: Option B (deferred)

**Decision (2026-09-06):** Option B. The first bakeoff runs without a gold reference. Pete blind-ranks the three contestants on voice + factual fidelity as absolute judgments, not as similarity-to-gold. `RDBMS_NARRATIVE_KASTNER_v1.md` is NOT required on disk before dispatch. The `local-model-upgrade-gates` skill permits this — its language is "blind-ranked … on voice + factual fidelity," not "closest match to gold."

If the first bakeoff is inconclusive and a tighter reference is later needed to break a tie, revisit and produce a gold narrative under Option A (Pete-authored or Pete-attached, dropped in this folder as `RDBMS_NARRATIVE_KASTNER_v1.md`). Until then, the fixture inputs are: dossier only.

---

## 7a. Threshold calibration — 2026-09-06 run

The LOCKED anchor-coverage threshold is 0.90 (workload-4 fixture note, Requirement 3). Empirical dry-run against a careful cloud-authored narrative on 2026-09-06 scored 0.35 with 21 explicit anchors across 60 factual sentences — the classifier is aggressive (every numeral or vendor-name sentence counts as factual), and multi-sentence paragraphs where one sentence carries an anchor and successors continue the same claim do not inherit the anchor.

**Decision for run_20260906T*** (Pete, 2026-09-06):** threshold LOWERED to 0.50 for this bakeoff only. Rationale: 0.90 is unachievable in a natural Kastner-voice narrative without anchor-per-sentence density that would harm readability; 0.50 preserves the pre-filter's ability to catch contestants that write uncited prose, while allowing careful narratives through. Change recorded in `outputs/run_<UTC>/run_<UTC>.log` via `COVERAGE_THRESHOLD=0.50`.

**For future bakeoffs and the M5 Pro re-baseline (October 2026):** revisit the threshold once the classifier's factual/framing split can be tightened, or once the anchor-coverage definition is reworked to give partial credit for paragraph-level (not sentence-level) anchoring. Do not carry 0.50 forward as the new default without an explicit re-decision — the LOCKED 0.90 remains the reference.

---

## 8. Anchor-coverage measurement

**Definition.** A *factual claim* is any sentence that asserts a specific vendor action, study finding, benchmark number, quotation, date, market share, or prescience outcome. Framing sentences, transitions, thesis statements, and rhetorical moves are not factual claims.

**Measurement.** A short script (`coverage.py`, to be written before the bakeoff runs, lives in this folder) does the following:
1. Splits the narrative into sentences.
2. Classifies each sentence as `factual` or `framing` using a simple rule set (verbs of assertion, presence of numerals, presence of vendor/study/product proper nouns).
3. For each `factual` sentence, checks whether it contains at least one anchor in the allowed forms (`[study-*]`, `[obs-*]`, `[ps=*]`).
4. Emits `{contestant, factual_count, anchored_count, coverage}` to `coverage_<contestant>.json`.

**Threshold:** `coverage ≥ 0.90`. Below that, disqualified before voice ranking (workload-4 fixture note, Requirement 3).

The classifier is intentionally simple and identical across contestants. Its errors are the same for all three, so relative coverage numbers remain comparable even if absolute classification is imperfect.

---

## 9. Outputs the bakeoff will leave behind

```
workload4_databases/
├── README.md                                    (this file)
├── DB_LONGITUDINAL_DOSSIER_v2.md                (fixture input, LOCKED)
├── RDBMS_NARRATIVE_KASTNER_v1.md                (gold reference — Option A only)
├── coverage.py                                  (anchor-coverage script)
├── run_bakeoff.sh                               (dispatcher — writes the three narratives)
├── outputs/
│   ├── narrative_cloud.md
│   ├── narrative_ollama.md
│   ├── narrative_pplx.md
│   ├── sidecar_cloud.yaml
│   ├── sidecar_ollama.yaml
│   ├── sidecar_pplx.yaml
│   ├── coverage_cloud.json
│   ├── coverage_ollama.json
│   ├── coverage_pplx.json
│   └── prefilter_report.md                      (which contestants passed §6)
├── blind/
│   ├── A.md                                     (one of the three, chosen by run_bakeoff.sh)
│   ├── B.md
│   ├── C.md
│   └── key.json                                 (mapping — not opened until after ranking)
└── ranking/
    └── pete_ranking_<date>.md                   (Pete's blind rank + rationale)
```

---

## 10. What has to happen before the first dispatch

Ordered, blocking. Items 1–3 are DONE (2026-09-06). Items 4–7 remain.

1. ~~**Pete confirms the gold-reference path.**~~ DONE 2026-09-06 — Option B (deferred). See §7.
2. ~~**Pete signs off on this README, the LOCKED prompt (§4), and the LOCKED sidecar schema (§5).**~~ DONE 2026-09-06. After sign-off, no edits without re-baselining.
3. ~~**`coverage.py` is written and unit-tested.**~~ DONE 2026-09-06 — 4 self-test cases pass (zero-anchors, full-coverage, mixed, backtick-anchor); real-world validation against `Perplexity_Only/SMOKE_TEST_local_model_2026-09-06.md` returns `coverage=0.00` (7 factual sentences, 0 anchored) matching the smoke test's own self-report.
4. **`run_bakeoff.sh` is written** — one dispatcher script that invokes all three contestants with identical inputs and writes to `outputs/`. Blocks contestant execution.
5. **Dry-run on the cloud contestant only**, to confirm the prompt template + sidecar schema produce a well-formed output and that the pre-filter script catches problems the way it should. Blocks live bakeoff.
6. **Live bakeoff** — all three contestants run, outputs land in `outputs/`, pre-filter runs, blind bundle assembles in `blind/`.
7. **Pete blind-ranks** and writes rationale to `ranking/pete_ranking_<date>.md`. Key revealed. Result recorded in the skill's decisions log.

Nothing on items 4–7 runs until Pete says "start" on each step.
