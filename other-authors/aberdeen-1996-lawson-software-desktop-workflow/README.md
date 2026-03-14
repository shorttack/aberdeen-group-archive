# Lawson Software Delivers the Desktop and Workflow Combination One-Two-Punch

**Aberdeen Group Product Viewpoint | Volume 9, Number 1 | January 12, 1996**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-lawson-software-desktop-workflow |
| **Author** | Aberdeen Group |
| **Date** | 1996-01-12 |
| **Type** | market-study |
| **Domain** | ERP-client-server-workflow |
| **Methodology** | industry-analysis, competitive-profiling, expert-opinion |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112010744/http://www.aberdeen.com:80/secure/viewpnts/v9n1/v9n1.htm) |
| **License** | CC-BY-4.0 |

---

## Abstract

Aberdeen Group evaluates Lawson Software's Open Enterprise Desktop (OED) and forthcoming integrated Lawson Workflow as a compelling "one-two-punch" in the client-server solutions (CSS) marketplace, asserting that Lawson's multi-tier workflow architecture and process-oriented GUI give it a significant competitive advantage over Oracle, PeopleSoft, and SAP. The study analyzes workflow forms, integration levels, and scalability criteria while concluding that Lawson is uniquely positioned across multiple market segments.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Published at the height of the mid-1990s ERP/CSS boom, this Aberdeen Product Viewpoint provided early evaluative coverage of integrated workflow in packaged business applications—a topic of significant IS buyer interest—though its scope was limited to a single vendor profile. |
| **Relevance** | low | The specific products (Lawson OED, v7.0 CSS) are long superseded; however, the analytical framework for evaluating workflow integration—flexibility, scalability, productivity—retains methodological relevance for modern BPM assessments. |
| **Prescience** | medium | Aberdeen correctly predicted Lawson would remain viable and competitive in vertical markets (healthcare, distribution), which proved true until its 2011 acquisition by Infor for $2 billion. The prediction that OED's Internet/Java capabilities would keep Lawson in the CSS vanguard was only partially realized. |

---

## Data Tables Summary

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 10 |
| Technologies | data/technologies.csv | 7 |
| Observations | data/observations.csv | 25 |
| Codes | data/codes.csv | 23 |

---

## Quick Load (Python/pandas)

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")

print(f"Observations: {len(observations)}")
print(observations["observation_type"].value_counts())
```

---

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

---

## Demo Analysis

```bash
python scripts/demo_analysis.py
```

---

## Citation

> Aberdeen Group. (1996, January 12). *Lawson Software Delivers the Desktop and Workflow Combination One-Two-Punch* (Volume 9, Number 1). Aberdeen Group, Inc., Boston, Massachusetts. Archived at https://web.archive.org/web/19970112010744/http://www.aberdeen.com:80/secure/viewpnts/v9n1/v9n1.htm

**DOI**: [PLACEHOLDER — assign via Zenodo]

---

## Methodology Summary

This Product Viewpoint combines industry analysis of the mid-1990s CSS/ERP market with competitive profiling of Lawson Software's workflow and desktop technologies versus Oracle, PeopleSoft, and SAP. Aberdeen's evaluation framework applies three criteria (flexibility, scalability, productivity) to assess integrated workflow in packaged business applications, drawing on field interviews with Lawson customers.

---

*Processed by Archival Ingest Skill v13 — 2026-03-14*
