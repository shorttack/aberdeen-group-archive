# Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Aberdeen Group) |
| Date | 1992-02-01 |
| Type | market-study |
| Domain | transaction-processing-benchmarks-distributed-computing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group slide deck from February 1992 (dated '2/92' in footer) presenting TPC-A and TPC-B benchmark results and introducing Aberdeen's DOPS (Distributed Online Processing Systems) framework. Highlights an 85% price decline for equivalent transaction-processing capacity from the DEC VAX 8830 (1988 best-performance, $1,800K 5-year cost for 27 tps) to the VAX 3100-80 (1992 entry-level, $280K). Compares TPC-A at 40 tps-A across Bull DPX/2, DEC VAX 4000-300, HP 9000 957LX, IBM AS/400 D70, and IBM RS/6000 530H (costs $450K-$920K). TPC-B results at 39.7-46 tps-B across Compaq 486/50L, DECsystem 5500, HP 9000 807S, Data General AViiON 4600, MIPS 3330, RS/6000 320H, and Sun SPARC Server 2 (cluster ~$100K). Introduces the DOPS environment (multiple databases, networks, hetero-geneous hardware, mixed OLTP/OLDS) with performance issues including 'Production/Snapshot/Test/Runamuck' database categories.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 12 |
| observations.csv | 17 |
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

Peter S. Kastner (Aberdeen Group) (1992). Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

benchmark-analysis, market-tracking, competitive-profiling
