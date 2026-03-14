# Remote Access: Cisco's Untold Story

**Aberdeen Group Archival Research Collection — Frictionless Data Package**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-remote-access-cisco-untold-story` |
| **Author** | Aberdeen Group |
| **Date** | 1996-11-25 |
| **Type** | market-study |
| **Domain** | networking, remote-access, ISP-infrastructure, enterprise-networking |
| **Methodology** | industry-analysis, competitive-profiling, field-research, expert-opinion |
| **License** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group examines Cisco Systems' remote access strategy as of November 1996, revealing Cisco's 'untold story' of quietly dominating the enterprise branch-to-branch segment (60%+ market share) while making aggressive inroads into the high-end ISP and carrier markets with the AS5200 access server. The study evaluates Cisco's multi-product portfolio (AS5200, 3600, 1600 series), IOS software competitive advantages, and the Telebit MICA technology acquisition, predicting Cisco is better positioned than competitors to serve the rapidly evolving ISP/carrier market.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study documented Cisco's strategic pivot to the ISP/carrier market at the inflection point when internet access was transitioning from experimental to commercial infrastructure; Cisco's subsequent dominance of this market makes this a historically significant analysis of a turning-point moment. |
| **Relevance** | medium | Cisco remains dominant in enterprise networking 30 years later; the strategic frameworks (end-to-end solutions, IOS software as moat, acquisition-led tech expansion) remain applicable, though specific products (AS5200, ISDN, modem-based access) are long obsolete. |
| **Prescience** | high | Aberdeen correctly predicted Cisco would extend leadership to the ISP/carrier market (verified: Cisco became dominant in ISP infrastructure by 1999-2000), that IOS software would be Cisco's durable competitive moat, and that internet access would commoditize driving ISP consolidation—all of which materialized. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | `data/studies.csv` | 1 |
| Entities | `data/entities.csv` | 8 |
| Technologies | `data/technologies.csv` | 10 |
| Observations | `data/observations.csv` | 30 |
| Codes | `data/codes.csv` | (controlled vocabulary) |

**Observation types:** actual-outcome: 4; benchmark-result: 5; expert-opinion: 1; framework-factor: 2; market-data: 4; strategy-classification: 3; technology-assessment: 7; viability-prediction: 4

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

> Aberdeen Group. (1996). *Remote Access: Cisco's Untold Story*. Aberdeen Group, Inc., Boston, MA.
> Archived: [aberdeen-1996-remote-access-cisco-untold-story](https://web.archive.org/web/19970604113407/http://www.aberdeen.com:80/secure/profiles/1997/cisco1/body.htm)
> Dataset DOI: [PENDING — assign via Zenodo]

---

## Source

Original document archived at the Wayback Machine:
https://web.archive.org/web/19970604113407/http://www.aberdeen.com:80/secure/profiles/1997/cisco1/body.htm

Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
This dataset is released under CC-BY-4.0 for research and archival purposes.
