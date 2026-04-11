# Who Cares If The Computer Breaks?

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1995-10-01 |
| Type | white-paper |
| Domain | fault-tolerance, high-availability |
| License | CC-BY-4.0 |

## Abstract

A presentation delivered at the MIT Forum in October 1995 examining why computer failures are increasingly catastrophic as society's dependence on computing grows. Kastner surveys the causes of hardware, software, and network failure, then presents a spectrum of high-availability and fault-tolerance strategies ranging from RAID to fully redundant failover architectures. The talk concludes that future availability gains will depend on system software enabling application failover without prohibitive development costs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 5 |
| technologies.csv | 7 |
| observations.csv | 24 |
| codes.csv | 27 |

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

Peter S. Kastner (1995). Who Cares If The Computer Breaks?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
