# Computerworld: Stratus Readies XA2000 Series to Take on Tandem High-End — Pete Kastner on Floating-Point + Yankee Group's Henkel on VLX/3090 Class (February 1987)

| Field | Value |
|-------|-------|
| Author | James Connolly (Computerworld staff) |
| Date | 1987-02 |
| Type | trade-press-product-launch |
| Domain | fault-tolerant-computing/product-launch |
| License | CC-BY-4.0 |

## Abstract

February 1987 Computerworld product-launch story by James Connolly on the Stratus XA2000 series (Models 100-140), positioned to take on Tandem's 10-month-old NonStop VLX. Both companies claim peak rates over 50 tps. Stratus officials anticipate near-simultaneous announcement of XA2000 inclusion in IBM's System/88 line (IBM resells Stratus-built FT systems as System/88). Stratus CEO William E. Foster: 'We are selling into a market that has an insatiable appetite for transactions per second' and cites the design assumption of 45% annual growth in OLTP over the next five years. Pete S. Kastner — quoted as 'manager of marketing support programs for Stratus' — explains the new Motorola 68881 floating-point coprocessor is intended to help OLTP users perform tasks like financial modeling, NOT to enter scientific/engineering markets. Hardware: 16 MHz Motorola 68020 processors (vs prior 68010), 64 MB memory, 64 KB cache, 128 MB virtual address space, 46 GB disk. Model 140 has four tightly-coupled duplicated CPUs and is rated 15 / 27-29 / 37-40 / 47-53 tps for Models 110/120/130/140 on ET-1; Model 140 is 3x XA600 ET-1 and 2.5x XA600 TP-1. Pricing: $260K-$500K (Model 110) up to $770K-$1.1M (Model 140). Stratus claims tps cost is half that of earlier products. Yankee Group analyst Thomas Henkel: 'This is really the first time they have gotten into the VLX or IBM 3090 class' — but questions IBM's relationship with Stratus and Stratus's app/database software depth in growth areas like manufacturing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 8 |
| observations.csv | 10 |
| codes.csv | 29 |

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

James Connolly (Computerworld staff) (1987). Computerworld: Stratus Readies XA2000 Series to Take on Tandem High-End — Pete Kastner on Floating-Point + Yankee Group's Henkel on VLX/3090 Class (February 1987).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-reporter-with-vendor-and-analyst-quotes
