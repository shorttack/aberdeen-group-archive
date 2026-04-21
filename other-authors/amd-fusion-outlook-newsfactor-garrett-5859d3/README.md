# The Outlook on AMD's Fusion Plans

| Field | Value |
|-------|-------|
| Author | David Garrett, NewsFactor |
| Date | 2006-10-27 |
| Type | news-article |
| Domain | cpu-gpu-integration |
| License | CC-BY-4.0 |

## Abstract

NewsFactor article (Oct 27 2006, David Garrett) on AMD's Fusion program announced the week AMD closed its $5.4B ATI acquisition. Fusion would combine AMD CPUs with ATI GPUs in a single unified processor, targeted for late 2007 / early 2008. Peter Kastner, VP and research director for information technology at Aberdeen Group, frames Fusion as enabling 'a one-chip computer that contains the functions that in the past have been in the chipset and the processor,' allowing 'a much less expensive PC to be made, because you'd have fewer chips to put on the motherboard.' Kastner caveats: 'I don't see this as moving to $200 PCs.' Samir Bhavnani of Current Analysis emphasizes the power-efficiency angle and Windows Vista Aero implications. Ad-sidebar date stamps indicate this 2006 article was captured in June 2009 during the CloudAve/Palm Pre era.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 4 |
| observations.csv | 7 |
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

David Garrett, NewsFactor (2006). The Outlook on AMD's Fusion Plans.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-analysis, analyst-commentary
