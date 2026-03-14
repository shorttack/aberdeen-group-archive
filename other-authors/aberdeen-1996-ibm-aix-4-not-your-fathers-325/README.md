# The New IBM AIX 4: Not Your Father's 3.2.5

**Aberdeen Group | April 30, 1996 | Volume 9 / Number 9**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-ibm-aix-4-not-your-fathers-325 |
| **Author** | Aberdeen Group |
| **Date** | 1996-04-30 |
| **Type** | market-study |
| **Domain** | Unix-operating-systems |
| **Methodology** | industry-analysis, field-research, expert-opinion |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19961023182518/http://www.aberdeen.com:80/secure/viewpnts/v9n9/htframe.htm) |

---

## Abstract

Aberdeen Group analyzes the extremely low adoption rate of IBM AIX 4 among RS/6000 users—estimated at less than 10% of the installed base 18 months after launch—and argues that best-practice IS management requires an immediate upgrade from AIX 3.2.5. The study examines user resistance rooted in version-3 PTF fatigue, evaluates AIX 4's modular VRMF architecture and SMP readiness, and concludes that the reward-to-risk ratio overwhelmingly favors migration in 1996.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Addressed a real adoption gap in a commercially important OS with field-level evidence; narrowly scoped to one vendor's platform. |
| **Relevance** | medium | AIX remains active through AIX 7.3 (supported to 2028); change-management framework for OS migration resistance still applicable. |
| **Prescience** | high | Aberdeen's prediction that AIX 4 would dominate proved correct—AIX evolved to version 7.3 and IBM Power remains a production enterprise platform 30 years later. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 3 |
| Technologies | data/technologies.csv | 7 |
| Observations | data/observations.csv | 22 |
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

print(observations['observation_type'].value_counts())
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

> Aberdeen Group. (1996, April 30). *The New IBM AIX 4: Not Your Father's 3.2.5* (Volume 9, Number 9). Aberdeen Group Market Viewpoint. Archived at https://web.archive.org/web/19961023182518/http://www.aberdeen.com:80/secure/viewpnts/v9n9/htframe.htm

**Dataset DOI:** [pending Zenodo registration]

---

## Methodology Notes

This is a single-page Aberdeen Market Viewpoint based on primary field interviews with RS/6000 AIX users and IS managers. Aberdeen conducted original surveys to measure migration rates and identify adoption barriers. The SMP Efficiency Rating (Figure 1) represents Aberdeen's proprietary benchmarking methodology. Predictions have been verified against public IBM product lifecycle records.
