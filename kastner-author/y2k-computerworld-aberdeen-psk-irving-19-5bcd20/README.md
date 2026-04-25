# Year 2000 Solutions Series Part 1 — Aberdeen Group lead article + 12-point Best Practices (PSK + Susan Irving + John R. Logan, Computerworld Custom Publication, 1997)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner and Susan L. Irving (lead article); Peter S. Kastner (12-point Best-Practice sidebar); John R. Logan (companion editorial); Anna Tortig and Computerworld Custom Publications staff (case studies) |
| Date | 1997-05 |
| Type | advertorial-magazine-supplement |
| Domain | Y2K-enterprise-IT-management |
| License | CC-BY-4.0 |

## Abstract

Kastner is identified as Group Vice President of Aberdeen Group and 'general manager of its commercial systems practice' covering databases, OLTP, decision support, client/server architectures and distributed commercial systems development. PSK and Susan Irving co-author the lead, framing Y2K as 'as much about competitive advantage as it is about technology' and warning that 'tightly integrated, Web-enabled technology infrastructures are becoming the circulatory system of companies.' The 12-point Best Practice Recommendations attributed to Aberdeen include: 'Start immediately!'; 'Stop wounding Year 2000 messengers'; 'Send lawyers, guns and money'; 'Treat this as a war-time effort'; 'Secure trusted outside resources quickly. By mid-1997, there will be little capacity left in the industry'; 'Insist on seeing external partner compliance plans'; 'Beware the Law of Unintended Consequences'; and 'Save the blame for January 1, 2000'. PSK's rolodex of CXO targets (CFO, COO, CIO/CTO, Controller, Board of Directors, CEO) anticipates the modern multi-stakeholder cybersecurity-incident playbook.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 12 |
| technologies.csv | 6 |
| observations.csv | 12 |
| codes.csv | 35 |

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

Peter S. Kastner and Susan L. Irving (lead article); Peter S. Kastner (12-point Best-Practice sidebar); John R. Logan (companion editorial); Anna Tortig and Computerworld Custom Publications staff (case studies) (1997). Year 2000 Solutions Series Part 1 — Aberdeen Group lead article + 12-point Best Practices (PSK + Susan Irving + John R. Logan, Computerworld Custom Publication, 1997).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen Group authored the lead article 'How Enterprise Executives Can Play a Pivotal Role in the Year 2000 Solution' and a 12-point 'Year 2000 Best Practice Recommendations' sidebar in a Computerworld special advertising supplement co-sponsored by HP, Data Dimensions (Ardes 2k), and MS Millennium (MSM/2000). Logan contributed a separate editorial 'Year 2000 Issues: Understanding Will Lead to Action.' Case studies of BJ's Wholesale Club, Datapro, and United Stationers complete the Part 1 supplement (Part 2 promised in CW June 2 issue).
