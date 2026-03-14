# Unisys Corporation - ClearPath SMP Servers

**Aberdeen Group | April 1996 | Aberdeen Profile**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-unisys-clearpath-smp-servers |
| **Author** | Aberdeen Group |
| **Date** | 1996-04-01 |
| **Type** | market-study |
| **Domain** | enterprise-servers |
| **Methodology** | competitive-profiling, industry-analysis, expert-opinion, benchmarking |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112011850/http://www.aberdeen.com:80/secure/profiles/unisys_2/unisys2.htm) |

---

## Abstract

Aberdeen Group profiles Unisys Corporation's ClearPath SMP Server product line following Unisys's 1995 reorganization into three business groups. The study examines Unisys's strategy of providing "full-service" computing to enterprises overwhelmed by open systems complexity, covering entry-level (SMP5200/5400), mid-range (SMP61000), and high-end server offerings, clustering via Veritas Vx Reliant, and the balance between Unix openness and proprietary ClearPath RAS requirements.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Captures Unisys at a key strategic pivot—from proprietary mainframe heritage to Intel-based SMP servers—at a time when enterprise server markets were consolidating around Intel/Unix architectures. |
| **Relevance** | medium | Unisys ClearPath Forward remains active through 2026 with roadmap to 2050; however specific 1996 server specifications are primarily of historical interest. |
| **Prescience** | medium | Aberdeen's solution-centric evolution prediction proved partially correct—Unisys shifted to services and ClearPath survived; but Unisys exited commodity Intel server markets, which Aberdeen did not fully anticipate. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 10 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 22 |
| Codes | data/codes.csv | 22 |

---

## Quick Load (Python)

```python
import pandas as pd
observations = pd.read_csv('data/observations.csv')
market = observations[observations['observation_type'] == 'market-data']
print(market[['metric_name', 'metric_value']])
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

> Aberdeen Group. (1996, April). *Unisys Corporation - ClearPath SMP Servers*. Aberdeen Group Profile. Archived at https://web.archive.org/web/19970112011850/http://www.aberdeen.com:80/secure/profiles/unisys_2/unisys2.htm

**Dataset DOI:** [pending Zenodo registration]
