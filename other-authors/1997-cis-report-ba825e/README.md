# Managing Customers with Next-Generation Software Applications: 1997 Edition

**Study ID:** 1997-cis-report-ba825e  
**Authors:** Hugh Bishop, Chris Pavlic & Bill Hills (Aberdeen Group)  
**Date:** October 1997  
**Type:** Market Research Report  
**Source:** [Aberdeen Group CIS Report 1997](https://web.archive.org/web/19980131053659/http://www.aberdeen.com:80/research/reports/cisrpt.htm)  
**License:** CC-BY-4.0

## Overview

Aberdeen Group's third annual market research report on Customer Interaction Software (CIS) — the category that would later be universally renamed CRM. At 246 pages and $895 per copy, this study profiled over 60 software suppliers, analyzed market size and growth, and documented the pivotal transition from client-server to web-based CIS architectures.

Key themes: Web-based CIS transition, CIS-to-ERP integration, Computer-Telephony Integration (CTI), diverging paths of customer service vs. help desk vs. internal support applications, and profiles of the dominant vendors of the era (Siebel, Clarify, Vantive, Remedy, Scopus, Aurum, and 55+ others).

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | **high** | Captured the CRM market at its inflection point; Aberdeen's CIS framework became reference architecture during peak consolidation period 1997-2005 |
| Relevance | **high** | Conceptual framework of CIS modules maps directly to modern CRM pillars; vendor profiles are dated but market structure analysis remains explanatory |
| Prescience | **high** | Web-based CIS prediction proved accurate; CIS-ERP integration became table stakes; CTI evolved into CCaaS; however, Salesforce SaaS model (not in this report) disrupted all incumbent vendors |

## Contents

| File | Description |
|------|-------------|
| `data/studies.csv` | Study metadata with assessments |
| `data/entities.csv` | 14 entities — CIS vendors, acquirers, Aberdeen Group |
| `data/technologies.csv` | 9 technologies — CIS modules, CTI, web architecture, SFA, ERP integration |
| `data/observations.csv` | 33 observations including 5 viability predictions and 8 actual outcomes |
| `data/codes.csv` | Canonical code definitions |
| `schema/schema_org.json` | Schema.org Dataset metadata |
| `source/original_text.md` | Full original document text with metadata appendix |
| `scripts/demo_analysis.py` | Demo analysis and validation script |

## Key Findings

- Aberdeen's 1997 CIS framework (SFA, customer service, help desk, field service, telemarketing, sales configuration) directly maps to modern CRM module structures
- Over 60 CIS vendors were profiled; the vast majority were acquired, merged, or dissolved within 10 years
- Siebel Systems rose to ~45% market share by 2002 before Oracle acquisition ($5.8B, 2005)
- Salesforce.com (founded 1999, not in this report) disrupted the entire market Aberdeen analyzed through SaaS delivery model
- Web-based CIS transition prediction: fully validated by 2003

## Running the Demo

```bash
python scripts/demo_analysis.py
```
