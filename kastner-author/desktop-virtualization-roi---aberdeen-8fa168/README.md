# Measuring the Returns from a Desktop Virtualization Program

| Field | Value |
|-------|-------|
| Author | Dick Csaplar |
| Date | 2011-09 |
| Type | benchmark |
| Domain | Desktop Virtualization / Enterprise IT |
| License | CC-BY-4.0 |

## Abstract

Aberdeen survey of 76 organizations on desktop virtualization deployment outcomes (May 2011). Reports seven operational performance metrics comparing virtualized vs. non-virtualized desktops. Key findings: 20.4% reduction in routine maintenance time, 11.7% cost reduction, 2.9 vs. 6.8 downtime incidents per year, 1.0 vs. 4.3 hour recovery time, 0.9 vs. 2.3 hours data lost per incident. Argues ROI is primarily operational rather than financial. Covers deployment adoption rates by company size, best practices (user role standardization, IT training, executive visibility), and technology enablers (thin/zero clients, BYOD).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 9 |
| observations.csv | 28 |
| codes.csv | 28 |

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

Dick Csaplar (2011). Measuring the Returns from a Desktop Virtualization Program.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Primary survey research; 76 organizations surveyed in May 2011; comparative analysis between companies with and without desktop virtualization programs; seven desktop performance metrics analyzed
