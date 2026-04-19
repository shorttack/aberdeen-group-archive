# Top iSeries ISVs — IBM Business Partner Directory Appendix

| Field | Value |
|-------|-------|
| Author | Peter Kastner (compiler) |
| Date | 2002-04-20 |
| Type | market-study |
| Domain | isv-partner-analysis |
| License | CC-BY-4.0 |

## Abstract

Appendix B from the Sun AS/400 RAMP engagement: a directory of top-tier IBM iSeries ISV partners, their classification (Developer Business Partner vs Premier Level vs Advanced Level), locations (US, Canada, UK, Malaysia), and their flagship iSeries-compatible solutions. Named partners include Alltel Information Services (Horizon Banking), DWL Incorporated (DWL Customer/Unifi), e-Business Exchange Pte, E3 Corporation (E3 Marketplace, E3CRISP), EFA Software Services (Equator), Geac Enterprise Solutions (System21), and Hyperion Solutions. Used to shortlist Sun's counter-partner targets.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 6 |
| observations.csv | 19 |
| codes.csv | 26 |

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

Peter Kastner (compiler) (2002). Top iSeries ISVs — IBM Business Partner Directory Appendix.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, partner-analysis
