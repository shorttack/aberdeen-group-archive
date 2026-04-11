# Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)

| Field | Value |
|-------|-------|
| Author | Digital Equipment Corporation |
| Date | 1991-01-01 |
| Type | employer-record |
| Domain | transaction-processing |
| License | CC-BY-4.0 |

## Abstract

This issue of the Digital Technical Journal presents eight peer-reviewed technical papers documenting DEC's complete distributed transaction processing stack, including the DECdta architecture, ACMS and DECintact TP monitors, DECdtm kernel-level transaction management, TPC Benchmark A performance results, database availability strategies, optimized commit protocols, and VAXft 3000 fault-tolerant system verification. The papers collectively define DEC's strategy to lead the distributed TP market through an integrated, standards-aligned, client/server architecture. Formal TPC Benchmark A results are disclosed: 69.4 tpsA-Local on VAX 9000 Model 210 and 21.6 tpsA-Local on VAX 4000 Model 300.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 36 |
| technologies.csv | 28 |
| observations.csv | 40 |
| codes.csv | 35 |

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

Digital Equipment Corporation (1991). Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, industry-analysis
