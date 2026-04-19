# Don't Fall for the Siren-Song Price of Under-powered Desktop PCs (Aberdeen Impact)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1998-09-10 |
| Type | white-paper |
| Domain | enterprise-pcs |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group 'Impact' publication (Sept 10, 1998) in which Kastner warns IS executives against the 'siren song' of sub-$1,000 and Celeron-class corporate desktops. Argues that memory pressure from Windows 95/98/NT + Office 97 + Outlook 98 + IE4 + SNMP + anti-virus consumes 60MB virtual memory, making 32MB PCs obsolete. Recommends a 400 MHz Pentium II with 128 MB and a 17-inch monitor at $1,800-2,000 for a 3-year useful life, sized for Office 2000, IE 5, and Windows NT 5.0 (later Windows 2000). Introduces Aberdeen's 'Welded Case' model — buy extra PC power now to avoid labor-intensive upgrades.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 4 |
| technologies.csv | 14 |
| observations.csv | 16 |
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

Peter S. Kastner (1998). Don't Fall for the Siren-Song Price of Under-powered Desktop PCs (Aberdeen Impact).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, expert-opinion, buying-guide
