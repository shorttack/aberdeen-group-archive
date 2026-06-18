# Decisions Log Entry — 2026-06-18 PM-2 (v1.7.0 Ship-Gate Cleanup)

**Session focus:** Close the four must-fix findings (F2, F3, F6, F7) from the §11v Prescience Architecture Audit so v1.7.0 is fully gated for next-session Mac-side cutover.

**Repo state at session start:** archive `origin/main` at `0f5c9d71` (PRESCIENCE_ARCHITECTURE.md MAP shipped earlier today PM-1). Wiki `origin/main` unchanged from PM-1.

**Repo state at session close (PM-2):** archive `origin/main` at `a6c7a007` (docs batch). Three new commits this segment: `7935aec7` (F2), `5f945dd9` (F3+F6+F7 scripts batch), `a6c7a007` (docs batch). Wiki unchanged.

---

## Decisions

### D1 — F2: promote_pass_c_to_master_v1.py byte-aligned to Mac canonical (CLOSED)

**Question.** The repo copy of `scripts/promote_pass_c_to_master_v1.py` was the stale 207-line pre-patch version. The Mac active copy (canonical for §11v Path A — File 1 → File 2 promotion) is 211 lines and contains the §11v F2 patch (4-line provenance comment + 2-line `scorer_version`/`source_pass` default-injection at lines 151-156). Should the sandbox just commit a guess, or get the Mac active copy verbatim?

**Decision.** Pete pasted the cat output of the Mac active 211-line copy. Sandbox saved verbatim to `/home/user/workspace/promote_pass_c_to_master_v1.py`, verified byte-identity against the paste, then overwrote the repo copy via `gh api -X PUT contents/`. Commit `7935aec7`. Sandbox ↔ Mac promote script now byte-identical; future Path A promotions on Mac run against the canonical file with no surprises.

**Why this matters.** Path A (scorer-is-judge) depends on the promote script appending File 1 rows to File 2 with the correct `scorer_version=cloud_v1` and `source_pass=pass_c_cloud` tags. Pre-patch behavior left those columns empty for the runner's default invocation, which the existing File 2 rows did NOT tolerate (per `kastner-archive-pipeline` skill Pass C §"Existing File 2 rows use `scorer_version=cloud_v1`..."). The §11v patch makes the defaults explicit so Path A is replayable from a clean checkout.

### D2 — F3: row_class column on _master_prescience_scores.csv (CLOSED)

**Question.** The Pass C scoring data in `_master_prescience_scores.csv` (File 2 in the 3-file architecture) is currently 11 columns. The §11v audit (F3) flagged that the same file mixes six distinct row kinds — `scored`, `parse_fail`, `prefilter_skip`, `preseed_skip`, `no_anchor`, `pending` — without a column to discriminate them. Downstream queries must reconstruct the class from a combination of `prescience_score` (sentinel `-1` for parse_fail, empty for skips), `source_pass`, and flag columns. Should we add an explicit `row_class` enum column (option A), or keep the implicit discrimination (option B)?

**Decision.** Pete chose **A — add the column.** New 12th column `row_class` with enum `{scored, parse_fail, prefilter_skip, preseed_skip, no_anchor, pending}`. All six classes modeled, even if `no_anchor` and `pending` are zero today (they exist in v8 driver semantics for v1.7.0 SH support).

**Implementation.** Sandbox drafted `scripts/add_row_class_to_prescience_scores_v1.py` (251 LOC, dry-run default, `--commit` opt-in, `csv.QUOTE_ALL`, UTC-stamped backup before write, row-parity check, prints class distribution before/after). Classifier derives the class from existing columns (never a free-text inference): `prescience_score=-1` AND `source_pass=pass_c_cloud` → `parse_fail`; `prescience_score=-1` AND prefilter-flag set → `prefilter_skip`; `prescience_score=''` AND preseed-flag set → `preseed_skip`; etc.

**Predicted distribution** (computed from Pass C state on Mac, pre-cutover): scored=8119, parse_fail=64, prefilter_skip=4, preseed_skip=253, no_anchor=0, pending=0. Total=8,440 rows. **Pete will run F3 dry-run on Mac next session and diff the printed distribution against this prediction before `--commit`.** If counts drift, sandbox patches MASTERS_NOTES/PRESCIENCE_ARCHITECTURE/RELEASE_NOTES to reflect actual numbers.

**Why this matters.** Downstream Path A and Path B both want to query "scored rows only" for verdict math. Today that requires `WHERE prescience_score IS NOT NULL AND prescience_score != -1`. After F3 it becomes `WHERE row_class = 'scored'`. Self-documenting, robust to future sentinel-value additions.

### D3 — F6: cloud parse-fail retag (CLOSED)

**Question.** 12 rows in `_master_prescience_scores.csv` are currently tagged `source_pass=pass_c_cloud` with `prescience_score=-1` (cloud parse failures). After F3 adds `row_class`, these will show `row_class=parse_fail` AND `source_pass=pass_c_cloud`, which conflates them with the SH parse-fail bucket. Should F6 retag them to a distinct `source_pass=pass_c_cloud_parse_fail`?

**Decision.** Pete chose **A — retag.** New `source_pass=pass_c_cloud_parse_fail` value. The 12 rows get `row_class=parse_fail` (unchanged by F6, set by F3) AND `source_pass=pass_c_cloud_parse_fail` (set by F6). `parse_ok` cloud rows (the 8,119 scored ones) keep `source_pass=pass_c_cloud` unchanged.

**Implementation.** Sandbox drafted `scripts/retag_cloud_parse_fails_v1.py` (154 LOC, same invariants as F3). **Must run AFTER F3** because F3 sets `row_class`; F6 only touches `source_pass`. Surgical 12-row touch with row-parity check before/after.

**Why this matters.** v1.7.0 introduces SH (short-horizon) scoring with its own parse-fail rows tagged `pass_c_sh_parse_fail`. Without F6, cloud parse-fails and SH parse-fails would both show `source_pass='pass_c_cloud'` (cloud) or `source_pass='pass_c_sh_3y'` etc. (SH) and only `row_class=parse_fail` would distinguish them as a group from `scored`. F6 makes the source_pass taxonomy fully self-describing: `pass_c_cloud` = cloud success, `pass_c_cloud_parse_fail` = cloud failure, `pass_c_sh_3y`/`pass_c_sh_5y` = SH success, `pass_c_sh_parse_fail` = SH failure.

### D4 — F7: preseed_skip rows score normally under SH (CLOSED, decision-only)

**Question.** Preseed-skip rows are observations the LH (long-horizon, 10y window) driver deferred because of a preseed-suppression rule (e.g., the entity/tech was preseeded as low-prescience and the observation didn't override). Should the SH driver (v8, new for v1.7.0) honor that suppression and skip them too, or score them normally?

**Decision.** Pete chose **A — score normally under SH.** Rationale documented in `Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md` (89 LOC). The preseed rule is fundamentally a **long-horizon** rule: it says "this entity/tech is preseeded as low-prescience over the full 10y window, so an observation about it isn't worth scoring against that LH window unless it explicitly overrides." A 5y SH window doesn't trigger that suppression — the entity/tech might have been preseeded low at 10y but plausibly high at 3y/5y (or vice versa).

**Implications.**
- Driver v8 (for SH) does NOT honor preseed-skip flags. It scores all observations against the SH window.
- SH verdicts run in **parallel** to LH verdicts. Each study gets both an LH verdict (existing Rule A) and an SH verdict (new Rule A SH, below). The two can diverge — that's the point.
- **Rule A SH rollup** (canonical, locked):
  ```sql
  SELECT study_id,
         AVG(CASE WHEN prescience_score >= 0 THEN prescience_score END) AS mean_sh
  FROM read_csv_auto('~/Desktop/Archive/archive_masters/_master_prescience_scores.csv')
  WHERE source_pass IN ('pass_c_sh_3y', 'pass_c_sh_5y')
    AND prescience_score >= 0
  GROUP BY study_id;
  -- thresholds: >= 3.5 high, >= 2.0 medium, else low; empty -> not-applicable
  ```
- New SH source_pass taxonomy (locked for driver v8): `pass_c_sh_3y` (3-year score), `pass_c_sh_5y` (5-year score), `pass_c_sh_parse_fail` (SH parse failure, sentinel `-1`).

**No script needed in v1.7.0** — this is a semantics lock-in for when driver v8 ships. The decision doc is the artifact.

### D5 — Three batch commits via Git Data API (CLOSED, mechanics)

**Question.** F2 was a single-file overwrite (used `gh api -X PUT contents/`). The F3+F6+F7 batch (3 files: 2 new scripts + 1 new decision doc) and the docs batch (3 files: 2 overwrite + 1 new) needed atomic commits. Should sandbox use the Git Data API (blob → tree → commit → ref) or three individual `gh api -X PUT contents/` calls per batch?

**Decision.** Git Data API for both batches. Each batch is now one commit, atomic across all three files. Mac `git pull` lands all three at once — no half-state where F3 ships without F6.

**Mechanics validated this segment** (worth memorizing for future EOD batches):
```bash
HEAD_SHA=$(gh api repos/$REPO/git/ref/heads/main --jq '.object.sha')
BASE_TREE=$(gh api repos/$REPO/git/commits/$HEAD_SHA --jq '.tree.sha')
# mkblob: base64 -w0 file | python3 to {content, encoding:base64} | gh api POST blobs --jq .sha
# tree: python3 builds {base_tree, tree:[{path,mode:100644,type:blob,sha}, ...]} -> gh api POST trees --jq .sha
# commit: python3 builds {message, tree, parents:[HEAD_SHA]} -> gh api POST commits --jq .sha
# ref: python3 builds {sha:NEW_COMMIT, force:false} -> gh api PATCH refs/heads/main
```

---

## Shape audit (before / after — UNCHANGED, no masters edits this segment)

```
studies:                 1453
observations:            23926
entities:                3276
technologies:            4361
studies_with_pub_year:   1453
decades_covered:         6 (using `//` integer division)
high_prescience_studies: 865
```

v1.7.0 is a **schema-and-discipline release**, not a corpus release. Corpus shape unchanged from v1.6.2 + methodology-demo v2.0 (shipped earlier today PM-1).

---

## Commits shipped this segment

| Commit | Branch | Files | Purpose |
|---|---|---|---|
| `7935aec7` | archive/main | `scripts/promote_pass_c_to_master_v1.py` (overwrite) | **F2 closure** — byte-align to Mac §11v patch (211 lines) |
| `5f945dd9` | archive/main | `scripts/add_row_class_to_prescience_scores_v1.py` (new, 251 LOC) + `scripts/retag_cloud_parse_fails_v1.py` (new, 154 LOC) + `Perplexity_Only/F7_preseed_skip_sh_treatment_decision_v1.md` (new, 89 LOC) | **F3 + F6 + F7 closure** — scripts + decision doc |
| `a6c7a007` | archive/main | `Perplexity_Only/PRESCIENCE_ARCHITECTURE.md` (overwrite, rev2) + `Perplexity_Only/MASTERS_NOTES.md` (overwrite, v3) + `Perplexity_Only/RELEASE_NOTES_v1_7_0.md` (new, 205 LOC) | **Docs batch** — close F2/F3/F6/F7 in architecture map + masters notes; release notes for v1.7.0 with Mac-side cutover runbook |
| EOD (this commit) | archive/main | `WORKLIST.md` + `WORKLIST_2026_06_18.md` + this decisions log entry + `logs/log_entry_2026_06_18_v1_7_0_ship_gate_cleanup_v1.md` | **EOD batch** |

---

## Open follow-ups for next session

1. **v1.7.0 Mac-side cutover** (top priority next session). Sequence per `Perplexity_Only/RELEASE_NOTES_v1_7_0.md` §"Pre-flight for the v1.7.0 cutover":
   - `cd ~/Desktop/Archive/aberdeen-group-archive && git pull`
   - `cp scripts/add_row_class_to_prescience_scores_v1.py scripts/retag_cloud_parse_fails_v1.py ~/Desktop/Archive/scripts/`
   - F3 dry-run → diff distribution vs. expected (8119/64/4/253/0/0=8440) → `--commit`
   - F6 dry-run → diff against expected (exactly 12 rows touched) → `--commit`
   - Phase 1+2 rebuild on `~/Repos/kastner-aberdeen-wiki/`
   - Shape audit → must be 1453/23926/3276/4361/865-high (unchanged)
   - Surgical Phase 5 re-embed of the 3 changed `Perplexity_Only/` docs only (PRESCIENCE_ARCHITECTURE.md, MASTERS_NOTES.md, RELEASE_NOTES_v1_7_0.md) via `reembed_single_page_v1.py`
   - If counts drift from prediction: sandbox patches MASTERS_NOTES/PRESCIENCE_ARCHITECTURE/RELEASE_NOTES + ships doc-only update commit before tag
2. **Tag v1.7.0 + GitHub Release** after cutover green. Proposed title: "Multi-Horizon Prescience: row_class discipline + cloud parse-fail retag". Body: RELEASE_NOTES_v1_7_0.md.
3. **Six should-fix items NOT in v1.7.0** (per the §11v audit findings report): F1 (stray artifacts at repo root), F4 (scorer_version naming drift), F5 (1,106 cloud rows have `elapsed_sec='0.0'`), F8 (pass_c_prefilter_v1 unmodeled in v8 spec), F9, F10. Defer to v1.7.1 or v1.8.
4. **Editing gotcha** (sandbox-only): multi-edit batches with long blocks fail silently in the `edit` tool. Worked around by splitting into single edits or 2-3 small edits per call. If this persists across sessions, worth folding into agent operating procedure.
5. **Carry-forward from PM-1** (unchanged by this segment): #3 Git LFS migration plan, #4 Phase 6 template README/AGENTS/chat-starter vocabulary refresh, 4 `[DEFERRED]` prescience reconcile, tech-006.md investigation, Zenodo DOI confirmation for v1.6.1, commit signing setup, §11v KW Console v2 design, `_master_player_rebuttals.csv` move-to-root (preauthorization required).

---

_Pete's standing rule (D3 from §11v): production master moves require preauthorization. This segment touched no masters — only `Perplexity_Only/` docs, `scripts/`, and (in EOD) `WORKLIST.md`. Rule respected._
