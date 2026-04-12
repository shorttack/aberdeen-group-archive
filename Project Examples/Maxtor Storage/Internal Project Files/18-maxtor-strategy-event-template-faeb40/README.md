# Maxtor ILM Pools of Storage Strategy Event Data Collection Template

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2003-01-01 |
| Type | employer-record |
| Domain | storage-strategy / interactive-tool |
| License | CC-BY-4.0 |

## Abstract

A template specification extracted from the Hardware Hawker (HH) ILM/Pools of Storage interactive sales tool, defining the data input fields and scenario structure for Strategy Events. Each Strategy Event models a customer's data environment across structured, semi-structured, and unstructured data; storage tiers (online disk, nearline tape, offline tape, midline disk, nearline disk); cost-per-GB parameters; and workflow flow directions. The template supports iterative scenario modeling with duplicate slides for sequential steps, quantifying bottom-line benefits from storage tier migration including downtime savings, admin management savings, opportunity cost savings, and revenue operations improvements.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 2 |
| technologies.csv | 8 |
| observations.csv | 16 |
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

Aberdeen Group (2003). Maxtor ILM Pools of Storage Strategy Event Data Collection Template.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review
