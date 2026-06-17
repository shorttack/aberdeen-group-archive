# Kastner IT Research Archive

[![DOI](https://zenodo.org/badge/1181715405.svg)](https://doi.org/10.5281/zenodo.20245076)

A structured archive of research studies, articles, memoirs, and related artifacts spanning **1979–2026**, centered on the work of **Peter S. Kastner** at Aberdeen Group, Arthur D. Little, Philip Hankins Inc. (PHI), Digital Equipment Corporation, Stratus Computer, and Obian Group, plus contributions from other Aberdeen analysts.

Every study is packaged as a self-contained [Frictionless Data Package](https://frictionlessdata.io/), with structured CSV tables, a JSON descriptor, a Schema.org dataset descriptor, and a human-readable README.

Kastner had the prescience to save much of his work in digital form; about one-third has survived. It is all in this "Kastner Research Archive".

**v1.6.2 — "Multi-Horizon Prescience"** (2026-06-17)

The current corpus: **1,452 studies · 23,926 observations · 3,276 entity rows · 4,361 technology rows · 498 high-prescience studies** (`study_prescience_enum = 'high'`), spanning **1979–2026**.

New in v1.6.2: 3-year and 5-year prescience results promoted into the masters via Tier B sentinel-aware rebuild. Observations with a prescience score grew from 3,829 (v1.6.1) to **15,924**; authored high-prescience study count grew from 125 to **498**. No new studies; this is a deeper read of the existing corpus.

These are the live counts. Per-subdirectory and per-section numbers elsewhere may lag the masters — when in doubt, `_master_*.csv` is truth.

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
- **Pages**: **10,382** — 1,452 study pages, 3,276 entity pages, 4,361 tech pages, 1,293 code pages, plus 33 decade/theme/collection/index pages.
- **Embedding index**: bge-m3 (1024-dim), 10,438 rows.
- **Cross-linking**: Every study page emits `[[entity-slug]]` and `[[tech-slug]]` wikilinks (**5,597 study→entity links** and **11,050 study→technology links**), powering Dataview reverse-lookups on every entity and technology page.
- **Local-first**: Lives at `~/Repos/kastner-aberdeen-wiki/` on the build host (migrated from `~/Desktop/kastner_wiki/` on 2026-06-01 to escape iCloud Desktop sync). Opens in Obsidian, queryable from DuckDB, browsable from Python/pandas via the Parquet exports.
- **Builder skill**: `kastner-wiki-builder` (custom user skill).
- **GitHub mirror**: [shorttack/kastner-aberdeen-wiki](https://github.com/shorttack/kastner-aberdeen-wiki) — same v1.6.2 tag.

### Prescience ratings

Each study is rated for the prescience of its forecasts when checked against subsequent history:

| Rating | Studies |
|---|---:|
| high | 498 |
| medium | 330 |
| low | 276 |
| not-applicable | 346 |
| [DEFERRED] | 1 |
| (unrated) | 1 |

The `[DEFERRED]` v1.4 backlog bucket (formerly 370 studies) was drained by the Tier B promote in v1.6.2 — 1 row remaining.

The **498** figure above is the author-curated `study_prescience_enum = 'high'` surface. Two observation-derived surfaces are also exposed in `v_studies`: **865** studies satisfy `prescience_max ≥ 4` (loose) and **115** studies satisfy `prescience_mean ≥ 3.5` (tight). The `v_studies_with_high_prescience` view filters on the authored verdict (498); downstream researchers can pick the threshold appropriate to their question.

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

> Kastner, Peter S. (2026). *Kastner IT Research Archive*, version 1.6.2.
> Licensed under CC-BY-4.0.

Version history is in [`CHANGELOG.md`](./CHANGELOG.md). Curatorial decisions and data-hygiene history are in [`_decisions_log.md`](./_decisions_log.md).

---

## For Data Engineers / Analysts

### Top-level layout (v1.6.2)

```
aberdeen-group-archive/
├── _master_studies.csv          #   1,452 rows — index of all studies
├── _master_entities.csv         #   3,276 rows — per-study entity rows
├── _master_technologies.csv     #   4,361 rows — per-study technology rows
├── _master_observations.csv     #  23,926 rows — every observation
├── _master_prescience_scores.csv  # 17,085 rows — obs-level scores (Pass C cloud_v1)
├── _master_player_rebuttals.csv  # author rebuttals of scorer verdicts (Path B)
├── _master_tech_studies.csv     # tech_id → study_id bridge
├── _master_tech_field_conflicts.csv  # tech-field conflict audit
├── _master_tech_canonicalization_TODO.csv  # tech_id canonicalization queue
├── _collection_stats.csv        # per-study counts and ratings
├── _known_entities.csv          #   3,300 rows — deduped entity cache (root)
├── _known_technologies.csv      #   4,371 rows — deduped technology cache (root)
├── _web_cache.json              # Phase 3 web-verification cache
├── _audits/                     # Referential-integrity audit reports
├── _skills/                     # Frozen copy of the archival-ingest skill (v20)
├── _decisions_log.md            # Curatorial decisions and data-hygiene history
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

**`studies.csv`** — 16 columns: `study_id, title, author, date, type, subject_domain, methodology, source_file, abstract, license, importance, importance_rationale, relevance, relevance_rationale, prescience, prescience_rationale`.

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

For a fully pre-built DuckDB database and Parquet exports against these same masters, see the companion **Kastner Aberdeen Wiki** at `../kastner_wiki/`.

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

The current archive passes all three layers with 0 failures across all 1,452 audited studies.

v20 of the ingest skill adds the **obs_id Universal Normalizer** (13-bucket classifier-driven repair of legacy observation IDs) and the **`legacy_obs_id` audit column** on `_master_observations.csv`.

### v1.6.2 changes

- **Multi-horizon prescience**: 3-year and 5-year results promoted into the masters. Observations with a prescience score grew from 3,829 (v1.6.1) to **15,924**.
- **Tier B promote**: 8,645 previously-prefiltered observations restored into `_master_prescience_scores.csv` (8,440 → 17,085 rows).
- **Sentinel filter at ingest**: Phase 1 (`01_load_csvs_v3.py`) drops `prescience_score < 0` sentinel rows at the chokepoint before joins (908 sentinels filtered on the v1.6.2 build). Sentinel taxonomy: `-1` = parse_fail or prefilter_excluded (disambiguated by `source_pass`); `-99` = content_unrecoverable.
- **Pass C three-file architecture**: documented and codified in the `kastner-archive-pipeline` skill (v1.7) — File 1 (live), File 2 (studies-attached), File 3 (repo snapshot).
- **Path B (player rebuttal)**: authored `prescience` enum is preserved by Phase 1; observation-derived math (`prescience_mean` / `prescience_max` / `prescience_obs_count`) is exposed alongside for transparency. Canonical example: Plaza DECtp transcript (authored `high`, observation mean 0.46).
- **`promote_pass_c_to_master_v1.py`** — append-only, dedupes on `obs_id`, explicit `scorer_version=cloud_v1` and `source_pass=pass_c_cloud`.
- **`sync_studies_verdicts_repo_from_archive_masters_v2.py`** — narrows sync to `prescience` + `prescience_rationale` columns.
- **`roll_up_prescience_v3.py` deprecated** — relocated to `scripts/v3_obsolete/`; replaced by manual verdict write + sync.
- **Wiki rebuild**: Phase 3-6 on `qwen3.5:27b-mlx` (local Ollama, MLX engine). Embeddings on `bge-m3` (1024-dim). 10,382 pages, 10,438 embedding rows.
- **`[DEFERRED]` bucket drained**: 370 → 1 after Tier B promote.

#### Prior releases

- **v1.6.1** (2026-06-13): Pass B reconcile, +1 high-prescience study (Plaza DECtp via Path B rebuttal).
- **v1.6** (2026-05-31): Full 1,400+ study content, initial Pass C cloud scoring.
- **v1.5.1** (2026-05-27): pub_year backfill v6+v6.1.
- **v1.4.0** (2026-05-23): +490 studies from the May 2026 weekend bucket pass; obs_id Universal Normalizer.

Full curatorial decision history is in [`_decisions_log.md`](./_decisions_log.md).
