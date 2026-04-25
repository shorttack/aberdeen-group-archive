# Technology That's As Dynamic As Your Organization (Informix Dynamic Scalable Architecture full-page ad)

| Field | Value |
|-------|-------|
| Author | Informix Software (full-page advertisement, Datamation, 1 March 1994) |
| Date | 1994-03-01 |
| Type | vendor-advertisement |
| Domain | RDBMS/parallel-processing/SMP-MPP |
| License | CC-BY-4.0 |

## Abstract

Informix Software's full-page Datamation ad (1 March 1994) launching Dynamic Scalable Architecture (DSA), pitched as enabling Informix to leapfrog Oracle and Sybase in parallel/SMP/MPP database performance. Quotes IDC's John Morrell, Alternative Technologies' David McGoveran, Mota Group's Rob Tholomoler, Hyatt Hotels VP Gordon Kerr, and Michael Bloomberg of Bloomberg Financial Markets. Offers free Aberdeen Group and IDC reports via 1-800-688-IFMX, cementing Aberdeen's and IDC's positioning as the third-party validation analysts for the 1994 RDBMS-parallel wave. Filed in Kastner archive given the Aberdeen report-fulfillment offer (the underlying Aberdeen Informix DSA report would be Kastner-authored).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 15 |
| technologies.csv | 5 |
| observations.csv | 8 |
| codes.csv | 32 |

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

Informix Software (full-page advertisement, Datamation, 1 March 1994) (1994). Technology That's As Dynamic As Your Organization (Informix Dynamic Scalable Architecture full-page ad).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

advertisement-with-third-party-quotes
