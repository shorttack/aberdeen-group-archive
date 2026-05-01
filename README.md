# Aberdeen Group Research Archive

A structured archive of research studies, articles, memoirs, and related artifacts spanning **1979–2026**, centered on the work of **Peter S. Kastner** at Aberdeen Group, Arthur D. Little, Project Hindsight Inc. (PHI), Digital Equipment Corporation, Stratus Computer, and Obian Group, plus contributions from other Aberdeen analysts.

Every study is packaged as a self-contained [Frictionless Data Package](https://frictionlessdata.io/), with structured CSV tables, a JSON descriptor, a Schema.org dataset descriptor, and a human-readable README.

| Metric | Count |
|---|---:|
| Total studies | **822** |
| Total observations | **14,742** |
| Master entity rows | **7,834** |
| Master technology rows | **6,269** |
| Unique entities (deduped cache) | **3,198** |
| Unique technologies (deduped cache) | **4,054** |
| Date range | 1979 – 2026 |
| Audit failures (Layer A / B / C) | **0 / 0 / 0** |

---

## For Researchers

The archive is organized by who wrote each study and, for Peter S. Kastner's own work, by which employer he was at when the study was produced. Most readers will start in `kastner-author/` and drill into the employer subdirectory of interest.

### Key reading paths

- **`kastner-author/employer/aberdeen-group/`** — Kastner's published Aberdeen Group analyst work (1995–2001 core), 29 studies, 609 observations.
- **`kastner-author/employer/DEC/`** — Digital Equipment Corporation engineering and product memos (1980s).
- **`kastner-author/employer/arthur-d-little/`** — ADL consulting engagements (1972–1979), including 9-1-1 / CAD public-safety systems and the ASE/ASEP two-way power-line communications study.
- **`kastner-author/employer/phi-computer-services/`** — PHI Computer Services (1969–1972) and the 1995 Wang Labs *Riding the Runaway Horse* retrospective.
- **`kastner-author/employer/stratus-computer/`** and **`/obian-group/`** — earlier vendor/consulting roles.
- **`kastner-author/dct/`** — Digital Consumer Technology (DCT) studies, 76 entries.
- **`kastner-author/`** (top-level) — 205 studies that pre-date the employer-scoped reorganization or sit outside any single employer (memoirs, AI responses, technology topics, expert reports, video transcripts).
- **`other-authors/`** — 475 studies authored by other Aberdeen analysts and outside writers.

### Prescience ratings

Each study is rated for the prescience of its forecasts when checked against subsequent history:

| Rating | Studies |
|---|---:|
| high | 394 |
| medium | 250 |
| low | 67 |
| not-applicable | 110 |
| (deferred) | 1 |

### Aberdeen Group Category Creator roster

Eight Aberdeen analysts are credited with creating practice areas at the firm. Their entity rows in this archive carry an `Aberdeen Group Category Creator: …` prefix in `notes`, credited by Peter S. Kastner.

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

Each study's `datapackage.json` carries a stable `study_id` and a Schema.org `Dataset` descriptor in `schema/schema_org.json`. Cite by `study_id` plus the path to the package directory.

### License

Original Aberdeen Group analyst content is proprietary; structured artifacts (CSVs, descriptors, code) in this repository are released under **CC-BY-4.0** with attribution to Peter S. Kastner unless a study's own README states otherwise.

---

## For Data Engineers / Analysts

### Top-level layout

```
aberdeen-group-archive/
├── _master_studies.csv          # 822 rows  — index of all studies
├── _master_entities.csv         # 7,834 rows — per-study entity rows
├── _master_technologies.csv     # 6,269 rows — per-study technology rows
├── _master_observations.csv     # 14,742 rows — every observation
├── _collection_stats.csv        # 822 rows — per-study counts and ratings
├── _known_entities.csv          # 3,198 rows — deduped entity cache (root)
├── _known_technologies.csv      # 4,054 rows — deduped technology cache (root)
├── _audits/                     # Referential-integrity audit reports
├── _skills/                     # Frozen copy of the archival-ingest skill
├── kastner-author/              # 347 studies authored by Peter S. Kastner
│   ├── _known_entities.csv      # Collection-scoped cache
│   ├── _known_technologies.csv
│   ├── dct/                     # Digital Consumer Technology — 76 studies
│   ├── employer/                # Studies grouped by Kastner's employer at the time
│   │   ├── aberdeen-group/          (29 studies, 609 obs)
│   │   ├── stratus-computer/        (11 studies,  66 obs)
│   │   ├── DEC/                     ( 5 studies, 153 obs)
│   │   ├── arthur-d-little/         ( 3 studies,  71 obs)
│   │   ├── phi-computer-services/   ( 2 studies,  59 obs)
│   │   └── obian-group/             ( 1 study,    5 obs)
│   └── <study-slug>/                (205 top-level studies)
├── other-authors/               # 475 studies by other authors
│   ├── _known_entities.csv
│   ├── _known_technologies.csv
│   └── <study-slug>/
├── aberdeen-group-inc/          # Aberdeen Group corporate / about-the-company files
├── Aberdeen Outbound Marketing/ # Period marketing collateral (raw)
└── Project Examples/            # Sample / illustrative engagements
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

**`studies.csv`** — 16 columns: `study_id, title, author, employer, date, type, era, importance, relevance, prescience, license, source_path, source_url, n_observations, n_entities, n_technologies`.

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
   .groupby(["author", "employer"])
   .size()
   .sort_values(ascending=False)
   .head(10))

# Top 20 entities by observation count
(obs.merge(studies[["study_id", "date"]], on="study_id")
    .groupby("entity_id").size()
    .sort_values(ascending=False).head(20))

# All Kastner ADL-era studies
adl = studies[studies.employer.str.contains("Arthur D. Little", na=False)]
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

### Ingestion pipeline

Studies are produced by the `archival-ingest` skill (currently v18) running on Perplexity Computer. The frozen skill source — including the assembler, validator, and supporting templates — is mirrored at `_skills/archival-ingest/`. The assembler invocation pattern:

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

The current archive passes all three layers with 0 failures across 680 audited studies.
