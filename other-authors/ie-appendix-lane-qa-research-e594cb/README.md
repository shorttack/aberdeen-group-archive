# Research Findings: The Role of Professional Services Suppliers' Internal Quality Assurance Organizations in Large-scale Systems Integration Engagements

**Study ID**: `ie-appendix-lane-qa-research-e594cb`
**Author**: Stephen Lane, Aberdeen Group Senior Analyst
**Date**: June 21, 1999
**Type**: Expert Report (Appendix V, IE v. Andersen Consulting)
**License**: CC-BY-4.0

## Overview

Comprehensive comparative study of internal quality assurance (QA) programs at eight major IT professional services firms, undertaken at the request of Peter Kastner, Executive Vice President of the Aberdeen Group. Based on telephone interviews with QA practice leaders and review of Andersen Consulting's Client Quality Management Reference Manual.

## Firms Profiled

| Firm | Current Status | Key QA Feature |
|------|---------------|----------------|
| Ernst & Young LLP | Active | Quality Advisor program (1992), $1M threshold |
| Computer Sciences Corporation (CSC) | Acquired → DXC Technology | SEI CMM Levels 2-5, TMG since 1996 |
| KPMG Consulting | Acquired → BearingPoint | Proactive QAP since 1996, $1M threshold |
| Deloitte Consulting | Active | Separate Risk Management and QA/QC functions |
| Keane Inc. | Acquired → NTT DATA | Corporate QA org since 1994, quarterly reviews |
| Electronic Data Systems (EDS) | Acquired → HP Enterprise Services | 75+ solutions centers, PM2/SC3 methodologies |
| PricewaterhouseCoopers | Active | Regional QA orgs since 1988, destroys reports after 1 year |
| Andersen Consulting | Active → Accenture | QMS/CQM system, mandatory reviews above industry norm |

## Key Findings

1. **Centralized QA**: 6 of 8 firms have centralized organizations actively conducting project reviews; remaining 2 use senior partners
2. **Andersen Above Norm**: Andersen's requirement that all projects undergo at least one independent QA review is above industry norms
3. **Report Sharing**: Only Deloitte, CSC, and Keane share complete QA reports with clients as general practice
4. **No Legal Precedent**: None of the interviewees could recall QA documents being used in legal actions
5. **Revenue Thresholds**: E&Y and KPMG both use $1M revenue thresholds for mandatory QA assignment
6. **SEI/ISO Adoption**: CSC most advanced with CMM Levels 2-5; Deloitte ISO 9000 in Europe/Canada; Keane ISO 9001 in UK

## Data Package Contents

```
ie-appendix-lane-qa-research-e594cb/
├── README.md                    # This file
├── datapackage.json             # Frictionless Data Package descriptor
├── data/
│   ├── studies.csv              # Study metadata (1 row, 16 fields)
│   ├── entities.csv             # Organizations and individuals (14 entities)
│   ├── technologies.csv         # Frameworks and tools (6 technologies)
│   ├── observations.csv         # Extracted findings (40 observations)
│   └── codes.csv                # Controlled vocabulary (43 codes)
├── schema/
│   └── schema_org.json          # Schema.org Dataset JSON-LD
├── source/
│   └── original_text.md         # Original document text
└── scripts/
    └── demo_analysis.py         # Validation and analysis script
```

## Observations Summary

- **40 observations** extracted across 8 canonical types
- **framework-factor**: 18 (QA organizational structures, review processes, policies)
- **technology-assessment**: 10 (CMM levels, ISO certifications, methodology maturity)
- **expert-opinion**: 2 (overall assessment of Andersen, CSC legal history)
- **benchmark-result**: 1 (cross-firm revenue threshold comparison)
- **market-data**: 1 (EDS solutions center count)
- **Methodology**: Primarily field-research (interviews) and document-review (Andersen manuals)

## Validation

Run the validation script:
```bash
cd ie-appendix-lane-qa-research-e594cb
python scripts/demo_analysis.py
```

## Assessment Ratings

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | High | Rare comparative study of QA practices across 8 major IT consulting firms based on primary research interviews |
| Relevance | Medium | QA frameworks and organizational patterns remain relevant; specific firm names and structures changed through M&A |
| Prescience | Not Applicable | Study was descriptive and comparative rather than predictive |
