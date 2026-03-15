# IBM Information Integration Family
## Aberdeen Group Profile (1997)

**Study ID:** `1997-ibm-information-integration-family--29351c`  
**Source:** Aberdeen Group, Inc. — IBM Network Computing Profile Series  
**Original URL:** https://web.archive.org/web/19970604113322/http://www.aberdeen.com:80/secure/profiles/1997/ibmiif/ibmiif.htm  
**Date:** June 4, 1997  
**License:** CC-BY-4.0

---

## Overview

This data package archives Aberdeen Group's 1997 evaluation of IBM's **Information Integration** product family. The study assessed IBM's tools for coordinating, federating, and replicating data across heterogeneous distributed databases in network-computing environments.

**Products covered:**
- **DataJoiner** — federated heterogeneous query across DB2, Oracle, Informix, Sybase, IMS, VSAM
- **DataPropagator (Relational and NonRelational)** — log-based CDC replication across multiple database types
- **Net.data (DB2 WWW Connection)** — dynamic HTML/SQL macros for web-to-database connectivity
- **MQSeries** — store-and-forward messaging for data movement

**Key insight:** Aberdeen framed the problem as managing "data archipelagoes" and argued that middleware reuse across recurring data-integration projects was the key economic imperative.

---

## Scores

| Dimension | Score (1–10) | Rationale |
|---|---|---|
| Importance | 7 | Documented emergence of data federation as enterprise imperative; DataJoiner's federated query model anticipates modern query engines |
| Relevance | 8 | 'Data archipelago' metaphor, CDC replication, and web-to-database dynamic query patterns are all directly contemporary |
| Prescience | 7 | CDC dominance predicted; VPE/visual dev partially confirmed; DataJoiner write-once vision materialized via other means |

---

## Contents

```
1997-ibm-information-integration-family--29351c/
├── README.md
├── datapackage.json
├── data/
│   ├── studies.csv          (1 row, 16 fields)
│   ├── entities.csv         (6 entities)
│   ├── technologies.csv     (8 technologies)
│   ├── observations.csv     (25 observations)
│   └── codes.csv
├── schema/
│   └── schema_org.json
├── source/
│   └── original_text.md     (full original text + metadata appendix)
└── scripts/
    └── demo_analysis.py
```

---

## Key Findings

- DataPropagator's **log-based CDC** architecture (described as its key differentiator) became the dominant industry replication pattern, validated by Debezium, AWS DMS, Fivetran, and Striim
- The **"data archipelago"** metaphor for enterprise data fragmentation directly anticipates modern data mesh architecture
- **DataJoiner's** federated query model anticipated Apache Drill, Presto/Trino, and Google BigQuery federation
- **Net.data's** web-to-database dynamic query pattern was ahead of its time but superseded by WebSphere/JSP

---

## Predictions vs. Outcomes

| Prediction (1997) | Outcome | Result |
|---|---|---|
| DataPropagator will add RDBMS scalability features | Absorbed into IBM DB2 replication; CDC industry-standard | Confirmed |
| Visual Programming Environment for Net.data (~1998) | IBM Rational / Eclipse-based tools; WebSphere superseded | Partial |
| Write-once apps across multiple legacy databases | Achieved via JDBC/ORM/Presto — not DataJoiner directly | Partial |
| Log-based CDC as superior replication architecture | Dominant pattern in 2020s (Debezium, Fivetran, DMS) | Strongly Confirmed |

---

## Citation

Aberdeen Group, Inc. (1997). *IBM Information Integration Family* [Profile]. Aberdeen Group. Archived via Wayback Machine: https://web.archive.org/web/19970604113322/http://www.aberdeen.com:80/secure/profiles/1997/ibmiif/ibmiif.htm  
Archival package: CC-BY-4.0, Blue Bridge Group Archival Project, 2026.
