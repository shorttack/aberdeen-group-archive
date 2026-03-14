# Open Market: Delivering the Infrastructure For Truly Open Web-based Commerce

**Aberdeen Group Archival Research Collection — Frictionless Data Package**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-open-market-web-based-commerce` |
| **Author** | Aberdeen Group |
| **Date** | 1996-10-01 |
| **Type** | market-study |
| **Domain** | web-commerce, e-commerce-infrastructure, payment-systems |
| **Methodology** | industry-analysis, competitive-profiling, field-research, expert-opinion |
| **License** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group profiles Open Market, Inc. (Cambridge, MA), a pioneer in enterprise-grade web commerce infrastructure. The study examines Open Market's product suite—OM-Transact, OM-Axcess, and OM-SecureLink—designed to support many-to-many web-based transactions across multiple content servers and back-office systems. Aberdeen strongly recommends Open Market's platform as the most comprehensive and production-ready solution for enterprises building next-generation electronic commerce infrastructure, and contrasts it favorably against IBM and point-to-point proprietary competitors.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Open Market was among the first enterprise-grade web commerce platforms at a pivotal moment in e-commerce infrastructure formation (1996); Aberdeen's endorsement to AT&T, BT, MCI, and major banks made this a significant industry signal. |
| **Relevance** | medium | The many-to-many transaction architecture and CSP model anticipated API-based commerce ecosystems; specific OM-Transact/OM-Axcess products are obsolete, but the conceptual framework for distributed commerce middleware remains instructive. |
| **Prescience** | medium | Aberdeen correctly predicted that enterprise web commerce would require comprehensive back-office integration beyond simple HTTP servers; however Open Market was acquired by Divine (2001) then went bankrupt (2003), not achieving the sustained market leadership Aberdeen projected. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | `data/studies.csv` | 1 |
| Entities | `data/entities.csv` | 10 |
| Technologies | `data/technologies.csv` | 7 |
| Observations | `data/observations.csv` | 28 |
| Codes | `data/codes.csv` | (controlled vocabulary) |

**Observation types:** actual-outcome: 3; benchmark-result: 1; expert-opinion: 2; framework-factor: 4; market-data: 5; strategy-classification: 5; technology-assessment: 6; viability-prediction: 2

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

> Aberdeen Group. (1996). *Open Market: Delivering the Infrastructure For Truly Open Web-based Commerce*. Aberdeen Group, Inc., Boston, MA.
> Archived: [aberdeen-1996-open-market-web-based-commerce](https://web.archive.org/web/19970604113516/http://www.aberdeen.com:80/secure/profiles/openmk/body.htm)
> Dataset DOI: [PENDING — assign via Zenodo]

---

## Source

Original document archived at the Wayback Machine:
https://web.archive.org/web/19970604113516/http://www.aberdeen.com:80/secure/profiles/openmk/body.htm

Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts
This dataset is released under CC-BY-4.0 for research and archival purposes.
