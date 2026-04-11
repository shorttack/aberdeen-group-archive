# Electronic Commerce: Virtual Corporations Selling to a Virtual Marketplace

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner; Christopher Stevens |
| Date | 1996 |
| Type | white-paper |
| Domain | Electronic Commerce; Internet Business; Supply Chain |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group white paper summarizing field research on electronic commerce. Identifies three types of EC (B2B, B2C, C2C), outlines key Internet EC technologies, and recommends that IT organizations architect their EC endeavors carefully, considering make-vs-buy decisions. Projects over $7.2 billion in EC IT investment over three years.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 10 |
| observations.csv | 18 |
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

Peter S. Kastner; Christopher Stevens (1996). Electronic Commerce: Virtual Corporations Selling to a Virtual Marketplace.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Field research; expert analysis; best-practice synthesis
