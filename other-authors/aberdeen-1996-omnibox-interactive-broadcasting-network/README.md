# OmniBox Interactive Broadcasting Network: Bringing Electronic Commerce and Entertainment to the Masses

**Aberdeen Group Archival Research Collection — Frictionless Data Package**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-omnibox-interactive-broadcasting-network` |
| **Author** | Aberdeen Group |
| **Date** | 1996-11-01 |
| **Type** | market-study |
| **Domain** | interactive-TV, e-commerce, digital-broadcasting |
| **Methodology** | industry-analysis, competitive-profiling, expert-opinion |
| **License** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group profiles OmniBox, Inc., a Stamford CT startup with patented technology for delivering interactive television, electronic commerce, and digital content to homes via cable, satellite, and the Internet. The study evaluates OmniBox's architecture—comprising compression technology, transaction processing, and set-top hardware—and positions it as the most comprehensive model for home electronic commerce delivery seen to date. Aberdeen predicts OmniBox stands out as an early leader among vendors competing for the nascent 100-million-household US interactive TV market.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | OmniBox was an Aberdeen vendor profile in the emerging interactive-TV/e-commerce space; while Aberdeen was influential, OmniBox was a small startup and the study filled a niche rather than shaping broad industry direction. |
| **Relevance** | medium | The architectural vision of converging broadcast content with transactional e-commerce foreshadows streaming+commerce platforms; the specific hardware details (set-top boxes, 28.8Kbps modems) are obsolete. |
| **Prescience** | low | OmniBox predicted rapid 1997 rollout and mass-market success; the company never achieved commercial scale, was overtaken by cable-modem ISPs and web browsers, and the OmniBox network never materialized as described. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | `data/studies.csv` | 1 |
| Entities | `data/entities.csv` | 6 |
| Technologies | `data/technologies.csv` | 7 |
| Observations | `data/observations.csv` | 26 |
| Codes | `data/codes.csv` | (controlled vocabulary) |

**Observation types:** actual-outcome: 3; benchmark-result: 1; framework-factor: 3; market-data: 4; strategy-classification: 2; technology-assessment: 9; viability-prediction: 4

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

> Aberdeen Group. (1996). *OmniBox Interactive Broadcasting Network: Bringing Electronic Commerce and Entertainment to the Masses*. Aberdeen Group, Inc., Boston, MA.
> Archived: [aberdeen-1996-omnibox-interactive-broadcasting-network](https://web.archive.org/web/19970604113432/http://www.aberdeen.com:80/secure/profiles/1997/omni/body.htm)
> Dataset DOI: [PENDING — assign via Zenodo]

---

## Source

Original document archived at the Wayback Machine:
https://web.archive.org/web/19970604113432/http://www.aberdeen.com:80/secure/profiles/1997/omni/body.htm

Copyright 1996 Aberdeen Group, Inc., Boston, Massachusetts
This dataset is released under CC-BY-4.0 for research and archival purposes.
