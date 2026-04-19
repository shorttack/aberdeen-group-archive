# Aberdeen Group Corporate Background Deck (Outbound Marketing)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 2001-01-01 |
| Type | employer-record |
| Domain | outbound-marketing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group corporate background slide deck (v9-19) used for outbound marketing — client meetings, new-hire orientation, and investor briefings. Three offices (Boston, Palo Alto, Amsterdam), aberdeen.com URL. Four-slide structure: (1) title; (2) Aberdeen's Market Positioning; (3) Aberdeen's Competitive Landscape; (4) business architecture diagram mapping IT Supplier Executives and Private Equity audiences through Services, Practice Areas, Surveys/Field Instruments, Emerging Market Intelligence, Webcasts/Conferences/Seminars, aberdeen.com aggregation, Supplier Meetings, e-Learning, Field Sales, and Marketing Consulting. Primary text extraction is sparse — the deck is diagram-heavy.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 1 |
| technologies.csv | 0 |
| observations.csv | 6 |
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

Aberdeen Group (2001). Aberdeen Group Corporate Background Deck (Outbound Marketing).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, presentation-analysis
