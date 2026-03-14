# Live Object Caching: High-Performance for Object/Relational Applications

**Aberdeen Group Technology Viewpoint | Volume 9, Number 15 | August 13, 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-live-object-caching-high-performance |
| **Author** | Aberdeen Group |
| **Date** | 1996-08-13 |
| **Type** | market-study |
| **Domain** | object-relational-database-middleware |
| **Methodology** | industry-analysis, competitive-profiling, field-research, expert-opinion |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970604112359/http://www.aberdeen.com:80/secure/viewpnts/v9n15/v9n15.htm) |
| **License** | CC-BY-4.0 |

---

## Abstract

Aberdeen Group analyzes the performance challenge of combining object-oriented application code with relational databases, defining "live object caching" as the solution to object-relational impedance mismatch. The study profiles Persistence Software's Object Builder and Object Server as the leading tools enabling commercial object/relational production systems, and recommends that IS organizations adopting OO development evaluate live object caching before proceeding.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study addressed a critical and largely unresolved technical problem at the frontier of mid-1990s software architecture: combining the emerging OO paradigm with relational databases. Aberdeen's formulation of "live object caching" was an early articulation of what became a standard ORM pattern. |
| **Relevance** | medium | The object/relational mapping problem Aberdeen described remains fundamental; frameworks such as Hibernate, JPA, and Django ORM are its direct descendants. The specific vendor (Persistence Software, acquired 2004) is historical, but architectural concepts are directly applicable. |
| **Prescience** | high | Aberdeen correctly predicted OO/relational hybrid architecture would dominate and that ODBMS would fail to achieve mainstream adoption — both proved exactly correct. Sun licensed Persistence technology for Enterprise JavaBeans in 1998, validating the prediction. |

---

## Data Tables Summary

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 10 |
| Technologies | data/technologies.csv | 9 |
| Observations | data/observations.csv | 28 |
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

> Aberdeen Group. (1996, August 13). *Live Object Caching: High-Performance for Object/Relational Applications* (Volume 9, Number 15). Aberdeen Group, Inc., Boston, Massachusetts. Archived at https://web.archive.org/web/19970604112359/http://www.aberdeen.com:80/secure/viewpnts/v9n15/v9n15.htm

**DOI**: [PLACEHOLDER — assign via Zenodo]

---

*Processed by Archival Ingest Skill v13 — 2026-03-14*
