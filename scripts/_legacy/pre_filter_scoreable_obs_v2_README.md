# `pre_filter_scoreable_obs_v2.py` — README

**Purpose:** Pass C pre-filter, now bucket-aware. Adds `--bucket-filter A,B`
so prescience scoring runs only on observation-dense report formats
(Bucket A: benchmark reports 20-30pp, Bucket B: executive summaries 2-6pp).

## v2 delta vs v1

| Change                                | v1                          | v2                                                            |
| ------------------------------------- | --------------------------- | ------------------------------------------------------------- |
| Bucket filter                         | none                        | `--bucket-filter A,B`                                         |
| Bucket source-of-truth                | n/a                         | `<study>/manifest.json["bucket"]`                             |
| Audit CSV                             | none                        | `<root>/_bucket_audit_v2.csv` (always written in --root mode) |
| `filter_summary_v1.json` extra fields | n/a                         | adds `bucket`, `predicted_bucket`                             |
| Filter rules (the 4 skip reasons)     | unchanged                   | unchanged                                                     |
| Output filenames in `working/`        | `scoreable_obs_v1.csv` etc. | unchanged                                                     |

Filter rules (still frozen from calibration):

- empty/whitespace → skip "empty"
- <40 chars after stripping markdown → skip "too_short(Nchars)"
- markdown header (`^#` etc.) → skip "markdown_header"
- bare bold wrapper with no period → skip "bold_header_no_sentence"

## Bucket source-of-truth

Each prepared study has `manifest.json` (or legacy `manifest_v20.json`)
written by `prepare_for_ingest.py`. The `bucket` field is the **operator-
assigned** value passed to `--bucket A/B/C/D/E`. The `predicted_bucket`
field is the classifier's sanity check (informational, not used for
filtering).

Studies missing a manifest or missing the `bucket` field are reported as
`UNKNOWN` and filtered out when `--bucket-filter` is supplied. They show
up in `_bucket_audit_v2.csv` with `no_manifest=yes` for follow-up.

## Usage

### Production: Bucket A+B audit (dry-run first)

```bash
cd /Users/scott/Desktop/Archive/scripts
python3 pre_filter_scoreable_obs_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --bucket-filter A,B \
  --dry-run
```

This prints per-study counts, writes **only** `_bucket_audit_v2.csv` at the
root, and does NOT modify any `working/` files. Use this to size the Pass C
run before committing to compute.

### Production: Bucket A+B real filter pass

```bash
python3 pre_filter_scoreable_obs_v2.py \
  --root /Users/scott/Desktop/Archive/prepared \
  --bucket-filter A,B
```

For every kept study, rewrites:
- `<study>/working/scoreable_obs_v1.csv`
- `<study>/working/skipped_obs_v1.csv`
- `<study>/working/filter_summary_v1.json`

Filtered-out studies have their `working/` directory left untouched.

### Single study (bypasses bucket filter)

```bash
python3 pre_filter_scoreable_obs_v2.py \
  --study /Users/scott/Desktop/Archive/prepared/ra-warehouseautomation
```

Explicit single-study mode ignores `--bucket-filter` so you can re-filter
one study without changing the global scope. Manifest bucket is still
recorded in the summary JSON.

### Legacy v1 behavior (all buckets)

```bash
python3 pre_filter_scoreable_obs_v2.py \
  --root /Users/scott/Desktop/Archive/prepared
```

Omitting `--bucket-filter` processes everything, just like v1.

## Reading `_bucket_audit_v2.csv`

Columns:

| Column                  | Meaning                                                                  |
| ----------------------- | ------------------------------------------------------------------------ |
| `study_id`              | Directory name under `prepared/`                                         |
| `bucket`                | Assigned bucket (A/B/C/D/E/UNKNOWN)                                      |
| `predicted_bucket`      | Classifier sanity-check                                                  |
| `kept`                  | `yes` / `no` / `no_obs`                                                  |
| `total_obs`             | Total observations in `data/observations.csv` (blank if filtered out)    |
| `scoreable`             | Obs that passed the 4 filter rules                                       |
| `skipped`               | Obs that failed (non-claim)                                              |
| `no_manifest`           | `yes` if neither manifest.json nor manifest_v20.json was present         |

Sort by `bucket` then `scoreable desc` to see the highest-density studies
first. Studies with `kept=yes` are the Pass C work queue.

## Pass C compute estimate (Bucket A+B)

The 494-study, 3,253-scoreable-obs dry-run was for **all** buckets.
A+B is expected to be ~60% of total observations (Bucket A is dense, B is
short but operator-curated). After this v2 dry-run we'll have the real
number — likely ~1,800-2,200 obs → ~8-10 hrs on qwen3.5:27b-mlx at 16 s/obs.

## Forever-archive compliance

- Atomic writes via `.tmp` + `os.replace`
- CSV §16.5: `csv.QUOTE_ALL` everywhere
- Idempotent: re-running overwrites cleanly
- v1 outputs remain valid (same filenames inside `working/`); only the
  scope of what gets (re)written changes
