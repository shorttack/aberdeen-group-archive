# Upgrading To ISV Methodology For Enterprise Application Development

> Aberdeen Group archival study — 1995-12-07

## Study Metadata

| Field | Value |
|---|---|
| Study ID | `aberdeen-1995-upgrading-isv-methodology-enterprise-application-development` |
| Title | Upgrading To ISV Methodology For Enterprise Application Development |
| Author | Aberdeen Group |
| Date | 1995-12-07 |
| Type | practice-viewpoint |
| Subject Domain | enterprise application development methodology |
| License | CC-BY-4.0 |
| Wayback URL | [https://web.archive.org/web/19970112010805/http://www.aberdeen.com:80/secure/viewpnts/v8n17/v8n17.htm](https://web.archive.org/web/19970112010805/http://www.aberdeen.com:80/secure/viewpnts/v8n17/v8n17.htm) |

## Abstract

Aberdeen examines ADM's SCRUM methodology — a codification of ISV best practices for enterprise application development — and argues that in-house IS organizations should adopt ISV-style rapid iterative development over traditional waterfall planning-heavy methods. The study details SCRUM's three phases (Planning, Sprints, Closure) and ADM's Product Management Facility implementation, concluding that IS teams must adopt sprint-based methods with small teams, short cycles, and flexible toolsets to compete with the speed of the best ISVs.

## Document Assessment

| Dimension | Rating | Rationale |
|---|---|---|
| Importance | **high** | This 1995 document is a direct precursor to modern Agile methodologies. Aberdeen's endorsement of SCRUM — 6 years before the Agile Manifesto (2001) — documents the intellectual lineage from ISV practices to formalized Agile frameworks. ADM's Jeff Sutherland is credited as SCRUM co-creator. |
| Relevance | **high** | SCRUM/Agile has become the dominant software development methodology globally. This document provides primary-source evidence of the methodology's roots in ISV practices and the specific framing used in 1995 to advocate for its enterprise adoption. |
| Prescience | **high** | Aberdeen's predictions proved exceptionally accurate: SCRUM became a global standard (the Scrum Guide, Scrum.org); ISV practices (small teams, short sprints, early delivery) were codified in the 2001 Agile Manifesto; traditional waterfall methods did lose ground in enterprise IS. Aberdeen correctly identified the methodology transition 6+ years before its formalization. |

## Key Findings

- Traditional IS prioritizes cost/compatibility/functionality/quality; ISVs prioritize time-to-launch (cost is not a primary ISV trade-off).
- SCRUM methodology consists of 3 phases: Planning and System Architecture, multiple Sprints, Closure.
- Sprint teams: 1-7 members (developer + QA + documentation), 1-6 week duration, deliver executable code.
- Sprint reviews include teams, project manager, customers/prospects, and senior executives.
- ADM codified best practices of driven-to-succeed ISVs into Product Management Facility (4th MATE module).
- IS organizations that don't adopt ISV-style development will face growing frustration with management demands.

## Data Package Structure

```
aberdeen-1995-upgrading-isv-methodology-enterprise-application-development/
├── README.md
├── datapackage.json
├── data/
│   ├── studies.csv        (v12 schema: 16 fields)
│   ├── entities.csv
│   ├── technologies.csv
│   ├── observations.csv   (12-column canonical schema)
│   └── codes.csv
├── schema/
│   └── schema_org.json
├── source/
│   └── original_text.md   (full text + appended metadata)
└── scripts/
    └── demo_analysis.py
```

## Data Tables Summary

| File | Rows | Description |
|---|---|---|
| studies.csv | 1 | Study metadata, abstract, and assessment scores |
| entities.csv | 2 | Organizations and products referenced |
| technologies.csv | 6 | Technologies assessed with lifecycle status |
| observations.csv | 25 | Structured observations, predictions, and outcomes |
| codes.csv | 11+ | Methodology and observation type codes |

## Python Load Example

```python
import csv
from pathlib import Path

base = Path('aberdeen-1995-upgrading-isv-methodology-enterprise-application-development/data')

def load(name):
    with open(base / name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

studies = load('studies.csv')
entities = load('entities.csv')
technologies = load('technologies.csv')
observations = load('observations.csv')
codes = load('codes.csv')

# Get viability predictions
predictions = [o for o in observations if o['observation_type'] == 'viability-prediction']
outcomes = [o for o in observations if o['observation_type'] == 'actual-outcome']
print(f'Predictions: {len(predictions)}, Outcomes: {len(outcomes)}')
```

## Citation

```
Aberdeen Group. (1995). Upgrading To ISV Methodology For Enterprise Application Development. Aberdeen Group, Inc., Boston, MA.
Archived at: https://web.archive.org/web/19970112010805/http://www.aberdeen.com:80/secure/viewpnts/v8n17/v8n17.htm
Dataset: https://aberdeenarchive.bluebridgegrp.com/datasets/aberdeen-1995-upgrading-isv-methodology-enterprise-application-development
License: CC-BY-4.0
```
