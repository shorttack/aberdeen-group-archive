# Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads

**Frictionless Data Package** for the Aberdeen Group white paper (March 2004)

## Study Overview

| Field | Value |
|-------|-------|
| **Study ID** | `2004-03-intelitaniummfewp11.doc-618d4a` |
| **Author** | Aberdeen Group |
| **Date** | 2004-03-01 |
| **Type** | White Paper |
| **Domain** | Enterprise Computing |
| **Methodology** | Field Research, Statistical Analysis, Industry Analysis |
| **License** | CC-BY-4.0 |

## Abstract

Aberdeen Group white paper examining whether Intel Itanium processors are ready to handle mainframe-class workloads. Based on interviews with migration users and a survey of 98 mainframe users, the study finds that Itanium platforms match or exceed mainframes in performance, scalability, and cost-effectiveness while being equally robust. 40% of mainframe users express openness to Itanium migration, attracted by TCO advantages. The study recommends enterprises place Itanium on equal footing with mainframes in purchasing decisions, though users prefer surround and extend strategies over full replacement. Key barriers cited are migration risk (30%) and technology roadmap risk (26%).

## Ratings

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | High | Comprehensive survey-based analysis of mainframe-to-Itanium migration at a critical inflection point; 98 respondents provided statistically significant data on enterprise platform decisions |
| **Relevance** | Medium | Itanium was discontinued by Intel in 2021; however the methodology for evaluating platform migration and TCO analysis remains applicable to current cloud migration decisions |
| **Prescience** | Low | Predicted Itanium would become the dominant enterprise platform replacing mainframes; instead x86-64 (AMD64/Intel 64) won the market and Itanium was discontinued in 2021 |

## Directory Structure

```
2004-03-intelitaniummfewp11.doc-618d4a/
├── README.md                  # This file
├── datapackage.json           # Frictionless Data Package descriptor
├── data/
│   ├── studies.csv            # Study metadata (1 record, 16 fields)
│   ├── entities.csv           # Organizations referenced (15 records, 9 fields)
│   ├── technologies.csv       # Technologies analyzed (10 records, 9 fields)
│   ├── observations.csv       # Research observations (45 records, 12 fields)
│   └── codes.csv              # Code definitions (18 records, 4 fields)
├── schema/
│   └── schema_org.json        # Schema.org JSON-LD metadata
├── source/
│   └── original_text.md       # Original document text with metadata
└── scripts/
    └── demo_analysis.py       # Demo analysis script
```

## Data Files

### studies.csv
Single record containing study metadata including title, author, date, methodology, abstract, and importance/relevance/prescience ratings with rationales.

### entities.csv
15 organizations referenced in the study:
- **Semiconductor**: Intel, AMD
- **Corporations**: IBM, HP, Dell, Unisys, Microsoft, SAP AG, PeopleSoft, Oracle, British Petroleum, CompUSA
- **Software**: Micro Focus, Siebel Systems
- **Research**: Aberdeen Group

### technologies.csv
10 technologies analyzed:
- **Processors**: Intel Itanium (discontinued 2021), Intel Xeon (active), AMD Opteron (discontinued)
- **Platforms**: IBM zSeries (active as IBM Z), Windows Server (active), Linux on Mainframe (active), Unisys ES7000 (discontinued)
- **Applications/Languages**: COBOL (legacy), IBM DB2 (active), CICS (active)

### observations.csv
45 observations covering:
- **benchmark-result** (19): Survey data and performance measurements
- **market-data** (7): Adoption rates and market statistics
- **actual-outcome** (5): Verified real-world outcomes (added retrospectively)
- **viability-prediction** (4): Forward-looking assessments from 2004
- **expert-opinion** (5): Analyst and user qualitative judgments
- **technology-assessment** (3): Capability evaluations
- **strategy-classification** (1): Vendor strategic approaches
- **framework-factor** (1): Key analytical factors

### codes.csv
18 code definitions covering methodology types, observation types, and confidence levels.

## Key Findings from the Study

1. **Itanium Performance**: 30-100% better than Xeon; users reported 2x+ performance vs mainframes
2. **Migration Feasibility**: 2900 COBOL programs migrated in 1.25 years without recompilation
3. **Cost Advantages**: Cost of ownership one-third of mainframe; payback period of 3 months
4. **User Sentiment**: 40% of mainframe users open to Itanium; 64% believe it can handle workloads
5. **Barriers**: Migration risk (30%) and technology roadmap risk (26%) were primary concerns

## Predictions vs. Actual Outcomes

| Prediction (2004) | Actual Outcome |
|---|---|
| Itanium performance to improve 7x in 3 years | Itanium improved but never achieved dominance; discontinued 2021 |
| Intel to achieve Xeon/Itanium cost parity | x86-64 extensions made this moot; Xeon won the server market |
| Surround/extend strategies would succeed | Partially correct; enterprises adopted Intel but via x86-64 not Itanium |
| 30-40% of mainframe users motivated to switch | Mainframe usage declined but IBM mainframes persist; migration went to x86-64 and cloud |

## Usage

### Running the Demo Analysis

```bash
cd 2004-03-intelitaniummfewp11.doc-618d4a
python scripts/demo_analysis.py
```

### Loading Data in Python

```python
import csv

with open("data/observations.csv") as f:
    observations = list(csv.DictReader(f))

# Filter for survey results
survey = [o for o in observations if o["methodology_code"] == "statistical-analysis"]
for o in survey:
    print(f"{o['metric_name']}: {o['metric_value']}")
```

### Loading Data in R

```r
library(readr)
observations <- read_csv("data/observations.csv")
survey <- observations[observations$methodology_code == "statistical-analysis",]
print(survey[, c("metric_name", "metric_value")])
```

## Validation

The `demo_analysis.py` script includes a referential integrity checker that validates:
- All entity and technology `study_id` values reference valid studies
- All observation `entity_id` and `tech_id` values reference valid entities/technologies
- All `observation_type` values match definitions in `codes.csv`
- All `methodology_code` values match definitions in `codes.csv`
- All `confidence` values match definitions in `codes.csv`
