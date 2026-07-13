# Surfing the Parallel Architectures

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1994-09-27 |
| Type | market-study |
| Domain | parallel-computing |
| License | CC-BY-4.0 |

## Abstract

This board-level presentation surveys the 1994 commercial parallel-computing market across uniprocessors, SMP systems, clusters, and massively parallel machines, then compares the leading hardware and database suppliers against Tandem's position. Kastner argues that software-enabled clustering and parallel databases will matter more than pure MPP experimentation, and he frames data warehousing plus distributed object computing as Tandem's best near-term strategic opening. The deck combines architecture taxonomy, vendor-by-vendor competitive critique, and explicit forward-looking judgments about how the market would evolve.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 27 |
| technologies.csv | 25 |
| observations.csv | 49 |
| codes.csv | 24 |

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

Peter S. Kastner (1994). Surfing the Parallel Architectures.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, competitive-profiling, expert-opinion
