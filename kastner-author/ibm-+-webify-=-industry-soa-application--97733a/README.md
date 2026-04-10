# IBM + Webify = Industry SOA Application Jumpstart

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2006-08-03 |
| Type | market-study |
| Domain | Enterprise Software / SOA |
| License | CC-BY-4.0 |

## Abstract

Analysis of IBM's acquisition of Webify Solutions and its strategic implications for the nascent SOA application development market. Argues that 'SOA Lite' general-purpose approaches are insufficient for enterprise needs and that IBM with Webify's industry-specific component library is positioned uniquely to provide Enterprise SOA with vertical market focus in insurance, healthcare, banking, and telecoms.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 12 |
| observations.csv | 16 |
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

Peter S. Kastner (2006). IBM + Webify = Industry SOA Application Jumpstart.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Expert analysis; references Aberdeen survey (ESB and SOA Middleware study with Global 5000 survey)
