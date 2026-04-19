# Adobe Systems Inc. — Aberdeen DCT Company Snapshot

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2002-06-01 |
| Type | dct |
| Domain | dct/company-profile |
| License | CC-BY-4.0 |

## Abstract

Short Aberdeen DCT company-snapshot on Adobe Systems, covering corporate facts (founded 1982, second-largest PC software company, 345 Park Avenue San Jose), product categories (content design/production/publishing; digital video; digital imaging; document rendering including fonts, print rendering, ePaper), and executive roster (Warnock, Geschke as co-chairmen; Chizen CEO; Demo CFO; Lamkin SVP Graphics; Eschbach VP ePaper).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 6 |
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

Peter S. Kastner (2002). Adobe Systems Inc. — Aberdeen DCT Company Snapshot.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
