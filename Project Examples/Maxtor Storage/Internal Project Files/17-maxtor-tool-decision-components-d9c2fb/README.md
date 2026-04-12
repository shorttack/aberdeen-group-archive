# ILM/Pools of Storage Tool Decision Components and IP Framework

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Peter Kastner) |
| Date | 2003-01-01 |
| Type | employer-record |
| Domain | storage-strategy / intellectual-property |
| License | CC-BY-4.0 |

## Abstract

An internal Aberdeen Group strategy presentation outlining the business premises and IP framework for the ILM/Pools of Storage (PoS) Hardware Hawker (HH) sales tool developed for Maxtor. The document establishes that the HH tool is Aberdeen IP with Maxtor receiving limited usage rights; proposes a broader commercialization strategy through a Storage COE involving HP, EMC, IBM, Intel, Sun, and others; and presents a permitted usage matrix defining where Aberdeen deliverables (white papers and ILM tools) may be deployed. A critical IP dispute between Aberdeen and Maxtor over tool rights is documented.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 5 |
| observations.csv | 16 |
| codes.csv | 29 |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

Aberdeen Group (Peter Kastner) (2003). ILM/Pools of Storage Tool Decision Components and IP Framework.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
