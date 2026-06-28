# PC Deals Study — v1, v2, and the Lessons Learned

A self-contained study bundle on the Aberdeen *PC Deals* weekly reports (2002–2003), tracing one analysis across two extraction generations and documenting the fidelity gains in between.

Prepared for Peter S. Kastner · June 2026

## Contents

| File | What it is |
|---|---|
| [PC_Deals_Study_v2.md](./PC_Deals_Study_v2.md) | **Version 2** — the analysis rebuilt on the `-mx` model-extraction layer. Start here. Opens with §0 "Why Version 2 is better." |
| [PC_Deals_Study_v1.md](./PC_Deals_Study_v1.md) | **Version 1** — the original analysis on the legacy ingest, including its Section 6 self-audit that exposed the loss modes. |
| [LESSONS_LEARNED.md](./LESSONS_LEARNED.md) | **Synthesis** — the loss taxonomy v1 found, mapped to exactly how the `-mx` re-ingest repaired each mode, with before/after counts. |
| [SMOKE_TEST_REPORT.md](./SMOKE_TEST_REPORT.md) | The 3-study proof run (per-SKU journeys, phantom kill). |
| [FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md) | The 50-study re-extraction and its quality gate. |
| [v1_v2_comparison_report.md](./v1_v2_comparison_report.md) | The head-to-head Pass C prescience-scoring comparison on the 13 scored studies. |

## The arc in one line

v1 read a structured layer that dropped the reasoning (0-for-4 on the highest-value facts); the `-mx` re-ingest repaired every loss mode; v2 reads the repaired layer and recovers all four flagship facts as queryable, prescience-scored observations. Fewer rows, more truth.

## Data provenance

- Primary: rebuilt Kastner Aberdeen Wiki `kastner.duckdb` (27 `v_*` views), `-mx` PC Deals sub-corpus (50 studies / 725 observations), verified live 2026-06-28.
- Pass C verdicts: `run_prescience_pass_c_v7.py`, verdict rule locked 2026-06-27.
- Secondary market record: cited inline in each report (Computerworld/Dataquest, IDC, CNET, The Register, Intel, AnandTech, Bloomberg, BGR).
