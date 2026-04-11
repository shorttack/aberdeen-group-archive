# Intel Decision Support Market Research Proposal

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1999-06-16 |
| Type | consulting-report |
| Domain | decision-support, data-warehousing, server-market-analysis |
| License | CC-BY-4.0 |

## Abstract

This Aberdeen Group proposal for Intel's Enterprise Server Group outlines a market research engagement to assess the decision support (DSS/OLAP/data mining) marketplace, specifically investigating where CPU power demand is located—server, workstation, or desktop—and testing IT manager perceptions of Intel as a strategic player in decision support. The proposed methodology combines telephone and face-to-face interviews with senior executives using analytical tools, delivering findings as a market characteristics report, market positioning analysis, and actionable marketing recommendations for Intel.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 7 |
| observations.csv | 14 |
| codes.csv | 23 |

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

Peter S. Kastner / Aberdeen Group (1999). Intel Decision Support Market Research Proposal.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

field-interviews, market-research, customer-surveys, proposal
