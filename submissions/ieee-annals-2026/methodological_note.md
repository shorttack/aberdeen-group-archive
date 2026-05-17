# Methodological Note
## Archive Construction, Scoring Method, and Reproducibility

**Study:** The Enterprise AI Arc: Forty-Four Years of AI-Adjacent Product Claims in an Analyst Archive (1980–2024)
**Author:** Peter S. Kastner
**Date:** May 2026

---

## 1. The Archive as Primary Source

The Kastner IT Research Archive is a structured corpus of 947 research studies produced between 1979 and 2026, packaged as Frictionless Data Packages and publicly archived at GitHub (https://github.com/shorttack/aberdeen-group-archive, DOI: 10.5281/zenodo.20245076). Each study package contains five CSV tables: `studies.csv` (one row per study), `entities.csv` (named organizations and persons referenced), `technologies.csv` (named hardware, software, and platforms), `observations.csv` (one row per factual claim, prediction, or analytical judgment), and `codes.csv` (methodology and observation-type taxonomy). All tables conform to Frictionless Data standards with explicit JSON schema descriptors (`datapackage.json`, `schema/schema_org.json`).

The archive covers Aberdeen Group analyst output from 1988 through 2007 (the core period), supplemented by earlier Kastner-authored material from Arthur D. Little (1972–1979), Stratus Computer (1981–1985), DEC (1986–1989), and PHI Computer Services (1969–1972), plus post-Aberdeen work through 2026. The corpus includes 19,628 observation rows, 9,440 entity records, and 7,712 technology records.

**Epistemological status:** The archive is a contemporaneous documentary record, not a retrospective reconstruction. The primary studies were written at the time of the events they describe — product launches, benchmark contests, market forecasts — and archived in their original form. The structured data extraction (observations, entities, technologies) was performed in 2025–2026 using the archival-ingest pipeline described below, but the underlying text is unmodified.

---

## 2. The Archival-Ingest Pipeline

All structured data in the archive was produced by the archival-ingest v18 pipeline, a three-phase process:

**Phase 1 (AI-assisted extraction):** Each source document is read by an LLM (Perplexity Computer, Claude Sonnet / GPT-4 class) that extracts observations, entities, and technologies into structured CSV tables. The extraction follows explicit schemas with mandatory fields, controlled vocabulary for observation types and confidence levels, and a CSV Write Validation Gate (v17+) that prevents encoding defects (base64-encoded output, column-shift errors) from entering the master tables.

**Phase 2 (deterministic assembly):** A Python assembler script (`scripts/assembler.py`) generates all derivative files — `datapackage.json`, `schema_org.json`, `codes.csv`, `README.md`, `demo_analysis.py` — from the Phase 1 CSVs without LLM involvement. This ensures reproducibility: the same CSVs always produce the same package.

**Phase 3 (web verification):** Entity and prediction rows are verified against external sources in a deferred batch pass, with results cached incrementally in `_web_cache.json`. Verified rows carry `confidence: verified`; unverified rows carry `confidence: [DEFERRED]` or a human-assigned rating. The validation log (`_validation_log.csv`) is append-only and records every quality gate pass and failure.

The pipeline is public and documented in the archive repository. Any researcher can reproduce the structured extraction by running the assembler on the raw source files.

---

## 3. The Enterprise AI Arc Scoring Method

The Enterprise AI Arc study applies two analytical scores to each AI-adjacent precursor observation:

**Specificity (1–5):** Measures how precisely the archived claim matches a modern LLM-era capability.

| Score | Definition | Example |
|---|---|---|
| 5 | Named feature functionally identical to LLM-era capability | Oracle InterOffice (1995): "document summarization" |
| 4 | Directionally specific with named domain or integration target | IBM MedSpeak (1997): clinical continuous speech-to-text for EMR |
| 3 | Architectural precursor with demonstrated capability | Tandem ORDM (1997): in-database ML via SQL |
| 2 | Structural analog — same pattern, different mechanism | Lotus Notes agents (1989): rule-based autonomous document processing |
| 1 | Ambient claim — general AI aspiration, no named capability | Generic "AI-enabled" marketing language |

**Predictive distance (years):** The number of years from the archive observation to the 2022 LLM mainstream baseline (defined as ChatGPT launch, November 30, 2022 — 1 million users in five days, 100 million users in two months, the accepted commercial inflection point).

**Composite score:** `specificity × (distance / 5)`. This formula rewards early, precise claims over late or vague ones. Oracle InterOffice (specificity 5, distance 27) scores 27.0 — the highest composite in the archive. A 2019 claim with specificity 3 scores 1.8. The composite is illustrative, not determinative; the article's argument rests on the specificity scores and the documented textual record, not on the composite ranking alone.

---

## 4. The Three Supporting Longitudinals

The Enterprise AI Arc study synthesizes three completed single-entity longitudinal studies:

| Study | Observations | Source Studies | Span | Key AI Finding |
|---|---|---|---|---|
| IBM Longitudinal (`2026-kastner-ibm-longitudinal`) | 117 | 174 | 1967–2026 | IBM ran the archive's broadest pre-2000 AI portfolio (speech, chess, data mining, NLP); converted none to durable market position |
| Oracle Longitudinal (`2026-kastner-oracle-longitudinal`) | 91 | 73 | 1988–2026 | Oracle InterOffice (1995) is the archive's highest-specificity AI precursor; Oracle 23ai (2024) closes the same company's arc 29 years later |
| Intel Longitudinal (`2026-kastner-intel-longitudinal-776f7e`) | 562 | 102 | 1990–2026 | Zero Intel AI-adjacent product claims before 2019; Intel enables AI infrastructure without building AI products |

Each longitudinal study is a standalone Frictionless Data Package in the archive, fully citable and independently verifiable.

---

## 5. Limitations and Scope Boundaries

**Archive coverage is not comprehensive.** The archive documents what Aberdeen Group and Kastner chose to study. Vendors not covered (notably Hewlett-Packard for AI, Sybase for in-database ML, SAS for statistical computing) may have made comparable claims; this article does not assert the archive is exhaustive. It asserts that the archive's AI-adjacent claims are contemporaneous, structured, and scoreable.

**The LLM mainstream baseline (2022) is definitional, not the only valid anchor.** Readers who anchor to GPT-3 (2020) or the Transformer paper (2017) will produce different predictive-distance scores. The article's claims are robust to any post-2015 baseline; the directional finding (enterprise AI capability was commercially conceptualized decades earlier) holds regardless of the exact anchor year.

**Specificity scoring is the author's analytical judgment.** The five-level scale is defined explicitly and applied consistently across observations. Independent reviewers applying the same scale to the same source texts may score individual observations differently; the article does not claim precision to half a point. The key findings (Oracle InterOffice at specificity 5; IBM MedSpeak at specificity 5; Lotus Notes agents at specificity 2) represent the range of the scale, not marginal cases.

**The archive's AI observation count (78 in this study) is a subset of the full corpus.** The study includes observations specifically selected for AI-adjacency across eleven threads. The full master archive contains 19,628 observations on topics ranging from transaction processing benchmarks to ERP implementation metrics.

---

## 6. Data Access and Citation

All data are openly available under CC-BY-4.0.

**Repository:** https://github.com/shorttack/aberdeen-group-archive

**Zenodo DOI:** https://doi.org/10.5281/zenodo.20245076

**Primary submission artifact:**
`kastner-author/2026-kastner-enterprise-ai-arc/`

**Supporting longitudinals:**
- `kastner-author/2026-kastner-ibm-longitudinal/`
- `kastner-author/2026-kastner-oracle-longitudinal/`
- `kastner-author/2026-kastner-intel-longitudinal-776f7e/`

**Suggested citation for the dataset:**
> Kastner, P.S. (2026). *Kastner IT Research Archive* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20245076

The dataset will be additionally uploaded to IEEE DataPort concurrent with submission, per Annals policy.

---

*One-page methodological note — Enterprise AI Arc IEEE Annals submission — May 2026*
