# run_prescience_pass_c_v4.py — README

## What it does

Scores **every** observation in `_master_observations.csv` (~23,605 rows) for prescience using local `qwen3.5:27b-mlx` via Ollama. No bucket filter, no shape filter, no observation_type filter. Same prompt that produced κ=0.853 calibration (`prescience_score_prompt_v2.md`).

## Why corpus-wide (architectural decision 2026-05-29)

Pass C v1 (cloud LLM) scored the full corpus. v2/v3 attempted to pre-filter to "scoreable" predictions to save credits. v4 reverts to corpus-wide because:

1. **Local Qwen costs no credits.** The filter saved nothing valuable; it destroyed signal.
2. **Drift analysis requires same-corpus comparison.** v1 cloud scores already exist; Qwen scores on the same rows enable a clean v1-vs-Qwen drift study across all 23,605 obs. Pre-filtering breaks the comparison.
3. **Forever-archive principle.** Extract everything, slice later. Filter-then-rescore is irretrievable.

## Inputs

- `~/Desktop/Archive/archive_masters/_master_observations.csv` — every obs
- `~/Desktop/Archive/archive_masters/_master_studies.csv` — title + pub_year for prompt context
- `~/Desktop/Archive/prescience_score_prompt_v2.md` — system + user template (κ=0.853 calibrated)

## Outputs

| Path | Format | Purpose |
|---|---|---|
| `~/Desktop/Archive/prescience_scores_pass_c_v4.csv` | CSV, QUOTE_ALL | Per-obs scores: `obs_id, study_id, prescience_score, confidence, rationale, model, prompt_version, ts_utc` |
| `/tmp/pass_c_v4_checkpoint.jsonl` | JSONL | Resume state: one line per completed obs_id |
| `/tmp/pass_c_v4_failures.jsonl` | JSONL | Per-failure detail for inspection |
| `~/Desktop/Archive/logs/pass_c_v4.log` | text | nohup capture (stdout + stderr) |

A row in the output CSV with `prescience_score = -1` means the model call or JSON parse failed for that obs. Failure detail is in `/tmp/pass_c_v4_failures.jsonl`.

## Decoding (matches v2 calibration)

| Param | Value |
|---|---|
| model | `qwen3.5:27b-mlx` |
| think | `False` |
| keep_alive | `30m` |
| num_ctx | `8192` |
| num_predict | `400` |
| temperature | `0.2` |
| format | `json` (Ollama JSON-mode) |

## Run it

```bash
cd ~/Desktop/Archive
nohup python3 scripts/run_prescience_pass_c_v4.py > logs/pass_c_v4.log 2>&1 &
echo $! > /tmp/pass_c_v4.pid
tail -f logs/pass_c_v4.log
```

Check progress in another terminal:

```bash
tail -f ~/Desktop/Archive/logs/pass_c_v4.log
wc -l /tmp/pass_c_v4_checkpoint.jsonl    # rows scored so far
wc -l /tmp/pass_c_v4_failures.jsonl      # failures so far
```

## Throughput estimate

| Metric | Estimate |
|---|---|
| Per-row latency on M4 Pro | ~3 sec |
| Total rows | 23,605 |
| Total wall-clock | ~20 hours (single process) |
| Resumable | yes — Ctrl-C and re-run, checkpoint dedupes |

## Resume after interruption

Just re-run the same command. The checkpoint JSONL is the source of truth — already-scored obs_ids are skipped automatically. The output CSV will have duplicate rows if a previous partial run wrote rows that aren't in the checkpoint, but the checkpoint is authoritative for "what's done." If you need a clean output CSV after a partial run:

```bash
# Dedupe output CSV against checkpoint (post-run, only if needed)
python3 -c "
import csv, json
done = set()
with open('/tmp/pass_c_v4_checkpoint.jsonl') as f:
    for line in f:
        rec = json.loads(line)
        if rec.get('status') == 'ok':
            done.add(rec['obs_id'])
print(f'ok obs_ids in checkpoint: {len(done)}')
"
```

## Stop it cleanly

```bash
kill $(cat /tmp/pass_c_v4.pid)
```

Or `Ctrl-C` if running in foreground. Either way, the current row finishes (or fails) and is checkpointed before exit.

## After it completes

Hand off to `roll_up_prescience_to_master_v2.py` (already shipped) to merge scores into `_master_observations.csv` as a column.

Then run Workflow C from `kastner-archive-pipeline` skill:
1. Phase 1 (`01_load_csvs_v2.py`) — re-derive enriched columns
2. Phase 2 (`02_build_data_layer_v2.py`) — rebuild DuckDB
3. Shape audit — confirm `high_prescience_studies (max>=4)` count
4. Phases 3-6 if `kw ask` results need to reflect new scores
5. EOD batch commit via `kastner-github` skill

## Drift analysis (post-completion)

The v1 cloud LLM scores already exist in `_master_observations.csv` (`prescience_score` column or similar). The v4 Qwen scores will be in `prescience_scores_pass_c_v4.csv`. Join on `obs_id` to produce:

- Per-obs delta (cloud_score - qwen_score)
- Distribution of disagreement by observation_type, by pub_year, by study
- κ between cloud and Qwen (pairwise agreement)

This is a v1.6 backlog item; not blocking for the Pass C run itself.

## Failure modes to watch

| Symptom in log | Likely cause | Action |
|---|---|---|
| Many `Ollama call failed` lines | Ollama crashed or model unloaded | `ollama list`, restart `ollama serve` if needed, re-run script (checkpoint resumes) |
| Many JSON parse failures | Model emitting prose despite `format: json` | Inspect a failure record — if widespread, may need prompt tweak (defer to v5) |
| Per-row latency >10s | Model not warm or another process competing | Confirm `keep_alive: 30m` is honored; check Activity Monitor |
| Empty `_raw_text.txt` claims (claim text == "(no claim text)") | obs row has neither `metric_value` nor `notes` | Script handles gracefully — model returns score=0 most likely |

## Schema notes

The output CSV has 8 columns; the existing `_master_observations.csv` has 14. Roll-up script merges by adding/updating `prescience_score` column (and optionally `prescience_confidence`, `prescience_rationale` as v1.6 additions — TBD per `roll_up_prescience_to_master_v2.py` config).

## Version history

- v1: cloud LLM corpus-wide (left scores in master)
- v2: local Qwen w/ Bucket A only, calibration-only run
- v3: local Qwen w/ v3 pre-filter (aborted before commit due to thin scoreable counts)
- **v4: local Qwen corpus-wide (this script)**
