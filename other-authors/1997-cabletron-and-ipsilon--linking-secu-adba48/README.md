# Cabletron and Ipsilon: Linking SecureFast Architecture and IP Switching

**Study ID:** 1997-cabletron-and-ipsilon--linking-secu-adba48  
**Author:** Samuel M. Alunni (Aberdeen Group)  
**Date:** April 17, 1997  
**Type:** Impact Brief  
**Source:** [Aberdeen Group Impact Brief, April 1997](https://web.archive.org/web/19970604114310/http://www.aberdeen.com:80/secure/impacts/1997/cable/body.htm)  
**License:** CC-BY-4.0

## Overview

Aberdeen Group Impact Brief analyzing the $20M equity investment and technology alliance between Cabletron Systems and Ipsilon Networks. The deal combined Cabletron's award-winning SecureFast SmartSwitch VLAN technology with Ipsilon's IP Switching (which offered 5x router performance at a fraction of cost) to create an end-to-end switched network from desktop to WAN. Aberdeen endorsed the alliance as among the most rational in a wave of networking M&A, and positioned it as direct competition to Cisco's Tag Switching.

The brief proved prescient about the technology rationale but incorrect about outcomes: Nokia acquired Ipsilon for $120M just 8 months later (December 1997), effectively dissolving the alliance. IP Switching lost the standards battle to Cisco's MPLS, and Cabletron itself was broken up in 2000.

## Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | **medium** | Documents a pivotal moment in the routing vs. switching debate; captures industry dynamics just before MPLS emerged as the standard |
| Relevance | **medium** | The strategic logic (combining switching speed with routing intelligence) anticipates SD-WAN; specific protocols are obsolete |
| Prescience | **low** | Alliance dissolved within 8 months; IP Switching lost to MPLS; Cabletron declined; Aberdeen's positive assessment was incorrect |

## Contents

| File | Description |
|------|-------------|
| `data/studies.csv` | Study metadata |
| `data/entities.csv` | 5 entities — Cabletron, Ipsilon, Nokia, Cisco, Enterasys |
| `data/technologies.csv` | 8 technologies — IP Switching, SecureFast, GSMP, IFMP, LFAP, Tag Switching, MPLS, SmartSwitches |
| `data/observations.csv` | 17 observations including 3 viability predictions and 4 actual outcomes |
| `data/codes.csv` | Canonical code definitions |
| `schema/schema_org.json` | Schema.org Dataset metadata |
| `source/original_text.md` | Full original document text with metadata appendix |
| `scripts/demo_analysis.py` | Demo analysis and validation script |

## Running the Demo

```bash
python scripts/demo_analysis.py
```
