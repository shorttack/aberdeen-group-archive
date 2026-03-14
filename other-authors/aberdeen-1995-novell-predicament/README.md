# The Novell Predicament

> Aberdeen Group archival study — 1995-08-09

## Study Metadata

| Field | Value |
|---|---|
| Study ID | `aberdeen-1995-novell-predicament` |
| Title | The Novell Predicament |
| Author | Aberdeen Group |
| Date | 1995-08-09 |
| Type | market-viewpoint |
| Subject Domain | network operating systems and enterprise server market |
| License | CC-BY-4.0 |
| Wayback URL | [https://web.archive.org/web/19961023174148/http://www.aberdeen.com:80/secure/viewpnts/v9n14/v9n14.htm](https://web.archive.org/web/19961023174148/http://www.aberdeen.com:80/secure/viewpnts/v9n14/v9n14.htm) |

## Abstract

Aberdeen examines Novell's strategic crisis in August 1995, finding that IT managers are standardizing on Windows NT and that Novell has failed to execute its application server strategy. The report details Novell's three principal failure modes (tactical changes, technical execution failures, ISV attrition) and projects erosion of Novell's enterprise position. Aberdeen advises IT executives to carefully evaluate NetWare for medium and long term use while outlining prescriptions for Novell's survival.

## Document Assessment

| Dimension | Rating | Rationale |
|---|---|---|
| Importance | **high** | This Market Viewpoint is a precise contemporaneous prediction of Novell's decline, issued August 1995. It documents the exact inflection point when enterprise IT shifted from NetWare to Windows NT, with supporting data from IT managers, hardware suppliers, and ISVs—a rare multi-source convergence. |
| Relevance | **high** | Novell's fate is a canonical case study in disruption by a platform transition. The specific mechanisms Aberdeen identified (ISV attrition, NDS vs. NT directory war, file/print commoditization) are directly relevant to understanding platform-era market shifts. |
| Prescience | **high** | Aberdeen's predictions were remarkably accurate: Windows NT did displace NetWare in enterprise file/print; Novell was acquired by Attachmate in 2011; NDS/eDirectory did not achieve broad cross-platform adoption; LDAP did become the dominant directory protocol over NDS. |

## Key Findings

- IT managers standardizing on Windows NT Workstation as strategic desktop; expect NT Server to replace NetWare file/print.
- Novell's three failure modes: annual tactic changes destroying focus, repeated technical execution failures, ISV attrition.
- NDS is technically strong for interoperability but unlikely to achieve acceptance outside Novell installed base.
- Microsoft OLE Directory Services will succeed due to application drag-in effect; LDAP will become de-facto internet directory standard.
- Aberdeen issues explicit IT advisory: carefully evaluate NetWare for medium and long term.
- Novell survival prescription: make NDS best-on-NT, open new markets (telecom, multimedia) to dominate.

## Data Package Structure

```
aberdeen-1995-novell-predicament/
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
| entities.csv | 7 | Organizations and products referenced |
| technologies.csv | 8 | Technologies assessed with lifecycle status |
| observations.csv | 28 | Structured observations, predictions, and outcomes |
| codes.csv | 11+ | Methodology and observation type codes |

## Python Load Example

```python
import csv
from pathlib import Path

base = Path('aberdeen-1995-novell-predicament/data')

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
Aberdeen Group. (1995). The Novell Predicament. Aberdeen Group, Inc., Boston, MA.
Archived at: https://web.archive.org/web/19961023174148/http://www.aberdeen.com:80/secure/viewpnts/v9n14/v9n14.htm
Dataset: https://aberdeenarchive.bluebridgegrp.com/datasets/aberdeen-1995-novell-predicament
License: CC-BY-4.0
```
