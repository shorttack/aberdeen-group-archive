# Salesforce.com's Apex Code: Good Idea or Superfluous Code?

| Field | Value |
|-------|-------|
| Author | Robyn Weisman, itmanagement.earthweb.com (Datamation/internet.com) |
| Date | 2007-04-26 |
| Type | news-article |
| Domain | saas-crm-proprietary-language |
| License | CC-BY-4.0 |

## Abstract

Datamation / internet.com IT management feature (April 26, 2007) on Salesforce.com's Apex Code — a new proprietary server-side programming language introduced via developer preview at Dreamforce 2006 and generally available in January 2007. CEO Marc Benioff positions Apex as enabling 'unlimited innovation on demand' for the 'Business Web.' Peter Kastner, vice president of enterprise integration at Aberdeen Group, reports client skepticism: 'They like the idea of opening up the application to custom integration, but are perplexed over why salesforce is inventing a new scripting language when Perl, Ruby, and Javascript are already well understood by enterprise developers.' Article notes Apex differentiates via multi-tenant fault isolation and data-management / business-logic focus (vs general-purpose scripting).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 7 |
| technologies.csv | 6 |
| observations.csv | 5 |
| codes.csv | 25 |

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

Robyn Weisman, itmanagement.earthweb.com (Datamation/internet.com) (2007). Salesforce.com's Apex Code: Good Idea or Superfluous Code?.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

industry-analysis, analyst-commentary
