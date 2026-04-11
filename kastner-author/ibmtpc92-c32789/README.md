# IBM Section: TPC Benchmark Viewpoint (Aberdeen Group, 1992)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1992 |
| Type | market-study |
| Domain | OLTP-benchmarking, mainframe-and-midrange-computing, commercial-price-performance |
| License | CC-BY-4.0 |

## Abstract

This section of Aberdeen's 1992 TPC Benchmark Viewpoint examines IBM's two-pronged TPC benchmark strategy using its AS/400 and RS/6000 midrange lines, documenting strong AS/400 E-series price-performance improvements and a 59% RS/6000 model 550 throughput gain from AIX 3.2, while noting that IBM has conspicuously excluded its System/390 mainframe from TPC disclosures. Aberdeen argues that IBM has almost certainly run TPC benchmarks internally on the System/390 but is withholding results, and encourages IBM customers to demand TPC disclosure across all IBM product lines to enable fair cross-platform comparisons.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 6 |
| observations.csv | 13 |
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

Peter S. Kastner / Aberdeen Group (1992). IBM Section: TPC Benchmark Viewpoint (Aberdeen Group, 1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, competitive-analysis, price-performance-modeling
