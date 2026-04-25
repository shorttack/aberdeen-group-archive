# Melding Financial Operations and Analytics: The New Financial Battleground

| Field | Value |
|-------|-------|
| Author | Alex Veytsel |
| Date | 2003-06-10 |
| Type | industry-insight |
| Domain | financial-compliance |
| License | CC-BY-4.0 |

## Abstract

Alex Veytsel of Aberdeen Group argues that the Sarbanes-Oxley Act is accelerating convergence between Financial Value Chain Management (FVCM) and financial analytics software, creating a corporate performance management imperative. The insight categorizes three supplier heritage types—financial analytics vendors, FVCM specialists, and ERP companies—evaluating each against SOX compliance needs, with ERP vendors holding a trump card via general ledger control. Aberdeen predicts that innovative FVCM suppliers will either add analytic capability or be displaced, and that SOX-driven transparency will prove beneficial beyond compliance.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 7 |
| observations.csv | 23 |
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

Alex Veytsel (2003). Melding Financial Operations and Analytics: The New Financial Battleground.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion
