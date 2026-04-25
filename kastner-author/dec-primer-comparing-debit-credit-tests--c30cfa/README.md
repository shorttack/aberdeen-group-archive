# A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988)

| Field | Value |
|-------|-------|
| Author | Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs |
| Date | 1988-01-01 |
| Type | internal-competitive-marketing-paper |
| Domain | OLTP-benchmark-vendor-comparison |
| License | CC-BY-4.0 |

## Abstract

Internal Digital Equipment Corporation Corporate Systems Group competitive marketing paper authored by Peter S. Kastner (Competitive Marketing Programs, PDM1-2(E1), DTN 291-0364) circa 1988. Provides DEC sales and marketing teams with a primer on interpreting and comparing Debit-Credit benchmark results across vendors (IBM, Tandem, Stratus, System/3X). Defines DEC's three styles of Debit-Credit: Style 1 (fully qualified, all presentation services in SUT — DEC's most rigorous; not directly comparable to competitors), Style 2 (forms/character offloaded to front-end VAX, cost included in COO), and Style 3 (MicroVAX or intelligent controllers in branches — recommended for vendor comparison since no other vendor tests presentation-services costs). Critiques IBM (RAMP-C obscures comparison; OneKay 1000-tps benchmark unfairly extrapolated to 750 Debit-Credit tps under IMS Fastpath), Tandem (TopGun March 1987: 90%/2-sec instead of 95%/1-sec, only 1000 tellers per 100 tps instead of 10,000, partitioned files, NonStop SQL relative-record-key extension), and Stratus (ET-1 ≠ Debit-Credit; no journaling; single-threaded logging caps at 15-17 tps; aggressive caching of account file). Provides DEC-eye estimates: Stratus Model 120 ≈ less than 8.5 Style-1 Debit-Credit tps. Notes Tandem reports 2.5 tps/processor on CLX to 6.5 tps/processor on VLX using TopGun. States Style 1 presentation services consume 40% of VUPS on an 8700. Document signed Peter S. Kastner, CSG Competitive Marketing Programs.

## Data Tables

| Table | Rows |
|-------|------|
| studies.csv | 1 |
| entities.csv | 6 |
| technologies.csv | 10 |
| observations.csv | 11 |
| codes.csv | 41 |

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

Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs (1988). A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988).
Archived in Kastner Research Archive. DOI: [pending]

## Methodology

competitive-analysis-paper
