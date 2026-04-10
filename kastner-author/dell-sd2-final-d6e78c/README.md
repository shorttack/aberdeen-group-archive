# Asset Recovery Services Field Guide: A New Way to Strengthen Relationships and Increase Sales

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2003-2004 |
| Type | white-paper |
| Domain | IT asset recovery / sales enablement / e-waste / IT lifecycle management |
| License | CC-BY-4.0 |

## Abstract

Dell internal confidential field guide for sales representatives selling Asset Recovery Services (ARS). Covers mission overview (80% of customers store unwanted hardware), two disposition services (Value Recovery at $59-$69/unit and Recycling at $49-$59/unit), flexible logistics options, detailed reporting requirements, FAQ with researched objection responses, and SKU/legend code chart for order entry. Positions ARS as a customer relationship tool that also generates revenue and margin credit for sales.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 4 |
| observations.csv | 15 |
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

Peter S. Kastner (2003). Asset Recovery Services Field Guide: A New Way to Strengthen Relationships and Increase Sales.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Internal sales enablement document; customer objection handling and SKU reference guide
