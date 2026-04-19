# Project eLiza Positioning and Messaging Workshop Report

| Field | Value |
|-------|-------|
| Author | Joyce Becknell, Gordon Haff, Peter Kastner (Aberdeen Group) |
| Date | 2001-06-01 |
| Type | market-study |
| Domain | autonomic-computing-positioning |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group consulting deliverable to IBM following the May 16, 2001 Somers positioning workshop for Project eLiza — IBM's self-managing, self-healing server architecture initiative. Provides a high-level computing vision and three key messages (Best Practices Automation, Simplification, Lower Cost) mapped to three stakeholder classes (LOB Executive, IT Management & Staff, Internal/External Users). Predicts 'computers managing computers' in five to ten years. Flag: IBM-internal confidentiality.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 7 |
| observations.csv | 35 |
| codes.csv | 24 |

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

Joyce Becknell, Gordon Haff, Peter Kastner (Aberdeen Group) (2001). Project eLiza Positioning and Messaging Workshop Report.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, framework-development, expert-opinion
