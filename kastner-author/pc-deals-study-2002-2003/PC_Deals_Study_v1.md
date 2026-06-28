# The Aberdeen *PC Deals* Weekly Reports, 2002–2003: A Data-Driven Study of Consumer PC Price Tracking at an Inflection Point

**A heterogeneous analysis of the Kastner Aberdeen Archive *PC Deals* corpus, combined with the contemporaneous market record**

Author: Prepared for Peter S. Kastner
Date: June 27, 2026
Method: Read-only DuckDB queries against the Kastner Aberdeen Wiki (`kastner.duckdb`, 27 `v_*` views) over the *PC Deals* sub-corpus, cross-referenced with the contemporaneous trade and analyst record (Gartner/Dataquest, IDC, CNET, Intel, Computerworld, The Register).

---

## Abstract

Between July 2002 and August 2003, the Aberdeen Group Digital Consumer Technology (DCT) practice published a weekly retail price tracker, *PC Deals*, that scored the best name-brand consumer desktop bargains across a fixed grid of price points. This study treats that 14-month run as a structured dataset rather than a set of newsletters. Working from the archive's master tables, we isolate a **42-study weekly sub-corpus carrying 903 observations** and decompose it along five axes the original analyst tracked by hand: store chain, PC vendor, configuration, price band, and editorial commentary ("bang for the buck"). The quantitative structure of the archive corroborates — and sharpens — the qualitative narrative: Dell dominates analyst attention (96 observation links), the post-merger HP/Compaq entity is the clear number two (59), and a value tier of eMachines, Sony, and Gateway clusters tightly behind (~30 each), with the three national big-box chains — Best Buy, CompUSA, Circuit City — each appearing ~21–22 times as the locus of *bundled* value. Against the external record, the period emerges as a genuine inflection point: Dell's direct-model price leadership, the HP-Compaq brand consolidation, the AMD Athlon XP value insurgency, the DDR-displaces-RDRAM memory transition, the November 2002 arrival of Pentium 4 Hyper-Threading, and the collapse of LCD flat panels from luxury to mainstream. A distinctive feature of the archive — **42 matched forecast/actual-outcome observation pairs** — lets us read the tracker not only as a price log but as a small, auditable record of one analyst's near-term market calls.

---

## 1. Introduction and motivation

Most surviving artifacts of the early-2000s PC price war are aggregate: quarterly shipment shares from Gartner/Dataquest and IDC, vendor earnings, and journalistic retrospectives. What is comparatively rare is a **high-frequency, point-of-sale view of the consumer desktop market captured contemporaneously, week by week, by a working industry analyst** — and rarer still one preserved in machine-readable form. The Aberdeen *PC Deals* corpus is exactly that. Its stated purpose was a weekly retail price tracker identifying the best deals on name-brand PCs from Compaq, Dell, eMachines, Gateway, HP, and Sony across nine price-point targets from roughly $550 to over $1,550, with "winners" chosen on processor speed, memory size and bandwidth, hard-drive capacity, optical drives, and bundled monitor/printer components, and adjusted for shipping, instant savings, and mail-in rebates to find true cost (as summarized in the archive's own corpus retrieval, `study-dct-about-weekly-pc-deals-2002`).

This study asks: **treated as data, what does the *PC Deals* run teach us that the prose alone does not?** The answer is that the structured layer turns impressionistic claims ("Dell prices were volatile," "Best Buy owned the bundles") into countable, dated, cross-referenced evidence — and that the archive's forecast-verification layer turns a price newsletter into a testable record of analyst judgment.

---

## 2. Data and method

### 2.1 The archive

The Kastner Aberdeen Wiki exposes a 27-view DuckDB query layer over master CSV tables (`_master_studies`, `_master_observations`, `_master_entities`, `_master_technologies`, and their join tables). The full archive baseline at query time was **1,454 studies**. The *PC Deals* material lives inside the 74-study `dct` (Digital Consumer Technology) collection.

### 2.2 Defining the weekly sub-corpus

The `dct` bucket mixes practice-methodology decks, webinars, vendor briefings, and company snapshots with the price tracker proper. To isolate the weekly tracker we restricted to study IDs matching the weekly/business-deals/methodology patterns (`dct-weekly-*`, `dct-business-*pc-deals*`, the `about`/`why` methodology pieces, and the Intel-processor-price analysis). This yields a clean **42-study weekly sub-corpus** spanning **2002-07-01 to 2003-08-24**, carrying **903 observations**.

### 2.3 Observation structure

Observations are typed. For the weekly sub-corpus the distribution is:

| observation_type | count |
|---|---:|
| market-data | 465 |
| technology-assessment | 250 |
| expert-opinion | 87 |
| viability-prediction | 46 |
| actual-outcome | 42 |
| framework-factor | 8 |
| topic-insight | 3 |
| (other) | 2 |

Price points are not stored as a clean numeric matrix; they are extracted as commentary-anchored `metric_value` snippets (e.g., *"Price point highlighted in commentary: $900"*), so price analysis here is frequency-of-mention and band-level, not a reconstructed SKU ledger. This is an important methodological caveat: **the corpus is a curated editorial record, not a complete price database**, a limitation the reports themselves acknowledged — they could not monitor volatile online pricing 24/7, comparing it to airline-ticket pricing (`study-dct-weekly-2003-03-02`).

### 2.4 External corroboration

Structured findings were checked against the contemporaneous record: Gartner/Dataquest and IDC shipment-share data via Computerworld and CNET, Intel's own launch press, and trade coverage of LCD pricing and the Gateway/eMachines endgame. These are cited inline below.

---

## 3. Findings

### 3.1 Temporal cadence — the calendar drives the deals

Reports per month reveal the retail calendar in the data itself:

| Month | Reports | | Month | Reports |
|---|---:|---|---|---:|
| 2002-07 | 1 | | 2003-02 | 0 |
| 2002-08 | 2 | | 2003-03 | 5 |
| 2002-09 | 1 | | 2003-04 | 3 |
| 2002-10 | 2 | | 2003-05 | 2 |
| 2002-11 | 4 | | 2003-06 | 3 |
| 2002-12 | **7** | | 2003-07 | 3 |
| 2003-01 | 5 | | 2003-08 | 4 |

Two features stand out. The **December 2002 spike (7 reports)** tracks holiday-season intensity, and the **February 2003 gap (0 reports)** marks the post-holiday dead zone. The reports are explicit that the calendar, not the technology, sets the rhythm: back-to-school (July–August) and the holidays produced the most offers, while the corpus names the "Dads and Grads" early-summer lull and the "slow summer months" before the August "Back to School shopping frenzy" (`dct-weekly-2003-06-08`). The holiday optimism was misplaced: the December 30, 2002 report opens by noting "this year's holiday season's sales yielded the lowest rate of growth in decades. Frankly, PC Deals is not surprised" (`dct-weekly-2002-12-30`).

### 3.2 PC vendors — Dell's gravity, HP's weight, and the value tier

Ranking entities by observation linkage across the weekly sub-corpus:

| Vendor | Obs. mentions |
|---|---:|
| Dell Computer Corporation | **96** |
| Hewlett-Packard (post-merger) | 59 |
| eMachines, Inc. | 31 |
| Sony Corporation | 30 |
| Gateway, Inc. | 30 |
| Compaq Computer Corporation | 10 |

Dell's dominance of *analyst attention* mirrors its dominance of the *market*: Dell held roughly **27.9–28% of U.S. PC shipments in 2002**, comfortably ahead of HP at ~19.8% ([Computerworld/Dataquest](https://www.computerworld.com/article/1573804/dataquest-consumer-shipments-boosted-2002-pc-sales.html)), and retook the worldwide lead from HP in Q1 2003 on 24.7% unit growth ([Computerworld/IDC](https://www.computerworld.com/article/1340039/idc-dell-s-back-on-top-of-worldwide-pc-shipments.html)). The corpus captures the *mechanism* behind that share — relentless, opportunistic pricing — better than any quarterly number can. Dell's behavior is the single most-commented theme: prices that "jolt upwards" over $200 between weeks (`dct-weekly-2003-08-17`: *"This week, Dimension desktop prices jolted upwards in some cases over $200"*) alternating with aggressive cuts ("Spring Cleaning. It's spring. Dell is cutting prices," `dct-weekly-2003-04-13`), and the August 24, 2003 observation that Dell announced cuts "ranging from 6% in consumer desktops to 22% for business servers" — forcing Gateway to drop its 500-series by $100 in response (`dct-weekly-2003-08-24`).

The value tier is where the archive adds nuance. **eMachines** appears as often as Sony and Gateway despite being a budget brand — the corpus repeatedly names it the under-$1,000 value winner, sourced primarily through Best Buy ("eMachines... wins on — ta, dah — low price, according to store managers," `dct-weekly-2002-12-15`; "lots of features for not a lot of cash," `dct-weekly-2003-07-06`). The external record vindicates this: eMachines' budget momentum carried it into the **top five U.S. PC vendors by end of 2003, surpassing Gateway and Apple** ([CNET/IDC](https://www.cnet.com/tech/computing/hp-back-on-top-of-pc-market/)) — and the brand's strength was such that Gateway acquired eMachines in 2004 ([BGR](https://www.bgr.com/2167267/what-happened-to-gateway-computers/)).

**Gateway**, conversely, is the cautionary tale. The corpus first criticizes its static pricing and absence of bundles, then watches it diversify into electronics retail ("the Gateway logo is showing up more and more at online storefronts," `dct-weekly-2003-01-05`) and finally cut PC prices to compete (`dct-weekly-2003-08-24`). The external arc is harsher than the contemporaneous reports could see: Gateway fell to ~3.5% U.S. share in 2003 as its PC business shrank 26% ([The Register](https://www.theregister.com/2004/01/15/dell_tops_up_pc_market/)), closed dozens of Gateway Country stores, and was ultimately acquired by Acer in 2007 ([BGR](https://www.bgr.com/2167267/what-happened-to-gateway-computers/)).

### 3.3 The retail channel — bundles belong to the big boxes

The three national chains appear in a near-dead heat:

| Retailer | Obs. mentions |
|---|---:|
| Best Buy Co., Inc. | 22 |
| CompUSA | 22 |
| Circuit City Stores, Inc. | 21 |

The structural finding here is the **direct-vs-retail split**: manufacturer sites (Dell, HP, Gateway) offered competitive bare-system prices and free shipping, but the best *bundled* deals (PC + monitor + printer) were almost exclusively at the national chains, paired with $100–$400 mail-in rebates and 12–24-month no-interest financing (per the archive's own corpus synthesis, drawing on `study-dct-weekly-2003-01-26`, `-07-26`, `-08-10`). The chains also played distinct roles the data exposes: **Best Buy** as the primary channel for eMachines and Sony; **CompUSA** as the liquidator, "continuing to sell 'older' PC models after Best Buy and Circuit City had removed them" (`study-dct-weekly-2003-06-15`, `-07-26`). The August 2003 back-to-school surge is visible as a sudden bloom of chain circulars: "A lot more deals appeared in this week's flyers from Best Buy and Circuit City, finally hailing the back-to-school buying frenzy" (`dct-weekly-2003-08-03`). The Circuit City presence is poignant in hindsight — the chain that the corpus treats as a co-equal value leader would liquidate entirely by 2009.

### 3.4 Configuration and technology — what a "winning" machine contained

Technologies ranked by observation linkage:

| Technology | Obs. mentions |
|---|---:|
| Desktop PC (tower) | 64 |
| Intel Pentium 4 (2.4 GHz class) | 54 |
| AMD Athlon XP | 33 |
| AMD Athlon (non-XP) | 27 |
| DDR SDRAM | 26 |
| Intel Celeron | 20 |
| Notebook form factor | 19 |
| Pentium 4 with Hyper-Threading | 18 |
| Windows Media Center PC | 11 |
| LCD Flat-Panel Monitor | 10 |
| Pentium 4-M (Mobile) | 10 |
| DVD+RW/+R | 9 |
| RDRAM (Rambus) | 5 |

This ranking tells the configuration story of the era with unusual economy. The **Pentium 4 is the spine** of the mainstream pick, but the **combined AMD Athlon/Athlon XP linkage (60) exceeds the headline P4 count (54)** — a quantitative fingerprint of the AMD value insurgency the prose celebrates ("AMD ruled the retail ads this week with an abundance of Athlon machines at great prices... competitive machines that cost less than their Intel counterparts," `dct-weekly-2002-11-03`). The corpus explicitly framed AMD Athlon as the value answer to Intel Celeron in the sub-$900 band.

The **memory transition is legible in the counts**: DDR SDRAM (26) has decisively displaced RDRAM (5), matching the period's industry shift away from Rambus's premium, royalty-encumbered memory. The corpus notes RDRAM machines (e.g., Dell's 8200) cost "about $200 more than comparable DDR" (`dct-weekly-2002-08-24`) and flags high-performance RDRAM Pentium machines as a segment "improving the least."

The corpus also captures **Pentium 4 Hyper-Threading in real time**. Intel launched the 3.06 GHz P4 with HT on **November 14, 2002** ([Intel press release](https://www.intel.com/pressroom/archive/releases/2002/20021114comp.htm)) — and the archive carries a dedicated special report dated **that exact day** explaining the feature ("HT technology works by providing hardware support for a second executing compute task. There is still only a single central processor unit," `dct-weekly-2002-11-14-p4-ht`). The reports then track HT's price descent until, by May 2003, HT had fallen far enough that *PC Deals* "decided to eliminate the separate Hyper-Threading (HT) category" and fold HT machines in with regular P4s (`dct-weekly-2003-05-18`) — a structural editorial change driven by price compression.

Finally, the **emergence of the living-room PC**: Microsoft's Windows Media Center PC (11 mentions) appears, with HP's m200 Media Center series launching "under $999" in June 2003 (`dct-weekly-2003-06-22`), and **LCD flat panels (10)** transition from luxury to mainstream over the run — the corpus notes them dropping from $700–$1,000 toward under $500 by early 2003, consistent with the broader trade narrative of flat panels moving "for the masses" through 2003 ([Bloomberg](https://www.bloomberg.com/news/articles/2003-06-22/flat-panels-for-the-masses)).

### 3.5 Price bands — compression and bifurcation

Price points highlighted in commentary (top system-level bands, excluding rebate/component deltas like $100/$150/$200):

| Band | Frequency |
|---|---:|
| $900 | 24 |
| $600 | 11 |
| $1,000 | 6 |
| $750 | 5 |
| $1,600 | 5 |
| $1,200 | 4 |
| $800 | 3 |

The **$900 band is the gravitational center** of the mainstream consumer market in this period — the most-discussed system price point by a wide margin. The narrative arc around the bands is one of **compression at the bottom and bifurcation at the top**. Early 2003 saw "an explosion of affordable options in the under-$900 category" driven by AMD value (corpus synthesis; `dct-weekly-2003-04-06`, `-01-12`), while the previously "hot" $1,200–$1,400 mid-high bands "diminished to sparse pickings" as deals migrated to a new "over $1,600 range" for media-centric and gaming systems (`dct-weekly-2003-03-23`). In other words, the middle of the market hollowed out: buyers either traded down into newly-cheap sub-$900 machines or up into media/gaming systems above $1,600.

### 3.6 The "bang for the buck" methodology

The corpus's editorial signature is the phrase "bang for the buck," used from the first week ("the market is in the midst of adding enormous technology bang for the buyer's buck," `dct-weekly-2002-08-24`). The most explicit codification of the winning recipe is the March 17, 2003 reference configuration for "best combination of price, value, and longevity": **Pentium 4 at 2.4 GHz (533 MHz front-side bus), 256 MB DDR SDRAM minimum, a 7200 RPM hard drive** (`dct-business-2003-03-17-pc-deals`). The expert-opinion observations encode the component priorities directly: a memory tier threshold ("128MB significantly slower than 256MB; multimedia = 512MB"), a hard-drive preference ("Faster 7200 RPM > bigger"), and a flat-panel aspiration ("19-inch flat-panel 'to die for'"). The method was holistic — true cost after shipping, instant savings, and rebates — and component-weighted, privileging processor class, memory bandwidth (DDR over the dying RDRAM, and over plain SDRAM), and drive speed over raw capacity.

### 3.7 The forecast-verification layer — reading *PC Deals* as analyst judgment

The archive's most analytically distinctive feature is a set of **42 matched `viability-prediction` → `actual-outcome` observation pairs**: each near-term call Kastner made in the commentary is paired with a retrospectively-authored assessment of how it played out. A few illustrative cases:

- **HP-Compaq aggression (Aug 2002 call):** Kastner predicted HP would chase back lost share with "outstanding PC deals." Outcome: *"HP-Compaq did push aggressive consumer PC deals through Q3–Q4 2002 as predicted... narrowed but did not eliminate Dell's global PC share lead."* Verdict in the archive: direction correct, magnitude overstated.
- **Compaq/HP brand split (Oct 2002 call):** Kastner expected Compaq to focus on business/bread-and-butter productivity while HP emphasized performance/multimedia. Outcome: *"CNET June 16 2003 report confirms HP announced exactly this strategy... Compaq brand fully discontinued"* — scored as a clean hit.
- **Athlon XP 2800+ into mainstream bands (Oct 2002 call):** Predicted to reach covered price points "until next year." Outcome: confirmed — the 2800+ moved into $700–$1,000 configurations through 2003, visible in the corpus itself.
- **Gateway to a high-end niche (Oct 2002 call):** Outcome: *"Gateway did retreat from broad-line retail, but not to a profitable high-end niche — closed Gateway Country stores 2004 after losing $1B+; acquired by Acer 2007."* Verdict: direction right, outcome wrong.

The pattern is instructive: **Kastner's short-horizon, mechanism-level calls (next week's circular volume, a chip moving into a price band, a brand's pricing posture) were reliably accurate; the longer-horizon strategic calls (where a struggling brand would land) were directionally right but optimistic about the struggling player's fate.** This is a recognizable signature of competent near-term market tracking: excellent at reading the tape, weaker at predicting structural endgames. Consistent with this being a *price tracker* rather than a *forecasting product*, 40 of the 42 weekly studies carry a `not-applicable` prescience verdict; only the methodology pieces score `high`/`medium`.

---

## 4. Discussion — what the deep dive teaches

**1. The structured archive validates the qualitative summary and quantifies it.** Every major claim in the corpus-level narrative — Dell's price volatility, Best Buy/CompUSA/Circuit City as the bundle channel, eMachines as the budget value winner, AMD's value insurgency, the DDR/RDRAM transition, HT's arrival and folding-in — has a countable structural footprint (entity link counts, technology link counts, price-band frequencies, dated observations). The data does not contradict the prose; it disciplines it.

**2. *PC Deals* is a rare high-frequency ground-truth complement to quarterly share data.** Gartner/IDC tell us *that* Dell gained share and eMachines broke into the top five; the *PC Deals* corpus shows *how* — week by week, at the point of sale, through specific machines, rebates, and financing terms. It is the retail microstructure beneath the macro shares.

**3. The period is a genuine inflection point, and the tracker caught it.** 2002–2003 compressed several transitions into 14 months: the HP-Compaq integration and brand consolidation, the Dell direct-model apex, the Gateway decline and eMachines ascent, the AMD value challenge, the RDRAM-to-DDR memory shift, the P4 Hyper-Threading debut, and the LCD flat-panel democratization. The corpus is a contemporaneous eyewitness to all of them.

**4. The forecast layer turns a newsletter into a study of analyst calibration.** The 42 forecast/outcome pairs are a small but clean dataset for examining where a working analyst's near-term judgment held and where it strayed — short-horizon accurate, long-horizon optimistic — a finding with methodological value well beyond the PC market.

**5. The bundle is the unit of consumer value, not the box.** The single most actionable lesson for the 2002–2003 mass-market buyer encoded in the data: true value lived in the national-chain bundle (system + monitor + printer + rebate + financing), not the manufacturer's bare-system web price — even when the web price looked lower on a spec-for-spec basis.

---

## 5. Limitations

- **Editorial, not exhaustive.** The corpus is a curated record of *notable* weekly deals, not a complete price database. Price points are commentary-anchored snippets, so band-level frequency analysis is sound but per-SKU price reconstruction is not.
- **Online pricing volatility.** The reports themselves disclaim 24/7 coverage of fast-moving online prices (`dct-weekly-2003-03-02`).
- **Window-bounded.** Coverage runs late 2002 through August 2003; the corpus contains no data beyond this window, so the longer arcs (Gateway's collapse, Circuit City's bankruptcy, eMachines' absorption) are supplied here from the external record, not the archive.
- **Single-analyst voice.** The commentary and forecasts reflect one analyst's framing; the forecast-verification layer is a retrospective reconstruction, valuable but authored after the fact.

---

## 6. Extraction fidelity — an A:B audit of the structured layer against the full text

Every quantitative finding in Sections 3–5 rests on the archive's **structured extraction layer** (the per-study `observations.csv`, `entities.csv`, and `technologies.csv` tables, surfaced through the DuckDB views). Those tables are themselves the product of an automated, LLM-assisted ingest (the *Archival Ingest Skill*, here v16) reading each study's original document text. A serious question for any corpus built this way — and the one Pete posed — is: **how faithfully does the structured layer represent the source, and what does the extraction systematically compress, distort, or drop?** This matters because downstream analysis (including this very study) reads the *tables*, not the *prose*, and inherits whatever the extractor blinkered.

To answer it, we ran a controlled **A:B comparison**. The **A side** is the structured extraction (CSV rows). The **B side** is the authoritative full text — each study package's `source/original_text.md` under `kastner-author/dct/` in the archive repo, the canonical record per the README. We purposively sampled **seven studies** spanning the analytic axes: the methodology charter (`dct-about-weekly-pc-deals-2002`), the AMD-value week (`dct-weekly-2002-11-03`), the Pentium 4 Hyper-Threading special (`dct-weekly-2002-11-14-p4-ht`), the holiday post-mortem (`dct-weekly-2002-12-30`), the 3,000-word business reference-desktop report (`dct-business-2003-03-17-pc-deals`), the price-band-bifurcation week (`dct-weekly-2003-03-23`), and the Dell-cuts-force-Gateway week (`dct-weekly-2003-08-24`). Together they carry **129 observation rows, 75 entity rows, and 46 technology rows** extracted from roughly **6,500 words** of source prose. Each was read line-by-line against its source.

### 6.1 What the structured layer captures well

The audit is not a catalog of failure. Three things extract reliably:

1. **Entities and technologies are near-complete and enriched.** Across the sample, the named vendors, chips, and form factors present in the prose almost always appear as rows — and the rows add genuine value the source lacks: a `successor`/`status` lineage ("Gateway → Acer Inc. (acquired October 2007, $710M); brand discontinued ~2011") and an era/lifecycle stamp. This is *augmentation*, not just transcription, and it is the layer's clear strength.
2. **Source structure propagates into clean rows.** The two "buying-tips" weeklies whose source is organized under per-retailer headers (BestBuy / Circuit City / CompUSA / Dell / Gateway / Sony / HP) produced one clean, correctly-attributed row per retailer (`dct-weekly-2003-03-23` OBS-002–009; `dct-weekly-2003-08-24` OBS-002–009). **Where the document is structured, the extraction is faithful.**
3. **A well-formed source yields a near-lossless table.** The methodology charter is the positive control: its 13 rows are semantically distinct and complete — program mission, the six tracked vendors, the ">60% combined U.S. share" figure, all nine price-point bands verbatim ($550…$1,550+), the selection-criteria ranking, the bundle-valuation rule, and the weekly cadence. It also **correctly recorded that this charter was authored by Caroline S. Kastner, not Peter** (`personal-recollection`, OBS-013) — an authorship distinction Section 1 of this study had blurred by attributing the methodology framing to the archive generally. The A:B audit thus also functions as a fact-check on the analysis built atop the tables.

### 6.2 A loss taxonomy — how extraction compresses the record

Where the source is narrative rather than tabular, six recurring failure modes appear. Counts are across the seven-study sample.

| # | Failure mode | What it looks like | Where observed |
|---|---|---|---|
| L1 | **Window-fragment truncation** | `metric_value` stored as a fixed-width character slice that begins or ends mid-word | Pervasive in every price row, e.g. `dct-weekly-2002-11-14-p4-ht` OBS-002 = "uct line as Intel rolls out…" ("[prod]uct") |
| L2 | **Relational collapse of tables** | A source price table shredded into disconnected single-value rows, destroying the model→price→delta mapping | `dct-business-2003-03-17-pc-deals` OBS-003–009: nine fragments of one 4-row price table |
| L3 | **Quota padding / placeholder rows** | Empty stub rows ("Additional commentary points… see original_text.md", confidence `low`, `unverified`) inserted to reach a row count | 5 placeholder rows in the sample (`dct-weekly-2002-11-14-p4-ht` OBS-014/015; `dct-weekly-2002-11-03` OBS-015) |
| L4 | **Duplicated source spans** | The same sentence copied verbatim across multiple rows (often one per linked technology) | 15 duplicate-source rows in the sample; four P4-HT tech rows share one sentence; `dct-business-2003-03-17` forecasts 2 and 4 are identical |
| L5 | **Phantom entities/technologies** | A row for something never actually in the source | `dct-weekly-2002-11-14-p4-ht` lists *Intel Pentium 4-M (Mobile)* as referenced — the term never appears in that document |
| L6 | **Type miscasting of claims** | A non-forecast sentence stored as a `viability-prediction`; a price hike stored as commentary | `dct-weekly-2002-12-30` "Prediction 2" = "expect to pay at all other sites from Compusa" (a shipping-policy statement, not a forecast) |

### 6.3 The blinder effect — the highest-value content is the most likely to be lost

The taxonomy's mechanical failures (L1–L6) matter, but the deeper finding is **semantic**: the material an extractor drops is disproportionately the material a *historian* most wants. The structured layer reliably keeps nouns (vendors, chips, price points) and reliably loses **reasoning, specificity, and narrative causation**. Worked examples from the B side that have **no structured representation** on the A side:

- **Named SKU + price pairs — the actual deals.** The Dec 30 report's centerpiece is the **HP 573n collapsing from $900 at Staples one week to $1,418 at HP Online the next** — which the analyst calls "the largest price hike recorded in PC Deal's history." The A side contains the fragments "$900" and "$1,418" as separate window-slices (L1) and mis-files the hike as a "prediction" (L6); the *event* — a specific machine, two retailers, a one-week 58% swing — exists nowhere as a structured fact (`dct-weekly-2002-12-30`).
- **Analytical inferences.** The Nov 3 report observes the Dell Dimension 2300 jumping **$709 → $848** and reasons that "Dell is collecting the price of its 'free' upgrades somewhere else in its configuration" — a sharp read of vendor pricing behavior. Neither the prices nor the inference survive extraction (`dct-weekly-2002-11-03`).
- **The reference architecture itself.** The entire point of the March 17 business report is its **Enterprise Reference Desktop spec** (P4 2.4 GHz / 533 FSB, 256 MB DDR minimum, 7200 RPM drive, 15–17" LCD, WinXP Pro SP1, 3-year next-business-day warranty). On the A side this exists only inside one truncated free-text blob (OBS-001), not as structured fields (L2) — even though it is the most reusable, queryable content in the document.
- **The empirical evidence.** The same report's lab finding — "at least a 10% improvement (and sometimes 30%) in XP throughput with 256MB compared to 128MB" — is absent. So is the P4-HT special's striking claim that "many application mixes show performance improvements more in the 80%–90% range" against a 50% clock increase, and its "335 tasks in Task Manager" empirical hook.
- **The most prescient passage in the sample.** The March 17 "Your Next Desktop is a Laptop" thesis — the Centrino launch flagged with "Mark down March 12th, 2003 on your computer history calendar," the Dothan + Tablet PC + OneNote convertible forecast, and the call that such notebooks would be "more than 10% of corporate clients in 2004" — reduces to a single truncated forecast fragment (L1). The milestone sentence itself returns **zero** hits in the structured layer. A prescience-scoring pass that reads only the tables would never see the call it most deserves to score.

The pattern is consistent and directional: **extraction preserves the *what* (entities, counts, price points) and discards the *why* and the *how-much* (causal reasoning, hedged judgment, quantified deltas, named-SKU specificity).** A corpus built solely from the A side is an index of *topics covered*, not a record of *what was argued* — and our own Section 3 analysis, by counting mention-frequencies, silently adopted that compression. The frequency tables are sound as a map of analyst *attention*; they are not, and cannot be, a reconstruction of analyst *judgment*. That judgment lives in the prose.

### 6.4 A quantitative sketch of the gap

The loss is measurable. In the sample, roughly **half of all observation rows are degraded** by at least one mechanical failure: of 129 rows, **≈39 are window-fragment price slices (L1/L2), 15 are duplicate-source spans (L4), and 5 are placeholders (L3)** — leaving a minority of rows that are both well-formed and information-bearing. Of the four documents containing a genuine forecast or analytical inference of historical interest (the 573n hike, the Dell-upgrade inference, the reference spec, the Centrino milestone), **none is represented as a clean, queryable structured fact** — a 0-for-4 capture rate on the highest-value content even as entity capture approaches 100%. The asymmetry *is* the finding: **capture rate is inversely correlated with interpretive value.**

### 6.5 Implications for corpus construction and extraction practice

This A:B exercise is, as Pete framed it, a calibration step — and it yields concrete, transferable guidance for building higher-fidelity research corpora:

1. **Treat tabular source as tabular.** The single largest loss (L2) comes from running narrative-prose extractors over embedded tables. Detect tables first and ingest them as typed records (model, price, delta, date) so SKU→price relationships survive. The March 17 price grid should have become four clean rows, not nine fragments.
2. **Store spans by offsets, never by fixed-width slices.** L1 truncation is gratuitous: capture `(char_start, char_end)` into the source and store the *clean sentence*, not a byte window. This alone repairs every price row in the sample.
3. **Abolish quota padding.** Never emit a row to reach a target count. A study with five real observations should yield five rows; placeholders (L3) pollute frequency analysis with phantom mass and should fail validation.
4. **One claim, one row; deduplicate source spans.** Linking a sentence to three technologies should produce three *links*, not three copies of the sentence (L4). Separate the claim text from the entity/tech association.
5. **Validate entities/technologies against the source string.** A row whose name does not appear (even as a synonym) in the source text should be flagged — catching phantoms like the P4-Mobile reference (L5).
6. **Type-check claims with the source's own framing.** Future tense / modal verbs ("we forecast," "we expect," "by next April") gate `viability-prediction`; statements of present policy do not (L6). Mis-typing corrupts the very forecast-verification layer (Section 3.7) that makes this corpus distinctive.
7. **Add a quantitative-claim and a reasoning extractor.** The systematically-lost content — numeric deltas ("$709→$848"), test results ("10–30% throughput"), and causal inferences ("Dell is collecting the cost elsewhere") — needs dedicated passes. Capturing the *number with its referent* and the *claim with its warrant* is what would let the structured layer represent argument, not just topic.
8. **Keep the full text first-class and audit against it.** The reason this calibration was even possible is that the archive preserves `source/original_text.md` beside every package. That discipline — never discard the B side — is the precondition for measuring and improving the A side. Periodic A:B sampling should be a standing part of corpus QA, not a one-off.

The broader lesson for *teaching* extraction is that **the extractor's silent editorial choices are themselves historical data.** Knowing that this pipeline keeps entities and drops reasoning tells a future researcher exactly how to read — and how far to trust — any query run against the tables: excellent for "who and what was discussed, how often," unreliable for "what was concluded and why." Documenting that boundary is more valuable than pretending it does not exist.

---

## 7. Conclusion

Read as data, the Aberdeen *PC Deals* weekly run is far more than a price newsletter. Its 42 weekly studies and 903 observations form a dated, cross-referenced, point-of-sale chronicle of the U.S. consumer desktop market at one of its most consequential moments — and the structured archive lets us measure what the prose only asserts. Dell's gravitational pull on analyst attention matches its market dominance; the value tier of eMachines, Sony, and Gateway is quantitatively distinct from it; the big-box chains own the bundle; AMD's Athlon footprint rivals the Pentium 4's; and a 42-pair forecast-verification layer reveals an analyst who read the weekly tape with precision but underestimated how badly the era's losers would fare. The deepest lesson is methodological: a disciplined, high-frequency, component-weighted price tracker — even one that disclaimed being a forecasting product — produced a durable, auditable, and surprisingly predictive record of a market in transition.

---

## Sources

### Primary — Kastner Aberdeen Archive (DuckDB `v_studies`/`v_observations`/`v_entities`/`v_technologies`)
- *About Aberdeen Weekly PC Deals* — `dct-about-weekly-pc-deals-2002`
- *Why Aberdeen Is Following Consumer PC Deals (DCT Practice Methodology)* — `dct-why-aberdeen-follows-pc-deals-2002`
- Weekly/Business *PC Deals* reports, 2002-08-24 through 2003-08-24 (42-study sub-corpus), incl. the Nov 14 2002 P4-HT special (`dct-weekly-2002-11-14-p4-ht`), the Dec 30 2002 holiday post-mortem (`dct-weekly-2002-12-30`), the Mar 17 2003 reference configuration (`dct-business-2003-03-17-pc-deals`), the Mar 23 2003 price-band bifurcation (`dct-weekly-2003-03-23`), and the May 18 2003 HT-category retirement (`dct-weekly-2003-05-18`).
- Forecast/actual-outcome observation pairs (42 matched), `v_observations` `observation_type IN ('viability-prediction','actual-outcome')`.

### Secondary — contemporaneous market record
- [Computerworld / Dataquest — Consumer shipments boosted 2002 PC sales](https://www.computerworld.com/article/1573804/dataquest-consumer-shipments-boosted-2002-pc-sales.html)
- [Computerworld / IDC — Dell back on top of worldwide PC shipments (Q1 2003)](https://www.computerworld.com/article/1340039/idc-dell-s-back-on-top-of-worldwide-pc-shipments.html)
- [The Register — Dell tops up PC market in 2003 (Gateway -26%)](https://www.theregister.com/2004/01/15/dell_tops_up_pc_market/)
- [CNET / IDC — HP back on top of PC market (eMachines enters top five)](https://www.cnet.com/tech/computing/hp-back-on-top-of-pc-market/)
- [CNET — PC market hurting, but Dell grabs share](https://www.cnet.com/culture/pc-market-hurting-but-dell-grabs-share/)
- [Intel — Hyper-Threading Technology With Pentium 4 3.06 GHz (Nov 14 2002)](https://www.intel.com/pressroom/archive/releases/2002/20021114comp.htm)
- [AnandTech — Pentium 4 3.06 GHz: Hyper-Threading on Desktops](https://www.anandtech.com/show/1031)
- [Bloomberg — Flat Panels for the Masses (Jun 2003)](https://www.bloomberg.com/news/articles/2003-06-22/flat-panels-for-the-masses)
- [BGR — What happened to Gateway Computers](https://www.bgr.com/2167267/what-happened-to-gateway-computers/)
