# Boston Globe — Wang Labs Q1 turnaround (Jeffrey Krasner; PSK Aberdeen Group quoted, 1990-10)

| Field | Value |
|-------|-------|
| Author | Jeffrey Krasner (Boston Globe Staff) |
| Date | 1990-10 |
| Type | newspaper-business-coverage |
| Domain | office-computing-turnaround |
| License | CC-BY-4.0 |

## Abstract

Wang Q1 earnings: 2 cents/share ($2.6M) vs prior-year loss of $62.1M (38 cents/share); first profitable quarter since 1988. Wang Class B stock +25 cents to $3.25 (+8%); bonds +$32.50 per $1,000 face (+8% to $462.50). Bank debt eliminated (down from $575M August 1989). PSK quote: 'They made real money. Wang should be applauded for coming back from its position in the grave a year ago and reporting some real honest-to-goodness taxable profits. Miller has lived up to his advance billing.' Customer-side endorsement from Matt Gillman of Blue Cross Blue Shield Chicago. Counter-balance from Byron Walker (Moody's Investors Service): 'This is an accomplishment, but the important question is if it can be sustained.' Wang ultimately filed for bankruptcy August 1992 — Walker's caution proved correct.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 0 |
| observations.csv | 7 |
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

Jeffrey Krasner (Boston Globe Staff) (1990). Boston Globe — Wang Labs Q1 turnaround (Jeffrey Krasner; PSK Aberdeen Group quoted, 1990-10).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Boston Globe coverage of Wang Laboratories' Q1 FY (ended Sept. 30) earnings — first profit in six quarters under Chairman Richard Miller. PSK quoted as analyst at The Aberdeen Group (Boston market-research firm) endorsing the turnaround as 'real money.'
