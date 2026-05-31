# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-05-30 PM (Pass C cloud scoring run completed — 3,761 obs scored across 492 studies via sonar-reasoning-pro + claude-sonnet-4.6 pilot; 369 [DEFERRED] studies rolled up via Rule A into 18 high / 54 medium / 200 low / 97 not-applicable; new evidence file `_master_prescience_scores.csv` (3,761 rows × 11 cols) committed to masters; studies-master post-rollup: 489 high / 346 not-applicable / 325 medium / 272 low / 1 [DEFERRED] / 1 NULL; Phases 1+2 rebuilt against `~/Desktop/kastner_wiki/`, Phase 3 in flight when Pete walked away)
**Current ship state:** **v1.5.0 released 2026-05-29** on both `shorttack/aberdeen-group-archive` and `shorttack/kastner-aberdeen-wiki` (Zenodo DOIs pending webhook fire). Wiki HEAD: `kw_note v4` (commit `20e9143c`). Archive HEAD: `roll_up_prescience_v3.py` (commit `5b2e88cb`). 1434/1434 studies have pub_year; **492/1434 prescience-scored via Pass C cloud (sonar-reasoning-pro + claude-sonnet-4.6)** — rolled up; **489 studies high prescience operationally** (`study_prescience_enum`); 124 high via obs-evidence layer (`v_studies_with_high_prescience`); bge-m3:latest is the canonical embedding model.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

- [ ] **Wait for Phase 3 to complete on Pete's Mac** (tier-1 LLM regen for 124 studies + 200 entities + 150 techs — ETA 30-90 min from 17:48 EDT start). Then run Phases 4-6 (`04_generate_indices_v2.py`, `05_compute_embeddings_v2.py`, `06_emit_scaffolding_v1.py`) to refresh wiki pages, embeddings, and scaffolding.
- [ ] **EOD batch commit to `shorttack/aberdeen-group-archive`** (pending Pete's go-ahead this evening). Files staged: `_master_studies.csv` (updated, 1434×16), `_master_prescience_scores.csv` (new, 3761×11), `_rollup_v3_audit_20260530T212525Z.csv`, `prescience_scores_pass_c_cloud_v1.csv`, `logs/pass_c_cloud_v1_run_report.md`, `logs/pass_c_cloud_v1_failures.jsonl`, `WORKLIST.md`, `_decisions_log.md` (append). Backup tree: `archive_masters_pre_rollup_v3_20260530T212525Z/_master_studies.csv`. See `commit_plan_2026_05_30_v1.md` for the exact Git Data API recipe.
- [ ] **EOD batch commit to `shorttack/kastner-aberdeen-wiki`** — deferred until Phase 1+2 are re-run against `~/Repos/kastner-aberdeen-wiki/` per v1.6 §11 (today's rebuild ran against the deprecated `~/Desktop/kastner_wiki/`). Once §11 closes, ship refreshed parquets + DB + wiki pages + embeddings + scaffolding.
- [ ] Cron `2e191f67` will auto-delete the abandoned v1 quarantine on **2026-06-05 09:00 EDT** — no action needed.

---

## v1.6 candidates

### 1. Recover the three known-missing sources

Status registry: `_missing_sources.csv` (archive root)

- [ ] **Robbins 1991 ATM** — search Wayback Machine (`web.archive.org/web/*/aberdeen.com/*`), ex-Aberdeen networking-team contacts, any institutional library that subscribed to Aberdeen's networking practice in 1991-1992. Founding artifact of the entire ATM-vs-Ethernet thesis — highest provenance value.
- [ ] **Casale 1989 Computational Chemistry** — Pete has hard copy. Scan to PDF, OCR, ingest via `archival-ingest` skill. `computational-chemistry` tech_id is already wired into `_master_technologies.csv` (commit `0d48d9a8`, 2026-05-26) and waits for the study.
- [ ] **Kastner 1987 Yankee Group Transaction Processing** — Yankee Group archives or Kastner personal records. Ghostwritten for John Logan; if recovered, ingest with dual author credit.

Recovery workflow is codified in `_decisions_log.md` 2026-05-26 entry.

### 2. Bucket C+D prescience scoring — superseded by cloud-scoring pivot

- [ ] **Status update 2026-05-30**: the Pass C cloud-scoring pivot (sonar-reasoning-pro + claude-sonnet-4.6) replaced the original local-Ollama Bucket A+B scope. Today's run covered 492 studies / 3,761 observations (the full cloud-scoreable population from `prepared/`). Remaining ~942 studies in `prepared/` either have zero scoreable observations or weren't included in this run; needs an audit before Pass C-equivalent scoring is extended.
- [ ] Audit which of the remaining ~942 studies have any scoreable observations under the v4 filter; if material, run an extension pass.
- [ ] Re-emit `v_top_prescient_studies`, `v_low_confidence_prescience`, and decade-level prescience views after any extension passes complete (Phases 1+2).

### 3. Cloud-LLM confidence sweep — partly superseded

- [ ] Original ask was a second-opinion pass on `confidence=1` obs from local Pass C. Today's cloud run effectively absorbed this: sonar-reasoning-pro is the primary scorer; the 100-obs claude-sonnet-4.6 pilot is the cross-model spot-check. Compute inter-model agreement on those 100 obs as a v1.6 deliverable (`_master_prescience_scores.csv` has `model` and `confidence` per row).
- [ ] 11 cloud-Pass-C failures (`logs/pass_c_cloud_v1_failures.jsonl`, all JSONDecodeError after 3 retries) — retry in a v6 retry script (see §15).
- [ ] Wire `kw_ask.py --cloud` properly (currently stubbed in v4) — moved to v1.7 §12.

### 4. Fill the 350 missing `pub_year` values — ✅ SHIPPED 2026-05-27

Closed via v6 backfill (350 rows) + v6.1 corrections (4 rows). All 1434 studies now have `pub_year` set, all within [1970, 2026]. See `_decisions_log.md` 2026-05-27 entry. Three follow-on items captured below (items 4a, 4b, 4c).

### 4a. Fix the pub_year date parser in `01_load_csvs_v2.py`

The v6 backfill was needed because Phase 1's parser silently dropped values it couldn't recognize. Two failure modes:

- [ ] Plain-English date strings in `_master_studies.csv`'s `date` column fail to parse (`June 2001`, `November 2006`, `May 1997`, `April 13, 2004`). Add a `dateutil.parser.parse(value, fuzzy=True)` fallback with a [1970, 2026] range sanity check.
- [ ] `f-4q04-*` filename patterns (the Aberdeen "fast" research format) aren't recognized by the qcode extractor. Extend regex to match `f-?[1-4]q\d{2}` in addition to the current `[1-4]q\d{2}`.
- [ ] Acceptance: unit test covering all four plain-English forms + an `f-4q04-...` filename, plus Phase 1 logs `1434/1434 resolved; 0 missing` against current masters.

Full spec in `future_work_v1.6.md` §1.

### 4b. Full filename-vs-text year audit ("choice b" from v6 review)

v6.1 caught 4 misparses outside the [1970, 2026] range (1904, 1905×2, 2030). Silent misparses **inside** that range remain undetected — the v2 extractor's earliest-year-in-raw-text rule can be fooled by OCR artifacts, page numbers, copyright footer years, or quoted historical years.

- [ ] For every study whose `study_id` contains a qcode or MMDDYY pattern, derive the filename-implied year independently and compare against `pub_year`. Flag disagreements > 1 year.
- [ ] Emit `pub_year_audit_v1.csv` (study_id, filename_year, text_pub_year, delta, sample_filename_pattern).
- [ ] Pete reviews flagged rows; corrections applied via `apply_pub_year_v6_2.py` (same dry-run / `--commit` pattern).

Full spec in `future_work_v1.6.md` §2.

### 4c. Fix the `v_studies_by_decade` view — ✅ SHIPPED 2026-05-29 (`02_build_data_layer_v3.py`)

View was returning 38 rows because pub_year is stored as DOUBLE in studies.parquet (pandas float64 when nulls present). The v2 expression `CAST(pub_year / 10 * 10 AS INTEGER)` performed DOUBLE math (1997.0 → 199.7 → 1997.0) and the cast only truncated at the end, yielding 1997 → '1997s'. **Same bug existed in `v_prescience_by_decade` — fixed in the same patch.**

- [x] Patched both views in `02_build_data_layer_v3.py`: `((CAST(pub_year AS INTEGER) / 10) * 10) || 's' AS decade` — cast FIRST so DuckDB integer arithmetic buckets correctly.
- [x] Shipped to `shorttack/aberdeen-group-archive/scripts/build/02_build_data_layer_v3.py` (sha `da1e7345`).
- [ ] **Pete action**: `git pull && cp scripts/build/02_build_data_layer_v3.py ~/Desktop/Archive/scripts/` then re-run Phase 2 to refresh DuckDB. Expected: `v_studies_by_decade` returns 6 rows (1970s..2020s), `v_prescience_by_decade` returns matching shape. **Carry-forward note**: today's Phase 2 ran with the v2 script; the 38-decade bug persisted in the post-rebuild shape audit.
- [ ] After Pete re-runs Phase 2: audit `wiki/decades/*.md` and any `kw ask` decade prompts for downstream impact (deferred to v1.6).

Full spec in `future_work_v1.6.md` §3.

### 5. The 1,890 zero-occurrence entities + 1,323 zero-occurrence technologies

Many are legacy catalog rows the build never linked to observations. Two paths:
- [ ] **Audit**: spot-check a sample (50 entities, 50 techs) to determine whether these are (a) genuinely orphaned catalog entries from the v0 schema migration or (b) entities/techs that should have been linked during ingest but were missed.
- [ ] **Decision**: either link them retrospectively (cheap-but-tedious) or mark them `status: catalog-only` in the masters and exclude from the default Dataview/DuckDB views (cheap-and-honest).

### 6. Permanent Notes workflow (`kw_note.py`) — ✅ v1 shipped, ✅ v2 bug-fixed, in v1.5 expansion

Pete's standing TODO, reminded 2026-05-28: "we have a to_do to create a script that takes KW output and creates new Wiki pages or updates to existing pages. That's how the corpus grows with new insights."

Shipped (2026-05-28 / 2026-05-29):
- [x] Ship `scripts/kw_note.py` — parses `kw ask` output, emits a scaffolded permanent note (slug, frontmatter, citations, body) — **v1 commit `43baa07e`, v2 commit `8218f1d5`, v4 commit `20e9143c`**
- [x] Create `wiki/notes/` subdirectory in the canonical wiki — created on first `--commit`
- [x] Add `kw note` subcommand to `bin/kw` (delegates to `kw_note.py`) — **bin/kw v2 shipped in `43baa07e`**
- [x] Extend `kw_ask.py` with `--no-notes` / `--only-notes` / `--type` filters so a query can be scoped to archive-only, notes-only, or one page type — **kw_ask v5 shipped in `43baa07e`, v7 in `b5a899ca`**
- [x] USER_GUIDE.md §6.6 walkthrough — **shipped in commit `8218f1d5` (USER_GUIDE.md 1239 → 1492 lines)**

Deferred to v1.5+:
- [ ] `kw note --promote <slug>` — elevate a note into a first-class `wiki/studies/` page with prescience/importance/relevance scoring and `_master_studies.csv` row generation
- [ ] `kw --help` overhaul — full subcommand catalog, per-subcommand help routing, auto-sync flag lists, `kw help <subcommand>` convenience
- [ ] `~/.kw/identity.yaml` for default author + signing (no more `--author pete` on every invocation)
- [ ] Multi-author CONTRIBUTING.md + CI lint (frontmatter required fields) + contact path for Bill Wallet and future contributors
- [ ] Dictation polish pass + wikilink proposal pass + batch review pass (`kw note --review <slug>`)
- [ ] Re-run wikilink rewriter on `--append` bodies (v1 limitation: only the initial body gets `[slug]` → `[[slug]]` rewriting)
- [ ] Auto-bump `kw note --version` from `__doc__` string so the footer credit stays in sync

### 7. Update the Kastner Technology Breadth Memoir with v1.5.1 metrics (AI-assisted)

The memoir page (`study-kastner-technology-breadth-memoir-2026.md`) currently cites v1.4 numbers (915 studies / 2537 techs / 479 domains / 4628 mentions). Refresh against current shape audit (1434 studies / 4312 techs / etc.). Diff-review pattern: AI proposes the prose update; Pete approves before commit. See WORKLIST §11 for the broader content-drift refresh.

### 8. Canonical layout migration cleanup

Shipped 2026-05-28: canonical wiki moved to `~/Repos/kastner-aberdeen-wiki/`. Cleanup tasks:

- [ ] After 2026-06-04 (one-week grace window), rename `~/Desktop/kastner_wiki/` to `.DEPRECATED_20260528/` on Pete's Mac. **Reminder 2026-05-30**: today's Phase 1+2 ran against `~/Desktop/kastner_wiki/`, which is exactly the divergence the canonical layout decision was meant to prevent. v1.6 §11 will re-run against `~/Repos/`; the rename can proceed once that's done.
- [x] Audit `~/Desktop/Archive/scripts/*.py` for any hardcoded paths to `~/Desktop/kastner_wiki/`; patch to use `--wiki` argument — **completed 2026-05-29: no real findings**.
- [x] Audit `~/Repos/kastner-aberdeen-wiki/scripts/*.py` for any sandbox-path leftovers — **completed 2026-05-29**. Moved three one-shot scripts to `scripts/_legacy/` (wiki commit `eda7bf35`).
- [x] Patch `kastner-archive-pipeline` skill to v1.2 — ✅ DONE in 2026-05-28 session.

### 9. Schema contract enforcement

The kw_ask BinderException after Phase 5 was avoidable. Add:

- [ ] `scripts/verify.py` step that opens `data/embeddings.parquet` and asserts the column list matches what `kw_ask.py` expects. Fails loudly if not.
- [ ] Mirror assertion at the top of `kw_ask.py` so any kw user gets a readable error, not a DuckDB BinderException.
- [ ] Add to `kw verify` so the launcher catches it before the user does.

### 9a. Embeddings / pages_manifest hygiene (discovered 2026-05-28 via kw_note v3)

_(Unchanged from 2026-05-29 worklist — three issues — see prior worklist text. No new work today.)_

### 9b. kw_note CLI/UX cleanup — ✅ SHIPPED 2026-05-29 (`kw_note v4`, wiki commit `20e9143c`)

_(Unchanged. Open follow-up: live-exercise `--overwrite` and `--git-commit` paths on Pete's Mac next session.)_

### 10. Tier-1 LLM regen for the 459 deferred pages

Phase 3 ran with `--skip-llm` after the first attempt hung on the tier-1 LLM. ~459 study pages had their tier-1 LLM summary at the prior version.

- [x] **Partial resolution 2026-05-30**: today's Phase 3 (full run, no `--skip-llm`) refreshed tier-1 for 124 high-prescience studies + 200 entities + 150 techs.
- [ ] Hang did not recur today. Diagnose remained-tier-1-eligible page set: which pages still carry stale tier-1 summaries from pre-2026-05-29 builds? Spec: identify any tier-1-eligible page whose `last_tier1_regen` < today's Phase 3 timestamp.

### 11. Refresh five v1.4-narrative pages with v1.5.1 metrics (content-drift refresh)

_(Unchanged from prior worklist — five pages. The prescience-related narrative pages (e.g., `study-2026-kastner-prescience-methodology-demo-0cdf48`, `wiki/themes/kastner-prescience-market-rollup.md`) now have NEW stale numbers as of today's rollup — they previously said 933 high-prescience-derived; the post-rollup canonical is 489 operational / 124 evidence-derived. Bake into the §11 refresh.)_

---

## v1.6 candidates added 2026-05-30 (Pass C cloud session)

### 11a. Re-run Phase 1+2 against canonical wiki (`~/Repos/kastner-aberdeen-wiki/`)

Today's Phase 1+2 rebuild ran against `~/Desktop/kastner_wiki/` (the deprecated path). The canonical layout decision (2026-05-28) names `~/Repos/kastner-aberdeen-wiki/` as the live working wiki. Until the canonical DuckDB is rebuilt, Pete's `kw ask` queries against `~/Repos/` return pre-Pass-C answers.

- [ ] Re-run `01_load_csvs_v2.py --archive ~/Desktop/Archive/archive_masters --wiki ~/Repos/kastner-aberdeen-wiki` and `02_build_data_layer_v2.py --wiki ~/Repos/kastner-aberdeen-wiki`.
- [ ] Confirm shape audit against `~/Repos/.../db/kastner.duckdb` matches today's `~/Desktop/kastner_wiki/db/kastner.duckdb` shape (124 high-prescience-evidence; 489 high-operational; 492 with prescience scores).
- [ ] Re-run Phases 3-6 against `~/Repos/` and commit the resulting wiki snapshot to `shorttack/kastner-aberdeen-wiki`.

### 11b. Complete Phases 3-6 (vault, indices, embeddings, scaffolding)

In-flight when session ended 2026-05-30 PM.

- [ ] Phase 3 (`03_generate_vault_v2.py`) — tier-1 regen for 124 studies + 200 entities + 150 techs. Started 17:47 EDT; expected ~30-90 min for entity + tech tier-1 generation; small final flush. Pete to confirm completion when he returns this evening.
- [ ] Phase 4 (`04_generate_indices_v2.py`) — indices, Bases, Dataview. <30 sec.
- [ ] Phase 5 (`05_compute_embeddings_v2.py`) — re-embed with bge-m3:latest. ~17 min. **Critical**: do NOT run against `~/Desktop/kastner_wiki/` (iCloud trap). If running today's wiki forward, mitigate per `kastner-archive-pipeline` Workflow C Step 5; or defer until §11a relocates to `~/Repos/`.
- [ ] Phase 6 (`06_emit_scaffolding_v1.py`) — refresh README, AGENTS.md, chat-starter.md with new counts (489 high / 492 scored / 124 evidence-derived). <30 sec.
- [ ] After Phase 6: validate `kw ask "what is the shape of the Kastner archive"` returns the updated counts (Gotcha 7 check).

### 11c. Hand-spot-check the 18 new "high"-prescience studies (small-n cohort)

Today's Rule A rollup promoted 18 studies into `high` based on max_used=3 observations each. Small-n cohort is potentially overweighted by single strong predictions; worth a hand audit.

- [ ] Pull the 18 from `_rollup_v3_audit_20260530T212525Z.csv` where `new_prescience='high' AND n_used <= 3`.
- [ ] Pete reads each study's predicted text + actual outcome; confirms or downgrades.
- [ ] Candidate gems list output: feeds the lessons-learned blog content (cross-ref WORKLIST §17).

### 11d. Identify the 1 remaining `[DEFERRED]` study + the 1 `NULL`-prescience study

Post-rollup distribution shows 1 [DEFERRED] and 1 NULL remain. Likely the [DEFERRED] was filtered out earlier in Pass A/B and never made it to Pass C; the NULL is probably an even older import artifact. Worth resolving so the studies-master enum is clean.

- [ ] Query: `SELECT study_id, title, prescience FROM v_studies WHERE prescience IN ('[DEFERRED]', '') OR prescience IS NULL;`
- [ ] For each, determine why it lacks a score, and assign or set `not-applicable` with rationale.

### 11e. Retry 11 failed Pass C observations

`logs/pass_c_cloud_v1_failures.jsonl` preserves the 11 JSONDecodeError failures (all returned `"raw":""` after 3 retries).

- [ ] Script: `retry_pass_c_failures_v1.py` — reads failures.jsonl, re-calls sonar-reasoning-pro with bumped retry count + slight prompt-template tweak (add explicit "respond ONLY with valid JSON").
- [ ] Merge results into `_master_prescience_scores.csv` (delta only).
- [ ] If any new scores affect their parent study's Rule A rollup, re-apply `roll_up_prescience_v3.py` for the affected study_ids.

### 11f. Commit operating profile to `aberdeen-group-archive/OPERATING_PROFILE.md`

Pete delivered a long-form operating-profile prompt mid-session 2026-05-30 codifying durable working relationship rules (peer-vs-engineer framing, CSV-as-truth, durability, posture, plan-first protocol, destructive-op safeguards, single-question cadence). Committing a copy to the repo makes the framing durable beyond agent memory.

- [ ] Draft `OPERATING_PROFILE.md` lifted verbatim from Pete's prompt + short preamble noting provenance.
- [ ] Decide whether to fold into `AGENTS.md` or keep as a separate doc. Likely separate; `AGENTS.md` is the canonical entry point and should link to it.
- [ ] Ship in next EOD batch commit.

### 11g. Update `kastner-archive-pipeline` skill baseline (109 → 124)

The skill's "Expected baseline as of 2026-05-27" block still cites `high_prescience_studies: 109`. Today's rebuild raised that to 124 (obs-evidence-derived). Bump the baseline and add a one-paragraph note explaining the two-layer prescience schema (operational study-level `prescience` vs. evidence-derived `v_studies_with_high_prescience`).

- [ ] Patch skill to v1.3 in the next pipeline-touching session.

### 11h. Update `readme_prescience.md` with §8 evidence-layer subsection

`readme_prescience.md` documents the operational study-level prescience. Today added an evidence layer (`_master_prescience_scores.csv`) that the doc doesn't mention.

- [ ] Append §8 "Per-observation evidence layer" with schema (11 columns), Rule A specification (templated rationale), and the principle that researchers can derive their own rule via `roll_up_prescience_v*.py`.
- [ ] Ship in next EOD batch commit to `shorttack/aberdeen-group-archive`.

### 11i. Fix `datetime.utcnow()` deprecation in `roll_up_prescience_v3.py`

Cosmetic. `datetime.utcnow()` is deprecated in Python 3.12+; replace with `datetime.now(datetime.UTC)`. Batch with the next pipeline edit.

- [ ] Bump to `roll_up_prescience_v4.py`. Behavior unchanged.

---

## v1.7 candidates

### 12. Cloud provider wiring for `kw_ask.py`

Currently `--cloud` exits cleanly with a "not available" message (v4 carries forward v3's stub). Wire one provider — Gemini free tier is the lowest-cost entry point. Patches:
- [ ] `kw_ask.py` v5: `--cloud` calls Gemini via `requests`, reads `GEMINI_API_KEY` from env
- [ ] USER_GUIDE.md §6.5: lift the "reserved" caveat, document setup
- [ ] Decisions log entry

### 13. Incremental embeddings

`scripts/05_compute_embeddings_v2.py` walks every `wiki/**/*.md` on every run (~17 min with bge-m3:latest). For routine updates (one new stub page, one corrected fact) this is overkill.
- [ ] Patch `05_compute_embeddings_v2.py` to support `--incremental`: check page mtimes against `embeddings.parquet`'s build timestamp, re-embed only the delta
- [ ] Add `kw rebuild-embeddings --incremental` as the launcher default; full re-embed via `--full`

### 14. Memoir Volume 2 ingest

Volume 1 chapter pages shipped in v1.5.1 + v1.5.2. If/when Pete writes or finalizes Volume 2:
- [ ] Add `wiki/volume-2/` directory + per-chapter pages
- [ ] Extend the themes taxonomy if new themes emerge
- [ ] Update `_collection_stats.csv`

### 15. Patent / IP corpus

Pete's archive interests include patent strategy. Consider a parallel `wiki/patents/` directory if patent docs become part of the corpus.

---

## v1.8+ / strategic

### 16. Public release strategy

- [ ] Decide what (if anything) of `kastner-restricted-sources` ever moves to public. Most-likely candidates: anything older than ~30 years where copyright posture is benign.
- [ ] Add a `LICENSE_REVIEW.md` to the archive that tracks copyright status per source.

### 17. Adoptex × Aberdeen archive cross-pollination

The Aberdeen archive's prescience scoring methodology could feed Adoptex's AI-adoption-readiness frameworks. Possible deliverables:
- [ ] A "what Aberdeen got right about technology adoption curves 1988-2008" report — methodology blueprint for Adoptex's broadband ISP work. **2026-05-30 input**: today's Rule A rollup now gives a clean, reproducible high/medium/low signal across 492 studies — this is the report's data spine.
- [ ] A LinkedIn series on prescient Aberdeen predictions (use the `linkedin-skill` for output)

### 18. Wider readership

- [ ] One-page "what is this archive" landing page on a custom domain (kastner-research.com or similar) that links to both repos and explains the methodology to non-Aberdeen readers
- [ ] Submit a writeup to one analyst-history-focused outlet (no obvious target — Tech History Cafe, longreads, IEEE Annals of the History of Computing all candidates)

### 19. KW Console — web GUI for `kw ask` + `kw note` with dictation (proposed 2026-05-28)

_(Unchanged from prior worklist. v1 scope ~700 LOC; FastAPI + plain HTML/JS, localhost only, Web Speech in v1 then Whisper-on-Ollama in v1.1. Audience: shared tool on GitHub for all future researchers.)_

---

## Maintenance / hygiene (low-priority but evergreen)

- [ ] Quarterly self-test: `kw verify` + spot-check 5 random `kw ask` queries against ground truth
- [ ] Annual master CSV re-validation: re-run `archival-ingest` Pass A on a random 5% sample of studies, verify schema integrity
- [ ] Annual review of `_decisions_log.md`: prune duplicate decisions, tag entries by version
- [ ] Watch for new "missing source" candidates as queries expose them

---

## Not on the list / explicitly deferred

- **Cloud-only RAG service** — no plan to host this anywhere. Local-first is the design.
- **Multi-user wiki editing** — single-author archive by design (but multi-author identity layer for permanent notes IS on the list — see §6).
- **Mobile app / web UI** — Obsidian is the UI. No additional frontend (except KW Console localhost in §19).
- **Real-time data integration** — this is a historical archive. Pinning it to a static snapshot is the point.

---

## Done this session (2026-05-30 PM — Pass C cloud)

_(End-of-day commit clears this section)_

### Pass C cloud-scoring run completed (2026-05-30 PM)

- **Cloud scoring run completed across 3,761 observations / 492 studies.** Models: `sonar-reasoning-pro` (3,661 obs) + `claude-sonnet-4.6` (100 obs cross-model pilot). Score distribution: -1 prefilter=795, 0=1,717, 1=8, 2=62, 3=349, 4=764, 5=66. Wall time ~14 hrs across two relaunches. API cost ~$24 of $49.99 monthly cap. 99.7% parse rate; 11 failures (JSONDecodeError, deferred to v1.6 §11e). Bimodal distribution (0s + 4s dominate) consistent across both models.
- **Canonical prescience architecture confirmed** mid-session via `readme_prescience.md` (root of `aberdeen-group-archive`, Peter S. Kastner, February 2026): operational study-level (`high`/`medium`/`low`/`not-applicable` in `_master_studies.csv`) + evidence-layer (`_master_observations.csv` viability-prediction + actual-outcome joined via `_prediction_outcome_links.csv`). Today's per-obs cloud-scoring artifact extends the evidence layer as a new first-class file `_master_prescience_scores.csv` (3,761 rows × 11 cols). Both layers are queryable; no production tables introduced.
- **Pete's science principle codified**: researchers must be able to take the public archive and derive their own prescience weights with their own aggregation rule, deterministically. `roll_up_prescience_v*.py` is the reference implementation; the evidence CSV is the input; forks are encouraged.
- **Rule A (mean-threshold rollup) adopted as canonical**: for each study, drop -1 prefilter scores; if no scores remain → `not-applicable`; mean ≥ 3.5 → `high`; mean ≥ 2.0 → `medium`; else → `low`. Rationale is deterministic templated text (mean, n_used, distribution). Confidence ignored (reserved for future Rule C).
- **`roll_up_prescience_v3.py` shipped** to `shorttack/aberdeen-group-archive/scripts/roll_up_prescience_v3.py` (sha `5b2e88cb`) via script-delivery protocol. 8434 bytes.
- **`_master_studies.csv` updated**: 369 [DEFERRED] studies resolved to 18 high / 54 medium / 200 low / 97 not-applicable. 1434 rows in / 1434 rows out; 16 cols preserved (QUOTE_ALL). Backup at `_master_studies.csv.bak_rollup_v3_20260530T212525Z`. Audit at `_rollup_v3_audit_20260530T212525Z.csv` (369 rows).
- **Studies-master post-rollup distribution**: high=489 (+18) / not-applicable=346 (+97) / medium=325 (+54) / low=272 (+200) / [DEFERRED]=1 (-369) / NULL=1.
- **Phase 1+2 rebuild against `~/Desktop/kastner_wiki/`** — clean. `_master_prescience_scores.csv` was already wired into `01_load_csvs_v2.py` (prior session laid the groundwork). 27 v_* views regenerated. `v_high_holistic_prescience: 489` matches studies-master exactly. `v_studies_with_high_prescience: 124` (was 109; +15 obs-evidence-derived). **Carry-forward**: Phase 1+2 against `~/Repos/` (canonical) deferred to v1.6 §11a.
- **Phase 3 in flight when session ended**: tier-1 regen for 124 studies + 200 entities + 150 techs. Started 17:47 EDT.
- **Shape audit before / after rebuild**: studies 1434 (unchanged), observations 23605 (unchanged), entities 3207 (unchanged), technologies 4312 (unchanged), pub_year-resolved 1434 (unchanged), decades_covered 38 (v_studies_by_decade bug carries forward — fixed in `02_build_data_layer_v3.py` but not yet pulled), high_prescience_studies 109 → 124 (+15).
- **Operating profile prompt received from Pete** mid-session and saved to memory across three categories (style, archive principles, naming/workflow rules). Backlog item §11f: commit a copy to `aberdeen-group-archive/OPERATING_PROFILE.md`.
- **Process lessons captured** (5 total) in today's `_decisions_log.md` entry — including the "read the canonical doc before architecting" lesson (would have prevented an early two-table proposal), the "Phase 1 was already wired" lesson (read pipeline scripts before adding masters), the science-principle artifact-classification lesson, the OPERATING_PROFILE provenance lesson, and the "bash pseudocode shouldn't look like bash" lesson (Python pseudo pasted into Pete's shell cascaded errors).
- **Decisions log entry drafted**: `decisions_log_entry_2026_05_30_pass_c_cloud_v1.md` (workspace; not yet committed). 225 lines; full session shape, both shape audits, all artifacts listed, lessons + backlog appended.
- **EOD batch commit pending Pete's go-ahead** — files staged in `commit_plan_2026_05_30_v1.md`.

---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._
