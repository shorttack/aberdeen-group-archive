# Enterprise Integration Technology: Aberdeen Group's Market Trends & Research for 2006

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, Aberdeen Group |
| Date | 2006-02-22 |
| Type | employer-record |
| Domain | Enterprise IT Integration / SOA / Research Agenda |
| License | CC-BY-4.0 |

## Abstract

24-slide Aberdeen Group webinar presentation deck (SOA_AON_webinar_022206a). Covers enterprise integration market challenges/opportunities, 2005 SOA benchmark findings, and Aberdeen's full 2006 Enterprise Integration Research Agenda (Q1-Q4). Key 2005 findings: 92% of companies at or below 25% SOA adoption; over half predict 50%+ SOA-based software in 5 years. Best-in-Class SOA adopters spend 29.6% of IT budget on innovation vs. 18.5% average; software maintenance costs 12.4% vs. 27.3% average. Research agenda spans NAP, SOA app development, edge computing, data center integration, real-time BI, and knowledge worker productivity.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 13 |
| observations.csv | 28 |
| codes.csv | 32 |

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

Peter S. Kastner, Aberdeen Group (2006). Enterprise Integration Technology: Aberdeen Group's Market Trends & Research for 2006.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Benchmark survey + qualitative interviews; Aberdeen research membership pool 137,000+ members
