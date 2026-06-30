# Lessons Learned: Extraction Fidelity in the *PC Deals* Corpus

**How Version 1's self-audit became a work order — and how the `-mx` model-extraction re-ingest repaired every loss mode it found**

Prepared for: Peter S. Kastner
Date: June 28, 2026
Companions: [PC_Deals_Study_v1.md](./PC_Deals_Study_v1.md) · [PC_Deals_Study_v2.md](./PC_Deals_Study_v2.md) · [SMOKE_TEST_REPORT.md](./SMOKE_TEST_REPORT.md) · [FULL_RUN_REPORT.md](./FULL_RUN_REPORT.md) · [v1_v2_comparison_report.md](./v1_v2_comparison_report.md)

---

## The premise, in one sentence

A year of model progress means re-reading the same studies with a far better reader recovers facts, structure, and reasoning that the original *scripted* ingest silently dropped — so we re-pay the ingest cost to buy back **fidelity**, not just schema-compliance.

The extraction brain this time was the **agent** doing model-grade reading, not a patched script. The `archival-ingest` v20 skill contributed only the packaging skeleton (the 5-CSV schema, `datapackage.json`, the directory layout, the `obs_id` format). New rows were written with a **`-mx` suffix** so they sit *parallel* to the originals for live A:B comparison in DuckDB — nothing was overwritten.

---

## 1. What Version 1 discovered (the diagnosis)

[Version 1's Section 6](./PC_Deals_Study_v1.md) ran a controlled A:B audit: the **A side** was the legacy structured extraction (CSV rows); the **B side** was the authoritative full text (`source/original_text.md`). It read seven studies line-by-line against their sources and reached a single, uncomfortable verdict:

> **Capture rate is inversely correlated with interpretive value.**

The legacy pass captured entities and technologies at nearly 100% but scored **0-for-4** on the four richest facts in the sample. It kept the *nouns* (vendors, chips, price points) and dropped the *reasoning, specificity, and narrative causation* — exactly the material a historian most wants. v1 catalogued the mechanical failures behind that asymmetry as a six-mode loss taxonomy (L1–L6); the `expand-pc-deals` re-ingest later added L7 for the dense-table case.

---

## 2. The loss taxonomy — and how `-mx` repaired each mode

The table below is the heart of this document: each loss mode v1 diagnosed, the repair strategy, and the **measured before/after** from the [smoke test](./SMOKE_TEST_REPORT.md) (3 studies) and [full run](./FULL_RUN_REPORT.md) (50 studies).

| Code | Loss mode (v1 diagnosis) | Repair (`-mx` strategy) | Before → After |
|---|---|---|---|
| **L1** | **Window-fragment truncation** — `metric_value` stored as a fixed-width character slice beginning/ending mid-word ("uct line as Intel rolls out…") | Read the source; author the *clean, complete* sentence as the fact | Smoke: 14 → **0**. Full run: 288 front-sliced fragments → **0** |
| **L2** | **Relational collapse of tables** — a price table shredded into disconnected single-value rows, destroying the model→price→delta mapping | Detect tables; preserve row relationships as discrete, typed records | The Mar-17 reference grid that was 9 fragments is now clean structured fields; per-SKU journeys carry first/last/min/max/delta (L7) |
| **L3** | **Quota padding / placeholder rows** — empty stubs ("see original_text.md", confidence `low`) inserted to hit a row count | Never emit a row to reach a target; delete placeholders | Smoke: 3 → **0**. Full run: 8 → **0** |
| **L4** | **Duplicated source spans** — the same sentence copied verbatim across rows (often one per linked technology) | One claim, one row; separate the claim text from entity/tech *links* | Duplicate-source spans removed across the sample; FK links replace copy-rows |
| **L5** | **Phantom entities/technologies** — a row for something never in the source | Verify every entity/tech against the source string; kill fabrications | Smoke: 1 phantom ("Intel Pentium 4-M (Mobile)") → **0**, replaced with the real Pentium M the doc discusses |
| **L6** | **Type miscasting** — a non-forecast sentence stored as `viability-prediction`; a price hike filed as a prediction | Type each claim against the source's own framing; reserve `viability-prediction` for genuine forward-looking claims | Smoke: 1 → **0**. Full run: 3 phantom `actual-outcome` rows → **0**; honest `viability-prediction` count falls from 46 (legacy) to 22 (`-mx`) |
| **L7** | **Lossy over-aggregation of dense tabular source** — the Access DB flattened to monthly averages | Emit one observation per PCmaker×SKU **price journey** | Smoke: 122 monthly averages → **249 per-SKU journeys** (staged; not yet promoted to live masters) |

### The aggregate repair (full 50-study run)

| Metric | Legacy A-side | `-mx` B-side |
|---|---:|---:|
| Total observation rows | 1,014 | **725** |
| — of which junk (fragment + placeholder + phantom) | **299** | **0** |
| — real content | 715 | **725** |
| Foreign-key links (entity + tech) | 911 | **1,113** (+202) |

**Fewer rows, more truth.** The B-side has *slightly more* faithful observations than the A-side had *real* ones (725 vs. 715), with every fragment, placeholder, and phantom removed and the relational graph densified by 202 links. On the PC Deals query set specifically, the live DuckDB confirms the densification: the `-mx` rows carry **557 entity + 556 tech** links versus the legacy **435 entity + 363 tech**, on ~28% fewer rows.

---

## 3. The blinder effect, reversed — the four flagship facts

v1's deepest finding was *semantic*: the material an extractor drops is disproportionately the material a historian most wants. The four worked examples that had **no structured representation** on the A-side are now first-class observations in the `-mx` layer:

| Flagship fact | v1 status (legacy) | v2 status (`-mx`) |
|---|---|---|
| **HP 573n price hike** — $900 at Staples → $1,418 at HP Online, "largest hike in PC Deals history" (58% in one week) | fragments "$900"/"$1,418" as separate slices (L1); event mis-filed as prediction (L6) | one clean `market-data` observation with machine, both retailers, both prices, and the editorial superlative (`dct-weekly-2002-12-30-mx`) |
| **Dell upgrade inference** — Dimension 2300 $709 → $848; "Dell is collecting the price of its 'free' upgrades elsewhere" | neither prices nor inference survived | the $709→$848 jump is structured `market-data`, restoring the empirical hook (`dct-weekly-2002-11-03-mx`) |
| **Enterprise Reference Desktop spec** — P4 2.4 GHz/533 FSB, 256 MB DDR min, 7200 RPM, 15–17" LCD, WinXP Pro SP1, 3-yr NBD | existed only inside one truncated free-text blob (L2) | two clean structured fields: the spec summary *and* the 2.0→2.4 GHz upgrade rationale (`dct-business-2002-12-17-pc-deals-mx`) |
| **Centrino "Your Next Desktop is a Laptop" milestone** — March 12 2003, >10% of corporate clients in 2004 | reduced to a single truncated fragment (L1); milestone sentence returned **zero** structured hits | launch date + platform description + strategic-importance assessment + a scorable `viability-prediction` (`dct-business-2003-03-17-pc-deals-mx`) |

**0-for-4 → 4-for-4.** The asymmetry v1 lamented is inverted, because the re-read targeted exactly the interpretive content the scripted pass blinkered.

---

## 4. The downstream payoff — prescience scoring honesty

Repairing extraction did not just recover facts; it made the **forecast-verification layer trustworthy**. Re-running Pass C on the typed `-mx` extraction ([v1_v2_comparison_report.md](./v1_v2_comparison_report.md)) showed three effects:

1. **Coverage win** — 8 of 13 studies got their *first-ever* Pass C verdict; the legacy pass had never scored the weeklies.
2. **False-positive correction** — of the 5 studies scored both ways, the legacy pass rated all five "high"; v2 corrects three to "medium." Root cause: the legacy pass blurred descriptive market-data into the prediction pool, so a fact that happened to align with reality was rewarded like a fulfilled forecast. Typed extraction parks those facts at **0 = cannot-assess** and judges only genuine predictions.
3. **Prediction-yield increase** — the assessable denominator rises 1.25×–3.5× per study, so the verdicts that remain rest on a broader, better-classified base.

The pivotal rule learned this session: **score 0 means "cannot assess" (too vague / a market-data fact / unknowable), not "failed prediction."** Excluding 0 from the verdict mean is what separates predictions from facts — and it is only *possible* because `-mx` typing tells them apart. v1's extraction could not.

---

## 5. Transferable principles for corpus construction

These are the durable, project-independent lessons — the guidance any future high-fidelity research corpus should adopt:

1. **Treat tabular source as tabular.** The single largest loss (L2) comes from running narrative-prose extractors over embedded tables. Detect tables first; ingest typed records so SKU→price relationships survive.
2. **Store spans by offsets, never fixed-width slices.** L1 truncation is gratuitous; capture the clean sentence, not a byte window.
3. **Abolish quota padding.** A study with five real observations yields five rows. Placeholders (L3) pollute frequency analysis with phantom mass and should fail validation.
4. **One claim, one row; deduplicate spans.** Linking a sentence to three technologies produces three *links*, not three copies (L4).
5. **Validate every entity/technology against the source string.** A name absent from the text (even as a synonym) is a phantom (L5).
6. **Type-check claims with the source's own framing.** Future tense/modal verbs gate `viability-prediction`; statements of present policy do not (L6). Mis-typing corrupts the forecast-verification layer.
7. **Capture the number with its referent and the claim with its warrant.** Numeric deltas ("$709→$848"), test results, and causal inferences need dedicated attention — that is what lets the structured layer represent *argument*, not just *topic*.
8. **Keep the full text first-class and audit against it.** The only reason this calibration was possible is that the archive preserves `source/original_text.md` beside every package. Periodic A:B sampling should be standing QA, not a one-off.

The meta-lesson: **the extractor's silent editorial choices are themselves historical data.** Knowing a pipeline keeps entities and drops reasoning tells a future researcher exactly how far to trust any query run against the tables. And — the new lesson from this project — **that boundary is not fixed.** A faithful re-read with a better reader can move it, and the movement is measurable.

---

## 6. Deliverable boundary and provenance

Per Pete's cost-control rule, the agent's deliverable ends at **validated 5-CSV packages + the A:B comparison + these reports**. The well-proven, cheaper local jobs run on the Mac: masters merge (versioned/`-mx`-suffixed, coexisting with originals), Pass C scoring + roll-up, wiki rebuild + re-embedding, and this report rewrite.

- All 50 `-mx` packages passed the v20 CSV Validation Gate with **0 failures** (column counts 16/9/9/12, controlled vocab valid, `csv.QUOTE_ALL` enforced, `obs_id` format + uniqueness, full FK integrity).
- Live shape verified against the rebuilt `kastner.duckdb` (27 `v_*` views) on 2026-06-28: 50 `-mx` studies / 725 observations / 502 market-data + 178 expert-opinion + 23 topic-insight + 22 viability-prediction.
- The Access per-SKU journey rebuild (L7, 249 journeys) is proven in the [smoke test](./SMOKE_TEST_REPORT.md) and staged, but not yet promoted into the live masters — the natural next step.
