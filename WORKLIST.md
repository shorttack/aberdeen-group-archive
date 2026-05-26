# Kastner Aberdeen Archive — Active Worklist

**Last updated:** 2026-05-26 (end of session)
**Current ship state:** wiki `v1.5.1` (commit `23c01603`) + kw_ask.py v3 + provenance-gap system live

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
- [ ] Once a provider is chosen, this also unlocks wiring `kw_ask.py --cloud` properly (currently stubbed in v3).

### 4. Fill the 350 missing `pub_year` values

- [ ] 24% of studies lack a parseable publication year. Some are in filenames, some in PDF metadata, some buried in body text.
- [ ] Build a single-purpose script: rip dates from PDF metadata + first-page header + filename, run through the same date-extractor used in `extract_missing_dates_script` (workspace).
- [ ] Re-run decade-rollup queries after the fill.

### 5. The 1,890 zero-occurrence entities + 1,323 zero-occurrence technologies

Many are legacy catalog rows the build never linked to observations. Two paths:
- [ ] **Audit**: spot-check a sample (50 entities, 50 techs) to determine whether these are (a) genuinely orphaned catalog entries from the v0 schema migration or (b) entities/techs that should have been linked during ingest but were missed.
- [ ] **Decision**: either link them retrospectively (cheap-but-tedious) or mark them `status: catalog-only` in the masters and exclude from the default Dataview/DuckDB views (cheap-and-honest).

---

## v1.7 candidates

### 6. Cloud provider wiring for `kw_ask.py`

Currently `--cloud` exits cleanly with a "not available" message. Wire one provider — Gemini free tier is the lowest-cost entry point. Patches:
- [ ] `kw_ask.py` v4: `--cloud` calls Gemini via `requests`, reads `GEMINI_API_KEY` from env
- [ ] USER_GUIDE.md §6.5: lift the "reserved" caveat, document setup
- [ ] Decisions log entry

### 7. Incremental embeddings

`scripts/reembed.py` walks every `wiki/**/*.md` on every run (~12 min). For routine updates (one new stub page, one corrected fact) this is overkill.
- [ ] Patch `reembed.py` to support `--incremental`: check page mtimes against `embeddings.parquet`'s build timestamp, re-embed only the delta
- [ ] Add `kw rebuild-embeddings --incremental` as the launcher default; full re-embed via `--full`

### 8. Memoir Volume 2 ingest

Volume 1 chapter pages shipped in v1.5.1. If/when Pete writes or finalizes Volume 2:
- [ ] Add `wiki/volume-2/` directory + per-chapter pages
- [ ] Extend the themes taxonomy if new themes emerge
- [ ] Update `_collection_stats.csv`

### 9. Patent / IP corpus

Pete's archive interests include patent strategy. Consider a parallel `wiki/patents/` directory if patent docs become part of the corpus.

---

## v1.8+ / strategic

### 10. Public release strategy

- [ ] Decide what (if anything) of `kastner-restricted-sources` ever moves to public. Most-likely candidates: anything older than ~30 years where copyright posture is benign.
- [ ] Add a `LICENSE_REVIEW.md` to the archive that tracks copyright status per source.

### 11. Adoptex × Aberdeen archive cross-pollination

The Aberdeen archive's prescience scoring methodology could feed Adoptex's AI-adoption-readiness frameworks. Possible deliverables:
- [ ] A "what Aberdeen got right about technology adoption curves 1988-2008" report — methodology blueprint for Adoptex's broadband ISP work
- [ ] A LinkedIn series on prescient Aberdeen predictions (use the `linkedin-skill` for output)

### 12. Wider readership

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
- **Multi-user wiki editing** — single-author archive by design.
- **Mobile app / web UI** — Obsidian is the UI. No additional frontend.
- **Real-time data integration** — this is a historical archive. Pinning it to a static snapshot is the point.

---

## Done this session (2026-05-26)

_(End-of-day commit clears this section)_

- v1.5.1 close-out: decisions log entry, USER_GUIDE.md §6.5 (`kw ask` cookbook), kastner-github skill updates (iCloud trap, force-push policy)
- kw_ask.py v3 (stub `--cloud` with clean error)
- Missing-source provenance system shipped: `_missing_sources.csv` + Robbins 1991 stub page + 3 cross-link backlinks (atm, atm-networking, decades/1990s)
- `_master_technologies.csv` +1 row (`computational-chemistry`), pre-change backup under `archive_masters_pre_compchem_20260526T203955Z/`
- Workflow plan established: this WORKLIST.md + daily-session protocol in `kastner-github` skill

---

_Owner: Pete Kastner. Updates inline during sessions; end-of-day commit clears "Done this session" and refreshes "Last updated"._
