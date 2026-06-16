# Decisions Log — 2026-06-16 — SH ≤2015 Sweep, Sentinel Refactor, Eras Findings (Draft)

**Session:** §11v Phase 0 follow-on → Phase 1 sweep → eras study v1 draft
**Status:** Sweep + reclass + gates COMPLETE. Findings draft pending Pete review.

---

## Decisions Made Today

### D1 — Anchor cutoff for the SH sweep set at ≤ 2015
- **Rationale:** "fits within the arc of the observations" (Pete). ≥ 11 years elapsed since anchor for the most recent rows.
- **Result:** 8,659 eligible observations.
- **Cost ceiling raised to $500** for this session to absorb the full sweep.

### D2 — Calibration-first run before full sweep
- 100-obs stratified sample (20 buckets, seed 20260615) confirmed sweep would pass v2 acceptance gates G1–G10 before committing $$.
- 0 HARD fails at calibration → green-lit full sweep.

### D3 — Schema extension applied to `_master_observations.csv`
- 17 cols → 31 cols (14 new SH-related columns).
- Backup written: `~/Desktop/Archive/archive_masters/_master_observations.csv.bak_pre_sh_extend_20260616T071946Z`
- Pre-SHA `9427887d…` → Post-SHA `83f97b38e49ca9e1b2738197ea3a1b63c1bae87b1ac4a07a3e9f72af43674bb6`

### D4 — Sentinel scheme locked at three values, plus -2 reserved
- `0–5`: valid Sonar score
- `-1`: parse_fail:malformed (true parser failure)
- `-2`: pending (window not elapsed) — reserved, not used in this sweep
- `-99`: content_unrecoverable (Sonar refusal where the model declined to score)
- **Pete's choice on -99** (vs reusing -1 or -3): preserves the distinction between "parser broke" and "model refused" for future archive-hygiene work.

### D5 — Refusal reclassification done post-hoc, not in driver
- Driver v8 emitted -1 for both true parse failures and Sonar refusals.
- Post-hoc script `reclassify_sonar_refusals_v1.py` walked the 27 -1 rows, classified 16 as refusals (→ -99) and retained 11 as true parse_fail (→ -1).
- Pre-reclass file SHA `adb0e22e…`, post-reclass `ba99b96e…`.
- Refusal manifest persisted: `Perplexity_Only/sh_sweep_le_2015_refusal_manifest_v1.csv`
- **Follow-on (deferred):** bake the -99 distinction into Driver v9 to avoid the post-hoc step on future sweeps.

### D6 — Per-author analysis (T2) deferred to a separate future study
- Original hypothesis doc had three tests (era, author, methodology).
- T2 (author ranking / Kastner-accuracy) deliberately deferred to its own study, separate framing.
- Current eras study scope is era + methodology only.

### D7 — Anchor cutoff for the eras analysis tightened from ≤2015 to ≤2007
- **Rationale:** Pete Kastner left Aberdeen in June 2007. Post-departure Aberdeen output is of unknown provenance from Pete's perspective ("who knows what happened? I'm not paying to find out").
- ≤ 2007 cohort: **n = 8,381** (97.7% of sweep).
- ≥ 2008 cohort: 202 obs retained in sweep CSV but **not analyzed** in this study.
- Slight imprecision noted: anchor_year is integer, June 2007 cut is approximated by anchor_year ≤ 2007 (overcounts last 6 months of 2007 Aberdeen output by ~unknown amount; immaterial to findings).

### D8 — Study framing pivoted from "era decline" to "methodology, not era"
- **Original hypothesis:** Aberdeen analyst quality declined monotonically across decades.
- **Result of T1:** Pattern is NOT monotonic. 1990s reads highest (mean 3.15), 2000s lowest (2.75), 1970s and 1980s between.
- **Critical confound identified by Pete:** the archive's *recovery mechanism* differs by decade — pre-2006 obs survived because Pete retained personal copies (himself + immediate colleagues); 2006–2007 surge reflects Wayback Machine archiving Aberdeen's public web output. This is **author-presence bias**.
- **Result of T3:** `industry-analysis` (n=4,528, 53% of methodology-tagged sample) scores structurally lowest among major methodologies at mean 2.69, 38.8% high-prescience share. This is a within-archive, within-author finding that survives the author-presence bias confound.
- **Reframed finding:** The methodology finding (T3) is the cleaner result. The era finding (T1) is reported with the bias mechanism named explicitly, but the report declines to use it to claim era-level prescience effects.
- **Pete's correction logged:** "Pete kept the good studies" framing rejected — Pete has ingested everything he has, good and bad, and let machine scoring assign prescience. The bias is *author-presence* (retention), not *curation* (quality selection).

### D9 — Kastner 2006–2007 SOA content explicitly acknowledged
- Per Pete: "Kastner's 2006–2007 SOA content stands alone as excellent content in any event."
- §6 of the findings doc dedicated to this acknowledgment, ensuring the report's emphasis on the methodology finding is not read as diminishing the late-Kastner-era content.

---

## Findings Doc Status

**Draft:** `/home/user/workspace/study_findings_prescience_decline_aberdeen_eras_v1.md` (228 lines, 19.4KB)
**Target path on commit:** `Archive/decisions/study_findings_prescience_decline_aberdeen_eras_v1.md`
**Status:** Shared to Pete for review. Will commit after sign-off, possibly with revisions.
**Framing decision (B):** Both T1 and T3 reported with full transparency on author-presence bias. T1 not used to make era claims. T3 stands as the cleaner finding.

---

## Sweep + Reclass + Gates Summary (Final)

| Metric | Value |
|---|---|
| Sweep duration | 619.7 min (10.3h) |
| Total rows scored | 8,659 |
| Valid scores (post-reclass) | 8,632 |
| -99 content_unrecoverable | 16 |
| -1 parse_fail:malformed | 11 |
| -2 pending | 0 |
| 3y mean (overall) | 2.867 |
| 5y mean (overall) | 2.953 |
| Score 4+5 share (3y) | 43.4% |
| Divergence rate | 24.4% |
| Gates HARD fails | 0 |
| Gates soft flags | 2 (G2c 3y, G8b — both read healthy given G3b/G9/G10) |

---

## Open Items at EOD

1. Findings doc review + commit (pending Pete sign-off)
2. Driver v9 — bake -99 sentinel into driver natively
3. Methodology code normalization pass (492 codes → cleaner taxonomy)
4. 16-obs archive-hygiene pass (use refusal manifest as worklist)
5. Tier B Pass C still running at 83.5% as of EOD (PID 2163)
6. archival-ingest skill v21 — register `archive-meta` as 7th Kastner collection (deferred from earlier in session)
7. The deferred T2 / Kastner-accuracy study — separate future deliverable
