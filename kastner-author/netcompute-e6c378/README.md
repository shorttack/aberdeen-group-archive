# NC Server White Paper -- DRAFT

| Field | Value |
|-------|-------|
| Author | Network Computer, Inc. (NCI) / Aberdeen Group |
| Date | 1997-01-01 |
| Type | white-paper |
| Domain | network-computing |
| License | CC-BY-4.0 |

## Abstract

This draft white paper describes the NC Server from Network Computer, Inc. (NCI), a platform enabling network computing via a three-tier architecture of OS substrate, required system services, and NC applications. The document details NC components including initialization (BOOTP/DHCP), authentication (smart card), file system (NFS), print services, and applications (Oracle-based productivity tools, web server, mail, billing). The NC Server is positioned as a low-cost, centrally managed alternative to desktop PCs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 17 |
| observations.csv | 20 |
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

Network Computer, Inc. (NCI) / Aberdeen Group (1997). NC Server White Paper -- DRAFT.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-specification, industry-analysis
