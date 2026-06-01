# run_prescience_pass_c_v4_2.py — README

**Version**: v4.2
**Date**: 2026-05-29
**Adds over v4.1**: `--model` flag, `--study-ids` filter, raw_response capture in failures log
**Behavior**: otherwise identical to v4.1 — same prompt v2, same decoding, same tolerant validator

## Why v4.2

v4 ran the corpus on `qwen3.5:27b-mlx` and failed 100% of rows in production with `prescience_score out of range` (raw values like 85, 8, percentages) and `confidence out of range: None`. Calibration (κ=0.853) was on a single warehouseautomation study where 27b-mlx produced 68/68 clean rows. The failure is content-sensitivity drift across the diverse corpus.

v4.2 lets us swap models without writing a v5, and captures the raw model output on every failure so we can diagnose drift offline.

## Smoke test plan (today)

**Goal**: confirm `qwen3.5:35b-mlx` produces in-range scores on the same content where 27b-mlx failed.

**Two studies**:
1. `01-difranco-report-on-aberdeen-group-res-444a19` (DeFranco / Maxtor board memo, 2003-06-01)
2. `ra-warehouseautomation-3867-89c99f` (warehouse automation, the original calibration study)

**Run** (Mac):

```bash
cd ~/Desktop/Archive

nohup python3 scripts/run_prescience_pass_c_v4_2.py \
  --model qwen3.5:35b-mlx \
  --study-ids 01-difranco-report-on-aberdeen-group-res-444a19,ra-warehouseautomation-3867-89c99f \
  --tag smoke \
  > logs/pass_c_v4_2_35b_smoke.log 2>&1 &

echo $! > /tmp/pass_c_v4_2_35b_smoke.pid
tail -f logs/pass_c_v4_2_35b_smoke.log
```

**Expected outputs** (paths chosen to avoid colliding with v4):

- `~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv`
- `/tmp/pass_c_v4_2__qwen3_5_35b_mlx__smoke_checkpoint.jsonl`
- `/tmp/pass_c_v4_2__qwen3_5_35b_mlx__smoke_failures.jsonl`
- `~/Desktop/Archive/logs/pass_c_v4_2_35b_smoke.log`

**Time budget**: DeFranco has ~5 observations, warehouseautomation has ~68. ~73 rows × 35b-mlx latency. Plan for 30-60 min wall-clock.

## What to look at when it completes

```bash
# 1. Did anything score out-of-range? (Should be zero for a viable model.)
awk -F',' 'NR>1 && $3=="-1"' \
  ~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv \
  | wc -l

# 2. Score distribution
awk -F',' 'NR>1 {gsub(/"/, "", $3); print $3}' \
  ~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv \
  | sort | uniq -c | sort -rn

# 3. Confidence distribution (should be 1/2/3, no -1)
awk -F',' 'NR>1 {gsub(/"/, "", $4); print $4}' \
  ~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv \
  | sort | uniq -c | sort -rn

# 4. Inspect any failures (now includes raw_response)
cat /tmp/pass_c_v4_2__qwen3_5_35b_mlx__smoke_failures.jsonl | jq '.'

# 5. Per-study breakdown
awk -F',' 'NR>1 {gsub(/"/, "", $2); gsub(/"/, "", $3); print $2"\t"$3}' \
  ~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv \
  | sort | uniq -c | sort -k2,2 -k1,1rn
```

## Decision matrix after smoke

| 35b result on 73 rows | Next step |
|---|---|
| ≥95% in-range, no -1 sentinels | 35b is the answer. Plan the 3-study calibration sweep (warehouseautomation + DeFranco + Intel/Dell mid-importance) to confirm before corpus-wide. |
| 50-94% in-range | Still drifty. Either move to prompt v3 (explicit "MUST be 0..5") or escalate to a larger model. |
| <50% in-range | 35b isn't materially better than 27b. Need scaffolding (retry-with-correction + clamping) or a different model family. |

## Failure log schema (v4.2 — new fields)

```json
{
  "obs_id": "ra-warehouseautomation-3867-89c99f-OBS-001",
  "study_id": "ra-warehouseautomation-3867-89c99f",
  "model": "qwen3.5:35b-mlx",
  "reason": "ScoringError",
  "detail": "prescience_score out of range or wrong type: 85",
  "raw_response": "{\"prescience_score\": 85, \"confidence\": null, ...}",
  "ts_utc": "2026-05-29T20:50:00+00:00"
}
```

`raw_response` is truncated to 2000 chars. `model` is per-record so a mixed-model failures log is debuggable.

## Resume / re-run

Re-running the same command resumes from the checkpoint. To start fresh:

```bash
rm /tmp/pass_c_v4_2__qwen3_5_35b_mlx__smoke_checkpoint.jsonl
rm /tmp/pass_c_v4_2__qwen3_5_35b_mlx__smoke_failures.jsonl
rm ~/Desktop/Archive/prescience_scores_pass_c_v4_2__qwen3_5_35b_mlx__smoke.csv
```

## Mac vs. sandbox

Script lives in `/home/user/workspace/run_prescience_pass_c_v4_2.py` and is committed to `shorttack/aberdeen-group-archive/scripts/run_prescience_pass_c_v4_2.py`. Per protocol:

```bash
cd ~/Desktop/Archive/aberdeen-group-archive
git pull
cp scripts/run_prescience_pass_c_v4_2.py /Users/scott/Desktop/Archive/scripts/
```
