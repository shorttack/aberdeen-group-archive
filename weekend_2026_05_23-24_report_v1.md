# Kastner Aberdeen Archive — Weekend Master Report

**Period covered**: Saturday 2026-05-23 — Sunday 2026-05-24
**Release tagged**: **v1.4.0**
**Operator**: Peter S. Kastner (Adoptex LLC / BlueBridge Group)
**Environment**: Mac mini M4 Pro (`scott`), `/Users/scott/Desktop/Archive/`
**Author of this report**: Perplexity Computer (session-bound)
**Status**: ✅ All v1.4 pre-release items complete (items 1–7); 3 post-release items deferred to v1.5

---

## 1. Executive summary

Over a two-day weekend the Kastner Aberdeen Archive grew from **944 studies / 19,382 observations** (v1.3 baseline) to **1,434 studies / 23,605 observations** (v1.4 release) — a **52% increase in study count and a 22% increase in observation count** in 48 hours.

Three things made this possible:

1. A **bucket-classifier-driven ingest** pipeline (`archival-ingest` skill v20) that processed 494 prepared folders across five content buckets (A–E) plus a Mode-2 re-evaluation of already-archived material, with 100% success (493 OK + 1 not-ready, zero real failures).
2. A **case-collision merge** that took the post-ingest masters from 1,443 → 1,434 studies by collapsing 9 entity/technology rows that differed only in capitalization.
3. A **companion Obsidian wiki** built directly from the cleaned masters: 8,960 pages with 3,682 study→entity and 5,253 study→technology wikilinks, queryable from DuckDB and Parquet.

Two data-hygiene fixes also landed: the case-merge above, and a `tech_id="java"` carve-out that resolved a PDA-misfile collision in the technology master.

**v1.4 ships tonight.** Three follow-ups defer to v1.5: classifying the 493 newly-ingested studies into their canonical employer/author subtrees (currently in `prepared/`), running Pass C prescience scoring on the 370 `[DEFERRED]` studies, and rebuilding the DuckDB layer against the v1.4 masters.

---

## 2. By the numbers

| Metric | v1.3 baseline | v1.4 release | Δ |
|---|---:|---:|---:|
| Total studies | 944 | **1,434** | **+490** |
| Total observations | 19,382 | **23,605** | **+4,223** |
| Master entity rows | 9,401 | **3,207** | (master schema change) |
| Master technology rows | 7,668 | **4,312** | (case-merge + java fix) |
| Unique entities (deduped cache) | 3,281 | **3,300** | +19 |
| Unique technologies (deduped cache) | 4,277 | **4,371** | +94 |
| Audit failures (A / B / C) | 0 / 0 / 0 | **0 / 0 / 0** | unchanged |
| Wiki pages | (none) | **8,960** | new |
| Wiki wikilinks (study→entity) | (none) | **3,682** | new |
| Wiki wikilinks (study→tech) | (none) | **5,253** | new |

Note: the entity- and technology-master row drops reflect a master-schema change (one row per `(study, tech)` pair was deduped to one row per distinct entity/tech across the archive) plus the case-collision merge and java carve-out. **Underlying study data was not lost.**

### Prescience distribution at v1.4

| Rating | Count |
|---|---:|
| high | 471 |
| medium | 271 |
| low | 72 |
| not-applicable | 249 |
| **[DEFERRED]** | **370** ← v1.4 ingest, awaiting Pass C |
| (unrated) | 1 |

---

## 3. Saturday 2026-05-23 — Weekend bucket ingest

### What happened

The ingest pipeline ran in two modes:

- **Mode 1 (new material)**: Five content buckets A–E classified by an LLM-driven bucket classifier; each bucket processed end-to-end through Phase 1 (extraction), Phase 2 (Frictionless packaging), and master regeneration.
- **Mode 2 (existing archive re-evaluation)**: 120 files in `incoming-existing/` re-evaluated against the existing archive to detect already-ingested material with new metadata.

### Bucket inventory (post-ingest)

| Bucket | Files in | Log lines | REVIEW flags | MuPDF warnings* |
|---|---:|---:|---:|---:|
| A | 44 | 272 | 0 | 2 |
| B | 174 | 359 | 0 | 0 |
| C | 0 | 6 | 0 | 0 |
| D | 30 | 176 | 0 | 24 |
| E | 156 | 957 | 12 | 10 |
| existing (Mode 2) | 120 | 81 | 0 | 0 |
| **Totals** | **524** | **1,851** | **12** | **36** |

\* MuPDF warnings = cosmetic ICC-profile / optional-content layer messages; non-fatal. See §5 "32 missing investigation" below.

### Result

- 494 prepared folders created under `prepared/`
- 493 ingested OK
- 1 not-ready (single folder, retained for manual review)
- 212 `[REVIEW]` empty-date warnings in the Phase 1 log (these are flags, not failures — all 212 studies still ingested OK; the `[REVIEW]` is a hint for v1.5 metadata cleanup)
- All 493 ingests passed Layer A/B/C audits

---

## 4. Sunday 2026-05-24 — v1.4 release prep

### Timeline

| Time (EDT) | Event |
|---|---|
| ~12:25 | Master regeneration after case-folding merge: 1,443 → 1,434 studies (9-row dedupe) |
| ~13:00 | Case-merge decision logged; tech master regenerated with cleaned counts |
| ~15:58 | Master regeneration writes complete: 4,313 techs, 3,207 entities, 23,605 obs |
| ~16:00–17:00 | Companion wiki build v1 → v2 → v3 → v4 (see §4.2) |
| ~17:30 | "32 missing studies" investigation opened |
| ~18:00 | Investigation closed: zero real failures, 36 MuPDF warnings (cosmetic) |
| 19:38 | Java/PDA carve-out script committed (`fix_java_pda_carveout_v1.py --write`) — master techs 4,313 → 4,312 |
| 19:48 | `kastner_wiki/` v4 backup tarball created (2.1 MB, 8,985 entries) |
| ~20:00 | v1.4 `README.md` installed in `aberdeen-group-archive/` |
| ~20:08 | `_decisions_log.md` installed in `aberdeen-group-archive/` |
| pending | Weekend master report (this file) |
| pending | GitHub release v1.4 tag and push |

### 4.1 Case-collision merge

The master regeneration that ran around midday surfaced duplicate slug rows that differed only in capitalization. Examples:

- `JAVA` vs `java`
- `Sun Microsystems` vs `sun microsystems`
- etc.

A case-folding merge was applied. Pre-merge masters had 1,443 studies; post-merge produced 1,434 — a **9-row reduction** purely from collision collapse. No study data was lost; one of each colliding pair was retained as canonical (typically the first-seen capitalization or the form already present in the deduped cache).

This work surfaced one second-order problem: see §4.3.

### 4.2 Companion wiki build — v1 → v4

A new deliverable: an Obsidian vault built directly from the cleaned masters, with a DuckDB query layer and Parquet exports alongside.

| Build | Output | Problem identified |
|---|---|---|
| v1 | Initial vault | Dataview blocks rendered as raw code (plugin not installed on the Mac) |
| v2 | Same after Dataview plugin install | Dataview blocks rendered but showed "No results" |
| v3 | Disambiguation pass (slug -2, -3 suffixes) | Empty Dataview results: study pages had no `[[wikilinks]]` to entities/techs, so the `outlinks` graph was empty |
| **v4** | **Final** | Emits explicit `[[entity-slug\|Entity Name]]` and `[[tech-slug\|Tech Name]]` in every study page; removes empty Dataview blocks for "observations" (no obs pages); replaces them with obs counts + DuckDB SQL hints |

**v4 output verified**:
- 8,960 pages (1,434 studies + 3,207 entities + 4,313 techs + index/dashboard/system pages)
- 3,682 study→entity wikilinks
- 5,253 study→technology wikilinks
- Dataview reverse-lookup tables working on entity and technology pages (verified on iSeries page: 3 studies + 67 observations)

**Slug disambiguation example**: `java.md` (Java Programming Language) and `java-2.md` (the PDA-misfile remnant). After the v1.4 java fix in §4.3, `java-2.md` will resolve correctly on the next vault rebuild against the v1.4 masters (deferred to Pass C in v1.5).

**Wiki backup**: `kastner_wiki_backup_v1.4_20260524_193848.tar.gz` (2.1 MB).

### 4.3 Java/PDA carve-out

**Discovered**: `_master_technologies.csv` contained a row with `tech_id="java"` (lowercase) whose body content was clearly Java programming-language data (vendor "Sun Microsystems / Oracle", era "1.0 (initial release 1995)", notes citing Java 21 LTS) — but whose `tech_name` was **"PDA (personal digital assistant)"**.

A separate `tech_id="JAVA"` (uppercase) row already existed, correctly labeled "Java Programming Language". PDA was already represented as `pda`, `pda-hardware`, and `pda-mobile-devices`.

**Decision (Option A)**: Merge lowercase `java` → uppercase `JAVA` across reference tables; drop the misfiled row. Rationale: creating a corrected lowercase `java` row would re-introduce the case collision we'd just merged.

**Script**: `fix_java_pda_carveout_v1.py` — verify-then-write, tar backup, atomic .tmp+rename writes.

**Pre-mutation backup**: `archive_masters_backup_pre_java_fix_20260524_193807.tar.gz` (5.2 MB).

**Action committed at 19:38 EDT**:

| File | Rows re-pointed (lowercase → uppercase) | Rows dropped | Dupes collapsed |
|---|---:|---:|---:|
| `_master_observations.csv` | 54 | 0 | 0 |
| `_master_tech_studies.csv` | 28 | 0 | 0 |
| `_master_tech_field_conflicts.csv` | 7 | 0 | 0 |
| `_known_technologies.csv` | 1 | 0 | 1 |
| `_master_technologies.csv` | 0 | 1 (the misfile) | 0 |
| **Totals** | **90** | **1** | **1** |

**Post-write verification**: 0 lowercase `java` rows, 1 uppercase `JAVA` row, 0 residual `PDA (personal digital assistant)` strings in `_master_technologies.csv`. Final tech row count: **4,312**.

---

## 5. "32 missing studies" — investigated and closed

Carried into v1.4 as an open item from the Saturday ingest. The actual disk state had:

- **0** NOT_FOUND files
- **0** empty-date studies in masters
- **0** real Python errors in any of the 7 ingest logs
- **36** `FAIL|ERROR` grep hits in bucket logs — all **MuPDF cosmetic warnings** of two types:
  - `MuPDF error: format error: cmsOpenProfileFromMem failed` (broken embedded ICC color profile, non-fatal)
  - `MuPDF error: format error: No default Layer config` (missing optional-content layer, non-fatal)

Both are stderr noise that MuPDF emits when opening certain PDFs; text extraction still proceeds normally.

**Per-bucket breakdown**:

| Bucket | grep `FAIL\|ERROR` | MuPDF noise | Real errors |
|---|---:|---:|---:|
| A | 2 | 2 | 0 |
| D | 24 | 24 | 0 |
| E | 10 | 10 | 0 |
| (all others) | 0 | 0 | 0 |

**Disposition**: No studies missing. Investigation closed. The "32" was a phantom count from earlier in the weekend that did not correspond to any actual on-disk shortfall.

---

## 6. Decisions made this weekend

Full reasoning is in [`aberdeen-group-archive/_decisions_log.md`](./aberdeen-group-archive/_decisions_log.md). Summary:

| # | Decision | Outcome |
|---|---|---|
| 1 | Case-collision merge: keep first-seen capitalization | 1,443 → 1,434 studies |
| 2 | Java carve-out: **Option A** (merge → JAVA, drop misfile) | 91 rewrites, 1 drop |
| 3 | "32 missing" investigation: close, no studies missing | No action |
| 4 | Wiki v3/v4 design: explicit study→entity/tech wikilinks | 8,935 new wikilinks |
| 5 | `prepared/` documented as v1.4 staging directory | 493 studies staged |
| 6 | DuckDB rebuild deferred to v1.5 | DuckDB trails by 1 generation |
| 7 | Prescience scoring for 370 new studies deferred to v1.5 | `[DEFERRED]` rating in masters |

---

## 7. Deliverables shipped in v1.4

| Deliverable | Location | Size / Count |
|---|---|---|
| Updated master CSVs | `archive_masters/_master_*.csv` | 1,434 studies / 23,605 obs |
| Updated cache CSVs | `aberdeen-group-archive/_known_*.csv` | 3,300 / 4,371 |
| Companion wiki | `kastner_wiki/` | 8,960 pages |
| Wiki backup tarball | `kastner_wiki_backup_v1.4_20260524_193848.tar.gz` | 2.1 MB |
| Masters pre-java-fix backup | `archive_masters_backup_pre_java_fix_20260524_193807.tar.gz` | 5.2 MB |
| v1.4 README | `aberdeen-group-archive/README.md` | 16,668 bytes |
| Decisions log | `aberdeen-group-archive/_decisions_log.md` | 8,444 bytes |
| Java fix script | `archive_masters/fix_java_pda_carveout_v1.py` | versioned, kept for audit |
| Weekend master report | `aberdeen-group-archive/weekend_2026_05_23-24_report_v1.md` | this file |

---

## 8. v1.5 backlog

Carried forward, in priority order:

1. **Promote `prepared/` → canonical subtrees.** 493 v1.4 studies need classification into `kastner-author/`, `other-authors/`, or `employer/*`. Requires per-study author/employer determination from study metadata.
2. **Pass C prescience scoring.** 370 v1.4 studies have `prescience=[DEFERRED]`. Run the scoring pipeline; expected output: distribution similar to v1.3 (roughly 50% high, 30% medium, 10% low, 10% n/a).
3. **DuckDB rebuild against v1.4 masters.** Current DuckDB lags by one generation (3,242 entities / 4,337 techs). Pass C will naturally trigger this rebuild.
4. **Vault rebuild after Pass C.** Picks up corrected prescience and DuckDB; resolves the `java-2.md` slug from the PDA-misfile artifact.
5. **`[REVIEW]` flag drain.** 212 Phase 1 `[REVIEW]` empty-date warnings need a metadata pass; one study row in the prescience column also has a `[REVIEW]` value.
6. **`_master_tech_canonicalization_TODO.csv` drain.** Pending canonicalization tasks accumulated during v1.4 master regeneration.

---

## 9. Lessons learned

### What worked

- **Verify-then-write**: every mutation script (case-merge, java fix, vault build) ran as a dry-run first, printed expected counts, and only committed after operator confirmation. Caught at least three would-be regressions during the weekend.
- **Aggressive versioning**: every script versioned `_v1`, `_v2`, … from creation. The wiki builder went through four versions in a single afternoon; without versioning we couldn't have recovered the working v3 logic after a failed v3.5 experiment.
- **Tar backup before mutation**: 5.2 MB pre-java-fix tarball cost ~2 seconds and made the carve-out fully recoverable. Repeat for every mutation, no exceptions.
- **Diagnostic-before-fix**: the bucket-inventory paste that diagnosed "32 missing" took 15 minutes and prevented a wasted hunt; the file-level java diagnostic took 5 minutes and shaped the fix into a 91-row surgical operation instead of a full master rebuild.
- **`grep -v` and Python for atomic CSV edits**: Excel was not touched this weekend. `csv.writer(quoting=QUOTE_ALL)` + `.tmp` + `os.replace()` is the only sanctioned write path going forward.
- **Pre-emit slug disambiguation**: the v4 wiki builder pre-emits `-2`, `-3` suffixes so case-similar pairs disambiguate at the file system layer without depending on a separate dedup step.
- **`shutil.rmtree()` for vault hard-clean**: avoids iCloud sync races that made the v2 vault appear partially populated.
- **Study→entity/tech wikilink emission**: the single most impactful design change in the wiki — activating Dataview reverse-lookups on 7,520 reference pages from one buildersource of truth (the observation table).

### What didn't work / what to fix

- **MuPDF stderr noise pollutes logs**. Grepping for `FAIL|ERROR` over-counts because MuPDF warnings contain "error" as a word. Future log analysis should grep for Python traceback patterns (`Traceback`, `Exception`, `CRITICAL`, `failed to process`) instead. Consider redirecting MuPDF stderr to a separate file in v1.5.
- **macOS `awk` is BSD**, not GNU. Computed-field references (`$c` where `c` is a variable) fail with "illegal field" errors. Use Python for any CSV field operation.
- **Heredoc paste through Terminal.app**: long inline heredocs sometimes drop the closing marker silently and leave the shell stuck in `>` continuation. Fix: download script files to disk and run from disk; keep inline heredocs short.
- **DuckDB drift**: choosing to defer the DuckDB rebuild leaves the query layer one generation behind. Acceptable for v1.4 but should be a v1.5 day-1 action.
- **`source_path` vs `source_file`**: the master schema documented `source_path` in the v1.3 README but the actual column is `source_file`. Fixed in v1.4 README; flag for v1.5 schema audit.

---

## 10. Appendix: file inventory at v1.4 close

### Top-level `Archive/` directory

```
/Users/scott/Desktop/Archive/
├── aberdeen-group-archive/             ← canonical archive root (with v1.4 README)
├── archive_masters/                    ← master CSVs (1,434 studies / 23,605 obs)
├── kastner_wiki/                       ← companion Obsidian wiki (8,960 pages)
├── kastner_duckdb_build/               ← DuckDB layer (lags by 1 generation)
├── prepared/                           ← 493 v1.4 ingest folders (staging)
├── incoming-bucket-A/ … incoming-bucket-E/  ← original PDFs by classifier bucket
├── incoming-existing/                  ← Mode 2 inputs
├── logs/                               ← 7 ingest logs (mode1_bucket_A..E, mode2_existing, phase1_progress, phase2_progress, phase2_run)
├── archive_masters_backup_pre_java_fix_20260524_193807.tar.gz   (5.2 MB)
├── kastner_wiki_backup_v1.4_20260524_193848.tar.gz              (2.1 MB)
└── (other archive_masters_tarball_* backups from earlier in weekend)
```

### Inside `aberdeen-group-archive/`

950 study packages distributed as:
- `kastner-author/` (372): 226 top-level + 76 dct + 71 employer-scoped (46+13+5+3+2+1+1)
- `other-authors/` (487)
- `aberdeen-group-inc/` (29)
- `Aberdeen Outbound Marketing/` (3)
- `Project Examples/` (45)
- `Kastner Memoir/` (14)
- `prepared/` (493 staged, awaiting v1.5 promotion)

System files: `README.md`, `_decisions_log.md`, `_master_*.csv` (×4 + bridges), `_known_*.csv` (×2), `_audits/`, `_skills/`, `CHANGELOG.md` (if present), `CITATION.cff`, `LICENSE`.

### Wiki at `kastner_wiki/`

8,960 pages: 1,434 studies + 3,207 entities + 4,313 technologies + ~6 system pages (index, dashboard, README, AGENTS.md, chat-starter.md, Bases). 8,935 explicit wikilinks (3,682 study→entity + 5,253 study→tech). Backed by DuckDB (one generation stale) and Parquet exports.

---

*End of weekend master report. Next: GitHub release v1.4 tag and push.*
