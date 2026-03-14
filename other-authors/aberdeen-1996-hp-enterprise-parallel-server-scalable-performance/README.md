# Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance

> Aberdeen Group Research Profile | 1996-07-01 | CC-BY-4.0

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-hp-enterprise-parallel-server-scalable-performance` |
| **Author** | Aberdeen Group |
| **Date** | 1996-07-01 |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112011544/http://www.aberdeen.com:80/secure/profiles/hp_eps/hpeps.htm) |

## Abstract

This Aberdeen Group profile evaluates Hewlett-Packard's Enterprise Parallel Server (EPS) architecture, specifically the EPS21 and EPS30 introduced May 15, 1996. The study examines EPS's combination of SMP nodes connected via a fibre channel switch for high-end OLTP and data warehousing, compares it against IBM RS/6000 SP and other competitors, documents a TPC-C benchmark of 17,826 tpmC at $396/tpmC for the EPS30, and reports positive feedback from early adopters.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First detailed independent assessment of HP's EPS architecture at launch, documenting its TPC-C benchmark results and positioning against IBM RS/6000 SP at a decisive moment in Unix datacenter competition; directly informed enterprise procurement decisions. |
| **Relevance** | low | HP's EPS platform and PA-RISC architecture are long discontinued; HP-UX servers have declined significantly since the rise of x86/Linux; methodology for evaluating parallel server architectures retains some value for historical comparison. |
| **Prescience** | medium | Aberdeen correctly predicted HP's PA-8000 upgrade would improve performance and that fibre channel would become an industry standard. The prediction that EPS would become a 'datacenter system of choice' was overstated; HP servers lost significant ground to x86/Linux in subsequent years. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata with assessment ratings |
| `data/entities.csv` | 10 | Organizations and companies referenced |
| `data/technologies.csv` | 8 | Technologies mentioned |
| `data/observations.csv` | 20 | Extracted observations and predictions |
| `data/codes.csv` | 24 | Controlled vocabulary definitions |

**Observation types:** actual-outcome: 3; benchmark-result: 4; expert-opinion: 1; framework-factor: 3; market-data: 1; strategy-classification: 1; technology-assessment: 4; viability-prediction: 3

## Quick Start (Python)

```python
import pandas as pd

obs = pd.read_csv("data/observations.csv")
entities = pd.read_csv("data/entities.csv")
techs = pd.read_csv("data/technologies.csv")

# Show predictions and outcomes
predictions = obs[obs["observation_type"] == "viability-prediction"]
outcomes = obs[obs["observation_type"] == "actual-outcome"]
print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

## Validation

```bash
frictionless validate datapackage.json
python scripts/demo_analysis.py
```

## Citation

```
Aberdeen Group. (1996). Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance. Aberdeen Group, Inc., Boston MA.
Archived: https://web.archive.org/web/19970112011544/http://www.aberdeen.com:80/secure/profiles/hp_eps/hpeps.htm
Dataset: https://github.com/kastner/aberdeen-archival/aberdeen-1996-hp-enterprise-parallel-server-scalable-performance
License: CC-BY-4.0
DOI: [PENDING — assign via Zenodo]
```

## Methodology

This profile was produced using Aberdeen Group's vendor assessment methodology combining:
- Industry analysis and competitive profiling
- Field research with enterprise customers
- Benchmarking against published TPC and industry standards (where applicable)

---
*Processed by Archival Ingest Skill v13 | 2026-03-14*
