# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-05-28 (PM session — kw_note v1 + v2 + USER_GUIDE §6.6 shipped)
**Current ship state:** wiki `v1.5.2` (canonical layout migration + Phases 1-6 refresh + kw_ask v4); 1434/1434 studies have pub_year; 308/1434 prescience-scored; bge-m3:latest is the canonical embedding model

This is the **daily living doc**. Every session begins by reading this and proposing the next action. Items are appended as they emerge during sessions. At release time (v1.6, v1.7, ...) a versioned snapshot is saved (e.g., `future_work_v1.6.md`) and items shipped in that release are removed from here.

How to use:
- **Active items** = at the top, under "Next up" — what we're working on or about to start
- **Backlog** = below, organized by target release
- **Done this session** = bottom — gets cleared on commit at end of day

---

## Next up

_(Empty after end-of-session commit; populated at session start)_

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

### 4c. Fix the `v_studies_by_decade` view

View currently returns 38 rows — one per distinct year — with `'s'` appended (`'2003s'`, `'2004s'`, etc.). The intent was decade bucketing. **Re-confirmed in today's shape audit: still bugged.**

- [ ] Patch view definition in `02_build_data_layer_v2.py` to use `((CAST(pub_year AS INTEGER)/10)*10) || 's' AS decade`.
- [ ] Verify: `SELECT decade, COUNT(*) FROM v_studies_by_decade GROUP BY decade ORDER BY decade;` returns ~6 rows (1970s, 1980s, 1990s, 2000s, 2010s, 2020s).
- [ ] Audit `wiki/decades/*.md` and any `kw ask` decade prompts for downstream impact.

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
- [ ] Audit `~/Desktop/Archive/scripts/*.py` for any hardcoded paths to `~/Desktop/kastner_wiki/`; patch to use `--wiki` argument
- [ ] Audit `~/Repos/kastner-aberdeen-wiki/scripts/*.py` for any sandbox-path leftovers (`/home/user/workspace`, etc.) in comments or default arg values
- [ ] Patch `kastner-archive-pipeline` skill to v1.2 — ✅ DONE in this session

### 9. Schema contract enforcement

The kw_ask BinderException after Phase 5 was avoidable. Add:

- [ ] `scripts/verify.py` step that opens `data/embeddings.parquet` and asserts the column list matches what `kw_ask.py` expects. Fails loudly if not.
- [ ] Mirror assertion at the top of `kw_ask.py` so any kw user gets a readable error, not a DuckDB BinderException.
- [ ] Add to `kw verify` so the launcher catches it before the user does.

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

## Done this session (2026-05-28)

_(End-of-day commit clears this section)_

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
