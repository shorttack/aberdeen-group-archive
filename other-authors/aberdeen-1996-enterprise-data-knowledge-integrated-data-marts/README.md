# True Enterprise Data Knowledge Through Integrated Data Marts

**Aberdeen Group | September 23, 1996 | Volume 9, Number 16 | Market Viewpoint**

---

## Study Metadata

| Field | Value |
|-------|-------|
| **Study ID** | aberdeen-1996-enterprise-data-knowledge-integrated-data-marts |
| **Author** | Aberdeen Group |
| **Date** | 1996-09-23 |
| **Type** | market-study |
| **Domain** | data-warehousing |
| **Methodology** | industry-analysis, field-research, expert-opinion, document-review |
| **License** | CC-BY-4.0 |
| **Source** | [Wayback Machine](https://web.archive.org/web/19970112010232/http://www.aberdeen.com:80/secure/viewpnts/v9n16/v9n16.htm) |

---

## Abstract

Aberdeen Group argues that the proliferation of standalone departmental data marts—while individually successful—creates enterprise fragmentation, contradictory business rules, and ROI erosion. The study presents an iterative "integrated data marts" architecture: building subject-specific data marts that feed a common RDBMS-based enterprise warehouse, using high-level industry templates and synchronization methodologies to deliver both business-unit autonomy and enterprise data integrity.

---

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Published at the peak of the first data mart boom (1996), this study directly addressed the fragmentation problem that would plague enterprises for years; Aberdeen's framework anticipated hub-and-spoke BI architecture. |
| **Relevance** | high | The core problem—siloed data marts with contradictory business rules—remains acute in modern data lake and lakehouse architectures; maps directly to current data mesh and data catalog debates. |
| **Prescience** | high | Aberdeen's "disastrous fragmentation" prediction proved correct—the data swamp problem of the 2010s echoed this warning exactly; integrated warehouse architecture became the dominant enterprise data strategy. |

---

## Data Tables

| Table | File | Rows |
|-------|------|------|
| Studies | data/studies.csv | 1 |
| Entities | data/entities.csv | 7 |
| Technologies | data/technologies.csv | 6 |
| Observations | data/observations.csv | 25 |
| Codes | data/codes.csv | 22 |

---

## Quick Load (Python)

```python
import pandas as pd

observations = pd.read_csv('data/observations.csv')
framework = observations[observations['observation_type'] == 'framework-factor']
print(framework[['metric_name', 'metric_value']])
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

> Aberdeen Group. (1996, September 23). *True Enterprise Data Knowledge Through Integrated Data Marts* (Volume 9, Number 16). Aberdeen Group Market Viewpoint. Archived at https://web.archive.org/web/19970112010232/http://www.aberdeen.com:80/secure/viewpnts/v9n16/v9n16.htm

**Dataset DOI:** [pending Zenodo registration]

---

## Methodology Notes

This 5-page Aberdeen Market Viewpoint draws on Aberdeen field research with enterprise IS executives and IS planners, combined with supplier briefings from NCR, Tandem, and Prism Solutions. The integrated data mart framework presented is empirically grounded in Aberdeen's direct observation of both successful and failed data warehouse initiatives across multiple industries in 1995-1996.
