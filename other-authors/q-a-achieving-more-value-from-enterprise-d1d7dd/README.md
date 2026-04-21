# Q&A: Achieving More Value from Enterprise Applications

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (AberdeenGroup) — Enterprise Systems Journal |
| Date | 2006-05-23 |
| Type | memoir |
| Domain | enterprise-soa-applications |
| License | CC-BY-4.0 |

## Abstract

Kastner-authored Q&A for Enterprise Systems Journal (2006-05-23) accompanying the AberdeenGroup Benchmark Report 'Achieving More Value from Enterprise Applications.' Kastner, then Research Vice President and co-founder of enterprise integration research at AberdeenGroup, diagnoses 'siloed applications connected with the software equivalent of chewing gum and baling wire,' reports that more than half of surveyed enterprises are unhappy with enterprise-application ROI and that over two-thirds view SOA technologies as the improvement path, warns against relying on SOA-enabled ERP as a general SOA toolset (the 'accidental architecture' trap), and recommends cross-platform, cross-process, cross-application capabilities when evaluating SOA infrastructure.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 5 |
| observations.csv | 8 |
| codes.csv | 25 |

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

Peter S. Kastner (AberdeenGroup) — Enterprise Systems Journal (2006). Q&A: Achieving More Value from Enterprise Applications.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, oral-history
