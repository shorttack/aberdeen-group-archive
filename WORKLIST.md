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

**Last updated:** 2026-06-14 PM (§11v cont 7 EOD — Pass C v2 Qwen calibration FAILED. κ_max=0.331 across all variants on n=1,041 paired obs vs Sonar. NO-GO for full Qwen rescore. Three-path strategy adopted: Path 1 Sonar primary scorer (short-term), Path 2 Qwen-pre-filter+Sonar-scorer hybrid (documented not adopted), Path 3 Llama 3.3 70B / DeepSeek R1 70B / Mistral Large 2 evaluation (medium-term) against locked 1,041-obs fixture. OLLAMA_GOTCHAS gains G2a/G2b split + G3 (frozen-LLM scoring structural failure). Skill `local-model-upgrade-gates` bumped to v1.3 with canonical 0-5 scale + Layer 2 paired-fixture lock + Qwen failure baseline κ_max=0.331. §11v prescience architecture audit (D6) remains tomorrow's priority — still gates v1.7.0.)
**Current ship state:** archive `origin/main` at `ce3262f3` (Pass B masters merge: +17 studies, +295 obs, +69 ent, +49 tech, +194 ES pairs, +122 TS pairs — plus M:N tables `_master_entity_studies.csv` + `_master_tech_studies.csv` committed for the first time, closing the 2026-05-26 gap). Parent `2a151bed` (Pass B Completion: 4 Perplexity_Only files + RELEASE_NOTES + WORKLIST banner + decisions log v2). Tag `v1.6.1` pushed; GitHub Release "17 video transcripts including 1988 DECtp and 2003 SARS" published 2026-06-13 11:54:54 UTC. Wiki `origin/main` at `6d0723e6` (1,085 files: 18 new study pages, 69 new entity pages, 48 new tech pages, 9 root parquets, 7 _validated parquets, 5 decade rollups, kastner.duckdb, README/Makefile/build_manifest.json). Mac state: **1452 studies / 23926 observations / 3276 entities / 4361 techs / 3876 entity-study pairs / 5375 tech-study pairs**. `v_studies_with_high_prescience` = 124. `decades_covered` = 6 (using `//` integer division). Pass B obs canonical-ID rate: 295/295 = 100%. **Prescience-scoring rate for new transcripts: 13/17 valid (76%) + 4 `[DEFERRED]` placeholders that need argument-of-record before assignment.** bge-m3:latest canonical embedding model (10,437 embeddings, 17m 4s, ~10/sec). **Security:** git `user.name` was "Catalina" (one of Pete's passwords); leak found 2026-06-01 PM, rotated to `shorttack`; 976 historical commits across the two public repos retain dead-string "Catalina" in Author metadata.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

- [ ] **§11v PRESCIENCE ARCHITECTURE AUDIT (D6, raised 2026-06-13 PM)**. Pete: *"audit the entire prescience architecture locally on the Mac and at GitHub. It used to be simple. Now, I don't think I can explain the process or the files used."* Surfaces accumulated: File 1 (live Pass C output, 8 cols, Mac), File 2 (master, 11 cols, Mac), File 3 (repo snapshot, 8 cols, stale), repo `_master_prescience_scores.csv` at root (last touched 2026-05-31 — likely ~2 weeks lagged), `_master_player_rebuttals.csv` at `archive_masters/` (Path B), `prescience` enum in `_master_studies.csv` (authored verdict, pass-through), `v_studies_with_high_prescience` view (filters authored enum), `promote_pass_c_to_master_v1.py`, `sync_studies_verdicts_repo_from_archive_masters_v2.py`, deprecated `roll_up_prescience_v3.py`. Path A (math-driven) and Path B (player rebuttal override) branching logic is in skill v1.5+ but operator can't recite it. Deliverable: `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` enumerating files, schemas, update protocols, Path A/B flows, known lag points, open questions, simplification proposals. Pete-driven 2-4 hour deep-dive. PRIORITY HIGH — do not ship v1.7.0 until audit is reconciled and the May 31 lag on repo `_master_prescience_scores.csv` is understood.
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

## Done this session

### 2026-06-14 (§11v cont 7 — Pass C v2 Qwen calibration FAILED + skill v1.3)

- **AM (08:53-09:22):** Pass C v2 calibration v5 disaster — 28 of 30 obs returned empty `response` because Qwen 3.x default thinking-mode swallowed token budget. Root cause: `"think": false` must be TOP-LEVEL of request body, NOT inside `options`. Pete: *"You told me about think:false two weeks ago and then forgot it."* Documented as G1 in `Perplexity_Only/OLLAMA_GOTCHAS.md` so it can never be lost again.
- **AM (09:11-09:18):** v6 driver kappa=0.000 four runs in a row — root cause was scale mismatch: Qwen on 0-100, master on 1-5. Pete picked B1 (1-5 wins, master is source of truth). v7 driver rewritten. Skill `local-model-upgrade-gates` fixture bumped to v2 (1-5). Decision: `decisions/decisions_log_entry_2026_06_14_prescience_scale_1_5_v1.md`.
- **AM (11:47-12:01):** Pivot — Pete: *"v1 Pass C passed Kappa we are failing on."* Found `prescience_score_prompt_v2.md` on Mac (canonical 0-5 rubric authored 2026-05-25, NOT in repo). 1-5 "decision" was a misread; **canonical scale is 0-5** (0 = cannot assess, legitimate verdict). Working dirs everywhere — 574 LIVE under `~/Desktop/Archive/prepared/` + 309 ABANDONED under `~/Desktop/Archive/_pass_c_abandoned_runs/20260526/`. Pete: *"Stop and save this map. It's gold."* Saved as `Perplexity_Only/WORKING_DIRS_MAP_2026_06_14.md`. May 26 abandon = agent-quality (Pro→Max regression), not methodology — data salvageable.
- **PM (12:54-13:05):** Salvage audit verdict GREEN — 2,723 abandoned Qwen rows, 100% parse_ok, single model, 2,722 obs overlap with master. Computed quadratic-weighted κ vs Sonar/Claude on the master: raw κ=0.2379 (n=1,041), Qwen−1 shift κ=0.3308 (best), tier-bucket κ=0.2393. **All variants fail 0.70 gate; all fail 0.60 substantial threshold.** Abstention asymmetry 88×: Sonar abstains 795× where Qwen commits.
- **PM (13:08):** Decision recorded — Qwen 27B FAILS Pass C calibration. Three-path strategy adopted: Path 1 (Sonar primary scorer, effective immediately) / Path 2 (Qwen pre-filter + Sonar scorer hybrid, documented not adopted) / Path 3 (Llama 3.3 70B / DeepSeek R1 70B / Mistral Large 2 against locked 1,041-obs fixture, medium-term). Qwen 27B retained for Phase 3 wiki gen, kw_ask synthesis, summarization, `is_non_claim()` filtering. Decision: `decisions/decisions_log_entry_2026_06_14_qwen27b_calibration_failed_v1.md` (commit `95e0595b`).
- **PM (13:14-13:20):** Follow-on commits — `Perplexity_Only/OLLAMA_GOTCHAS.md` split G2 → G2a (num_predict defense) + G2b (scale-must-match-master) + added G3 (frozen-LLM scoring structurally underperforms grounded — Qwen κ_max=0.331 baseline locked). Skill `local-model-upgrade-gates` bumped to v1.3 via `save_custom_skill`: `pass_c_scoring.md` rewritten to canonical 0-5 + Layer 2 paired-fixture lock at 1,041 obs; SKILL.md adds frozen-LLM anti-pattern + Qwen failure baseline; `decisions_log_qwen27b_calibration_failed_2026_06_14.md` bundled into `references/`. Session arc captured in `logs/session_2026_06_14_agent_progress.md`. Final commit `786ad0ca`.
- **Carry-forward to tomorrow:** §11v PRESCIENCE ARCHITECTURE AUDIT (D6) still gates v1.7.0 release. New open question: should `scripts/qwen_master_kappa_v2_paired.csv` (when next generated on Mac) move to `Perplexity_Only/` since it's now the locked Gate 4 fixture, not a one-off script artifact? Defer to Pete.
- **Commits today (10):** `49d0c392`, `2d80c66d`, `51f9873c`, `accf7e8e`, `91765ea6`, `b292c986`, `583cd584`, `8309e0c0`, `95e0595b`, **`786ad0ca`** (HEAD).

### 2026-06-13 PM (§11v cont 3-5 — KW Console v1 SHIPPED + DEBUGGED + Skill v1.7 + new standing rule)

- **KW Console v1 shipped** to wiki repo via 5 commits: `e267d14d` (initial 743 LOC FastAPI + 493 LOC HTML + bin/kw v3), `b876802f` (Unicode dash-fold + manifest cache + macOS open fix), `0397f6c8` (pages_manifest ↔ v_studies slug-form bridge), `cfa64211` (`type` not `collection_type` BinderError fix), `f33b5fa2` (Pete's first Save&Commit — Debit-Credit IBM-vs-DEC 1988 rebuttal, end-to-end verified as one-time EOD-watching test at 20:33Z).
- **Phase 3 wiki regen complete** on Mac at ~19:54Z: 10,382 pages emitted (1452 studies + 3276 entities + 4361 technologies + decades/themes/codes/collections), tier-1 LLM enrichments 126/200/150, qwen3.5:27b-mlx still in effect per §11q rollback (94 min CPU, 60% utilization during peak).
- **§11q Qwen 3.6 rollback Mac copy verified** as already in sync: 4 files (`_llm_helper_v4.py`, `04_generate_indices_v6.py`, `06_emit_scaffolding_v4.py`, `pre_filter_scoreable_obs_v7.py`) match between Mac `~/Desktop/Archive/scripts/` and `aberdeen-group-archive/scripts/` since 2026-06-02 (sizes 9166/13657/13181/13599 bytes, both sides). No-op rollback — todo was stale from earlier plan.
- **Skill `kastner-archive-pipeline` bumped v1.6 → v1.7** via `save_custom_skill` (skill_id `fe5dc1e1-e51d-4f60-88e7-4d2651afa18b` unchanged). New Gotcha 12: `v_studies` bucket-type column is `type`, NOT `collection_type`. Added row to Gotcha 11 mapping table cross-referencing Gotcha 12. Full `DESCRIBE v_studies` output captured (20 columns total). Description length 995/1024 chars. Also clarified: archive masters live at repo root, NOT under any `master_csvs/` directory (the agent invented `master_csvs/` in conversation earlier and Pete corrected).
- **Skill `kastner-github` EOD section** patched at session start with mandatory `kw pending` semantic check (preferred) or `git status --porcelain wiki/notes/` equivalent before staging anything. Notes-check tonight returned clean for the wiki repo because Pete's Debit-Credit rebuttal already shipped as a standalone commit via KW Console's own Save&Commit (the v1 contract).
- **NEW STANDING RULE (D3)**: production master CSV moves, renames, or location changes require **explicit, declared, preauthorized approval from Pete in the same conversation turn**. Triggered by the agent attempting to bundle `_master_player_rebuttals.csv` move from `archive_masters/` to repo root as "cleanup for consistency" in tonight's EOD. Move WITHDRAWN. Promoted to backlog under §11v. Skill amendments to follow.
- **NEW BACKLOG (D6)**: full prescience architecture audit. Pete's concern verbatim: *"audit the entire prescience architecture locally on the Mac and at GitHub. It used to be simple. Now, I don't think I can explain the process or the files used."* Surface inventory captured in decisions log entry. Priority HIGH — hold v1.7.0 release until audit reconciled. Hidden lag identified: repo `_master_prescience_scores.csv` at root last touched 2026-05-31 (`2fc84158`), likely ~2 weeks behind Mac File 2.
- **Plaza-Hotel rebuttal note retrieved** from archive repo at `kastner-author/notes/dectp_prescience_rationale_2026_06_13.md` (8104 bytes, committed earlier today at `604dfec0`). Whether to also mirror to `wiki/notes/` via KW Console is deferred to v2 design.
- **Wiki repo state at EOD**: HEAD `f33b5fa2` (Pete's rebuttal). `kw pending` clean. No wiki-side artifacts pending.
- **Archive repo state at EOD**: HEAD `604dfec0` pre-EOD (Plaza rebuttal + helper script from 15:54Z). This EOD adds WORKLIST + decisions log only. NO master edits this session.

### 2026-06-13 AM (§11u-cont Pass B Completion + Release v1.6.1)

- **Pass B Completion Commit landed:** `2a151bed` via Git Data API — 8 sandbox files in one commit. `Perplexity_Only/MASTERS_NOTES.md` (329 lines, v2 rewrite), `Perplexity_Only/CANONICAL_IDS.md` (129 lines, anti-pattern catalog with 3-column table format), `Perplexity_Only/PIPELINE_QUICKREF.md` (208 lines, Phases 1-6 with `//` integer-division fix), `Perplexity_Only/OLLAMA_STATE.md` (154 lines, `_llm_helper_v4` + model state), `Perplexity_Only/README.md` (83 lines), `WORKLIST.md` (banner added), `_decisions_log.md` (appended v2 entry, 3127 lines total), `RELEASE_NOTES_v1.6.1.md` (92 lines).
- **Masters merge committed:** `ce3262f3` on Mac — `_master_studies.csv` (1435→1452), `_master_observations.csv` (23631→23926), `_master_entities.csv` (3207→3276), `_master_technologies.csv` (4312→4361), and crucially **`_master_entity_studies.csv` (3876 rows) + `_master_tech_studies.csv` (5375 rows) committed to the repo for the first time** despite existing on Mac since 2026-05-26 — closes the M:N-table-not-in-repo gap. Pre-merge backup tree `archive_masters_pre_passb_v2_20260612T172545Z/` (6 CSVs + `_README.md`) also committed. 13 files / 51,251 insertions.
- **Phase 3-6 verified complete on Mac:** Phase 3 = 10,382 pages emitted overnight (~5-6 hr). Phase 4 = 6 decades + 6 collections + 1293-code index + 5 bases. Phase 5 = **10,437 embeddings in 17m 4s via bge-m3** (~10 pages/sec). Phase 6 = scaffolding refreshed (README/AGENTS/chat-starter/Makefile/.gitignore).
- **Shape audit GREEN:** studies=1452, observations=23926, entities=3276, technologies=4361, high_prescience_studies=124, decades_covered=6 (with `//` integer division — the §11v gotcha), embeddings=10437. All exact.
- **Tag `v1.6.1` pushed; GitHub Release published** 2026-06-13 11:54:54 UTC with title "17 video transcripts including 1988 DECtp and 2003 SARS" and full RELEASE_NOTES_v1.6.1.md body. URL: [aberdeen-group-archive/releases/tag/v1.6.1](https://github.com/shorttack/aberdeen-group-archive/releases/tag/v1.6.1). Zenodo webhook fired automatically (DOI minting async, 1-5 min).
- **Wiki regen commit:** `6d0723e6` on `kastner-aberdeen-wiki` — 1,085 files, 9,915 insertions, 3,913 deletions. Distribution: 505 study pages / 313 entity pages / 240 tech pages / 5 decades / 7 _validated parquets / 9 root parquets / 1 duckdb / 3 docs. Zero junk (no .DS_Store, no .obsidian/workspace.json, no stray scripts). The data/embeddings.parquet 63MB file triggered an LFS warning (informational, not blocking — under the 100MB hard limit).
- **Pre-flight prescience audit found 4 `[DEFERRED]` values** in `batch_studies_REPLACE_v1.csv` (and now in `_master_studies.csv` post-merge). These are intentional placeholders (the extractor declined to guess on 4 transcripts where outcome verification was open) but `[DEFERRED]` is not in the v20 enum {low|medium|high}. Promoted to next-up item §11u-cont-tail. Distribution of the 13 valid scores: 8 high / 2 medium / 3 low. The 8 high-prescience: SARS-CNBC, NBC-Nightly, Sybase-XI, Informix-competitive, CNBC-Tech-Edge, Portal-Software, Ingres-4GL, Software-2000.
- **Pass B end-to-end complete.** From 2026-06-12 AM transcript reads through 2026-06-13 AM Release v1.6.1 publish: 4 sandbox/Mac commits + 1 tag + 1 GitHub Release + 1 Zenodo DOI in ~24 hours.

### §11u DECtp Pass B + §11u-cont 17-transcript Pass A ingest (2026-06-12)

- §11u Stage A DECtp Pass B shipped on Mac: 26 obs appended (23605 → 23631), distribution 18 dec / 4 ibm / 4 tandem-computers entities + 22 dectp / 4 debit-credit techs. Backup `bak_dectp_obs_ingest_20260612T110659Z`. Script `scripts/ingest_dectp_observations_v2.py` at commit `7770680c` earlier today.
- §11u-cont Pass 0: read all 17 transcripts in `~/Desktop/Archive/transcripts_extract/` end-to-end + characterized content (vendor-event 12, broadcast 4, internal-sales-training 1).
- Built `transcript_manifest_v1.csv` (17 rows × 16 master_studies cols). Pete approved with no changes.
- Wrote `ingest_transcript_studies_v1.py` (generalized, manifest-driven, dry-run default, QUOTE_ALL, row-count parity check, backup-before-write). Sandbox dry-run + commit-sim PASS; negative-path tests for exit codes 2/3/4/5 PASS.
- Pete ran on Mac: 17 rows appended to `_master_studies.csv` (1435 → 1452). Backup `bak_ingest_transcript_studies_20260612T134209Z`. Phase 1+2 reran clean on `~/Repos/kastner-aberdeen-wiki/`.
- Methodology vocabulary locked in manifest: `internal-sales-training-archive` (Blue Monday only), `vendor-event-archive` (12 vendor talks), `broadcast-archive` (4 TV news). Plus `oral-history; ai-generated-summary` on all 17 (and `expert-quote` on the 4 broadcasts).
- Shape audit post both ingests: 1452 / 23631 / 3207 / 4312 / 1452 / 6 / 124. `v_high_holistic_prescience` correctly bumped 489 → 491 (+2 SARS broadcasts at prescience='high' in manifest). `v_studies_with_high_prescience` unchanged at 124 — this is the obs-rollup view and won't budge until Pass B observations land for the new studies.
- Pete corrected an earlier conflation: I predicted `high_prescience_studies` would bump 124→126 from manifest prescience values; that's wrong because the column is obs-rollup-derived, not studies-row-derived. Correction logged in tonight's decisions entry.
- EOD batch: Mac commits `_master_studies.csv` + `_master_observations.csv` + 2 backup-tree dirs. Sandbox ships `scripts/ingest_transcript_studies_v1.py` + `scripts/transcript_manifest_v1.csv` + appended `_decisions_log.md` + refreshed `WORKLIST.md`.
- §11v deferred maintenance noted: skill `kastner-archive-pipeline` still references `~/Desktop/kastner_wiki/` (stale); shape-audit SQL uses `pub_year / 10` (DOUBLE bug — 38 decade buckets); document `v_studies_by_decade` view as canonical.


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
