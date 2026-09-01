---
name: local-model-upgrade-gates
description: "Five-gate decision flow for evaluating ANY candidate local LLM (Qwen, Gemma, Llama, Mistral, etc.) before pulling and refactoring. Use when Pete receives a Perplexity Events notification about a new local model, asks 'should I upgrade to model X', mentions a new Ollama release, or proposes swapping the LOCAL_MODEL constant in _llm_helper. Codifies the lesson from §11q (2026-06-02): a 20 GB Qwen 3.6 pull + 4 hours of bug-chasing was avoidable with 5 minutes of paper review. Gate 0 (added 2026-06-14) requires reading Perplexity_Only/OLLAMA_GOTCHAS.md so institutional memory enters the evaluation before benchmark reading. Locks identical fixtures (Phase 3 wiki gen + kw_ask synthesis + Pass C scoring) across all future evaluations so models are comparable apples-to-apples regardless of family."
metadata:
  author: pete-kastner
  version: '1.2'
  created: '2026-06-02'
  updated: '2026-06-14'
  changelog: 'v1.2 (2026-06-14) rescales Pass C fixture to canonical 1-5 (matches master); v1.1 added Gate 0'
  scope: kastner-aberdeen-archive
---

# Local Model Upgrade Gates

## When to Use This Skill

Activate whenever Pete is considering swapping the local LLM that powers any of the archive workloads. Trigger phrases:

- "Perplexity Events notified me about Qwen X / Gemma X / Llama X / Mistral X"
- "Should I upgrade to <model>?"
- "Should we bump LOCAL_MODEL?"
- "New <family> model dropped"
- "Worth pulling <tag>?"
- Pete pastes an Ollama tag URL and asks "what do you think"

Do NOT activate for:

- Embedding-model changes (bge-m3 lives in a different lane; use a separate evaluation)
- Cloud model changes (Claude, GPT, Gemini — different cost/quality calculus)
- Routine version bumps within the same generation (e.g., Qwen 3.5 patch release with no behavior change)

## Core Principle

**Status quo wins ties.** Every gate is biased toward "don't pull". The default outcome is "keep the incumbent". The candidate has to earn its way through four gates in order; failing any one stops the process.

This bias exists because the cost asymmetry is real:

- **Cost of skipping an upgrade we should have made:** maybe slightly worse Phase 3 output, easily revisited next month
- **Cost of pulling an upgrade we shouldn't have made:** 20 GB download + N hours of refactor + N hotfixes + a rollback session (see §11q, 2026-06-02)

We measured the second cost on 2026-06-02. The first cost is theoretical.

## The Five Gates

Gates are sequential. Each is a STOP point if the candidate fails. Document the gate-0 / gate-1 / gate-2 reasoning in the session before proceeding to the next gate. Never skip ahead.

### Gate 0 — Read the gotchas ledger (cost: 60 sec, 1 file fetch)

**Goal:** before doing ANY analysis on a candidate, read `Perplexity_Only/OLLAMA_GOTCHAS.md` end-to-end. This is the canonical, append-only ledger of every Ollama / local-LLM landmine we've stepped on. Skipping this gate caused us to re-discover the Qwen 3.x `think:false` requirement on 2026-06-14, ~2 weeks after first finding it.

**Fetch command:**

```bash
gh api -H "Accept: application/vnd.github.raw" \
  /repos/shorttack/aberdeen-group-archive/contents/Perplexity_Only/OLLAMA_GOTCHAS.md
```

**Process:**

1. Read every entry (G1, G2, ...) — these are short by design.
2. For each entry whose `Affected models` line could match the candidate's family, hold the symptom + fix in working context.
3. If the candidate is in a family that already has known gotchas (e.g., Qwen 3.x thinking-mode trap), pre-apply the documented fix to your Gate 3 fixture predictions and Gate 4 A/B harness payloads. Do not rediscover.

**Stop-conditions at Gate 0 (any one = abort):**

- A G-entry explicitly says "do not use this family for <workload>" and that workload is in scope. Respect it.
- The candidate's tag string matches a known-broken tag in any G-entry's `Affected models` line — wait for vendor fix.

**Outputs to capture in the session log:**

- Which G-entries are relevant to this candidate (by ID: G1, G3, ...).
- Any payload-shape changes the candidate inherits from a relevant G-entry (e.g., `"think": false` for any Qwen 3.x).

This gate has no judgment calls and no quality assessment. It exists purely to ensure institutional memory enters the evaluation BEFORE benchmark reading begins.

### Gate 1 — Independent benchmark review (cost: 5 min, 1-2 web fetches)

**Goal:** read one or two credible head-to-head comparisons of incumbent vs candidate, written by someone not selling either model.

**What "credible" means here:**

- Runs the same harness across multiple releases (so deltas are comparable)
- Tests both thinking AND non-thinking mode if the candidate is hybrid
- Publishes individual benchmark scores, not just aggregate averages
- Calls out regressions explicitly, not just gains

**Source-of-truth ladder (use in order):**

1. **The Kaitchup substack** (kaitchup.substack.com) — Benjamin Marie runs a stable harness across Qwen / Gemma / Mistral / Llama releases. Per §11q evidence: his article was the load-bearing finding that should have stopped the 3.5→3.6 pull. Some posts are paywalled at the latency section; the structural-regression discussion is usually in the free portion.
2. **Artificial Analysis** (artificialanalysis.ai/models/comparisons/<model-a>-vs-<model-b>) — independent benchmarks with per-task breakdowns. Use to corroborate Kaitchup.
3. **The model vendor's own release notes** — read AFTER 1 and 2 to understand what the vendor claims, but never as a load-bearing source. Vendors over-state gains and under-report regressions by construction.
4. **HuggingFace model card** — useful for context length, license, architecture, but never for quality claims.

**Stop-conditions at Gate 1 (any one of these = abort):**

- The candidate is "significantly worse" than incumbent on instruction-following (IFBench or equivalent)
- The candidate regresses on the specific benchmark family that maps to your workload (see Gate 2 mapping)
- Two independent sources find regressions in the same dimension
- The candidate's gains are concentrated in a domain you don't use (e.g., agentic coding when your workload is document synthesis)

**Do NOT proceed to Gate 2 if Gate 1 fails.** Write up the finding, decide against the upgrade, archive the candidate URL for future reference. This is the cheapest stop point and the one that would have saved §11q.

### Gate 2 — Workload-to-capability mapping (cost: 3 min, no tools)

**Goal:** for each of your three archive workloads, write down what specific capability the candidate would improve.

**The four workloads (these are LOCKED — do not change them when evaluating new models):**

| Workload | Primary capability needed | Secondary capabilities | What does NOT matter |
|---|---|---|---|
| **Phase 3 wiki generation** | Template-following: render structured CSV fields as Obsidian Markdown with YAML frontmatter + fixed section headers. Discipline > creativity. | Stable long-context reading of the CSV row + masters context. Acceptable Markdown structural fidelity over ~1,400 pages. | Math reasoning. Coding. Multimodality. Long thinking traces. |
| **kw_ask synthesis** | Faithful extractive Q&A over retrieved bge-m3 passages. Citation discipline: cite passage IDs that appear in input; never invent. | Concise prose. Refusing to answer when context is insufficient. | Math reasoning. Coding. Agentic tool use. Multimodality. |
| **Pass C prescience scoring** | Calibrated numeric output (0-100) with structured JSON. Consistent rationale formatting. | Light reasoning to compare prediction → outcome. Tolerance for ambiguous evidence. | Coding. Multimodality. Visual reasoning. |
| **Kastner-voice narrative drafting** (added 2026-09-01) | Voice fidelity to `Perplexity_Only/kastner_voice_prompt_v1.md`: correct we/I split, thesis discipline (Kastner argues to a point), the 8 rhetorical moves used only where they earn their place, no invented facts. | Citation-tag placement in `[study-<id>]` form for `convert_citations.py`, concrete-number anchoring, register shifts to fit the passage, honest "what I got wrong" reckoning. | Coding. Math. Multimodality. Agentic tool use. |

**Fixture note for the fourth workload.** No fixture is locked yet. The Databases study — input `DB_LONGITUDINAL_DOSSIER_v2.md`, known-good output `RDBMS_NARRATIVE_KASTNER_v1.md` — is the designated candidate fixture pending Pete's approval. Until it is frozen and Pete has blind-ranked incumbent vs. candidate outputs on voice + factual fidelity, cloud remains the Phase-3-narrative default and no local candidate replaces it. This workload's pass criteria are Pete's blind ranking, not automated structural checks — narrative quality does not lend itself to `run_gates.py`.

**Process:**

1. For each row above, ask: "Does the Gate 1 evidence show the candidate is BETTER on the primary capability?"
2. If "no" on any row → STOP. The candidate doesn't help that workload.
3. If "yes" on at least one row → proceed to Gate 3 ONLY for the workloads where the answer was yes. Don't burn fixture time on workloads the candidate can't improve.

**Hardware ceiling note (added 2026-09-01).** Pete's M4 Pro Mac mini has 32GB unified memory, which caps comfortable MLX residency at ~27B-parameter dense models. **A 64GB M5 Pro Mac mini is arriving October 2026** and raises that ceiling substantially — MLX candidates in the 40-70B range that were previously out of scope become viable Gate-1 sources. After the M5 Pro cutover: re-open any candidate that failed Gate 2 solely because its target size didn't fit 32GB, and re-run the Layer-2 paired fixture for any Pass C candidate that couldn't be evaluated at full precision on M4. Do not carry M4-era "too big to test" verdicts across the hardware change without a fresh probe.

**Stop-conditions at Gate 2 (any one of these = abort):**

- The candidate's gains are entirely in "what does NOT matter" columns
- The candidate is reported as a thinking model by default and the workloads above are factual-extraction (thinking adds latency without quality)
- The candidate's architectural changes (e.g., MoE vs dense, multimodal added, agentic tooling added) target capabilities not used here

**Document explicitly:** "Candidate <X> proposed for upgrade. Gate 1 evidence: <link + quote>. Gate 2 mapping: <which workloads benefit, which don't>. Proceeding to Gate 3 for: <list>." This goes in the decisions log so future sessions can audit the reasoning.

### Gate 3 — Paper smoke-test with fixture prompts (cost: 10 min, no model pull required)

**Goal:** before any model pull, read each fixture prompt and predict the candidate's failure modes.

**The fixtures live at `assets/fixtures/`.** They are LOCKED — never edit, never substitute, never "improve" them between evaluations. The point is that comparison across all future model upgrades uses the IDENTICAL probe. Variability between candidates is then attributable to the candidate, not to fixture drift.

Three fixtures (one per workload):

- `assets/fixtures/phase3_study_page.md` — input: a small CSV row + 3 sample observations. Pass criteria: YAML frontmatter parses cleanly, four required section headers present in order, no fabricated observation IDs.
- `assets/fixtures/kw_ask_synthesis.md` — input: question + 5 retrieved passages with IDs P1-P5. Pass criteria: cites only [P1]-[P5], refuses to answer if asked about content not in passages, no parametric knowledge bleeding through.
- `assets/fixtures/pass_c_scoring.md` — input: prediction + outcome pair. Pass criteria: returns integer 0-5 (canonical Aberdeen scale, NOT 0-100, NOT 1-5), returns valid JSON, rationale references both the prediction and the outcome by name. **PLUS** a Layer 2 paired-fixture run against `scripts/qwen_master_kappa_v2_paired.csv` (1,041 obs, Qwen vs Sonar) with quadratic-weighted κ ≥ 0.70 raw or after ≤±1 shift. Qwen 3.5 27B MLX baseline-to-beat: κ_max = 0.331.

**Process:**

1. Read each fixture for the workloads that survived Gate 2.
2. For each, write a 2-sentence prediction of how the candidate will likely fail. Be specific: "I expect Qwen 3.6 in default thinking mode will swallow most of the citation tokens inside `<think>` and return an empty response field."
3. Save predictions to the session log.

**Stop-conditions at Gate 3 (any one of these = abort):**

- All predictions are "candidate will perform identically to incumbent" — no measurable upside justifies the pull
- The predicted failure modes require non-trivial new prompt engineering to mitigate (every workaround is technical debt)
- The fixture requires structured output and the candidate's published behavior is known to break it (e.g., always wraps output in markdown code blocks)

This gate is paper-only. It surfaces "we don't actually expect this to help" before any 20 GB download.

### Gate 4 — Real hardware A/B (cost: 1 model pull + ~30 min wall-clock)

**Only reach this gate after Gates 1-3 pass.** This is the ONLY gate that should ever burn a model pull.

**Pre-flight checklist:**

- Incumbent is still installed (do not remove)
- At least one workload survived Gate 2 with a "yes"
- Disk space: candidate size + 30 GB headroom
- Pete has at least 60 minutes of uninterrupted time

**Process:**

1. Pull the candidate via `change_local_model_v3.sh` (or its current version) — the installer's pre-flight checks belong to the model-install lane, not this skill.
2. Run `scripts/run_gates.py --incumbent <tag> --candidate <tag>` (in this skill's `scripts/`). It exercises all three fixtures against both models, records:
   - Pass/fail for each fixture's structural criteria
   - Wall-clock to first token
   - Total tokens generated
   - Eval count
   - Side-by-side raw output for human read
3. Output lands in `/home/user/workspace/model_eval_<candidate_tag>_<YYYYMMDD>/`:
   - `summary.md` — table of pass/fail + timing
   - `raw_outputs/<fixture>_<model>.txt` — full responses for manual quality read
   - `decision.md` — Pete's final call, pasted into decisions log

**Decision rule:**

The candidate replaces the incumbent ONLY if ALL of:

- It passes every structural criterion the incumbent passes (no regressions on what already works)
- It passes at least one criterion the incumbent fails (real measurable upside)
- It does not increase Phase 3 wall-clock estimate by more than 25% (the 3-hour Phase 3 run cannot become a 4-hour run without a quality justification)

If those conditions fail, the candidate stays installed on the soak schedule (7 days for human-eyeball validation in production-like use), then gets removed if no upside emerges.

## Emergency Override

The four gates can be skipped only if ALL of the following are true:

1. The incumbent has a known, reproducible quality regression (not a feature gap — a regression)
2. The incumbent is no longer available on the Ollama registry (vendor pulled it)
3. A drop-in replacement from the same family is announced

Otherwise: gates apply. Skipping gates for any "this looks really exciting" reason is what produced §11q.

## Per-Family Source Index

Pre-curated Gate 1 sources for each model family. Update this section when new credible reviewers emerge.

### Qwen family

- **Kaitchup head-to-head** (template): `https://kaitchup.substack.com/p/qwen<X>-<Y>-vs-qwen<X-1>-<Y>-vs-gemma`
  - 2026-06-02 finding: Qwen 3.6 27B IFBench + GPQA Diamond regressions vs 3.5
- **Artificial Analysis comparison** (template): `https://artificialanalysis.ai/models/comparisons/qwen<X>-<Y>-vs-qwen<X-1>-<Y>`
- **Unsloth ops guide** (sampling params, MLX vs GGUF tradeoffs): `https://unsloth.ai/docs/models/qwen<X>`
- **Ollama tag page** (verify MLX availability, file sizes): `https://ollama.com/library/qwen<X>/tags`

### PPLX (Perplexity Hybrid runtime)

Special-case source, not a regular family. PPLX Qwen 3.8 27B is the local half of Perplexity Hybrid Compute (launched 2026-09-01), managed by the Perplexity Mac app rather than pulled through Ollama.

- **Perplexity Hybrid launch post**: `https://www.perplexity.ai/hub/blog/` (search for the 2026-09-01 hybrid-compute announcement)
- **9to5Mac coverage** for hardware requirements: `https://9to5mac.com/2026/09/01/perplexity-launches-privacy-minded-hybrid-compute-ai-feature-for-mac/`
- **No independent head-to-head yet.** Treat PPLX as a Gate-1 candidate with vendor-only benchmarks — this is a Gate-1 red flag, not a stop-condition, but weight it accordingly.

**PPLX cannot displace an Ollama incumbent on Pass C prescience scoring** (workload 3) without independently clearing Layer 2 of the paired fixture at κ ≥ 0.70. Non-grounded models fail this by construction (G3 in `OLLAMA_GOTCHAS.md`); PPLX is non-grounded local inference. If Layer 2 fails, PPLX remains a legitimate candidate for workloads 1, 2, and 4 only.

### Gemma family

- **Kaitchup head-to-head** (template): `https://kaitchup.substack.com/p/gemma-<X>-vs-qwen<Y>-vs-llama<Z>`
- **Google blog announcement** — context, not quality claims
- **Ollama tag page**: `https://ollama.com/library/gemma<X>/tags`

### Llama family

- **Kaitchup**: searches for "llama<X>" usually surface a head-to-head
- **Meta announcement** — context, not quality claims
- **Ollama tag page**: `https://ollama.com/library/llama<X>/tags`

### Mistral family

- **Mistral release blog** — usually publishes benchmark comparisons (more honest than most vendors, but still vendor-sourced)
- **Kaitchup** — slower to cover Mistral than Qwen/Gemma; check 2-4 weeks after release
- **Ollama tag page**: `https://ollama.com/library/mistral<X>/tags`

### Apple-Silicon-specific note

For all families, prefer MLX-native tags over GGUF on Pete's M4 Pro Mac mini. MLX tags preserve the Apple Silicon matmul paths; GGUF Q4_K_M variants typically run 1.5-2× slower on the same hardware. When the tag page shows both, the MLX variant is the default candidate. Honor the standing rule: **abort if no MLX**.

## Gate 6 — Runtime candidacy (added 2026-09-01)

**Goal:** for any candidate that clears Gates 0-4, decide which runtime hosts it in production. This gate exists because as of 2026-09-01 there are three distinct local-runtime options on the Mac, not one, and choosing the wrong one is a rollback problem even when the model itself is good.

**The three runtimes:**

| Runtime | What it is | Fits which workloads | Fixture history |
|---|---|---|---|
| **Ollama on Mac** | Direct Ollama server, MLX-native tags preferred, incumbent for all archive workloads | Phase 3, `kw_ask`, Pass C, and narrative drafting when the bakeoff supports it. The only runtime with a locked fixture regime today. | Full: all four workloads have baselines; Pass C has Layer-2 κ history at 0.331 (Qwen 3.5 27B MLX). |
| **Hybrid / PPLX** | Cloud-orchestrated with local model (PPLX Qwen 3.8 27B) invoked for gated steps. App-managed; no Terminal, no Ollama. | Interactive Computer sessions where cloud planning + one-shot local reads are the shape of the work. Not scriptable from `pipeline_canonical_v3.sh`. | None on any archive workload as of 2026-09-01. |
| **Cloud** | Frontier cloud models via Computer | Phase 3 narrative drafting (current default), Phase 1/2 interpretive synthesis over public archive content, any workload needing cross-archive breadth. | Not applicable to this skill's regime. |

**Decision rule:**

1. **Batch, scripted, reproducibility-critical work (Phase 3 wiki gen, Pass C, `kw_ask` at scale)** → **Ollama on Mac.** Hybrid's orchestration model does not support unattended overnight runs driven by `pipeline_canonical_v3.sh`, and its lack of fixture history means adopting it for Pass C would invalidate prescience-score comparability. This is not a quality claim about PPLX; it is a claim about the runtime's fit to the surrounding tooling.
2. **Interactive, one-shot, human-in-the-loop work (Phase 2 v2 ingest, narrow verification passes, ad-hoc `kw ask`-like questions when the bridge sandbox blocks localhost)** → **Hybrid/PPLX is a legitimate first-class option.** Zero cloud credits, runs entirely on the Mac, sensible when the question is bounded and the answer is not headed for a master CSV.
3. **Narrative drafting (workload 4)** → **cloud default, with local bakeoff in progress.** Once the Databases fixture is frozen and Pete blind-ranks candidates, the winning runtime becomes the default for that workload only.
4. **Never mix runtimes on a single load-bearing pipeline invocation.** A Pass C run is Ollama end-to-end or it is not a Pass C run; a Hybrid narrative pass is Hybrid end-to-end.

**Post-M5-Pro-cutover (October 2026):** re-evaluate this table. A 64GB machine may make Ollama-hosted 40-70B MLX models competitive with cloud on narrative drafting, in which case Gate 6 for workload 4 flips from "cloud default" to "Ollama default" without needing Hybrid at all. Do not assume the runtime split above is stable across hardware changes.

## Anti-Patterns (don't repeat §11q)

- **Don't pull before reading.** "Notification fired → ollama pull" is the §11q anti-pattern. Always Gate 1 first.
- **Don't trust vendor benchmarks.** Vendors picked their benchmarks; independent reviewers found regressions Qwen did not advertise.
- **Don't conflate "newer" with "better."** Hybrid-thinking models add maintenance surface (top-level `think:false` flag, fixture variance between thinking and non-thinking modes, latency unpredictability). For factual-extraction workloads, non-thinking incumbents are often the better choice.
- **Don't change fixtures between candidates.** The Phase 3 + kw_ask + Pass C fixtures are LOCKED. Any improvement to the fixtures applies to ALL future evaluations and requires re-running incumbent baseline.
- **Don't skip the rollback plan.** Before Gate 4, write down the exact one-line edit that rolls back to incumbent. If the rollback isn't trivially trivial, the upgrade pack is wrong.
- **Don't skip Gate 0.** OLLAMA_GOTCHAS.md is short by design. Reading it costs less than re-discovering a landmine. The 2026-06-14 Qwen 3.5 calibration v5 disaster (28 of 30 obs returned empty `response`, parse_ok=false, all 30 obs wasted) was preventable by 60 seconds of ledger-reading.
- **Don't substitute frozen LLMs for grounded scorers on prescience tasks.** The 2026-06-14 PM Qwen 3.5 27B MLX calibration produced κ_max = 0.331 vs Sonar across 1,041 obs (raw, ±1 shift, tier-bucket — all variants failed 0.70 gate). Root cause is structural: grounded models (Sonar) retrieve evidence and abstain; frozen LLMs commit from training priors. No prompt anchoring fixes this. See G3 in OLLAMA_GOTCHAS.md. If a candidate is non-grounded and the workload is Pass C, expect to fail Layer 2 of the fixture — Gate 1 should catch it before any pull.

## Files in This Skill

- `SKILL.md` — this file
- `assets/fixtures/phase3_study_page.md` — Phase 3 fixture (LOCKED)
- `assets/fixtures/kw_ask_synthesis.md` — kw_ask fixture (LOCKED)
- `assets/fixtures/pass_c_scoring.md` — Pass C fixture v3 (LOCKED, 0-5 canonical + Layer 2 paired-fixture lock)
- `scripts/run_gates.py` — Gate 4 A/B runner against Ollama
- `references/decisions_log_11q_2026_06_02.md` — the §11q evidence trail that motivated this skill
- `references/decisions_log_qwen27b_calibration_failed_2026_06_14.md` — the 2026-06-14 Qwen failure evidence (Layer 2 paired-fixture established, κ_max=0.331 baseline)

## External Companion Files (not in skill, but required reading)

- `Perplexity_Only/OLLAMA_GOTCHAS.md` in `shorttack/aberdeen-group-archive` — the append-only landmine ledger. Gate 0 reads this. Add entries here, not in this skill, when new gotchas surface in production. The repo file is the single source of truth so it's accessible from Mac, sandbox, and future sessions without loading this skill.

## Quick Reference

| Gate | Cost | What to do | Output |
|---|---|---|---|
| 0 | 60 sec | Fetch + read `Perplexity_Only/OLLAMA_GOTCHAS.md` | List of relevant G-entries + inherited payload changes |
| 1 | 5 min | Read Kaitchup + ArtificialAnalysis | Stop OR proceed; quote regressions found |
| 2 | 3 min | Map candidate gains to 3 workloads | Stop OR list workloads that benefit |
| 3 | 10 min | Read 3 fixtures, predict failures | Stop OR document predictions |
| 4 | 30 min + 1 pull | Run A/B via `scripts/run_gates.py` | Pass/fail table; Pete's call |
