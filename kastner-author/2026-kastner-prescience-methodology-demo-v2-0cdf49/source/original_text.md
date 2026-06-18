# A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 — Multi-Horizon)

> study_id: 2026-kastner-prescience-methodology-demo-v2-0cdf49
> Methodology version: v2.0 (multi-horizon prescience against v1.6.2 corpus)
> Publication date: 2026-06-18
> Supersedes: 2026-kastner-prescience-methodology-demo-0cdf48 (v1.0, 2026-05-16)
> Author: Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect)

---

## Original Document Text

---
title: "A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 — Multi-Horizon)"
slug: 2026-kastner-prescience-methodology-demo-v2-0cdf49
page_type: theme
tier: 1
study_type: methodology-demonstration
audience: industry-analyst-peers
tags: [type/theme, type/methodology, theme/prescience-attribution, theme/archive-as-instrument, theme/multi-horizon]
date_built: 2026-05-16
date_regenerated: 2026-06-18
methodology_version: v2.0
build_software: perplexity-computer
sources_per_anchor_min: 3
primary_sources_per_anchor_min: 1
inclusion_threshold_studies: 10
attribution_formula: "lead × contrarian × specificity / 250, clamped [0.02, 0.80]"
prescience_horizons: ["overall", "3yr", "5yr"]
---

# A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive

> **Note on framing.** This page is not a biography. It is a methodology demonstration showing how the [[_index|Kastner IT Research Archive]] can be used as a primary-source research instrument. The case study happens to be Peter S. Kastner's own analyst output (1979–present); the question being answered — *how do you defensibly quantify the economic value of a body of analyst prescience?* — is the actual subject. Readers are invited to replicate, extend, or refute the result using the open data, named DuckDB views, and explicit formulas documented below.

> **v2.0 methodology refresh (2026-06-18).** This regeneration runs the methodology against the v1.6.2 corpus (1,452 studies / 23,926 observations / 865 high-prescience studies) and adds two horizon-specific prescience cuts (3-year and 5-year) alongside the original overall score. Dollar figures from the v1.0 worked example (2026-05-16, against the 933-study v1.4 corpus) are marked `$TBD (v2.0 recompute pending)` throughout — the structural methodology stands, but per-theme dollar anchors require fresh source triangulation against the expanded study pool before publication.

---

## Abstract

Using the 1,452-study Kastner IT Research Archive (23,926 structured observations, 865 high-prescience studies under the `prescience_max ≥ 4` rule), we demonstrate a reproducible methodology for attributing economic value to analyst forecasts. We cluster all technology-tagged high-prescience studies into 15 inclusion-threshold themes (≥10 studies per theme) and a long tail of below-threshold rollup themes. For each headline theme we build a 2026-dollar cumulative-value anchor using ≥3 independent sources with ≥1 primary source (IDC tracker, Gartner forecast, SEC 10-K, BLS CPI-U, or named market authority). We then apply a transparent share-of-prescience discount based on lead time, contrarian-vs-consensus position, and specificity of the call. Sensitivity analysis stress-tests every anchor against a low/mid/high band. **v2.0 adds two horizon-specific score columns (`score_3yr`, `score_5yr`) alongside the original `score_overall`**, enabling the same theme set to be re-attributed at near-term (3-year) and medium-term (5-year) horizons in addition to the open-ended verdict.

**Result of the v1.0 worked example (against 466 studies, 2026-05-16):** $10.9 trillion mid net-attributed cumulative value in 2026 USD, with a defensible sensitivity band of $8.8T–$13.4T. Gross unweighted total was $41.3T. The mid figure represented 26.4% share-of-prescience attribution of the gross.

**Status of the v2.0 worked example (against 865 studies, 2026-06-18):** Per-theme dollar anchors are flagged `$TBD (v2.0 recompute pending)` — see §11. The 85% expansion in the high-prescience pool (466 → 865) materially changes per-theme membership and likely raises the gross totals proportionally before share-of-prescience discounts are re-applied. A Pete-authored recompute pass against the new pool is the prerequisite for publishing v2.0 dollar figures.

**Result of the methodology demonstration:** The archive can be queried as a structured database (Parquet + DuckDB), themes can be derived programmatically from `v_studies_with_high_prescience` and tech tags, and every claim in this study is reproducible from the open data plus three sources of triangulation per anchor. The multi-horizon extension shows the same archive supports both retrospective open-ended verdicts and forward-looking time-windowed scoring without restructuring.

---

## 1. Motivation

Quantifying the economic value of analyst prescience is rare in the industry-research literature. Most retrospectives are anecdotal ("I called the cloud in 1998") or hagiographic. The harder questions — *how much of the eventual market does the analyst deserve credit for forecasting?* and *what does the cumulative value look like in defensible 2026 dollars?* — require a methodology that can withstand a hostile reviewer.

A second pressure point is **time horizon**. A prescient call made in 1998 about cloud computing materialized 8–10 years later (2006 AWS launch, 2008 Salesforce IPO); a prescient call made in 2003 about smartphones materialized 4–6 years later (2007 iPhone). Holding both under a single "did it come true" verdict erases the operational difference between *near-term tactical foresight* and *medium-term strategic foresight*. v2.0 splits these out via `score_3yr` and `score_5yr`.

This study demonstrates such a methodology, applied as a case study to the Kastner archive. It is meant to be reused: a future researcher could substitute any well-structured analyst archive (Forrester, Gartner, IDC author archives, NBER working papers) and produce a comparable estimate.

## 2. Data

### 2.1 The archive as instrument

The archive is shipped as three interlocking layers:

| Layer | Path | Format | Purpose |
|---|---|---|---|
| Wiki | `wiki/` | Obsidian Markdown | Human navigation, [[wikilinks]], YAML frontmatter |
| Data | `data/` | Parquet | Columnar query layer |
| Database | `db/kastner.duckdb` | DuckDB | Named views over Parquet |

### 2.2 Relevant DuckDB views

```sql
-- Used in this study:
SELECT * FROM v_studies_with_high_prescience;        -- 865 rows (prescience_max ≥ 4)
SELECT * FROM v_studies_by_decade;                   -- decade rollups
SELECT * FROM v_observations_by_year;                -- yearly time series
SELECT * FROM v_prescience_summary;                  -- prescience distribution
```

**Note on v_studies column names** (see `kastner-archive-pipeline` skill v1.7 Gotcha 11/12): the authored study-level verdict is exposed as `study_prescience_enum` (NOT `prescience`), and the bucket-type column is `type` (NOT `collection_type`). The per-observation columns `prescience_max`, `prescience_mean`, `prescience_obs_count` are computed alongside the authored verdict, not in place of it (Gotcha 10 — Phase 1 pass-through preserves Path B rebuttals).

**Per-observation horizon columns added in v1.6.2** (`_master_prescience_scores.csv`): `score_overall` (1–5, the original column), `score_3yr` (1–5, materialization within 3 years), `score_5yr` (1–5, materialization within 5 years). Total rows in `_master_prescience_scores.csv` after Tier B promote: 17,085.

### 2.3 Universe summary (v1.6.2 corpus)

| Layer | Count | Notes |
|---|---|---|
| Studies in archive | **1,452** | +519 vs. v1.4 |
| Observations | **23,926** | +4,751 vs. v1.4 |
| Authored verdict `high` (study-level) | **498** | new in v1.6.2 release; canonical for Path B |
| High-prescience studies (`prescience_max ≥ 4`) | **865** | +399 vs. v1.4 — this study's analytical population |
| High-prescience studies (`prescience_mean ≥ 3.5`) | 115 | stricter mean-anchored cut; for sensitivity |
| Technology-tagged subset (used in this study) | TBD (v2.0 recompute) | v1.0 was 386/466 |
| Themes meeting threshold (≥10 studies) | 15 | unchanged from v1.0 (expanded membership) |
| Below-threshold rollup themes | 20+ | new candidates expected from expansion |
| Out-of-scope (not technology) | TBD (v2.0 recompute) | v1.0 was 36 |

**Pool selection rationale.** The 865-study `prescience_max ≥ 4` cut is the canonical analytical population, matching the v1.0 methodology's anchor. The 498 authored-high count and the 115 mean-anchored count are tracked for sensitivity in §11 but not used as primary inputs — the max-anchored cut admits any study where at least one observation cleared the 4-point threshold, which is the most inclusive defensible frame for "prescient at the call level."

## 3. Methods

### 3.1 Theme classification (Phase 1)

We applied priority-ordered tagging to the technology-tagged subset to resolve overlap collisions (e.g., AI/E-Commerce/Java studies that touch multiple themes). Pseudocode:

```python
THEME_PRIORITY = [
    "ai-ml-infrastructure",          # below threshold in v1.0; expected at threshold in v2.0
    "cloud-saas",
    "mobile-smartphone",
    "digital-consumer-tech",
    # ... (15 headline themes in resolution order)
]
for study in high_prescience_studies:
    for theme in THEME_PRIORITY:
        if matches(study, theme_tags[theme]):
            assign(study, theme)
            break
```

Coverage in v1.0: **99.4%** of 466 high-prescience studies were classified. Coverage in v2.0: TBD (v2.0 recompute pending). The 0.6% residual (3 studies in v1.0) was out-of-scope (purely industry-financial, no technology content) and the same pattern is expected to dominate v2.0 residuals.

### 3.2 Cumulative market value (Phase 2)

For each headline theme we built a year-by-year market-size series, then summed it across the **decade of materialization** in 2026-CPI dollars:

```
inflator(year) = CPI_U[2026] / CPI_U[year]    # CPI_U 2026 = 332.407 (BLS April 2026)
value_2026(year) = market_size(year) × inflator(year)
cumulative_theme = Σ value_2026(year) for year in materialization_decade
```

**Anchor interpolation:** linear between known data points; zero before the first verified anchor year. This is conservative — it does not extrapolate beyond observed evidence.

**E-commerce outlier fix:** The naive GMV interpretation of e-commerce yields >$150T cumulative — clearly an outlier because GMV represents the total flow of goods through e-commerce platforms, not the platform-software revenue attributable to the prescient analyst call. We replaced GMV with **platform software revenue** (Shopify, Adobe Commerce, Salesforce Commerce Cloud, BigCommerce, plus the long tail), reducing the theme from ~$158T to $159B cumulative in v1.0.

**DCT narrow-scope fix:** Digital Consumer Technology, taken broadly, includes traditional white-goods consumer electronics ($1.1T/yr). The prescient call was about *digital* sub-segments (smartphones-as-cameras, smart wearables, smart TVs, connected audio), which sums to ~$180B/yr in 2025. We use the narrow definition, reducing the theme from $21T to $4.75T cumulative in v1.0.

### 3.3 Source rigor (Phase 3)

Every market-size anchor cites ≥3 independent sources, with ≥1 primary source from the following whitelist:

- IDC trackers (containerId prefix `prUS` or `US`)
- Gartner Magic Quadrants or named forecasts
- SEC 10-K segment data (for company-attributable estimates)
- BLS CPI-U series for inflation adjustment
- Named-source benchmark consortia (TPC Council, SPEC)

Cross-source discrepancies are documented inline (see §6, definition-mismatch flags).

### 3.4 Share-of-prescience attribution (Phase 4)

Each theme receives an attribution factor based on three 1–5 scored dimensions:

| Dimension | Scoring rule |
|---|---|
| **Lead time** | 1 (≤1y before materialization), 2 (2–3y), 3 (4–5y), 4 (6–8y), 5 (>8y) |
| **Contrarian** | 1 (consensus view), 2 (mildly contrarian), 3 (against the analyst herd), 4 (strongly contrarian), 5 (polar opposite — most analysts wrong) |
| **Specificity** | 1 (vague theme), 2 (named theme), 3 (named theme + rough size), 4 (named winners), 5 (named winners + numbers + dates) |

Formula:

```
attribution_factor = clamp( lead × contrarian × specificity / 250, 0.02, 0.80 )
net_attributed = gross_cumulative × attribution_factor
```

The denominator (250) is calibrated so a maximum 5×5×5 product yields a 50% attribution share (with the soft cap at 80%) — i.e., even the most prescient possible call earns at most half the cumulative market in this framework. A consensus-view 1×1×1 call earns the 2% floor, acknowledging that even consensus analyst coverage contributes some value (research is not zero-value when it confirms a thesis).

### 3.5 Sensitivity (Phase 5)

For each theme we re-ran the attribution using low/mid/high market-size multipliers derived from the actual source spread in the Phase 3 table. The low multiplier corresponds to the smallest defensible source; high to the largest; mid to the IDC/Gartner/SEC anchor.

Sensitivity is reported as a tornado chart (see §5.3) ordered by absolute range of net attributed value, so reviewers can immediately identify which themes drive uncertainty.

### 3.6 Multi-horizon scoring (Phase 6 — new in v2.0)

v1.6.2 added two horizon-specific score columns alongside the original. Each observation in `_master_prescience_scores.csv` now carries three independent prescience scores (1–5) against the same rubric, evaluated at three time horizons:

| Column | Horizon | Question being scored |
|---|---|---|
| `score_overall` | Open-ended | Did the prediction come true *ever*, on any timescale? |
| `score_3yr` | 3 years from prediction date | Did the prediction materialize within 3 years? |
| `score_5yr` | 5 years from prediction date | Did the prediction materialize within 5 years? |

Theme-level horizon rollup: for each of the 15 headline themes, we compute the share of member observations scoring `≥4` on each horizon column. A theme dominated by `score_5yr ≥ 4` reflects medium-term strategic foresight (e.g., RDBMS, ERP); a theme dominated by `score_3yr ≥ 4` reflects near-term tactical foresight (e.g., OLTP/TPC, Windows NT); a theme strong on `score_overall` but weak on both timed horizons reflects long-term visionary calls that took >5 years to materialize (e.g., Cloud Computing, Mobile/Smartphone).

The horizon scores feed into a refined attribution at Phase 4: the lead-time dimension is no longer reviewer-judged but read from the actual horizon-bucket distribution. A theme where 80% of observations are `score_3yr ≥ 4` gets lead-time score 2; a theme where 80% are `score_5yr ≥ 4` but `score_3yr < 4` gets lead-time score 3; a theme where neither timed horizon scores ≥4 but `score_overall ≥ 4` gets lead-time score 4 or 5 (medium-to-long-term). This removes one source of reviewer-subjectivity criticism leveled at v1.0.

## 4. Inclusion criteria & themes

### 4.1 Threshold rationale

We adopted a **10-study threshold** for headline themes after the user (Peter Kastner) requested: *"2 threshold at 10 plus roll up plus note on what is in roll up for future analysis."* The rationale is methodological: ≥10 studies in a single theme indicates sustained analyst coverage rather than a one-off call. Below-threshold themes are tracked separately in §4.3 for future researchers.

In v2.0, the 85% expansion in the high-prescience pool (466 → 865) is expected to promote several previously-below-threshold themes into the headline set. AI/ML Infrastructure (8 studies in v1.0, narrowly below threshold) is the most consequential candidate. v2.0 keeps the same 10-study threshold so the v1.0 ↔ v2.0 comparison is apples-to-apples on theme inclusion criteria.

### 4.2 Headline themes (15, v1.0 — membership counts to be re-derived in v2.0)

| # | Theme | Decade | First predict | v1.0 study count | v2.0 study count | Tagged tech anchors |
|---|---|---|---|---|---|---|
| 1 | [[theme-mainframes-midrange\|Fault-Tolerant / High-Availability Servers]] | 1980s | 1981 | 12 | TBD | Stratus, Tandem, Sequoia |
| 2 | [[theme-databases\|OLTP / TPC-Benchmarked Transaction Processing]] | 1990s | 1985 | 14 | TBD | TPC-A, TPC-C, DEC Rdb |
| 3 | [[theme-databases\|Relational Databases (RDBMS)]] | 1990s | 1991 | 17 | TBD | Oracle, DB2, SQL Server |
| 4 | [[theme-personal-computers-os\|Desktop PC / Windows Client]] | 1990s | 1994 | 31 | TBD | Windows 95/XP, AMD K7 |
| 5 | [[theme-networking-internet\|Enterprise Networking (IP/VoIP)]] | 1990s | 1996 | 22 | TBD | Cisco, MPLS, SIP |
| 6 | [[theme-personal-computers-os\|Windows NT / Server OS]] | 1990s | 1992 | 15 | TBD | NT 3.5, NT 4.0, Win2K |
| 7 | [[theme-erp-enterprise-apps\|Enterprise Resource Planning (ERP)]] | 1990s | 1993 | 19 | TBD | SAP R/3, PeopleSoft, Oracle Apps |
| 8 | [[theme-programming-dev-tools\|Java / Web Application Platforms]] | 1990s | 1996 | 13 | TBD | J2EE, WebLogic, WebSphere |
| 9 | [[theme-unix-open-systems\|Linux / Open Source Server OS]] | 2000s | 1998 | 18 | TBD | Red Hat, SUSE, Caldera |
| 10 | [[theme-soa-bpm-integration\|SOA / Web Services / API Management]] | 2000s | 2003 | 14 | TBD | XML, SOAP, REST, MuleSoft |
| 11 | [[theme-storage-hardware\|Enterprise Storage / ILM]] | 2000s | 1998 | 11 | TBD | EMC, NetApp, SATA midline |
| 12 | Digital Consumer Tech / Globalized Supply Chain | 2000s | 2002 | 21 | TBD | iPod, smartphones-as-cameras, Foxconn |
| 13 | E-Commerce Platform Software | 2000s | 1996 | 16 | TBD | Shopify, Adobe Commerce, BigCommerce |
| 14 | Cloud Computing & SaaS | 2010s | 1998 | 28 | TBD | AWS, Salesforce, Azure |
| 15 | Mobile / Smartphone Computing | 2010s | 2001 | 24 | TBD | iPhone, Android, ARM SoC |

**v2.0 recompute step.** Pete-driven theme re-derivation against the 865-study pool is required to populate the "v2.0 study count" column. The methodology is unchanged; only the pool changed.

### 4.3 Below-threshold rollup themes (v1.0: 20 themes) — for future researchers

The following themes had meaningful prescient coverage (1–9 studies in v1.0) but did not meet the 10-study inclusion threshold. They are documented here as an explicit invitation to future researchers — particularly the **AI/ML Infrastructure cluster (8 studies in v1.0, 2020s)** which narrowly missed inclusion in v1.0 and is expected to clear the threshold in v2.0.

| Theme | v1.0 count | v2.0 count | Decade | Future-research priority |
|---|---|---|---|---|
| **AI/ML Infrastructure** | 8 | TBD (expected ≥10) | 2020s | **High — expected to promote into headline set in v2.0** |
| Client-Server Computing | 9 | TBD | 1990s | Medium — partially captured by RDBMS + NT themes |
| x86-64 Server | 9 | TBD | 2000s | Medium — partially captured by Linux + Cloud themes |
| Consumer Electronics / Digital Media | 5 | TBD | 2000s | Low — overlaps DCT theme |
| Wireless 802.11 / Wi-Fi | 5 | TBD | 2000s | Medium |
| Tech-Sector Financial Analysis Methodology | 3 | TBD | 1980s | Medium — methodological prescience, hard to size |
| Y2K | 3 | TBD | 1990s | Low — narrow window |
| CRM | 3 | TBD | 2000s | High — clean theme, just below threshold |
| BI / Decision Support | 3 | TBD | 2000s | Medium |
| IT Outsourcing | 3 | TBD | 2000s | Low |
| Security / Trusted Computing | 3 | TBD | 2010s | Medium |
| EAI / Middleware | 2 | TBD | 1990s | Low — overlaps SOA |
| E-Learning | 2 | TBD | 2000s | Low |
| Videoconferencing | 2 | TBD | 2010s | Medium |
| Smart Grid / IoT | 2 | TBD | (from 1979!) | High — exceptional lead time |
| SMP / Parallel Computing | 1 | TBD | 1990s | Low |
| SAN / Fibre Channel | 1 | TBD | 2000s | Low |
| ITSM | 1 | TBD | 2000s | Low |
| Tape Archival | 1 | TBD | 2000s | Low |
| Tablet Computing | 1 | TBD | 2010s | Low |

### 4.4 Out-of-scope studies

The remaining high-prescience studies were classified as out-of-scope for this technology-themed analysis. v1.0 had 36 OOS studies, predominantly:
- Industry-financial analysis (M&A, valuation, capital markets) — 19 studies
- Strategic/management commentary not tied to a specific technology — 12 studies
- Vendor-specific operational forecasts (without broader technology generalization) — 5 studies

These are still valuable archive content but cannot be sized via market-anchor methodology. v2.0 OOS count is TBD pending recompute.

## 5. Results

### 5.1 Headline result

**v1.0 (2026-05-16, against 466 studies):**

| | Low | **Mid** | High | Range |
|---|---|---|---|---|
| **Net attributed (2026 USD)** | **$8.8T** | **$10.9T** | **$13.4T** | $4.6T |
| Gross unweighted (2026 USD) | $34.5T | $41.3T | $48.1T | $13.7T |
| Overall attribution share | 25.5% | **26.4%** | 27.9% | — |

**v2.0 (2026-06-18, against 865 studies):** `$TBD (v2.0 recompute pending)`.

The structural expectation is that gross totals scale roughly with pool size (466 → 865 ≈ +85%, suggesting gross ~$76T mid pre-attribution), but per-theme attribution factors may shift as the share-of-prescience discount reflects the expanded membership. Net attributed total at v2.0 is bounded below by v1.0's $8.8T and above by a naive pool-scaling estimate of ~$25T. The Pete-authored recompute pass against the new pool is the prerequisite for narrowing this range.

### 5.2 Per-theme breakdown (v1.0, retained for reference)

Sorted by net attributed value (mid estimate). **All v2.0 dollar figures `$TBD (v2.0 recompute pending)`.**

| # | Theme | v1.0 Mid gross $B | v1.0 Attr % | v1.0 Mid net $B | v1.0 Lead | v1.0 Contrarian | v1.0 Specificity |
|---|---|---|---|---|---|---|---|
| 1 | Cloud Computing & SaaS | 7,696 | 40% | **3,078** | 5 | 5 | 4 |
| 2 | Mobile / Smartphone | 8,914 | 32% | **2,853** | 4 | 4 | 5 |
| 3 | Digital Consumer Tech | 4,751 | 32% | **1,520** | 4 | 4 | 5 |
| 4 | OLTP / TPC | 1,849 | 50% | **925** | 5 | 5 | 5 |
| 5 | Desktop PC / Windows Client | 9,650 | 6% | **618** | 2 | 2 | 4 |
| 6 | Enterprise Networking | 1,894 | 32% | **606** | 4 | 4 | 5 |
| 7 | RDBMS | 1,888 | 14% | **272** | 3 | 3 | 4 |
| 8 | Enterprise Storage / ILM | 921 | 24% | **221** | 4 | 3 | 5 |
| 9 | Windows NT / Server OS | 619 | 32% | **198** | 4 | 4 | 5 |
| 10 | ERP | 1,622 | 12% | **195** | 3 | 2 | 5 |
| 11 | Fault-Tolerant Servers | 347 | 40% | **139** | 5 | 4 | 5 |
| 12 | Linux | 307 | 40% | **123** | 4 | 5 | 5 |
| 13 | Java / Web App Platforms | 515 | 14% | **74** | 3 | 3 | 4 |
| 14 | SOA / API Management | 150 | 40% | **60** | 5 | 4 | 5 |
| 15 | E-Commerce Platform Software | 159 | 24% | **38** | 4 | 3 | 5 |
| | **v1.0 TOTAL (15 themes)** | **41,283** | **26.4%** | **10,919** | | | |

Three observations from v1.0 (retained):

1. **Top 4 themes contribute 78%** of net attributed value (Cloud, Mobile, DCT, OLTP). These are the calls where lead × contrarian × specificity was maxed out and the eventual market was large.
2. **High-attribution but small markets** (Linux, SOA, Fault-Tolerant) demonstrate that the methodology rewards specificity even when total market is modest — preventing the result from being dominated purely by market size.
3. **Low-attribution but large markets** (Desktop PC, ERP) demonstrate the share-of-prescience discount working as intended — when the analyst joined an already-established consensus, the discount drops attribution to 6–12%.

### 5.3 Sensitivity

![Sensitivity tornado chart](attachments/phase5_tornado.png)

**Largest uncertainty drivers in v1.0** (by absolute range of net attributed):

| Theme | v1.0 Range $B | Cause |
|---|---|---|
| Digital Consumer Tech | 1,779 | DCT scope ($90B narrow ↔ $300B broad-with-tablets-and-connected-TV) |
| OLTP / TPC | 1,507 | No clean modern proxy ($50B narrow RDBMS slice ↔ $170B broad DBMS+middleware+benchmark-tracked) |
| Cloud Computing & SaaS | 646 | $723B Gartner Public Cloud ↔ $913B CloudZero TCV |
| Enterprise Storage / ILM | 150 | $33B IDC enterprise storage ↔ $10.5B OpenText/Radicati narrow archiving |

**Stable themes in v1.0** (range <$60B): Java, SOA, Desktop PC, RDBMS, Mobile. These have tight source consensus.

v2.0 sensitivity recompute pending.

### 5.4 Multi-horizon attribution (NEW in v2.0)

This section is the structural addition that justifies v2.0. Once the recompute lands, it will populate three sub-tables corresponding to the three horizon columns.

**5.4.1 Overall horizon (open-ended)** — directly comparable to v1.0; uses `score_overall ≥ 4` rollup. Expected to closely track the v1.0 attribution totals (scaled to the 865-study pool).

| # | Theme | Members (`score_overall ≥ 4`) | Mid gross $B | Mid net $B |
|---|---|---|---|---|
| (1–15) | (per §4.2) | TBD | TBD | TBD |

**5.4.2 3-year horizon (near-term tactical foresight)** — uses `score_3yr ≥ 4` rollup. Expected leaders: OLTP/TPC, Windows NT, Enterprise Networking, ERP — themes where Kastner's calls were specific enough about contemporaneous shipping products that materialization happened within the next product cycle.

| # | Theme | Members (`score_3yr ≥ 4`) | Mid gross $B | Mid net $B |
|---|---|---|---|---|
| (1–15) | (per §4.2) | TBD | TBD | TBD |

**5.4.3 5-year horizon (medium-term strategic foresight)** — uses `score_5yr ≥ 4` rollup. Expected leaders: RDBMS, Java, SOA, E-Commerce Platform — themes where the prescient call required the industry to do 3–5 years of platform work before the prediction could be verified.

| # | Theme | Members (`score_5yr ≥ 4`) | Mid gross $B | Mid net $B |
|---|---|---|---|---|
| (1–15) | (per §4.2) | TBD | TBD | TBD |

**5.4.4 Beyond-5-year (long-term visionary foresight)** — derived: `score_overall ≥ 4 AND score_3yr < 4 AND score_5yr < 4`. Expected leaders: Cloud Computing, Mobile/Smartphone, Linux, Fault-Tolerant Servers — themes where Kastner's calls preceded materialization by 6+ years, and the share-of-prescience discount appropriately rewards the long lead time.

| # | Theme | Members (overall-only) | Mid gross $B | Mid net $B |
|---|---|---|---|---|
| (1–15) | (per §4.2) | TBD | TBD | TBD |

**Analytical contribution of the horizon split.** A skeptical reviewer of v1.0 could argue that the lead-time dimension in the attribution formula (3.4) was scored subjectively. v2.0 grounds lead-time in the horizon-column distributions themselves: if 80% of a theme's observations score `≥4` on `score_3yr`, the theme objectively earned lead-time score 2; if 80% score `≥4` on `score_5yr` but not on `score_3yr`, the theme earned lead-time score 3; if the only `≥4` scores are on `score_overall`, the theme earned lead-time score 4 or 5. This replaces reviewer judgment with a data-driven cut on the same `_master_prescience_scores.csv` rows the headline result already depends on.

## 6. Limitations & definition-mismatch transparency

The v1.0 five themes with documented definition mismatches are retained as starting points for v2.0 recompute:

| # | Theme | v1.0 Mismatch |
|---|---|---|
| 1 | OLTP / TPC | No clean modern proxy. Embedded in DBMS + transaction-processing-middleware + benchmark-tracked workload categories. Anchor of $75B 2025 was ~90% of RDBMS transactional share. |
| 2 | Linux Enterprise | $20–26.4B range reflects scope: Fortune BI's $26.4B includes hardware-bundle; narrower software-only definitions land $20B. |
| 3 | Enterprise Storage / ILM | $33B IDC enterprise storage tracker vs. $10.5B narrow archiving (OpenText/Radicati). |
| 4 | Digital Consumer Tech | Narrow ($180B/yr) vs. broad-CE ($1.1T/yr) — narrow chosen per outlier-rejection methodology. |
| 5 | Windows NT / Server OS | $27B Microsoft-attributable on-prem Windows Server licenses (FY25 10-K segment) vs. $366B total server hardware (with bundled OS). |

Other limitations (v1.0, mostly retained for v2.0):

- **Lead-time scoring was reviewer-judged in v1.0.** v2.0 replaces reviewer judgment with horizon-column distribution (see §3.6 and §5.4). This addresses the largest review surface.
- **Contrarian scoring requires reading the period analyst literature.** A skeptical reviewer could re-score contrarian factor down for any theme where consensus formed earlier than credited. This limitation is unchanged in v2.0; only lead-time was de-subjectivized.
- **Cumulative-value method is conservative.** We sum only the decade of materialization, not subsequent decades when the technology continued to generate revenue. A more aggressive cumulative-through-2026 approach would roughly double the gross totals. Unchanged.
- **Attribution formula is opinionated.** The choice of `lead × contrarian × specificity / 250` with [2%, 80%] clamping reflects a particular philosophy. Alternative formulations (additive, log-scale, Bayesian) would yield different totals. Unchanged.
- **Below-threshold themes are uncounted.** Adding the 20+ rollup themes (especially AI/ML Infrastructure, CRM, Smart Grid/IoT — all expected to grow in v2.0) would add an estimated $0.5T–$2T to the v1.0 net attributed total. v2.0 should re-estimate this.
- **Authored verdict vs. observation-derived count divergence.** The v1.6.2 corpus has 498 authored `study_prescience_enum='high'` but 865 studies clearing `prescience_max ≥ 4`. This study uses the 865 cut. A future v2.1 could re-run against the stricter 498 authored cut for sensitivity, or against the 115 `prescience_mean ≥ 3.5` cut for the most conservative read.

## 7. Replication appendix

This section is for grad students, analyst peers, or anyone who wants to reproduce or extend the result.

### 7.1 Pull the prescient studies yourself

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)

# All 865 high-prescience studies (max-anchored, v1.6.2)
df = con.execute("""
  SELECT study_id, date, title, study_prescience_enum, study_prescience_rationale,
         prescience_max, prescience_mean, prescience_obs_count
  FROM v_studies_with_high_prescience
  ORDER BY date
""").df()

# Theme-tagged subset (technology breadth)
tech_df = con.execute("""
  SELECT s.study_id, s.date, s.title, s.study_prescience_enum,
         s.prescience_max, s.prescience_mean
  FROM v_studies_with_high_prescience s
  JOIN v_observations o ON o.study_id = s.study_id
  WHERE o.technology_id IS NOT NULL
""").df()
```

**v1.6.2 column-name note.** The authored study verdict is `study_prescience_enum` (NOT `prescience`) and the rationale is `study_prescience_rationale` (NOT `prescience_rationale`). These were renamed during the Phase 1 pass-through for Path B rebuttal preservation — the raw master CSV retains the original `prescience`/`prescience_rationale` headers.

### 7.2 Pull the multi-horizon scores (new in v2.0)

```python
# Horizon-bucketed observations
horizons = con.execute("""
  SELECT o.study_id, o.obs_id,
         p.score_overall, p.score_3yr, p.score_5yr
  FROM v_observations o
  JOIN _master_prescience_scores p USING (obs_id)
  WHERE p.score_overall IS NOT NULL
""").df()

# Theme-level horizon rollup (example: count members of each horizon bucket per theme)
horizons["overall_high"] = (horizons["score_overall"] >= 4).astype(int)
horizons["near_term"]    = (horizons["score_3yr"]     >= 4).astype(int)
horizons["medium_term"]  = (horizons["score_5yr"]     >= 4).astype(int)
```

### 7.3 Build your own theme

```python
# Example: re-create the Cloud Computing & SaaS theme
cloud_keywords = ["cloud", "utility", "grid computing", "saas", "asp", "salesforce"]
cloud_studies = tech_df[tech_df["title"].str.lower().str.contains("|".join(cloud_keywords))]
print(f"Cloud theme: {len(cloud_studies)} studies")
```

### 7.4 Recompute attribution

```python
def attribution_factor(lead, contrarian, specificity):
    """Returns share-of-prescience factor in [0.02, 0.80]."""
    raw = (lead * contrarian * specificity) / 250
    return max(0.02, min(0.80, raw))

# v2.0: derive lead from horizon distribution rather than reviewer judgment
def horizon_lead(theme_obs):
    """Compute lead-time score from horizon-column distribution."""
    n = len(theme_obs)
    pct_3yr = (theme_obs["score_3yr"] >= 4).sum() / n
    pct_5yr = (theme_obs["score_5yr"] >= 4).sum() / n
    pct_overall = (theme_obs["score_overall"] >= 4).sum() / n
    if pct_3yr >= 0.5:    return 2  # near-term tactical
    if pct_5yr >= 0.5:    return 3  # medium-term strategic
    if pct_overall >= 0.5: return 5  # long-term visionary
    return 4                          # mixed / 6–8y typical

# Example: re-score with stricter contrarian factor
new_attr = attribution_factor(lead=5, contrarian=3, specificity=4)  # 24% instead of 40%
```

### 7.5 Replace an anchor

```python
import json
with open("data/value_table.json") as f:
    anchors = json.load(f)

# Substitute your own 2025 anchor for Cloud Computing
anchors["cloud-saas"]["anchor_2025_b"] = 1000  # your number here
# Re-run cumulative summation, apply attribution, observe new total
```

### 7.6 Add a below-threshold theme

The CRM theme (3 studies in v1.0, just below threshold) is a clean candidate; AI/ML Infrastructure (8 studies in v1.0, expected to clear threshold in v2.0) is the highest-priority target:
- Pull the studies via `SELECT ... WHERE study_id IN (...)` (specific IDs in `phase1_final.json`)
- Build market anchor: e.g., Gartner CRM forecast 2024 = $96B; IDC AI infrastructure 2025 = $200B
- Score: lead, contrarian, specificity per §3.4 (or derive lead from horizon distribution per §3.6)
- Attribution: apply formula
- Decade-of-materialization sum → net attributed

### 7.7 Code & data manifest

| Artifact | Path | Description |
|---|---|---|
| Final theme classification (v1.0) | `phase1_final.json` | 15 headline + 20 rollup + 36 OOS, against 466 studies |
| Final theme classification (v2.0) | `phase1_final_v2.json` | TBD — to be regenerated against 865 studies |
| Cumulative value table | `value_table.json` | Per-theme decade-of-materialization sums |
| Source triangulation | `phase3_source_table.md` | 3+ sources per theme, ≥1 primary |
| Attribution scoring | `phase4_attributed.json` | Per-theme lead/contrarian/specificity + factor + rationale |
| Horizon rollup (v2.0) | `phase6_horizon_rollup.json` | TBD — per-theme `score_overall`/`score_3yr`/`score_5yr` distributions |
| Sensitivity bands | `phase5_sensitivity.json` | Low/mid/high net attributed per theme |
| Sensitivity chart | `phase5_tornado.png` | Tornado visualization |

All artifacts are in the source archive at `shorttack/aberdeen-group-archive` under the relevant phase tags.

## 8. Discussion: what this demonstrates about the archive

The methodology demonstration shows that the Kastner archive supports research questions of four distinct types (one added in v2.0):

1. **Aggregate counting** (Phase 1): "How many high-prescience studies are there by decade and theme?" — answerable in seconds via DuckDB views.
2. **Anchored quantification** (Phases 2–3): "What is the 2026-dollar market size of the technologies Kastner correctly forecast?" — requires triangulating with external sources, but the archive supplies the universe of forecast claims.
3. **Attribution analysis** (Phases 4–5): "What share of that value is attributable to the prescience itself versus the natural emergence of the technology?" — requires reading prescience rationales (`study_prescience_rationale` column) plus period analyst literature.
4. **Horizon decomposition** (Phase 6, NEW v2.0): "How much of the prescient value reflects near-term tactical foresight (3-year) vs. medium-term strategic foresight (5-year) vs. long-term visionary foresight (beyond 5 years)?" — answerable directly from the `score_3yr`/`score_5yr`/`score_overall` columns in `_master_prescience_scores.csv`.

The same four-type structure applies to any analyst archive. Forrester's, Gartner's, IDC's individual-author archives, or even academic forecast literature (e.g., NBER working papers) could be subjected to comparable analysis if structured to expose `prescience` (or equivalent) AND horizon-bucketed scores as queryable fields.

## 9. Open questions for future researchers

1. **AI/ML Infrastructure deep sweep.** v1.0 had 8 studies (below threshold); v2.0 corpus expansion likely promotes this to a headline theme. The deep sweep against the 865-study pool is the highest-leverage v2.0 task.
2. **Below-threshold roll-up under v2.0.** Quantify the 20+ rollup themes as a group; v1.0 estimated $0.5T–$2T additional net attributed; v2.0 expansion may double this.
3. **Alternative attribution formulas.** Compare multiplicative (used here), additive, log-scale, and Bayesian approaches. The choice substantially affects which themes dominate.
4. **Cross-archive comparison.** Apply the same methodology to a peer analyst's archive (Forrester, Gartner) and benchmark.
5. **Cumulative-through-present scope.** Re-run with cumulative summation extended through 2026 (not just decade-of-materialization), which would roughly double gross totals.
6. **Specificity de-aggregation.** Score specificity at study-level rather than theme-level; surface the single most specific high-impact studies.
7. **Authored verdict vs. observation-derived count divergence.** Run a sensitivity pass at the 498 authored cut and the 115 mean-anchored cut to bracket the methodology's robustness.
8. **Horizon-rubric refinement.** The current `score_3yr` / `score_5yr` rubric uses a binary `≥4` threshold. A continuous-weight alternative (e.g., linearly weighted by score on each horizon) may surface intermediate-horizon themes that the binary cut overlooks.

## 10. Provenance

| Field | Value |
|---|---|
| Build date (v1.0) | 2026-05-16 |
| Regeneration date (v2.0) | 2026-06-18 |
| Build software | Perplexity Computer (Claude Sonnet 4.6) |
| Archive commit (v1.0) | `8d00ab5` |
| Archive commit (v2.0 regen target) | `a472cc4f` (v1.6.2 release) |
| Studies queried (v1.0) | 466 (high-prescience subset of 933) |
| Studies queried (v2.0) | 865 (high-prescience subset of 1,452) |
| Sources cited (Phase 3, v1.0) | 60+ across 15 themes |
| Inflation index | BLS CPI-U April 2026 = 332.407 |
| Methodology version | v2.0 (multi-horizon) |
| Reviewer | Peter S. Kastner (study subject; methodology approved at each phase checkpoint) |

## 11. v2.0 recompute checklist (Pete-driven, dollar figures pending)

The structural regeneration (this document) ships the v2.0 framework — multi-horizon scoring, refined lead-time derivation, expanded universe summary, horizon decomposition section (§5.4). The per-theme dollar attributions require a Pete-authored recompute pass before publication. Items pending:

- [ ] Re-derive theme membership against the 865-study `prescience_max ≥ 4` pool (§4.2 v2.0 column)
- [ ] Compute below-threshold theme counts against the 865-study pool (§4.3 v2.0 column)
- [ ] Re-anchor the 15 headline themes against 2026 market sources (§5.2 v2.0 dollar figures)
- [ ] Run horizon rollup (§5.4) — group observations by theme and bucket by `score_3yr ≥ 4` / `score_5yr ≥ 4` / `score_overall ≥ 4` only
- [ ] Re-derive lead-time scores from horizon distributions (§3.6 → §3.4 inputs)
- [ ] Recompute attribution and sensitivity (§5.1, §5.3) under the new pool and refined lead-times
- [ ] Update OOS count (§4.4) against the 865-study pool
- [ ] Settle on whether AI/ML Infrastructure is promoted to a headline theme (§4.3 → §4.2)
- [ ] Replace all `$TBD (v2.0 recompute pending)` markers with the recomputed figures

Estimated effort: 4–8 hours of Pete-driven analytical work, depending on how much per-theme anchor research the v1.0 spreadsheet can be reused for.

---

## See also

- [[_index|Wiki index]] · [[_index-themes|All themes]] · [[_index-decades|By decade]] · [[_index-studies|Study list]]
- [[kastner-technology-breadth-memoir-2026|Breadth memoir]] (companion narrative)
- [[AGENTS|AGENTS.md]] (LLM-facing query guide)
- [[study-findings-prescience-decline-aberdeen-eras|Prescience decline by Aberdeen era]] (companion findings doc, pending sign-off)


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16; updated by v2.0 manual regen 2026-06-18

### Study Record

| Field | Value |
|-------|-------|
| study_id | 2026-kastner-prescience-methodology-demo-v2-0cdf49 |
| title | A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 — Multi-Horizon) |
| author | Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect) |
| date | 2026-06-18 |
| supersedes | 2026-kastner-prescience-methodology-demo-0cdf48 |
| type | topic-analysis |
| subject_domain | research-methodology |
| methodology | industry-analysis,attribution-modeling,multi-horizon-scoring,sensitivity-analysis,primary-source-triangulation,reproducibility-framework |
| methodology_version | v2.0 |
| source_file | kastner-author/2026-kastner-prescience-methodology-demo-v2-0cdf49/source/original_text.md |
| license | CC-BY-4.0 |

### Abstract

This 2026 methodology-demonstration study uses the 1,452-study Kastner IT Research Archive (23,926 structured observations, 865 high-prescience studies under the `prescience_max ≥ 4` rule) as a primary-source research instrument to develop and apply a reproducible methodology for attributing economic value to analyst prescience. Across 15 inclusion-threshold themes, the study triangulates every market-size anchor against three or more independent sources with at least one primary source (IDC, Gartner, SEC 10-K, BLS), then applies a share-of-prescience discount based on lead time, contrarian position, and specificity. v2.0 adds two horizon-specific score columns (`score_3yr`, `score_5yr`) alongside the original `score_overall`, enabling per-theme decomposition into near-term tactical, medium-term strategic, and long-term visionary foresight. The v1.0 worked example (against 466 studies, 2026-05-16) yielded $10.9 trillion cumulative net-attributed value in 2026 USD (sensitivity band $8.8T–$13.4T). The v2.0 worked example against the expanded 865-study pool is pending Pete-authored recompute. The result and the methodology are both intended for hostile peer review.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Sets precedent for archive-as-instrument: first study in the Kastner archive that demonstrates how the archive itself can be used for rigorous research. Defines the share-of-prescience attribution formula (lead × contrarian × specificity / 250) used for future archive analyses. v2.0 adds the multi-horizon decomposition framework. |
| **Relevance** | high | Methodology is immediately reusable for any structured analyst archive (Forrester, Gartner, IDC author archives). Provides replication appendix with DuckDB queries and Python code so future researchers can extend or refute the result. |
| **Prescience** | not-applicable | This study is a methodology-demonstration retrospective, not a forecast. It quantifies past prescience rather than making new predictions. |

### Prescience Detail

**Prediction 1:** Kastner predicted fault-tolerant-servers materialization
- **Claimed:** correct
- **Year:** 1981
- **Confidence at time:** verified

**Prediction 2:** Kastner predicted oltp-tpc materialization
- **Claimed:** correct
- **Year:** 1985
- **Confidence at time:** verified

**Prediction 3:** Kastner predicted rdbms materialization
- **Claimed:** correct
- **Year:** 1991
- **Confidence at time:** verified

**Prediction 4:** Kastner predicted desktop-pc-windows materialization
- **Claimed:** correct
- **Year:** 1994
- **Confidence at time:** verified

**Prediction 5:** Kastner predicted enterprise-networking materialization
- **Claimed:** correct
- **Year:** 1996
- **Confidence at time:** verified

**Prediction 6:** Kastner predicted windows-nt-server-os materialization
- **Claimed:** correct
- **Year:** 1992
- **Confidence at time:** verified

**Prediction 7:** Kastner predicted erp materialization
- **Claimed:** correct
- **Year:** 1993
- **Confidence at time:** verified

**Prediction 8:** Kastner predicted java-web-app-platforms materialization
- **Claimed:** correct
- **Year:** 1996
- **Confidence at time:** verified

**Prediction 9:** Kastner predicted linux materialization
- **Claimed:** correct
- **Year:** 1998
- **Confidence at time:** verified

**Prediction 10:** Kastner predicted soa-api-management materialization
- **Claimed:** correct
- **Year:** 2003
- **Confidence at time:** verified

**Prediction 11:** Kastner predicted enterprise-storage-ilm materialization
- **Claimed:** correct
- **Year:** 1998
- **Confidence at time:** verified

**Prediction 12:** Kastner predicted digital-consumer-technology materialization
- **Claimed:** correct
- **Year:** 2002
- **Confidence at time:** verified

**Prediction 13:** Kastner predicted e-commerce-platform-software materialization
- **Claimed:** correct
- **Year:** 1996
- **Confidence at time:** verified

**Prediction 14:** Kastner predicted cloud-saas materialization
- **Claimed:** correct
- **Year:** 1998
- **Confidence at time:** verified

**Prediction 15:** Kastner predicted mobile-smartphone materialization
- **Claimed:** correct
- **Year:** 2001
- **Confidence at time:** verified


### Entities Referenced (15)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| International Data Corporation (IDC) | firm | active |  |
| Gartner, Inc. | firm | active |  |
| U.S. Bureau of Labor Statistics | agency | active |  |
| U.S. Securities and Exchange Commission | agency | active |  |
| Transaction Processing Performance Council | institution | active |  |
| Microsoft Corporation | company | active |  |
| Shopify Inc. | company | active |  |
| Salesforce, Inc. | company | active |  |
| Adobe Inc. | company | active |  |
| Red Hat, Inc. (IBM subsidiary) | company | active | IBM (acquired 2019) |
| International Business Machines | company | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (2002) |
| Adoptex LLC | company | active |  |
| National Bureau of Economic Research | institution | active |  |
| Perplexity AI | company | active |  |

### Technologies Referenced (18)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Fault-Tolerant / High-Availability Servers | platform | Stratus/Tandem/IBM | mature | mature |
| OLTP / TPC-Benchmarked Transaction Processing | framework | TPC Council | mature | mature |
| Relational Database Management Systems | platform | Oracle/IBM/Microsoft | mature | mature |
| Desktop PC / Windows Client | platform | Microsoft/Intel | mature | mature-declining |
| Enterprise Networking (IP/VoIP) | protocol | Cisco/Juniper | mature | mature |
| Windows NT / Server OS | platform | Microsoft | mature | mature |
| Enterprise Resource Planning | application | SAP/Oracle/Microsoft | mature | mature |
| Java / Web Application Platforms | framework | Oracle/IBM/Microsoft | mature | mature |
| Linux / Open Source Server OS | platform | Red Hat/SUSE/Canonical | mature | mature |
| Service-Oriented Architecture / API Management | framework | Mulesoft/Kong/AWS | mature | mature |
| Enterprise Storage / Information Lifecycle Management | platform | EMC/NetApp/IBM | mature | mature |
| Digital Consumer Technology | platform | Apple/Samsung/HP | mature | mature |
| E-Commerce Platform Software | application | Shopify/Adobe/Salesforce | mature | mature |
| Cloud Computing & SaaS | platform | AWS/Microsoft/Google | mature | mature |
| Mobile / Smartphone Computing | platform | Apple/Samsung/Google | mature | mature |
| DuckDB | platform | DuckDB Foundation | emerging | mature |
| Frictionless Data Package | framework | Open Knowledge Foundation | mature | mature |
| CPI-U (Consumer Price Index for All Urban Consumers) | framework | BLS | mature | mature |

### Observation Summary

- Total observations: 98 (v1.0); v2.0 obs count TBD pending recompute
- By type (v1.0): topic-insight: 63, market-data: 20, viability-prediction: 15
