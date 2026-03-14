# Progress Software's WebSpeed: Business Transaction Processing On The Internet

**Aberdeen Group Archival Research Collection — Frictionless Data Package**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-progress-software-webspeed-internet` |
| **Author** | Aberdeen Group |
| **Date** | 1996-10-01 |
| **Type** | market-study |
| **Domain** | internet-development-tools, transaction-processing, web-application-development |
| **Methodology** | industry-analysis, competitive-profiling, expert-opinion, document-review |
| **License** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group profiles Progress Software's WebSpeed, an Internet development platform aimed at building data-intensive, scalable web applications that integrate with legacy transaction-processing systems. WebSpeed combines the Progress 4GL development environment with a multi-tier Transaction Server providing TP-monitor-like middleware, state management, and load balancing. Aberdeen recommends WebSpeed to enterprises seeking to merge proven client-server data-management with Internet architecture, and positions Progress as superior to both traditional CADE suppliers and new web-only toolset vendors for data-intensive Internet applications.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Progress Software held a meaningful but niche position in the mid-1990s application development market; WebSpeed addressed a real architectural gap but was less influential than Oracle, Microsoft, or Netscape in shaping internet application development at the industry level. |
| **Relevance** | low | WebSpeed's specific 4GL-based architecture was superseded by Java EE, .NET, and later frameworks; Progress Software survived as a company but WebSpeed is a legacy product primarily of historical interest to researchers studying 1990s internet development tooling. |
| **Prescience** | medium | Aberdeen correctly identified that state management and TP-monitor middleware would be essential for scalable web apps (validated by J2EE/EJB, later microservices), but WebSpeed itself lost to Java and .NET; Progress Software survived via pivot to OpenEdge and data integration. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | `data/studies.csv` | 1 |
| Entities | `data/entities.csv` | 8 |
| Technologies | `data/technologies.csv` | 9 |
| Observations | `data/observations.csv` | 24 |
| Codes | `data/codes.csv` | (controlled vocabulary) |

**Observation types:** actual-outcome: 2; benchmark-result: 1; expert-opinion: 1; framework-factor: 2; market-data: 3; strategy-classification: 3; technology-assessment: 10; viability-prediction: 2

---

## Quick Start

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")

# Filter predictions and their actual outcomes
predictions = observations[observations.observation_type == "viability-prediction"]
outcomes = observations[observations.observation_type == "actual-outcome"]
print(f"Predictions: {len(predictions)}, Actual outcomes: {len(outcomes)}")
```

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

## Run Demo Analysis

```bash
python scripts/demo_analysis.py
```

---

## Citation

> Aberdeen Group. (1996). *Progress Software's WebSpeed: Business Transaction Processing On The Internet*. Aberdeen Group, Inc., Boston, MA.
> Archived: [aberdeen-1996-progress-software-webspeed-internet](https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm)
> Dataset DOI: [PENDING — assign via Zenodo]

---

## Source

Original document archived at the Wayback Machine:
https://web.archive.org/web/19970604103320/http://www.aberdeen.com:80/secure/profiles/proweb/body.htm

Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts
This dataset is released under CC-BY-4.0 for research and archival purposes.
