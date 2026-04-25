# Aberdeen Group — Putting Headlines In Context (Multitrak User's Group, Sep 1991)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner — Vice-President, Aberdeen Group, Inc. |
| Date | 1991-09-01 |
| Type | conference-presentation |
| Domain | downsizing-and-cooperative-processing |
| License | CC-BY-4.0 |

## Abstract

Aberdeen Group conference presentation deck delivered by Peter S. Kastner (Vice-President, Aberdeen Group) at the Multitrak User's Group meeting in September 1991, footer 92 State Street Boston MA, (617) 723-7890. Agenda: Headline Confusion, Spoke-Node-Ring (S-N-R), Downsizing, Client-Server, Software Tools, Managing Change, Wrap-up. Presents Kastner's signature Spoke-Node-Ring planning model showing Corporate Data Node, Spoke Nodes, Middle Manager Ring, and Data Collection nodes. Includes IBM 'Two Tier - Two Mainframes' (S/370 + AS/400) framing. Defines Downsizing both operationally (moving MIS function down org) and technically (migrating computer-based functions from central mainframe to dispersed systems). Three case histories: (1) Banking — regional bank gains corporate cash-management share via multiple minicomputers; (2) Manufacturing — three-year migration from central 4381 to plant rings with systems integrator; (3) Automotive — moving program development from mainframe to desktop systems (initial programmer revolt followed by acceptance, more apps released but more demanded — no backlog reduction). Cooperative Processing section covers four IBM models: Remote Presentation (Easel), Remote Database (LU 6.2), IBM's Definition (OS/2 R2 → CICS → DB2), and What Users Want (SAA with DB2 circa 1994; OS/2 EE → AIX → DB2). Application Development Tools section quotes George H. Conrades (IBM Senior VP, Sept 19 1989): 'It Doesn't Make Sense For Computers To Process 100 Million Instructions Per Second, While Programmers Produce Just Ten Lines Of Code Per Day.' Discusses CASE — panacea, 4GL, management control tool, industrial-strength application development. Programming Staff Profile generational deterministic: YES Cobol/CICS, NO C++/X.Windows. IBM AD/Cycle Vision diagram. Why CASE Will Use PS/2 On A LAN section. Closes with Organizational Paradoxes of Downsizing and Managing Change. Includes Aberdeen Group corporate background and Kastner CV (DEC, Prime Computer, Stratus Computer, ADL prior).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 9 |
| technologies.csv | 11 |
| observations.csv | 10 |
| codes.csv | 39 |

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

Peter S. Kastner — Vice-President, Aberdeen Group, Inc. (1991). Aberdeen Group — Putting Headlines In Context (Multitrak User's Group, Sep 1991).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

Aberdeen-Group-presentation-deck
