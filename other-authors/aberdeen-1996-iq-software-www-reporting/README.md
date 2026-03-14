# IQ Software: Applying the WWW To Reporting Problems

**Aberdeen Group Product Profile — 1996**

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | aberdeen-1996-iq-software-www-reporting |
| Author | Aberdeen Group |
| Date | 1996-06-01 |
| Type | product-profile |
| Domain | web-enabled-business-intelligence |
| License | CC-BY-4.0 |
| Importance | medium |
| Relevance | medium |
| Prescience | medium |

## Abstract

Aberdeen Group profiles IQ Software Corporation's IQ/LiveWeb product, which applies World Wide Web technologies to enterprise reporting and decision support. The study argues that IQ/LiveWeb's three-tier architecture, object-oriented query capabilities, and Internet/Intranet publishing engine positions IQ Software ahead of competitors in WWW-enabled business intelligence, predicting the product will maintain a leadership position if IQ Software sustains its innovation pace.

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with assessment ratings |
| entities.csv | 12 | Organizations mentioned in the study |
| technologies.csv | 9 | Technologies evaluated |
| observations.csv | 27 | Structured analytical observations |
| codes.csv | 24 | Controlled vocabulary definitions |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv('data/observations.csv')
tech = pd.read_csv('data/technologies.csv')
print(tech[['tech_name','lifecycle_current']].to_string())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Aberdeen Group. (1996). *IQ Software: Applying the WWW To Reporting Problems*.
Aberdeen Group, Boston MA.
Archived: https://web.archive.org/web/19970112011740/http://www.aberdeen.com:80/secure/profiles/iq_sftwr/iq_sftwr.htm
DOI: [pending Zenodo deposit]

## Methodology

Industry analysis, competitive profiling, and field research. Examines IQ Software's IQ/LiveWeb product
architecture, object-oriented capabilities, and competitive position against Cognos Impromptu/Powerplay
and Business Objects in the emerging WWW-enabled enterprise reporting market.
