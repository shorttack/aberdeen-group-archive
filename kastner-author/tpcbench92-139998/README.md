# TPC Benchmarks: Users Benefit From Competition (1992 Presentation Notes)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1992 |
| Type | market-study |
| Domain | TPC Benchmark Competition / Transaction Processing Price-Performance |
| License | CC-BY-4.0 |

## Abstract

Outline and notes for a 1992 Aberdeen Group presentation on TPC benchmarks covering TPC-A and TPC-B standards and their role as the primary vehicle for commercial system price/performance competition. Per-supplier analysis covers Digital (VAX), HP, IBM (RS/6000, AS/400, mainframes), Bull, Data General, and Sun, with specific data points including HP's Jan-1990 cost of $36.50/TPS-A falling to DEC's $7.69/TPS-A by March 1992, and Digital VAX 4000-300 improving price-performance by 50% over 18 months.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 14 |
| observations.csv | 21 |
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

Peter S. Kastner / Aberdeen Group (1992). TPC Benchmarks: Users Benefit From Competition (1992 Presentation Notes).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, competitive-analysis, expert-opinion
