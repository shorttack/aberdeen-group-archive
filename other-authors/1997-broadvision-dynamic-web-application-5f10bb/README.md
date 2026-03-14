# BroadVision Dynamic Web Applications Enhance Employees, Clinch Customers, and Pamper Partners

**Aberdeen Group Product Viewpoint | July 7, 1997 | Volume 10, Number 11**

## Study Metadata

| Field | Value |
|-------|-------|
| study_id | 1997-broadvision-dynamic-web-application-5f10bb |
| title | BroadVision Dynamic Web Applications Enhance Employees, Clinch Customers, and Pamper Partners |
| author | Aberdeen Group |
| date | 1997-07-07 |
| type | product-viewpoint |
| subject_domain | e-commerce-web-applications |
| methodology | field-research, competitive-profiling, product-profiling, industry-analysis |
| source_file | 1997 BroadVision Dynamic Web Applications Enhance Employees, Clinch Customers, and Pamper Partners pvp.pdf |
| license | CC-BY-4.0 |

## Abstract

Aberdeen Group's Product Viewpoint (Volume 10, Number 11, July 7, 1997) evaluates BroadVision's One-to-One Application System as a high-end dynamic Web application platform for corporate relationship management. Aberdeen defines a three-tier hierarchy of dynamic web servers (low-end CGI, mid-range ODBC, high-end CORBA-based object-oriented) and positions One-to-One as the industry leader in the high-end tier for personalized content delivery across Internet, intranet, and extranet channels. The study profiles One-to-One's capabilities for customer management, employee knowledge management, and partner/supplier extranets, citing customers including Liberty Financial, Banco Santander, USWest, and Kodak Picture Network.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Published at the dawn of commercial e-commerce, this study accurately characterized the personalization and relationship management paradigm that would define CRM and e-commerce platforms for the next two decades; Aberdeen's categorization of dynamic web application tiers (CGI/ODBC/CORBA) was widely adopted in industry discourse. |
| Relevance | medium | The conceptual framework of personalized web applications, customer data exploitation, and relationship management via digital channels directly anticipates modern CRM, CDP, and martech platforms; specific performance benchmarks and product details are dated. |
| Prescience | high | Aberdeen's predictions about customer data becoming a competitive advantage, channel shift to internet reducing costs, and CRM/personalization as a strategic imperative all proved highly accurate; however, BroadVision itself lost market leadership to Salesforce.com and SAP by 2005. |

## Data Tables

| Table | Rows | Description |
|-------|------|-------------|
| studies.csv | 1 | Study metadata and assessments |
| entities.csv | 13 | Organizations referenced |
| technologies.csv | 8 | Technologies discussed |
| observations.csv | 25 | Extracted analytical observations |
| codes.csv | 25 | Controlled vocabulary |

## Quick Load (Python)

```python
import pandas as pd
obs = pd.read_csv("data/observations.csv")
print(obs.groupby("observation_type").size())
# Show prescient predictions
preds = obs[obs.observation_type == "viability-prediction"]
print(preds[["metric_name", "metric_value"]].to_string())
```

## Notable Findings

- Aberdeen's performance benchmarks show BroadVision One-to-One delivered **51,428 pages/hour** vs. 4,737 for custom CGI (10x improvement) on single-processor Sun UltraSPARC
- Aberdeen correctly identified customer data as strategic competitive advantage 7+ years before CRM market matured
- Push technology (PointCast) assessment as ineffective proved highly accurate; PointCast failed in 1999

## Citation

Aberdeen Group. (1997, July 7). *BroadVision Dynamic Web Applications Enhance Employees, Clinch Customers, and Pamper Partners*. Aberdeen Group Product Viewpoint, Volume 10, Number 11.
Archived: https://web.archive.org/web/19971007154340/http://www.aberdeen.com:80/secure/viewpnts/1997/v10n11/body.htm
License: CC-BY-4.0
