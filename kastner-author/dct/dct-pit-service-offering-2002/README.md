# Personal Information Technology (PIT) Service Offering — Tiered Pricing

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-03-01 |
| Type | dct |
| Domain | DCT,service-offering,pricing |
| License | CC-BY-4.0 |

## Abstract

Internal/sales-facing tiered service offering for Aberdeen's Personal Information Technology practice. Defines target company classes (CE, computer, cable equipment, WiFi-x, HomePNA, retail, ILECs), five core category slides (Gateways, Media Servers/PC-CE convergence, Networks, Displays/UI/Usability, Internet/Cable enablement), and three pricing tiers: $19,500 Basic, $24,500 Basic+Contenders, and $24,500 + $4,000/diem Custom Consulting.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 23 |
| technologies.csv | 7 |
| observations.csv | 13 |
| codes.csv | 23 |

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

Peter S. Kastner (2002). Personal Information Technology (PIT) Service Offering — Tiered Pricing.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review,industry-analysis
