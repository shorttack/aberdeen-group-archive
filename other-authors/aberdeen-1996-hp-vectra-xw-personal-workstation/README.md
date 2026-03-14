# The Vectra XW Personal Workstation: Hewlett-Packard's NT-based Alternative for Technical Computing

**Aberdeen Group | August 26, 1996 | Aberdeen Profile**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-hp-vectra-xw-personal-workstation |
| **Author** | Aberdeen Group |
| **Date** | 1996-08-26 |
| **Type** | market-study |
| **Domain** | workstation-computing |
| **Methodology** | competitive-profiling, benchmarking, industry-analysis, expert-opinion |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112011343/http://www.aberdeen.com:80/secure/profiles/hpvectra/hpvectra.htm) |

---

## Abstract

Aberdeen Group profiles Hewlett-Packard's Vectra XW personal workstation, the company's first major Windows NT/Intel platform aimed at technical computing markets traditionally served by Unix/RISC workstations. The study analyzes HP's mixed NT-Unix strategy, benchmarks the Vectra XW against Silicon Graphics Indigo 2 and NeTpower Calisto, evaluates software solution supplier relationships in MDA/EDA/GIS markets, and concludes HP has built a compelling price/performance alternative that threatens low-end Unix workstations.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Captures the pivotal inflection point: the leading Unix workstation maker committing to Windows NT/Intel for technical computing, directly challenging SGI's Unix-only strategy. |
| **Relevance** | medium | The NT-vs-Unix workstation battle is historically resolved (Wintel won decisively), but the strategic analysis of mixed platform management and ISV porting economics remains instructive. |
| **Prescience** | high | Aberdeen's prediction that NT/Intel would disrupt Unix workstations proved correct—SGI exited the workstation market and was acquired by HPE; Wintel dominated technical computing by the early 2000s. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 9 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 24 |
| Codes | data/codes.csv | 22 |

---

## Quick Load (Python)

```python
import pandas as pd

studies = pd.read_csv('data/studies.csv')
entities = pd.read_csv('data/entities.csv')
technologies = pd.read_csv('data/technologies.csv')
observations = pd.read_csv('data/observations.csv')
codes = pd.read_csv('data/codes.csv')

# Show benchmark results
benchmarks = observations[observations['observation_type'] == 'benchmark-result']
print(benchmarks[['metric_name', 'metric_value']])
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

> Aberdeen Group. (1996, August 26). *The Vectra XW Personal Workstation: Hewlett-Packard's NT-based Alternative for Technical Computing*. Aberdeen Group Profile. Archived at https://web.archive.org/web/19970112011343/http://www.aberdeen.com:80/secure/profiles/hpvectra/hpvectra.htm

**Dataset DOI:** [pending Zenodo registration]

---

## Methodology Notes

This is a 3-page Aberdeen Profile based on vendor briefings, public product specifications, and proprietary TI Bench'95 benchmark data. Aberdeen benchmarked the Vectra XW against Silicon Graphics Indigo2 using Price*Bench95 metrics (lower = better price/performance). ISV ecosystem coverage reflects Aberdeen's knowledge of the MDA/EDA/GIS market from its Unix workstation research practice.
