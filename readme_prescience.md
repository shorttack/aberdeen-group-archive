```Aberdeen Group Research Prescience 1995-2025
# Prescience Scoring Guide

This document explains how prescience is defined and scored in the Archival Ingest Skill, and how it relates to the observations extracted from each study.

## 1. What “Prescience” Means

Prescience measures how accurate a study’s forward-looking claims turned out to be, based on what actually happened later.

- It answers: “Did this study’s predictions about companies, technologies, or markets actually come true?”
- It is separate from **importance** (how significant the study was at the time) and **relevance** (how useful it remains today).

## 2. Prescience Rating Scale

Each study’s row in `studies.csv` includes two fields related to prescience:

- `prescience`
- `prescience_rationale`

The allowed values for `prescience` are:

- `high`
- `medium`
- `low`
- `not-applicable`

Interpretation:

- **High**: Most of the study’s important predictions proved correct.
- **Medium**: Mixed record; some predictions were accurate, others were not.
- **Low**: Predominantly inaccurate or meaningfully misleading predictions.
- **Not-applicable**: The study made no forward-looking claims.

The `prescience_rationale` must be a concise (1–2 sentence) explanation that ties the rating to concrete evidence:

- Refer to specific predictions in the study.
- Refer to later outcomes that confirm or contradict those predictions.

### Example rationale patterns

- *High prescience*:  
  “The report predicted that Platform X would remain a core system of record in large enterprises for at least a decade; subsequent market adoption and continued installed base validated this view.”

- *Medium prescience*:  
  “The study correctly anticipated the consolidation of vendors in this market, but underestimated the speed of cloud adoption and overestimated Vendor Y’s long-term share.”

- *Low prescience*:  
  “The analysis predicted strong survival prospects for several distributors that later failed or were acquired at distressed valuations, indicating that its forward-looking assessments were largely incorrect.”

- *Not-applicable*:  
  “This study is descriptive and historical only; it does not contain explicit forward-looking predictions.”

## 3. Evidence Basis: Observations Table

The prescience score is not assigned in isolation; it is derived from the structured observations extracted from each document.

Within `observations.csv`:

- Each prediction is recorded as an observation with `observation_type = viability-prediction`.
- Later, separate observations record what actually happened with `observation_type = actual-outcome`.

Each row connects to entities and technologies via:

- `entity_id` (linking into `entities.csv`)
- `tech_id` (linking into `technologies.csv`)

Other fields in the observation capture:

- `year_observed`
- `metric_name`
- `metric_value`
- `confidence`
- `methodology_code`
- `source_page`
- `notes`

The key idea is:

- Every prediction the study makes about viability, survival, success, or failure is encoded as a `viability-prediction`.
- Each known real-world outcome is encoded as an `actual-outcome`.
- Prescience is then judged by comparing these pairs.

## 4. Pairing Predictions with Outcomes

To evaluate prescience, each `viability-prediction` should be matched with one or more `actual-outcome` observations.

Typical pairing approaches:

- Match by the same `entity_id` and, optionally, `tech_id`.
- Match by topic when entity/tech is implicit but the subject is clearly the same (e.g., “midrange UNIX servers” as a category).

For each pair:

- The `viability-prediction` row captures what the study claimed at the time.
- The `actual-outcome` row captures what actually happened and when.
- The `confidence` field on each row documents the strength of the judgment, and `notes` can describe nuances.

Examples of pairing:

- Prediction: Distributor A will remain a top-tier national channel partner over the next five years.
- Outcome: Distributor A files for bankruptcy or is acquired at distressed valuation three years later.

Or:

- Prediction: Technology B will become the dominant platform for a specific class of enterprise workloads.
- Outcome: Market data and vendor roadmaps show that another platform became dominant instead, while Technology B stagnated.

## 5. Using External Verification

The skill allows selective use of external verification to support prescience scoring.

Typical validation steps:

- Check whether a company remained active, was acquired, or went bankrupt.
- Confirm whether a technology became dominant, remained niche, or was discontinued.
- Validate key market-structure predictions (e.g., number of major vendors, consolidation patterns).

This external information is then encoded in the `actual-outcome` observations with `confidence = verified` when appropriate.

## 6. Assigning the Prescience Score

Once predictions and outcomes are encoded:

1. Enumerate all `viability-prediction` observations for the study.
2. For each prediction, identify corresponding `actual-outcome` observations.
3. Judge whether each prediction is:
   - Correct (strong qualitative alignment with reality),
   - Partially correct (some aspects right, others wrong),
   - Incorrect or contradicted by events.
4. Consider the **importance** of each prediction:
   - Heavily weight predictions about core entities and technologies central to the study.
   - Lightly weight minor or incidental predictions.

Then assign the prescience rating:

- **High**:
  - The majority of significant predictions are correct.
  - No major prediction is decisively and clearly wrong.
  - External verification supports the conclusions.

- **Medium**:
  - Mixed record across the major predictions.
  - Some notable successes and some notable misses.
  - Overall, the study offered useful forward-looking guidance, but not consistently.

- **Low**:
  - Most salient predictions are contradicted by actual outcomes.
  - The study’s forward-looking guidance would have misled decision-makers in important ways.

- **Not-applicable**:
  - There are no `viability-prediction` observations for this study.
  - The document is purely descriptive, historical, or methodological.

The `prescience_rationale` should summarize this evaluation explicitly, referencing the pattern of prediction vs. outcome rather than just generic statements.

## 7. Documentation in the Archive

Prescience appears in two main locations in the archived package:

1. **`studies.csv`**  
   - Fields: `prescience`, `prescience_rationale`  
   - Provides a concise, machine-readable and human-readable summary.

2. **`source/original_text.md`**  
   - In the “Document Assessment” table:
     - Lists Prescience rating alongside Importance and Relevance.
   - In the “Prescience Detail” section:
     - Explicitly lists each forward-looking prediction with its:
       - Claimed metric/value.
       - Year observed.
       - Confidence at time of publication.
     - Lists the corresponding actual outcome:
       - Actual result.
       - Confidence level (often `verified`).
       - Notes explaining the outcome and any nuances.
     - If no predictions exist, this section states: “This study did not make forward-looking claims.”

Together, these elements make the prescience score both auditable and reusable:

- Auditable: A reader can inspect every prediction-outcome pair behind the rating.
- Reusable: Downstream tools can programmatically assess forecasting quality across studies, years, sectors, entities, or technologies.

---

This guide can be placed at the repository root or inside an `/docs` directory as `readme_prescience.md` and linked from the main README so that users understand how prescience is computed and how to interpret it.
```

Script Author: Peter S. Kastner, February 2026
