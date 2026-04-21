# The Outlook on Intel's Quad-Core Chips

| Field | Value |
|-------|-------|
| Author | David Garrett, NewsFactor |
| Date | 2006-11-15 |
| Type | news-article |
| Domain | cpu-multicore |
| License | CC-BY-4.0 |

## Abstract

NewsFactor article (Nov 15 2006, David Garrett) on Intel's quad-core processor release: the Xeon 5300 server series (up to 50% faster than dual-core Xeon 5100) and the Core 2 Extreme desktop series (up to 80% faster for threaded apps). Peter Kastner, VP and research director for enterprise technology at Aberdeen Group, predicts 'rapid adoption reaching mainstream in Q2 of next year [2007],' driven by aggressive Intel pricing. He flags server virtualization-driven consolidation as the killer app: 'Quad-core becomes really exciting for the many IT organizations that are looking at server consolidation through virtualization.' For consumers, Kastner calls quad-core gaming/multimedia performance 'awesome' and 'your Christmas dream.' The article captures Intel's attempt to regain enterprise momentum lost to AMD Opteron (esp. Dell's 2006 Opteron server capitulation).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 4 |
| observations.csv | 9 |
| codes.csv | 27 |

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

David Garrett, NewsFactor (2006). The Outlook on Intel's Quad-Core Chips.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

product-analysis, analyst-commentary
