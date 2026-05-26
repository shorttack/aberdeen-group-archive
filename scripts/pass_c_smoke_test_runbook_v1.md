# Pass C — 2-study smoke test runbook v1

**Goal:** Verify the production driver (`run_prescience_pass_c_v1.py`) works end-to-end against the real masters + qwen3.5:27b-mlx + the v2-filtered scoreable obs CSVs, BEFORE committing to the ~12 hr full Bucket A+B run.

**Scope:** Two studies, one large, one small. Both Bucket A.

| Role           | Study slug                       | Scoreable obs | ~Time @16s/obs |
| -------------- | -------------------------------- | ------------- | -------------- |
| Large stress   | `ra-warehouseautomation-3867-89c99f` | 68            | ~18 min        |
| Small canary   | `09010005-d36601`                    | 4             | ~1 min         |

Combined: **72 obs, ~19 min**. Lets you verify checkpointing, resume-on-crash, parse-rate, and JSON shape without burning the night.

## Pre-flight (90 seconds)

```bash
cd ~/Desktop/Archive/aberdeen-group-archive && git pull
```

Should fetch `drop_duplicate_3910_v1.sh` and the decisions log update.

```bash
bash scripts/drop_duplicate_3910_v1.sh
```

Expected output: `Already moved — ...prepared_dropped_dups/... exists, nothing to do.` (Idempotent — already moved by hand.)

## Step 1 — Real-pass v2 pre-filter (writes scoreable_obs_v1.csv per study)

The earlier audit was a `--dry-run`. The real pass writes `working/scoreable_obs_v1.csv` into each kept study so the driver has something to read.

```bash
python3 scripts/pre_filter_scoreable_obs_v2.py \
  --root ~/Desktop/Archive/prepared \
  --bucket-filter A,B \
  2>&1 | tee ~/Desktop/Archive/logs/pre_filter_v2_$(date -u +%Y%m%dT%H%M%SZ).log | tail -3
```

Expected within ~30 sec:

```
TOTAL              3290    2723     567  (kept: 309, filtered_out: 184, no_obs: 0, no_manifest: 0)
Audit written → /Users/scott/Desktop/Archive/prepared/_bucket_audit_v2.csv
```

Verify two of the working files exist:

```bash
ls -la ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/scoreable_obs_v1.csv \
       ~/Desktop/Archive/prepared/09010005-d36601/working/scoreable_obs_v1.csv
```

Both should be present, non-zero bytes.

## Step 2 — Pre-flight Ollama check (10 sec)

```bash
ollama list | grep qwen3.5:27b-mlx
ollama ps | head
```

Expected: model listed; nothing currently loaded is fine, the driver will warm it.

## Step 3 — Smoke run, large study first (18 min)

```bash
cd ~/Desktop/Archive/aberdeen-group-archive
python3 scripts/run_prescience_pass_c_v1.py \
  --study ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f \
  --model qwen3.5:27b-mlx \
  --prompt ~/Desktop/Archive/prescience_score_prompt_v2.md \
  --out ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/prescience_scores_v1.csv \
  2>&1 | tee ~/Desktop/Archive/logs/passc_smoke_warehouse_$(date -u +%Y%m%dT%H%M%SZ).log
```

What you should see within first 60 sec:
- `Loaded prompt v2 from ...`
- `Loaded N=68 scoreable obs from working/scoreable_obs_v1.csv`
- `Warming model qwen3.5:27b-mlx ...`
- First score line: `[1/68] obs=... score=... conf=... t=12.4s parse_ok=True`

Mid-run checkpoints to watch:
- **Throughput:** ~12-18 s/obs. If you see >25 s/obs sustained, hit Ctrl+C and re-run — likely a thermal throttle or another process competing.
- **Parse rate:** `parse_ok=True` rate should be 100% based on calibration. If any `parse_ok=False` show up, log them but keep going — the driver writes them with the rationale field set to the raw response for the cloud reviewer.
- **Throttle pause:** every 10 obs you'll see "throttle 5s" — that's by design.

After completion:
- Tail of log shows `Done. 68/68 scored. Parse rate: 68/68 (100.0%). Elapsed: ~18m.`
- Output CSV `working/prescience_scores_v1.csv` has 68 data rows + header.

## Step 4 — Resume-on-crash test (optional but worth 30 sec)

After the warehouse run, simulate an interrupted run on the canary by deleting half the output rows, then re-running:

```bash
# Manually edit the canary's output to remove last 2 of 4 rows, then re-run
python3 scripts/run_prescience_pass_c_v1.py \
  --study ~/Desktop/Archive/prepared/09010005-d36601 \
  --model qwen3.5:27b-mlx \
  --prompt ~/Desktop/Archive/prescience_score_prompt_v2.md \
  --out ~/Desktop/Archive/prepared/09010005-d36601/working/prescience_scores_v1.csv
```

You should see `Found N=2 already-scored obs in output. Resuming at obs 3/4.`

Skip this step if you'd rather just run the canary clean — it's 4 obs, 1 minute.

## Step 5 — Canary run (small, 1 min)

```bash
python3 scripts/run_prescience_pass_c_v1.py \
  --study ~/Desktop/Archive/prepared/09010005-d36601 \
  --model qwen3.5:27b-mlx \
  --prompt ~/Desktop/Archive/prescience_score_prompt_v2.md \
  --out ~/Desktop/Archive/prepared/09010005-d36601/working/prescience_scores_v1.csv
```

Expected: 4/4 scored, <90 sec elapsed.

## Step 6 — Sanity-check the two output CSVs

```bash
head -1 ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/prescience_scores_v1.csv
wc -l ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/prescience_scores_v1.csv
wc -l ~/Desktop/Archive/prepared/09010005-d36601/working/prescience_scores_v1.csv

# Score distribution
cut -d, -f4 ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/prescience_scores_v1.csv \
  | sort | uniq -c

# Confidence distribution
cut -d, -f5 ~/Desktop/Archive/prepared/ra-warehouseautomation-3867-89c99f/working/prescience_scores_v1.csv \
  | sort | uniq -c
```

Expected header columns (11): `obs_id, study_id, model, prescience_score, confidence, rationale, scored_at, scorer_version, source_pass, elapsed_sec, parse_ok`

Expected: 69 lines (header + 68) for warehouse; 5 lines (header + 4) for canary.

Score distribution should span 0-5 with a peak around 2-3. Confidence 1 (low) should be the smallest bucket — most rows confidence 2 or 3.

## Step 7 — Paste results back

Paste back to me:
1. The tail of each log (last 5 lines)
2. The two `wc -l` outputs
3. The score + confidence distributions for the warehouse study

I'll review for any anomalies. If clean, **kickoff the full run** with `nohup` overnight, est. ~12.1 hrs, scoring 309 studies / 2,723 observations.

## If something goes wrong

| Symptom                              | Likely cause                                 | Fix                                                             |
| ------------------------------------ | -------------------------------------------- | --------------------------------------------------------------- |
| `FileNotFoundError: scoreable_obs`   | Step 1 wasn't run                            | Run Step 1                                                      |
| `model not found`                    | Wrong model tag                              | `ollama pull qwen3.5:27b-mlx`                                   |
| First obs takes >60 sec              | Cold model + cold disk cache                 | Wait 90s, then look for second obs — should drop to 12-18s      |
| Parse rate <95%                      | Prompt regression                            | Stop, check `prescience_score_prompt_v2.md` matches calibration |
| Driver crashes mid-study             | OOM / thermal                                | Re-run same command — checkpoint will resume                    |
| All scores cluster at 0 or 5         | Prompt drift / wrong model                   | Stop, verify model tag & prompt SHA vs calibration record       |

## Files referenced

- `scripts/run_prescience_pass_c_v1.py` — driver
- `scripts/pre_filter_scoreable_obs_v2.py` — bucket-aware pre-filter
- `~/Desktop/Archive/prescience_score_prompt_v2.md` — prompt
- `~/Desktop/Archive/logs/` — all run logs land here
