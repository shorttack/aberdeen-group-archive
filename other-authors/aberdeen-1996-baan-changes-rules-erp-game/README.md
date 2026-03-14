# BAAN Changes the Rules of the ERP Game with Dynamic Enterprise Modeling

> Aberdeen Group, April 24, 1996 | Archived from Wayback Machine

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-baan-changes-rules-erp-game |
| Author | Aberdeen Group |
| Date | April 24, 1996 |
| Type | Market Study |
| Domain | ERP Software |
| Methodology | Industry Analysis, Competitive Profiling, Expert Opinion |
| License | CC-BY-4.0 |
| Importance | High |
| Relevance | Medium |
| Prescience | Low |

## Abstract

Aberdeen Group evaluates Baan Company's April 1996 release of BAAN IV, featuring Dynamic Enterprise Modeling (DEM) and Orgware. The report argues BAAN IV's process-oriented, dynamically configurable architecture fundamentally advances ERP beyond static competitors, giving Baan at least a 12-month competitive lead. Aberdeen concludes Baan should be on every serious ERP evaluation shortlist.

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata with importance/relevance/prescience ratings |
| entities.csv | 4 | Organizations referenced (Baan, Aberdeen, Boeing, SAP) |
| technologies.csv | 4 | Technologies (BAAN IV, Orgware, DEM, Static ERP) |
| observations.csv | 20 | Analytical observations, predictions, and verified outcomes |
| codes.csv | 18 | Controlled vocabulary definitions |

## Load Example

```python
import pandas as pd

studies = pd.read_csv('data/studies.csv')
entities = pd.read_csv('data/entities.csv')
technologies = pd.read_csv('data/technologies.csv')
observations = pd.read_csv('data/observations.csv')
codes = pd.read_csv('data/codes.csv')

predictions = observations[observations['observation_type'] == 'viability-prediction']
outcomes = observations[observations['observation_type'] == 'actual-outcome']
print(f"Predictions: {len(predictions)}, Verified Outcomes: {len(outcomes)}")
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1996). *BAAN Changes the Rules of the ERP Game with Dynamic Enterprise Modeling*. Aberdeen Group, Inc., Boston, MA. Archived: https://web.archive.org/web/19970604113856/http://www.aberdeen.com:80/secure/profiles/baan/baan.htm. Dataset DOI: [PENDING]

## Methodology Summary

This Aberdeen Group profile is a sponsored vendor analysis combining analyst research on enterprise buyer requirements with evaluation of Baan's product announcement. The study introduces the Dynamic-ERP vs. Static-ERP analytical framework. Data derives from Aberdeen field research with enterprise ERP buyers plus review of Baan product documentation.
