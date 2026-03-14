# Aberdeen Group — New LIMD Technology: Speed Plus Real-World Experience (1995)

**Frictionless Data Package** | Study ID: `aberdeen-1995-limd-technology` | Study #12

---

## Overview

This data package archives the Aberdeen Group Technology Viewpoint **Volume 8, Number 15** (December 1, 1995), titled *"New LIMD Technology: Speed Plus Real-World Experience"*. The study analyzes Large-Scale In-Memory Database (LIMD) technology — specifically how 64-bit server architectures and large main memories deliver 10-100× performance improvements for data warehousing, OLTP, and decision support workloads.

The package follows the [Frictionless Data](https://frictionlessdata.io/) specification and includes normalized CSV resources derived from the original PDF, a `datapackage.json` descriptor, a Schema.org JSON-LD metadata file, and a Python demo analysis script.

**Source:** [Aberdeen Group Technology Viewpoints Archive (via Wayback Machine)](https://web.archive.org/web/19970112010820/http://www.aberdeen.com:80/secure/viewpnts/v8n15/v8n15.htm)

---

## Study Metadata

| Field | Value |
|---|---|
| Title | New LIMD Technology: Speed Plus Real-World Experience |
| Author | Aberdeen Group |
| Publisher | Aberdeen Group |
| Date | December 1, 1995 |
| Volume/Issue | Vol. 8 / No. 15 |
| Type | market-study (Technology Viewpoint) |
| Domain | database-performance-technology |
| Methodology | industry-analysis, benchmarking, field-research |
| Language | English |
| Geographic Scope | Global |

---

## Abstract

Technology Viewpoint analyzing Large-Scale In-Memory Database (LIMD) technology, examining how 64-bit architectures and large main memories deliver 10-100× performance improvements for data warehousing, OLTP, and decision support. The study defines LIMD as systems supporting ≥5 GB of main memory paired with RDBMS software capable of exploiting in-memory data storage. Aberdeen identifies Digital Equipment Corporation (with its Alpha 8200/8400 servers and VLM64 architecture) as the clear market leader, partnered with Oracle, Sybase, and Informix RDBMSs. Key benchmark evidence includes a record TPC-C result of 11,456 tpmC at $286/tpmC for Digital/Oracle, a measured 105× speedup for 5-way joins, and a strong correlation of 1 GB RAM ≈ 1,300 additional tpmC. The study concludes that LIMD has cleared the real-world acceptance threshold and recommends immediate prototyping and implementation.

---

## Directory Structure

```
aberdeen-1995-limd-technology/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Bibliographic record for the study
│   ├── entities.csv          # Organizations with current corporate status
│   ├── technologies.csv      # Technologies with lifecycle status
│   ├── observations.csv      # All extracted observations (48 rows)
│   └── codes.csv             # Controlled vocabulary for coded fields
├── schema/
│   └── schema_org.json       # Schema.org JSON-LD metadata
└── scripts/
    └── demo_analysis.py      # Python demo: load, validate, and analyze the package
```

---

## Resources

### `data/studies.csv`
Single-row master record for the study with full bibliographic metadata including publication date, volume/issue, methodology, and source URL.

**Key fields:** `study_id`, `title`, `author`, `publication_date`, `study_type`, `domain`, `methodology`, `source_url`

---

### `data/entities.csv`
14 organizational entities mentioned in the study, each with:
- Role in the study (author, subject-leader, subject, case-study-user)
- Current corporate status as of 2026 (active, acquired, defunct, rebranded)
- Acquisition history and acquiring entity

**Notable entities:**

| Entity | Role | Current Status |
|---|---|---|
| Aberdeen Group | Author | Acquired (Harte-Hanks 2001) |
| Digital Equipment Corporation | Subject Leader | Acquired → Compaq 1998 → HP 2002 |
| Oracle Corporation | Subject Leader | Active |
| Sybase | Subject Leader | Acquired by SAP 2010 |
| Informix | Subject | Acquired by IBM 2001 |
| Silicon Graphics (SGI) | Subject | Defunct (assets to HPE) |
| Sun Microsystems | Subject | Acquired by Oracle 2010 |
| Tandem Computers | Subject | Acquired by Compaq 1997 |
| Merrill Lynch | Case Study User | Acquired by Bank of America 2009 |
| CA-Ingres | Subject | Rebranded as Actian |

---

### `data/technologies.csv`
20 technologies discussed in the study, each with:
- Technology category (database-architecture, hardware-architecture, processor, etc.)
- Lifecycle status (active, evolved, obsolete, ubiquitous)
- Approximate introduction year and obsolescence year
- Modern successor technologies

**Lifecycle summary:**

| Status | Count | Examples |
|---|---|---|
| Evolved | 8 | LIMD → SAP HANA/Oracle TimesTen; Oracle 7.x → Oracle 23c; Sybase System 11 → SAP ASE |
| Obsolete | 7 | VLM64; Alpha chip; 32-bit architecture; Memory Channel; PA-RISC; MIPS 64-bit; ATM |
| Active | 3 | SMP; MPP; TPC-C benchmark |
| Ubiquitous | 1 | 64-bit computing |
| Other/Niche | 1 | NonStop Guardian (evolved → HPE NonStop SQL) |

---

### `data/observations.csv`
**48 observations** extracted from the study covering:

| Observation Type | Count |
|---|---|
| Performance claims | 14 |
| Benchmark results | 7 |
| Hardware specifications | 7 |
| Market assessments | 5 |
| Use cases | 5 |
| Market statistics | 4 |
| Technology context/definition | 4 |
| Forecasts | 1 |
| Other | 1 |

**Key quantitative observations:**

| Metric | Value | Unit | Source |
|---|---|---|---|
| Digital/Oracle TPC-C record | 11,456 | tpmC | Primary text |
| Digital/Oracle price-performance | 286 | USD/tpmC | Primary text |
| RAM-to-tpmC correlation | 1,300 | tpmC per GB | Primary text |
| Real-world performance improvement (typical) | 20–40 | × | Primary text |
| 5-way join speedup | 105 | × | Primary text |
| Oracle LIMD improvement (typical) | 20–40 | × | Primary text |
| Oracle join speedup (3-4-5-way vs non-LIMD) | >200 | × | Primary text |
| Alpha 8200 max memory | 6 | GB | Primary text |
| Alpha 8400 max memory | 14 | GB | Primary text |
| Alpha 8200 max CPUs | 6 | count | Primary text |
| Alpha 8400 max CPUs | 12 | count | Primary text |
| Total storage (Alpha 8x00) | 8.5 | TB | Primary text |
| Memory Channel bandwidth | 100 | MB/s | Primary text |
| Concurrent users (single server) | 10,000 | users | Primary text |
| Backup throughput | ≥100 | GB/hour | Primary text |
| Non-LIMD TPC-C scaling ceiling | 5,000 | tpmC | Primary text |

---

### `data/codes.csv`
Controlled vocabulary reference table with 40 codes across 9 code types:
`entity_type`, `current_status`, `tech_category`, `observation_type`, `methodology`, `domain`, `study_type`, `confidence`, `role_in_study`

---

## Entity Status Notes

| Entity | 1995 Status | Current (2026) |
|---|---|---|
| Digital | Market leader in LIMD | Absorbed into HP; VLM64/Alpha discontinued |
| Oracle | Leading RDBMS partner | Active; Oracle Database 23c current version |
| Sybase | Major RDBMS partner | SAP ASE; SAP IQ (IQ Accelerator lineage) |
| Informix | Strong RDBMS partner | IBM Informix 14.x |
| SGI | Minor player; OS limited to 2GB/process | Defunct; assets to HPE 2016 |
| Sun | Early-stage 64-bit UltraSPARC | Acquired by Oracle 2010; SPARC discontinued 2017 |
| Tandem | Experienced in >32-bit; NonStop line | HPE NonStop (active niche) |
| Merrill Lynch | LIMD early adopter | Bank of America (acquired 2009) |

---

## Technology Lifecycle Notes

LIMD as a concept has fully matured into modern **in-memory database** products including SAP HANA, Oracle TimesTen, VoltDB, SingleStore, and Redis. The specific 1995-era implementations (DEC Alpha/VLM64) are long obsolete, but their architectural principles directly underpin today's IMDB landscape.

The TPC-C benchmark record of 11,456 tpmC that was "record-shattering" in 1995 is exceeded by several orders of magnitude in 2024 (current TPC-C records exceed 800 million tpmC on modern cloud hardware).

---

## Usage

### Validate the package (requires `frictionless` Python library)
```bash
pip install frictionless
frictionless validate datapackage.json
```

### Run the demo analysis
```bash
pip install pandas matplotlib
python scripts/demo_analysis.py
```

### Load a resource in Python
```python
import pandas as pd

obs = pd.read_csv("data/observations.csv")
benchmarks = obs[obs["observation_type"] == "benchmark-result"]
print(benchmarks[["metric_name", "metric_value", "metric_unit"]].to_string())
```

---

## License

Data extracted and structured under [ODC Attribution License 1.0](https://opendatacommons.org/licenses/by/1-0/). Original study © 1995 Aberdeen Group, Inc. All trademarks are the property of their respective holders.

---

## Citation

> Aberdeen Group. (1995, December 1). *New LIMD Technology: Speed Plus Real-World Experience* (Technology Viewpoint, Vol. 8, No. 15). Aberdeen Group, Inc. Archived: https://web.archive.org/web/19970112010820/http://www.aberdeen.com:80/secure/viewpnts/v8n15/v8n15.htm
