# The Aberdeen *PC Deals* Weekly Reports, 2002–2003: A Data-Driven Study of Consumer PC Price Tracking at an Inflection Point — Version 2

**A heterogeneous analysis of the Kastner Aberdeen Archive *PC Deals* corpus, rebuilt on a model-grade re-extraction (`-mx`) and combined with the contemporaneous market record**

Author: Prepared for Peter S. Kastner
Date: June 28, 2026
Supersedes: [Version 1 (June 27, 2026)](./PC_Deals_Study_v1.md)
Method: Read-only DuckDB queries against the rebuilt Kastner Aberdeen Wiki (`kastner.duckdb`, 27 `v_*` views) over the **model-extracted `-mx` *PC Deals* sub-corpus**, cross-referenced with the contemporaneous trade and analyst record (Gartner/Dataquest, IDC, CNET, Intel, Computerworld, The Register).

> **What changed since v1, in one sentence.** Version 1 read a *legacy* extraction layer that kept the nouns (vendors, chips, price points) and silently dropped the reasoning, the quantified deltas, and the named-SKU deals; its own [Section 6 A:B audit](./PC_Deals_Study_v1.md) measured a **0-for-4 capture rate on the highest-value content.** Version 2 reads the **`-mx` model-extraction layer** that was built specifically to repair those losses — so the four flagship facts v1 could only describe from prose are now first-class, queryable observations. See [§0 Why Version 2 is better](#0-why-version-2-is-better) and the companion [LESSONS_LEARNED.md](./LESSONS_LEARNED.md).

---

## 0. Why Version 2 is better

Version 1 was honest about its own foundation. Its closing section ran a controlled A:B audit of the structured layer against the full source text and reached an uncomfortable verdict: **"capture rate is inversely correlated with interpretive value."** The legacy ingest captured entities at nearly 100% but scored **0-for-4** on the four richest facts in the sampled studies — the HP 573n price hike, the Dell 2300 upgrade inference, the March-17 reference architecture, and the Centrino "Your Next Desktop is a Laptop" milestone. v1's frequency tables were sound as a map of analyst *attention* but, by construction, could not reconstruct analyst *judgment*.

That audit became a work order. The [`expand-pc-deals` model-extraction re-ingest](./FULL_RUN_REPORT.md) re-read every PC Deals study with a model-grade reader (the agent, not a scripted extractor), repaired the loss modes, and wrote a parallel `-mx` study set into the masters. Version 2 is the same analysis rebuilt on that repaired layer. Concretely, v2 is better on five measurable axes:

| Axis | Version 1 (legacy A-side) | Version 2 (`-mx` model-extraction) | Evidence |
|---|---|---|---|
| **High-value facts captured** | 0 of 4 as structured facts | **4 of 4** as structured, typed, queryable observations | [§3.8](#38-the-facts-v1-could-not-see-now-structured); [LESSONS_LEARNED.md](./LESSONS_LEARNED.md) |
| **Junk rows (fragments/placeholders/phantoms)** | 299 of 1,014 rows were junk (~29%) | **0** across all 50 `-mx` studies | [FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md) |
| **Foreign-key density (PC Deals set)** | 435 entity + 363 tech links | **557 entity + 556 tech** links on fewer, cleaner rows | live DuckDB (`v_observations`) |
| **Prescience coverage** | most weeklies never scored | **13 studies scored**, 8 receiving their *first-ever* verdict | [v1_v2_comparison_report.md](./v1_v2_comparison_report.md) |
| **Forecast vs. fact separation** | facts scored as if predictions → inflated "high" verdicts | typed extraction parks facts at "cannot-assess"; 3 inflated highs corrected to medium | [v1_v2_comparison_report.md](./v1_v2_comparison_report.md) |

The headline reframing: the count of observations *fell* (1,006 legacy PC Deals rows → 725 `-mx` rows) **and that is the improvement.** The legacy layer was padded with 299 truncated fragments, placeholders, and phantoms; removing them while simultaneously recovering reasoning and densifying the relational graph is exactly the loss-mode repair working as designed ([FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md)). Fewer rows, more truth.

This study directory bundles the full evidentiary chain so the improvement is auditable end to end:

- [PC_Deals_Study_v1.md](./PC_Deals_Study_v1.md) — the original analysis and its self-audit.
- [PC_Deals_Study_v2.md](./PC_Deals_Study_v2.md) — this document.
- [LESSONS_LEARNED.md](./LESSONS_LEARNED.md) — the synthesis: the loss taxonomy v1 discovered, and exactly how the `-mx` re-ingest fixed each mode, with before/after counts.
- [SMOKE_TEST_REPORT.md](./SMOKE_TEST_REPORT.md) — the 3-study proof run (L7 per-SKU journeys, phantom kill).
- [FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md) — the 50-study re-extraction and its quality gate.
- [v1_v2_comparison_report.md](./v1_v2_comparison_report.md) — the head-to-head prescience-scoring comparison on the 13 scored studies.

---

## Abstract

Between July 2002 and August 2003, the Aberdeen Group Digital Consumer Technology (DCT) practice published a weekly retail price tracker, *PC Deals*, scoring the best name-brand consumer desktop bargains across a fixed grid of price points. This study treats that 14-month run as a structured dataset. Version 2 rebuilds the analysis on the **model-extracted `-mx` sub-corpus** — **50 re-read studies carrying 725 faithful observations** — replacing the legacy layer whose fragment-padding and table-collapse v1's own audit had exposed. The quantitative structure of the repaired archive corroborates and sharpens the qualitative narrative: Dell dominates analyst attention and the market alike, the post-merger HP/Compaq entity is the clear number two, and a value tier of eMachines, Sony, and Gateway clusters behind, with the three national big-box chains — Best Buy, CompUSA, Circuit City — as the locus of *bundled* value. Against the external record, the period emerges as a genuine inflection point: Dell's direct-model price leadership, the HP-Compaq brand consolidation, the AMD Athlon XP value insurgency, the DDR-displaces-RDRAM memory transition, the November 2002 arrival of Pentium 4 Hyper-Threading, and the collapse of LCD flat panels from luxury to mainstream. Crucially, where v1 could only *describe* the era's sharpest moments from prose, v2 can *query* them: the HP 573n's 58% one-week price hike, Dell's "free-upgrade" pricing inference, the Enterprise Reference Desktop spec, and the Centrino "your next desktop is a laptop" milestone now exist as discrete, typed, prescience-scored observations. A rerun of the forecast-verification layer through the Pass C scorer shows v2 trading a handful of inflated "high" verdicts for honest "mediums" while minting first-ever verdicts on studies the legacy pass abandoned — verdict quality up in both directions.

---

## 1. Introduction and motivation

Most surviving artifacts of the early-2000s PC price war are aggregate: quarterly shipment shares from Gartner/Dataquest and IDC, vendor earnings, and journalistic retrospectives. What is comparatively rare is a **high-frequency, point-of-sale view of the consumer desktop market captured contemporaneously, week by week, by a working industry analyst** — and rarer still one preserved in machine-readable form. The Aberdeen *PC Deals* corpus is exactly that. Its stated purpose was a weekly retail price tracker identifying the best deals on name-brand PCs from Compaq, Dell, eMachines, Gateway, HP, and Sony across nine price-point targets from roughly $550 to over $1,550, with "winners" chosen on processor speed, memory size and bandwidth, hard-drive capacity, optical drives, and bundled monitor/printer components, and adjusted for shipping, instant savings, and mail-in rebates to find true cost (the methodology charter, `dct-about-weekly-pc-deals-2002-mx`).

This study asks: **treated as data, what does the *PC Deals* run teach us that the prose alone does not?** Version 1 answered that the structured layer turns impressionistic claims into countable evidence — but its own audit found that the *legacy* structured layer dropped the most interpretively valuable material. **Version 2 asks the question again against a structured layer that no longer drops it.** The answer is stronger: with the reasoning, the deltas, and the named-SKU deals now structured, the corpus reads not only as a record of analyst *attention* but as an auditable record of analyst *judgment*.

---

## 2. Data and method

### 2.1 The archive

The Kastner Aberdeen Wiki exposes a 27-view DuckDB query layer over master CSV tables (`_master_studies`, `_master_observations`, `_master_entities`, `_master_technologies`, and their join tables). Following the overnight rebuild of 2026-06-28, the full archive baseline is **1,504 studies / 24,715 observations / 3,293 entities / 4,376 technologies**, with 876 high-prescience studies. The *PC Deals* material lives inside the `dct` (Digital Consumer Technology) collection.

### 2.2 Defining the weekly sub-corpus — and the `-mx` re-extraction

The `dct` bucket mixes practice-methodology decks, webinars, vendor briefings, and company snapshots with the price tracker proper. The 50 PC Deals studies (weeklies + business-deals editions + processor/business price series + notebook/lineup + shipments/replacement-market pieces) were re-read end to end by a model-grade extractor and written back into the masters with a **`-mx` suffix**, so the repaired rows sit *parallel* to the originals for live A:B querying. **Version 2 restricts to that `-mx` set: 50 studies carrying 725 observations**, spanning 2002-07 through 2003-08.

For comparison, the legacy ("A-side") PC Deals rows total 1,006 observations across 42 studies. The 281-row difference is not lost analysis — it is the removal of 299 junk rows (truncated fragments, quota-padding placeholders, phantoms) partly offset by genuine new content recovered from dense tables that the legacy pass *under*-extracted. The net is **fewer rows, zero junk, and a denser, better-typed relational graph** ([FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md)).

### 2.3 Observation structure

In the `-mx` layer, observations are typed — and, critically, the typing is *trustworthy*, because the model-grade pass classified each statement against its source framing rather than miscasting facts as forecasts. The distribution across the 50 `-mx` studies:

| observation_type | count |
|---|---:|
| market-data | 502 |
| expert-opinion | 178 |
| topic-insight | 23 |
| viability-prediction | 22 |

This distribution is itself a finding. *PC Deals* is overwhelmingly a market-pricing corpus, so a large `market-data` plurality is correct; the comparatively small `viability-prediction` count (22) is the *honest* yield of genuine forward-looking claims, after the legacy pass's habit of dressing descriptive facts as predictions was removed. The legacy v1 distribution reported 46 `viability-prediction` and 42 paired `actual-outcome` rows — but v1's own audit (L6) showed several of those "predictions" were shipping-policy statements and price hikes mis-typed, and the paired `actual-outcome` rows were partly retrospective reconstructions. v2's leaner prediction count is the price of honesty.

Price points are still extracted as commentary-anchored snippets where the source is narrative, but where the source is tabular the `-mx` pass preserves the relationship (model → price → delta → date) instead of shredding it — the single largest repair (see [§3.8](#38-the-facts-v1-could-not-see-now-structured) and [LESSONS_LEARNED.md](./LESSONS_LEARNED.md)). The corpus remains a curated editorial record, not a complete price database — a limitation the reports themselves acknowledged, comparing volatile online pricing to airline-ticket pricing (`dct-weekly-2003-03-02-mx`).

### 2.4 External corroboration

Structured findings were checked against the contemporaneous record: Gartner/Dataquest and IDC shipment-share data via Computerworld and CNET, Intel's own launch press, and trade coverage of LCD pricing and the Gateway/eMachines endgame. These are cited inline below.

---

## 3. Findings

### 3.1 Temporal cadence — the calendar drives the deals

The retail calendar is visible in the data itself: the **December 2002 holiday spike** and the **February 2003 post-holiday dead zone** bracket the run. The reports are explicit that the calendar, not the technology, sets the rhythm — back-to-school (July–August) and the holidays produced the most offers, while the corpus names the "Dads and Grads" early-summer lull and the "slow summer months" before the August "Back to School shopping frenzy" (`dct-weekly-2003-06-15-mx`). The holiday optimism was misplaced: the December 30, 2002 report opens by noting "this year's holiday season's sales yielded the lowest rate of growth in decades. Frankly, PC Deals is not surprised" (`dct-weekly-2002-12-30-mx`).

### 3.2 PC vendors — Dell's gravity, HP's weight, and the value tier

Dell's dominance of *analyst attention* in the corpus mirrors its dominance of the *market*: Dell held roughly **27.9–28% of U.S. PC shipments in 2002**, comfortably ahead of HP at ~19.8% ([Computerworld/Dataquest](https://www.computerworld.com/article/1573804/dataquest-consumer-shipments-boosted-2002-pc-sales.html)), and retook the worldwide lead from HP in Q1 2003 on 24.7% unit growth ([Computerworld/IDC](https://www.computerworld.com/article/1340039/idc-dell-s-back-on-top-of-worldwide-pc-shipments.html)). The corpus captures the *mechanism* behind that share — relentless, opportunistic pricing — better than any quarterly number can. In the `-mx` layer that mechanism is now legible at the SKU level: Dimension prices that "jolted upwards in some cases over $200" between weeks (`dct-weekly-2002-11-03-mx` records the Dimension 2300 jumping **$709 → $848**) alternating with aggressive cuts (`dct-weekly-2003-08-24-mx`: Dell cuts "ranging from 6% in consumer desktops to 22% for business servers," forcing Gateway to drop its 500-series by $100 in response).

The value tier is where the repaired archive adds the most nuance. **eMachines** appears as the under-$1,000 value winner, sourced primarily through Best Buy ("eMachines… wins on — ta, dah — low price, according to store managers," `dct-weekly-2002-12-15-mx`; "lots of features for not a lot of cash," `dct-weekly-2003-07-06-mx`). The external record vindicates this: eMachines' budget momentum carried it into the **top five U.S. PC vendors by end of 2003, surpassing Gateway and Apple** ([CNET/IDC](https://www.cnet.com/tech/computing/hp-back-on-top-of-pc-market/)) — and the brand's strength was such that Gateway acquired eMachines in 2004 ([BGR](https://www.bgr.com/2167267/what-happened-to-gateway-computers/)).

**Gateway**, conversely, is the cautionary tale. The corpus first criticizes its static pricing and absence of bundles, then watches it diversify into electronics retail ("the Gateway logo is showing up more and more at online storefronts," `dct-weekly-2003-01-05-mx`) and finally cut PC prices to compete (`dct-weekly-2003-08-24-mx`). The external arc is harsher than the contemporaneous reports could see: Gateway fell to ~3.5% U.S. share in 2003 as its PC business shrank 26% ([The Register](https://www.theregister.com/2004/01/15/dell_tops_up_pc_market/)), closed dozens of Gateway Country stores, and was ultimately acquired by Acer in 2007 ([BGR](https://www.bgr.com/2167267/what-happened-to-gateway-computers/)).

### 3.3 The retail channel — bundles belong to the big boxes

The three national chains — Best Buy, CompUSA, Circuit City — appear in a near-dead heat across the corpus. The structural finding is the **direct-vs-retail split**: manufacturer sites (Dell, HP, Gateway) offered competitive bare-system prices and free shipping, but the best *bundled* deals (PC + monitor + printer) were almost exclusively at the national chains, paired with $100–$400 mail-in rebates and 12–24-month no-interest financing (`dct-weekly-2003-01-26-mx`, `-07-26-mx`, `-08-10-mx`). The chains played distinct roles the data exposes: **Best Buy** as the primary channel for eMachines and Sony; **CompUSA** as the liquidator, "continuing to sell 'older' PC models after Best Buy and Circuit City had removed them" (`dct-weekly-2003-06-15-mx`, `-07-26-mx`). The August 2003 back-to-school surge is visible as a sudden bloom of chain circulars (`dct-weekly-2003-08-03-mx`). The Circuit City presence is poignant in hindsight — the chain the corpus treats as a co-equal value leader would liquidate entirely by 2009.

### 3.4 Configuration and technology — what a "winning" machine contained

The configuration story of the era reads with unusual economy off the `-mx` technology links. The **Pentium 4 is the spine** of the mainstream pick, but the **combined AMD Athlon/Athlon XP footprint rivals it** — a quantitative fingerprint of the AMD value insurgency the prose celebrates ("AMD ruled the retail ads this week with an abundance of Athlon machines at great prices… competitive machines that cost less than their Intel counterparts," `dct-weekly-2002-11-03-mx`). The corpus explicitly framed AMD Athlon as the value answer to Intel Celeron in the sub-$900 band.

The **memory transition is legible**: DDR SDRAM has decisively displaced RDRAM, matching the period's industry shift away from Rambus's premium, royalty-encumbered memory. The corpus notes RDRAM machines cost "about $200 more than comparable DDR" and flags high-performance RDRAM Pentium machines as a segment "improving the least."

The corpus also captures **Pentium 4 Hyper-Threading in real time**. Intel launched the 3.06 GHz P4 with HT on **November 14, 2002** ([Intel press release](https://www.intel.com/pressroom/archive/releases/2002/20021114comp.htm); cf. [AnandTech](https://www.anandtech.com/show/1031)) — and the archive carries a dedicated special report dated **that exact day** explaining the feature (`dct-weekly-2002-11-14-p4-ht-mx`). The reports then track HT's price descent until, by May 2003, HT had fallen far enough that *PC Deals* "decided to eliminate the separate Hyper-Threading category" and fold HT machines in with regular P4s (`dct-weekly-2003-05-18-mx`) — a structural editorial change driven by price compression. (Notably, the `-mx` re-read of this study **removed the phantom "Intel Pentium 4-M (Mobile)" technology** that the legacy layer had fabricated — see [§3.8](#38-the-facts-v1-could-not-see-now-structured).)

Finally, the **emergence of the living-room PC**: Microsoft's Windows Media Center PC appears, with HP's m200 Media Center series launching "under $999" in June 2003 (`dct-weekly-2003-06-22-mx`), and **LCD flat panels** transition from luxury to mainstream over the run — dropping from $700–$1,000 toward under $500 by early 2003, consistent with the broader trade narrative of flat panels moving "for the masses" through 2003 ([Bloomberg](https://www.bloomberg.com/news/articles/2003-06-22/flat-panels-for-the-masses)).

### 3.5 Price bands — compression and bifurcation

The **$900 band is the gravitational center** of the mainstream consumer market in this period — the most-discussed system price point by a wide margin. The narrative arc is one of **compression at the bottom and bifurcation at the top**: early 2003 saw "an explosion of affordable options in the under-$900 category" driven by AMD value (`dct-weekly-2003-04-06-mx`, `-01-12-mx`), while the previously "hot" $1,200–$1,400 mid-high bands "diminished to sparse pickings" as deals migrated to a new "over $1,600 range" for media-centric and gaming systems (`dct-weekly-2003-03-23-mx`). The middle of the market hollowed out: buyers either traded down into newly-cheap sub-$900 machines or up into media/gaming systems above $1,600.

### 3.6 The "bang for the buck" methodology — now a structured spec

The corpus's editorial signature is the phrase "bang for the buck." In v1, the most explicit codification — the reference configuration for "best combination of price, value, and longevity" — survived only inside one truncated free-text blob. In the `-mx` layer it is **structured as discrete fields** (`dct-business-2002-12-17-pc-deals-mx`): Aberdeen upgrades its reference spec from a 2.0 GHz to a **2.4 GHz P4 (533 MHz FSB vs. 400 MHz)**, with a full summary row — "P4 2.4 GHz 533 MHz FSB; 256 MB DDR (min); 7200 RPM 40 GB HDD; CD-ROM; no floppy; 15/17in LCD; 10/100 Eth; WinXP Pro SP1; 3yr NBD; Office XP; AV." The component priorities are now queryable rather than buried: a memory-tier threshold (128 MB significantly slower than 256 MB; multimedia = 512 MB), a hard-drive preference (faster 7200 RPM over bigger), and a flat-panel aspiration.

### 3.7 The forecast-verification layer — reading *PC Deals* as analyst judgment

The archive's most analytically distinctive feature is its forecast/outcome structure: near-term calls paired with retrospective assessments of how they played out. **Version 2's decisive advance is that this layer was re-scored through the Pass C prescience scorer on the `-mx` extraction**, producing the first apples-to-apples comparison of verdict quality between the two ingests ([v1_v2_comparison_report.md](./v1_v2_comparison_report.md)).

Of the 50 `-mx` studies, **13 carry Pass C verdicts** under the rule locked 2026-06-27 (mean of assessable scores 1–5; 0 = "cannot assess" excluded; ≥3.5 high, ≥2.0 medium):

| `-mx` study | verdict |
|---|---|
| dct-business-2003-03-17-pc-deals-mx | high |
| dct-traveling-with-centrino-2003-05-mx | high |
| dct-weekly-2002-10-27-mx | high |
| dct-weekly-2002-11-03-mx | high |
| dct-weekly-2002-11-17-mx | high |
| dct-apple-powermac-g5-2003-06-mx | medium |
| dct-intel-processor-prices-2003-01-mx | medium |
| dct-pc-replacement-insight1-2003-04-mx | medium |
| dct-weekly-2002-11-14-p4-ht-mx | medium |
| dct-weekly-2002-12-22-mx | medium |
| dct-weekly-2003-01-05-mx | medium |
| dct-weekly-2003-01-19-mx | medium |
| dct-why-aberdeen-follows-pc-deals-2002-mx | medium |

Three results matter. **(1) Coverage:** 8 of these 13 received their *first-ever* Pass C verdict — the legacy pass had never scored the weeklies at all. **(2) False-positive correction:** of the 5 studies scored under both ingests, the legacy pass rated all five "high"; v2 corrects three to "medium" because typed extraction lets the scorer park descriptive market-data facts at "cannot-assess" instead of rewarding them like fulfilled predictions. **(3) Yield:** the assessable denominator rises 1.25×–3.5× per study, so the verdicts that remain rest on a broader, better-classified base ([v1_v2_comparison_report.md](./v1_v2_comparison_report.md)).

The substantive pattern v1 identified survives and is now better-grounded: **Kastner's short-horizon, mechanism-level calls (next week's circular volume, a chip moving into a price band, a brand's pricing posture) were reliably accurate; the longer-horizon strategic calls (where a struggling brand would land) were directionally right but optimistic about the loser's fate.** The Centrino "more than 10% of corporate clients in 2004" prediction (`dct-business-2003-03-17-pc-deals-mx`) — a genuine, forward-looking, now-structured `viability-prediction` — is the cleanest scorable instance of the analyst's strong near-to-mid-horizon judgment.

### 3.8 The facts v1 could not see, now structured

This section has no analogue in v1 — it could not, because the facts did not exist as data. v1's audit named **four flagship facts** that the legacy layer failed to capture as structured observations (a 0-for-4 rate). All four are now present in the `-mx` layer:

1. **The HP 573n price hike (the largest in PC Deals history).** v1 had the fragments "$900" and "$1,418" as disconnected window-slices and mis-filed the event as a "prediction." The `-mx` layer carries it as one clean `market-data` observation: *"HP 573n (Athlon 2600+, 512 MB): sold at Staples last week for $900; this week costs $1,418 at HP Online — the largest price hike recorded in PC Deals history"* (`dct-weekly-2002-12-30-mx`). The 58% one-week swing — a specific machine, two retailers, two prices — is now queryable.
2. **The Dell upgrade inference.** v1 lost both the prices and the reasoning. The `-mx` layer records the Dimension 2300's **$709 → $848** jump as structured `market-data` (`dct-weekly-2002-11-03-mx`), restoring the empirical hook for the analyst's read that "Dell is collecting the price of its 'free' upgrades somewhere else in its configuration."
3. **The Enterprise Reference Desktop spec.** In v1 this existed only inside one truncated blob (loss mode L2). It is now two clean structured fields capturing both the spec and the upgrade rationale (`dct-business-2002-12-17-pc-deals-mx`; see [§3.6](#36-the-bang-for-the-buck-methodology--now-a-structured-spec)).
4. **The Centrino "Your Next Desktop is a Laptop" milestone.** v1 reduced the most prescient passage in the sample to a single truncated fragment, and the milestone sentence itself returned zero structured hits. The `-mx` layer carries the launch date (March 12, 2003), a platform description, a strategic-importance assessment ("Most important Intel introduction of 2003"), **and the scorable corporate-adoption prediction** (`dct-business-2003-03-17-pc-deals-mx`) — which the Pass C scorer rates among the strongest calls in the corpus.

The asymmetry v1 lamented is inverted: the material that was *most likely to be lost* is now *reliably captured*, because the re-read targeted exactly the interpretive content the scripted pass blinkered.

---

## 4. Discussion — what the deep dive teaches

**1. The repaired archive validates the qualitative summary and now also reconstructs the judgment.** Every major claim in the corpus-level narrative has a countable structural footprint — and, unlike v1, the *reasoning* behind those claims (causal inferences, quantified deltas, named-SKU deals) is now structured too. The data no longer merely disciplines the prose; it preserves the argument.

**2. *PC Deals* is a rare high-frequency ground-truth complement to quarterly share data.** Gartner/IDC tell us *that* Dell gained share and eMachines broke into the top five; the *PC Deals* corpus shows *how* — week by week, at the point of sale, through specific machines, rebates, and financing terms.

**3. The period is a genuine inflection point, and the tracker caught it.** 2002–2003 compressed the HP-Compaq integration, the Dell direct-model apex, the Gateway decline and eMachines ascent, the AMD value challenge, the RDRAM-to-DDR shift, the P4 Hyper-Threading debut, and the LCD democratization into 14 months. The corpus is a contemporaneous eyewitness to all of them.

**4. The forecast layer is now a *scored* study of analyst calibration.** Re-running Pass C on the typed `-mx` extraction converts v1's qualitative read ("short-horizon accurate, long-horizon optimistic") into graded verdicts on 13 studies, with disclosed denominators — short-horizon mechanism calls scoring high, strategic-endgame calls scoring lower.

**5. Extraction fidelity is itself a research result.** The single most transferable lesson from this project is methodological: a year of model progress, applied to a faithful re-read, can buy back the exact content a scripted pass silently dropped — and the gap is measurable. That story is told in full in [LESSONS_LEARNED.md](./LESSONS_LEARNED.md).

**6. The bundle is the unit of consumer value, not the box.** The single most actionable lesson for the 2002–2003 mass-market buyer encoded in the data: true value lived in the national-chain bundle (system + monitor + printer + rebate + financing), not the manufacturer's bare-system web price.

---

## 5. Limitations

- **Editorial, not exhaustive.** The corpus is a curated record of *notable* weekly deals, not a complete price database. Even after the `-mx` repair, where the source is narrative the price points are commentary-anchored.
- **Online pricing volatility.** The reports themselves disclaim 24/7 coverage of fast-moving online prices (`dct-weekly-2003-03-02-mx`).
- **Window-bounded.** Coverage runs late 2002 through August 2003; the longer arcs (Gateway's collapse, Circuit City's bankruptcy, eMachines' absorption) are supplied here from the external record, not the archive.
- **Single-analyst voice.** The commentary and forecasts reflect one analyst's framing; the forecast-verification layer's retrospective assessments are authored after the fact.
- **`-mx` is a re-extraction, not a new source.** The `-mx` layer recovers content the source *contained* but the legacy pass dropped; it cannot add facts the analyst never wrote. The Access per-SKU price-journey rebuild (L7), proven in the [smoke test](./SMOKE_TEST_REPORT.md) at 249 journeys, is staged but not yet promoted into the live masters analyzed here (the live `dct-access-pc-deals-2002-2003` study still carries its 122-row legacy aggregation); promoting it is the natural next step.

---

## 6. Conclusion

Read as data, the Aberdeen *PC Deals* weekly run is far more than a price newsletter. Its 50 re-extracted studies and 725 faithful observations form a dated, cross-referenced, point-of-sale chronicle of the U.S. consumer desktop market at one of its most consequential moments — and, for the first time, the structured archive preserves not just *what* was discussed but *what was argued*. Dell's gravitational pull on analyst attention matches its market dominance; the value tier of eMachines, Sony, and Gateway is quantitatively distinct from it; the big-box chains own the bundle; AMD's Athlon footprint rivals the Pentium 4's; and a Pass C–scored forecast layer reveals an analyst who read the weekly tape with precision but underestimated how badly the era's losers would fare. Version 2's deepest contribution is methodological: by rebuilding the analysis on a model-grade re-extraction that repaired the very loss modes v1 had diagnosed, it demonstrates that corpus fidelity is not fixed at ingest time — it can be measured, and bought back. The four facts v1 could only describe, v2 can query.

---

## Sources

### Primary — Kastner Aberdeen Archive, `-mx` model-extraction layer (DuckDB `v_studies`/`v_observations`/`v_entities`/`v_technologies`)
- Methodology charter — `dct-about-weekly-pc-deals-2002-mx`; practice rationale — `dct-why-aberdeen-follows-pc-deals-2002-mx`
- 50 re-extracted weekly/business *PC Deals* studies, 2002-08 through 2003-08, incl. the Nov 14 2002 P4-HT special (`dct-weekly-2002-11-14-p4-ht-mx`), the Dec 30 2002 holiday post-mortem with the HP 573n hike (`dct-weekly-2002-12-30-mx`), the Dec 17 2002 reference-spec upgrade (`dct-business-2002-12-17-pc-deals-mx`), the Mar 17 2003 Centrino milestone (`dct-business-2003-03-17-pc-deals-mx`), the Mar 23 2003 price-band bifurcation (`dct-weekly-2003-03-23-mx`), and the May 18 2003 HT-category retirement (`dct-weekly-2003-05-18-mx`).
- Pass C prescience verdicts on 13 `-mx` studies (scorer `run_prescience_pass_c_v7.py`, verdict rule locked 2026-06-27).

### Companion documents (this study directory)
- [PC_Deals_Study_v1.md](./PC_Deals_Study_v1.md) · [LESSONS_LEARNED.md](./LESSONS_LEARNED.md) · [SMOKE_TEST_REPORT.md](./SMOKE_TEST_REPORT.md) · [FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md) · [v1_v2_comparison_report.md](./v1_v2_comparison_report.md)

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
