# AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science

**Study ID**: `amd-profile01-db9623`
**Author**: Aberdeen Group
**Date**: March 2002
**Type**: White Paper (Aberdeen Profile)

## Overview

This Frictionless Data Package contains a structured analysis of Aberdeen Group's critical examination of AMD's Athlon XP gigahertz equivalency model numbering methodology. The original white paper (~23K characters) identified fundamental flaws in both AMD's benchmark methodology and the conceptual basis for expressing processor performance as a gigahertz-equivalent model number.

## Key Findings

- AMD's Athlon XP model numbers (e.g., 2000+ = 1.667GHz actual) claimed equivalence to Intel Pentium 4 clock speeds based on application benchmarks
- Five benchmark methodology flaws: non-disclosure to BAPCo, selective bug fixes, inconsistent results, obsolete benchmarks, and Intel outperforming AMD-on-Intel configurations
- Four conceptual flaws: time dependency, workload assumption, I/O mixing, and platform dependency
- AMD's True Performance Initiative (TPI) had stalled despite being announced as strategic
- European advertisements were reporting GHz-equivalent model numbers as actual GHz

## Assessment Ratings

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | High | Influential early critique that shaped industry discourse on benchmark transparency |
| Relevance | Medium | Benchmark integrity remains relevant; specific GHz metrics are historical |
| Prescience | High | Correctly predicted AMD would abandon GHz equivalency; anticipated increased benchmark scrutiny |

## Package Contents

```
amd-profile01-db9623/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── studies.csv           # Study metadata (16 fields)
│   ├── entities.csv          # 12 organizations (9 fields)
│   ├── technologies.csv      # 10 technologies (9 fields)
│   ├── observations.csv      # 36 coded observations (12 fields)
│   └── codes.csv             # 40 code definitions (4 fields)
├── schema/
│   └── schema_org.json       # Schema.org JSON-LD metadata
├── source/
│   └── original_text.md      # Full source text (lines 1-73)
└── scripts/
    └── demo_analysis.py      # Demonstration analysis script
```

## Data Files

### studies.csv
Single-row study metadata with 16 fields including importance, relevance, and prescience ratings with rationales.

### entities.csv
12 entities: AMD, Intel, Arthur Andersen, BAPCo, SPEC, MadOnion/Futuremark, Ziff Davis, Aberdeen Group, Microsoft, Macromedia, Adobe, and Sonic Foundry. Includes current status and post-study developments.

### technologies.csv
10 technologies: Athlon XP, Pentium 4 (Willamette), Pentium 4 (Northwood), SYSmark 2001, SPEC CPU 2000, 3DMark 2001, Winstone 2001, DirectX 7.0, DirectX 8.1, and Windows XP.

### observations.csv
36 observations across 8 canonical types:
- **strategy-classification**: AMD's GHz equivalency strategy, TPI initiative, benchmarketing approach
- **benchmark-result**: Specific scores, configurations, and methodology details
- **technology-assessment**: Evaluations of processors, benchmarks, and software
- **framework-factor**: The four fundamental conceptual flaws
- **expert-opinion**: Aberdeen's conclusions and recommendations
- **viability-prediction**: Predictions about AMD abandoning GHz equivalency, TPI stalling
- **actual-outcome**: Post-study events confirming predictions (Northwood, Andersen collapse, industry shift)
- **market-data**: Workload model assumptions, consumer behavior, model number mappings

### codes.csv
40 code definitions across 10 code types: 8 observation types, 4 confidence levels, 6 methodology codes, 4 importance levels, 4 relevance levels, 4 prescience levels, 3 entity types, 3 tech categories, 3 entity statuses, and 1 study type.

## Usage

```bash
# Run the demonstration analysis
cd scripts
python demo_analysis.py
```

## Historical Context

This white paper was published at a pivotal moment in processor marketing history. AMD introduced GHz-equivalent model numbers in October 2001 for the Athlon XP line. Aberdeen's critique proved prescient: AMD abandoned explicit GHz equivalency with the Athlon 64 launch in September 2003, and the entire industry eventually moved beyond clock speed as a primary marketing metric during the multi-core era. The auditor of AMD's benchmarks, Arthur Andersen, dissolved in 2002 following the Enron scandal, adding retrospective irony to their attestation role.

## License

CC-BY-4.0
