# A Measure of Transaction Processing Power (Tandem Technical Report 85.2)

| Field | Value |
|-------|-------|
| Author | Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers) |
| Date | 1985-02-01 |
| Type | benchmark |
| Domain | transaction-processing-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Tandem Technical Report 85.2 (February 1985) by 'Anon et al' — the foundational transaction-processing benchmark paper that defined Sort, Scan, and DebitCredit (ET-1/TP-1) and introduced the Transactions Per Second (TPS) and 5-year capital-cost price/performance metrics. A condensed version appeared in Datamation April 1, 1985. The 'Anon et al' byline concealed a collaboration led by Jim Gray (then at Tandem) with ~24 academics, vendors, and users. This paper is the direct ancestor of the Transaction Processing Performance Council (TPC) benchmarks (TPC-A, TPC-B, TPC-C) and is foundational to Kastner's subsequent career as an OLTP/benchmarks analyst at Stratus and Aberdeen Group.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 7 |
| observations.csv | 11 |
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

Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers) (1985). A Measure of Transaction Processing Power (Tandem Technical Report 85.2).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-specification, industry-consensus
