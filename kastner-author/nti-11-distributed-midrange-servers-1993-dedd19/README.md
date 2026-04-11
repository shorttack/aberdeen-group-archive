# Building Distributed Systems with Midrange Servers

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner, John Logan, Thomas Willmott |
| Date | 1993-08-01 |
| Type | market-study |
| Domain | distributed-computing-midrange |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group presents a comprehensive guide for IS executives on building enterprise distributed systems using midrange servers, covering enterprise requirements, server characteristics, operating systems, and distributed architectures. The study advocates the three-tier-plus topology and demonstrates how midrange servers surpass mainframes in I/O bandwidth, processor performance, and cost, delivering 50% IS cost reductions on average. Aberdeen profiles leading hardware suppliers (HP, NCR, Unisys, Compaq, DEC) and RDBMS vendors (Oracle, Sybase, Informix, Ingres, Software AG) as the foundation for distributed production systems.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 22 |
| technologies.csv | 20 |
| observations.csv | 30 |
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

Peter S. Kastner, John Logan, Thomas Willmott (1993). Building Distributed Systems with Midrange Servers.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, technology-assessment, vendor-profiling
