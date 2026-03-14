# Silknet Software: Changing the Rules for Next-Generation Customer Support Applications

**Aberdeen Group | July 8, 1997 | Customer Interaction Software**

## Study Metadata

| Field | Value |
|-------|-------|
| Study ID | `aberdeen-1997-silknet-software` |
| Author | Aberdeen Group |
| Date | July 8, 1997 (AberdeenGroup Volume 10, Number 9) |
| Type | Market Study (Product Viewpoint) |
| Domain | Customer Interaction Software (CIS) |
| Methodology | Competitive Profiling, Industry Analysis, Field Research |
| License | CC-BY-4.0 |

## Abstract

This July 1997 Aberdeen Group Product Viewpoint profiles Silknet Software's eService, characterizing it as the first viable internet-native customer support application built from the ground up for web deployment. Aberdeen identifies four trends driving next-generation customer support — problem resolution, customer self-service, enterprise integration, and multimedia — and asserts that Silknet's thin-client architecture uniquely satisfies all four. The study predicts Silknet will radically redefine the $1B+ customer interaction software (CIS) market, forcing client-server incumbent vendors (call-tracking specialists) to fundamentally rethink their product strategies.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Silknet eService was the first true internet-native customer support application in 1997, predating Salesforce Service Cloud and other SaaS CRM by years; Aberdeen's assessment correctly identified the architectural discontinuity that would reshape the entire CIS market category. |
| **Relevance** | high | The four trends Aberdeen identified (self-service, omnichannel, enterprise integration, multimedia support) remain the defining characteristics of modern customer service platforms; Silknet's architecture foreshadowed cloud-native CRM/CIS — direct intellectual lineage to Salesforce Service Cloud, Zendesk, Kustomer. |
| **Prescience** | high | Aberdeen's prediction that Silknet would force market restructuring was confirmed: Kana Communications acquired Silknet for $4.2B in 2000 at dot-com peak; the internet-native CIS market Aberdeen described became the dominant delivery model (Salesforce, Zendesk, ServiceNow) within a decade. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study-level metadata with ratings |
| entities.csv | 3 | Organizations mentioned |
| technologies.csv | 6 | Technologies referenced |
| observations.csv | 24 | Structured analytical observations |
| codes.csv | 22 | Controlled vocabulary definitions |

## Load with Python

```python
import pandas as pd
observations = pd.read_csv('data/observations.csv')
preds = observations[observations.observation_type == 'viability-prediction']
outcomes = observations[observations.observation_type == 'actual-outcome']
```

## Frictionless Validation

```bash
frictionless validate datapackage.json
```

## Citation

> Aberdeen Group. (1997). *Silknet Software: Changing the Rules for Next-Generation Customer Support Applications*.
> AberdeenGroup Vol.10 No.9. Aberdeen Group, Inc., Boston, MA.
> Archived: https://web.archive.org/web/19971007154357/http://www.aberdeen.com:80/secure/viewpnts/1997/v10n9/body.htm
> Dataset: `aberdeen-1997-silknet-software` | License: CC-BY-4.0
