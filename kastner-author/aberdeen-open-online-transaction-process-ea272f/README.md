# Open Online Transaction Processing: An Enterprise Manager's Guide

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Aberdeen Group), funded by NCR Corporation |
| Date | 1991 |
| Type | vendor-funded-aberdeen-paper-fragment |
| Domain | open-OLTP/UNIX/transaction-processing |
| License | CC-BY-4.0 |

## Abstract

Title page and references list of an Aberdeen Group paper authored by Peter S. Kastner and funded by NCR Corporation: 'Open Online Transaction Processing: An Enterprise Manager's Guide'. The body of the report is not present in this fragment. Reference list documents the open-OLTP-on-UNIX corpus that Kastner drew upon: Andrade/Carges/Kovach UniForum papers (1989/1992), Dwyer (1991), Hesselgrave (1990), two prior Aberdeen Kastner papers (Casale Feb 1992 commercial client/server, Logan Aug 1990 Online TP Hardware Suppliers), the Willmott microprocessor MP paper (Aug 1991), Oracle and USL TP/RDBMS documents, NCR TOP END product overview, Transarc Encina overview, and TUXEDO ETP System reference manual (USL). Filed under 1991 per filename convention; references include 1992 papers, suggesting actual publication 1992.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 18 |
| technologies.csv | 7 |
| observations.csv | 11 |
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

Peter S. Kastner (Aberdeen Group), funded by NCR Corporation (1991). Open Online Transaction Processing: An Enterprise Manager's Guide.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

title-page-and-sources-only-fragment
