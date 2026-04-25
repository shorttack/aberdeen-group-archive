# Aberdeen Group Practice Definitions Compendium — Web/Internal Templates (January 2000)

| Field | Value |
|-------|-------|
| Author | Aberdeen Group practice coordinators (multi-author): Jack Maynard, Karen Moser, Katherine Jones, Steve Lane, James Ayube, David Hofferberth (EAS); Valerie O'Connell (Enterprise Management); Wayne Kernochan, Dave Hill, Dan Tanner (Platform Infrastructure); Joyce Becknell, James Gruener (Platforms Group); Suresh Chakravarthy, Bill Claybrook, Riddhi Patel (Platforms Group contributors); David Alschuler (B-to-B e-Business & Supply Chain Management); anonymous (Data Knowledge / Decision Support / Knowledge Management) |
| Date | 2000-01 |
| Type | employer-record |
| Domain | practice-area definitions; analyst rosters; coverage scope; supplier lists; market sizing; strategic market questions |
| License | CC-BY-4.0 |

## Abstract

Compendium of seven Aberdeen Group practice-definition templates produced for the firm's January 2000 planning cycle and intended for web publication and internal reference. Each template names the practice group coordinator and contributing analysts, articulates the practice's coverage scope and objectives, lists supplier coverage universe, surfaces strategic market questions, and (in several cases) supplies 1999-2000 market-size estimates by segment. Practice areas covered: (1) Enterprise Applications and Services (EAS) — ERP, professional services, eLearning — coordinated by Maynard with Hofferberth as Professional Services lead; (2) Enterprise Management — systems/network/applications/web operations management — Valerie O'Connell as Research Director; (3) Platform Infrastructure (PI) — Kernochan, Hill, Tanner — covering storage, mainframes, databases, application servers; (4) Platforms Group — Becknell, Gruener — covering server/client architectures, OS, RISC/EPIC/MAJC, information appliances; (5) Data Knowledge / Decision Support / Knowledge Management — query/reporting, OLAP, analytical applications, data mining, content management, data warehouse/mart, ETL with detailed market-size estimates; (6) B-to-B e-Business & Supply Chain Management — David Alschuler memo to Peter Kastner (Jan 17 2000) defining e-Procurement/e-Sales/e-Distribution/e-Messaging segments. Two near-duplicate Platform Infrastructure templates document active editing iterations of practice scope. The compendium establishes the canonical 'practice area definition' attribution baseline for each named analyst and is the primary documented evidence supporting Aberdeen Group practice-area Category Creator credits beyond Hofferberth (PSA) and Fletcher (CRM).

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 68 |
| technologies.csv | 50 |
| observations.csv | 35 |
| codes.csv | 28 |

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

Aberdeen Group practice coordinators (multi-author): Jack Maynard, Karen Moser, Katherine Jones, Steve Lane, James Ayube, David Hofferberth (EAS); Valerie O'Connell (Enterprise Management); Wayne Kernochan, Dave Hill, Dan Tanner (Platform Infrastructure); Joyce Becknell, James Gruener (Platforms Group); Suresh Chakravarthy, Bill Claybrook, Riddhi Patel (Platforms Group contributors); David Alschuler (B-to-B e-Business & Supply Chain Management); anonymous (Data Knowledge / Decision Support / Knowledge Management) (2000). Aberdeen Group Practice Definitions Compendium — Web/Internal Templates (January 2000).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

internal-practice-definition-templates
