# Data General Corporation — Aberdeen Group Company Profile

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | `aberdeen-1996-data-general-corporation` |
| **Author** | Aberdeen Group |
| **Date** | 1996-05-01 |
| **Type** | market-study |
| **Domain** | enterprise-computing |
| **License** | CC-BY-4.0 |
| **Source File** | 1996 Data General Corporation pr.pdf |

## Abstract

Aberdeen Group profiles Data General Corporation's strategy of delivering integrated open-systems solutions through deep ISV partnerships with SAP, Oracle, and PeopleSoft, anchored by its AViiON UNIX/NT servers and CLARiiON storage subsystems. The study documents DG's revenue mix transformation from proprietary minicomputers to over 90% open-systems revenues, and validates partner and customer satisfaction through primary interviews. Aberdeen concludes DG has found a sustainable balance between responsiveness and global scale.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | The profile captured DG's pivotal transition from proprietary minicomputers to open systems at a critical juncture in mid-1990s enterprise computing; valuable as an independent benchmark of ISV partnership depth, though narrowly scoped to a single vendor. |
| **Relevance** | low | Data General was acquired by EMC in 1999 and all server lines were discontinued; the specific hardware and ISV context is largely obsolete, leaving the study as primarily archival/historical interest. |
| **Prescience** | low | Aberdeen's optimistic prediction of DG's long-term viability proved incorrect; EMC acquired DG in 1999 for $1.1 billion and immediately shut down AViiON, retaining only CLARiiON storage. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessments |
| entities.csv | 6 | Organizations referenced in the study |
| technologies.csv | 6 | Technologies referenced in the study |
| observations.csv | 23 | Extracted analytical observations |
| codes.csv | 18 | Controlled vocabulary definitions |

### Observations by Type

| Type | Count |
|------|-------|
| actual-outcome | 2 |
| benchmark-result | 1 |
| expert-opinion | 4 |
| framework-factor | 5 |
| market-data | 3 |
| strategy-classification | 3 |
| technology-assessment | 3 |
| viability-prediction | 2 |

## Quick Start

```python
import pandas as pd
import os

base = os.path.dirname(os.path.abspath(__file__))
studies = pd.read_csv(os.path.join(base, "data/studies.csv"))
entities = pd.read_csv(os.path.join(base, "data/entities.csv"))
technologies = pd.read_csv(os.path.join(base, "data/technologies.csv"))
observations = pd.read_csv(os.path.join(base, "data/observations.csv"))
codes = pd.read_csv(os.path.join(base, "data/codes.csv"))

print(f"Study: {studies.iloc[0]['title']}")
print(f"Observations: {len(observations)}")
print(observations.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996). *Data General Corporation — Aberdeen Group Company Profile*. Aberdeen Group, Inc., Boston, Massachusetts.
> Archived: https://web.archive.org/web/19970112011812/http://www.aberdeen.com:80/secure/profiles/datagen/dg.htm
> Dataset DOI: [pending Zenodo deposit]

## Methodology

industry-analysis, competitive-profiling, field-research
