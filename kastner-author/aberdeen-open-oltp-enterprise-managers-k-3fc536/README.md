# Open Online Transaction Processing: An Enterprise Manager's Guide — Korean (Hangul) Translation, c. 1991/1992

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner (Aberdeen Group); Korean translation by NCR Korea (publisher) |
| Date | 1991 |
| Type | translated-white-paper |
| Domain | open-OLTP/enterprise-IS-strategy/Korean-localization |
| License | CC-BY-4.0 |

## Abstract

Korean-language (Hangul) translation of the Aberdeen Group white paper 'Open Online Transaction Processing: An Enterprise Manager's Guide' authored by Peter S. Kastner (and developed/funded by Aberdeen and its sponsor company, per the bilingual title-page note). This is the international localization companion to the English-language Aberdeen Open OLTP study archived in Batch 22 (slug aberdeen-open-online-transaction-process). Four source files were reconciled per user instruction ('reconcile translations... pick the best or merge to fix artifacts'): (1) NCR-Open-OLTP-1991-Hangul-Korean-8.docx — primary Korean original (89,020 bytes); (2) NCR-Open-OLTP-Korea-1991-9.docx — duplicate of the same Hangul original (89,437 bytes; trivial differences); (3) NCR-Korea-1991-Google-Translate-3.docx — clean Korean→English Google Translate rendering used as the primary English text in this archive; (4) NCR-Korea-1991-poor-translation-4.docx — older/poor translation with severe character-encoding artifacts ('0=11', '0？611 01.7？'), retained for completeness but not authoritative. The cleanest English text (file #3) preserves the full Aberdeen argument: Open OLTP definition (computer mechanism that changes the state of a business in real time while using industry standards), six standards bodies (ISO/X-Open/POSIX/SQL-Access/OSF DCE/Unix International), ACID test components, six executive checklist items, fifteen-stage life-cycle model, and the Aberdeen claim that >90% of OLTP applications need ≤12 transactions per second. Includes table of OLTP applications by industry (banking ATMs, securities trading, insurance claims, telecom directory assistance, government emergency dispatch, retail credit, home shopping). The Korean localization documents NCR Corporation's strategy of using Aberdeen-authored, NCR-funded technical white papers as Asian-market education collateral.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 16 |
| technologies.csv | 12 |
| observations.csv | 13 |
| codes.csv | 35 |

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

Peter S. Kastner (Aberdeen Group); Korean translation by NCR Korea (publisher) (1991). Open Online Transaction Processing: An Enterprise Manager's Guide — Korean (Hangul) Translation, c. 1991/1992.
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

translation-reconciliation-of-Aberdeen-white-paper
