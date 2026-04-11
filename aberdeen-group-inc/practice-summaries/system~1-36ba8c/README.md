# Systems and Network Management: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | systems-network-management |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 survey of the enterprise systems and network management market, covering network management, systems management, and application management. The report identifies the central market debate as Framework (Computer Associates Unicenter TNG, IBM Tivoli TME) versus Best-of-Breed (HP, BMC, Candle, Platinum) approaches, forecasts 20% annual market growth, and highlights application management as the fastest-growing segment. Supplier profiles cover 10 vendors including BMC Software, Computer Associates, IBM/Tivoli, and HP.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 10 |
| observations.csv | 24 |
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

Aberdeen Group (1998). Systems and Network Management: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
