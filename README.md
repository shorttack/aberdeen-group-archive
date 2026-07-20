# Kastner IT Research Archive

[![DOI](https://zenodo.org/badge/1181715405.svg)](https://doi.org/10.5281/zenodo.20245076)

A structured archive of research studies, articles, memoirs, and related artifacts spanning **1979–2026**, centered on the work of **Peter S. Kastner** at Aberdeen Group, Arthur D. Little, Philip Hankins Inc. (PHI), Digital Equipment Corporation, Stratus Computer, and Obian Group, plus contributions from other Aberdeen analysts.

Every study is packaged as a self-contained [Frictionless Data Package](https://frictionlessdata.io/), with structured CSV tables, a JSON descriptor, a Schema.org dataset descriptor, and a human-readable README.

Kastner had the prescience to save much of his work in digital form; about one-third has survived. It is all in this "Kastner Research Archive".

**v2.1 — "Complete Long-Horizon Prescience Scoring"** (2026-07-18)

> **All corpus counts live in one generated file: [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md)** (written by `scripts/generate_archive_stats.py` from the live DuckDB, refreshed on every rebuild). This README no longer hard-codes numbers — see that file for current studies / observations / entities / technologies / prescience surfaces / embedding pages. When in doubt, `_master_*.csv` is truth and `ARCHIVE_STATS.md` is its generated summary.

The archive spans **1972–2026** across **6 decades**, centered on Peter S. Kastner's work.

New in v2.1: the long-horizon (holistic) Pass C scoring is now **complete across the corpus**. A full backlog sweep scored the previously-unscored gradeable observations, and study-level verdicts were recomputed by Rule A on the now-complete score set. This recalibrated the holistic verdict distribution materially: the `study_prescience_enum = 'high'` surface fell sharply from its v2.0 level, because many prior "high" verdicts had been computed on partial (sampled) scoring and did not survive full evaluation. The 24 memoir chapters (`type = memoir`) retain their curated verdicts and were excluded from the recompute. This is a data/scoring release — no schema change (studies master stays 20 cols). The v2.0 short-horizon (3y/5y) layer is unchanged. Current numbers: [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md). See also [`RELEASE_NOTES_v2.1.md`](./releases/RELEASE_NOTES_v2.1.md).

---

## For Researchers

The archive is organized by who wrote each study and, for Peter S. Kastner's own work, by which employer he was at when the study was produced. Most readers will start in `kastner-author/` and drill into the employer subdirectory of interest.

### Key reading paths

- **`kastner-author/employer/aberdeen-group/`** — Kastner's published Aberdeen Group analyst work (1988–2007 core), including the SOA / BPM / EII / outsourcing series of 2003–2007; **46 studies**.
- **`kastner-author/employer/stratus-computer/`** — Stratus Computer marketing/sales-support era (1981–1985), including corporate overviews, fault-tolerant market analyses, the Stratus-Tandem competitive series, and Kastner's June 1983 IEEE *Database Engineering Bulletin* technical article on the Stratus/32 architecture; **13 studies**.
- **`kastner-author/employer/DEC/`** — Digital Equipment Corporation engineering, competitive-marketing, and OLTP/Debit-Credit performance memos (1986–1989); **5 studies**.
- **`kastner-author/employer/arthur-d-little/`** — ADL consulting engagements (1972–1979), including 9-1-1 / CAD public-safety systems and the ASE/ASEP two-way power-line communications study; **3 studies**.
- **`kastner-author/employer/phi-computer-services/`** — PHI Computer Services (1969–1972) and the 1995 Wang Labs *Riding the Runaway Horse* retrospective; **2 studies**.
- **`kastner-author/employer/prime-computer/`** — Prime Computer Market Planning era (1979–1981), built around the July 15, 1981 *Industry Product Requirements Plan* — the principal surviving Kastner-authored five-year strategic plan covering all Prime vertical markets, seven System Use Categories, and the 1981 product-gap priority list against DEC VAX; **1 study**.
- **`kastner-author/employer/obian-group/`** — Obian Group consulting engagements; **1 study**.
- **`kastner-author/dct/`** — Digital Consumer Technology (DCT) studies, **76 entries**.
- **`kastner-author/`** (top-level) — **226 studies** that pre-date the employer-scoped reorganization or sit outside any single employer (memoirs, AI responses, technology topics, expert reports, video transcripts, the Top-100 Economic Calls ranking, and the Prescience Methodology Demo).
- **`other-authors/`** — **487 studies** authored by other Aberdeen analysts and outside writers.
- **`prepared/`** — **493 newly-ingested studies** from the May 2026 weekend bucket pass. These are fully registered in the masters and indexed in the companion wiki, but physically remain in this v1.4 staging directory pending classification into `kastner-author/`, `other-authors/`, or `employer/` subtrees. Promotion is tracked as a v1.5 backlog item.
- **`Project Examples/`** — **45 client-engagement studies** (Maxtor Midline Storage RAMP, Sun AS/400 RAMP, the 2026 Kastner Technology Breadth Memoir, etc.) showing the full Aberdeen RAMP methodology in action and the meta-narrative of the archive's coverage.
- **`aberdeen-group-inc/`** — Aberdeen Group corporate / about-the-company files; **29 studies**.
- **`Aberdeen Outbound Marketing/`** — Period marketing collateral as analyzable studies; **3 studies**.
- **`Kastner Memoir/`** — Volume 1 of *Arguments with Reality: Fifty Years in Computing, Consulting, and Consequence* (2026), split into 14 chapter-level study packages (Introduction + 10 chapters + Epilogue + About + Appendix); **14 studies**, 1,242 observations covering 1960–2026.

### Companion wiki: Kastner Aberdeen Wiki

A second-pass deliverable built directly from this archive's master CSVs.

- **Format**: Obsidian vault + DuckDB query layer + Parquet exports + bge-m3 embedding index (1024-dim).
- **Pages**: study, entity, tech, and code pages plus decade/theme/collection/index pages, all rebuilt against the v2.0 masters. Study pages now carry a **Short-horizon prescience** section rendering the 3y/5y verdicts so `kw ask` can answer horizon questions from retrieved text.
- **Embedding index**: bge-m3 (1024-dim), **10,944 pages** re-embedded (Phase 5).
- **Cross-linking**: Every study page emits `[[entity-slug]]` and `[[tech-slug]]` wikilinks, powering Dataview reverse-lookups on every entity and technology page.
- **Local-first**: Lives at `~/Repos/kastner-aberdeen-wiki/` on the build host (migrated from `~/Desktop/kastner_wiki/` on 2026-06-01 to escape iCloud Desktop sync). Opens in Obsidian, queryable from DuckDB, browsable from Python/pandas via the Parquet exports.
- **Builder skill**: `kastner-wiki-builder` (custom user skill).
- **GitHub mirror**: [shorttack/kastner-aberdeen-wiki](https://github.com/shorttack/kastner-aberdeen-wiki) — same v2.0 tag.

### Prescience ratings

Each study is rated for the prescience of its forecasts when checked against subsequent history. **Current distribution counts: [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md).**

Three prescience surfaces are exposed in `v_studies`, and they measure different things:

- **`study_prescience_enum`** — the Rule-A *mean* verdict (high / medium / low / not-applicable). The scorer makes the call; verdicts are not hand-overridden. This is the holistic headline verdict. (Recalibrated in v2.1: after complete backlog scoring, the `enum = 'high'` surface fell sharply from its v2.0 level, because the earlier figure rested on partial scoring.)
- **`prescience_max ≥ 4`** (loose) — flags any study with at least one observation scored 4–5. This is what the `v_studies_with_high_prescience` view filters on, and what the "high-prescience studies" corpus headline refers to.
- **`prescience_mean ≥ 3.5`** (tight) — the strictest mean threshold.

Pick the surface that fits your question. Exact current counts for all three are in [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md).

### Short-horizon prescience (3-year / 5-year)

v2.0 added fixed-window prescience reads alongside the holistic verdict (unchanged in v2.1). Every gradeable observation is scored at **3 years** and **5 years** after its anchor year, with rolled-up `prescience_3y_enum` / `prescience_5y_enum` study verdicts. Current 3y/5y verdict counts and the per-horizon high/medium/low distribution live in [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md) and the `v_sh_3y_distribution` / `v_sh_5y_distribution` views.

The observation-level scores live in `_master_prescience_short_horizon.csv` and are exposed as `v_prescience_sh`, `v_studies_with_sh_verdicts`, `v_observations_with_sh`, `v_sh_3y_distribution`, and `v_sh_5y_distribution`. Sentinel values: `-1` = prefiltered / parse-reject; `-2` = window not elapsed. Both are excluded from verdict means.

### Aberdeen Group Category Creator roster

Eight Aberdeen analysts are credited with creating practice areas at the firm. Their entity rows in this archive carry an `Aberdeen Group Category Creator: …` prefix in `notes`, credited by Peter S. Kastner. Stephen Defranco and Kastner created "midline storage" and Hill and Kastner created "Pools of Storage" categories.

| Analyst | Practice |
|---|---|
| David Hofferberth | PSA |
| Christopher Fletcher | CRM |
| Jack Maynard | EAS |
| Valerie O'Connell | Enterprise Management |
| Wayne Kernochan | Platform Infrastructure |
| Joyce Becknell + James Gruener | Platforms Group |
| David Alschuler | B-to-B e-Business & SCM |
| Tim Minahan | Supply Chain Management / e-Procurement / e-Sourcing |

### Citing a study

Each study's `datapackage.json` carries a stable `study_id` and a Schema.org `Dataset` descriptor in `schema/schema_org.json`. Cite by `study_id` plus the path to the package directory. See citation rules below.

### License & citation

Structured artifacts (CSVs, descriptors, code, schemas, READMEs) are released
under **CC-BY-4.0** — see [`LICENSE`](./LICENSE) for the full text. Original
source content (analyst studies, trade-press articles, vendor brochures,
photographs, etc.) remains the property of its respective rights holders.

For academic / data-set citation, use [`CITATION.cff`](./CITATION.cff) or:

> Kastner, Peter S. (2026). *Kastner IT Research Archive*, version 2.0.
> Licensed under CC-BY-4.0. DOI: 10.5281/zenodo.20245076.

Version history is in [`CHANGELOG.md`](./CHANGELOG.md). Curatorial decisions and data-hygiene history are in [`_decisions_log.md`](./_decisions_log.md).

---

## For Data Engineers / Analysts

### Top-level layout (v2.0)

```
aberdeen-group-archive/
├── _master_studies.csv          #   20 cols — index of all studies (incl. 3y/5y enums)   [row counts: ARCHIVE_STATS.md]
├── _master_entities.csv         #   per-study entity rows
├── _master_technologies.csv     #   per-study technology rows
├── _master_observations.csv     #   every observation
├── _master_prescience_scores.csv  # obs-level holistic scores (Pass C)
├── _master_prescience_short_horizon.csv  # obs-level 3y/5y scores (SH sweep, v9)
├── _master_player_rebuttals.csv  # author rebuttals of scorer verdicts (Path B)
├── _master_tech_studies.csv     # tech_id → study_id bridge
├── _master_tech_field_conflicts.csv  # tech-field conflict audit
├── _master_tech_canonicalization_TODO.csv  # tech_id canonicalization queue
├── _known_entities.csv          #   3,300 rows — deduped entity cache (root)
├── _known_technologies.csv      #   4,371 rows — deduped technology cache (root)
├── _decisions_log.md            # Curatorial decisions and data-hygiene history
├── WORKLIST.md                  # Current session worklist (release-facing)
├── CHANGELOG.md  ·  CITATION.cff  ·  LICENSE  ·  .zenodo.json
├── _skills/                     # Frozen copy of the archival-ingest skill (v20)
├── releases/                    # v2.0 reorg — RELEASE_NOTES_v*.md, future_work_v*.md, RESUME_2026_*.md
├── reports/                     # v2.0 reorg — audit/validation outputs
│   ├── _audits/                 #   Referential-integrity audit reports
│   ├── _validation_log.csv  ·  _rebuild_diff_report.csv  ·  _collection_stats.csv
│   ├── _missing_sources.csv  ·  _skipped_sources.md  ·  PASS_A_VERIFICATION_REPORT.md
│   ├── _web_cache.json  ·  _web_verification_results.json
│   └── *_audit_*.csv  ·  model_prescience_scoring_finding_v1.md  ·  _master_entity_field_conflicts.csv
├── data_sources/                # v2.0 reorg — *_processed.zip source bundles (7)
├── _local_backups/              # v2.0 reorg — *.bak* and archive_masters_pre_* (gitignored; NOT in Zenodo tarball)
├── kastner-author/              # 372 studies authored by Peter S. Kastner
│   ├── _known_entities.csv      # Collection-scoped cache
│   ├── _known_technologies.csv
│   ├── dct/                     # Digital Consumer Technology — 76 studies
│   ├── employer/                # Studies grouped by Kastner's employer at the time
│   │   ├── aberdeen-group/          (46 studies)
│   │   ├── stratus-computer/        (13 studies)
│   │   ├── DEC/                     ( 5 studies)
│   │   ├── arthur-d-little/         ( 3 studies)
│   │   ├── phi-computer-services/   ( 2 studies)
│   │   ├── prime-computer/          ( 1 study)
│   │   └── obian-group/             ( 1 study)
│   └── <study-slug>/                (226 top-level studies)
├── other-authors/               # 487 studies by other authors
│   ├── _known_entities.csv
│   ├── _known_technologies.csv
│   └── <study-slug>/
├── prepared/                    # 493 newly-ingested studies — v1.4 staging directory
│   └── <study-slug>/            #   awaiting promotion to kastner-author/, other-authors/, or employer/* in v1.5
├── aberdeen-group-inc/          # Aberdeen Group corporate / about-the-company files (29 studies)
├── Aberdeen Outbound Marketing/ # Period marketing collateral (3 studies)
├── Project Examples/            # Sample / illustrative engagements (45 studies)
└── Kastner Memoir/              # 'Arguments with Reality' Vol. 1 — 14 chapter packages (14 studies, 1,242 obs)
```

### Per-study layout (Frictionless Data Package)

```
<study-slug>/
├── datapackage.json             # Frictionless descriptor (resources, schemas)
├── README.md                    # Human-readable narrative
├── data/
│   ├── studies.csv              # 1 row of study metadata
│   ├── entities.csv             # Organizations / people referenced
│   ├── technologies.csv         # Technologies with lifecycle stage
│   ├── observations.csv         # Structured analytical observations
│   └── codes.csv                # Controlled vocabulary for observation_type
├── schema/
│   └── schema_org.json          # Schema.org Dataset metadata
├── source/                      # Original source PDFs / docs / extracted text
└── scripts/
    └── demo_analysis.py         # Self-contained validation + demo
```

### Canonical CSV schemas

**`studies.csv`** (per-study package) — 16 columns: `study_id, title, author, date, type, subject_domain, methodology, source_file, abstract, license, importance, importance_rationale, relevance, relevance_rationale, prescience, prescience_rationale`. The aggregate `_master_studies.csv` carries **4 additional v2.0 columns** — `prescience_3y_enum, prescience_3y_rationale, prescience_5y_enum, prescience_5y_rationale` (20 columns total).

**`entities.csv`** — 9 columns: `entity_id, entity_name, entity_type, sector, status, successor, years_active, study_id, notes`.

**`technologies.csv`** — 9 columns: `tech_id, tech_name, category, vendor, era, lifecycle_at_study, lifecycle_current, study_id, notes`.

**`observations.csv`** — 12 columns including `obs_id, study_id, entity_id, tech_id, observation_type, finding, evidence, confidence, importance, relevance, prescience, notes`.

All CSVs follow §16.5 write rules: `csv.writer` with `quoting=csv.QUOTE_ALL`, lowercase ratings (`low | medium | high`), license string `CC-BY-4.0`, lowercase confidence.

### Quickstart — pandas

```python
import pandas as pd

studies = pd.read_csv("_master_studies.csv")
obs     = pd.read_csv("_master_observations.csv")
ents    = pd.read_csv("_known_entities.csv")    # deduped
techs   = pd.read_csv("_known_technologies.csv")  # deduped

# How many high-prescience studies per author/employer combo?
(studies[studies.prescience == "high"]
   .groupby("author")
   .size()
   .sort_values(ascending=False)
   .head(10))

# Top 20 entities by observation count
(obs.merge(studies[["study_id", "date"]], on="study_id")
    .groupby("entity_id").size()
    .sort_values(ascending=False).head(20))

# All studies authored by Kastner
kp = studies[studies.author.str.contains("Kastner", na=False)]
```

### Quickstart — DuckDB

```python
import duckdb

con = duckdb.connect()
con.execute("""
  CREATE VIEW studies     AS SELECT * FROM read_csv_auto('_master_studies.csv');
  CREATE VIEW observations AS SELECT * FROM read_csv_auto('_master_observations.csv');
  CREATE VIEW entities    AS SELECT * FROM read_csv_auto('_known_entities.csv');
  CREATE VIEW techs       AS SELECT * FROM read_csv_auto('_known_technologies.csv');
""")

# Most-cited technologies across the whole archive
con.sql("""
  SELECT t.tech_name, COUNT(*) AS n_obs
  FROM observations o
  JOIN techs t ON o.tech_id = t.tech_id
  GROUP BY t.tech_name
  ORDER BY n_obs DESC
  LIMIT 25
""").show()

# High-prescience observations from the 1990s, with study context
con.sql("""
  SELECT s.date, s.title, o.finding
  FROM observations o
  JOIN studies s USING (study_id)
  WHERE o.prescience = 'high'
    AND s.date BETWEEN '1990-01-01' AND '1999-12-31'
  ORDER BY s.date
""").show()
```

For a fully pre-built DuckDB database and Parquet exports against these same masters, see the companion **Kastner Aberdeen Wiki** at `~/Repos/kastner-aberdeen-wiki/` ([shorttack/kastner-aberdeen-wiki](https://github.com/shorttack/kastner-aberdeen-wiki)).

### Ingestion pipeline

Studies are produced by the `archival-ingest` skill (currently **v20**) running on Perplexity Computer. The frozen skill source — including the assembler, validator, and supporting templates — is mirrored at `_skills/archival-ingest/`. The assembler invocation pattern:

```bash
ASM=_skills/archival-ingest/scripts/assembler.py
python3 "$ASM" assemble    <study_dir>
python3 "$ASM" validate    <study_dir>
python3 "$ASM" cache-update . <study_dir>
```

After per-study cache updates, masters are regenerated by `_audits/` tooling and audited by `audit_script_v2.py` in three layers:

1. **Layer A** — per-study referential integrity (entity_id / tech_id / observation_type all resolve within the study).
2. **Layer B** — §16 CSV write validation gate (no base64, correct quoting, schema-conformant headers).
3. **Layer C** — cross-study cache integrity (no missing entries, no duplicate IDs).

The current archive passes all three layers with 0 failures across all audited studies (count in [`ARCHIVE_STATS.md`](./ARCHIVE_STATS.md)).

v20 of the ingest skill adds the **obs_id Universal Normalizer** (13-bucket classifier-driven repair of legacy observation IDs) and the **`legacy_obs_id` audit column** on `_master_observations.csv`.

### v2.0 changes

- **Full-corpus 3-year / 5-year prescience**: new `_master_prescience_short_horizon.csv` (**17,030 rows**) scores every gradeable observation at fixed 3y and 5y windows; **792 studies** carry rolled-up `prescience_3y_enum` / `prescience_5y_enum` verdicts. Studies master grew 16 → 20 columns. 3y: 522 high / 264 med / 4 low / 1 na / 1 pending. 5y: 518 high / 268 med / 4 low / 1 na / 1 pending.
- **v9 confabulation fix**: the SH scorer enforces a **window-not-elapsed sentinel (`-2`)** at the chokepoint, ending the failure mode where the model fabricated retrospective verdicts for windows that hadn't elapsed. Net across the 16,232-call sweep: 2 of 13,885 scored SH calls reduced to a `-1` parse-reject (retained as sentinels). SH sentinel taxonomy: `-1` = prefiltered / parse-reject; `-2` = window not elapsed; both excluded from verdict means.
- **PC Deals per-SKU price journeys**: the weekly-bulletin `-mx` tier gains **249 per-SKU journeys**, tracking individual hardware SKUs across successive bulletins as longitudinal price-history series.
- **Pipeline**: Phase 1 → `01_load_csvs_v3.py` (reads SH master, writes `short_horizon.parquet`); Phase 2 → `02_build_data_layer_v5.py` (promotes `short_horizon`, registers `v_prescience_sh` / `v_studies_with_sh_verdicts` / `v_observations_with_sh` / `v_sh_3y_distribution` / `v_sh_5y_distribution`); Phase 3 → `03_generate_vault_v3.py` (study pages render the SH section); Phase 6 → `06_emit_scaffolding_v2.py` (README/AGENTS/chat-starter SH blocks, `verify.py` +4 SH views).
- **New scripts**: `merge_sh_scores_to_master_v1.py`, `apply_sh_study_verdicts_v1.py`.
- **Wiki rebuild**: Phase 3-6 on local Ollama; bge-m3 (1024-dim) re-embed of **10,862 pages**. `kw ask` now answers 3y/5y questions from real retrieved text.

#### Prior releases

- **v1.9.0** (2026-06-22): Substrate silent-loss recovery + CompChem 1989 exemplar.
- **v1.7.0** (2026-06-18): Multi-horizon prescience groundwork; `row_class` backfill.
- **v1.6.2** (2026-06-17): Tier B promote; observation-level scores 3,829 → 15,924; `[DEFERRED]` bucket drained 370 → 1.
- **v1.6.1** (2026-06-13): Pass B reconcile; Path B player rebuttal (Plaza DECtp).
- **v1.6** (2026-05-31): Full 1,400+ study content; initial Pass C cloud scoring.
- **v1.5.1** (2026-05-27): pub_year backfill v6+v6.1.
- **v1.4.0** (2026-05-23): +490 studies from the May 2026 weekend bucket pass; obs_id Universal Normalizer.

Full curatorial decision history is in [`_decisions_log.md`](./_decisions_log.md).
