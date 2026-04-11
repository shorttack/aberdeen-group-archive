# Uses and Abuses of the Corporate Hockey Stick — Or Is This Any Way to Run an Industry?

| Field | Value |
|-------|-------|
| Author | Charles T. Casale |
| Date | 1983-01-05 |
| Type | market-study |
| Domain | tech-equity-analysis |
| License | CC-BY-4.0 |

## Abstract

Executive Viewpoint #3 introduces the 'hockey stick' concept — the skewed end-of-period concentration of bookings, billings, and shipments common to fast-growing technology companies. Casale argues that the quarterly hockey stick is structurally superior to the annual cycle for managing high-tech operations and examines two management approaches (sales force management via 'stick' and factory management via 'carrot') for moderating the pattern. The newsletter analyzes how Datapoint's booking-oriented compensation plan and Tandem's booking-to-revenue disconnect exemplify the pathological form of the hockey stick.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 0 |
| observations.csv | 18 |
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

Charles T. Casale (1983). Uses and Abuses of the Corporate Hockey Stick — Or Is This Any Way to Run an Industry?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
