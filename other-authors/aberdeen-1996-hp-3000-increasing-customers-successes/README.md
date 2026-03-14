# HP 3000: Continuously Increasing Customers' Successes

**Aberdeen Group | 1996 | Archival Dataset**

---

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-hp-3000-increasing-customers-successes |
| Author | Aberdeen Group |
| Date | 1996 |
| Type | market-study |
| Domain | midrange-computing |
| License | CC-BY-4.0 |
| Source | [Wayback Machine](https://web.archive.org/web/19970112012100/http://www.aberdeen.com:80/secure/profiles/hp3000/hp3000.htm) |

## Abstract

Aberdeen Group analyzes Hewlett-Packard's "Customer First" strategy for the HP 3000 midrange platform, arguing that HP's decision to focus on retaining its large and loyal installed base rather than pursuing new customers is pragmatic and financially sound. The study documents deep customer loyalty, a $1.2 billion annual revenue base, and a strategic commitment to continued platform enhancement into the HP 3000's third decade.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | medium | Aberdeen's endorsement of HP's 'Customer First' strategy was influential in an era of intense platform competition; the study provided IS executives and HP stakeholders with a credible third-party rationale for continued HP 3000 investment. |
| Relevance | medium | The study's installed-base retention framework and customer-loyalty analysis remain applicable to technology platform lifecycle management today; hardware-specific performance benchmarks are dated. |
| Prescience | medium | HP did sustain the HP 3000 for over a decade beyond this study (support extended to 2010), validating the installed-base loyalty prediction; however, the platform was ultimately discontinued rather than evolving into the HP-Intel Merced era as projected. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 8 |
| Technologies | data/technologies.csv | 8 |
| Observations | data/observations.csv | 27 |
| Codes | data/codes.csv | 18 |

### Observation Types Breakdown

| Type | Count |
|------|-------|
| framework-factor | 5 |
| market-data | 4 |
| technology-assessment | 4 |
| actual-outcome | 3 |
| viability-prediction | 3 |
| expert-opinion | 2 |
| strategy-classification | 2 |
| benchmark-result | 1 |

---

## Quick Load (Python)

```python
import pandas as pd

base = "."
studies = pd.read_csv(f"{base}/data/studies.csv")
entities = pd.read_csv(f"{base}/data/entities.csv")
technologies = pd.read_csv(f"{base}/data/technologies.csv")
observations = pd.read_csv(f"{base}/data/observations.csv")
codes = pd.read_csv(f"{base}/data/codes.csv")

print(observations["observation_type"].value_counts())
```

## Validation

```bash
# Frictionless Data validation
frictionless validate datapackage.json

# Demo analysis script
python scripts/demo_analysis.py
```

---

## Citation

> Aberdeen Group. (1996). *HP 3000: Continuously Increasing Customers' Successes*. Aberdeen Group, Boston, MA.
> Archived: https://web.archive.org/web/19970112012100/http://www.aberdeen.com:80/secure/profiles/hp3000/hp3000.htm
> Dataset DOI: [pending Zenodo deposit]

---

## Methodology

This study used industry analysis, competitive profiling, and field research (customer interviews) to evaluate HP's strategy for the HP 3000 midrange platform. Aberdeen conducted interviews with HP 3000 enterprise customers to assess loyalty, satisfaction, and future deployment plans.

---

*Processed by Archival Ingest Skill v13 | 2026-03-14*
