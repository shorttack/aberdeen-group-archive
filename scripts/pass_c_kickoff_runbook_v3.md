# Bucket A+B Pass C v2 — Kickoff Runbook

**Document ID**: `pass_c_kickoff_runbook_v3`
**Date**: 2026-05-29 PM (v4 filter patch)
**For**: Pete Kastner, Mac mini M4 Pro (`scott`)
**Scope**: Bucket A+B studies under `/Users/scott/Desktop/Archive/prepared/`
**Production model**: `qwen3.5:27b-mlx` (UNCHANGED — κ=0.853 ground truth)
**Decoding params**: UNCHANGED (think=False, keep_alive=30m, num_ctx=8192, num_predict=400, temperature=0.2)
**Estimated wall clock**: ~3.6 hours (~810 obs × 16 s/obs) — expanded v4 filter allow-list (Moderate scope) over v3's 287 obs / 1.3 hr

---

## What's new in v2 vs v1

| Aspect | v1 (abandoned) | v2 (this run) |
|---|---|---|
| Bucket scope | A only (implicit) | A+B (explicit, manifest-driven) |
| Pre-filter script | `pre_filter_scoreable_obs_v1.py` | `pre_filter_scoreable_obs_v4.py` |
| Scoreable input filename | `working/scoreable_obs_v1.csv` | `working/scoreable_obs_v4.csv` |
| Runner script | `run_prescience_pass_c_v1.py` | `run_prescience_pass_c_v3.py` |
| Per-study output | `working/prescience_scores_27b_passC_v1.csv` | `working/prescience_scores_27b_passC_v2.csv` |
| Checkpoint | `prepared/pass_c_checkpoint_v1.json` | `prepared/pass_c_checkpoint_v2.json` |
| JSONL log | `working/pass_c_log_v1.jsonl` | `working/pass_c_log_v2.jsonl` |
| `source_pass` value | `pass_c` | `pass_c_v2` |
| `scorer_version` value | `qwen3.5:27b-mlx_passC_v1` | `qwen3.5:27b-mlx_passC_v2` |
| Cloud review queue | `pass_c_cloud_review_queue_v1.csv` | `pass_c_cloud_review_queue_v2.csv` |

**Model + KW prompt are unchanged.** Only the orchestration filenames and the
explicit Bucket A+B filter are new.

**Quarantine status (2026-05-29)**: 1,548 files from the abandoned v1 run were
moved to `_pass_c_abandoned_runs/20260526/`. Cron `2e191f67` will hard-delete
that quarantine on 2026-06-05.

---

## Pre-flight checklist (do this before kickoff)

### 1. Confirm Ollama is up

```
ollama list | grep qwen3.5:27b-mlx
```

You should see the model listed. If not:

```
ollama pull qwen3.5:27b-mlx
```

### 2. Pull the new scripts from the repo

```
cd /Users/scott/Desktop/Archive/aberdeen-group-archive && git pull
```

Expected output: 5 new files added under `scripts/`:

- `pre_filter_scoreable_obs_v4.py`
- `run_prescience_pass_c_v3.py`
- `roll_up_prescience_to_master_v2.py`
- `route_low_confidence_v2.py`
- `pass_c_kickoff_runbook_v2.md` (this file)

### 3. Copy to working scripts dir

```
cp scripts/pre_filter_scoreable_obs_v4.py \
   scripts/run_prescience_pass_c_v3.py \
   scripts/roll_up_prescience_to_master_v2.py \
   scripts/route_low_confidence_v2.py \
   /Users/scott/Desktop/Archive/scripts/
```

### 4. Verify the prompt file location

```
ls -l /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md
```

If it's elsewhere, note the path — you'll pass it with `--prompt`.

### 5. Sanity-check the quarantine

```
ls /Users/scott/Desktop/Archive/_pass_c_abandoned_runs/20260526/ | wc -l
ls /Users/scott/Desktop/Archive/prepared/working/ 2>/dev/null || true
find /Users/scott/Desktop/Archive/prepared -name 'scoreable_obs_v1.csv' | head -5
find /Users/scott/Desktop/Archive/prepared -name 'prescience_scores_27b_passC_v1.csv' | head -5
find /Users/scott/Desktop/Archive/prepared -name 'pass_c_checkpoint_v1.json' | head -5
```

Expected: quarantine has ~1,548 files; the four `find` calls return nothing or
only return files inside the quarantine subtree.

---

## Step 1: Run the v4 pre-filter across Bucket A+B (dry-run first)

```
python3 /Users/scott/Desktop/Archive/scripts/pre_filter_scoreable_obs_v4.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --dry-run
```

**Expected (within ~10 seconds)**: A table with one row per Bucket A+B study
showing total observations, scoreable, skipped. Bottom line should be
roughly **~810 scoreable obs** across **~309 studies** (A=135 + B=174).
If the count is wildly off (e.g., zero, or 30,000), stop and tell me.

The ~810 estimate reflects the v4 filter's expanded observation_type
allow-list (added `market-forecast`, `market-assessment`, `competitive-assessment`,
`analytical-claim` after 2026-05-29 live audit). The earlier ~2,562 estimate
was a master-CSV upper bound; the actual prepared/ corpus is smaller.

Then commit the filter outputs for real:

```
python3 /Users/scott/Desktop/Archive/scripts/pre_filter_scoreable_obs_v4.py \
  --root /Users/scott/Desktop/Archive/prepared
```

This writes `working/scoreable_obs_v4.csv`, `working/skipped_obs_v4.csv`, and
`working/filter_summary_v4.json` into each Bucket A+B study directory. It also
writes `prepared/_bucket_audit_v4.csv` summarizing the overall bucket
distribution. Idempotent — safe to re-run.

**Bucket scope is configurable** but defaults to `A,B` per the 2026-05-25
decision memo:

```
# only Bucket A
python3 .../pre_filter_scoreable_obs_v4.py --root ... --bucket-filter A

# Bucket A+B+D
python3 .../pre_filter_scoreable_obs_v4.py --root ... --bucket-filter A,B,D
```

---

## Step 2: Pass C v2 dry-run (no Ollama calls)

```
python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v3.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  --dry-run
```

**Expected (within ~5 seconds)**: Lists the studies it would process (only
those with a `working/scoreable_obs_v4.csv` from Step 1) plus a total scoreable
count and an ETA in hours (should be ~3.6 hours at ~810 obs × 16 s/obs).
No Ollama calls, no writes. Checkpoint file is also untouched.

If the dry-run says "0 studies with scoreable_obs_v4.csv", you skipped Step 1
— go back and run the filter for real.

---

## Step 3: 2-study smoke test (skip if explicitly authorized to go straight to full run)

> **Pete's standing directive 2026-05-29**: "I believe we are starting clean
> on Pass C. No smokiest, for instance." → **Skip Step 3 by default.**
> The dry-run in Step 2 is sufficient confirmation.

If you want a smoke test anyway:

```
python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v3.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  --max-studies 2
```

Per-study output and checkpoint behaviors are identical to v1 (see v1 runbook
§Step 3 for spot-check commands; substitute `_v2` for `_v1` everywhere).

---

## Step 4: Full Pass C v2 kickoff

```
nohup python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v3.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  > /Users/scott/Desktop/Archive/pass_c_v2_run.log 2>&1 &
```

Then write down the PID:

```
echo "PID: $!"
```

You should see two lines: the `&` job spec and the `PID: NNNNN` echo within
1 second.

### Monitoring while it runs

Tail the log:

```
tail -f /Users/scott/Desktop/Archive/pass_c_v2_run.log
```

Press Ctrl-C to detach (the run keeps going — `nohup` ensures it survives
your terminal closing).

Checkpoint snapshot:

```
cat /Users/scott/Desktop/Archive/prepared/pass_c_checkpoint_v2.json | python3 -m json.tool
```

Look for `completed_studies` count growing and `in_progress.last_obs_idx`
advancing.

### Killing it cleanly

```
kill <PID>
```

The runner writes the checkpoint and exits. **Safe to restart with the same
command** — it will resume from the checkpoint.

---

## Step 5: After Pass C v2 completes

### 5a. Roll up to the 8th master

```
python3 /Users/scott/Desktop/Archive/scripts/roll_up_prescience_to_master_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --masters-dir /Users/scott/Desktop/Archive/archive_masters \
  --dry-run
```

Expected: prints row count it would write (~2,562 — matching total obs scored)
and a cross-check against `_master_observations.csv` (23,605 canonical obs_ids
in v1.5). Orphans should be 0.

Then for real (creates `_master_prescience_scores.csv` and snapshots any
prior version to `archive_masters_pre_prescience_rollup_v2_<ts>/`):

```
python3 /Users/scott/Desktop/Archive/scripts/roll_up_prescience_to_master_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --masters-dir /Users/scott/Desktop/Archive/archive_masters
```

### 5b. Build the cloud review queue

```
python3 /Users/scott/Desktop/Archive/scripts/route_low_confidence_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --build-queue
```

Expected: ~75–100 rows in `pass_c_cloud_review_queue_v2.csv` (based on
calibration's ~2 of 68 ≈ 3% rate scaled to ~2,562 obs).

Then bring the queue back to me (Computer) in a fresh session, and I'll do
the cloud scoring. You'll then run:

```
python3 /Users/scott/Desktop/Archive/scripts/route_low_confidence_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --apply
```

to fan results back into per-study `prescience_scores_cloud_review_v2.csv`
files, then re-run the v2 rollup to merge cloud-review rows into the master.

---

## Recovery scenarios

### Mac reboots / loses power mid-run

Re-run the same `nohup ...` command. Checkpoint picks up where it left off,
including mid-study (resumes the in-progress study from `last_obs_idx + 1`).

### Ollama crashes

Pass C will log `urllib.error.URLError` errors and mark those rows
`parse_ok=false` with empty score. Restart Ollama:

```
brew services restart ollama  # or however you start it
ollama run qwen3.5:27b-mlx ""  # warm the model
```

Then restart Pass C v2 with the same command. Failed rows will need to be
re-scored manually if you want to recover them.

### Parse rate drops below 95%

Stop the run (`kill <PID>`), tail the log for the offending
`raw_response` snippets, paste them to me. Usually a prompt edge case.

---

## What "done" looks like

- `completed_studies` in checkpoint has ~309 entries (Bucket A+B)
- `_master_prescience_scores.csv` has ~2,562 rows
- Cross-check orphans against `_master_observations.csv` = 0
- Cloud review queue applied and merged (~75–100 cloud rows)
- Decisions log appended with kickoff and completion timestamps
- Per-study CSVs preserved in `prepared/<study>/working/` (never deleted —
  forever-archive principle)

---

## Tell me

When you've finished Step 4 (kickoff), drop me a one-liner: "kicked off v2,
PID NNNNN, ETA HH:MM." I'll mark the roadmap and set up the cloud review
session for whenever Pass C v2 lands.
