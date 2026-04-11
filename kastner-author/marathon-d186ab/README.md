# How I'd Succeed as a Marathon Sales Exec

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner |
| Date | 1998-04-29 |
| Type | market-study |
| Domain | fault-tolerant-computing |
| License | CC-BY-4.0 |

## Abstract

A 14-slide sales strategy presentation delivered by Aberdeen Group Chief Research Officer Peter S. Kastner to Marathon Technologies in April 1998. The deck argues that the NT high-availability market is ripe for Marathon's Endurance product, that named competitors (Stratus, Tandem/Compaq, Microsoft Cluster Server) are weak or misaligned, and that the real obstacle is customer inertia. It prescribes a go-to-market plan based on FUD around downtime costs, alliance-building with Microsoft field sales and Big Six systems integrators, and vertical market focus across retail, healthcare, public safety, utilities, financial services, and ISPs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 8 |
| technologies.csv | 13 |
| observations.csv | 25 |
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

Peter S. Kastner (1998). How I'd Succeed as a Marathon Sales Exec.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-profiling, expert-opinion, strategic-recommendation
