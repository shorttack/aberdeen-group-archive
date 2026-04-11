# RDBMS Market Overview — Computer Associates Sales Training

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1997-11-12 |
| Type | market-study |
| Domain | RDBMS-competitive-analysis |
| License | CC-BY-4.0 |

## Abstract

A 31-slide competitive intelligence training deck prepared by Aberdeen Group analyst Peter S. Kastner for Computer Associates' sales force. Covers 1997–1998 RDBMS strategies and competitive positioning for IBM DB2, Informix, Oracle, Sybase, Microsoft SQL Server, and CA-Ingres. Includes Aberdeen Group's vendor rating framework across scalability, distributed technology, open technology, development tools, and supplier solutions. Contains dedicated weakness assessments for each vendor, hardware platform revenue share data, and strategic guidance for selling CA-Ingres against incumbent rivals.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 13 |
| technologies.csv | 30 |
| observations.csv | 72 |
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

Peter S. Kastner (1997). RDBMS Market Overview — Computer Associates Sales Training.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, benchmarking, industry-analysis, expert-opinion
