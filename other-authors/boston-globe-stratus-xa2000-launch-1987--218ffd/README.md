# Boston Globe — 'Stratus' new computer line aimed at rival Digital' (XA2000 launch, Ronald Rosenberg, 1987-02-02)

| Field | Value |
|-------|-------|
| Author | Ronald Rosenberg (Boston Globe Staff) |
| Date | 1987-02-02 |
| Type | newspaper-trade-coverage |
| Domain | fault-tolerant-systems-launch |
| License | CC-BY-4.0 |

## Abstract

Same-day Boston Globe coverage of Stratus's XA2000 launch announcement. Foster (Stratus president and co-founder, Marlborough MA) quoted on the new line: 'We have tripled the high end of our computer performance and reduced the cost per transaction by half.' Stratus's most powerful new model handles 50 tps vs Tandem's 40 tps and ~15 tps for the VAX 8650. Pricing $261,000-$1M. Stratus relies on redundant hardware (dual CPU, dual memory, dual disks) where Tandem achieves similar fault tolerance largely through software. Foster cites Digital as 'becoming more of a factor and over time we expect them to be our biggest competitor.' IBM OEM relationship: 14.5% of Stratus FY revenue ($124M total). New line available in 90 days; IBM will also market.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 4 |
| observations.csv | 8 |
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

Ronald Rosenberg (Boston Globe Staff) (1987). Boston Globe — 'Stratus' new computer line aimed at rival Digital' (XA2000 launch, Ronald Rosenberg, 1987-02-02).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Boston Globe daily-newspaper coverage of the same XA2000 launch covered in the Computerworld piece in Batch 25 (Connolly, 1987-02). Foster quoted; PSK NOT named in this piece (XA2000 launch coverage that doesn't quote PSK); IBM OEM context.
