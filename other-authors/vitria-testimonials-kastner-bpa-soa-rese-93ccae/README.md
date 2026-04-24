# Vitria Testimonials — Aberdeen on BPA / SOA Stack

| Field | Value |
|-------|-------|
| Author | Vitria Technology, Inc. |
| Date | 2007-01-01 |
| Type | vendor-marketing-page |
| Domain | BPA-SOA-EAI-vendor-testimonials |
| License | CC-BY-4.0 |

## Abstract

Vitria Technology testimonials page (archived 2009) features Peter S. Kastner, Vice President of Enterprise Integration Research at AberdeenGroup, endorsing Vitria's Business Process Automation (BPA) vision. Kastner cites Aberdeen primary research showing buyers prefer SOA stacks for integration. Date estimated as 2007 from Kastner's Aberdeen title and Vitria's BPA product framing [REVIEW].

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 10 |
| technologies.csv | 5 |
| observations.csv | 5 |
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

Vitria Technology, Inc. (2007). Vitria Testimonials — Aberdeen on BPA / SOA Stack.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

vendor-curated-quote-collection
