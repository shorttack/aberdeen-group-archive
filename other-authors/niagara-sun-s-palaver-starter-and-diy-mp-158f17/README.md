# Niagara: Sun's Palaver Starter? (IT Blogwatch)

| Field | Value |
|-------|-------|
| Author | Richi Jennings (IT Blogwatch, Computerworld Blogs) |
| Date | 2005-11-15 |
| Type | news-article |
| Domain | server-processors |
| License | CC-BY-4.0 |

## Abstract

Computerworld IT Blogwatch aggregation (2005-11-15) curating reactions to Sun Microsystems' UltraSPARC T1 'Niagara' launch — an 8-core, 8-thread-per-core chip promising 70-watt power envelopes for servers. Peter S. Kastner (quoted from a reader comment) recalls being briefed on the Niagara roadmap circa 2000, argues Sun's poor delivery record in SPARC has hurt badly, and would have been market-turning in mid-2002 — though Niagara is a big help to Sun's SPARC base, he doubts it will shake the market's penchant for x64 AMD Opteron servers.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 5 |
| observations.csv | 8 |
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

Richi Jennings (IT Blogwatch, Computerworld Blogs) (2005). Niagara: Sun's Palaver Starter? (IT Blogwatch).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, blog-roundup
