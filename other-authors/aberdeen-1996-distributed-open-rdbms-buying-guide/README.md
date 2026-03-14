# The Distributed, Open Relational Database Management Systems Buying Guide: 1996 Edition

> **Study ID:** `aberdeen-1996-distributed-open-rdbms-buying-guide`
> **Author:** Aberdeen Group
> **Date:** 1996-10-01
> **License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
> **Archived:** 2026-03-14 via Archival Ingest Skill v13

---

## Abstract

Aberdeen Group's 1996 Distributed, Open Relational Database Management Systems (DORS) Buying Guide evaluates eight leading RDBMS suppliers—including IBM, Oracle, Microsoft, Sybase, Informix, Computer Associates, Progress Software, and Software AG—against five core technology categories: scalability, distributed technology, open technology, toolkits, and next-generation capabilities including Internet/Intranet, OLAP, and universal servers. The guide identifies the shift toward distributed data access and Internet-driven data management as the defining trend, and provides IS buyers with a framework for evaluating vendor offerings against enterprise requirements.

---

## Study Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This was a leading analyst guide addressing the pivotal 1996 RDBMS market transition toward distributed and Internet-connected data architectures, published by Aberdeen Group at a moment when enterprises were choosing platforms that would define their data infrastructure for a decade. |
| **Relevance** | medium | The five core evaluation dimensions (scalability, distributed technology, openness, tooling, next-gen capability) remain a valid analytical framework; however, most specific vendor products and competitive rankings are obsolete given Oracle's dominance, Microsoft SQL Server's rise, and the acquisition of Sybase by SAP. |
| **Prescience** | high | Aberdeen's prediction that distributed data access and Internet connectivity would drive RDBMS evolution proved entirely correct—Oracle, IBM DB2, and Microsoft SQL Server all pivoted to Internet-era architectures through the late 1990s and early 2000s, exactly as forecasted. |

---

## Dataset Contents

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata (16-field v12 schema) |
| `data/entities.csv` | 9 | Named organizations and institutions |
| `data/technologies.csv` | 7 | Technologies referenced in study |
| `data/observations.csv` | 19 | Analytical observations and outcomes |
| `data/codes.csv` | 23 | Controlled vocabulary definitions |
| `schema/schema_org.json` | — | Schema.org Dataset JSON-LD |
| `source/original_text.md` | — | Full original document + metadata appendix |
| `scripts/demo_analysis.py` | — | Validation and analysis script |

**Observation breakdown:** actual-outcome: 3; expert-opinion: 2; framework-factor: 5; market-data: 1; strategy-classification: 3; technology-assessment: 2; viability-prediction: 3

**Viability predictions:** 3 | **Actual outcomes:** 3

---

## Metadata

| Field | Value |
|-------|-------|
| study_id | `aberdeen-1996-distributed-open-rdbms-buying-guide` |
| type | market-study |
| subject_domain | RDBMS-database-software |
| methodology | industry-analysis, competitive-profiling, document-review |
| source_file | 1996 THE DISTRIBUTED, OPEN RELATIONAL DATABASE MANAGEMENT SYSTEMS BUYING GUIDE_ 1996 EDITION.pdf |

---

## Quick Start (Python / pandas)

```python
import pandas as pd
import os

base = os.path.dirname(os.path.abspath(__file__))

studies      = pd.read_csv(os.path.join(base, 'data', 'studies.csv'))
entities     = pd.read_csv(os.path.join(base, 'data', 'entities.csv'))
technologies = pd.read_csv(os.path.join(base, 'data', 'technologies.csv'))
observations = pd.read_csv(os.path.join(base, 'data', 'observations.csv'))
codes        = pd.read_csv(os.path.join(base, 'data', 'codes.csv'))

# Show observation type distribution
print(observations['observation_type'].value_counts())

# Show predictions vs. outcomes
preds    = observations[observations['observation_type'] == 'viability-prediction']
outcomes = observations[observations['observation_type'] == 'actual-outcome']
print(f"Predictions: {len(preds)}, Outcomes: {len(outcomes)}")
```

---

## Frictionless Validation

```bash
pip install frictionless
frictionless validate datapackage.json
```

---

## Citation

```
Aberdeen Group. (1996). The Distributed, Open Relational Database Management Systems Buying Guide: 1996 Edition.
Aberdeen Group, Inc., Boston, Massachusetts.
Archived 2026-03-14 via Archival Ingest Skill v13.
DOI: [PENDING]
Wayback Machine source: https://web.archive.org/web/*/http://www.aberdeen.com/
```

---

## License

[Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/)

Original study copyright © 1996 Aberdeen Group, Inc. Archival metadata and structured datasets © 2026 under CC-BY-4.0.
