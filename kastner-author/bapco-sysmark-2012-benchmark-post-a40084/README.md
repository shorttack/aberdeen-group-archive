# BAPco SYSmark 2012: Why AMD Dropped Out and What the Benchmark Actually Measures

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2011-08-01 |
| Type | white-paper |
| Domain | commercial-benchmarks |
| License | CC-BY-4.0 |

## Abstract

Kastner blog post defending BAPco's SYSmark 2012 benchmark against AMD's June 2011 withdrawal from the consortium. Reports Kastner's own test results on the AMD Fusion A8-3850 APU ('Llano', scored 91) versus Intel Sandy Bridge Pentium 840 (98), Core i3-2120 (127), and Core i5-2500 (166). Argues the benchmark reflects 20 years of real-workload modeling across six scenarios (Office, Media, Web, Data/Financial, 3D, System Management) and rejects AMD's framing. The post is a commercial-benchmarks topic deep-dive from Kastner's post-Aberdeen independent-analyst era.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 14 |
| observations.csv | 14 |
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

Peter S. Kastner (2011). BAPco SYSmark 2012: Why AMD Dropped Out and What the Benchmark Actually Measures.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmarking, competitive-profiling, expert-opinion
