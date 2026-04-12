# Maxtor Midline Storage Interactive Demo (Adobe Flash)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group / Maxtor Corporation |
| Date | 2003-01-01 |
| Type | interactive-demo |
| Domain | enterprise-storage |
| License | CC-BY-4.0 |

## Abstract

An interactive Adobe Flash (Macromedia Flash 6) demonstration tool created by Aberdeen Group for Maxtor Corporation circa 2003 as a companion to the Mid-Line Disk Storage white paper. The SWF binary visualizes the enterprise storage hierarchy and positions Maxtor's Serial ATA midline drives between high-end Fibre Channel storage and offline tape. Designed as an innovative sales enablement and analyst-led content marketing tool for use by Maxtor's marketing team and in press/analyst interactions.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 7 |
| observations.csv | 12 |
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

Aberdeen Group / Maxtor Corporation (2003). Maxtor Midline Storage Interactive Demo (Adobe Flash).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

interactive-content, sales-enablement, data-visualization
