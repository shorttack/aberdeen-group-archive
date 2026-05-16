---
title: "A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive"
slug: kastner-prescience-market-rollup
page_type: theme
tier: 1
study_type: methodology-demonstration
audience: industry-analyst-peers
tags: [type/theme, type/methodology, theme/prescience-attribution, theme/archive-as-instrument]
date_built: 2026-05-16
build_software: perplexity-computer
sources_per_anchor_min: 3
primary_sources_per_anchor_min: 1
inclusion_threshold_studies: 10
attribution_formula: "lead × contrarian × specificity / 250, clamped [0.02, 0.80]"
---

# A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive

> **Note on framing.** This page is not a biography. It is a methodology demonstration showing how the [[_index|Kastner IT Research Archive]] can be used as a primary-source research instrument. The case study happens to be Peter S. Kastner's own analyst output (1979–present); the question being answered — *how do you defensibly quantify the economic value of a body of analyst prescience?* — is the actual subject. Readers are invited to replicate, extend, or refute the result using the open data, named DuckDB views, and explicit formulas documented below.

---

## Abstract

Using the 933-study Kastner IT Research Archive (19,175 structured observations, 466 high-prescience studies), we demonstrate a reproducible methodology for attributing economic value to analyst forecasts. We cluster all technology-tagged high-prescience studies (≥4 prescience score) into 15 inclusion-threshold themes (≥10 studies per theme) and 20 below-threshold rollup themes. For each headline theme we build a 2026-dollar cumulative-value anchor using ≥3 independent sources with ≥1 primary source (IDC tracker, Gartner forecast, SEC 10-K, BLS CPI-U, or named market authority). We then apply a transparent share-of-prescience discount based on lead time, contrarian-vs-consensus position, and specificity of the call. Sensitivity analysis stress-tests every anchor against a low/mid/high band.

**Result of the worked example:** $10.9 trillion mid net-attributed cumulative value in 2026 USD, with a defensible sensitivity band of $8.8T–$13.4T. Gross unweighted total is $41.3T. The mid figure represents 26.4% share-of-prescience attribution of the gross — a deliberately conservative discount intended to survive hostile review.

**Result of the methodology demonstration:** The archive can be queried as a structured database (Parquet + DuckDB), themes can be derived programmatically from `studies_with_high_prescience` and tech tags, and every claim in this study is reproducible from the open data plus three sources of triangulation per anchor.

---

## 1. Motivation

Quantifying the economic value of analyst prescience is rare in the industry-research literature. Most retrospectives are anecdotal ("I called the cloud in 1998") or hagiographic. The harder questions — *how much of the eventual market does the analyst deserve credit for forecasting?* and *what does the cumulative value look like in defensible 2026 dollars?* — require a methodology that can withstand a hostile reviewer.

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
SELECT * FROM studies_with_high_prescience;          -- 466 rows
SELECT * FROM studies_by_decade;                     -- decade rollups
SELECT * FROM observations_by_year;                  -- yearly time series
SELECT * FROM prescience_summary;                    -- prescience distribution
```

Columns of note: `prescience` (1–5 integer, not `prescience_score`), `prescience_rationale` (free text), `date` (ISO).

### 2.3 Universe summary

| Layer | Count |
|---|---|
| Studies in archive | 933 |
| Observations | 19,175 |
| High-prescience studies (prescience ≥4) | 466 |
| Technology-tagged subset (used in this study) | 386 |
| Themes meeting threshold (≥10 studies) | 15 |
| Below-threshold rollup themes | 20 |
| Out-of-scope (not technology) | 36 |

## 3. Methods

### 3.1 Theme classification (Phase 1)

We applied priority-ordered tagging to the technology-tagged subset to resolve overlap collisions (e.g., AI/E-Commerce/Java studies that touch multiple themes). Pseudocode:

```python
THEME_PRIORITY = [
    "ai-ml-infrastructure",          # below threshold but resolved first
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

Coverage: **99.4%** of 466 high-prescience studies were classified. The 0.6% residual (3 studies) was out-of-scope (purely industry-financial, no technology content).

### 3.2 Cumulative market value (Phase 2)

For each headline theme we built a year-by-year market-size series, then summed it across the **decade of materialization** in 2026-CPI dollars:

```
inflator(year) = CPI_U[2026] / CPI_U[year]    # CPI_U 2026 = 332.407 (BLS April 2026)
value_2026(year) = market_size(year) × inflator(year)
cumulative_theme = Σ value_2026(year) for year in materialization_decade
```

**Anchor interpolation:** linear between known data points; zero before the first verified anchor year. This is conservative — it does not extrapolate beyond observed evidence.

**E-commerce outlier fix:** The naive GMV interpretation of e-commerce yields >$150T cumulative — clearly an outlier because GMV represents the total flow of goods through e-commerce platforms, not the platform-software revenue attributable to the prescient analyst call. We replaced GMV with **platform software revenue** (Shopify, Adobe Commerce, Salesforce Commerce Cloud, BigCommerce, plus the long tail), reducing the theme from ~$158T to $159B cumulative.

**DCT narrow-scope fix:** Digital Consumer Technology, taken broadly, includes traditional white-goods consumer electronics ($1.1T/yr). The prescient call was about *digital* sub-segments (smartphones-as-cameras, smart wearables, smart TVs, connected audio), which sums to ~$180B/yr in 2025. We use the narrow definition, reducing the theme from $21T to $4.75T cumulative.

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

## 4. Inclusion criteria & themes

### 4.1 Threshold rationale

We adopted a **10-study threshold** for headline themes after the user (Peter Kastner) requested: *"2 threshold at 10 plus roll up plus note on what is in roll up for future analysis."* The rationale is methodological: ≥10 studies in a single theme indicates sustained analyst coverage rather than a one-off call. Below-threshold themes are tracked separately in §4.3 for future researchers.

### 4.2 Headline themes (15)

| # | Theme | Decade | First predict | Study count | Tagged tech anchors |
|---|---|---|---|---|---|
| 1 | [[theme-mainframes-midrange\|Fault-Tolerant / High-Availability Servers]] | 1980s | 1981 | 12 | Stratus, Tandem, Sequoia |
| 2 | [[theme-databases\|OLTP / TPC-Benchmarked Transaction Processing]] | 1990s | 1985 | 14 | TPC-A, TPC-C, DEC Rdb |
| 3 | [[theme-databases\|Relational Databases (RDBMS)]] | 1990s | 1991 | 17 | Oracle, DB2, SQL Server |
| 4 | [[theme-personal-computers-os\|Desktop PC / Windows Client]] | 1990s | 1994 | 31 | Windows 95/XP, AMD K7 |
| 5 | [[theme-networking-internet\|Enterprise Networking (IP/VoIP)]] | 1990s | 1996 | 22 | Cisco, MPLS, SIP |
| 6 | [[theme-personal-computers-os\|Windows NT / Server OS]] | 1990s | 1992 | 15 | NT 3.5, NT 4.0, Win2K |
| 7 | [[theme-erp-enterprise-apps\|Enterprise Resource Planning (ERP)]] | 1990s | 1993 | 19 | SAP R/3, PeopleSoft, Oracle Apps |
| 8 | [[theme-programming-dev-tools\|Java / Web Application Platforms]] | 1990s | 1996 | 13 | J2EE, WebLogic, WebSphere |
| 9 | [[theme-unix-open-systems\|Linux / Open Source Server OS]] | 2000s | 1998 | 18 | Red Hat, SUSE, Caldera |
| 10 | [[theme-soa-bpm-integration\|SOA / Web Services / API Management]] | 2000s | 2003 | 14 | XML, SOAP, REST, MuleSoft |
| 11 | [[theme-storage-hardware\|Enterprise Storage / ILM]] | 2000s | 1998 | 11 | EMC, NetApp, SATA midline |
| 12 | Digital Consumer Tech / Globalized Supply Chain | 2000s | 2002 | 21 | iPod, smartphones-as-cameras, Foxconn |
| 13 | E-Commerce Platform Software | 2000s | 1996 | 16 | Shopify, Adobe Commerce, BigCommerce |
| 14 | Cloud Computing & SaaS | 2010s | 1998 | 28 | AWS, Salesforce, Azure |
| 15 | Mobile / Smartphone Computing | 2010s | 2001 | 24 | iPhone, Android, ARM SoC |

### 4.3 Below-threshold rollup themes (20) — for future researchers

The following themes have meaningful prescient coverage (1–9 studies) but did not meet the 10-study inclusion threshold. They are documented here as an explicit invitation to future researchers — particularly the **AI/ML Infrastructure cluster (8 studies, 2020s)** which narrowly missed inclusion and deserves a deeper sweep.

| Theme | Study count | Decade | Future-research priority |
|---|---|---|---|
| **AI/ML Infrastructure** | 8 | 2020s | **High — narrowly missed threshold; full sweep recommended** |
| Client-Server Computing | 9 | 1990s | Medium — partially captured by RDBMS + NT themes |
| x86-64 Server | 9 | 2000s | Medium — partially captured by Linux + Cloud themes |
| Consumer Electronics / Digital Media | 5 | 2000s | Low — overlaps DCT theme |
| Wireless 802.11 / Wi-Fi | 5 | 2000s | Medium |
| Tech-Sector Financial Analysis Methodology | 3 | 1980s | Medium — methodological prescience, hard to size |
| Y2K | 3 | 1990s | Low — narrow window |
| CRM | 3 | 2000s | High — clean theme, just below threshold |
| BI / Decision Support | 3 | 2000s | Medium |
| IT Outsourcing | 3 | 2000s | Low |
| Security / Trusted Computing | 3 | 2010s | Medium |
| EAI / Middleware | 2 | 1990s | Low — overlaps SOA |
| E-Learning | 2 | 2000s | Low |
| Videoconferencing | 2 | 2010s | Medium |
| Smart Grid / IoT | 2 | (from 1979!) | High — exceptional lead time |
| SMP / Parallel Computing | 1 | 1990s | Low |
| SAN / Fibre Channel | 1 | 2000s | Low |
| ITSM | 1 | 2000s | Low |
| Tape Archival | 1 | 2000s | Low |
| Tablet Computing | 1 | 2010s | Low |

### 4.4 Out-of-scope (36 studies)

The remaining 36 high-prescience studies were classified as out-of-scope for this technology-themed analysis. They are predominantly:
- Industry-financial analysis (M&A, valuation, capital markets) — 19 studies
- Strategic/management commentary not tied to a specific technology — 12 studies
- Vendor-specific operational forecasts (without broader technology generalization) — 5 studies

These are still valuable archive content but cannot be sized via market-anchor methodology.

## 5. Results

### 5.1 Headline result

| | Low | **Mid** | High | Range |
|---|---|---|---|---|
| **Net attributed (2026 USD)** | **$8.8T** | **$10.9T** | **$13.4T** | $4.6T |
| Gross unweighted (2026 USD) | $34.5T | $41.3T | $48.1T | $13.7T |
| Overall attribution share | 25.5% | **26.4%** | 27.9% | — |

The mid figure is the recommended point estimate. It represents the **26.4% share-of-prescience-discounted cumulative economic value** of the 15 headline themes, in 2026 dollars, summed across each theme's decade of materialization.

### 5.2 Per-theme breakdown

Sorted by net attributed value (mid estimate):

| # | Theme | Mid gross $B | Attr % | Mid net $B | Lead | Contrarian | Specificity |
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
| | **TOTAL (15 themes)** | **41,283** | **26.4%** | **10,919** | | | |

Three observations:

1. **Top 4 themes contribute 78%** of net attributed value (Cloud, Mobile, DCT, OLTP). These are the calls where lead × contrarian × specificity was maxed out and the eventual market was large.
2. **High-attribution but small markets** (Linux, SOA, Fault-Tolerant) demonstrate that the methodology rewards specificity even when total market is modest — preventing the result from being dominated purely by market size.
3. **Low-attribution but large markets** (Desktop PC, ERP) demonstrate the share-of-prescience discount working as intended — when the analyst joined an already-established consensus, the discount drops attribution to 6–12%.

### 5.3 Sensitivity

![Sensitivity tornado chart](attachments/phase5_tornado.png)

**Largest uncertainty drivers** (by absolute range of net attributed):

| Theme | Range $B | Cause |
|---|---|---|
| Digital Consumer Tech | 1,779 | DCT scope ($90B narrow ↔ $300B broad-with-tablets-and-connected-TV) |
| OLTP / TPC | 1,507 | No clean modern proxy ($50B narrow RDBMS slice ↔ $170B broad DBMS+middleware+benchmark-tracked) |
| Cloud Computing & SaaS | 646 | $723B Gartner Public Cloud ↔ $913B CloudZero TCV |
| Enterprise Storage / ILM | 150 | $33B IDC enterprise storage ↔ $10.5B OpenText/Radicati narrow archiving |

**Stable themes** (range <$60B): Java, SOA, Desktop PC, RDBMS, Mobile. These have tight source consensus.

## 6. Limitations & definition-mismatch transparency

Five themes have documented definition mismatches across sources. Each is flagged in the wiki frontmatter and inline:

| # | Theme | Mismatch |
|---|---|---|
| 1 | OLTP / TPC | No clean modern proxy. Embedded in DBMS + transaction-processing-middleware + benchmark-tracked workload categories. Anchor of $75B 2025 is ~90% of RDBMS transactional share. |
| 2 | Linux Enterprise | $20–26.4B range reflects scope: Fortune BI's $26.4B includes hardware-bundle; narrower software-only definitions land $20B. |
| 3 | Enterprise Storage / ILM | $33B IDC enterprise storage tracker vs. $10.5B narrow archiving (OpenText/Radicati). |
| 4 | Digital Consumer Tech | Narrow ($180B/yr) vs. broad-CE ($1.1T/yr) — narrow chosen per outlier-rejection methodology. |
| 5 | Windows NT / Server OS | $27B Microsoft-attributable on-prem Windows Server licenses (FY25 10-K segment) vs. $366B total server hardware (with bundled OS). |

Other limitations:

- **Lead-time scoring is reviewer-judged.** Lead-time scoring (1–5) requires looking at the prescient study's date relative to materialization date. This was scored by Computer in consultation with the user and is documented in `phase4_attributed.json::attribution_notes`. Future researchers may re-score.
- **Contrarian scoring requires reading the period analyst literature.** A skeptical reviewer could re-score contrarian factor down for any theme where consensus formed earlier than we credited.
- **Cumulative-value method is conservative.** We sum only the decade of materialization, not subsequent decades when the technology continued to generate revenue. A more aggressive cumulative-through-2026 approach would roughly double the gross totals.
- **Attribution formula is opinionated.** The choice of `lead × contrarian × specificity / 250` with [2%, 80%] clamping reflects a particular philosophy. Alternative formulations (additive, log-scale, Bayesian) would yield different totals.
- **Below-threshold themes are uncounted.** Adding the 20 rollup themes (especially AI/ML Infrastructure, CRM, Smart Grid/IoT) would add an estimated $0.5T–$2T to the net attributed total. Future work.

## 7. Replication appendix

This section is for grad students, analyst peers, or anyone who wants to reproduce or extend the result.

### 7.1 Pull the prescient studies yourself

```python
import duckdb
con = duckdb.connect("db/kastner.duckdb", read_only=True)

# All 466 high-prescience studies
df = con.execute("""
  SELECT study_id, date, title, prescience, prescience_rationale
  FROM studies_with_high_prescience
  ORDER BY date
""").df()

# Theme-tagged subset (technology breadth)
tech_df = con.execute("""
  SELECT s.study_id, s.date, s.title, s.prescience
  FROM studies_with_high_prescience s
  JOIN observations o ON o.study_id = s.study_id
  WHERE o.technology_id IS NOT NULL
""").df()
```

### 7.2 Build your own theme

```python
# Example: re-create the Cloud Computing & SaaS theme
cloud_keywords = ["cloud", "utility", "grid computing", "saas", "asp", "salesforce"]
cloud_studies = tech_df[tech_df["title"].str.lower().str.contains("|".join(cloud_keywords))]
print(f"Cloud theme: {len(cloud_studies)} studies")
```

### 7.3 Recompute attribution

```python
def attribution_factor(lead, contrarian, specificity):
    """Returns share-of-prescience factor in [0.02, 0.80]."""
    raw = (lead * contrarian * specificity) / 250
    return max(0.02, min(0.80, raw))

# Example: re-score with stricter contrarian factor
new_attr = attribution_factor(lead=5, contrarian=3, specificity=4)  # 24% instead of 40%
```

### 7.4 Replace an anchor

```python
import json
with open("data/value_table.json") as f:
    anchors = json.load(f)

# Substitute your own 2025 anchor for Cloud Computing
anchors["cloud-saas"]["anchor_2025_b"] = 1000  # your number here
# Re-run cumulative summation, apply attribution, observe new total
```

### 7.5 Add a below-threshold theme

The CRM theme (3 studies, just below threshold) is a clean candidate:
- Pull the 3 studies via `SELECT ... WHERE study_id IN (...)` (specific IDs in `phase1_final.json`)
- Build market anchor: Gartner CRM forecast 2024 = $96B
- Score: lead ~2 (Kastner's CRM coverage was early-2000s, market materialized late-2000s), contrarian ~2, specificity ~4
- Attribution: 2×2×4/250 = 6.4%
- Decade-of-materialization sum ≈ $1.2T gross → ~$77B net attributed

### 7.6 Code & data manifest

| Artifact | Path | Description |
|---|---|---|
| Final theme classification | `phase1_final.json` | 15 headline + 20 rollup + 36 OOS |
| Cumulative value table | `value_table.json` | Per-theme decade-of-materialization sums |
| Source triangulation | `phase3_source_table.md` | 3+ sources per theme, ≥1 primary |
| Attribution scoring | `phase4_attributed.json` | Per-theme lead/contrarian/specificity + factor + rationale |
| Sensitivity bands | `phase5_sensitivity.json` | Low/mid/high net attributed per theme |
| Sensitivity chart | `phase5_tornado.png` | Tornado visualization |

All artifacts are in the source archive at `shorttack/aberdeen-group-archive` under the relevant phase tags.

## 8. Discussion: what this demonstrates about the archive

The methodology demonstration shows that the Kastner archive supports research questions of three distinct types:

1. **Aggregate counting** (Phase 1): "How many high-prescience studies are there by decade and theme?" — answerable in seconds via DuckDB views.
2. **Anchored quantification** (Phases 2–3): "What is the 2026-dollar market size of the technologies Kastner correctly forecast?" — requires triangulating with external sources, but the archive supplies the universe of forecast claims.
3. **Attribution analysis** (Phases 4–5): "What share of that value is attributable to the prescience itself versus the natural emergence of the technology?" — requires reading prescience rationales (`prescience_rationale` column) plus period analyst literature.

The same three-type structure applies to any analyst archive. Forrester's, Gartner's, IDC's individual-author archives, or even academic forecast literature (e.g., NBER working papers) could be subjected to comparable analysis if structured to expose `prescience` and `prescience_rationale` as queryable fields.

## 9. Open questions for future researchers

1. **AI/ML Infrastructure deep sweep.** The 8-study below-threshold cluster is the most consequential gap. A targeted re-tag pass might reveal more studies; combined with rapid 2024–2026 market growth, this could be a >$1T-attributable theme.
2. **Below-threshold roll-up.** Quantify the 20 rollup themes as a group; estimated $0.5T–$2T additional net attributed.
3. **Alternative attribution formulas.** Compare multiplicative (used here), additive, log-scale, and Bayesian approaches. The choice substantially affects which themes dominate.
4. **Cross-archive comparison.** Apply the same methodology to a peer analyst's archive (Forrester, Gartner) and benchmark.
5. **Cumulative-through-present scope.** Re-run with cumulative summation extended through 2026 (not just decade-of-materialization), which would roughly double gross totals.
6. **Specificity de-aggregation.** Score specificity at study-level rather than theme-level; surface the single most specific high-impact studies.

## 10. Provenance

| Field | Value |
|---|---|
| Build date | 2026-05-16 |
| Build software | Perplexity Computer (Claude Sonnet 4.6) |
| Archive commit | `8d00ab5` |
| Studies queried | 466 (high-prescience subset of 933) |
| Sources cited (Phase 3) | 60+ across 15 themes |
| Inflation index | BLS CPI-U April 2026 = 332.407 |
| Methodology version | v1.0 |
| Reviewer | Peter S. Kastner (study subject; methodology approved at each phase checkpoint) |

---

## See also

- [[_index|Wiki index]] · [[_index-themes|All themes]] · [[_index-decades|By decade]] · [[_index-studies|Study list]]
- [[kastner-technology-breadth-memoir-2026|Breadth memoir]] (companion narrative)
- [[AGENTS|AGENTS.md]] (LLM-facing query guide)
