# Managing Customers with Next-Generation Software Applications: 1996 Edition

**Aberdeen Group Market Study | October 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-managing-customers-next-gen-helpdesk |
| **Author** | Aberdeen Group |
| **Date** | 1996-10-01 |
| **Type** | market-study |
| **Domain** | customer-interaction-software-CRM |
| **Methodology** | industry-analysis, competitive-profiling, field-research |
| **Source** | [Wayback Machine](https://web.archive.org/web/19961023152936/http://www.aberdeen.com:80/cisrpt.htm) |
| **License** | CC-BY-4.0 |

---

## Abstract

Aberdeen Group's second report on the Customer Interaction Software (CIS) market defines the category encompassing sales force automation, helpdesk, field service, telemarketing, and related technologies. The study profiles over 40 CIS suppliers, identifies market dynamics, and advises IS executives that CIS is the key to building long-term profitable customer relationships while warning that most of the hundreds of suppliers will not survive long-term.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | This study was an early and comprehensive market definition of what would become CRM software — a category that grew to $40+ billion annually. Aberdeen's 1996 CIS framework anticipated the consolidation and key functionality that shaped CRM platforms for the next three decades. |
| **Relevance** | medium | The CIS/CRM software category Aberdeen defined is now a major enterprise software sector. The analytical framework remains applicable, though specific vendors have largely consolidated or disappeared. |
| **Prescience** | high | Aberdeen predicted massive market consolidation and identified companies like Siebel Systems, Oracle, and Remedy that became market leaders. The prediction of Internet CIS implications proved accurate as web-based CRM became standard. |

---

## Data Tables Summary

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 11 |
| Technologies | data/technologies.csv | 6 |
| Observations | data/observations.csv | 19 |
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

> Aberdeen Group. (1996). *Managing Customers with Next-Generation Software Applications: 1996 Edition*. Aberdeen Group, Inc., Boston, Massachusetts. Archived at https://web.archive.org/web/19961023152936/http://www.aberdeen.com:80/cisrpt.htm

**DOI**: [PLACEHOLDER — assign via Zenodo]

---

*Processed by Archival Ingest Skill v13 — 2026-03-14*
