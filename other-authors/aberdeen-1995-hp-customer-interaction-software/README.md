# HP Smart ContAct/CIS: Customer Interaction Software — The New Market Weapon

**Frictionless Data Package — Aberdeen Group Research Archive**

---

## Study Metadata

| Field            | Value |
|-----------------|-------|
| **Study ID**    | `aberdeen-1995-hp-customer-interaction-software` |
| **Title**       | HP Smart ContAct/CIS: Customer Interaction Software - The New Market Weapon |
| **Author**      | Aberdeen Group |
| **Date**        | December 1, 1995 |
| **Type**        | Product Profile |
| **Domain**      | Customer Interaction Software (CIS) |
| **Methodology** | Industry Analysis, Competitive Profiling, Field Research |
| **Pages**       | 4 |
| **Source File** | `1995-cs-Hewlett-Packard-Company-pr_-Customer-Interaction-Software-The-New-Market-Weapon.pdf` |
| **Archived At** | https://web.archive.org/web/19970112012247/http://www.aberdeen.com:80/secure/profiles/hpcis/hp_cis.htm |

---

## Abstract

Aberdeen Group profile evaluating HP's Smart ContAct/CIS customer interaction software suite, positioned as a new market weapon for CTI and customer service automation. Published December 1995, this four-page research profile analyzes Hewlett-Packard's entry into the rapidly growing Customer Interaction Software market through its Smart ContAct initiative — a comprehensive program combining CTI middleware (ACT and CCM), professional services, RISC/Unix hardware, and strategic partnerships with leading ISVs (including Clarify, Remedy, Scopus, Siebel, and Vantive) and systems integrators (including Andersen Consulting and Cambridge Technology Partners). Aberdeen identified seven key components of Smart ContAct and assessed HP as the first full-service systems supplier for the CIS market, predicting HP would be the CIS systems-supplier-of-choice in 1996. The study reported the CIS market growing at 40%+ annually with total 1995 market value exceeding $1.5 billion.

---

## Data Tables

| File | Description | Rows |
|------|-------------|------|
| `data/studies.csv` | Study metadata record | 1 |
| `data/entities.csv` | Companies and organizations mentioned in the study | 51 |
| `data/technologies.csv` | Technologies, products, and technical concepts | 25 |
| `data/observations.csv` | Factual claims, market data, predictions, and assessments | 50 |
| `data/codes.csv` | Reference codes and controlled vocabulary | 59 |

### entities.csv — Key Fields

| Field | Description |
|-------|-------------|
| `entity_id` | Unique slug identifier |
| `entity_name` | Full entity name |
| `entity_type` | vendor / isv / systems-integrator / research-firm / telecommunications |
| `sector` | Primary industry sector |
| `status` | active / acquired / dissolved / merged / renamed / split / unknown |
| `successor` | Successor entity (if applicable) |
| `years_active` | Operational years |
| `study_id` | FK → studies.study_id |
| `notes` | Context and status notes |

### technologies.csv — Key Fields

| Field | Description |
|-------|-------------|
| `tech_id` | Unique slug identifier |
| `tech_name` | Full technology name |
| `category` | Technology category |
| `vendor` | Primary vendor |
| `era` | Time period of prominence |
| `lifecycle_at_study` | emerging / growth / mature |
| `lifecycle_current` | active / legacy / obsolete |
| `study_id` | FK → studies.study_id |

### observations.csv — Key Fields

| Field | Description |
|-------|-------------|
| `obs_id` | Unique observation identifier |
| `study_id` | FK → studies.study_id |
| `entity_id` | FK → entities.entity_id (nullable) |
| `tech_id` | FK → technologies.tech_id (nullable) |
| `observation_type` | Type of observation (see codes.csv) |
| `year_observed` | Year the observation pertains to |
| `metric_name` | Metric or data point name |
| `metric_value` | Value (string, accommodates mixed types) |
| `confidence` | high / medium / low |
| `methodology_code` | IA / FR / CP / SR |
| `source_page` | Page in source PDF |
| `notes` | Verbatim or paraphrased source text |

### Notable Observations

| obs_id | Metric | Value | Source |
|--------|--------|-------|--------|
| obs-001 | CIS market growth rate | 40%+ annually | Page 1 |
| obs-002 | CIS total market value 1995 | >$1.5 billion | Page 4 |
| obs-004 | HP ACT deployments | >200 call center sites | Page 1 |
| obs-006 | HP PSO headcount | 3,800 individuals | Page 1 |
| obs-007 | HP annual revenue | $30 billion | Page 3 |
| obs-008 | CCM price per user | $300–$800 | Page 2 |
| obs-009 | HP T-520 server benchmark | 5,621 tpm-C (12-way) | Page 2 |

---

## Entity Status Summary

| Status | Count | Notable Examples |
|--------|-------|------------------|
| acquired | 26 | Scopus → Siebel; Clarify → Nortel; Remedy → BMC; Genesys → Alcatel |
| active | 5 | AT&T, Ericsson, CAP Gemini (Capgemini), AMDOCS |
| merged | 6 | CSC → DXC; Alcatel → Nokia; Aspect → Concerto |
| dissolved | 3 | Northern Telecom (Nortel 2009), Wang Laboratories |
| renamed | 2 | Andersen Consulting → Accenture |
| split | 2 | HP → HP Inc / HPE; Rockwell → Boeing/Conexant |
| unknown | 7 | Smaller boutique firms |

---

## Technology Lifecycle Summary

| Lifecycle (Current) | Technologies |
|---------------------|-------------|
| **Active** | CIS, CTI, PBX, ACD, IVR, SFA, Helpdesk, Workflow, Data Warehousing, ANI, Screen Pop, Video Conferencing, Problem Resolution |
| **Legacy** | HP-UX, RISC/Unix Servers, HP OpenView, IBM 3270, Client-Server, TSAPI |
| **Obsolete** | HP Smart ContAct, HP CCM, HP ACT, Dialogic CT Connect, HP OpenMail, HP OpenWarehouse |

---

## Python Load Example

```python
import csv
import json
from pathlib import Path

base_dir = Path("output/aberdeen-1995-hp-customer-interaction-software")

def load_csv(filename):
    """Load a CSV file from the data/ subdirectory."""
    filepath = base_dir / "data" / filename
    with open(filepath, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# Load all tables
studies = load_csv("studies.csv")
entities = load_csv("entities.csv")
technologies = load_csv("technologies.csv")
observations = load_csv("observations.csv")
codes = load_csv("codes.csv")

print(f"Studies:      {len(studies)} rows")
print(f"Entities:     {len(entities)} rows")
print(f"Technologies: {len(technologies)} rows")
print(f"Observations: {len(observations)} rows")
print(f"Codes:        {len(codes)} rows")

# Example: find all acquired entities
acquired = [e for e in entities if e["status"] == "acquired"]
print(f"\nAcquired entities ({len(acquired)}):")
for e in acquired:
    print(f"  {e['entity_name']} → {e['successor']}")

# Example: find high-confidence market data observations
market_data = [
    o for o in observations
    if o["observation_type"] in ("market-size", "market-assessment")
    and o["confidence"] == "high"
]
print(f"\nHigh-confidence market observations ({len(market_data)}):")
for o in market_data:
    print(f"  [{o['obs_id']}] {o['metric_name']}: {o['metric_value']}")

# Load datapackage descriptor
with open(base_dir / "datapackage.json") as f:
    package = json.load(f)
print(f"\nDatapackage: {package['title']}")
print(f"Resources:   {len(package['resources'])}")
```

### Using the `frictionless` library

```python
from frictionless import Package

package = Package("output/aberdeen-1995-hp-customer-interaction-software/datapackage.json")
report = package.validate()
print(f"Valid: {report.valid}")

# Read a resource as a DataFrame
import pandas as pd
observations_df = pd.read_csv(
    "output/aberdeen-1995-hp-customer-interaction-software/data/observations.csv"
)
print(observations_df.groupby("observation_type").size().sort_values(ascending=False))
```

---

## Citation

> Aberdeen Group. (1995, December). *HP Smart ContAct/CIS: Customer Interaction Software — The New Market Weapon*. Aberdeen Group, Boston, MA.
>
> Archived: https://web.archive.org/web/19970112012247/http://www.aberdeen.com:80/secure/profiles/hpcis/hp_cis.htm

### BibTeX

```bibtex
@techreport{aberdeen1995hpcis,
  author      = {{Aberdeen Group}},
  title       = {{HP Smart ContAct/CIS: Customer Interaction Software -- The New Market Weapon}},
  institution = {Aberdeen Group},
  year        = {1995},
  month       = {December},
  address     = {Boston, MA},
  url         = {https://web.archive.org/web/19970112012247/http://www.aberdeen.com:80/secure/profiles/hpcis/hp_cis.htm},
  note        = {Product Profile. Domain: Customer Interaction Software.}
}
```

---

## Package Structure

```
aberdeen-1995-hp-customer-interaction-software/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study metadata (1 row)
│   ├── entities.csv          # Companies and organizations (51 rows)
│   ├── technologies.csv      # Technologies and products (25 rows)
│   ├── observations.csv      # Extracted observations (50 rows)
│   └── codes.csv             # Reference codes (59 rows)
├── schema/
│   └── schema_org.json       # Schema.org Dataset descriptor
└── scripts/
    └── demo_analysis.py      # Referential integrity validation and demo
```

---

## Notes on Entity Verification

Entity statuses were verified via web search against public sources:

- **Scopus Technology** → acquired by [Siebel Systems](https://www.sfgate.com/business/article/San-Mateo-s-Siebel-Gobbles-Up-Another-Company-3012338.php) for $461M in 1998
- **Genesys** → acquired by [Alcatel](https://www.marketwatch.com/story/alcatel-to-aquire-genesys-for-15-billion) for $1.5B in 2000; later divested; still active
- **Aspect Communications** → acquired by [Concerto Software](https://goldengatecap.com/golden-gate-capital-sponsors-1-0-billion-take-private-of-aspect-communications-by-concerto-software/) for $1B in 2005 (note: Aspect Telecom merged with Concord Communications to form Aspect Communications before this)
- **HP** → merged with Compaq 2002; split into HP Inc and HPE in 2015
- **Siebel Systems** → acquired by Oracle in 2006

---

*Generated 2026-03-13 | Study 5 of Aberdeen Group Research Archive*
