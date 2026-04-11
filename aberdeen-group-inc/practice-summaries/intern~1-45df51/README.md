# Internet Infrastructures: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | internet-infrastructure |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group's 1998 analysis of the Internet Infrastructure market, defining the four-component architecture (Application Development Environment, Application Runtime Environment, Service Middleware, and ISP Services) and introducing the 'Internet Object Computing' (IOC) framework. The report assesses the Java vs. Microsoft COM+/DNA battle, the role of CORBA and LDAP, the maturity of EJB and distributed computing standards, and provides competitive profiles of eight major vendors: Borland/Inprise, HP, IBM, Microsoft, Netscape, Novell, Oracle, and Sybase.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 18 |
| observations.csv | 25 |
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

Aberdeen Group (1998). Internet Infrastructures: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
