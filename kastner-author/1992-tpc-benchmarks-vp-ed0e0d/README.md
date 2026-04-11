# Better Performance and Lower Prices Through TPC Benchmarks

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1992-03 |
| Type | white-paper |
| Domain | transaction processing benchmarks |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Technology Viewpoint examining TPC benchmarks (TPC-A, TPC-B, TPC-C) as the de facto standard for measuring commercial performance and price-performance. Covers the history of Debit/Credit benchmarking, TPC formation in 1988, and detailed vendor comparisons across DEC VAX, HP, IBM AS/400, Sequent, Bull, Sun, and others. Concludes that TPC-A competition has driven a five-fold improvement in price-performance over two years and advocates that buyers mandate TPC-A results in RFPs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 9 |
| observations.csv | 32 |
| codes.csv | 31 |

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

Peter S. Kastner / Aberdeen Group (1992). Better Performance and Lower Prices Through TPC Benchmarks.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

market analysis; benchmark review; vendor comparison
