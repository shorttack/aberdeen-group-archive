# Driver v8 Spec — Short-Horizon Prescience (3y + 5y combined)

**Status:** DRAFT (Phase 0). No implementation yet.
**Successor to:** `driver_v7.py` (network-hardened, currently running Tier B PID 2163).
**Companion docs:**
- `decisions_log_entry_2026_06_15_short_horizon_prescience_v2.md` (spec)
- `anchor_year_resolver_v1.py` (resolver module)
- `short_horizon_prompt_v1.md` (prompt design)

---

## 1. What v8 inherits from v7 (DO NOT REGRESS)

- `nohup` + PID file + tee log pattern for long runs
- Network hardening: `except (HTTPError, URLError, TimeoutError, OSError, JSONDecodeError, KeyError, ValueError)`
- `REQUEST_TIMEOUT = 120`, `MAX_RETRIES = 5`
- CSV resume-on-restart (read existing output, skip already-scored obs_id)
- Exponential backoff between retries
- Per-row try/except so one failure doesn't kill the run
- Sonar API endpoint + auth pattern

---

## 2. What's new in v8

### 2a. Two-score architecture
- One API call per obs → fills 6 scoring fields (`prescience_{3y,5y}`, `confidence_{3y,5y}`, `rationale_{3y,5y}`) + 2 divergence fields (`windows_diverge`, `divergence_note`)
- max_tokens: `1200 → 2000`

### 2b. Pre-API anchor resolution + pending short-circuit
- Import `anchor_year_resolver_v1`
- Per row, BEFORE building request:
  ```
  try:
      anchor = resolve_anchor_year(obs_row, study_row)
  except AnchorResolutionError as e:
      write_no_anchor(row, reason=str(e))   # score=-1, both horizons
      continue

  elapsed_3y = is_window_elapsed(anchor.year, 3, TODAY_YEAR)
  elapsed_5y = is_window_elapsed(anchor.year, 5, TODAY_YEAR)

  if not elapsed_3y and not elapsed_5y:
      write_pending(row, anchor, horizons=[3,5])   # two -2 rows worth of cols, no API
      continue
  elif elapsed_3y and not elapsed_5y:
      result = call_sonar(prompt_3y_only, ...)     # variant prompt
      merge_3y(row, result); write_pending_5y(row)
  else:  # both elapsed
      result = call_sonar(prompt_combined, ...)
      merge_both(row, result)
  ```

### 2c. Output columns (writer order)
Existing v7 columns preserved, then appended (matches v2 decision doc):

```
obs_id, ...existing v7 cols...,
prescience_3y, confidence_3y, rationale_3y,
prescience_5y, confidence_5y, rationale_5y,
windows_diverge, divergence_note,
anchor_year, anchor_source,
scored_at_sh, scorer_version_sh, source_pass_sh,
raw_response_sh
```

- `anchor_source` ∈ `{obs_date, memoir_period_start, study_published_at}` — confirmed for v3 (Pete authorized).
- `scorer_version_sh` default: `pass_c_sonar_sh_v1`
- `source_pass_sh` default: `pass_c_sh_combined` | `pass_c_sh_3y_only` | `pass_c_sh_pending` | `pass_c_sh_no_anchor`

### 2d. Pending-row shape
```
prescience_Ny     = -2
confidence_Ny     = ""               # NULL in CSV
rationale_Ny      = "window_not_elapsed:Ny:cutoff_YYYY"
```
- For BOTH-pending rows: no API call, no `raw_response_sh`.
- `windows_diverge` = "" (never asserted without scoring)
- `divergence_note` = ""

### 2e. No-anchor row shape
```
prescience_3y = prescience_5y = -1
confidence_*  = ""
rationale_*   = f"no_anchor:{exception_message}"
source_pass_sh = "pass_c_sh_no_anchor"
```

### 2f. Parse-fail handling
Same pattern as Tier A: write row with `scorer_version_sh = pass_c_sonar_sh_v1_parse_fail`, preserve `raw_response_sh` for post-hoc retry. Do NOT promote parse-fail rows in first promote pass.

---

## 3. Constants block (top of file)

```python
TODAY_YEAR        = 2026                     # explicit, audit-friendly
SCORER_VERSION    = "pass_c_sonar_sh_v1"
MODEL             = "sonar-pro"              # CONFIRMED v3 (Pete: no downgrade)
REQUEST_TIMEOUT   = 120
MAX_RETRIES       = 5
MAX_TOKENS        = 2000
TEMPERATURE       = 0.0                      # deterministic
BACKOFF_BASE      = 2.0
SLEEP_BETWEEN_OBS = 0.0                      # rate limit governed by Sonar tier
```

`TODAY_YEAR` is a constant — NOT `datetime.now().year` — so a multi-day run produces consistent cutoffs even if it spans New Year's. Pete bumps it manually each scoring cycle.

---

## 4. CLI surface

```
python3 driver_v8.py \
  --input  unscored_obs_inventory_v1.csv \
  --studies _master_studies.csv \
  --output tier_X_results.csv \
  --resume \
  --limit 0 \
  --scorer-version pass_c_sonar_sh_v1 \
  --source-pass-default pass_c_sh_combined
```

`--resume` reads existing output and skips `obs_id` already present (matches v7 behavior).

---

## 5. Smoke test (before launching Tier B-sized run)

1. Run resolver self-test: `python3 anchor_year_resolver_v1.py` (must print PASS).
2. Build a 10-row mixed fixture covering all 4 paths: both-elapsed, 3y-only, both-pending, no-anchor.
3. Run driver with `--limit 10` against fixture, inspect output CSV by hand.
4. Validate JSON schema parse rate ≥ 95% on the 10 rows.
5. Run G1-G9 gates against fixture (G7 -2 rate, G8 windows_diverge rate will be noisy at n=10 — flag, don't block).

---

## 6. Calibration before sweep

Per the spec: 100-obs calibration sample anchored ≤ 2020 (both windows elapsed), drawn stratified across the 25 buckets used in Tier A/B. Run v8 against it, inspect by hand for:

- score distribution sanity (not all 0s, not all 5s)
- rationale quality (cites window-bound facts)
- windows_diverge rate (expect 5-15%, flag if >25%)
- confidence range (should span 0.3-0.95, flag if compressed)

If calibration passes, full sweep gets greenlit. Cost ceiling for full sweep: $250-300 already approved.

---

## 7. Resolved (v3 spec lock, 2026-06-15)

- ✓ MODEL = sonar-pro (Pete: no downgrade)
- ✓ Column order: append to end of master, 14 new cols
- ✓ anchor_source: kept (Pete: audit value)
- ✓ Calibration: AFTER Tier B completes (no thrashing)
- ✓ Confidence: int 1-3 (matches Tier A/B Sonar driver convention)
- ✓ windows_diverge: model-asserted; promote script computes mechanical cross-check for G8b

## 8. Still to confirm before v8 code written

- [ ] Operate on full corpus (~24K obs) or restrict to obs with existing long-horizon Pass C verdicts? Hypothesis: full corpus — long-horizon and short-horizon are independent. Pete to confirm at sweep-launch time, not now.