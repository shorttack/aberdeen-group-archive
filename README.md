# Kastner IT Research Archive

[![DOI](https://zenodo.org/badge/1181715405.svg)](https://doi.org/10.5281/zenodo.20245076)

A structured archive of research studies, articles, memoirs, and related artifacts spanning **1979–2026**, centered on the work of **Peter S. Kastner** at Aberdeen Group, Arthur D. Little, Philip Hankins Inc. (PHI), Digital Equipment Corporation, Stratus Computer, and Obian Group, plus contributions from other Aberdeen analysts.

Every study is packaged as a self-contained [Frictionless Data Package](https://frictionlessdata.io/), with structured CSV tables, a JSON descriptor, a Schema.org dataset descriptor, and a human-readable README.

Kastner had the prescience to save much of his work in digital form; about one-third has survived. It is all in this "Kastner Research Archive".

| Metric | Count |
|---|---:|
| Total studies | **1,434** |
| Total observations | **23,605** |
| Master entity rows | **3,207** |
| Master technology rows | **4,312** |
| Unique entities (deduped cache) | **3,300** |
| Unique technologies (deduped cache) | **4,371** |
| Date range | 1979 – 2026 |
| Audit failures (Layer A / B / C) | **0 / 0 / 0** |

**v1.4 release notes:** This release adds **490 new studies** from the May 2026 weekend ingest, including five bucket-classifier passes (A–E) and Mode 2 (existing-archive re-evaluation). It also lands two data-hygiene fixes: a case-collision merge across the entity master and a `tech_id="java"` carve-out that resolved a PDA-misfile collision (see [`CHANGELOG.md`](./CHANGELOG.md) and [`_decisions_log.md`](./_decisions_log.md)). New: a companion **Kastner Aberdeen Wiki** (Obsidian + DuckDB + Parquet) built directly from these masters — see "Companion wiki" below.

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

- **Format**: Obsidian vault + DuckDB query layer + Parquet exports + nomic-embed embedding index.
- **Pages**: **8,960** — 1,434 study pages, 3,207 entity pages, 4,313 tech pages, plus index/dashboard pages.
- **Cross-linking**: Every study page emits `[[entity-slug]]` and `[[tech-slug]]` wikilinks (3,682 study→entity links and 5,253 study→technology links), powering Dataview reverse-lookups on every entity and technology page.
- **Local-first**: Lives at `kastner_wiki/` in the parent archive directory; opens in Obsidian, queryable from DuckDB, browsable from Python/pandas via the Parquet exports.
- **Builder skill**: `kastner-wiki-builder` (custom user skill).
- **Backup**: `kastner_wiki_backup_v1.4_<timestamp>.tar.gz` lives in the Archive root.

### Prescience ratings

Each study is rated for the prescience of its forecasts when checked against subsequent history:

| Rating | Studies |
|---|---:|
| high | 471 |
| medium | 271 |
| low | 72 |
| not-applicable | 249 |
| [DEFERRED] | 370 |
| (unrated) | 1 |
| [REVIEW] | (legacy flag — to be drained in v1.5) |

The **`[DEFERRED]` bucket holds the 370 v1.4 ingest studies whose prescience scoring is queued for the Pass C scoring run** (post-v1.4 backlog item).

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

> Kastner, Peter S. (2026). *Kastner IT Research Archive*, version 1.4.0.
> Licensed under CC-BY-4.0.

Version history is in [`CHANGELOG.md`](./CHANGELOG.md). Curatorial decisions and data-hygiene history are in [`_decisions_log.md`](./_decisions_log.md).

---

## For Data Engineers / Analysts

### Top-level layout (v1.4)

```
aberdeen-group-archive/
├── _master_studies.csv          #   1,434 rows — index of all studies
├── _master_entities.csv         #   3,207 rows — per-study entity rows
├── _master_technologies.csv     #   4,312 rows — per-study technology rows
├── _master_observations.csv     #  23,605 rows — every observation
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

The current archive passes all three layers with 0 failures across all 1,434 audited studies.

v20 of the ingest skill adds the **obs_id Universal Normalizer** (13-bucket classifier-driven repair of legacy observation IDs) and the **`legacy_obs_id` audit column** on `_master_observations.csv`.

### v1.4 changes

- **+490 studies** ingested from the May 2026 weekend bucket pass (modes 1–2; buckets A–E + existing).
- **Case-collision merge** across `_known_entities.csv` and `_known_technologies.csv` (9-row dedupe).
- **Java carve-out**: a misfiled `tech_id="java"` row in `_master_technologies.csv` carrying `tech_name="PDA (personal digital assistant)"` was merged into the canonical uppercase `tech_id="JAVA"` (Java Programming Language). 91 observation, tech_studies, conflicts, and known_technologies rows were re-pointed; the misfiled row was dropped. Pre-merge backup: `archive_masters_backup_pre_java_fix_<timestamp>.tar.gz` in the Archive root.
- **Skill version bump**: `archival-ingest` v18 → v20 (adds obs_id Universal Normalizer and `legacy_obs_id` audit column).
- **New companion wiki**: 8,960-page Obsidian vault + DuckDB + Parquet, built from the cleaned masters. See `../kastner_wiki/`.
- **`prepared/` staging directory**: 493 v1.4 studies live here pending classification (a v1.5 promotion task).
- **`[DEFERRED]` prescience flag**: 370 newly-ingested studies await Pass C prescience scoring (a v1.5 backlog item).

Full curatorial decision history is in [`_decisions_log.md`](./_decisions_log.md).
