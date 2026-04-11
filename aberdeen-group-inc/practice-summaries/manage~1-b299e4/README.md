# Managed Carrier Services: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | managed-network-services |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 practice summary covering the managed carrier services market, analyzing how enterprises use telecom outsourcing and virtual private networks to reduce costs and improve network operations. The report profiles nine service providers including Ameritech, Bell Atlantic, IBM Global Services, and Infonet, and provides market sizing estimates projecting the managed services market will reach $36 billion by 2002. It documents enterprise attitudes toward outsourcing, service differentiator trends, and the emerging role of IP-based VPNs and TCP/IP in replacing traditional dedicated-circuit architectures.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 10 |
| observations.csv | 23 |
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

Aberdeen Group (1998). Managed Carrier Services: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
