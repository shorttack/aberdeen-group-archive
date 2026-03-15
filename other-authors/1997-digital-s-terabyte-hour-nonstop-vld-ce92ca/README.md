# Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities

**Study ID:** 1997-digital-s-terabyte-hour-nonstop-vld-ce92ca  
**Publisher:** Aberdeen Group  
**Date:** May 20, 1997  
**Type:** Viewpoint (Aberdeen Group Volume 10, Number 7)  
**Subject Domain:** Database Storage / Very Large Database Management  
**License:** CC-BY-4.0  

## Abstract

Aberdeen Group's Viewpoint newsletter assessed Digital Equipment Corporation's NonStop VLDB backup/restore solution in May 1997. NonStop VLDB delivered 400-500+ gigabytes/hour backup/restore rates — an order of magnitude improvement over typical 10 GB/hour systems of the era. Aberdeen predicted this technology would "go strategic," removing backup/restore as a database scaling barrier and enabling novel uses including rapid database reorganization, rolling OLTP backup for data warehouses, data migration servers, and cost-effective disaster tolerance. Aberdeen estimated Digital held a ½ to 1-year lead over competitors in this technology and predicted that SGI, HP, and Sun would be first entrants to market after Digital.

## Contents

| File | Description |
|------|-------------|
| data/studies.csv | Study-level metadata |
| data/entities.csv | Organizations referenced |
| data/technologies.csv | Technologies assessed |
| data/observations.csv | Structured observations |
| data/codes.csv | Controlled vocabulary |
| schema/schema_org.json | Schema.org JSON-LD |
| source/original_text.md | Full original text with appendix |
| scripts/demo_analysis.py | Python demo analysis |

## Key Findings (1997)

- NonStop VLDB delivered 400-750 GB/hour in benchmarks; estimated 1.5 TB/hour maximum with additional hardware.
- Typical contemporary backup systems: ~10 GB/hour (40-200 GB practical database size limit).
- CPU utilization during 400 GB/hour backup: only 3-16% — minimal production impact.
- Competing: Oracle, Informix, Sybase, Microsoft SQL Server; SAP R/3 compatible.
- Aberdeen estimated ½ to 1-year Digital lead over all competitors.

## Prescience Assessment

**Score: Medium-High.** Aberdeen's core technical assessment was correct: backup/restore speed did become a strategic capability, and the architectural insights Aberdeen described — rolling backup, disaster tolerance, data migration servers — are now standard enterprise data management practices. However, the specific Digital NonStop VLDB product and platform (AlphaServer) did not survive DEC's 1998 acquisition by Compaq. The broader backup/restore performance improvement Aberdeen predicted did occur through different vendors and technologies (SAN, tape automation, deduplication, cloud backup). Aberdeen correctly identified the disruption potential of fast backup/restore but was wrong about who would deliver it long-term.

## Source

Original archived at: https://web.archive.org/web/19970604112203/http://www.aberdeen.com:80/secure/viewpnts/1997/v10n7/body.htm
