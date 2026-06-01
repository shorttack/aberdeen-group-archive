# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-06-01 PM (v1.6.x backlog closure: §11k memoir-in-repo, §11l prescient totals, §11m ship 6 Mac-only scripts, §11n broader scripts audit — all closed)
**Current ship state:** **v1.6 EOD batch commit pending tonight** on both `shorttack/aberdeen-group-archive` and `shorttack/kastner-aberdeen-wiki`. Phase 1+2 v4 ran clean against `~/Repos/kastner-aberdeen-wiki/` (shape: 1434/23605/3207/4312/1434/6/124). Phase 3-6 ran 09:06–12:23 EDT. Phase 5 v2 wrote bad schema; rebuilt as v3 (page_path/page_type/slug/title/vector/dim contract); re-ran in 16m 55s; `kw ask` now passes (Gotcha 7 + Gotcha 9 codified). 1434/1434 studies have pub_year; **492/1434 prescience-scored via Pass C cloud (sonar-reasoning-pro + claude-sonnet-4.6)** — rolled up; **489 studies high prescience operationally** (`study_prescience_enum`); **124 high via obs-evidence layer** (`v_studies_with_high_prescience`); bge-m3:latest is the canonical embedding model.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

- [x] **EOD batch commit + v1.6 release** — DONE 2026-05-31 PM. Archive commit `954fc1b2`, Wiki commit `e78ce36a`. Both tags `v1.6` pushed and releases published. (Archive tag had to be moved from `2fc84158` → `954fc1b2` and the release republished from draft — new gotcha codified in memory.)
- [x] **§11j Scripts directory cleanup** — DONE 2026-06-01 AM. Archive repo commit `1efb09d9` reshuffled 25 files via Git Data API (50 tree edits, no blob duplication). `scripts/build/` keeps the 6 canonical pipeline scripts + `_llm_helper`; `scripts/build/_legacy/` holds 8 stale pipeline versions; `scripts/` (flat) holds 17 canonical one-offs; `scripts/_legacy/` holds 17 stale one-offs. Mac (`~/Desktop/Archive/scripts/`) mirrored via `/tmp/_11j_mac_reorg_v1.sh --commit` — same layout but `_legacy/` is a superset (49 vs 17 files) because Mac accumulated more historical work-products. Skill `kastner-archive-pipeline` updated (5 path edits, paths now point to `scripts/build/0X_*.py`) and saved back to library (skill_id preserved). Full entry in `decisions_log_entry_2026_06_01_11j_scripts_cleanup_v1.md` — appended to `_decisions_log.md` in tonight's EOD batch.
- [x] **§11k Memoir prose drift → memoir-in-repo** — DONE 2026-06-01 AM. Archive repo commit `56b86829`. Source memoir `kastner-author/memoirs/kastner_breadth_memoir.md` (199 lines) shipped with a 4-line "Note on numbers" preface (v1.4 → v1.6 disclosure). Wiki study page `study-kastner-technology-breadth-memoir-2026.md` intentionally NOT patched (Pete: "(a) leave it. move on.") — will self-correct at next full Phase 3 LLM regen. Full entry in `decisions_log_entry_2026_06_01_11k_memoir_in_repo_v1.md`.
- [x] **§11l `_prescient` total backfill** — DONE 2026-06-01 AM. Archive repo commit `ff73eed5`. Phase 4 patched v2 → v3 with two-totals computed-at-build-time (full filtered population, not just top-50 shown): `**Total: 124** high-prescience studies` + `**Total: 489** holistic-prescience studies` + "top 50 shown below". Pete re-ran Phase 4 on Mac; `_prescient.md` validated. Phase 5 re-embed re-ran 17m 9s (10,301 rows); `kw ask` now returns "**124** high-prescience studies" with `_prescient` citation. Full entry in `decisions_log_entry_2026_06_01_11l_prescient_totals_v1.md`.
- [x] **§11m Ship 6 Mac-only canonical scripts to archive repo** — DONE 2026-06-01 PM. Archive repo commit `c4fe9c66` (6 adds + 2 v4_2 → _legacy moves, 8 tree edits in one Git Data API batch). Shipped: `download_aberdeen_pdfs.sh`, `extract_missing_dates_v3.py`, `prepare_for_ingest.py`, `roll_up_prescience_to_master_v3.py` (sibling to repo's `roll_up_prescience_v3.py`, not successor), `run_prescience_calibration_v3.py`, `run_prescience_pass_c_v5.py`. Full entry in `decisions_log_entry_2026_06_01_11m_six_scripts_shipped_v1.md`.
- [x] **§11n Broader scripts audit (Mac working dir vs repo clone)** — DONE 2026-06-01 PM. Archive repo commit `208d8e58` (added `_legacy/refresh_data_layer_v1.py`). 13 differences resolved: 9 cleared by `git pull` (clone was 2 commits behind), 2 by mirroring §11m's `_legacy/` moves on Mac, 1 by recognizing `refresh_data_layer.py` as prototyping leftover (closed v1.6 backlog §9), 4 by copying repo-only files to Mac. Final `diff -rq` returns empty. Zero drift between Mac `~/Desktop/Archive/scripts/` and repo `scripts/` (excluding `_legacy/`). Full entry in `decisions_log_entry_2026_06_01_11n_scripts_audit_v1.md`.
- [x] **Decide fate of `~/Desktop/kastner_wiki/`** — DONE 2026-06-01 AM. Pete deleted from Desktop after v1.6 rebuild (2026-05-31) confirmed the canonical wiki at `~/Repos/kastner-aberdeen-wiki/` is verified-clean and the v1.6 release tags are pushed on both repos. State at deletion: 279 MB, 13,120 markdown files (vs ~10,301 canonical), 2,845 iCloud collision ghosts, DuckDB stale at 2026-05-30 17:42 (pre-v1.6). Decisions log entry `decisions_log_entry_2026_06_01_kastner_wiki_deletion_v1.md` appended to `_decisions_log.md` in tonight's EOD batch.
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

## Done this session (2026-06-01 — v1.6.x backlog closure: §11j/§11k/§11l/§11m/§11n + wiki deletion)

**5 commits to `shorttack/aberdeen-group-archive` (`origin/main` at `208d8e58`):**

| # | SHA | What |
|---|---|---|
| 1 | `1efb09d9` | §11j scripts cleanup (25 moves, 50 tree edits) |
| 2 | `ff73eed5` | §11l Phase 4 v3 — prescient totals (two computed-at-build-time totals + "top 50 shown") |
| 3 | `56b86829` | §11k memoir-in-repo at `kastner-author/memoirs/kastner_breadth_memoir.md` |
| 4 | `c4fe9c66` | §11m ship 6 Mac-only scripts + v4_2 → _legacy (8 tree edits) |
| 5 | `208d8e58` | §11n broader scripts audit — `_legacy/refresh_data_layer_v1.py` (closes v1.6 §9) |

**Mac actions:**
- §11j Mac mirror: 49 stale scripts moved to `_legacy/` via `/tmp/_11j_mac_reorg_v1.sh --commit`; `prepare_for_ingest backup.py` filename-space hazard renamed.
- §11j Mac canonical refresh: copied `02_build_data_layer_v4.py` + `05_compute_embeddings_v3.py` from repo clone into Mac's new `scripts/build/` (cleared yesterday's bad-schema producer).
- §11l Mac: Pete ran Phase 4 v3 + Phase 5 v3 (17m 9s re-embed). `kw ask` validates clean against new totals.
- §11n Mac: `git restore` two May 27 zero-byte truncations (memoir + skill files); `git pull` (ff73eed5 → c4fe9c66); 2× `mv` to `_legacy/` (v4_2 + refresh_data_layer_v1); 4× `cp` from repo clone to working dir.
- Final state: `diff -rq ~/Desktop/Archive/scripts/ ~/Desktop/Archive/aberdeen-group-archive/scripts/ --exclude=_legacy ...` returns empty (zero drift).

**Wiki deletion:**
- Deleted deprecated `~/Desktop/kastner_wiki/` (279 MB, 13,120 files including 2,845 iCloud ghosts). Canonical layout migration (§8) fully complete — only `~/Repos/kastner-aberdeen-wiki/` is the live working wiki.

**Skill updates:**
- `kastner-archive-pipeline` skill updated for §11j (5 path edits + Phase 5 v2→v3 schema description). Saved to library, `skill_id fe5dc1e1-e51d-4f60-88e7-4d2651afa18b` preserved.

**Decisions log entries (6, appended to `_decisions_log.md` in this commit):**
1. `decisions_log_entry_2026_06_01_11j_scripts_cleanup_v1.md` (111 lines)
2. `decisions_log_entry_2026_06_01_kastner_wiki_deletion_v1.md` (48 lines)
3. `decisions_log_entry_2026_06_01_11l_prescient_totals_v1.md` (86 lines)
4. `decisions_log_entry_2026_06_01_11k_memoir_in_repo_v1.md` (55 lines)
5. `decisions_log_entry_2026_06_01_11m_six_scripts_shipped_v1.md` (64 lines)
6. `decisions_log_entry_2026_06_01_11n_scripts_audit_v1.md` (82 lines)

**v1.6 backlog status after today:**
- §11k, §11l, §11m, §11n: closed.
- v1.6 §9 (weed `refresh_data_layer.py` sandbox-path leftover): closed by §11n.
- v1.6 §10 (rename `~/Desktop/kastner_wiki/`): superseded by today's deletion.
- Open: §5-8 (tier-1 regen, content drift, schema contract, public-wiki push policy), §11c (18 high-prescience hand-check), §11d, §11e, §11f, §11g, §11h, §11i.

_(End-of-day commit clears this section)_


---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._
