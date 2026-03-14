# Moving Effectively To Next-Generation Client-Server Development

**Aberdeen Group White Paper (Gupta Technologies sponsored) | 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-moving-effectively-next-gen-client-server |
| **Author** | Aberdeen Group |
| **Date** | 1996-01-12 |
| **Type** | white-paper |
| **Domain** | client-server-development-tools-CADE |
| **Methodology** | industry-analysis, competitive-profiling, field-research, expert-opinion |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112011022/http://www.aberdeen.com:80/secure/whtpaper/gupta/gupta.htm) |
| **License** | CC-BY-4.0 |

---

## Abstract

Aberdeen Group white paper, sponsored by Gupta Technologies, argues that first-generation client-server application development environments (CADEs) such as Visual Basic and PowerBuilder are "topping out" and recommends immediate adoption of next-generation CADEs. The study provides an evaluation framework for next-generation CADE selection and positions Gupta's Centura product as the leading choice for organizations migrating from first-generation toolsets.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Captured the mid-1990s transition from departmental to enterprise-scale client-server development, identifying limitations of VB and PowerBuilder. The CADE evaluation framework was substantive, though vendor-sponsored nature limits independence. |
| **Relevance** | low | Specific products are largely obsolete, but scalability challenges described (application partitioning, deployment automation, 3-tier architecture) directly anticipate modern cloud-native and microservices concerns. |
| **Prescience** | medium | Correctly predicted VB/PowerBuilder scalability constraints. However, the solution was Java EE and .NET (not Centura/Gupta, which was acquired through multiple hands to OpenText by 2015). |

---

## Data Tables Summary

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 10 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 30 |
| Codes | data/codes.csv | 24 |

---

## Quick Load (Python/pandas)

```python
import pandas as pd
observations = pd.read_csv("data/observations.csv")
print(observations["observation_type"].value_counts())
```

---

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

---

## Citation

> Aberdeen Group. (1996). *Moving Effectively To Next-Generation Client-Server Development* [White Paper]. Aberdeen Group, Inc., Boston, Massachusetts. Archived at https://web.archive.org/web/19970112011022/http://www.aberdeen.com:80/secure/whtpaper/gupta/gupta.htm

**DOI**: [PLACEHOLDER — assign via Zenodo]

---

*Processed by Archival Ingest Skill v13 — 2026-03-14*
