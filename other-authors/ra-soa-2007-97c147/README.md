# SOA and Web Services Testing: How Different Can It Be? (Full Unabridged Version)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group (Perry Donham) |
| Date | 2007-08 |
| Type | employer-record |
| Domain | SOA/Web Services Quality Assurance and Testing |
| License | CC-BY-4.0 |

## Abstract

Full 180pp unabridged version of the SOA/Web Services testing benchmark report. Study of 240 end-users involved in software quality. Best-in-Class (BIC) companies show 94% increase in deployed software quality, 61% reduction in defects, 57% faster repair times, 71% increase in code test coverage. Key finding: automation alone is insufficient — BIC companies test horizontally across entire business processes, not just vertically via unit testing. BIC companies 3x more likely to have redesigned their testing process. 45% of BIC use business requirements tracking tools vs 35% for others. File also contains appended Aberdeen reports: Enterprise Information Integration (July 2003), BPM Matching IT to Business Processes (Dec 2006), SOA Middleware Takes the Lead (July 2007), and Modernizing Legacy Applications (June 2007).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 11 |
| observations.csv | 100 |
| codes.csv | 30 |

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

Aberdeen Group (Perry Donham) (2007). SOA and Web Services Testing: How Different Can It Be? (Full Unabridged Version).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Survey-based benchmark (N~240-250); Aberdeen Maturity Class Framework; online survey July-August 2007 supplemented by telephone interviews
