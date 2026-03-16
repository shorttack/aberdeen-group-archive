# GoRemote Is Unifying Secure Remote Access Services

**Frictionless Data Package:** `goremote-profile-5-2a-ccacbd`

## Study Overview

| Field | Value |
|---|---|
| **Title** | GoRemote Is Unifying Secure Remote Access Services |
| **Author** | Aberdeen Group |
| **Date** | September 2003 |
| **Type** | Profile |
| **Subject Domain** | Remote Access Services |
| **Methodology** | Industry Analysis, Competitive Profiling |
| **License** | CC-BY-4.0 |
| **Source File** | Goremote Profile 5-2a.txt |

## Abstract

Aberdeen Group profile of GoRemote Communications (NASDAQ: GRIC), a leading supplier of managed communications services to remote and mobile knowledge workers. The report examines the growing challenges of managing "outworkers" outside the enterprise firewall, including rising telecommunications costs (up to $8,000/year per mobile worker), security vulnerabilities, and IT support overhead (10x the support calls of office workers). GoRemote's TierOne global network spans 150+ countries with 35,000+ access points aggregated from 300+ telecom providers. The profile covers GoRemote's MobileOffice universal access client, Total Security Protection service, and enterprise management portal, positioning the company as the first unified solution for outsourced remote access management with potential 60% cost savings vs. DIY infrastructure.

## Assessment Ratings

| Dimension | Rating | Rationale |
|---|---|---|
| **Importance** | Medium | Vendor profile documenting an early unified remote access solution; valuable as a snapshot of pre-cloud enterprise mobility challenges. |
| **Relevance** | Medium | Remote work concepts are highly relevant today but specific technologies (dial-up, ISDN, frame relay) are obsolete; the outsourced connectivity model anticipated modern cloud-based remote access. |
| **Prescience** | High | Predicted dramatic growth in remote/mobile worker population and the need for unified managed access services; validated by the post-2020 remote work revolution. |

## Key Entities

- **GoRemote Communications** (NASDAQ: GRIC) -- Subject of the profile. Acquired by iPass in February 2006.
- **iPass Inc.** -- Acquired GoRemote in 2006. Subsequently acquired by Pareteum Corporation in 2019.
- **Pareteum Corporation** -- Acquired iPass in 2019. Filed for bankruptcy in 2022 after SEC fraud charges.
- **Axcelerant** -- Acquired by GoRemote in late 2003 for fixed broadband capabilities.
- **Aberdeen Group** -- Analyst firm that authored the profile.
- Enterprise customers: Avnet, Lockheed Martin, Procter & Gamble, Saint-Gobain, Stanley Works, VeriSign
- Telecom partners: China Telecom, France Telecom, Level 3, MCI, SingTel, Telstra

## Key Technologies

- **TierOne Network** -- GoRemote's aggregated global virtual network
- **MobileOffice** -- Universal access client for Windows
- **Total Security Protection (TSP)** -- Integrated security agent
- **VPN** (IPSec and SSL), WiFi 802.11, DSL/Broadband, Frame Relay, ISDN

## Package Contents

```
goremote-profile-5-2a-ccacbd/
  README.md                    -- This file
  datapackage.json             -- Frictionless Data Package descriptor
  data/
    studies.csv                -- Study metadata (1 row, 16 columns)
    entities.csv               -- Organizations mentioned (17 rows, 9 columns)
    technologies.csv           -- Technologies assessed (10 rows, 9 columns)
    observations.csv           -- Extracted observations (40 rows, 12 columns)
    codes.csv                  -- Code definitions (18 rows, 4 columns)
  schema/
    schema_org.json            -- Schema.org JSON-LD metadata
  source/
    original_text.md           -- Original study text (lines 1-108)
  scripts/
    demo_analysis.py           -- Validation and analysis script
```

## Usage

### Validate the Data Package

```bash
cd goremote-profile-5-2a-ccacbd
python3 scripts/demo_analysis.py
```

### Load in Python

```python
import csv
import json

# Load the package descriptor
with open("datapackage.json") as f:
    package = json.load(f)

# Load observations
with open("data/observations.csv") as f:
    reader = csv.DictReader(f)
    observations = list(reader)

print(f"Total observations: {len(observations)}")
```

### Load in R

```r
library(readr)
observations <- read_csv("data/observations.csv")
entities <- read_csv("data/entities.csv")
technologies <- read_csv("data/technologies.csv")
```

## Historical Note

GoRemote Communications was acquired by iPass Inc. on February 16, 2006 for an undisclosed amount. iPass continued offering managed remote access services until it was acquired by Pareteum Corporation in 2019. Pareteum filed for bankruptcy in 2022 following SEC fraud charges against its executives, ending the corporate lineage that began with GoRemote. Despite the company's demise, Aberdeen's 2003 prediction that remote outworker usage would "go up dramatically" was prescient -- validated spectacularly by the post-2020 remote work revolution driven by the COVID-19 pandemic.
