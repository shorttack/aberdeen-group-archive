# OLTP Market Research for BBN Advanced Computers

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1989-04-04 |
| Type | consulting-report |
| Domain | OLTP-benchmarking, parallel-computing, commercial-data-processing |
| License | CC-BY-4.0 |

## Abstract

This consulting market letter, commissioned by BBN Advanced Computers, assesses the commercial OLTP market opportunity for BBN's Butterfly GP1000 parallel computer system, sizing the 1988 OLTP market at $24B worldwide and growing at 18% annually. Kastner surveys vertical market segments—banking, insurance, retail, manufacturing, and government—cataloging application transaction volumes and competitive dynamics to identify where the Butterfly's parallel architecture could compete. The letter concludes that several high-volume OLTP verticals represent viable target markets for a next-generation Butterfly product.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 14 |
| technologies.csv | 9 |
| observations.csv | 25 |
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

Peter S. Kastner (1989). OLTP Market Research for BBN Advanced Computers.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market-research, field-interviews, market-sizing, vertical-market-analysis
