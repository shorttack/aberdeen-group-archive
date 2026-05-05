# Kastner Technology Breadth Memoir: Forty-Seven Years Across the Computing Stack

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 2026-05-05 |
| Type | memoir |
| Domain | memoir/career-arc |
| License | CC-BY-4.0 |

## Abstract

First-person memoir by Peter S. Kastner quantifying the technology breadth of his 47-year career as analyst, marketer, and expert witness. Drawing on the Kastner-authored + Kastner-quoted corpus (592 of the archive's 915 studies), the memoir documents 2,537 distinct technologies across 4,628 mentions and 479 subject domains, organized into 14 thematic rollups from Personal Computers & OS through AI/Analytics & Emerging. A concluding section ('How and Why Did I Do This?') traces the five-rung curriculum (paper slips, operations, programming, marketing, market research) that produced the breadth, and credits a working trade-press partnership with Bill Bulkeley (Wall Street Journal) and Hiawatha Bray (Boston Globe), Aberdeen print runs of up to 100,000 copies, and 500+ documented personal press quotes for amplifying the work to millions of readers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 17 |
| technologies.csv | 15 |
| observations.csv | 74 |
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

Peter S. Kastner (2026). Kastner Technology Breadth Memoir: Forty-Seven Years Across the Computing Stack.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

oral-history, archive-quantification
