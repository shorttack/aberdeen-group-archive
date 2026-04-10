# AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-02 |
| Type | white-paper |
| Domain | Semiconductor / PC Processor Marketing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group critiques AMD's Athlon XP Gigahertz Equivalency (GHz-E) marketing strategy, arguing the model-numbering methodology is fundamentally flawed. GHz-E ratings are a snapshot-in-time metric that becomes misleading as benchmarks, operating systems, and Intel processors evolve. The paper documents benchmark disclosure failures (SYSmark 2001 not filed with Bapco), a Media Player bug fix incorporated post-audit, and I/O-inclusive benchmarks misapplied to processor-only comparison. Aberdeen concludes AMD will be forced to abandon GHz-E in 2002 and recommends investigation of SPECcpu 2000 as an alternative framework via the True Performance Initiative.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 8 |
| observations.csv | 17 |
| codes.csv | 30 |

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

Peter S. Kastner (2002). AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Benchmark analysis, competitive evaluation, literature review of public benchmark results
