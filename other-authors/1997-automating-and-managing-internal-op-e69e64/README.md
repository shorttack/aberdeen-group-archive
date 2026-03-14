# Automating and Managing Internal Operations

**Aberdeen Group White Paper | February 1997**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-automating-and-managing-internal-op-e69e64 |
| title | Automating and Managing Internal Operations |
| author | Aberdeen Group |
| date | 1997-02-01 |
| type | white-paper |
| subject_domain | IT-operations-management |
| methodology | field-research, industry-analysis, competitive-profiling |
| source_file | 1997 Automating and Managing Internal Operations wp.pdf |
| license | CC-BY-4.0 |

## Abstract

Aberdeen Group examines the trend toward 'Consolidated Operations Management' (COM) as enterprises automate internal processes—IT help desk, asset management, SLA tracking, procurement, and HR—using a common adaptable platform. The paper identifies six success factors for COM adoption and profiles Remedy Corporation's Action Request System (AR System) as the leading vehicle for this transition, citing its extensibility, 3,000-plus customer base, and use beyond traditional help desk functions.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | medium | Defined the 'Consolidated Operations Management' category and positioned help desk software as enterprise automation backbone; influential in framing ITSM market during Aberdeen's peak influence period. |
| Relevance | medium | The COM framework and its six success factors (adaptability, data access, UI, business rules, rapid modification, openness) remain conceptually applicable to modern ITSM and enterprise automation platforms, though specific product details are historical. |
| Prescience | high | Aberdeen's prediction that AR System would become a popular COM vehicle proved correct—Remedy grew to 7,000+ customers before acquisition by Peregrine/BMC; the ITSM platform consolidation trend Aberdeen described accurately forecast ServiceNow-era convergence. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 4 | Organizations referenced |
| technologies.csv | 5 | Technologies discussed |
| observations.csv | 21 | Extracted analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Aberdeen Group. (1997). *Automating and Managing Internal Operations*. Aberdeen Group White Paper.
Archived: https://web.archive.org/web/19970604112640/http://www.aberdeen.com:80/secure/whtpaper/1997/remedy/body.htm
License: CC-BY-4.0
