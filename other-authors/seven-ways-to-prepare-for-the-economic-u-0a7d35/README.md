# Seven Ways to Prepare for the Economic Upturn

| Field | Value |
|-------|-------|
| Author | Dan Tynan, InfoWorld |
| Date | 2004-02-13 |
| Type | feature-article |
| Domain | IT-strategy-economic-cycle |
| License | CC-BY-4.0 |

## Abstract

InfoWorld feature (Feb 13 2004) by Dan Tynan surveying seven strategic moves that IT organizations should make as the post-dot-com-crash economy begins to recover. Gartner, IDC, and Aberdeen Group forecast 2004 US tech budgets up 4-8%. The seven strategies include: don't get locked out of talent, manage capacity, prepare for Sarbanes-Oxley compliance, close the security gap, consolidate, retool for the knowledge economy, and watch outsourcing/offshoring carefully. Peter Kastner, executive vice president of research at Aberdeen Group, is quoted prominently on two of the strategies: (1) the growing number of retirements of old COBOL programmers in mainframe shops, with solutions including paying to retain, hiring back as consultants, or outsourcing; and (2) the impending erosion of Indian offshoring cost advantages as wage inflation accelerates. Kastner: 'Two or three years down the road, rapid wage inflation in India is likely to erode the economic benefits that are so enticing today.' The article is preserved across three web-archive pages (?page=0,1 / ?page=0,2) and merged into a single study per the multi-page article rule.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 6 |
| observations.csv | 8 |
| codes.csv | 24 |

## Load with Python

```python
import pandas as pd
studies = pd.read_csv('data/studies.csv')
observations = pd.read_csv('data/observations.csv')
```

## Validate

```bash
frictionless validate datapackage.json
```

## Citation

Dan Tynan, InfoWorld (2004). Seven Ways to Prepare for the Economic Upturn.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary, expert-opinion
