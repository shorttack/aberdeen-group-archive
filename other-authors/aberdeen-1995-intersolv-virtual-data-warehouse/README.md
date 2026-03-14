# Exploring Intersolv's Virtual Data Warehouse

**Data Package:** `aberdeen-1995-intersolv-virtual-data-warehouse`  
**Study Number:** 8  
**Author:** Aberdeen Group  
**Date:** October 1995  
**Type:** Product Profile  
**Domain:** Data Warehousing  

---

## Overview

This Frictionless Data Package contains structured data extracted from an Aberdeen Group product profile published in October 1995 examining **Intersolv's Virtual Data Warehouse** — a decision-support environment that combined metadata, ODBC-based data access technology, and query/analysis/reporting tools to provide unified access to distributed data sources without requiring physical data consolidation.

The Virtual Data Warehouse was introduced on October 2, 1995 by Intersolv Inc. (Rockville, Maryland). On October 23, 1995, Intersolv acquired TechGnosis International (Brussels, Belgium), adding the SequeLink server-based connectivity technology to the product stack.

### Source Document

- **Title:** Exploring Intersolv's Virtual Data Warehouse  
- **Publisher:** Aberdeen Group, One Boston Place, Boston, MA 02108  
- **Archived URL:** https://web.archive.org/web/19970108191541/http://www.aberdeen.com:80/secure/profiles/intsolv/interslv.htm  
- **Pages:** 3  
- **Approximate Word Count:** 3,200  

---

## Package Contents

```
aberdeen-1995-intersolv-virtual-data-warehouse/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study-level metadata (1 row)
│   ├── entities.csv          # Organizations and entities (12 rows)
│   ├── technologies.csv      # Technologies and products (15 rows)
│   ├── observations.csv      # Extracted observations (45 rows)
│   └── codes.csv             # Controlled vocabulary (30 rows)
├── schema/
│   └── schema_org.json       # Schema.org Dataset metadata
└── scripts/
    └── demo_analysis.py      # Python analysis demonstration
```

---

## Data Tables

### studies.csv
Top-level study metadata. One row per source document.

| Field | Description |
|---|---|
| study_id | Unique slug identifier |
| title | Full study title |
| author | Authoring organization |
| date | Publication date (ISO 8601) |
| type | Study type code |
| domain | Primary domain code |
| methodology | Comma-separated methodology codes |
| abstract | Study summary |
| source_url | Archival/canonical URL |
| pdf_filename | Source PDF filename |
| page_count | PDF page count |
| word_count_approx | Approximate word count |
| study_num | Sequential study number in collection |

### entities.csv
Organizations, companies, and named entities mentioned in the study, enriched with current (2026) status information based on web research.

| Field | Description |
|---|---|
| entity_id | Unique identifier (ent-NNN) |
| study_id | FK → studies.study_id |
| name | Entity name as referenced in study |
| entity_type | vendor / analyst-firm / product / standard |
| description | Description of entity |
| hq_location | Headquarters location at time of study |
| status | active / acquired / merged / renamed / discontinued |
| status_detail | Narrative explanation of current status |
| status_source_url | URL used for status determination |

**Key Entity Status Summary:**

| Entity | 1995 Status | Current Status |
|---|---|---|
| Intersolv Inc. | Active, independent | Acquired by Micro Focus (1998, $534M); combined entity renamed Merant |
| TechGnosis International | Active, independent | Acquired by Intersolv (Oct 23, 1995, ~$80M) |
| Cognos Corp. | Active, independent | Acquired by IBM (Jan 2008, ~$5B) |
| Business Objects | Active, independent | Acquired by SAP (Jan 2008, $6.8B) |
| DataDirect Technologies | Intersolv brand | Spun off; acquired by Progress Software (Dec 2003, $88M); still active |
| IBM | Active | Active (public company) |
| Microsoft | Active | Active (public company) |

### technologies.csv
Technologies, products, standards, and architectural patterns mentioned in the study, with lifecycle status as of 2026.

| Field | Description |
|---|---|
| tech_id | Unique identifier (tech-NNN) |
| study_id | FK → studies.study_id |
| name | Technology/product name |
| category | software-product / standard / architecture-pattern / category / practice |
| vendor | Vendor or standards body |
| description | Description from study context |
| lifecycle_status | active / evolved / legacy / discontinued |
| lifecycle_note | Narrative explanation of lifecycle |
| successor_technology | Successor technologies, if applicable |

**Technology Lifecycle Summary:**

| Technology | Lifecycle | Note |
|---|---|---|
| Virtual Data Warehouse (concept) | Evolved | Became data virtualization, then data fabric |
| DataDirect SmartData | Discontinued | Absorbed into successor DataDirect products |
| DataDirect Explorer | Discontinued | Desktop tool discontinued post-Merant restructuring |
| DataDirect ODBC Pack | Active | Continues as Progress DataDirect Drivers |
| DataDirect SequeLink | Discontinued | Superseded by modern middleware |
| ODBC Standard | Active | Remains widely supported connectivity standard |
| SQL | Active | Remains dominant query language |
| Cognos Impromptu | Discontinued | Replaced by IBM Cognos Analytics |
| Business Objects BusinessObjects | Active | Continues as SAP BusinessObjects BI |

### observations.csv
45 individual observations extracted from the study, covering analyst claims, factual statements, user feedback, product features, market observations, and pricing information.

| Field | Description |
|---|---|
| obs_id | Unique identifier (obs-NNN) |
| study_id | FK → studies.study_id |
| observation_type | claim / fact / user-feedback / market-observation / product-feature / pricing |
| subject_entity_id | FK → entities.entity_id (nullable) |
| subject_tech_id | FK → technologies.tech_id (nullable) |
| text | Full text of observation |
| sentiment | positive / neutral / negative |
| page_num | Source page number |
| section | Section heading in source document |
| tags | Comma-separated topic tags |

**Observation Distribution:**

| Type | Count |
|---|---|
| product-feature | 17 |
| claim | 12 |
| user-feedback | 6 |
| market-observation | 5 |
| fact | 4 |
| pricing | 1 |

**Sentiment Distribution:**

| Sentiment | Count |
|---|---|
| positive | 29 |
| neutral | 15 |
| negative | 1 |

### codes.csv
Controlled vocabulary for all categorical fields used across the package. Organized by scheme.

| Scheme | Purpose |
|---|---|
| study-type | Classification of study format |
| methodology | Research methods used |
| domain | Subject domain classification |
| entity-type | Classification of entities |
| entity-status | Current status of entities |
| tech-lifecycle | Current lifecycle of technologies |
| observation-type | Classification of extracted observations |
| sentiment | Sentiment of analyst statements |

---

## Key Themes

### 1. Metadata-Driven Data Access
The Virtual Data Warehouse's central innovation was its SmartData semantic layer — an ODBC driver that wrapped each data source in an intelligent metadata layer, creating "SmartSets" (virtual databases) that generated SQL dynamically. This approach anticipated modern data virtualization by 20+ years.

### 2. Virtual vs. Physical Warehousing
Aberdeen positioned the VDW as a flexible alternative or complement to physical data warehouses, useful for departmental needs, interim implementation phases, and transforming legacy/OLTP systems into analytical resources without the cost and complexity of ETL pipelines.

### 3. ODBC as Universal Connector
Intersolv's DataDirect ODBC Pack, supporting 35+ databases across 8 operating systems, was central to the VDW's cross-platform value proposition. ODBC remains active and relevant; the DataDirect brand survived through multiple ownership changes to Progress Software.

### 4. Competitive Stratification
Aberdeen observed a rapid reshaping of the query/reporting market in 1995. Both major competitors (Cognos with Impromptu, Business Objects with BusinessObjects) were in transition — Cognos merging Impromptu with Powerplay, Business Objects preparing the Mercury microcube system. Both were eventually acquired by major enterprise vendors (IBM and SAP respectively).

### 5. Server-Side Scalability via Acquisition
The TechGnosis acquisition gave Intersolv server-based scalability (SequeLink) to extend the VDW from departmental to enterprise scale. This acquisition strategy — buying specialized middleware to round out a product — was common in the 1990s data infrastructure market.

---

## Historical Context

This profile was published in the same month as the VDW's launch (October 1995), making it a near-contemporaneous review. Within three years, most of the major players covered in the study had been consolidated through M&A:

- **Intersolv** → Acquired by Micro Focus (1998) → Merant → DataDirect assets to Progress Software (2003)
- **TechGnosis** → Acquired by Intersolv just weeks before this profile was published (October 23, 1995)
- **Cognos** → Acquired by IBM (2008)
- **Business Objects** → Acquired by SAP (2008)

The Virtual Data Warehouse concept itself proved prescient: the idea of metadata-driven, virtualized access to distributed sources without physical consolidation became the foundation of modern data virtualization platforms (Denodo, TIBCO Data Virtualization) and data fabric architectures.

---

## Usage

### Load with frictionless-py

```python
from frictionless import Package

package = Package("datapackage.json")
for resource in package.resources:
    print(resource.name, resource.read())
```

### Load CSVs with pandas

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")
```

See `scripts/demo_analysis.py` for a complete demonstration with analysis queries.

---

## Sources

- Aberdeen Group (1995). *Exploring Intersolv's Virtual Data Warehouse*. https://web.archive.org/web/19970108191541/http://www.aberdeen.com:80/secure/profiles/intsolv/interslv.htm
- Micro Focus Wikipedia article: https://en.wikipedia.org/wiki/Micro_Focus
- Intersolv EDM2 article: https://www.edm2.com/index.php/Intersolv
- NYT: Micro Focus to Buy Intersolv (1998): https://www.nytimes.com/1998/06/18/business/company-news-micro-focus-to-buy-intersolv-for-534-million-in-stock.html
- Washington Post: Intersolv Buys TechGnosis (1995): https://www.washingtonpost.com/archive/business/1995/11/20/intersolv-buys-its-way-up-the-software-ladder/e7fd6b8a-11cb-4af5-9088-972a85f6a71f/
- BusinessObjects Wikipedia: https://en.wikipedia.org/wiki/BusinessObjects
- IBM acquires Cognos (2007): https://www.ibm.com/investor/att/pdf/ircorner/08-04-03-1.pdf
- Progress Software acquires DataDirect (2003): https://goldengatecap.com/progress-software-completes-acquisition-of-datadirect/
- Progress Software Wikipedia: https://en.wikipedia.org/wiki/Progress_Software
