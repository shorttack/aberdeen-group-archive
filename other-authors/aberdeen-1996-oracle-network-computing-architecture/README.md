# Oracle's Network Computing Architecture

**Aberdeen Group Archival Research Collection — Frictionless Data Package**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-oracle-network-computing-architecture` |
| **Author** | Aberdeen Group |
| **Date** | 1996-10-01 |
| **Type** | market-study |
| **Domain** | enterprise-software, distributed-computing, internet-architecture, RDBMS |
| **Methodology** | industry-analysis, competitive-profiling, expert-opinion, document-review |
| **License** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |

## Abstract

Aberdeen Group evaluates Oracle's Network Computing Architecture (NCA), a comprehensive framework integrating multi-tier client-server, Internet, and distributed-object technologies through a 'cartridge' component model and Inter-Cartridge Exchange (ICX) middleware based on CORBA. The study concludes that NCA is not a 'marketecture' but a substantive extension of proven Oracle products providing a least-cost migration path to mission-critical 21st-century transaction processing, and recommends ISVs and enterprise IS factor it into their 1-2 year technology strategies.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Oracle's NCA represented a defining moment in enterprise middleware strategy as the industry transitioned from client-server to Internet architectures; Aberdeen's endorsement of NCA over competing approaches from Microsoft and others carried significant weight with enterprise IT buyers. |
| **Relevance** | medium | The cartridge/component model anticipated modern microservices and API-based architectures; Oracle's Universal Server became the foundation for Oracle Database which remains active, though NCA-specific cartridge mechanisms are long obsolete. |
| **Prescience** | high | Aberdeen correctly predicted Oracle would dominate enterprise internet database strategy and that component-based architecture would become the standard; Oracle remains a dominant enterprise database and application platform 30 years later. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | `data/studies.csv` | 1 |
| Entities | `data/entities.csv` | 6 |
| Technologies | `data/technologies.csv` | 10 |
| Observations | `data/observations.csv` | 30 |
| Codes | `data/codes.csv` | (controlled vocabulary) |

**Observation types:** actual-outcome: 5; benchmark-result: 2; expert-opinion: 1; framework-factor: 3; market-data: 2; strategy-classification: 2; technology-assessment: 10; viability-prediction: 5

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

> Aberdeen Group. (1996). *Oracle's Network Computing Architecture*. Aberdeen Group, Inc., Boston, MA.
> Archived: [aberdeen-1996-oracle-network-computing-architecture](https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm)
> Dataset DOI: [PENDING — assign via Zenodo]

---

## Source

Original document archived at the Wayback Machine:
https://web.archive.org/web/19970604113530/http://www.aberdeen.com:80/secure/profiles/oraclnca/orclnca.htm

Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts
This dataset is released under CC-BY-4.0 for research and archival purposes.
