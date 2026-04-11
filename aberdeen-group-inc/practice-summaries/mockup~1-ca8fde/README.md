# Network Operating Systems: 1998 Practice Summary — Mockup/Template

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | network-operating-systems |
| License | CC-BY-4.0 |

## Abstract

A draft/skeleton version of Aberdeen Group's Network Operating Systems (NOS) 1998 Practice Summary, covering the competitive landscape among Novell NetWare, IBM OS/2 Warp Server, and Microsoft Windows NT Server. The document includes a table of contents, preface with strategic market questions, and abbreviated supplier abstracts for IBM, Microsoft, and Novell — but substantive body content is largely absent or placeholder. The strategic questions posed reflect the pivotal moment when Microsoft NT Server was rapidly displacing legacy NOS vendors.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 5 |
| observations.csv | 10 |
| codes.csv | 27 |

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

Aberdeen Group (1998). Network Operating Systems: 1998 Practice Summary — Mockup/Template.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
