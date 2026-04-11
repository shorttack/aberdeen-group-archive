# Proposal for CA interBiz White Paper (July 1999)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1999-07-23 |
| Type | consulting-report |
| Domain | enterprise-application-software, e-commerce-infrastructure |
| License | CC-BY-4.0 |

## Abstract

This proposal outlines an Aberdeen Group engagement to produce a white paper analyzing Computer Associates' market position and interBiz initiative—a suite of managed business process solutions built on the bizWorks infrastructure announced at CA World 99. Aberdeen proposes conducting executive interviews, delivering strategic analysis of CA's products, technologies, and competitive positioning in the application infrastructure space, and packaging findings as an Aberdeen Profile for broad use in CA's sales, marketing, and investor relations activities.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 2 |
| observations.csv | 12 |
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

Peter S. Kastner (1999). Proposal for CA interBiz White Paper (July 1999).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

proposal-development, market-positioning, executive-interviews
