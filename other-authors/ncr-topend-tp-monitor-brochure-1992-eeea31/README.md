# NCR TopEND Transaction Processing Monitor Brochure (1992)

| Field | Value |
|-------|-------|
| Author | NCR Corporation (vendor product brochure) |
| Date | 1992 |
| Type | vendor-product-brochure |
| Domain | open-tp-monitor/distributed-transaction-processing |
| License | CC-BY-4.0 |

## Abstract

NCR Corporation 1992 product brochure for TopEND, the NCR open transaction-processing monitor for distributed Open OLTP environments. TopEND is positioned as supporting full ACID semantics (Atomicity, Consistency, Isolation, Durability) and as compliant with the major open-systems standards stacks of the era — X/Open DTP (XA), POSIX, OSI communications, and OSF DCE. The brochure also emphasizes CICS interoperability as a migration bridge for enterprises moving from IBM mainframe TP to Unix-based distributed Open OLTP. TopEND is the implicit TP monitor referenced in Aberdeen's Open OLTP for Enterprise Managers white paper (Korean translation, study 3fc536) and in the 1992-09 NCR Norge AS Open OLTP/RDBMS mini-seminar (study 7f5414, where TopEND is named in lecture topics).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 7 |
| observations.csv | 6 |
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

NCR Corporation (vendor product brochure) (1992). NCR TopEND Transaction Processing Monitor Brochure (1992).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-product-collateral
