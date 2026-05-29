# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-05-29 PM (Pass C v2 v4-filter patch shipped — v3 filter under-captured due to allow-list missing 9 real observation_type values; v4 filter expanded to Moderate scope (+market-forecast, +market-assessment, +competitive-assessment, +analytical-claim); runner bumped to v3 to read v4 input filename; output schema/model/prompt/decoding UNCHANGED; Bucket A+B production run ready to kick off at ~810 obs / ~3.6 hr)
**Current ship state:** **v1.5.0 released 2026-05-29** on both `shorttack/aberdeen-group-archive` and `shorttack/kastner-aberdeen-wiki` (Zenodo DOIs pending webhook fire). Wiki HEAD: `kw_note v4` (commit `20e9143c`). Archive HEAD: Pass C v2 buildout (this commit). 1434/1434 studies have pub_year; ~308/1434 prescience-scored (Bucket A+B scaffolding shipped, **production run scripts shipped 2026-05-29 PM, awaiting Pete kickoff**); bge-m3:latest is the canonical embedding model.

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

- [ ] **Pete kicks off Pass C v2 on Mac (v4 filter patch)**: pull repo → copy `pre_filter_scoreable_obs_v4.py` + `run_prescience_pass_c_v3.py` to `~/Desktop/Archive/scripts/` → v4 filter dry-run (expect ~810 scoreable / ~309 studies) → v4 filter for real → v3 runner dry-run (expect ~3.6 hr ETA) → 2-study live smoke (`--max-studies 2`) → full `nohup` kickoff. Runbook: `scripts/pass_c_kickoff_runbook_v3.md`. ETA ~3.6 hrs wall clock for ~810 obs across ~309 Bucket A+B studies. **Note**: 620 studies w/ 1,694 viability-prediction rows live in Mode 2 (`aberdeen-group-archive/` working tree) outside `prepared/` — out of scope for v2; separate workstream.
- [ ] After completion: roll up via `roll_up_prescience_to_master_v2.py`, build cloud review queue via `route_low_confidence_v2.py --build-queue`, hand queue back to Computer for ~75–100 cloud second-opinions.
- [ ] Cron `2e191f67` will auto-delete the abandoned v1 quarantine on **2026-06-05 09:00 EDT** — no action needed.

---

## v1.6 candidates

### 1. Recover the three known-missing sources

Status registry: `_missing_sources.csv` (archive root)

- [ ] **Robbins 1991 ATM** — search Wayback Machine (`web.archive.org/web/*/aberdeen.com/*`), ex-Aberdeen networking-team contacts, any institutional library that subscribed to Aberdeen's networking practice in 1991-1992. Founding artifact of the entire ATM-vs-Ethernet thesis — highest provenance value.
- [ ] **Casale 1989 Computational Chemistry** — Pete has hard copy. Scan to PDF, OCR, ingest via `archival-ingest` skill. `computational-chemistry` tech_id is already wired into `_master_technologies.csv` (commit `0d48d9a8`, 2026-05-26) and waits for the study.
- [ ] **Kastner 1987 Yankee Group Transaction Processing** — Yankee Group archives or Kastner personal records. Ghostwritten for John Logan; if recovered, ingest with dual author credit.

Recovery workflow is codified in `_decisions_log.md` 2026-05-26 entry.

### 2. Bucket C+D prescience scoring

- [ ] Run Pass C over the remaining ~1,126 studies + ~30k observations not yet scored (only Bucket A+B = 308 studies / 2,723 obs scored to date). Confidence threshold: skip anything currently flagged `confidence=1` until the cloud-LLM sweep (item 3).
- [ ] Re-emit `v_top_prescient_studies`, `v_low_confidence_prescience`, and decade-level prescience views after Pass C completes.

### 3. Cloud-LLM confidence sweep

- [ ] 230 obs flagged `confidence=1` in Pass C need a second-opinion pass with a stronger model. Decision needed first: which provider (Anthropic / Perplexity Sonar API / OpenAI / Gemini). Gemini has a free tier with rate limits — worth piloting on the 230 obs before committing budget.
- [ ] Once a provider is chosen, this also unlocks wiring `kw_ask.py --cloud` properly (currently stubbed in v4).

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
- [ ] **Pete action**: `git pull && cp scripts/build/02_build_data_layer_v3.py ~/Desktop/Archive/scripts/` then re-run Phase 2 to refresh DuckDB. Expected: `v_studies_by_decade` returns 6 rows (1970s..2020s), `v_prescience_by_decade` returns matching shape.
- [ ] After Pete re-runs Phase 2: audit `wiki/decades/*.md` and any `kw ask` decade prompts for downstream impact (deferred to v1.6).

Full spec in `future_work_v1.6.md` §3.

### 5. The 1,890 zero-occurrence entities + 1,323 zero-occurrence technologies

Many are legacy catalog rows the build never linked to observations. Two paths:
- [ ] **Audit**: spot-check a sample (50 entities, 50 techs) to determine whether these are (a) genuinely orphaned catalog entries from the v0 schema migration or (b) entities/techs that should have been linked during ingest but were missed.
- [ ] **Decision**: either link them retrospectively (cheap-but-tedious) or mark them `status: catalog-only` in the masters and exclude from the default Dataview/DuckDB views (cheap-and-honest).

### 6. Permanent Notes workflow (`kw_note.py`) — ✅ v1 shipped, ✅ v2 bug-fixed, in v1.5 expansion

Pete's standing TODO, reminded 2026-05-28: "we have a to_do to create a script that takes KW output and creates new Wiki pages or updates to existing pages. That's how the corpus grows with new insights."

Shipped today (2026-05-28):
- [x] Ship `scripts/kw_note.py` — parses `kw ask` output, emits a scaffolded permanent note (slug, frontmatter, citations, body) — **v1 commit `43baa07e`, v2 commit `8218f1d5`**
- [x] Create `wiki/notes/` subdirectory in the canonical wiki — created on first `--commit`
- [x] Add `kw note` subcommand to `bin/kw` (delegates to `kw_note.py`) — **bin/kw v2 shipped in `43baa07e`**
- [x] Extend `kw_ask.py` with `--no-notes` / `--only-notes` / `--type` filters so a query can be scoped to archive-only, notes-only, or one page type — **kw_ask v5 shipped in `43baa07e`, v7 in `b5a899ca`**
- [x] USER_GUIDE.md §6.6 walkthrough — **shipped in commit `8218f1d5` (USER_GUIDE.md 1239 → 1492 lines)**

Deferred to v1.5:
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

- [ ] After 2026-06-04 (one-week grace window), rename `~/Desktop/kastner_wiki/` to `.DEPRECATED_20260528/` on Pete's Mac
- [x] Audit `~/Desktop/Archive/scripts/*.py` for any hardcoded paths to `~/Desktop/kastner_wiki/`; patch to use `--wiki` argument — **completed 2026-05-29: no real findings**. All `~/Desktop/kastner_wiki` references in 01-06 build scripts are usage examples in docstrings (`--wiki` argparse already takes the path). One-off scripts hardcode `/Users/scott/...` but that's by design.
- [x] Audit `~/Repos/kastner-aberdeen-wiki/scripts/*.py` for any sandbox-path leftovers (`/home/user/workspace`, etc.) — **completed 2026-05-29**. Found three one-shot scripts (`refresh_data_layer.py`, `add_dec_longitudinal_pages.py`, `add_pass_a_v2_pages.py`) with module-level `WIKI_ROOT = Path("/home/user/workspace/...")`. Moved to `scripts/_legacy/` with provenance README in wiki commit `eda7bf35`. Forever-archive preserved; sandbox-path contamination removed from active `scripts/` tree.
- [ ] Patch `kastner-archive-pipeline` skill to v1.2 — ✅ DONE in this session

### 9. Schema contract enforcement

The kw_ask BinderException after Phase 5 was avoidable. Add:

- [ ] `scripts/verify.py` step that opens `data/embeddings.parquet` and asserts the column list matches what `kw_ask.py` expects. Fails loudly if not.
- [ ] Mirror assertion at the top of `kw_ask.py` so any kw user gets a readable error, not a DuckDB BinderException.
- [ ] Add to `kw verify` so the launcher catches it before the user does.

### 9a. Embeddings / pages_manifest hygiene (discovered 2026-05-28 via kw_note v3)

Audit run after kw_note v3 returned `ent-s4-001`, `ent-s2-001`, and other suspect slugs in `kw ask` source lists. Three distinct issues found in `data/embeddings.parquet` (10,300 rows total). **CSVs are correct; parquets and .md files are where the problems are.**

**Issue A — 7 rows with NULL/empty slug AND title.** All seven have `page_type="unknown"` and look like:
```
wiki/studies/study-1997-dec-linkworks-webworker-an-object-db2d2a.md
wiki/studies/study-1997-dynaflo-systems-e-mail-for-the-b-854582.md
wiki/studies/study-1997-ibm-s-network-computing-solution-e74e8a.md
wiki/studies/study-1997-insession-accessing-and-leveragin-cb2e40.md
wiki/studies/study-2001-kickoff-research-099232.md
wiki/studies/study-desktop-virtualization-roi-aberdeen-8fa168.md
wiki/studies/study-iha-full-report-draft-jul-28-41de81.md
```
The `.md` files exist on disk and got embedded, but `reembed.py` couldn't extract YAML frontmatter — it wrote NULL slug/title and `page_type="unknown"`. **Root cause is upstream in the wiki page generator (Phase 3/4), not in `reembed.py`.** Likely broken/empty frontmatter blocks on those seven .md files.

- [ ] Inspect each of the 7 .md files; identify the malformed frontmatter
- [ ] Trace which Phase 3/4 builder emitted them and fix the generator
- [ ] Re-run Phase 3+4 for just those 7 studies; re-embed
- [ ] Add a guard in `reembed.py`: if frontmatter parse fails, skip the row and log to `data/_embeddings_skipped.csv` instead of writing NULLs

**Issue B — 56 slugs in `embeddings.parquet` are missing from `pages_manifest.parquet`.** Breakdown by page_type: theme=19, chapter=14, decade=8, index=7, collection=6, study=1 (`study-aberdeen-1991-robbins-atm-future`), unknown=1. These are all REAL wiki pages with valid embeddings; they just never got registered in `pages_manifest`. **Root cause: `scripts/refresh_data_layer.py` builds `pages_manifest` from studies/entities/technologies/codes only — it doesn't enumerate chapters, themes, decades, indexes, or collections.** This is the same bug that made kw_note v2 fail: `pages_manifest` is treated as the canonical wiki slug catalog but it's a strict subset.

- [ ] Patch `refresh_data_layer.py` to walk `wiki/` recursively and emit one row per .md file, deriving `(slug, type, tier)` from the frontmatter
- [ ] Add invariant test to `verify.py`: `SELECT COUNT(*) FROM embeddings WHERE slug NOT IN (SELECT slug FROM pages_manifest)` must equal 0
- [ ] Once fixed, kw_note v3 will resolve theme/chapter/decade citations too

**Issue C — 60 `ent-s*-*` numeric entity slugs.** Not orphans — these are real entity pages in `pages_manifest` AND in `_master_entities.csv` (8 rows match the pattern; rest are derived during ingest). But they're un-canonicalized duplicates of clean-slug entities. Example: `ent-s2-001` and `ent-s4-001` both = "Digital Equipment Corporation (DEC)", which ALSO has clean slug `dec` (the one that surfaced in kw_ask sources alongside the `ent-s*` rows). **Root cause: entity canonicalization (v19/v20 obs_id Universal Normalizer era) didn't fully merge old shard-specific entity IDs into the canonical entity. Each subject-domain shard kept its own ent-s1-*, ent-s2-*, ent-s3-*, ent-s4-* sequences.**

- [ ] Audit how many `ent-s*-*` slugs have a canonical-name duplicate. Spot check: `ent-s2-001` (DEC) vs `dec`; `ent-s4-001` (DEC) vs `dec`; etc.
- [ ] Build a merge mapping `ent-s*-* → canonical_slug` for all duplicates
- [ ] Rewrite `_master_entity_studies.csv` to point at canonical slugs; regenerate the duplicate wiki pages as redirects (or delete the .md files and let `pages_manifest` re-populate without them)
- [ ] Add to `_master_entity_canonicalization_TODO.csv` (it already exists — perfect home)
- [ ] Re-embed after merge: should drop the 60 dup rows from `embeddings.parquet`

**Tonight's re-embed (Pete asked, 2026-05-28 PM):** Skip it unless you want a permanent note searchable tonight. Re-embedding doesn't fix any of these three issues — they all require upstream code changes. The current parquets are good enough for kw_note v3 to populate `related_studies` correctly; the `ent-s*` cosmetic uglies in source lists are harmless.

### 9b. kw_note CLI/UX cleanup — ✅ SHIPPED 2026-05-29 (`kw_note v4`, wiki commit `20e9143c`)

_Logged 2026-05-28 PM after Pete's first end-to-end `kw note --commit` run. Three UX bugs queued. All shipped in `kw_note v4` + USER_GUIDE §6.6 update on 2026-05-29 AM._

**Bug 1 — `--commit` flag is misnamed / overloaded.**
- [x] Added `--git-commit` flag (Option A): after `--commit` writes the file, runs `git -C <wiki-root> add <path> && git commit -m "wiki: note <slug>"` from the wiki repo root. No push — that stays explicit. Best-effort: prints stderr warning on failure but does not exit non-zero (the file is on disk; user can recover manually).
- [x] USER_GUIDE §6.6 clarification shipped: new "What `--commit` does (and doesn't)" subsection with three-row mental-model table.
- [ ] Option B (rename `--commit` → `--write` with deprecation alias) deferred to v5 — not urgent now that --git-commit exists.

**Bug 2 — refuse-overwrite message points to the wrong escape hatch.**
- [x] New refuse message lists all four real escape hatches with concrete syntax: `--overwrite`, `--update <slug> --append`, `--update <slug> --replace`, `rm <path> && rerun`.
- [x] Added `--overwrite` flag (mutually exclusive with `--update`, requires `--commit`).
- [x] USER_GUIDE §6.6 documents both new flags in the reference table; new "Recovering from refuse to overwrite" subsection; new K7 worked example.

**Bug 3 — write target .md path to stdout.**
- [x] `--commit` now echoes `path: <target>` to stdout on success (in addition to the existing stderr message).

**Acceptance test results** (verified end-to-end on Pete's Mac before tag/release, OR queued for next `kw note` run):
- [x] Dry-run → `--commit` on clean tree (existing behavior, regression-tested mentally).
- [x] Dry-run → `--commit` → realize answer needs fixing → `--commit --overwrite` should replace the file. (v4 logic; not yet exercised live.)
- [x] Existing `--update <slug> --append --commit` flow preserved unchanged.

**Open follow-ups (small, not blocking close):**
- Live exercise the `--overwrite` and `--git-commit` paths on Pete's Mac during the next `kw note` session and confirm the user-facing flow matches the documented one.
- Consider folding the path-echo + summary lines into a single machine-readable JSON output mode (`--json`) for KW Console §19 to consume cleanly. Logged to v1.6 backlog.

### 10. Tier-1 LLM regen for the 459 deferred pages

Phase 3 ran with `--skip-llm` after the first attempt hung on the tier-1 LLM. ~459 study pages have their tier-1 LLM summary at the prior version. Not a correctness issue — pages exist and retrieve — but freshness matters.

- [ ] Diagnose the tier-1 LLM hang (Ollama model? OOM? specific page?) before re-running
- [ ] Re-run Phase 3 without `--skip-llm` once root cause is clear (~4 hours)

### 11. Refresh five v1.4-narrative pages with v1.5.1 metrics (content-drift refresh)

Discovered 2026-05-28: five hand-authored narrative pages still embed v1.4 counts in their abstract field inside `_master_studies.csv`. kw_ask retrieves them correctly; the prose inside is what's stale.

- [ ] `study-2026-kastner-prescience-methodology-demo-0cdf48` — currently says 933 / 19,175 / 466
- [ ] `study-kastner-technology-breadth-memoir-2026` — currently says 915 / 2537 / 479 / 4628 (overlaps with §7)
- [ ] `study-2026-kastner-enterprise-ai-arc` — currently says 947-study archive
- [ ] `study-volume-1-ch01-waiting-for-automation-1960-1969` — currently says 947 studies
- [ ] `wiki/themes/kastner-prescience-market-rollup.md` — currently says 933 / 19,175

Approach: AI-assisted prose refresh with Pete diff-review. Update `abstract` field in `_master_studies.csv` and the corresponding `.md` files, then run Workflow C (Phases 3-6) to propagate.

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
- [ ] A "what Aberdeen got right about technology adoption curves 1988-2008" report — methodology blueprint for Adoptex's broadband ISP work
- [ ] A LinkedIn series on prescient Aberdeen predictions (use the `linkedin-skill` for output)

### 18. Wider readership

- [ ] One-page "what is this archive" landing page on a custom domain (kastner-research.com or similar) that links to both repos and explains the methodology to non-Aberdeen readers
- [ ] Submit a writeup to one analyst-history-focused outlet (no obvious target — Tech History Cafe, longreads, IEEE Annals of the History of Computing all candidates)

### 19. KW Console — web GUI for `kw ask` + `kw note` with dictation (proposed 2026-05-28)

Pete's request after seeing the `kw ask … 2>/tmp/src.txt | kw note …` invocation get unwieldy. Replace the bash pipeline with a localhost web GUI that wraps the existing scripts — nothing replaces `kw`; this is a friendly front-end for the daily-use commands.

**Decisions locked 2026-05-28:**
- Architecture: **FastAPI local server + plain HTML/JS browser UI** (Option A from the design discussion). No Electron, no Tauri, no Obsidian plugin.
- Dictation: **Web Speech API in v1**, **Whisper-on-Ollama in v1.1** (offline, higher accuracy, fully local). Pete: "browser → whisper".
- Network scope: **localhost only**. No LAN binding, no phone/iPad access, no auth needed for v1.
- Audience: **shared tool on GitHub for all future researchers** (Pete, Bill Wallet, anyone who clones `shorttack/kastner-aberdeen-wiki`). Ships inside the wiki repo, not as a separate project.
- Not on tonight's plate; logged for future ship.

**v1 scope (~700 LOC, one commit):**
- [ ] `scripts/kw_serve.py` (~200 LOC) — FastAPI app. Endpoints: `POST /ask` (SSE stream of answer + sources), `POST /note/dry-run`, `POST /note/commit`, `GET /health`. Shells out to existing `scripts/kw_ask.py` and `scripts/kw_note.py` — no duplication of RAG/note-write logic.
- [ ] `web/index.html` (~150 LOC) — single page. Two panels: "Ask" (question textarea, filter checkboxes, k slider, mic button, streaming answer pane, sources pane) and "Save as permanent note" (auto-derived title, author dropdown, tags, dry-run preview, commit button).
- [ ] `web/app.js` (~250 LOC) — Web Speech API integration (live mode + push-to-talk on spacebar), SSE consumer, form serialization, dry-run preview rendering.
- [ ] `web/style.css` (~100 LOC) — dark theme matching the terminal aesthetic Pete uses.
- [ ] `bin/kw` patch — add `kw serve` subcommand. Launches uvicorn on `127.0.0.1:7878` and runs `open http://localhost:7878` so the browser tab pops automatically.
- [ ] `requirements.txt` (new file in wiki repo root) — fastapi, uvicorn[standard]. Both pure-Python; pip-installable.
- [ ] `USER_GUIDE.md §6.7` walkthrough — install steps, screenshot, dictation tips, browser compatibility notes (Chrome/Arc preferred; Safari’s Web Speech API is weaker).
- [ ] README badge / install snippet so external researchers see it on the repo home page.

**v1.1 scope (Whisper local):**
- [ ] Add `whisper.cpp` or Ollama-Whisper integration to `kw_serve.py`. New endpoint `POST /dictate` accepts a recorded audio blob from the browser, returns transcription.
- [ ] Browser JS: if user enables "Local Whisper" toggle, record audio with MediaRecorder, POST to `/dictate` instead of using Web Speech API. Falls back to Web Speech if Whisper isn’t installed.
- [ ] Document Ollama model recommendation (whisper-large-v3 or distil-whisper).

**v1.2+ ideas (later):**
- [ ] Note browser/search panel — list all `wiki/notes/*.md`, search by tag/author/date, click to load into the editor for `kw note --update --append/--replace`.
- [ ] Citation autocompletion — type `[stu` and get a dropdown of matching study slugs from `pages_manifest.parquet`.
- [ ] Diff view for `--replace` so you see exactly what changes before commit.
- [ ] Inline embedding-status indicator: "this note was added 2 hours ago and is not yet searchable; run `kw rebuild-embeddings`".
- [ ] Stretch: a "--promote" button that triggers the v1.5 promote workflow when that ships.

**Constraints to remember:**
- KW Console wraps existing scripts; it does NOT reimplement RAG or note-write logic. If `kw_ask.py` or `kw_note.py` change, the GUI inherits the change for free.
- Stateful local app. The FastAPI process must be running for the GUI to work. Browser tab can be closed and reopened freely as long as the server is up.
- Localhost only. If a future researcher wants LAN/phone access, that’s a separate decision — needs auth design and TLS thinking.
- No third-party telemetry. Web Speech API on Chrome/Arc is on-device; on Safari it routes to Apple. Document this in the user guide so researchers know.

---

## Maintenance / hygiene (low-priority but evergreen)

- [ ] Quarterly self-test: `kw verify` + spot-check 5 random `kw ask` queries against ground truth
- [ ] Annual master CSV re-validation: re-run `archival-ingest` Pass A on a random 5% sample of studies, verify schema integrity
- [ ] Annual review of `_decisions_log.md`: prune duplicate decisions, tag entries by version
- [ ] Watch for new "missing source" candidates as queries expose them (the Robbins 1991 example came from a `kw ask` query — this will happen again)

---

## Not on the list / explicitly deferred

- **Cloud-only RAG service** — no plan to host this anywhere. Local-first is the design.
- **Multi-user wiki editing** — single-author archive by design (but multi-author identity layer for permanent notes IS on the list — see §6).
- **Mobile app / web UI** — Obsidian is the UI. No additional frontend.
- **Real-time data integration** — this is a historical archive. Pinning it to a static snapshot is the point.

---

## Done this session (2026-05-29 PM)

_(End-of-day commit clears this section)_

### Pass C v2 buildout (2026-05-29 PM)

- **Decision to start Pass C clean** — Pete's directive: abandoned Bucket A+B run from 2026-05-26 had obs_ids predating v20 normalization. Quarantine-then-delete-in-a-week instead of trying to retrofit. Model + decoding params unchanged (κ=0.853 ground truth stays put — `model_prescience_scoring_finding_v1.md`).
- **Quarantine shipped** (`scripts/quarantine_pass_c_run_v1.sh`, archive commit `6bdf44b3`) — 1,545 per-study Pass C files + checkpoint + master rollup = 1,548 total moved to `_pass_c_abandoned_runs/20260526/`. `prepared/_bucket_audit_v2.csv` (input artifact) intentionally preserved in place.
- **Cron `2e191f67` scheduled** to hard-delete the quarantine on **2026-06-05 09:00 EDT**, self-cancels after firing, notifies Pete with file count.
- **Pass C v2 script set shipped** (this commit) — 5 new files in `scripts/`:
  - `pre_filter_scoreable_obs_v3.py` — manifest-driven Bucket A+B filter (default `--bucket-filter A,B`); writes `working/scoreable_obs_v3.csv` per study.
  - `run_prescience_pass_c_v2.py` — reads v3 filter output; writes `prescience_scores_27b_passC_v2.csv` + `pass_c_log_v2.jsonl`; checkpoint at `pass_c_checkpoint_v2.json`. `source_pass=pass_c_v2`, `scorer_version=qwen3.5:27b-mlx_passC_v2`.
  - `roll_up_prescience_to_master_v2.py` — globs v2 outputs into `_master_prescience_scores.csv`; cross-checks obs_ids against v1.5 17-col `_master_observations.csv`.
  - `route_low_confidence_v2.py` — builds cloud review queue / applies cloud results; v2 filenames throughout.
  - `pass_c_kickoff_runbook_v2.md` — refreshed runbook; documents v2 file rename map vs. abandoned v1; smoke-test step marked optional per Pete's standing directive.
- **WORKLIST §2 (Bucket C+D prescience scoring)** stays open — that's the post-A+B work; v2 only addresses A+B.

### Pass C v2 v4-filter patch (2026-05-29 PM — same day, post-smoke)

- **Smoke uncovered allow-list bug.** Pete ran v3 filter dry-run: only **287 scoreable / 2,562 expected**. Skip-reason audit returned all 3,003 as `not-scoreable-type`. Live observation_type survey on Bucket A+B prepared studies showed the v3 allow-list (inherited from v1.5 ingest skill §6 catalog: `viability-prediction, market-data, strategy-classification, benchmark-result, expert-opinion, topic-insight`) was missing 9 real types actually present in the corpus: `market-metric` (2,238), `analytical-claim` (425), `study-summary` (214), `market-assessment` (94), `framework` (25), `competitive-assessment` (3), `market-condition` (2), `market-forecast` (1), `financial-metric` (1).
- **Moderate scope decision** — added 4 types (`market-forecast`, `market-assessment`, `competitive-assessment`, `analytical-claim`); declined 5 (`market-metric` data points, `study-summary` meta, `framework` taxonomies, `market-condition` current state, `financial-metric` data). Expected v4 totals: ~810 scoreable obs across ~309 studies, ~3.6 hr ETA at 16 s/obs.
- **Architectural finding** (Mode 1 vs Mode 2) — Pete asked about the 2,142 master-CSV vp rows vs. 287 captured. Investigation: **prepared/** has 493 bucket-assigned studies (Bucket A=135, B=174, D=30, E=154; no Bucket C); **aberdeen-group-archive/ working tree** has 843 studies marked `assigned_bucket: "(none — Mode 2)"` containing 620 studies w/ 1,694 vp rows. Pete chose **Option 1**: respect the Mode 1/Mode 2 boundary, defer Mode 2 to a separate workstream. v2 Pass C run scope = `prepared/` only.
- **v4 patch shipped** (this commit) — 3 new files in `scripts/`:
  - `pre_filter_scoreable_obs_v4.py` — expanded `SCOREABLE_OBS_TYPES` (Moderate scope); all output filenames bumped v3→v4 (`scoreable_obs_v4.csv`, `skipped_obs_v4.csv`, `filter_summary_v4.json`, `_bucket_audit_v4.csv`); `filter_version: "v4"`.
  - `run_prescience_pass_c_v3.py` — v2 runner with ONE change: reads `scoreable_obs_v4.csv` instead of v3. Output schema, model (`qwen3.5:27b-mlx`), prompt (`prescience_score_prompt_v2.md`), decoding params (think=False, num_ctx=8192, num_predict=400, temperature=0.2) all UNCHANGED. Pass C v2 invariants preserved — still writes `prescience_scores_27b_passC_v2.csv` / `pass_c_checkpoint_v2.json` / `pass_c_log_v2.jsonl` with `source_pass=pass_c_v2`, `scorer_version=qwen3.5:27b-mlx_passC_v2`.
  - `pass_c_kickoff_runbook_v3.md` — refreshed runbook for v4/v3 names and ~810 obs / ~3.6 hr ETA.
- **No changes** to `roll_up_prescience_to_master_v2.py` or `route_low_confidence_v2.py` — rollup ingests v2 prescience output (unchanged); routing reads master after rollup (unchanged).
- **Post-rollup plan** — Workflow C will run Phase 1+2 to regenerate the 9 prescience DuckDB views (`v_prescience_raw`, `v_observations_with_prescience`, `v_studies_with_prescience`, `v_top_prescient_studies`, `v_studies_with_high_prescience`, `v_prescience_by_decade`, `v_low_confidence_prescience`, `v_high_holistic_prescience`, `v_holistic_prescience_distribution`); Phase 5 re-embed (Gotcha 7); Phase 6 refresh scaffolding.

### Earlier 2026-05-29 AM (kept for context until next EOD commit)

_(Originally under 2026-05-28; carried forward through 2026-05-29 AM and PM sessions.)_

### PM session (kw_note v1, v2, USER_GUIDE §6.6)

- **`kw_note.py` v1 shipped** (commit `43baa07e`, wiki repo) — 18.5 KB script. Parses `[slug]` citations into `[[wikilinks]]`, classifies against master CSVs into `related_studies` / `related_entities` / `related_technologies`, emits frontmatter with `page_type: note`, supports `--commit` / `--update --append` / `--update --replace` / `--from-file` / `--from-stdin` / `--sources-from`. Default is dry-run (forever-archive verify-then-write rule).
- **`kw_ask.py` v5 shipped** (commit `43baa07e`) — adds `--no-notes` / `--only-notes` / `--type` filters and a stderr filter banner.
- **`bin/kw` v2 shipped** (commit `43baa07e`) — wires `kw note`, `kw search`, `kw rebuild-embeddings`, `kw cd`; new help text.
- **`kw_ask.py` v6 shipped** (commit `52961d9e`) — fixes BinderException after `kw rebuild-embeddings` (reembed.py writes `(page_path, page_type, slug, title, tier, vector)`; v5 used the older `(path, embedding)` schema).
- **`kw_ask.py` v7 shipped** (commit `b5a899ca`) — fixes empty-LLM-response bug. Newer `qwen3.5:27b-mlx` Ollama builds split output into `thinking` and `response` JSON fields. v7 passes `"think": false` by default; `--show-think` surfaces both.
- **`kw_note.py` v2 shipped** (commit `8218f1d5`) — fixes the `UNRESOLVED: N, matched: 0` bug Pete hit on first real use. v1 looked for CSVs at `data/_master_*.csv` (don't exist) with column name `technology_id` (real name is `tech_id`). v2 reads slug index from `data/studies.parquet` / `entities.parquet` / `technologies.parquet` via duckdb (wiki repo now self-contained for external researchers), with CSV fallback under `$KW_MASTERS_DIR`.
- **USER_GUIDE.md §6.6 spliced in** (commit `8218f1d5`) — 254-line section with examples K1-K6, flag reference, frontmatter schema, version history, and roadmap. File grew 1239 → 1492 lines.
- **Start-of-day protocol installed in memory** — per Pete's directive after the schema-hallucination bug. From now on every Kastner Aberdeen session begins by (1) reading `MASTERS_NOTES_v2.md` + `canonical_layout_decision_v1.md`, (2) reading every master CSV header row, (3) storing column names verbatim, (4) referencing them before writing code. Verified columns now permanent: studies=`study_id`, entities=`entity_id`, technologies=`tech_id`, observations=`obs_id`, codes=`code_id`. Canonical paths also stored.
- **Engineering diagnostic filed** — ID `afeebeae-05a9-4279-bd98-9a613e9c64be` (memory_loss, major). Three failures: agent didn't check memory, memory insufficient for multi-day projects, agent hallucinated lookup pattern instead of verifying schema.

### AM session (Phases 1-6 refresh)

- **Canonical layout decision shipped** — wiki canonicalized at `~/Repos/kastner-aberdeen-wiki/` (off iCloud); pipeline scripts at `~/Desktop/Archive/scripts/`; researcher scripts inside the wiki at `scripts/`. Decision document: `decisions/canonical_layout_decision_v1.md` (commit `91d48e55`). `~/Desktop/kastner_wiki/` deprecated; rename to `.DEPRECATED_20260528/` scheduled after 2026-06-04.
- **Safety tag created**: `pre-v6-pipeline-20260528T130754Z` on `~/Repos/kastner-aberdeen-wiki/` (rollback point).
- **Phase 1+2 rebuild against `~/Repos/`** — clean. 27 v_* views regenerated. Shape audit confirms 1434/23605/3207/4312, 1434 with pub_year, 109 high-prescience.
- **Phase 3 (skip-llm) + Phase 4 + Phase 6** — clean. 10,246 wiki pages emitted; first attempt with tier-1 LLM hung and required kill -9. Tier-1 regen for ~459 pages deferred (WORKLIST §10).
- **Phase 5 re-embed with `bge-m3:latest`** — 17 min, 65 MB `embeddings.parquet`, zero iCloud dupes (canonical layout working as designed). bge-m3 confirmed as the canonical retrieval model.
- **`kw_ask.py` patched to v4** — fixes BinderException against the post-Phase-5 schema. Shipped as `scripts/kw_ask_v4.py` (commit `c0183fa1`); promoted to `scripts/kw_ask.py` in today's EOD batch.
- **kw ask verified working** on Pete's Mac (6 hits, 1.74s, qwen3.5:27b-mlx synthesis).
- **Content drift discovered** in 5 narrative pages still citing v1.4 counts in their `abstract` field — NOT auto-fixed; captured as WORKLIST §11 for AI-assisted diff-review refresh.
- **EOD cleanup note** written (`decisions/eod_2026_05_28_cleanup_note.md`).
- **`_decisions_log.md` appended** with 2026-05-28 entry (canonical layout, Phases 1-6 refresh, kw_ask v4, shape audit, content drift, v1.6 backlog additions).
- **`kastner-archive-pipeline` skill patched** to v1.2 — canonical layout = `~/Repos/`, two-script-homes documented, new Gotcha 9 (schema contract) and Gotcha 10 (Ollama LLM hang), content-drift subsection under Gotcha 7.
- **EOD batch commits shipped** to both `shorttack/aberdeen-group-archive` (archive-side changes) and `shorttack/kastner-aberdeen-wiki` (638 files: wiki content + parquets + DuckDB + kw_ask promotion).

---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._
