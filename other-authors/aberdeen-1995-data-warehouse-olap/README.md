# Aberdeen Group (1995) — Data Warehouse Query Tools: Evolving to Relational OLAP

**Frictionless Data Package** | Study ID: `aberdeen-1995-data-warehouse-olap`

## Overview

This data package archives and structures the Aberdeen Group Market Viewpoint titled *"Data Warehouse Query Tools: Evolving to Relational OLAP"*, published July 7, 1995 (Volume 8, Number 8). The original document analyzed the emerging Relational OLAP (ROLAP) technology category and assessed its competitive position against traditional report writers and multidimensional OLAP (MOLAP) tools.

**Original source (archived):** https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm

## Study Summary

Aberdeen Group segmented 1995 data warehouse query tools into three categories:

1. **Report Writer / Predefined** — Tools like Microsoft Access and Crystal Reports for operational data retrieval. Adequate for simple queries but limited by fat-client architecture, continuous IS dependency, and inability to handle complex ad hoc analysis.

2. **Multidimensional OLAP (MOLAP)** — Tools using proprietary multidimensional databases (MDBs) with array and sparse-matrix storage. Strong for consumer packaged goods market-share analysis and what-if scenarios, but practically limited to 20–50 GB before performance degrades, and lacking enterprise mission-critical features (security, high availability, incremental updates).

3. **Relational OLAP (ROLAP)** — The study's recommended next-generation approach, combining multidimensional query capabilities with parallel-scalable RDBMS backends. Key vendors identified: MicroStrategy Inc., Information Advantage Inc., and Stanford Technology Group.

Aberdeen predicted ROLAP would generate a new wave of data-mining applications within two years and that MDBs would face stiffening competition from ROLAP after a ~3-year datamart role.

## Key Findings

- MDB technology becomes impractical above **20–50 GB**; hundreds of sites already exceeded 100 GB with relational databases by 1995
- Over **1,000 customer sites** had already surpassed 50 GB with very large relational databases
- Report writers identified with **7 structural weaknesses** limiting decision-support use
- ROLAP architecture defined as a **7-layer multi-tier framework** (operational systems → RDBMS warehouse → metadata → SQL engine → desktop apps → app-dev environment → intelligent agents)
- Three core ROLAP database optimization techniques: **denormalization**, **summarization**, and **partitioning**
- MicroStrategy + Informix cited as the model **market-driven ROLAP/RDBMS partnership**
- Oracle acquiring IRI Software for its Express MDB product (1995)
- Arbor Software tightening alliance with Hewlett-Packard

## Entity Status (as of 2026)

| Entity | Status | Successor |
|--------|--------|-----------|
| MicroStrategy Inc. | **Active** (MSTR) | — |
| Information Advantage | Acquired 1999 | Sterling Software → CA Technologies |
| Stanford Technology Group | Acquired ~1998 | Unknown |
| Arbor Software | Merged 1998 | Hyperion Solutions → Oracle (2007) |
| IRI Software | Acquired 1995 | Oracle (Express) |
| D&B Software | Acquired 1996 | Geac Computer ($150M) |
| Pilot Software | Acquired 2007 | SAP AG |
| Holistic Systems | Acquired 1996 | Seagate Software → Crystal Decisions → Business Objects |
| Andyne Computing | Acquired 1997 | Hummingbird ($60M) |
| Business Objects | Acquired 2008 | SAP AG |
| Cognos Corp. | Acquired 2008 | IBM ($5B) |
| IQ Software | Acquired 1998 | Information Advantage ($36M) |
| Informix | Acquired 2001 | IBM |
| Sybase | Acquired 2010 | SAP AG |

## Technology Lifecycle (as of 2026)

| Technology | Status in 1995 | Status in 2026 |
|------------|----------------|----------------|
| Relational OLAP (ROLAP) | Emerging | Evolved (modern BI platforms) |
| Multidimensional OLAP (MOLAP) | Mainstream | Legacy/Niche |
| Data Warehousing | Emerging | Active (cloud data warehouses) |
| Dimensional Modeling | Emerging | Active (standard practice) |
| Fat-client architecture | Mainstream | Obsolete |
| Parallel-scalable RDBMS | Emerging | Evolved (cloud-native OLAP) |
| Intelligent agents/alerts | Emerging | Evolved (modern alerting) |
| Data Mining | Emerging | Active (ML/AI) |

## Package Structure

```
aberdeen-1995-data-warehouse-olap/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study master record (1 row)
│   ├── entities.csv          # Organizations (20 rows)
│   ├── technologies.csv      # Technologies and products (28 rows)
│   ├── observations.csv      # Structured findings (48 rows)
│   └── codes.csv             # Reference codes and vocabulary
├── schema/
│   └── schema_org.json       # Schema.org Dataset markup
└── scripts/
    └── demo_analysis.py      # Python demonstration analysis script
```

## Data Tables

### studies.csv
Master record for the study. Fields: `study_id`, `title`, `author`, `date`, `doc_type`, `domain`, `methodology`, `abstract`, `source_url`, `pages`.

### entities.csv
Organizations mentioned in the study (vendors, research firms, hardware companies), with current status verified as of 2026. Fields: `entity_id`, `entity_name`, `entity_type`, `sector`, `status`, `successor`, `years_active`, `study_id`, `notes`.

### technologies.csv
Technologies, products, standards, and analytical methodologies discussed in the study, with lifecycle status at publication (1995) and current (2026). Fields: `tech_id`, `tech_name`, `category`, `vendor`, `era`, `lifecycle_at_study`, `lifecycle_current`, `study_id`, `notes`.

### observations.csv
All factual claims, market data, predictions, competitive assessments, and strategic recommendations extracted from the study (48 observations). Each row is traceable to a source page. Fields: `obs_id`, `study_id`, `entity_id`, `tech_id`, `observation_type`, `year_observed`, `metric_name`, `metric_value`, `confidence`, `methodology_code`, `source_page`, `notes`.

### codes.csv
Controlled vocabulary for all coded fields across tables. Covers: `observation_type`, `methodology_code`, `entity_type`, `entity_status`, `tech_category`, `tech_lifecycle`, `doc_type`, `domain`, `methodology`, `confidence`.

## Usage

```python
import pandas as pd

# Load all tables
studies = pd.read_csv('data/studies.csv')
entities = pd.read_csv('data/entities.csv')
technologies = pd.read_csv('data/technologies.csv')
observations = pd.read_csv('data/observations.csv')
codes = pd.read_csv('data/codes.csv')

# Example: All market forecasts
forecasts = observations[observations['observation_type'] == 'market-forecast']

# Example: Technologies that were emerging in 1995 and are still active
still_active = technologies[
    (technologies['lifecycle_at_study'] == 'emerging') &
    (technologies['lifecycle_current'] == 'active')
]
```

See `scripts/demo_analysis.py` for full demonstration analysis.

## Citation

If using this data package in research, please cite:

> Aberdeen Group. (1995, July 7). *Data Warehouse Query Tools: Evolving to Relational OLAP*. Aberdeen Group Market Viewpoint, Vol. 8, No. 8. Boston, MA: Aberdeen Group, Inc. Archived at https://web.archive.org/web/19970112010847/http://www.aberdeen.com:80/secure/viewpnts/v8n8/v8n8.htm

## License

Data structured and archived under the Open Data Commons Attribution License (ODC-By). Original content copyright © 1995 Aberdeen Group, Inc.
