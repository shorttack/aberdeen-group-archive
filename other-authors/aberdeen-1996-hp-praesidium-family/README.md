# Hewlett-Packard's Praesidium: A Family of Products To make Business on the Net A Reality

> Aberdeen Group Research Profile | 1996-09-09 | CC-BY-4.0

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-hp-praesidium-family` |
| **Author** | Aberdeen Group |
| **Date** | 1996-09-09 |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19961023162641/http://www.aberdeen.com:80/secure/profiles/hp_praes/hp.htm) |

## Abstract

This Aberdeen Group profile, dated September 9, 1996, evaluates Hewlett-Packard's Praesidium security framework for enterprise Internet and Intranet transaction security. The study examines HP's VirtualVault trusted gateway, Praesidium Authorization Server, ImagineCard smart card authentication, and the International Cryptography Framework (ICF), positioning them as a comprehensive solution for moving enterprises from pilot electronic commerce projects to production-grade deployments.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | One of the earliest detailed assessments of a comprehensive enterprise Internet security framework at the dawn of commercial e-commerce; addressed foundational security architecture problems that defined the next decade of IT security practice. |
| **Relevance** | medium | The security framework concepts (authentication, authorization separation, trusted gateway, role-based access) remain foundational to modern security architecture; specific HP products are obsolete but the threat model and architectural patterns transfer directly to Zero Trust and IAM frameworks. |
| **Prescience** | high | Aberdeen's predictions that enterprise security would require integrated frameworks rather than point solutions, and that role-based authorization would displace access control lists, proved highly accurate — both are now standard security architecture principles. |

## Data Tables

| File | Rows | Description |
|------|------|-------------|
| `data/studies.csv` | 1 | Study metadata with assessment ratings |
| `data/entities.csv` | 10 | Organizations and companies referenced |
| `data/technologies.csv` | 8 | Technologies mentioned |
| `data/observations.csv` | 20 | Extracted observations and predictions |
| `data/codes.csv` | 24 | Controlled vocabulary definitions |

**Observation types:** actual-outcome: 4; expert-opinion: 1; framework-factor: 4; market-data: 2; strategy-classification: 2; technology-assessment: 3; viability-prediction: 4

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
Aberdeen Group. (1996). Hewlett-Packard's Praesidium: A Family of Products To make Business on the Net A Reality. Aberdeen Group, Inc., Boston MA.
Archived: https://web.archive.org/web/19961023162641/http://www.aberdeen.com:80/secure/profiles/hp_praes/hp.htm
Dataset: https://github.com/kastner/aberdeen-archival/aberdeen-1996-hp-praesidium-family
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
