# IBM RS/6000 Database Marketing Training Engagement (Aberdeen Group, June 1995)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1995-06-28 |
| Type | training-material |
| Domain | RDBMS-market-analysis, server-platform-strategy, sales-training |
| License | CC-BY-4.0 |

## Abstract

This letter confirms Aberdeen Group's engagement to develop and present a four-hour database marketing training module for IBM's RS/6000 Division, covering the business drivers for distributed database servers, database-hardware platform selection criteria, the RS/6000's strengths against Sun, HP, AT&T, and DEC, and detailed competitive positioning of the five major relational databases (DB2/6000, CA-Ingres, Informix, Oracle, and Sybase) available on the RS/6000 platform. The module is designed to sharpen the marketing knowledge of IBM's RS/6000 marketing specialists and Business Partners for customer-facing database sales engagements.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 10 |
| observations.csv | 12 |
| codes.csv | 28 |

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

Peter S. Kastner / Aberdeen Group (1995). IBM RS/6000 Database Marketing Training Engagement (Aberdeen Group, June 1995).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

curriculum-design, competitive-analysis, market-research
