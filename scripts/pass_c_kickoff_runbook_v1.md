# Bucket A Pass C — Kickoff Runbook

**Document ID**: `pass_c_kickoff_runbook_v1`
**Date**: 2026-05-25
**For**: Pete Kastner, Mac mini M4 Pro (`scott`)
**Scope**: All studies under `/Users/scott/Desktop/Archive/prepared/`
**Production model**: `qwen3.5:27b-mlx`
**Estimated wall clock**: ~45 hours

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
- `pre_filter_scoreable_obs_v1.py`
- `run_prescience_pass_c_v1.py`
- `roll_up_prescience_to_master_v1.py`
- `route_low_confidence_v1.py`
- `pass_c_kickoff_runbook_v1.md` (this file, in docs/ or scripts/)

### 3. Copy to working scripts dir

```
cp scripts/pre_filter_scoreable_obs_v1.py scripts/run_prescience_pass_c_v1.py scripts/roll_up_prescience_to_master_v1.py scripts/route_low_confidence_v1.py /Users/scott/Desktop/Archive/scripts/
```

### 4. Verify the prompt file location

```
ls -l /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md
```

If it's elsewhere, note the path — you'll pass it with `--prompt`.

---

## Step 1: Run the pre-filter across all studies (dry-run first)

```
python3 /Users/scott/Desktop/Archive/scripts/pre_filter_scoreable_obs_v1.py --root /Users/scott/Desktop/Archive/prepared --dry-run
```

**Expected (within ~10 seconds)**: A table with one row per study showing
total observations, scoreable, skipped. Bottom line `TOTAL` should be roughly
**~9,000–10,000 scoreable** across ~124 studies. If the count is wildly off
(e.g., zero, or 30,000), stop and tell me.

Then commit the filter outputs for real:

```
python3 /Users/scott/Desktop/Archive/scripts/pre_filter_scoreable_obs_v1.py --root /Users/scott/Desktop/Archive/prepared
```

This writes `working/scoreable_obs_v1.csv`, `working/skipped_obs_v1.csv`, and
`working/filter_summary_v1.json` into each study directory. Idempotent — safe
to re-run.

---

## Step 2: Pass C dry-run (no Ollama calls)

```
python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  --dry-run
```

**Expected (within ~5 seconds)**: Lists the studies it would process plus a
total scoreable count and an ETA in hours (should be ~38–45 hours). No
Ollama calls, no writes. Checkpoint file is also untouched.

---

## Step 3: 2-study smoke test

Before committing to the 45-hour run, verify the runner end-to-end on the
**first 2 studies**.

```
python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  --max-studies 2
```

**Expected (within ~35–60 minutes for two ~75-obs studies)**:
- Progress lines like `[ 1/75] OBS-001  score=4  14.8s  ok=True`
- A 5-second pause every 10 observations
- Per-study CSV at `prepared/<study>/working/prescience_scores_27b_passC_v1.csv`
- Log lines at `prepared/<study>/working/pass_c_log_v1.jsonl`
- Checkpoint at `prepared/pass_c_checkpoint_v1.json` updated after every 5 obs

**Spot-checks to run after smoke test**:

```
# Confirm 2 studies completed
cat /Users/scott/Desktop/Archive/prepared/pass_c_checkpoint_v1.json | python3 -m json.tool | head -20

# Sample a few scored rows
head -5 /Users/scott/Desktop/Archive/prepared/<first-study-name>/working/prescience_scores_27b_passC_v1.csv

# Parse rate
python3 -c "
import csv
with open('/Users/scott/Desktop/Archive/prepared/<first-study-name>/working/prescience_scores_27b_passC_v1.csv') as f:
    rows = list(csv.DictReader(f))
ok = sum(1 for r in rows if r['parse_ok'] == 'true')
print(f'{ok}/{len(rows)} parse_ok ({100*ok/len(rows):.1f}%)')
"
```

Parse rate target: ≥95%. If lower, paste the log file and stop.

---

## Step 4: Full Pass C kickoff

Once smoke test looks clean:

```
nohup python3 /Users/scott/Desktop/Archive/scripts/run_prescience_pass_c_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --prompt /Users/scott/Desktop/Archive/prescience_score_prompt_v2.md \
  > /Users/scott/Desktop/Archive/pass_c_run.log 2>&1 &
```

Then write down the PID:

```
echo "PID: $!"
```

After pasting, press Enter on an empty line if needed. You should see two lines:
the `&` job spec and the `PID: NNNNN` echo within 1 second.

**The checkpoint already accounts for the 2 studies completed in smoke test.**
The full run will skip them and continue.

### Monitoring while it runs

Tail the log:

```
tail -f /Users/scott/Desktop/Archive/pass_c_run.log
```

Press Ctrl-C to detach (the run keeps going — `nohup` ensures it survives
your terminal closing).

Checkpoint snapshot:

```
cat /Users/scott/Desktop/Archive/prepared/pass_c_checkpoint_v1.json | python3 -m json.tool
```

Look for `completed_studies` count growing and `in_progress.last_obs_idx`
advancing.

### Killing it cleanly

```
kill <PID>
```

The runner traps SIGTERM/SIGINT, writes the checkpoint, and exits. **Safe to
restart with the same command** — it will resume from the checkpoint.

---

## Step 5: After Pass C completes

### 5a. Roll up to the new 8th master

```
python3 /Users/scott/Desktop/Archive/scripts/roll_up_prescience_to_master_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --masters-dir /Users/scott/Desktop/Archive/archive_masters \
  --dry-run
```

Expected: prints row count it would write. Should be roughly equal to total
obs scored across all studies.

Then for real (creates `_master_prescience_scores.csv` and snapshots any
prior version):

```
python3 /Users/scott/Desktop/Archive/scripts/roll_up_prescience_to_master_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --masters-dir /Users/scott/Desktop/Archive/archive_masters
```

### 5b. Build the cloud review queue

```
python3 /Users/scott/Desktop/Archive/scripts/route_low_confidence_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --build-queue
```

Expected: ~100–300 rows in `pass_c_cloud_review_queue_v1.csv` (based on
calibration's ~2 of 68 ≈ 3% rate scaled to ~9,000 obs).

Then bring the queue back to me (Computer) in a fresh session, and I'll do
the cloud scoring. You'll then run:

```
python3 /Users/scott/Desktop/Archive/scripts/route_low_confidence_v1.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --apply
```

to fan results back into per-study files, then re-run the rollup to merge
cloud-review rows into the master.

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

Then restart Pass C with the same command. Failed rows will need to be
re-scored manually — easiest path is a one-off `--single-study` flag (not
implemented in v1; tell me if you want it for v2).

### Parse rate drops below 95%

Stop the run (`kill <PID>`), tail the log for the offending
`raw_response` snippets, paste them to me. Usually a prompt edge case.

---

## What "done" looks like

- `completed_studies` in checkpoint has ~124 entries
- `_master_prescience_scores.csv` has ~9,000 rows
- Cloud review queue applied and merged
- Decisions log appended with kickoff and completion timestamps
- Per-study CSVs preserved in `prepared/<study>/working/` (never deleted —
  forever-archive principle)

---

## Tell me

When you've finished Step 4 (kickoff), drop me a one-liner: "kicked off,
PID NNNNN, smoke test parse rate XX%." I'll mark the roadmap and set up the
cloud review session for whenever Pass C lands.
