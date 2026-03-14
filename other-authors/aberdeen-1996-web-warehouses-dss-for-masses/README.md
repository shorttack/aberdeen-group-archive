# Web Warehouses: DSS For The Masses

**Aberdeen Group | March 25, 1996 | Volume 9, Number 6 | Technology Viewpoint**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-web-warehouses-dss-for-masses |
| **Author** | Aberdeen Group |
| **Date** | 1996-03-25 |
| **Type** | market-study |
| **Domain** | data-warehousing |
| **Methodology** | industry-analysis, field-research, expert-opinion, competitive-profiling |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112010453/http://www.aberdeen.com:80/secure/viewpnts/v9n6/v9n6.htm) |

---

## Abstract

Aberdeen Group argues that the combination of the World Wide Web, Relational OLAP, and parallel-scalable hardware will "democratize" enterprise data warehousing by dramatically reducing per-seat decision support costs (Web browser at ~$50/seat vs. $1,000/seat for traditional DSS software). The study analyzes Web-based decision support architecture, identifies hurdles to enterprise adoption (security, CGI bottlenecks, browser immaturity), and concludes that Web-enabled warehouses will transform enterprise competitive behavior.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Published March 1996—more than a year before web-based BI tools became commercially mainstream—this study articulated the thin-client BI thesis that would drive the entire enterprise BI industry for the next decade. |
| **Relevance** | high | Web browser as universal BI client is now completely dominant (Tableau, Power BI, Looker all deliver via browser); thin-client economics Aberdeen predicted materialized; security/integration challenges remained active through cloud BI era. |
| **Prescience** | high | Aberdeen's core predictions—browser-based BI democratizing decision support, web removing cost barriers, parallel-scalable hardware becoming the warehouse standard, obstacles solved in 1-2 years—all proved correct. Modern cloud data warehouses are exactly the architecture Aberdeen envisioned. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 9 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 25 |
| Codes | data/codes.csv | 22 |

---

## Quick Load (Python)

```python
import pandas as pd

observations = pd.read_csv('data/observations.csv')
predictions = observations[observations['observation_type'] == 'viability-prediction']
outcomes = observations[observations['observation_type'] == 'actual-outcome']
print(f"Predictions: {len(predictions)}, Outcomes: {len(outcomes)}")
```

---

## Validation

```bash
frictionless validate datapackage.json
```

---

## Run Demo Analysis

```bash
python scripts/demo_analysis.py
```

---

## Citation

> Aberdeen Group. (1996, March 25). *Web Warehouses: DSS For The Masses* (Volume 9, Number 6). Aberdeen Group Technology Viewpoint. Archived at https://web.archive.org/web/19970112010453/http://www.aberdeen.com:80/secure/viewpnts/v9n6/v9n6.htm

**Dataset DOI:** [pending Zenodo registration]

---

## Methodology Notes

This 5-page Aberdeen Technology Viewpoint combines industry analysis, field research from enterprise IS executives, and competitive profiling of vendors including Oracle, MicroStrategy, Information Advantage, NCR/Teradata, and Netscape. Aberdeen's prediction of web-based BI democratization was one of the earliest published analyses of the economic case for thin-client enterprise decision support—predating Gartner's formal "magic quadrant" for BI tools by several years.
