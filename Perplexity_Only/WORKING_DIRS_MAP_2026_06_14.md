# Working Dirs Map — Pass C Prescience Scoring Archaeology

**Date discovered**: 2026-06-14 11:54 EDT
**Discovered by**: agent + Pete during v7 Qwen calibration failure root-cause hunt
**Significance**: There are **574 live + 309 abandoned working dirs** scattered across `~/Desktop/Archive`. The morning's calibration disaster (v5→v7, all failing) was caused by reinventing a manifest builder when **the entire Pass C apparatus already existed** in these dirs. This map prevents that mistake from recurring.

---

## The full inventory (from `find ~/Desktop/Archive -type d -name working`)

| Path pattern | Count | Status | What it contains |
|---|---|---|---|
| `./prepared/<study>/working` | 493 | **LIVE** | Pass C output staged on Mac, NOT yet in repo |
| `./aberdeen-group-archive/kastner-author/<study>/working` | 58 | **LIVE** | In-repo Pass C output for kastner-author studies |
| `./aberdeen-group-archive/other-authors/<study>/working` | 23 | **LIVE** | In-repo Pass C output for other-authors studies |
| `./_pass_c_abandoned_runs/20260526/prepared/<study>/working` | 309 | **ABANDONED** | May 26 Qwen 3.5 27B run. Shelved because Pete fired the agent and upgraded back from Pro to Max — agent quality, not methodology. The Qwen data itself may be salvageable. |
| **TOTAL LIVE** | **574** | | |
| **TOTAL ABANDONED** | **309** | | |

(Note: 493 + 58 + 23 = 574 live. The kastner-author subtree also has nested working dirs at `employer/aberdeen-group/<study>/working` (7), `dct/<study>/working` (2), `categories-created/<study>/working` (1), `ca-client/<study>/working` (1) — these are subsumed in the 58 count or counted twice; verify by deduping if precise count matters. Total `find` returned 574 non-abandoned.)

---

## What's inside each working dir

From sampling `./_pass_c_abandoned_runs/20260526/prepared/<study>/working/`:

```
filter_summary_v1.json           # what was skipped + why
pass_c_log_v1.jsonl              # per-obs run log
prescience_scores_27b_passC_v1.csv  # the actual model outputs
scoreable_obs_v1.csv             # obs that passed is_non_claim() filter
skipped_obs_v1.csv               # obs that failed is_non_claim() filter
```

**The CSV schema** (matches `_master_prescience_scores.csv`):
```
"obs_id","study_id","model","prescience_score","confidence","rationale",
"scored_at","scorer_version","source_pass","elapsed_sec","parse_ok"
```

**Sample row from abandoned May 26 Qwen run** (tivolisnapshot-b48230):
```
obs_id:           tivolisnapshot-b48230-OBS-001
model:            qwen3.5:27b-mlx
prescience_score: 0
confidence:       3
rationale:        "The provided claim text contains no actual prediction
                   or industry observation, only a placeholder indicating
                   an image was omitted. Without a substantive statement
                   regarding Tivoli software, IT management trends, or
                   specific technologies, it is impossible to evaluate its
                   accuracy against historical events from 1998 to 2026."
scored_at:        2026-05-26T11:42:16.135698+00:00
scorer_version:   qwen3.5:27b-mlx_passC_v1
source_pass:      pass_c
elapsed_sec:      14.32
parse_ok:         true
```

This is **exactly the same Qwen model + same prompt-style output** that v7 is trying to produce now — and it ran successfully in May.

---

## Why this matters (the lesson)

**v7 (this morning) reinvented the manifest from scratch** by sampling rows out of `_master_observations.csv` and hand-building a `claim_text` field as `metric_value`. That destroyed the calibration:

- v3 (the original working calibration driver) templated **6 fields** into a structured prompt: `study_title`, `publication_year`, `obs_id`, `observation_type`, `section`, `metric_value`
- v3 used a separate authored prompt file (`prescience_score_prompt_v2.md`) with canonical 0-5 rubric
- v3 ran the `is_non_claim()` filter upstream, producing `scoreable_obs_v1.csv` and `skipped_obs_v1.csv` as audit trail
- v3 wrote per-study working dirs that **persist as ground truth**

v7 did none of this. It pulled `metric_value` alone, fed it to Qwen as a naked one-line claim, and produced kappa ≈ 0.

**The working dirs are the ground truth.** Any future calibration attempt MUST start by reading what the working dirs already contain before writing a new manifest builder.

---

## Diagnostic answers (run 2026-06-14 11:58 EDT)

### Headline: only 204 score rows across all 574 live working dirs

| Source | Score rows |
|---|---|
| Live working dirs (574 dirs, in-repo + Mac `prepared/`) | **204** |
| `_master_prescience_scores.csv` (in repo) | **3,829** |
| Abandoned May 26 Qwen run (309 dirs) | ~unknown thousands |

**3,829 − 204 = 3,625 rows in master with no live working-dir counterpart.** Most live working dirs are upstream-only (`scoreable_obs_v1.csv`, `skipped_obs_v1.csv`, `filter_summary_v1.json`, log) with no actual scoring performed.

### Wiki postmortem is unrelated

`wiki_docs/v15_push_postmortem_v1.md` is the May 26 **wiki force-push** incident, not the Pass C abandonment. Two separate failures on the same day.

### Where did the 3,625 master rows come from?

Most likely Sonar/Claude were scored via **cloud API directly to master** (no per-study working dir needed). The 204 live working-dir rows are likely residue from later Qwen calibration smoke-tests that never got rolled up.

**The 309 abandoned May 26 Qwen working dirs are probably NOT in the master** (the abandonment was an agent-quality event before roll-up — Pete fired the agent mid-run). This means there is potentially a large reservoir of Qwen 27B scores produced by the canonical pipeline that the master has never seen.

### What the abandoned 309 dirs actually represent

Pete (2026-06-14 12:01 EDT): "May 26 abandon came because I fired the Agent and upgraded back from Pro to Max. I was getting bad output and getting nowhere."

Translation: the **scoring** wasn't necessarily bad — the **agent operating the project** was bad. The Qwen model output itself may be perfectly valid. Worth a focused audit before any v8:

```python
# Read abandoned Qwen scores, check parse_ok rate + score distribution
import csv, glob
from collections import Counter
rows = []
for f in glob.glob('/Users/scott/Desktop/Archive/_pass_c_abandoned_runs/**/working/prescience_scores*.csv', recursive=True):
    with open(f, newline='') as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
print('total rows:    ', len(rows))
print('parse_ok dist: ', Counter(r['parse_ok'] for r in rows))
print('score dist:    ', Counter(r['prescience_score'] for r in rows))
print('model dist:    ', Counter(r['model'] for r in rows))
print('version dist:  ', Counter(r['scorer_version'] for r in rows))
```

If the abandoned run has good parse_ok rate and a sensible score distribution, the right move is **harvest it into a Qwen calibration set** and skip v8 entirely — we'd already have hundreds-to-thousands of Qwen scores to compare against the Sonar/Claude master.

### Still unknown (run on Mac to confirm)

The shell diagnostics had CSV-parsing drift (awk -F'","' miscounted columns when rationale contained quoted text). Run these Python versions for ground truth:

```python
# scorer_versions and models across LIVE working dirs (Python, proper CSV)
import csv, glob
rows = []
for f in glob.glob('/Users/scott/Desktop/Archive/**/working/prescience_scores*.csv', recursive=True):
    if 'abandoned' in f: continue
    with open(f, newline='') as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
from collections import Counter
print('models:    ', Counter(r['model'] for r in rows))
print('versions:  ', Counter(r['scorer_version'] for r in rows))
print('scores:    ', Counter(r['prescience_score'] for r in rows))
print('total rows:', len(rows))
```

Resume by executing on Mac:

```bash
cd ~/Desktop/Archive

# 1. What scorer versions exist across LIVE working dirs?
find . -path "*/working/prescience_scores*.csv" -not -path "*abandoned*" \
  -exec awk -F'","' 'NR>1{gsub(/"/,"",$8); print $8}' {} \; \
  | sort | uniq -c | sort -rn

# 2. What models exist across LIVE working dirs?
find . -path "*/working/prescience_scores*.csv" -not -path "*abandoned*" \
  -exec awk -F'","' 'NR>1{gsub(/"/,"",$3); print $3}' {} \; \
  | sort | uniq -c | sort -rn

# 3. Total live rows vs the 3,829 in _master_prescience_scores.csv
find . -path "*/working/prescience_scores*.csv" -not -path "*abandoned*" \
  -exec tail -n +2 {} \; | wc -l

# 4. Read the wiki postmortem — may mention why May 26 Qwen was abandoned
cat ./aberdeen-group-archive/wiki_docs/v15_push_postmortem_v1.md
```

### Critical decision branches these answers unlock

| Scenario | What it means | v8 plan |
|---|---|---|
| **Live dirs contain Qwen rows** | Ground-truth Qwen scoring already exists. Calibrate Qwen-vs-Qwen across run dates instead of Qwen-vs-Sonar. | Skip new calibration; harvest live working dirs + score deltas |
| **Live dirs are only Sonar/Claude** | May 26 Qwen was abandoned, no live Qwen exists | v8 with `prescience_score_prompt_v2.md` + 6-field template + filtered against `_master_prescience_scores.csv` for ground truth |
| **Live rows ≈ 3,829** | Master is exactly union of live working dirs (clean lineage) | Master is source of truth, proceed with v8 |
| **Live rows >> 3,829** | Data in working dirs never made it to master (lost work) | Investigate roll-up logic before any new scoring; possible data recovery opportunity |

---

## Action items (do not skip)

1. **Read this file at the start of any prescience-related session.** Add it to `kastner-archive-pipeline` skill's "must-read" preamble.
2. **Update `kastner-archive-pipeline` skill** Gotcha 13: "Before writing any new Pass C driver or calibration manifest, `find ~/Desktop/Archive -type d -name working` and check what exists. 574 working dirs already have the answer."
3. **Update `local-model-upgrade-gates` skill** Gate 0: add "find working dirs" alongside "read OLLAMA_GOTCHAS.md".
4. **`_pass_c_abandoned_runs/20260526/` is itself a key artifact.** Pete confirmed 2026-06-14 12:01 EDT: "May 26 abandon came because I fired the Agent and upgraded back from Pro to Max. I was getting bad output and getting nowhere." The abandonment was an **agent-quality event, not a methodology event**. The 309 Qwen working dirs may still contain valid scores produced by the same Qwen 3.5 27B MLX model + same `prescience_score_prompt_v2.md` we want to use now. Audit before deleting.

---

## Connection to today's session

- v7 ran on 30 obs, kappa B1=0.091, B2=−0.269 → NO-GO
- Root cause hunt: SARS obs `claim_text` was `"~100 cases/day"` (just metric_value), not full row context
- Discovered v3 (the working driver) used 6 template fields + authored prompt v2
- Discovered the 574 + 309 working dirs map (this file)
- Stopped before answering the four unknowns above

Resume at: read the answers, decide v8 plan branch, then write driver.

---

*Saved by agent 2026-06-14 11:56 EDT per Pete's instruction "Stop and save this map in Perplexity_Only. It's gold."*
