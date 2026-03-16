# LaGrande Technology: A Proposal for Consumer Market Research

> **Study ID**: `2003-intel-consumer-lt-10-5-8c346e`
> **Processed by**: Archival Ingest Skill v13
> **Processing date**: 2026-03-16

## Overview

This data package contains the structured archival ingest of a 2003 proposal letter from Peter S. Kastner (EVP Research, Aberdeen Group) to Michael Ferron-Jones at Intel Corporation. The proposal argues that Intel should expand its LaGrande Technology (LT) plans to actively include the consumer market segment, which Aberdeen estimated could represent over $150 million in annual revenue to Intel.

### Key Facts

| Field | Value |
|-------|-------|
| **Author** | Peter S. Kastner |
| **Organization** | Aberdeen Group |
| **Date** | October 5, 2003 |
| **Type** | Market Research Proposal |
| **Subject Domain** | Hardware Security |
| **Recipient** | Michael Ferron-Jones, Intel Corporation |

## Package Contents

```
2003-intel-consumer-lt-10-5-8c346e/
├── README.md                    # This file
├── datapackage.json             # Frictionless Data Package descriptor
├── data/
│   ├── studies.csv              # Study metadata (1 record, 16 fields)
│   ├── entities.csv             # Referenced entities (8 records, 9 fields)
│   ├── technologies.csv         # Referenced technologies (5 records, 9 fields)
│   ├── observations.csv         # Coded observations (25 records, 12 fields)
│   └── codes.csv                # Code definitions (12 records, 4 fields)
├── schema/
│   └── schema_org.json          # Schema.org JSON-LD metadata
├── source/
│   └── original_text.md         # Original document text with metadata
└── scripts/
    └── demo_analysis.py         # Validation and analysis script
```

## Data Summary

### Entities (8)

| ID | Name | Type |
|----|------|------|
| ENT-001 | Intel Corporation | company |
| ENT-002 | Aberdeen Group | company |
| ENT-003 | Peter S. Kastner | person |
| ENT-004 | Michael Ferron-Jones | person |
| ENT-005 | Jim Hurley | person |
| ENT-006 | Narendar Sahgal | person |
| ENT-007 | Microsoft | company |
| ENT-008 | Trusted Computing Group | consortium |

### Technologies (5)

| ID | Name | Status at Study | Current Status |
|----|------|----------------|----------------|
| TECH-001 | Intel LaGrande Technology (LT) | pre-release | superseded |
| TECH-002 | LT Platform | conceptual | superseded |
| TECH-003 | Trusted Platform Module (TPM) | early-adoption | mainstream |
| TECH-004 | Intel Trusted Execution Technology (TXT) | not-yet-released | active |
| TECH-005 | NGSCB (Palladium) | pre-release | cancelled |

### Observations (25)

| Observation Type | Count |
|-----------------|-------|
| expert-opinion | 5 |
| strategy-classification | 4 |
| market-data | 4 |
| viability-prediction | 4 |
| actual-outcome | 3 |
| framework-factor | 2 |
| technology-assessment | 1 |

### Document Assessment

| Dimension | Score (1-10) | Rationale |
|-----------|:-----:|-----------|
| **Importance** | 7 | Early proposal to expand hardware-based trusted computing to consumer markets at a pivotal moment in platform security history |
| **Relevance** | 8 | Directly relevant to the evolution from LaGrande Technology to Intel TXT to TPM 2.0 mandates |
| **Prescience** | 6 | Correctly identified long-term consumer demand for hardware security, but significantly overestimated speed of adoption |

## Historical Context

Intel's LaGrande Technology was renamed **Intel Trusted Execution Technology (Intel TXT)** around 2006. It shipped primarily in enterprise/server Xeon processors. The broader trusted computing ecosystem, including TPM, evolved more slowly than Aberdeen predicted. The consumer market did not adopt hardware-rooted security at scale until **TPM 2.0 became mandatory for Windows 11 in 2021** -- approximately 15 years after Aberdeen's 2006 target date.

Aberdeen Group itself was acquired by Harte-Hanks in 2008 and later became part of Spiceworks Ziff Davis.

## Usage

### Quick Validation

```bash
python scripts/demo_analysis.py
```

### Loading Data

```python
import pandas as pd

studies = pd.read_csv("data/studies.csv")
entities = pd.read_csv("data/entities.csv")
technologies = pd.read_csv("data/technologies.csv")
observations = pd.read_csv("data/observations.csv")
codes = pd.read_csv("data/codes.csv")
```

## License

This data package is provided under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
