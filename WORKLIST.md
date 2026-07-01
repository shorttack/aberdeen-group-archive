# Kastner Aberdeen Archive — Active Worklist

> ## 🔴 BEFORE EDITING ANY MASTER CSV, ANY APPLY SCRIPT, OR ANY PIPELINE PHASE — READ `Perplexity_Only/`
>
> | file | when to read |
> |---|---|
> | [`Perplexity_Only/MASTERS_NOTES.md`](Perplexity_Only/MASTERS_NOTES.md) | Before any change to the 7 master CSVs. Schemas DIFFER from `archival-ingest` v20 per-study schemas. |
> | [`Perplexity_Only/CANONICAL_IDS.md`](Perplexity_Only/CANONICAL_IDS.md) | Before assigning any `entity_id` or `tech_id`. Contains the anti-pattern catalog (`att-corporation` → `ent-att`, `ibm-powerpc` → `powerpc`, etc.). |
> | [`Perplexity_Only/PIPELINE_QUICKREF.md`](Perplexity_Only/PIPELINE_QUICKREF.md) | Before running Phases 1-6 or writing an apply script. Includes the `//` integer-division fix for the shape audit. |
> | [`Perplexity_Only/OLLAMA_STATE.md`](Perplexity_Only/OLLAMA_STATE.md) | Before touching `_llm_helper_v4.py` or swapping any local model. |
>
> **Mac canonical:** `~/Desktop/Archive/Perplexity_Only/` — keep in sync with repo via `git pull`.
> **Most recent rewrite of MASTERS_NOTES:** 2026-06-12 §11u-cont Pass B (after the v1 apply-script crash). Assuming master schemas match per-study schemas has crashed apply scripts multiple times.

---

**Last updated:** 2026-07-01 EOD (embedding-upgrade-gates toolkit: 20 LOCKED probes + labeled gold set [198 rows / 151 relevant / 47 not] + two-part promotion gate [Recall@6 +0.05 margin AND per-query ≤1-hit no-regression floor]. First candidate — qwen3-embedding:8b MRL-1024 vs bge-m3 incumbent — **FAILS BOTH GATES → KEEP INCUMBENT** [Recall@6 0.586 vs 0.685, delta −0.100; 4 per-query regressions incl. prescience category-collapse Q11 −5 / Q14 −2]. Live index `data/embeddings.parquet` (bge-m3) UNTOUCHED. Toolkit shipped to BOTH `Archive/tools/` [public, light-touch] AND `Perplexity_Only/` [ops originals] with baseline record. Prior stamp: 2026-06-30 EOD-2 (model-eval scouting session: Track A qwen3.6:27b dense = NO-GO at Gate 2; Track B Sonar-replacement run-pack drafted but NOT shipped; kw_ask local-model scout = incumbent qwen3.5:27b-mlx stays, Gemma 3/4 27-31B is the only fixture-worthy candidate. ALL artifacts held in workspace, nothing committed. Prior stamp: v2.0 release: full-corpus 3y/5y SH prescience + v9 confab fix + PC Deals per-SKU journeys; SH master 17,030 rows / 792 verdict studies; live DuckDB 1504/24842/3293/4376/876; all four v2.0 docs written; wiki pushed; archive push handed to Pete)
**Current ship state:** **v2.0 — archive push PENDING (Pete runs on Mac).** Wiki `shorttack/kastner-aberdeen-wiki` PUSHED this session: main `3a992434..93499d11` (1623 files, 11459 ins / 524 del; embeddings.parquet 66 MB; README v1.6→v2.0-rebuild content; SH parquets present). Live DuckDB shape (post-SH Phase 1 v3 + Phase 2 v5 rebuild): **1504 studies / 24842 observations / 3293 entities / 4376 techs / 1504 pub_year / 6 decades / 876 high-prescience** (`v_studies_with_high_prescience` = `prescience_max ≥ 4` = 876; authored enum high = 503; mean≥3.5 = 88). SH: `v_prescience_sh` = 17,030; `v_studies_with_sh_verdicts` = 792 (3y 522H/264M/4L/1na/1pend; 5y 518H/268M/4L/1na/1pend). Prior archive `origin/main` at `ce3262f3` (Pass B masters merge); tag `v1.9.0` (2026-06-22) latest released. bge-m3 (1024-dim) re-embed of 10,862 pages (Phase 5). **Security:** git `user.name` was "Catalina" (one of Pete's passwords); leak found 2026-06-01 PM, rotated to `shorttack`; historical commits retain dead-string "Catalina" in Author metadata.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

### 2026-06-24 PM focus

- First concrete action: create `~/Repos/mac_mcp_bridge/` Phase 0 scaffold outside iCloud, with FastMCP project skeleton, README, and read-only scope only.
- Keep the existing v1.8.0/v1.9.0 backlog intact; do not close or reorder historical carry-forward items during setup.
- After Pete confirms, begin with the Mac MCP Bridge scaffold before moving to lower-priority cleanup items.

- [x] **v1.9.0 GitHub Release tags + release notes on both repos** — DONE 2026-06-22 PM. Version bumped v1.8.0 → v1.9.0 (skipping untagged v1.8.0 number); combined release notes cover v1.8.0 substrate silent-loss recovery (1087→1208 rows; F4 substrate-cap finding) + CompChem 1989 exemplar (first study under new top-level `project_examples/` path). Archive: tag `v1.9.0` on `a02c23f1`, [release shipped](https://github.com/shorttack/aberdeen-group-archive/releases/tag/v1.9.0). Wiki: tag `v1.9.0` on `e018d1f1`, [release shipped](https://github.com/shorttack/kastner-aberdeen-wiki/releases/tag/v1.9.0). Both done via Mac `gh release create` with pre-staged `RELEASE_NOTES_v1_9_0.md`. Branch-protection bypass warnings flagged for future commit-signing setup.
- [x] **Mac MCP Bridge — Phase 0 + Phase 1 + remote connector** — DONE 2026-06-27 (Phase 0/1 scaffold 2026-06-24; remote HTTP connector LIVE 2026-06-26/27, see Done-this-session). Connector "Perplexity bridge v2" CONNECTED at `https://dolphin-washer-slush.ngrok-free.dev/mcp`; `v_studies`=1454 verified from chat. ORIGINAL APPROVAL 2026-06-20 PM, see `docs/mac_mcp_bridge_architecture_v1.md` + `docs/promoted_mac.md`). Stub `mac_mcp_bridge/` directory in `~/Repos/` (NOT under `~/Desktop/` — iCloud trap). FastMCP scaffolding, `pyproject.toml`, README. Read-only scope, no local LLM. Phase 1 follows: `duckdb_query` / `duckdb_tables` / `duckdb_describe` against `~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb`. Full architecture + 6-tool surface + Phase 0–6 sequence already committed at `976bc833`.
- [x] **v1.8.0 — `route_quotations_to_horizon_v2.py`** DONE 2026-06-19 AM-3 (commit `56cc4622`). v1 shipped but produced 217 P1 only (Gotcha-9: stored corpus `headline_norm` field diverged from live `normalize_text(headline)` on 220 articles — dashes/slashes/commas). v2 recomputes the corpus norm at routing time from each article's `headline`; produces 474 P1 / 230 routed initially. After horizon backfill of 244 blank cells (commit `c38ff792`, see below), v2 re-run yields **474/474 routed, 292 tuples, 220 scorable after prefilter_skip removal**. Tuple distribution: prefilter_skip=72, SH-3y=186, SH-5y=26, LH=8. 10 admit-orphans triaged separately (Q1). Future v1.8.x scripts should read this script's output rather than re-derive horizon routing.
- [x] **v1.8.0 — `score_quotations_calibration_v1.py` A/B harness** — DONE 2026-06-19 PM (§11w). v1 shipped `31cd0a18` then v2 SSL fix shipped `e9818055` (certifi.where(); v1 hit `[SSL: CERTIFICATE_VERIFY_FAILED]` on all 300/300 calls). 150 rows × P1+P2 = 300 calls × ~$0.05 = ~$15, ~85 min. **Bucket agreement (Rule A): 119/144 = 82.6%.** Verdict: **P2 (quote-only) chosen as default for full corpus, with P1 as tiebreaker only on uncertain mediums (P2_bucket='medium' AND P2_confidence≤2 AND parse_ok).** Epistemic-honesty finding: P2 systematically downgrades generic-characterization quotes that P1 over-credits via article-context confabulation. Decisions log entry: `decisions_log_entry_2026_06_19_v1_8_0_calibration_p2_default_v1.md` (workspace, pending EOD).
- [x] **v1.8.0 — `score_quotations_corpus_v1.py` full-corpus scorer** — DONE 2026-06-19 PM (§11x). Shipped `f88107bf`. Phase A (P2 default) → Phase B (P1 tiebreak on uncertain medium) → Phase C (resolver). 383 calls, ~$19, ~95 min. **Final n=334: high 184 (55.1%), medium 84 (25.1%), low 66 (19.8%), parse_fail 0, human_review 0.** Tiebreakers: 42 invoked (12.6%), P1 changed verdict on 12/42 = 28.6%. Pipeline mix: P2=322, P1_tiebreak=12. Outputs at `kastner-author/quotations/quotations_corpus_v1.{csv,jsonl,_report.md}`. Decisions log entry: `decisions_log_entry_2026_06_19_v1_8_0_corpus_complete_v1.md` (workspace, pending EOD). **Cumulative v1.8.0 spend: ~$34 of $500 ceiling.**
- [x] **v1.8.0 NEXT — `promote_quotations_to_master_v1.py`** — DONE 2026-06-19 PM (§11x). Path β chosen (sidecar master `_master_quotations_prescience.csv` at repo root, 334×31, 4 audit cols: `blog_scrape_contamination_flag`/`scorer_version`/`source_pass`/`promoted_at`). Shipped at `3e4c1b66` after v1→v2→v3 predicate iteration (v1 false-positives on short legit quotes; v2 mis-named `low_signal_flag` conflating text-vs-verdict; v3 renamed to honest `blog_scrape_contamination_flag` audit signal — 11 rows flagged). Promote scripts v1 `464f104b`, v2 `48483679`, v3 `3c396807` (canonical).
- [x] **v1.8.0 NEXT — quotations corpus → wiki retrievability** — DONE 2026-06-19 PM (§11x). After monolithic 377 KB single-page approach failed retrieval (bge-m3 8192-token effective context produced "methodology centroid" embedding), per-quote chunking shipped: 334 individual `wiki/quotations/quote-<row_id>.md` pages + slim index page at `wiki/methodology/quotations_corpus_v1.md`. Script: `build_quotations_per_quote_v1.py` (`6918d6e0`, canonical). Phase 1+2+4+5+6 rebuild GREEN (Phase 3 skipped); Phase 5 v2 run 20.3 min over 10,774 pages. `kw ask` retrieval verified on Oracle/IBM/Itanium queries — quote pages surface as top hits, default k=6 retrieves quotes+context, `--k 15` mixes quote + tech-page + study evidence cleanly.
- [ ] **v1.8.0 BACKLOG — `clean_blog_artifacts_from_quotes_v1.py`** (raised 2026-06-19 PM §11x; PARTIAL 2026-06-24). 11 rows in `_master_quotations_prescience.csv` were flagged with `blog_scrape_contamination_flag=true`: footer text / share-button text / `Posted by anonymous` artifacts mixed into otherwise-substantive prescient predictions. Pattern set: `posted by anonymous`, `email thisblogthis`, `share to twitter`, `share to facebook`, `share to pinterest`, `blogging at`, `oncomputerstips`, `blog at oncomputers`, `no comments:`. **Critical: contamination is about TEXT quality, NOT verdict quality.** Affected row_ids: 1180, 1183, 1186, 1187, 1188, 1190, 1193, 1194, 1199, 1200, 1208. 2026-06-24 partial action: generated review report `Perplexity_Only/blog_artifact_cleaning_candidates_v2.csv`; Pete approved applying only the 5 clean auto-strip rows; `apply_blog_artifact_cleaning_auto5_v1.py --commit` updated quote text and set `blog_scrape_contamination_flag=false` for rows 1183, 1188, 1190, 1194, 1200; backup `_master_quotations_prescience.csv.bak_blog_artifact_auto5_20260624T195430Z`; audit `Perplexity_Only/blog_artifact_cleaning_apply_auto5_v1_audit_20260624T195430Z.csv`; row count preserved at 334; column count preserved at 31. Remaining manual-review row_ids still flagged true: 1180, 1186, 1187, 1193, 1199, 1208. Derived wiki quotation pages regenerated from the updated sidecar via `python3 scripts/build_quotations_per_quote_v1.py --commit`: 334 per-quote pages plus `wiki/methodology/quotations_corpus_v1.md`; builder reports 6 contaminated rows flagged, matching the remaining manual-review set. Phase 5 embeddings refreshed after page regeneration: `data/embeddings.parquet` written with 10803 rows. Deferred disposition: decide whether to hand-edit/reconstruct the six fragment/bio rows and whether to re-score any changed rows via the v1.8.0 corpus scorer.
- [ ] **v1.8.0 BACKLOG — `_master_studies.csv` row delta 1452→1453** (raised 2026-06-19 PM §11x). Phase 1 reported 1453 studies — one above the §11u-cont baseline. Possibly a Pete-added study from earlier this afternoon outside this thread, or a stray row from a prior session that didn't make the §11u-cont audit. Quick reconcile: `duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "SELECT study_id, title, created_at FROM v_studies ORDER BY created_at DESC LIMIT 5;"`. <10 min.
- [ ] **v1.8.0 BACKLOG — `v_studies_with_high_prescience` count 124→865 investigation** (raised 2026-06-19 PM §11x). The view returned 865 rows at Phase 2; baseline in kastner-archive-pipeline skill is 124-125 (post-Pass-B reconcile). Possible causes: view definition change to include Pass C scored obs that weren't in the prior baseline, merge with `high_holistic`, or rollup-level change. Not blocking v1.8.0 ship but flag for skill quickref update next session.
- [ ] **v1.8.0 BACKLOG — `kastner-archive-pipeline` skill update: kw ask + per-quote chunking + bge-m3 chunk-size rule** (raised 2026-06-19 PM §11x). Add Gotcha entry: "bge-m3 effective context is ~8192 tokens; embedding a multi-item dataset as a single page produces a smeared centroid that fails item-level retrieval. Canonical fix: per-item / per-claim chunking. Per-quote pages are the worked example (`build_quotations_per_quote_v1.py`, 2026-06-19)." Also document `kw ask --k N` flag in Quick command reference (default k=6 documented in `kw ask` output, real flag is `--k`).
- [ ] **v1.8.0 BACKLOG — quote-`<row_id>` slug convention documentation** (raised 2026-06-19 PM §11x). Per-quote wiki pages slug as `quote-<row_id>`. The numeric row_id correlates loosely with date (`quote-92` happens to be a 1992 prediction) but the slug is NOT year-based. Document the convention in `Perplexity_Only/CANONICAL_IDS.md` so future agents don't try to extract a year from a quote slug.
- [ ] **v1.8.0 BACKLOG — Phase B P1 parse-fail forensic** (carried from §11w). P1 tiebreaker parse-failed at 5/47 = 10.6% (rows 1146, 1173, 171, 1176, 84) vs Phase A P2 at 1.8%. All recovered via P2 fallback. Hypothesis: long article bodies trigger `<think>` blocks without closing tags or mid-stream truncation. Inspect `raw_response` field for these 5 JSONL records; if confirmed, add defensive `<think>` stripping for v2 of corpus scorer (also relevant to Pass C v6).
- [ ] **v1.8.0 BACKLOG — `datetime.utcnow()` deprecation in calibration v2** (carried from §11w; fixed in per-quote_v1 not yet ported back). Sister item to long-standing `roll_up_prescience_v3.py` and `apply_passb_reconcile_v2.py` deprecation items. Roll into the v3 apply-script template alongside Gate v1.1 pre-write validation.
- [ ] **v1.8.0 BACKLOG — 5-row tiebreaker spot-check** (carried from §11w). Manual review of tiebreaker-flipped rows: 731, 872, 873 medium→high; 933 medium→low. Sanity-check the resolver picked the right verdict on each.
- [ ] **v1.8.0 ORIG ITEM (now CLOSED, kept for context) — calibration A/B scoping note** (raised 2026-06-19 AM; **unblocked AM-3** with 220 scorable tuples & Q1 triage closed). 170-row highlight-reel calibration A/B harness. Source: `kastner-author/quotations/highlight_reel.md` (18KB, already in repo from May 23). Selects ~170 rows that are BOTH in `article_corpus_v1.json` (Pipeline 1 eligible, via `route_v2` output) AND have analyst-authored `prescience_score` truth in the CSV. Scores each row via both pipelines: (P1) full article body through horizon-routed prompt; (P2) `kastner_quotation + immediate_context` through the same horizon-routed prompt. Emits `calibration_ab_v1.csv` with per-row both verdicts + bucket-agreement metric (Rule A: ≥3.5 high, ≥2.0 medium, else low; agreement = both pipelines produced the same horizon bucket). If agreement ≥ 80%, Pipeline 2 is the cheaper default; if < 80%, Pipeline 1 wins by signal. Output also writes a Rule-A disagreement breakdown report. Cost est: ~170 × 2 scorers × ~$0.05 ≈ $17, well under $500 ceiling. Defer the full corpus scoring until this calibration result is in hand.
- [ ] **v1.8.0 BACKLOG — A-class admit-orphan recovery** (raised 2026-06-19 AM-3 from Q1 triage). 2 P1-admitted rows whose article body is absent from `article_corpus_v1.json`: rid 494 "IBM Lands Navy Supercomputer Deal" and rid 1005 "Dell, Oracle & Linux: Your Next SAP Platform?". Both present in raw PDF segments — the boundary detector dropped them during substrate build. Two recovery paths: (a) re-run substrate union with relaxed boundary heuristics targeting these 2 rids; (b) hand-author article stubs from segment text + commit to corpus JSON. Deferred — not blocking scorer; tuples scorable on quote text alone.
- [ ] **v1.8.0 BACKLOG — E-class admit-orphan documentation** (raised 2026-06-19 AM-3 from Q1 triage). 8 P1-admitted rows whose headlines are cited inside OTHER corpus articles' bodies (mentioned in narrative, standalone article never archived): rids 199, 374, 426, 458, 780, 1020, 1045, 1181. 7 of 8 also appear in raw RTF; rid 1181 "Sony Playstation" not even in RTF. Disposition: accept-as-cited; v1.8.0 scorer prompt does NOT require full article body, so these score on `kastner_quotation + immediate_context` alone. Document this class in v1.8.0 substrate trust manifest so future readers don't try to re-source.
- [ ] **v1.8.0 BACKLOG — Re-author 244 horizon-backfilled cells with real values** (raised 2026-06-19 AM-3). Backfill v2 plugged `3` (SH-3y default) into 244 P1-eligible blank `forecast_horizon_years` cells to unblock routing; sidecar audit at `kastner-author/quotations/_horizon_backfill_3y_v1_applied.txt` (20,481 B) lists every (rid, headline) pair. Real authoring should happen in batches — Pete reads quote + immediate_context, assigns real horizon. Scripted re-authoring tool can iterate the sidecar and prompt per row. Not blocking calibration (default-3 is a conservative SH-3y bias; calibration will surface if it skews verdicts).
- [x] **v1.7.0 Mac-side cutover** — DONE 2026-06-18 PM-3. F3 dry-run aborted with "column already exists" (prior Mac session had run an earlier F3 variant; 8,645 new Pass C rows landed with NULL `row_class` after that). F3b backfill drafted mid-cutover: `scripts/backfill_row_class_v1.py` 215 LOC, sandbox-simulated against Mac master fetched via `gh api .../git/blobs/<sha>` (master is 13.8MB, exceeds contents endpoint limit). Mac dry-run matched sandbox sim byte-for-byte; Pete locked Q1/Q2/Q3: `prefilter_skip` canonical (not `prefilter`), backfill all 8,645 NULL rows now, push through tonight. Mac `--commit` applied 8,649 mutations cleanly; backup `bak_backfill_row_class_20260618T222707Z`. Phase 1+2 GREEN; shape unchanged 1453/23926/3276/4361/865-high; prescience master 17,085 rows × 12 cols, zero NULL row_class. Commits: F3b script `730ac65f`, F3b cutover `bd819f4e`. Tag `v1.7.0` + GitHub Release shipped 22:37:52Z. Release ID 341674192. Branch-protection bypass warnings flagged for future signing setup. **v1.7.0 IS SHIPPED.**
- [ ] **`_master_observations.csv` 14-col schema migration audit** (raised 2026-06-18 PM-3 during cutover pre-commit). Pre-commit `git status` showed working-tree `_master_observations.csv` modified (`mtime` Jun 16 07:19, predates today): HEAD has 16 columns, Mac working tree has 30 columns. 14 unknown columns added, same 23,927 rows. Unshipped Mac-local migration of unknown provenance. **DEFERRED per D3 — production master moves require preauthorization.** Workflow when authorized: identify which session added the columns + read those columns' contents to determine intent + decide whether to ship, revert, or transform; ship in a standalone preauthorized commit (NOT bundled).
- [ ] **`kastner-archive-pipeline` skill update: detect-and-backfill mode for ship-gate scripts** (raised 2026-06-18 PM-3). F3 dry-run aborted with `sys.exit("Column '<col>' already exists. Aborting.")` instead of switching to backfill-of-new-rows mode. Capture as Workflow A enhancement: when column add is re-run and column already exists, detect partial-population state (header present + some NULL/missing values in newer rows) and offer a `--backfill` mode that fills the new rows without re-adding the header. F3b script is the canonical worked example. Update Workflow A Step 2 template.
- [ ] **`datetime.utcnow()` deprecation in `backfill_row_class_v1.py`** (raised 2026-06-18 PM-3). The script emitted Python 3.12+ `DeprecationWarning` on the backup-stamp line. Sister item to the long-standing `roll_up_prescience_v3.py` and `apply_passb_reconcile_v2.py` deprecation items. Roll into the v3 apply-script template alongside Gate v1.1 pre-write validation.
- [ ] **Junk file cleanup hardening — Phase 3-6 wrapper script quoting** (raised 2026-06-18 PM-3). Pre-commit `git status` surfaced 5 terminal-typo files created by broken `tee` redirects on the Mac: `--wiki`, `012`, `echo`, `python3`, `=== ALL PHASES COMPLETE ===`. Plus 5 similar orphans already in `logs/` (`phaseN_.log012`) and `"\012"` at repo root. Root cause: shell-escape mishandling in Phase 3-6 wrapper scripts. Fix: quote `tee` arguments properly; consider running `tee 2>&1` redirect inside a guarded wrapper that validates the output path is a single regular filename. Catalog the existing junk files for cleanup in next session.
- [ ] **Untracked work catalog** (raised 2026-06-18 PM-3). On Mac after cutover: 10+ files under `Perplexity_Only/` (SH calibration outputs), 10+ qwen kappa audit files under `scripts/`, an entire `scripts/v3_obsolete/` directory, and 5 `phaseN_.log012` orphans in `logs/`. Decide per-file: ship to repo, move to `_legacy/`, or delete. Probably one mid-session batch commit after the `_master_observations.csv` migration is resolved.
- [x] **2026-06-18 #1 — Regenerate methodology-demo against v1.6.2 corpus** — DONE 2026-06-18. Shipped as new slug `2026-kastner-prescience-methodology-demo-v2-0cdf49` (one-and-done, no in-place patch). 4 commits: archive `0a88d455` (source + add_methodology_demo_v2_study_row_v1.py), wiki `49f33d3f` (hand-authored page + patched RELEASE_NOTES_v1_6_2), archive `53fc748c` (surgical reembed_single_page_v1.py to fix Phase 5 race), archive `229843c4` (06_emit_scaffolding_v5.py — Phase 6 hardened against .gitignore clobber). Masters row 1452→1453 (D3 preauth). kw ask retrieves v2.0 at top (score 0.499). Shape: 1453/23926/3276/4361/865-high. Gotcha 13 candidate identified: Phase 5 reads file list at start; mid-flight git pulls race.
- [x] **2026-06-18 #2 — `.gitignore` patches for bycatch** — DONE 2026-06-18 AM. Archive commit `5c3f2f2d` (appended `*.bak_*`; `__pycache__/`+`*.pyc` already present). Wiki commit `9df154f4` (added `__pycache__/`+`*.pyc`+`*.pyo`+`*.bak_*` block; also removed the bycatch `study-2026-kastner-prescience-methodology-demo-0cdf48.md.bak_20260617T220304Z` from repo). Mac pulled clean on both repos; .bak file deleted from working tree by the pull. Total wall-clock: ~6 min.
- [ ] **2026-06-18 #3 — Git LFS migration plan for `data/embeddings.parquet`** (raised 2026-06-17 EOD). 63.41 MB at v1.6.2; exceeds GitHub's 50 MB soft limit (warning, not blocking — under 100 MB hard limit per §11u-cont closeout). Each future Phase 5 balloons repo. Plan: (a) install `git-lfs` on Mac if not present, (b) `git lfs track 'data/embeddings.parquet'`, (c) migrate history with `git lfs migrate import --include='data/embeddings.parquet' --everything` OR just track going forward without rewriting history (decision: rewriting history breaks tags v1.4/v1.6/v1.6.1/v1.6.2 — DEFAULT to track-going-forward), (d) verify Zenodo DOI minting still works against LFS-stored files, (e) ship at v1.6.3 or v1.7. Defer to after #1+#2.
- [~] **2026-06-18 #4 — Phase 6 template refresh** — PARTIALLY ADDRESSED 2026-06-18. Bumped to `06_emit_scaffolding_v5.py` (archive commit `229843c4`) with three fixes: (1) `.gitignore` template expanded from 3-line → 17-line with Python + `.bak_*` patterns + warning comment, (2) `LOCAL_MODEL` fallback corrected from stale `qwen3.6:27b-mlx` → `qwen3.5:27b-mlx`, (3) all script-name references bumped v2→v5; `--wiki` path corrected to `~/Repos/`. `.gitignore` specifically is now safe across reruns. README/AGENTS/chat-starter v1.6.2 vocabulary refresh still PENDING (Gotcha 8 mitigation incomplete for those three templates).
- [x] **§11v PRESCIENCE ARCHITECTURE AUDIT (D6)** — DONE 2026-06-18 PM. Architecture MAP shipped at `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` (archive commit `0f5c9d71`, 376 lines, 23,672 bytes). Companion to existing findings report at `Archive/decisions/prescience_architecture_audit_v1.md` (2026-06-15, F1-F10). MAP sections: (1) file inventory — 7 masters, 3-file Pass C arch, scripts, calibration artifacts, stray F1 items; (2) schemas — File 2 11-cols + 6 row classes, v_studies mapping; (3-4) Path A and Path B ASCII flow diagrams with Plaza canonical proof; (5) Rule A rollup math; (6) Phase 1 join contract + pass-through invariant; (7) **8 lag points L1-L8** with mitigations; (8) v1.7.0 cleanup map (F2/F3/F6/F7 = must-fix gates); (9) where-does-X-live quick-ref. **v1.7.0 ship gate reduced to four findings, all CLOSED in sandbox 2026-06-18 PM-2 (F2 `7935aec7`, F3+F6+F7 `5f945dd9`, docs rev `a6c7a007`).** Mac-side cutover pending next session.
- [x] **v1.7.0 Mac-side cutover** — DONE 2026-06-18 PM-3 (superseded by the [x] item above; this duplicate line raised 2026-06-18 PM-2 was closed by the same F3b commit `bd819f4e`).
- [ ] **v1.8.0 quotations corpus scoping** (raised 2026-06-19 AM). 1,087 quotes in `kastner-author/quotations/kastner_quotes_clean.csv` (18 cols, includes `is_predictive`, `prescience_score` under pre-v1.7.0 single-horizon enum, `prescience_rationale`, `forecast_horizon_years`, `accuracy_outcome`, `verdict_rationale`, `verdict_sources`). NOT loaded by Phase 1, NOT in wiki, NOT in embedding index — `kw ask` cannot retrieve them. Pete's overnight insight (2026-06-18 PM-3, last message before sleep): the long file containing every full article including the quotes may score materially differently from the isolated quote. **Three open architectural questions before any code/WORKLIST commit:** (Q1) **unit of prescience** — is the predictive claim the quote, the surrounding paragraph, or the whole article? Different answers produce different corpora and different page granularities; (Q2) **where does the long file live in the repo?** If under `kastner-author/` or `kastner-restricted-sources/`, a Pass B ingest path may already exist; if Mac-only, discovery is a prerequisite to v1.8.0 planning; (Q3) **calibration A/B on the 230-row highlight reel** — score both ways (quote-alone vs article-context-then-attribute-to-quote) and compare LH verdicts on the known-good subset before committing the full pipeline to one approach. Path A (full v1.7.0 multi-horizon: LH + SH-3y + SH-5y) is the chosen output format once Q1-Q3 resolve. Wiki output (per Pete 2026-06-18 PM-3): one `wiki/quotations/<row_id>-<slug>.md` per row with all 18 CSV columns as YAML frontmatter + bolded-header body so embedding picks up both label and value. Path A scoring expected ~2,174 LH+SH runs minus prefilter (`is_predictive=true` as gate, analyst-authored truth). Granularity decision (umbrella study vs per-article studies) deferred until Q1 resolves — if unit=quote, umbrella likely; if unit=article, per-article studies is natural. Not on WORKLIST proper until Pete authorizes — scoping only this session. Next session sequence per `Perplexity_Only/RELEASE_NOTES_v1_7_0.md` §"Pre-flight for the v1.7.0 cutover": (1) `cd ~/Desktop/Archive/aberdeen-group-archive && git pull` to land sandbox commits, (2) `cp scripts/add_row_class_to_prescience_scores_v1.py scripts/retag_cloud_parse_fails_v1.py ~/Desktop/Archive/scripts/`, (3) F3 dry-run expecting scored=8119, parse_fail=64, prefilter_skip=4, preseed_skip=253, no_anchor=0, pending=0, total=8440 — diff vs. expected before `--commit`, (4) F3 `--commit`, (5) F6 dry-run expecting exactly 12 cloud parse_fail rows retagged, (6) F6 `--commit`, (7) Phase 1+2 rebuild on `~/Repos/kastner-aberdeen-wiki/`, (8) shape audit — corpus must be 1453/23926/3276/4361/865-high (unchanged from v1.6.2 + methodology-demo v2.0), (9) surgical Phase 5 re-embed for the 3 changed `Perplexity_Only/` docs only (PRESCIENCE_ARCHITECTURE.md, MASTERS_NOTES.md, RELEASE_NOTES_v1_7_0.md) via `reembed_single_page_v1.py`, (10) if any expected counts drift, patch MASTERS_NOTES/PRESCIENCE_ARCHITECTURE/RELEASE_NOTES in sandbox + ship doc-only update commit. After cutover green: tag `v1.7.0` + GitHub Release titled "Multi-Horizon Prescience: row_class discipline + cloud parse-fail retag".
- [ ] **§11v KW Console v2 design** (overnight pondering item for Pete, raised 2026-06-13 PM). v1 (shipped today) is wiki-only markdown-only. v2 adds: (a) `kind` dropdown in UI (`note` / `rebuttal` / `annotation` / `comment`), (b) `kind=rebuttal` triggers writing to a wiki-side **spool file** (e.g., `wiki/_pending/rebuttals_spool.csv`) accumulating rows during the day, (c) EOD batch script `promote_rebuttals_spool_v1.py` reads the spool, appends rows to `_master_player_rebuttals.csv` IN THE ARCHIVE, copies markdown bodies from `wiki/notes/` to `aberdeen-group-archive/kastner-author/notes/`, then truncates spool. Architectural principle (Pete): the archive repo is self-sufficient for research — prose bodies AND metadata of rebuttals must live in the archive, not just the wiki. KW Console stays lightweight (UI only, no cross-repo writes). Spool is intra-day staging; promote script is testable in isolation; review-before-promotion at EOD catches misclassifications.
- [ ] **§11v `_master_player_rebuttals.csv` move-to-root** (raised 2026-06-13 PM, WITHDRAWN from tonight's EOD pending preauthorization). 9 other masters live at repo root; this one sits at `archive_masters/_master_player_rebuttals.csv`. Move would make layout consistent and create a stable path for v2 spool-promote script. **Requires explicit preauthorization from Pete in a future session.** Workflow when authorized: dry-run script, versioned, backup, row-parity check, Pete approves dry-run, then committed standalone (NOT as part of an EOD batch).
- [ ] **§11v Skill amendments for D3 standing rule** (raised 2026-06-13 PM). Add to `kastner-archive-pipeline` and `kastner-github` skills: "Production master moves require preauthorization" — any proposed master move/rename/location change must be flagged in plain language, follow the masters-edit ritual, get Pete's explicit sign-off, and ship standalone (never bundled in EOD cleanup). Triggered by the agent attempting to bundle `_master_player_rebuttals.csv` move as cleanup tonight.
- [ ] **§11u-cont-tail Reconcile 4 `[DEFERRED]` prescience values in `_master_studies.csv`** (raised 2026-06-13 AM post-release audit). 4 of 17 new transcripts shipped with `prescience='[DEFERRED]'` (a non-enum placeholder, not in {low|medium|high}) plus a rationale explaining what verification is needed. This was intentional restraint by the extractor — preferable to a guess — but the literal `[DEFERRED]` string violates the §13.1 v20 schema and will not be picked up by enum-bound filters. Affected studies and their rationales:
   - `oracle-data-warehousing-launch-multimedia-spatial-d63644` — "Predictions need Phase 3 verification."
   - `crossroads-launch-front-back-office-integration-508c58` — "Predictions about Crossroads category and integration economics need outcome verification."
   - `crossroads-june-1997-launch-variant-cut-caea12` — "Predictions overlap with primary cut; need Phase 3 verification."
   - `tandem-himalayan-airport-commercial-tpc-c-0b1c60` — "Tandem's eventual Compaq acquisition (1997) needs outcome verification against viability claims."
  Pete owns these scores per the §11s argument-of-record principle (the operator argues prescience before it lands). Options: (a) Pete-assigned scores in next session, (b) cloud Pass-C-style adjudication, (c) leave deferred and codify `[DEFERRED]` as a valid sentinel value in MASTERS_NOTES v2. Strong recommendation: (a) — these are 4 vendor-event/broadcast transcripts where Pete has direct domain context (Crossroads, Tandem trajectory, Oracle DW outcome). Workflow: 4-row mini-manifest CSV + tiny apply script (REPLACE-by-study_id-on-prescience+rationale only) + Phase 1+2 rebuild + commit. Estimated 30-60 min next session.
- [ ] **§11u-cont-tail Reconcile +49 master_technologies vs +48 wiki technology pages** (1 short, raised 2026-06-13 AM). Phase 1+2 added 49 tech rows but Phase 3 emitted only 48 new tech pages. Likely one tech row was a backlink-only update on an existing page (or had its slug collide with an existing tech). Quick reconcile: `SELECT t.tech_id FROM technologies t LEFT JOIN pages_manifest p ON p.entity_id = t.tech_id WHERE t.created_at > '2026-06-12' AND p.entity_id IS NULL;` against `kastner.duckdb`. <30 min.
- [ ] **§11u-cont-tail Investigate `wiki/technologies/tech-006.md`** (raised 2026-06-13 AM). Filename pattern `tech-NNN` is a fallback slug, suggesting one tech row was ingested without a proper canonical_id (likely a Pass B `_known_technologies.csv` lookup miss). Either the row needs a real canonical_id and the page renamed, or the row needs to be merged into an existing tech. Cross-reference with `Perplexity_Only/CANONICAL_IDS.md` anti-pattern catalog.
- [ ] **Build `Pete_Only/` directory at `~/Desktop/Archive/Pete_Only/`** (today, after the 3 tail items above are scoped). Companion to `Perplexity_Only/` — holds the scripts and references Pete personally needs day-to-day (Mac-side conveniences, his own quick-reference notes, frequently re-typed commands, anything that should travel with Pete but doesn't need to be in either the agent-context bucket or the public research dataset). First session task: enumerate what belongs there (apply scripts? shape-audit one-liners? wiki regen runner? `git pull && status` wrapper?) and seed the directory with a README documenting its purpose. Likely repo-mirrored at `Pete_Only/` for portability across machines.
- [ ] **Confirm Zenodo DOI minted for v1.6.1** (next session). Webhook fired 2026-06-13 ~11:55 UTC. Check [zenodo.org/account/settings/github](https://zenodo.org/account/settings/github) and the release page DOI badge. Add the DOI to `_decisions_log.md` v1.6.1 entry once it appears.
- [ ] **Set up commit signing on Mac** (low priority, raised 2026-06-13 AM). Branch protection on `aberdeen-group-archive` and `kastner-aberdeen-wiki` requires PRs + signed commits; we currently bypass with admin rights. Configure GPG or SSH commit signing in `git config --global` to satisfy the rule and clear the "bypassed violations" warnings on push.
- [x] **§11u DECtp Pass B observation extraction** — DONE 2026-06-12 AM on Mac. `ingest_dectp_observations_v2.py` (17-col schema with `section` + `legacy_obs_id`) ran clean; 26 observations appended to `_master_observations.csv` (23605 → 23631). Distribution as predicted: 18 dec / 4 ibm / 4 tandem-computers entities; 22 dectp / 4 debit-credit techs. Backup: `_master_observations.csv.bak_dectp_obs_ingest_20260612T110659Z`. Script shipped at commit `7770680c`. Decisions log entry in tonight's EOD batch.
- [x] **§11u-cont 17-transcript Pass A ingest** — DONE 2026-06-12 PM on Mac. Read all 17 transcripts in `~/Desktop/Archive/transcripts_extract/` end-to-end, built `transcript_manifest_v1.csv` (17 rows × 16 master_studies cols), Pete approved with no changes. Generalized `ingest_transcript_studies_v1.py` (manifest-driven, dry-run default, QUOTE_ALL, backup before write) ran clean on Mac; 17 rows appended to `_master_studies.csv` (1435 → 1452). Backup: `_master_studies.csv.bak_ingest_transcript_studies_20260612T134209Z`. Methodology vocabulary established: `internal-sales-training-archive` (Blue Monday only), `vendor-event-archive` (12 vendor talks), `broadcast-archive` (4 TV news). Phase 1+2 reran clean on `~/Repos/kastner-aberdeen-wiki/`. **Pass B (observation extraction for the 17 new studies) deferred to next session — Pete chose Option A: one transcript at a time, starting with SARS CNBC broadcast (prescience='high', ~5-8 obs expected).** Estimated ~150-300 total obs across 17 transcripts.
- [x] **§11u-cont Pass B — observation extraction for 17 new transcript studies** — EXTRACTS COMPLETE in sandbox 2026-06-12 PM. All 17 transcripts read end-to-end; **295 observations** extracted (range 5-53 per study, mean 17). Per-study breakdown: SARS CNBC=32 / NBC Nightly=16 / DEC Blue Monday=42 / Informix Universal=53 / Crossroads ad1=8 / Crossroads ad2=5 / Sybase XI=6 / Oracle DW=7 / Crossroads launch=9 / Crossroads variant=5 / Tandem=10 / Informix competitive=27 / CNBC Tech Edge=25 / MSNBC AOL=14 / Portal Software=13 / Ingres 4GL=12 / Software 2000=11. Plus 194 entities + 122 techs (canonical-ID-corrected: `att-corporation`→`ent-att`, `ibm-powerpc`→`powerpc`, etc.). All per-study sets §16 GREEN. Consolidated into 4 batch files (1 REPLACE studies, 3 APPEND ent/tech/obs); §16 batch gate GREEN after v1.1 patch (widened plain-text window 200→1000B; added `CC-BY-NC-SA-4.0` to license enum for the 2 SARS broadcast rows). License posture: 15 studies CC-BY-4.0, 2 SARS studies CC-BY-NC-SA-4.0 (NC-SA is safer for archived broadcast news). EOD ships 4 batch CSVs to `passb_batch/` + `apply_passb_transcripts_v1.py` to `scripts/`. Mac runs apply script (dry-run → review → --commit), then Phase 1+2 + §17 Pass A + §18 wiki surgical + §20 integrity + Phases 3-6.
- [ ] **§11u-cont Pass B Mac merge + downstream pipeline** (next session's primary task). Pete on Mac:
  ```bash
  cd ~/Desktop/Archive/aberdeen-group-archive && git pull
  mkdir -p ~/Desktop/Archive/passb_batch
  cp passb_batch/batch_*.csv ~/Desktop/Archive/passb_batch/
  cp scripts/apply_passb_transcripts_v1.py ~/Desktop/Archive/scripts/
  cd ~/Desktop/Archive
  python3 scripts/apply_passb_transcripts_v1.py            # dry-run
  python3 scripts/apply_passb_transcripts_v1.py --commit   # write
  python3 scripts/build/01_load_csvs_v2.py --archive ~/Desktop/Archive/archive_masters --wiki ~/Repos/kastner-aberdeen-wiki
  python3 scripts/build/02_build_data_layer_v4.py --wiki ~/Repos/kastner-aberdeen-wiki
  ```
  After Phase 1+2: shape audit (expect 1452 / **23926** / 3401 / 4434), then §17 Pass A v1 (`assembler.py pass-a`), then §18 surgical wiki update (`refresh_data_layer.py` + `add_pass_a_v2_pages.py`), then §20 integrity checks, then Phases 3-6 for the new studies + scaffolding refresh.
- [x] **§11v Skill maintenance (PARTIAL)** — DONE 2026-06-13 AM mid-session. Triggered by Pete's `IO Error: Cannot open file '/Users/scott/Desktop/kastner_wiki/db/kastner.duckdb'` after Phase 1+2 rebuild — the skill still pointed at the deleted Desktop path despite the 2026-06-01 migration. Quick-patch applied to `skills/user/kastner-archive-pipeline/SKILL.md` and saved as v1.3: (1) global path swap — all 23 `~/Desktop/kastner_wiki` references → `~/Repos/kastner-aberdeen-wiki` (also `/Users/scott/Desktop/...` form); (2) inverted the three-locations table — row #2 is now Repos as live, row #3 is the deleted Desktop path marked DO NOT USE; (3) rewrote Gotcha 2 to document the 2026-06-01 migration; (4) shape-audit SQL fixed `(...)/10` → `(...)//10` (DOUBLE-arithmetic bug, was producing 38 decade buckets instead of 6); (5) baseline numbers bumped from 2026-05-27 (1434/23605/3207/4312/109 high-pres) to 2026-06-13 (1452/23926/3276/4361/125 high-pres post Pass B reconcile); (6) updated pre-flight checklist item 10 + EOD shipping paragraph + Workflow B+C verification rule. Backup at `SKILL.md.bak_pre_v13_path_fix`. **Still deferred to next §11v session:** document `v_studies_by_decade` as the canonical decade-count view (currently the shape-audit query is canonical but the view exists and is more readable).
- [ ] **§11v-cont OCR-garbage study `ra-web-site-search-3910-sli-16eb05`** (raised 2026-06-13 AM mid-session). Confirmed on Mac via shape-audit follow-up query: title is literally `"==> picture [240 x 792] intentionally omitted <=="` — a PDF image-replacement marker that an old ingest pipeline mistook for a study title. `study_prescience_enum='[DEFERRED]'` is the consequence, not the cause. **This is NOT a real study and should be DELETED from `_master_studies.csv`**, not scored. Workflow: (a) confirm with Pete that there are no observations / entities / techs linked to this study_id (likely none, since it was never a real study); (b) write `delete_orphan_study_v1.py` (REPLACE-by-study_id-skip, dry-run default, QUOTE_ALL, backup); (c) verify no FK orphans in observations/entity_studies/tech_studies after delete; (d) Phase 1+2 rebuild; (e) commit. Once deleted, the gate's lone unexpected `[DEFERRED]` row disappears and the enum is clean WITHOUT needing `[DEFERRED]` as a sentinel.
- [ ] **§11v-cont NULL prescience: `perspecta-inc-september-1997-b8e81d`** (raised 2026-06-13 AM mid-session). One study has `study_prescience_enum IS NULL` — Perspecta Inc., September 1997. Likely a pre-Pass-C ingest from before prescience was required. Pete-owned score per §11s argument-of-record principle. Pattern: 1-row mini-manifest CSV + apply script (REPLACE-by-study_id-on-study_prescience_enum + study_prescience_rationale only) + Phase 1+2 rebuild + commit. ~15 min next session. Pair with the dectp obs-prescience gap (see Pass C scoring backlog item below).
- [ ] **Pass C observation-level prescience scoring on the 17 new transcripts** (raised 2026-06-13 AM mid-session). Confirmed gap between two prescience signals: `study_prescience_enum='high'` count is **498** at study level, but `v_studies_with_high_prescience` count is **124** at obs level — 374 studies are scored `high` at study level with zero rows in `_master_prescience_scores.csv`. The 17 new transcripts (including dectp, which now has `prescience='high'` post-reconcile) are part of this lag. Per the §11u-cont Pass B closeout, the +295 new obs from the transcripts have not yet been Pass-C-scored. Workflow: `run_prescience_pass_c_v5.py` on the 295 new obs → append to `_master_prescience_scores.csv` → Phase 1+2 rebuild → expect dectp + others to appear in `v_studies_with_high_prescience`. Long-running (~30-60 min for 295 obs at typical Pass C throughput). Defer until after Gate v1.1 ship.
- [ ] **Migrate `datetime.utcnow()` to `datetime.now(datetime.UTC)` in apply scripts** (raised 2026-06-13 AM during Pass B v2 apply). Python 3.12+ emits `DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).` Affects `apply_passb_reconcile_v2.py` (this session) and likely every `apply_*_v<N>.py` written before today. Pattern: replace `datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")` with `datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%SZ")`. Build into the v3 apply-script template alongside the Gate v1.1 pre-write validation hook. Also patch the `add_<col>_to_<table>_v1.py` template in `kastner-archive-pipeline` skill Workflow A Step 2. Cosmetic but visible on every run — Pete noticed it in the v2 apply output. Companion to the long-standing §11i item for `roll_up_prescience_v3.py`.
- [ ] **§11q Qwen 3.6 rollback — pending Pete pull-and-copy on Mac.** Archive `origin/main` at `f40ad150` (rollback bump). Pete still needs to run on Mac: `cd ~/Desktop/Archive/aberdeen-group-archive && git pull && cp scripts/build/_llm_helper_v4.py scripts/build/04_generate_indices_v6.py scripts/build/06_emit_scaffolding_v4.py ~/Desktop/Archive/scripts/build/ && cp scripts/pre_filter_scoreable_obs_v7.py ~/Desktop/Archive/scripts/`. After copy: LOCAL_MODEL resolves to `qwen3.5:27b-mlx`. Qwen 3.6 model stays installed for future re-evaluation but is not in active use. Wiki-repo `kw_ask.py` `DEFAULT_LLM` was never touched (decision deferred and now moot — no upgrade landed).
- [x] **NEW skill `local-model-upgrade-gates` v1.0** — DONE 2026-06-02 PM. Saved to user skill library (skill_id `0fda0938-7ab8-4670-838a-70b19bcb4b49`). Codifies the 4-gate decision flow (independent benchmark review → workload mapping → paper smoke-test → real hardware A/B) that would have stopped §11q at Gate 1 for 5 minutes of reading instead of ~3 hours of pull+debug+rollback. Three LOCKED fixtures (Phase 3 study page, kw_ask synthesis, Pass C scoring) reused across all future model evaluations so candidates are apples-to-apples comparable. Includes generalized `scripts/run_gates.py` Gate-4 A/B runner that takes incumbent+candidate as CLI flags. §11q evidence trail preserved under `references/decisions_log_11q_2026_06_02.md`.
- [ ] **§11o first live exercise:** drop 2-3 PDFs into `~/Desktop/Archive/_ingest_queue/` and walk Pass 1 → review → Pass 2 dry-run → `--commit` using `prepare_for_ingest_v3.py`. Validate SHA fast-path against a known DUPLICATE; validate BETTER heuristic against a known higher-res rescan; confirm public archive untouched on BETTER ACCEPT. Pete on Mac first: `cd ~/Desktop/Archive/aberdeen-group-archive && git pull && cp scripts/prepare_for_ingest_v3.py ~/Desktop/Archive/scripts/`.
- [ ] **§11p Git-author password leak postmortem** (new, raised 2026-06-01) — write a forever-archive memo on the credential exposure: how `git config user.name` and GitHub profile name both ended up as a password, the 976-commit blast radius, the API-commit identity gotcha (token uses GitHub profile name, not local Mac config), and the discovery path. Decide if any wiki/skill text needs to warn future operators.
- [x] **EOD batch commit + v1.6 release** — DONE 2026-05-31 PM. Archive commit `954fc1b2`, Wiki commit `e78ce36a`. Both tags `v1.6` pushed and releases published. (Archive tag had to be moved from `2fc84158` → `954fc1b2` and the release republished from draft — new gotcha codified in memory.)
- [x] **§11j Scripts directory cleanup** — DONE 2026-06-01 AM. Archive repo commit `1efb09d9` reshuffled 25 files via Git Data API (50 tree edits, no blob duplication). `scripts/build/` keeps the 6 canonical pipeline scripts + `_llm_helper`; `scripts/build/_legacy/` holds 8 stale pipeline versions; `scripts/` (flat) holds 17 canonical one-offs; `scripts/_legacy/` holds 17 stale one-offs. Mac (`~/Desktop/Archive/scripts/`) mirrored via `/tmp/_11j_mac_reorg_v1.sh --commit` — same layout but `_legacy/` is a superset (49 vs 17 files) because Mac accumulated more historical work-products. Skill `kastner-archive-pipeline` updated (5 path edits, paths now point to `scripts/build/0X_*.py`) and saved back to library (skill_id preserved). Full entry in `decisions_log_entry_2026_06_01_11j_scripts_cleanup_v1.md` — appended to `_decisions_log.md` in tonight's EOD batch.
- [x] **§11k Memoir prose drift → memoir-in-repo** — DONE 2026-06-01 AM. Archive repo commit `56b86829`. Source memoir `kastner-author/memoirs/kastner_breadth_memoir.md` (199 lines) shipped with a 4-line "Note on numbers" preface (v1.4 → v1.6 disclosure). Wiki study page `study-kastner-technology-breadth-memoir-2026.md` intentionally NOT patched (Pete: "(a) leave it. move on.") — will self-correct at next full Phase 3 LLM regen. Full entry in `decisions_log_entry_2026_06_01_11k_memoir_in_repo_v1.md`.
- [x] **§11l `_prescient` total backfill** — DONE 2026-06-01 AM. Archive repo commit `ff73eed5`. Phase 4 patched v2 → v3 with two-totals computed-at-build-time (full filtered population, not just top-50 shown): `**Total: 124** high-prescience studies` + `**Total: 489** holistic-prescience studies` + "top 50 shown below". Pete re-ran Phase 4 on Mac; `_prescient.md` validated. Phase 5 re-embed re-ran 17m 9s (10,301 rows); `kw ask` now returns "**124** high-prescience studies" with `_prescient` citation. Full entry in `decisions_log_entry_2026_06_01_11l_prescient_totals_v1.md`.
- [x] **§11m Ship 6 Mac-only canonical scripts to archive repo** — DONE 2026-06-01 PM. Archive repo commit `c4fe9c66` (6 adds + 2 v4_2 → _legacy moves, 8 tree edits in one Git Data API batch). Shipped: `download_aberdeen_pdfs.sh`, `extract_missing_dates_v3.py`, `prepare_for_ingest.py`, `roll_up_prescience_to_master_v3.py` (sibling to repo's `roll_up_prescience_v3.py`, not successor), `run_prescience_calibration_v3.py`, `run_prescience_pass_c_v5.py`. Full entry in `decisions_log_entry_2026_06_01_11m_six_scripts_shipped_v1.md`.
- [x] **§11n Broader scripts audit (Mac working dir vs repo clone)** — DONE 2026-06-01 PM. Archive repo commit `208d8e58` (added `_legacy/refresh_data_layer_v1.py`). 13 differences resolved: 9 cleared by `git pull` (clone was 2 commits behind), 2 by mirroring §11m's `_legacy/` moves on Mac, 1 by recognizing `refresh_data_layer.py` as prototyping leftover (closed v1.6 backlog §9), 4 by copying repo-only files to Mac. Final `diff -rq` returns empty. Zero drift between Mac `~/Desktop/Archive/scripts/` and repo `scripts/` (excluding `_legacy/`). Full entry in `decisions_log_entry_2026_06_01_11n_scripts_audit_v1.md`.
- [x] **Decide fate of `~/Desktop/kastner_wiki/`** — DONE 2026-06-01 AM. Pete deleted from Desktop after v1.6 rebuild (2026-05-31) confirmed the canonical wiki at `~/Repos/kastner-aberdeen-wiki/` is verified-clean and the v1.6 release tags are pushed on both repos. State at deletion: 279 MB, 13,120 markdown files (vs ~10,301 canonical), 2,845 iCloud collision ghosts, DuckDB stale at 2026-05-30 17:42 (pre-v1.6). Decisions log entry `decisions_log_entry_2026_06_01_kastner_wiki_deletion_v1.md` appended to `_decisions_log.md` in tonight's EOD batch.
- [ ] Cron `2e191f67` will auto-delete the abandoned v1 quarantine on **2026-06-05 09:00 EDT** — no action needed.
- [x] **§11r Archive cleanup of late-May one-time directories** — DONE 2026-06-04 AM on Mac (NOT YET COMMITTED to repo). Script `archive_cleanup_v1.sh` ran clean: 16 directories MOVED to `~/Desktop/Archive_legacy_2026_May/`, 1 DELETED (`__pycache__`). Moved: 5 `incoming-bucket-{B,C,D,E}` + `incoming-existing` + `bucket-A-processed` + 6 `archive_masters_pre_*` backups + `v1.5_workspace` + `kastner_duckdb_build` + `prepared_dropped_dups` + `logs/zip_test2`. Active dirs untouched: `aberdeen-group-archive/`, `archive_masters/`, `incoming-bucket-A/`, `kastner_wiki/`, `prepared/`, `scripts/`, `_pass_c_abandoned_runs/`. Script lives on Mac at `~/Desktop/Archive/scripts/archive_cleanup_v1.sh` and in workspace; not yet shipped to repo. Forever-archive principle preserved — nothing destroyed except regenerable `__pycache__`. Decision pending: ship `archive_cleanup_v1.sh` to `scripts/` in next EOD batch (Y/N).
- [ ] **§11s Kastner blog 2005 1H synthesis study** (deferred 2026-06-04 AM). Material: Google Blogger export, 2922 lines, ~60 entries Feb-Jun 2005, Pete owns the words. Decision: lean to one synthesis study (option 3 from neutral analysis) over per-post Pass C ingestion or new 7th collection type. Working file in workspace: `kastner_blogspot_content.md`. Plan:
   - Pete edits the input MD and supplies curated content (which predictions to feature, his framing).
   - Synthesis study `kastner-blog-synthesis-2005-1h.md` drafted from curated content using existing methodology-demo / memoir template. Collection type `technology_topic` (no new 7th type just for one study).
   - Source bodies preserved in `shorttack/kastner-restricted-sources/blog/blogspot_2005_export.md`.
   - **Argument-of-record requirement**: Pete wants an opportunity to argue prescience scores before they land. Example basis: on DIY-servers Pete's 2005 audience was enterprise IT buyers for whom hyperscaler-style ODM procurement was not yet an option; the 2010+ ODM/OCP outcome doesn't retroactively make the 2005 directional call wrong for the audience he was writing for. Operational rule: each prediction in the synthesis gets a Pete-assigned score AND a model-assigned score; disagreements get a rationale paragraph from Pete. The synthesis study Pass C score is Pete's call, not the model's.
   - Two Jan 2006 entries in tranche are out of scope for the 1H 2005 synthesis but retained for whatever 2H2005/2006 round comes next.
   - Other blogs Pete recalls writing post-Aberdeen: to be located in future session.

---

## v1.6 candidates

### 1. Recover the three known-missing sources

Status registry: `_missing_sources.csv` (archive root)

- [ ] **Robbins 1991 ATM** — search Wayback Machine (`web.archive.org/web/*/aberdeen.com/*`), ex-Aberdeen networking-team contacts, any institutional library that subscribed to Aberdeen's networking practice in 1991-1992. Founding artifact of the entire ATM-vs-Ethernet thesis — highest provenance value.
- [x] **Casale 1989 Computational Chemistry** — DONE 2026-06-22 PM. PDF (8.5MB, 168 pages, ABBYY FineReader OCR) ingested via `archival-ingest` v20. Date: **1989-01 canonical** (Jan 1989 publication; May 1989 cover is a reprint, noted in metadata). Author: Charles T. Casale (Aberdeen co-founder). Study path: NEW top-level `project_examples/conflicting-trends-computational-chemistry-fe5c31/` (NOT `other-authors/`). 175 files in one tree commit via Git Data API batch: 1 study / 24 entities / 10 technologies / **64 observations** / 31 codes / 165 figures. All 5 CSV validation gate checks PASS; all assembler validations PASS. Archive commit `a02c23f1`. Private repo: `kastner-restricted-sources/aberdeen-1989/CompChem.pdf` commit `33a52bf3`.
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

### 11a. Re-run Phase 1+2 against canonical wiki (`~/Repos/kastner-aberdeen-wiki/`) — ✅ SHIPPED 2026-05-31

DONE 2026-05-31. Phase 2 v3 had a decade-bucket bug (DuckDB `/` on INTEGER returns DOUBLE, breaking the `1990s` etc. string concatenation). Built v4 with `//` integer division; ran clean. Shape audit:

| Master | Rows |
|---|---:|
| studies | 1434 |
| observations | 23605 |
| entities | 3207 |
| technologies | 4312 |
| v_studies_by_decade (rows) | 1434 |
| distinct decades | 6 |
| high-prescience (P_max ≥ 4) | 124 |

v4 ships in tonight's EOD batch commit to `shorttack/aberdeen-group-archive`.

### 11b. Complete Phases 3-6 (vault, indices, embeddings, scaffolding) — ✅ SHIPPED 2026-05-31

DONE 2026-05-31. Unattended chain launched 09:06 EDT with caffeinate. Phase 5 v2 wrote the wrong parquet schema (`path, slug, embedding, dim`) and crashed `kw_ask.py` with `BinderError: column "vector" not found`. Built Phase 5 v3 to match the kw_ask consumer contract exactly (`page_path, page_type, slug, title, vector, dim`); re-ran in 16m 55s for 10,301 pages; bge-m3; 100% frontmatter coverage. Phase 6 complete. **`kw ask` validates clean** — no BinderError, 0.547+ top-hit retrieval scores, 6-source citations. v3 ships in tonight's EOD batch commit.

Gotcha 9 (producer/consumer schema drift) + pre-flight item 16 ("creators must verify with consumers before committing contractual code") added to `kastner-archive-pipeline` skill from this incident.

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

### 11j. Resolve dual scripts directories (~/Desktop/Archive/aberdeen-group-archive/scripts/build/ vs /Archive/scripts/)

Raised 2026-05-31. The archive repo has `scripts/build/` (versioned build scripts: 01_load_csvs through 06_emit_scaffolding). Pete's standing rule says "I prefer scripts at /Archive/scripts" which currently holds operational scripts (kw_note, kw_ask, semantic_search, verify, refresh_data_layer, reembed, roll_up_prescience). Two directories with overlapping intent.

- [ ] Decide canonical home for each script type: build vs. operational vs. one-off diagnostic.
- [ ] Either consolidate into one directory or document the split (e.g., `scripts/build/` for pipeline phases, `scripts/operational/` for daily tools) in `AGENTS.md`.
- [ ] See `decisions_log_entry_2026_05_31_scripts_dirs_v1.md` in workspace.

### 11k. Refresh memoir study prose with v1.6 counts — ✅ SHIPPED 2026-06-01 (path-divergent)

Closed 2026-06-01 via **memoir-in-repo** approach rather than wiki-page patch. Source memoir landed at `kastner-author/memoirs/kastner_breadth_memoir.md` (archive commit `56b86829`) with a "Note on numbers" preface disclosing the v1.4 → v1.6 drift. Wiki study page `study-kastner-technology-breadth-memoir-2026.md` will self-correct at next full Phase 3 LLM regen (~3 hours; deferred).

### 11l. Add total count to `_prescient.md` — ✅ SHIPPED 2026-06-01

Closed 2026-06-01 via Phase 4 v3 patch (archive commit `ff73eed5`). Two totals now computed at build time from the full filtered population: `**Total: 124** high-prescience studies` + `**Total: 489** holistic-prescience studies` + "top 50 shown below". Phase 5 re-embed (17m 9s) confirmed `kw ask` retrieval correctness.

---

## v1.7 candidates

### 11o. `archive-queue-ingest` skill v2 + `prepare_for_ingest_v3.py` (PDF-routing daily-driver)

Raised 2026-06-01. **Pivoted mid-day** from a markdown-only ingest skill (v1 design) to a PDF-routing daily-driver after Pete corrected the framing: the real ingest queue carries scanned Aberdeen PDFs, and the right skill is one that decides where each incoming PDF goes — public archive (text + CSVs) vs private repo (`kastner-restricted-sources`, PDFs only).

**Architecture (locked):**

- **Two repos, one wall.** `aberdeen-group-archive` (public): TEXT ONLY — markdown studies, master CSVs, decisions log. `kastner-restricted-sources` (private): ALL PDFs at flat `<study_slug>.pdf` layout.
- **One canonical PDF per study.** No accumulation, no `_superseded/` folder. BETTER copies REPLACE the prior canonical PDF; git history of the private repo is the binary audit.
- **Four dispositions:** NEW (new study), BETTER (incoming stronger, Pete ACCEPTs), DUPLICATE (SHA match or not stronger), AMBIGUOUS (title fuzzy 0.55-0.75 band → Pete decides).
- **BETTER heuristic** (ported from v2.2 canonical): more pages OR more embedded XObject images OR ≥30% higher text density.
- **Two-pass workflow:** Pass 1 `discover_queue` writes `_review_<UTC>.csv` (22 cols); Pete fills `pete_decision` for BETTER/AMBIGUOUS rows; Pass 2 `--apply-review` (dry-run, then `--commit`).
- **Public archive sticky on BETTER/DUPLICATE.** MD and master CSV are NEVER touched — work already done.
- **Audit:** one line per disposition in `_decisions_log.md`. No `_supersedes.txt` sidecars.
- **EOD ship:** TWO repos — PRIVATE first (PDF adds/replacements), then PUBLIC (MDs + master CSV + decisions log + archived review CSV).

**Scope discipline (deferred to other skills):**
- Pass A/B/C observation extraction → `archival-ingest` v20
- DOCX/XLSX/EPUB → `archival-ingest` v20
- Phase 1+2 data-layer rebuild after NEW → `kastner-archive-pipeline` Workflow B
- Phase 3-6 wiki refresh + embeddings → `kastner-archive-pipeline` Workflow C
- OCR on scan-only PDFs → out of scope (Pete edits review CSV manually if needed)
- bge-m3 cosine dedupe → out of scope for v3

- [x] **v1 markdown-only skill scaffolding** — DONE 2026-06-01 morning. Superseded same day by v2 PDF-routing redesign (see decisions log).
- [x] **`prepare_for_ingest_v3.py` authored** — DONE 2026-06-01 PM. 1346 lines, `ast.parse` passes. Single-queue input, three dispositions, six signals per PDF, SHA-256 fast-path, BETTER heuristic, flat restricted-sources layout. Workspace: `/home/user/workspace/prepare_for_ingest_v3.py`.
- [x] **Skill v2 rewritten** — DONE 2026-06-01 PM. Overwrites skill_id `0fcc8fbc-b4a4-493a-8605-fa0caf6be5fa` with PDF-routing design wrapping `prepare_for_ingest_v3.py`. Validated via `agentskills validate`.
- [x] **§11o decisions log entry rewritten** — DONE 2026-06-01 PM. See `decisions_log_entry_2026_06_01_11o_*.md` for full design rationale, signal definitions, threshold values, and the reasoning under each principle.
- [ ] **EOD ship:** v3 script → `shorttack/aberdeen-group-archive/scripts/prepare_for_ingest_v3.py`; skill v2 → save_custom_skill overwrite; decisions log entry → append to `_decisions_log.md`; WORKLIST diff.
- [ ] **First live exercise:** drop 2-3 PDFs into `~/Desktop/Archive/_ingest_queue/` and walk Pass 1 → review → Pass 2 dry-run → `--commit`. Validate SHA fast-path against a known DUPLICATE; validate BETTER heuristic against a known higher-res rescan; confirm public archive untouched on BETTER ACCEPT.
- [ ] Update `kastner-archive-pipeline` cross-skill handoffs to point at `archive-queue-ingest` v2 for daily PDF ingest.

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


### 20. TPC entity slug normalization (raised 2026-06-07)

Five competing entity slugs for the TPC organization co-exist in `_master_entities.csv` and `_master_observations.csv`:
`transaction-processing-council`, `tpc-council`, `tpc-org`, `tpc`, `transaction-processing-performance-council`.
Canonical slug: **`tpc-council`**.

- [ ] **Draft `normalize_tpc_entity_slugs_v1.py`:** dry-run default; `--commit` opt-in; reads `_master_entities.csv` and `_master_observations.csv`; collapses all four non-canonical slugs to `tpc-council`; QUOTE_ALL on write; backs up both masters before any write; row-parity check (total row count must be unchanged); prints before/after slug-frequency table. Raised during TPC longitudinal survey session.
- [ ] After `--commit`: run Phase 1 + Phase 2 to rebuild DuckDB; verify entity counts unchanged; confirm `kw ask` returns `tpc-council` for TPC org queries.
- [ ] Decisions log entry with before/after shape audit.


### 21. Memoir TPC content missing from entity/technology observations (raised 2026-06-07)

During TPC longitudinal survey assembly (2026-06-07), `tpc_coverage_v2.sh` showed 0 rows for
technology slugs in `v_observations`, and memoir chapters ch05/ch06/ch07 observations do NOT
carry `entity_id` or `tech_id` values referencing TPC slugs despite rich first-person TPC
benchmark content (Westwood Midnight Ambush, specsmanship sidebar, Debit/Credit experience).

**Symptoms:**
- ch06 OBS-020 through OBS-035 cover Debit/Credit benchmark, specsmanship, DECtp press event —
  zero TPC/debit-credit tech_id tags on any of them
- ch07 has only 1 TPC-related hit; Aberdeen Transaction Services auditor role not present in
  extracted observations at all
- `v_observations` tech_id query for all 16 TPC/benchmark slugs returns 148 obs — none from
  memoir chapter study_ids

**Hypothesis:** Memoir ingest (Pass A/B extraction) did not tag entity_id/tech_id on personal-
recollection observations; the extractor may have left those columns blank when obs_type is
`personal-recollection` or when no explicit entity name appears in the observation text.

**Investigation steps:**
- [ ] Spot-check ch06 observations.csv directly: are entity_id and tech_id columns populated
  at all, or blank across the board?
- [ ] Check what percentage of `personal-recollection` obs_type rows across ALL memoir chapters
  have non-null tech_id vs. other obs_types (expert-opinion, market-data, etc.)
- [ ] If blank: determine whether this is a Pass B extraction gap (extractor skipped tagging
  for memoir obs) or a Pass A structural issue (columns missing from ingest output)
- [ ] If tagging gap: draft a targeted re-tagging pass for memoir chapters using the known
  TPC/benchmark slug vocabulary — add to `archival-ingest` backlog or as a standalone script
- [ ] If Aberdeen Transaction Services auditor role is genuinely absent from ch07 observations:
  flag as memoir content gap (not in the text) vs. extraction gap (in text, not extracted)
- [ ] Decisions log entry with findings

**DuckDB diagnostic to run first:**
```bash
duckdb ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb -c "
SELECT obs_type,
       COUNT(*) AS total,
       COUNT(tech_id) AS has_tech_id,
       COUNT(entity_id) AS has_entity_id
FROM v_observations
WHERE study_id LIKE 'volume-1-%'
GROUP BY obs_type
ORDER BY total DESC;"
```

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

### 22. Mac MCP Bridge — read-only archive access from Perplexity Mac app (APPROVED 2026-06-20)

FastMCP stdio bridge exposing the archive + wiki to Perplexity Mac app. **No local LLM** — cloud Perplexity does synthesis; the bridge just runs DuckDB queries and reads files. Build sequence and rationale: see `docs/mac_mcp_bridge_architecture_v1.md` and `docs/promoted_mac.md` in the archive repo.

**Estimated effort**: 1–2 weeks across 5 phases (stub → DuckDB tools → file-read tools → kw_ask → Perplexity registration). Local-LLM path (Qwen + Rapid-MLX) deferred indefinitely; revisit only if Phase 1–5 usage reveals real need.

- [ ] Phase 0: `mac_mcp_bridge/` scaffolding in `~/Repos/` (NOT under `~/Desktop/` — iCloud trap)
- [ ] Phase 1: `duckdb_query`, `duckdb_tables`, `duckdb_describe` (read-only DuckDB)
- [ ] Phase 2: `read_archive_file`, `list_prepared` with path sanitization
- [ ] Phase 3: `kw_ask` integration (verify lazy-load, embedding path env)
- [ ] Phase 4: Install PerplexityXPC helper, register connector JSON, smoke-test from a real chat
- [ ] Phase 5 (separate decision): write/execute tools
- [ ] Phase 6 (future, possibly never): optional `qwen_synthesize` local-LLM tool

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

## Done this session

### Embedding-upgrade-gates toolkit + first candidate verdict (2026-07-01, EOD COMMIT)

- **New reusable toolkit `embedding-upgrade-gates/`** — the embedding-lane analogue of `local-model-upgrade-gates` (which covers the LLM lane; bge-m3 explicitly lives in a separate lane per that skill). Shipped to BOTH repos this EOD: **public light-touch** copy at `Archive/tools/embedding-upgrade-gates/` (for other scholars/posterity) and **ops originals** at `Perplexity_Only/embedding-upgrade-gates/`. Contents: `README.md`, `METHODOLOGY.md`, `probes_v1.txt` (20 LOCKED probes, `#`=comment), `scripts/{embed_ab_harness_v2.py, build_gold_template_v1.py}`, `gold/` (labeled gold + prefilled template), `baselines/`.
- **Two-part promotion gate LOCKED (2026-07-01).** Candidate promotes ONLY if BOTH: **(A)** aggregate Recall@6 ≥ incumbent + 0.05, AND **(B)** candidate loses ≤1 relevant hit vs incumbent on ANY single query. MRR@6 + mean-Jaccard(top-6) = context/risk signals only, NOT gates. Recall@6 (not @10/nDCG) because k=6 is the `kw_ask` default. Harness flags: `--queries`, `--gold`, `--recall-margin` (default 0.05), `--regression-floor` (default 1). Status quo wins ties.
- **Labeled gold set (Pete's judgment, reviewed + confirmed).** `gold/embed_gold_20probes_labeled_v1.csv` — 198 rows / 20 queries, **151 relevant / 47 not-relevant, 0 blanks**. Rubric: 1 = on-topic real content page; 0 = scaffolding/definition page (`code-pre-00x`, `code-prescience-assessment`, `_prescient`, bare decade tags) OR off-topic. Aggressive 0-labeling concentrated on the two prescience probes (Q11 5/12, Q14 2/11) — the category-collapse guard. Grounded in the full 48-slug resolver (`slug_resolution.txt`). Pete confirmed Q6 `linux-server`=1 and Q14 decade tags=0.
- **First candidate — qwen3-embedding:8b (MRL-1024) vs bge-m3 incumbent: KEEP INCUMBENT.** Both indexes 10,862 vecs / dim 1024, top-k 6. **Gate A FAIL:** Recall@6 inc 0.685 vs cand 0.586, delta −0.100 (candidate worse, not marginally better). **Gate B FAIL:** 4 per-query regressions — Q11 short-horizon prescience 5→0 (**−5**), Q14 3y-prescience 2→0 (−2), Q5 web-enterprise 4→2 (−2), Q6 lose-to-OSS 4→2 (−2). MRR@6 inc 0.912/cand 0.875; mean Jaccard(top-6) 0.237 (<0.3 band). The two prescience probes are the qwen category-collapse the gate was built to catch — candidate top-6 returned ONLY scaffolding pages. **The gate did its job.**
- **Baseline record written to both trees** — `baselines/bgem3_vs_qwen3emb8b_20260701.md` (ops = full internal detail; public = de-internalized). Supersedes the earlier "PENDING gold labels" agreement-only draft.
- **Live index UNTOUCHED.** `data/embeddings.parquet` (bge-m3) never modified; candidate `data/embeddings_qwen1024.parquet` + incumbent snapshot `data/embeddings_bgem3.parquet` stay on disk as recorded artifacts (local-only, NOT in repo). Rollback pre-written but unused.
- **Mac eval-dir artifacts stay local** at `/Users/scott/Desktop/Archive/eval/` — NOT committed (harness, probes, labeled/draft/verdict CSVs). Only the toolkit trees + baseline record go into the repo.
- **Notes-dir pre-commit check: CLEAN** (`git status --porcelain wiki/notes/` empty on the Mac). No KW Console notes to fold in.

### Model-eval scouting (2026-06-30 PM, NO COMMITS — all held in workspace)

- **Track A — qwen3.6:27b dense vs qwen3.5:27b-mlx: NO-GO (Gate 2 STOP honored).** Gate 0 flagged G1 (Qwen 3.x thinking trap) + G3 (frozen-LLM prescience failure). Gate 1 MIXED→STOP: gains are reasoning-mode-only; non-thinking IFBench regresses, ~12% JSON error rate + context drift. Gate 2: no non-thinking primary-capability gain across Phase 3 / kw_ask / Pass C; gains land in the "doesn't matter" coding column. Decision: **keep `qwen3.5:27b-mlx`**, no pull, Gate 3/4 not needed. Analysis: `trackA_gate1_gate2_qwen36_27b_v1.md` (workspace).
- **Track B — Sonar Pro replacement scout (per G3).** Replacement MUST retrieve+abstain at inference. Shortlist: Sonar Deep Research (top, lowest migration risk) → local Qwen + Ollama 0.18.1 web_search → Valyu DeepResearch. Eval gate LOCKED: quadratic-weighted κ≥0.70 (raw or ≤±1 shift); baseline-to-beat qwen3.5-27b κ_max=0.331. Run-pack drafted (2 scripts: `run_prescience_pass_c_sonar_deep_research_v1.py` [compiles OK] + `compute_pass_c_candidate_kappa_v1.py` [NOT compile-verified]). **Fixture discovery flagged:** `scripts/qwen_master_kappa_v2_paired.csv` is an OUTPUT not an input; real reference = `_master_prescience_scores.csv` filtered to `model='sonar-reasoning-pro'`. Run-pack + scout: `trackB_sonar_replacement_scout_v1.md` (workspace). NOT SHIPPED — Pete declined EOD commit.
- **kw_ask local-model scout (reframe, ~27-32B class, scouting only).** Key insight: kw_ask is retrieval-grounded, so G3 does NOT apply (evidence is in-prompt). Incumbent `qwen3.5:27b-mlx` is hard to beat (leads open-source IFEval at 95.0%). Only fixture-worthy candidate: **Gemma 3 27B / Gemma 4 31B** — upside is dropping the G1 thinking-mode tax + freeing RAM, not better extraction. Command R 35B is the citation-quality leader but gated by CC-BY-NC license + unverified MLX availability (abort-if-no-MLX). Qwen3.6 out (Track A precedent). Writeup: `kw_ask_local_model_scout_v1.md` (workspace + shared to artifacts). MLX-tag/license verification NOT done.
- **EOD decision (Pete):** hold all artifacts in workspace, no commit. No notes-dir items (`kw pending` clean per v2.0 session).

### v2.0 release prep — full-corpus SH prescience + PC-Deals per-SKU + Zenodo docs (2026-06-30)

- **SH (3y/5y) prescience integrated end-to-end.** `merge_sh_scores_to_master_v1.py` → `_master_prescience_short_horizon.csv` (**17,030 rows**); `apply_sh_study_verdicts_v1.py` → studies master 16→20 cols, **792 verdict studies** (3y: 522 high / 264 medium / 4 low / 1 not-applicable / 1 pending; 5y: 518 high / 268 medium / 4 low / 1 not-applicable / 1 pending). `apply_study_verdicts_v1.py` filled `perspecta-inc-september-1997` → medium.
- **Pipeline phases bumped for SH.** Phase 1 → `01_load_csvs_v3.py` (SH master in `MASTER_SCHEMAS` halt=0; `short_horizon` parquet). Phase 2 → `02_build_data_layer_v5.py` (PROMOTE `short_horizon`; new views `v_prescience_sh`, `v_observations_with_sh`, `v_studies_with_sh_verdicts`, `v_sh_3y_distribution`, `v_sh_5y_distribution`). Phase 3 → `03_generate_vault_v3.py` (study pages render SH verdicts in frontmatter + "Short-horizon prescience" body section so bge-m3 embeds them; tier-1 prompt gets 3y/5y). Phase 6 → `06_emit_scaffolding_v2.py` (README "What's new" SH block; AGENTS SH recipes; chat-starter prompts 4-6; verify.py +4 SH views). All `py_compile` OK. Canonical SH chain = 03_v3 / 04_v2 / 05_v3 (bge-m3) / 06_v2 — do NOT run the older non-SH v4/v5/v6 build scripts.
- **Phase 1 v3 + Phase 2 v5 rebuild RAN clean (Pete, this session).** All 33 views built. Shape audit BEFORE == AFTER (only SH cols/views added, no rows): **1504 studies / 24842 observations / 3293 entities / 4376 technologies / 1504 pub_year / 6 decades / 876 high-prescience**. `v_studies` now exposes `prescience_3y_enum/_rationale` + `prescience_5y_enum/_rationale`.
- **`kw ask` validation PASSED** — "which studies were prescient at 3 years" returned Object-Oriented Three-Tier-Plus 1996 (high, mean 3.92) as exemplar; population ground truth in `v_studies_with_sh_verdicts`.
- **Three high-prescience surfaces clarified (baked into README).** `v_studies_with_high_prescience` (`prescience_max ≥ 4`, loose) = **876** (headline count); authored enum (`study_prescience_enum='high'`) = **503**; `prescience_mean ≥ 3.5` (tight) = **88**. Authored-enum distribution: high 503 / not-applicable 384 / medium 339 / low 276 / [DEFERRED] 2.
- **Observation count reconciled.** Live `v_observations` = **24,842** is canonical for all v2.0 docs (the 2026-06-27 CSV snapshot of 24,715 predated the post-`-mx` rebuild; Δ +127 reconciled per Pete 2026-06-30).
- **PC Deals `-mx` per-SKU price journeys** — L7 tier: **249 per-SKU price journeys** (lead PC-Deals deliverable for v2.0 release notes).
- **Wiki repo PUSHED** — `shorttack/kastner-aberdeen-wiki` main `3a992434..93499d11` (1623 files, 11459 ins / 524 del; embeddings.parquet 66 MB under the 100 MB hard limit; SH parquets present; bge-m3 1024-dim re-embed of 10,862 pages). KW Console notes clean (`kw pending` empty).
- **Four v2.0 docs written + shared** — `RELEASE_NOTES_v2.0.md` (new; leads with full-corpus 3y/5y prescience + v9 confabulation fix, then PC-Deals per-SKU journeys), `README.md` (full v2.0 rewrite), `.zenodo.json` (new), `CITATION.cff` (v2.0). Decisions-log v2.0 entry drafted (both shape audits + obs reconciliation + prescience-surface clarification).
- **Archive repo push HANDED TO PETE (Mac).** SH masters (`_master_prescience_short_horizon.csv` 17,030 rows; `_master_studies.csv` 20 cols), PC-Deals per-SKU data, and the new build scripts live in Pete's working tree — Pete bundles everything plus the six doc files in ONE Mac `git add && git commit && git push`, then tags `v2.0` + `gh release create` (notes-file = `releases/RELEASE_NOTES_v2.0.md`) and deposits the archive + wiki to Zenodo (concept DOI `10.5281/zenodo.20245076`).
- **DECLUTTER_PLAN_v1 implemented (Groups A+B+C+D only; E/F/G deferred).** Built `reorg_archive_root_v1.py` (~340 lines; dry-run default, `--commit` executes, `--safety` runs only the path-safety grep gate, `--force` overrides, `--repo` defaults to CWD). Refuses to run unless CWD has `_master_studies.csv` + `.git`. `git mv` for tracked files (preserves history as `R` renames), plain `mv` for gitignored. Creates `releases/`, `reports/`, `data_sources/`, `_local_backups/`. **Move groups:** A = `*.bak*` / `archive_masters_pre_*` → `_local_backups/` (gitignored); B = `RELEASE_NOTES_v*.md` / `future_work_v*.md` / `RESUME_2026_*.md` → `releases/` (WORKLIST.md STAYS at root; dated WORKLISTs deferred); C = `_audits/`, validation/audit/report CSVs + `_web_cache.json` / `_web_verification_results.json` / `PASS_A_VERIFICATION_REPORT.md` / `model_prescience_scoring_finding_v1.md` / `_master_entity_field_conflicts.csv` → `reports/`; D = `*_processed.zip` (7) → `data_sources/`. Masters, `_known_*`, `_decisions_log.md`, `WORKLIST.md`, `CHANGELOG`/`CITATION`/`LICENSE` STAY at root (asserted post-run). Path-safety grep blocks any flagged name from moving unless `--force`; SAFETY_NAMES also covers Group F items so Pete can verify before any future stale-dup move. Idempotent (`0 to move` on re-run). Tested on a synthetic /tmp repo: 26 moved as `R` renames, masters preserved, `_collection_stats.csv` correctly BLOCKED by active script ref, Group F untouched. **Folded into the v2.0 commit** (Pete's choice): reorg runs FIRST on the Mac (`--safety` → paste grep → `--commit`), THEN docs drop (`RELEASE_NOTES_v2.0.md` into `releases/`), THEN ONE `git add -A && git commit && git push`. README updated for the new layout: `RELEASE_NOTES` internal link → `./releases/`, layout/tree block adds `releases/` `reports/` `data_sources/` `_local_backups/ (gitignored)`. `_local_backups/` added to `.gitignore` so Group A backups stay out of the Zenodo tarball.

## §11v BACKLOG — kw-note integration for player rebuttals

**Established:** 2026-06-13 §11v
**Status:** PARKED — non-blocking. First use (DECtp Plaza Hotel) already committed under the prior design.

**Problem.** `PLAYER_REBUTTAL_PROCESS.md` (drafted this session) writes rebuttals to `archive_masters/_master_player_rebuttals.csv` + `kastner-author/notes/`. Archive masters that are inaccessible to the wiki defeat the wiki's role as the home of added knowledge. The DECtp Plaza Hotel rebuttal note now sits in both repos but is **not** in the Obsidian vault, not embedded by nomic-embed, not in `kastner.duckdb`, and not linked from the study page.

**Correction.** Route rebuttals through Pete's existing Mac `kw note` CLI so they land in `kastner-aberdeen-wiki/wiki/` as first-class wiki pages — indexed by Obsidian, embedded, queryable in DuckDB, discoverable from study pages.

**`kw note` flags observed (2026-06-13):** `--title --slug --tags --from-file --from-stdin --body --author --update --append --replace --question --sources-from --model --retrieval-k --commit --overwrite --git-commit`.

**Open questions:**
- Where does `kw note` write? (which directory under `wiki/`?)
- What frontmatter does it produce?
- Does it accept a `--type`/`--note-type` flag to distinguish rebuttals from other notes?
- How does a rebuttal page bind back to its subject `study_id`? (frontmatter field, tag, or body wikilink?)
- Does `--git-commit` push to the wiki repo, or only commit locally?

**Tasks:**
- [ ] Capture `kw note --help` full output + `which kw` + source-code dispatch for the `note` subcommand
- [ ] Decide whether to KEEP `_master_player_rebuttals.csv` as a parallel audit ledger or retire it
- [ ] Revise `PLAYER_REBUTTAL_PROCESS.md` to make `kw note` the canonical path; install at `~/Desktop/Archive/Perplexity_Only/`
- [ ] Migrate the DECtp Plaza Hotel rebuttal (`kastner-author/notes/dectp_prescience_rationale_2026_06_13.md`) into the wiki via `kw note`
- [ ] Confirm the migrated note is embedded by nomic-embed and queryable in `kastner.duckdb`
- [ ] Add a `rebuttal_of: <study_id>` (or equivalent) frontmatter convention so study pages can surface rebuttals via Dataview

---


---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._

**Mac data state (live DuckDB, post-SH rebuild, 2026-06-30):** studies 1504 · observations 24842 (live `v_observations`; the 2026-06-27 CSV snapshot of 24715 predated the post-`-mx` rebuild, Δ +127, reconciled to 24842 per Pete 2026-06-30) · prescience-scores master 17251 · SH master 17030 (792 verdict studies) · high-prescience 876. v2.0 docs written, wiki pushed, archive push handed to Pete.
