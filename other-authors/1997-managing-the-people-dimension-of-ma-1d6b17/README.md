# Managing the People Dimension of Major Technology Transitions

**Aberdeen Group Impact Brief | January 7, 1997**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-managing-the-people-dimension-of-ma-1d6b17 |
| title | Managing the People Dimension of Major Technology Transitions |
| author | Susan Irving |
| date | 1997-01-07 |
| type | impact-brief |
| subject_domain | organizational-change-management |
| methodology | field-research, industry-analysis |
| source_file | 1997 Managing the People Dimension of Major Technology Transitions im.pdf |
| license | CC-BY-4.0 |

## Abstract

In September 1996, Hewlett-Packard engaged Aberdeen Group to conduct one-on-one interviews with senior IT executives and project leaders undergoing major technology transitions. The study identifies education and training as the critical enabler of successful technology adoption, documents barriers including time pressure and ROI measurement challenges, and finds that on-demand, customized training is preferred over classroom instruction. Author Susan Irving concludes that people and process challenges consistently exceed technical challenges in large-scale technology transitions.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | medium | HP-commissioned primary research with senior IT executives; early empirical documentation of change management as a first-order IT implementation challenge. Influential in establishing Aberdeen's organizational change practice. |
| Relevance | high | The core findings—that education/training is the critical enabler, that time pressure causes training to be cut, and that on-demand customized learning beats classroom instruction—remain directly applicable to ERP, cloud migration, and digital transformation projects today. |
| Prescience | high | Aberdeen's 1997 finding that demand was shifting from classroom to on-demand, customized training accurately forecast the e-learning industry explosion (Coursera, LinkedIn Learning, vendor LMS platforms). The prediction that skipping training leads to technology rejection proved borne out by countless failed ERP and CRM rollouts. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 3 | Organizations referenced |
| technologies.csv | 4 | Technologies discussed |
| observations.csv | 21 | Extracted analytical observations |
| codes.csv | 21 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
```

## Validation

```bash
frictionless validate datapackage.json
```

## Citation

Susan Irving. (1997). *Managing the People Dimension of Major Technology Transitions*. Aberdeen Group Impact Brief.
Archived: https://web.archive.org/web/19970604114352/http://www.aberdeen.com:80/secure/impacts/1997/hp/hp.htm
License: CC-BY-4.0
