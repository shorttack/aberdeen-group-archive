# Aberdeen 1996 DORS Buying Guide — aberdeen.com Marketing Page (Outbound Marketing)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group |
| Date | 1996-10-23 |
| Type | employer-record |
| Domain | outbound-marketing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group marketing landing page for the 1996 edition of the 'Distributed, Open Relational Database Management Systems Buying Guide' (DORS), captured by the Internet Archive on Oct 23, 1996. Marketing asset evaluating eight DORS suppliers (Computer Associates, IBM, Informix, Microsoft, Oracle, Progress, Software AG, Sybase) across five technology dimensions (Scalability, Distributed Technology, Open Technology, Toolkits, Next-Generation including Internet/Intranets, relational OLAP, universal servers, workgroup servers). Lists 11 benefits and 4 key buying benefits. Contact: Susan Rinehart, One Boston Place. Primary archival value as outbound-marketing artifact demonstrating Aberdeen's 1996 web presence, report-marketing copywriting style, and database-market framing.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 12 |
| observations.csv | 14 |
| codes.csv | 31 |

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

Aberdeen Group (1996). Aberdeen 1996 DORS Buying Guide — aberdeen.com Marketing Page (Outbound Marketing).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

document-review, web-archive
