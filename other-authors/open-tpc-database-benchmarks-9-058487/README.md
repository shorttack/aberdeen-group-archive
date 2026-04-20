# Open: TPC Database Benchmarks — Truth and Benchmarks

| Field | Value |
|-------|-------|
| Author | Nancy Cohen (Open Magazine) |
| Date | 2005-03-14 |
| Type | news-article |
| Domain | commercial-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Open Magazine feature (2005-03-14) on the Transaction Processing Performance Council (TPC) and why commercial buyers trust its database benchmarks. Peter Kastner is identified unusually as 'analyst for Vericours' rather than Aberdeen. Kastner credits TPC as an independence lever that has kept vendors on their toes, describes the 'lies, damned lies, and benchmarks' legacy before TPC's 1988 founding, and attributes 100-fold application-performance improvements to TPC-induced competition. He calls TPC benchmarks 'the gold standard of commercial benchmarks.'

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 5 |
| observations.csv | 10 |
| codes.csv | 26 |

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

Nancy Cohen (Open Magazine) (2005). Open: TPC Database Benchmarks — Truth and Benchmarks.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
