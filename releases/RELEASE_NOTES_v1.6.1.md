# v1.6.1 — 17 video transcripts including 1988 DECtp and 2003 SARS

**Released:** 2026-06-12
**Previous release:** [v1.6.0](https://github.com/shorttack/aberdeen-group-archive/releases/tag/v1.6) (2026-05-31)
**Zenodo:** Updated DOI assigned automatically on release.

## Summary

This release adds **17 video transcripts** to the Kastner Aberdeen Archive, spanning **1988 through 2003**. The set includes Pete Kastner's internal DEC "Blue Monday" sales-training session on DECtp vs. IBM (1988) and his on-camera CNBC and NBC Nightly News coverage of the 2003 SARS outbreak's impact on the electronics supply chain.

Schema is unchanged from v1.6.0. This is a content-only release plus a major documentation reorganization (new `Perplexity_Only/` directory and `MASTERS_NOTES.md` v2).

## What's new

### 17 transcripts ingested

| year | study | type |
|---|---|---|
| 1988 | DEC "Blue Monday" — internal sales training, DECtp vs IBM | internal sales training |
| 1990 | Ingres Windows 4GL launch — GUI development tools | vendor event |
| 1996 | Informix Universal Server launch — object-relational | vendor event |
| 1996 | Sybase System XI launch — multiple databases ("boats" analogy) | vendor event |
| 1996 | Oracle Data Warehousing launch — multimedia + spatial | vendor event |
| 1996 | Software 2000 — IT paradigm shift to client-server | vendor event |
| 1997 (×4) | Crossroads — ad/buy-vs-make, ad/process-wear, launch front/back office, June launch variant | vendor events |
| 1997 | Tandem Himalayan — airport commercial, TPC-C | vendor event |
| 1997 | Informix competitive update — Kastner's "RDBMS jungle" | vendor event |
| 1997 | Portal Software Infranet — real-time billing | vendor event |
| 1998 | CNBC Technology Edge — IBM/DEC/HP transitions | broadcast |
| 1998 | MSNBC — AOL modem shortage, customer refunds | broadcast |
| 2003 | CNBC — SARS impact on electronics supply chain | broadcast |
| 2003 | NBC Nightly News — SARS economic impact, electronics | broadcast |

All 17 carry full v20 §13.1 transcript extraction (importance, relevance, prescience scoring, abstracts, observations, entities, technologies). The two SARS broadcasts are licensed `CC-BY-NC-SA-4.0`; the other 15 are `CC-BY-4.0` (the archive default).

### Data layer changes

| master | pre-release | delta | post-release |
|---|---:|---:|---:|
| `_master_studies.csv` | 1435 | +17 | **1452** |
| `_master_observations.csv` | 23631 | +295 | **23926** |
| `_master_entities.csv` | 3207 | +69 | **3276** |
| `_master_technologies.csv` | 4312 | +49 | **4361** |
| `_master_entity_studies.csv` | 3682 | +194 pairs | **3876** |
| `_master_tech_studies.csv` | 5253 | +122 pairs | **5375** |

All 295 new observation IDs follow the canonical `<study_id>-OBS-NNN` format per the §21 Universal Normalizer (introduced 2026-05-24).

### High-prescience studies

`v_studies_with_high_prescience`: 109 → **124** (+15 from the DECtp §11u Pass B earlier this cycle and prescience-scored transcripts in this batch).

### Documentation reorganization

- **New** `Perplexity_Only/` directory at repo root and at `~/Desktop/Archive/` for AI-agent operating context. See `Perplexity_Only/README.md`.
- **New** `Perplexity_Only/MASTERS_NOTES.md` (v2, 329 lines) — authoritative reference for the seven master CSVs. Supersedes the 2026-05-24 v1 (which documented a pre-2026-05-26-M:N-refactor schema and had become misleading).

## Compatibility

- **Schema:** unchanged from v1.6.0. All seven masters retain their column counts (16 / 8 / 8 / 17 / 2 / 2).
- **Build pipeline:** unchanged. Phase 1+2 (data layer) ran clean on the post-merge masters; Phase 3-6 (wiki content + embeddings) ran successfully against `~/Repos/kastner-aberdeen-wiki/`.
- **Embeddings:** Phase 5 re-run with bge-m3 (1024-dim, 6-col schema per the 2026-05-31 Phase 5 v3 fix). Re-embed required because of the 295 new observations and 17 new study pages.

## Known issues / deferred work

Carried into the next release cycle (does not block v1.6.1):

1. **2,399 non-canonical legacy observation IDs** remain in `_master_observations.csv` (8.5% of total). These predate the §21 Universal Normalizer (2026-05-24) and are tagged in `legacy_obs_id`. A batch normalizer pass is planned.
2. **Entity canonicalization sweep** — `_master_entities.csv` has known duplicate candidates (variants of the same entity not yet merged into a single canonical row).
3. **Skill amendments** for `kastner-archive-pipeline`, `archival-ingest` v20, and `kastner-new-day` to gate on `Perplexity_Only/MASTERS_NOTES.md` at thread-start — patches in progress.
4. **`kastner-archive-pipeline` §11v shape audit query** — needs `/` → `//` correction for integer-division of `decades_covered`.

## Files of interest in this release

- `archive_masters/_master_*.csv` — the six updated master tables.
- `archive_masters/archive_masters_pre_passb_v2_20260612T172545Z/` — pre-merge backups.
- `Perplexity_Only/MASTERS_NOTES.md` — **MUST READ before any masters edit.**
- `Perplexity_Only/README.md` — directory purpose.
- `scripts/apply_passb_transcripts_v2.py` — the apply script that produced this state (shipped earlier today as commit `0391dabf`).
- `RELEASE_NOTES_v1.6.1.md` — this file.
- `_decisions_log.md` — full §11u-cont Pass B narrative.

## Citation

Cite this release via the Zenodo-minted DOI (issued automatically on tag push). The Zenodo record will read:

> Kastner, P. S. (2026). *Kastner Aberdeen Archive v1.6.1 — 17 video transcripts including 1988 DECtp and 2003 SARS* [Data set]. Zenodo.

---

**Maintained by:** Pete Kastner.
**Release engineer:** Perplexity Computer (sandbox session §11u-cont).
