# Microsoft Scalability Day: The Emperor Has No Clothes

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner / Aberdeen Group |
| Date | 1997 |
| Type | market-study |
| Domain | Windows NT Enterprise Scalability |
| License | CC-BY-4.0 |

## Abstract

A short Aberdeen Group commentary assessing Microsoft's claims at its Scalability Day event circa 1997. Kastner argues NT remains unsuitable for Fortune 500 enterprise environments and that partner solutions are required to achieve high transaction rates, availability, and fault tolerance. He concludes that Unix, AS/400, and mainframes remain the legitimate province of the enterprise high-end.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 3 |
| technologies.csv | 5 |
| observations.csv | 7 |
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

Peter S. Kastner / Aberdeen Group (1997). Microsoft Scalability Day: The Emperor Has No Clothes.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

expert-opinion, competitive-analysis
