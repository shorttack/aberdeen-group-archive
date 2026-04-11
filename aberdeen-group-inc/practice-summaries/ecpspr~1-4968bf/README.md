# Electronic Commerce Professional Services: 1998 Practice Summary

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1998-05-01 |
| Type | other-research |
| Domain | electronic-commerce |
| License | CC-BY-4.0 |

## Abstract

A 1998 practice summary analyzing the market for professional services supporting electronic commerce deployment. The report defines four categories of EC professional services providers (OEMs, SSPs, IPSPs, EDI/VAN integrators), identifies key implementation challenges (skills shortages, integration complexity, standards immaturity), and profiles 11 major service providers including IBM, HP, Digital, Microsoft, Oracle, SAP, Cambridge Technology Partners, EDS, GEIS, Sterling Commerce, and Harbinger. Key Aberdeen finding: enterprises are turning to outside service providers because internal IS resources lack EC skills.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 29 |
| technologies.csv | 14 |
| observations.csv | 30 |
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

Aberdeen Group (1998). Electronic Commerce Professional Services: 1998 Practice Summary.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, market-overview
