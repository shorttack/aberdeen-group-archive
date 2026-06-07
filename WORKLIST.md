# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-06-04 AM (§11r Archive cleanup of late-May one-time backups DONE on Mac — not yet committed; §11s Kastner blog 2005 1H synthesis study lane opened, deferred)
**Current ship state:** archive `origin/main` at `62d5df3e` (§11o EOD: v3 PDF-routing script + revised skill v2 design + revised §11o decisions log + WORKLIST diff). Wiki `origin/main` unchanged from v1.6 release. **Security:** git `user.name` was "Catalina" (one of Pete's passwords); leak found on 2026-06-01 PM, password rotated, Mac local + GitHub profile both reset to `shorttack` (the API commit `07b2458f` made under the bad name was amended to `62d5df3e` before Pete noticed). 976 historical commits across the two public repos still carry the dead-string "Catalina" in Author metadata — left in place since the credential is rotated. Phase 1+2 v4 baseline holds: 1434/23605/3207/4312/1434/6/124; 1434/1434 studies have pub_year; 492/1434 Pass C cloud-scored; 489 high (operational), 124 high (evidence layer); bge-m3:latest canonical embedding model.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

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

## Done this session (2026-06-02 — §11q Qwen 3.6 attempted, rolled back; gates skill created)

### AM — §11q Qwen 3.6 upgrade pack staged (commit `09ffd653`)
- Verified Qwen 3.6-27B-MLX exists on Ollama registry (`qwen3.6:27b-mlx`, ~20 GB); resolved Pete's three-way constraint ("abort if no MLX" + "do not sacrifice KW retrieval accuracy" + original `qwen3.6:27b-mtp-q8_0` tag intent) by going MLX-native.
- Inventoried 6 canonical scripts referencing `qwen3.5:27b-mlx`; aggressive B-refactor converted 04/06/pre_filter from hardcoded model strings to helper imports.
- Shipped 7-file pack via Git Data API batch.

### PM — Hot-fix #1: curl/grep/pipefail bug (commit `404022a6`)
- Pete's install transcript showed `change_local_model_v1.sh` failing at pre-flight 3 with `curl exit 56` — `curl -fsS ... | grep -q PATTERN` under `set -o pipefail` returns 1 even when grep matches. Fixed by downloading to tempfile first, grepping the file. v2 ran clean and pulled the 20 GB model.

### PM — Hot-fix #2: Ollama 0.24+ top-level `think:false` flag (commit `c9d173a8`)
- Pete's first smoke test returned empty response with `eval_count: 64`. Diagnosed Qwen 3.6 hybrid-thinking model swallowing visible tokens inside `<think>...</think>` because `think:false` was nested inside `options` instead of being a top-level request key.
- Shipped 5-file fix: `_llm_helper_v3.py` separates `LOCAL_TOPLEVEL = {"think": False, "keep_alive": "30m"}` from `LOCAL_OPTIONS` (sampling) and splats LOCAL_TOPLEVEL into the request body at top level. Plus `change_local_model_v3.sh` + 3 consumer bumps (v5/v3/v6).
- Second smoke test passed.

### PM — Paper comparison and ROLLBACK decision (commits `d05dea1b`, `f40ad150`)
- Pete asked for 3.5 vs 3.6 comparison for Phase 3 + kw_ask AFTER the 20 GB pull. Researched via Kaitchup substack + Artificial Analysis + Unsloth.
- Finding: Qwen 3.6 is significantly worse than 3.5 on IFBench (instruction-following) and GPQA Diamond. 3.6 wins are in agentic coding, AIME math, MMLU Pro — none of which Pete's workloads use.
- Pete's workloads (Phase 3 wiki gen, kw_ask synthesis, Pass C scoring) are template-discipline + citation-discipline + structured-output workloads → 3.5 is the right model.
- Rollback shipped: `_llm_helper_v4.py` pins `LOCAL_MODEL = "qwen3.5:27b-mlx"`; consumers bumped to v6/v4/v7 to import from v4. Pete to pull + copy on Mac next session.

### PM — NEW user skill `local-model-upgrade-gates` v1.0 (saved to library)
- Skill ID: `0fda0938-7ab8-4670-838a-70b19bcb4b49`. Saved via `save_custom_skill` to user scope.
- Codifies 4-gate decision flow: Gate 1 (5 min benchmark review on Kaitchup/ArtificialAnalysis) → Gate 2 (3 min workload mapping) → Gate 3 (10 min paper smoke-test against fixtures) → Gate 4 (model pull + 30 min A/B run).
- Three LOCKED fixtures live at `assets/fixtures/`: `phase3_study_page.md`, `kw_ask_synthesis.md`, `pass_c_scoring.md`. Fixtures NEVER change between candidate evaluations so models are apples-to-apples comparable.
- Generalized `scripts/run_gates.py` Gate-4 runner takes `--incumbent` + `--candidate` as CLI flags, calls Ollama `/api/generate` non-streaming with top-level `think:false`, grades all 3 fixtures against structural criteria, writes `summary.md` + `decision.md` + `raw_outputs/` to `model_eval_<tag>_<date>/`.
- §11q evidence trail preserved verbatim under `references/decisions_log_11q_2026_06_02.md` — including the two production bug-fixes (curl/grep/pipefail; top-level think:false) that survive the rollback.
- Replay finding: Gate 1 alone would have stopped §11q with 5 minutes of reading Kaitchup. Net savings against avoiding the pull-and-debug cycle: ~3 hours, 1 model pull, 4 unnecessary commits.

_(End-of-day commit clears this section)_


---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._
