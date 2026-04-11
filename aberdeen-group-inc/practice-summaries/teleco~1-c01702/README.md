# Telecommunications: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-11-01 |
| Type | other-research |
| Domain | telecommunications |
| License | Aberdeen Group's 1998 practice summary covering the full telecommunications landscape: deregulation, CLEC/ILEC dynamics, the shift from TDM to packet (IP/ATM) networks, managed services, telecom hardware/software vendors, and OSS/billing. The document profiles managed-services providers and analyzes the competitive forces reshaping carriers, equipment vendors, and ISPs as voice and data networks begin to converge. Key findings include the $670 billion global telecom market size, the growth of IP services alongside dominance of private-line revenues, and the challenge of providing PSTN-grade reliability on packet networks. |

## Abstract

TELECO~1.DOC

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 30 |
| technologies.csv | 18 |
| observations.csv | 25 |
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

Aberdeen Group (1998). Telecommunications: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis
