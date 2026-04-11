# Aberdeen's Competitive Landscape — CP 100 Builds

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 2000 |
| Type | employer-record |
| Domain | IT market research; competitive landscape visualization; analyst firm positioning |
| License | CC-BY-4.0 |

## Abstract

Seven-slide Aberdeen Group presentation consisting entirely of 'Aberdeen's Competitive Landscape' charts (CP 100 Builds format). Each slide appears to be a build step in the same competitive positioning diagram, progressively revealing Aberdeen's competitive landscape. Mostly graphical with minimal extractable text — text content is limited to the slide title repeated seven times. The visual content would show Aberdeen's market position relative to Gartner, IDC, Forrester, Meta Group, and other IT analyst firms.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 1 |
| observations.csv | 4 |
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

Peter S. Kastner / Aberdeen Group (2000). Aberdeen's Competitive Landscape — CP 100 Builds.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

corporate-presentation
