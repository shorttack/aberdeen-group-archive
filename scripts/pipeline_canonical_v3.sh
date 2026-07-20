#!/usr/bin/env bash
# pipeline_canonical_v3.sh — Kastner archive pipeline (Phases 0/1-6) orchestrator.
#
# v3 (2026-07-09): pin the Python interpreter. v2 (and every prior version)
# invoked a bare `python3`, which follows PATH order. On 2026-05-25 Homebrew
# upgraded /opt/homebrew/bin/python3 to 3.14 WITHOUT pyarrow, silently shadowing
# the working python.org framework build at /usr/local/bin/python3 (which HAS
# pyarrow 24.0.0 / pandas / duckdb). Result: Phase 1's df.to_parquet() died with
# "Unable to find a usable engine" on the poolsofstoragewp-3a0151 rebuild.
# v3 resolves PYTHON_BIN by probing candidate interpreters for the ability to
# import pandas+pyarrow+duckdb, uses the first that works, and fails preflight
# with an actionable message if none do. Override with PYTHON_BIN=/path env var.
# See kastner-archive-pipeline skill Gotcha 14.
#
# v2 (2026-07-08): dry-run no longer touches the filesystem. v1 unconditionally
# ran `mkdir -p "$LOG_DIR"` and the BEFORE shape audit (which tees to disk)
# during the preflight, so a bare invocation on a permissioned volume printed
# `Operation not permitted` and tripped the ERR trap. v2 guards all filesystem
# writes behind $COMMIT=1 so a dry-run is a pure plan-print + read-only check.
#
# ONE canonical entry point for the pipeline. Locks the SH-aware chain that
# was validated end-to-end on 2026-07-07/08. Replaces overnight_v2.sh,
# overnight_v3_resume.sh, monitor_phases_3to6_v1.sh, and the runbook
# incantations by encoding all of them here.
#
# The six phases remain independently invocable python scripts (they must —
# Phase 3 is ~3h tier-1 LLM, Phase 5 is ~15 min bge-m3, so re-runnability
# matters). This script simply orchestrates them in the right order with
# the right versions and shared shape audits.
#
# CANONICAL PHASE VERSIONS (as of 2026-07-08 verified end-to-end):
#   Phase 1: 01_load_csvs_v3.py           — SH-aware; loads _master_prescience_short_horizon.csv
#   Phase 2: 02_build_data_layer_v5.py    — 32 views incl. 5 SH views
#   Phase 0: 07_audit_masters_v1.py       — regression harness (runs between 2 and 3)
#   Phase 3: 03_generate_vault_v3.py      — SH content in study pages
#   Phase 4: 04_generate_indices_v6.py    — uses _llm_helper_v4 (LOCAL_MODEL=qwen3.5:27b-mlx)
#   Phase 5: 05_compute_embeddings_v3.py  — bge-m3 (1024-dim). NOT v4 (rejected qwen candidate)
#   Phase 6: 06_emit_scaffolding_v2.py    — SH-aware README/AGENTS templates
#
# USAGE:
#   pipeline_canonical_v3.sh                           # dry-run (default; prints plan, no writes)
#   pipeline_canonical_v3.sh --commit                  # run all phases
#   pipeline_canonical_v3.sh --commit --skip 3,5       # skip Phase 3+5
#   pipeline_canonical_v3.sh --commit --only 1,2,0     # only Phases 1, 2, 0
#   pipeline_canonical_v3.sh --commit --resume-from 3  # start at Phase 3 (skip 1, 2, 0)
#   PYTHON_BIN=/usr/local/bin/python3 pipeline_canonical_v3.sh --commit  # force interpreter
#
# Every phase's stdout+stderr is teed to $LOG_DIR/${phase}.log. On any failure,
# writes STATUS_FAIL and fires a macOS notification. On success, writes
# STATUS_OK. This subsumes overnight_v2.sh and overnight_v3_resume.sh — the
# --resume-from flag replaces having a separate "resume" script.
#
# Idempotency:
#   Re-running any phase is safe. Phase 1+2 rebuild parquets and DuckDB
#   deterministically from masters. Phase 3-6 overwrite their outputs. The
#   Phase 0 audit is read-only. If nothing changed on disk since the last run,
#   the outputs will be byte-identical (except for embedded timestamps).

set -euo pipefail

# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────
ARCHIVE=~/Desktop/Archive
REPO=$ARCHIVE/aberdeen-group-archive
WIKI=~/Repos/kastner-aberdeen-wiki
BUILD=$ARCHIVE/scripts/build
DUCKDB=/opt/homebrew/bin/duckdb

# ─────────────────────────────────────────────────────────────────────────────
# Python interpreter resolution (v3)
# ─────────────────────────────────────────────────────────────────────────────
# The phase scripts need pandas + pyarrow (for df.to_parquet) + duckdb. A bare
# `python3` follows PATH and can resolve to an interpreter missing pyarrow (see
# the v3 header note). Probe candidates in priority order for a working import
# set; the first that passes wins. Override explicitly with:
#   PYTHON_BIN=/usr/local/bin/python3 bash pipeline_canonical_v3.sh --commit
_py_ok() {  # $1 = candidate python path; returns 0 iff it can import the deps
  [ -x "$1" ] || command -v "$1" >/dev/null 2>&1 || return 1
  "$1" -c 'import pandas, pyarrow, duckdb' >/dev/null 2>&1
}

resolve_python() {
  # Honor an explicit override first, but still verify it works.
  if [ -n "${PYTHON_BIN:-}" ]; then
    if _py_ok "$PYTHON_BIN"; then echo "$PYTHON_BIN"; return 0; fi
    echo "" ; return 1
  fi
  local cand
  for cand in /usr/local/bin/python3 /opt/homebrew/bin/python3 "$(command -v python3 || true)" /usr/bin/python3; do
    [ -n "$cand" ] || continue
    if _py_ok "$cand"; then echo "$cand"; return 0; fi
  done
  echo "" ; return 1
}

PYTHON_BIN="$(resolve_python || true)"

STAMP=$(date -u +"%Y%m%dT%H%M%SZ")
LOG_DIR="$ARCHIVE/logs/pipeline_$STAMP"
STATUS_OK="$ARCHIVE/logs/PIPELINE_STATUS_${STAMP}.OK"
STATUS_FAIL="$ARCHIVE/logs/PIPELINE_STATUS_${STAMP}.FAIL"

# Canonical version map (change here if a phase ships a new canonical version)
declare_phase() { echo "$1:$2"; }
PHASE_1_SCRIPT="01_load_csvs_v3.py"
PHASE_2_SCRIPT="02_build_data_layer_v5.py"
PHASE_0_SCRIPT="07_audit_masters_v1.py"
PHASE_3_SCRIPT="03_generate_vault_v3.py"
PHASE_4_SCRIPT="04_generate_indices_v6.py"
PHASE_5_SCRIPT="05_compute_embeddings_v3.py"
PHASE_6_SCRIPT="06_emit_scaffolding_v2.py"

# Order of execution (Phase 0 = audit gate; runs after Phase 2)
PHASE_ORDER=(1 2 0 3 4 5 6)

# ─────────────────────────────────────────────────────────────────────────────
# Argument parsing
# ─────────────────────────────────────────────────────────────────────────────
COMMIT=0
SKIP=""
ONLY=""
RESUME_FROM=""

while [ $# -gt 0 ]; do
  case "$1" in
    --commit) COMMIT=1; shift ;;
    --skip) SKIP="$2"; shift 2 ;;
    --only) ONLY="$2"; shift 2 ;;
    --resume-from) RESUME_FROM="$2"; shift 2 ;;
    -h|--help)
      grep -E "^# " "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      echo "unknown arg: $1" >&2
      echo "Run with -h for help." >&2
      exit 2
      ;;
  esac
done

# Belt-and-suspenders exit-on-error trap must fire on the exit above too;
# but `exit 2` inside a case doesn't trigger ERR trap. That's intentional here.

# Decide which phases run
phase_included() {
  local phase="$1"
  if [ -n "$ONLY" ]; then
    echo ",$ONLY," | grep -q ",$phase,"
    return $?
  fi
  if [ -n "$RESUME_FROM" ]; then
    # Skip phases that come before RESUME_FROM in PHASE_ORDER
    local found=0
    for p in "${PHASE_ORDER[@]}"; do
      [ "$p" = "$RESUME_FROM" ] && found=1
      [ "$p" = "$phase" ] && { [ "$found" = "1" ] && return 0 || return 1; }
    done
    return 1
  fi
  if [ -n "$SKIP" ]; then
    echo ",$SKIP," | grep -q ",$phase," && return 1
  fi
  return 0
}

phase_script() {
  case "$1" in
    1) echo "$BUILD/$PHASE_1_SCRIPT" ;;
    2) echo "$BUILD/$PHASE_2_SCRIPT" ;;
    0) echo "$BUILD/$PHASE_0_SCRIPT" ;;
    3) echo "$BUILD/$PHASE_3_SCRIPT" ;;
    4) echo "$BUILD/$PHASE_4_SCRIPT" ;;
    5) echo "$BUILD/$PHASE_5_SCRIPT" ;;
    6) echo "$BUILD/$PHASE_6_SCRIPT" ;;
  esac
}

phase_args() {
  case "$1" in
    1) echo "--archive $REPO --wiki $WIKI" ;;
    2) echo "--wiki $WIKI" ;;
    0) echo "--db $WIKI/db/kastner.duckdb --baseline $ARCHIVE/Perplexity_Only/audit_masters_baseline.json --write-report $LOG_DIR/07_audit_report.md" ;;
    3) echo "--wiki $WIKI" ;;
    4) echo "--wiki $WIKI" ;;
    5) echo "--wiki $WIKI" ;;
    6) echo "--wiki $WIKI" ;;
  esac
}

phase_label() {
  case "$1" in
    1) echo "Phase 1 (load CSVs)" ;;
    2) echo "Phase 2 (build data layer + views)" ;;
    0) echo "Phase 0 (audit masters — regression harness)" ;;
    3) echo "Phase 3 (generate vault — LONGEST, ~6.5h tier-1 LLM)" ;;
    4) echo "Phase 4 (indices)" ;;
    5) echo "Phase 5 (embeddings — ~15 min)" ;;
    6) echo "Phase 6 (scaffolding docs)" ;;
  esac
}

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

notify_fail() {
  local phase="$1"; local extra="${2:-}"
  {
    echo "PIPELINE RUN FAILED"
    echo "Timestamp:  $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "Failed at:  $phase"
    echo "Log dir:    $LOG_DIR"
    echo "Latest log: $(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)"
    echo ""; echo "$extra"
    echo ""; echo "To inspect: cat $LOG_DIR/*.log | tail -100"
    echo "To resume:  bash $0 --commit --resume-from <phase>"
  } > "$STATUS_FAIL"
  osascript -e "display notification \"Pipeline failed at $phase\" with title \"Kastner pipeline\" sound name \"Basso\"" 2>/dev/null || true
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  PIPELINE FAILED at $phase"
  echo "  Status: $STATUS_FAIL"
  echo "═══════════════════════════════════════════════════════════════════"
  exit 1
}

trap 'notify_fail "unexpected error (line $LINENO)" "Command that failed: $BASH_COMMAND"' ERR

run_phase() {
  local phase="$1"
  local label="$(phase_label $phase)"
  local script="$(phase_script $phase)"
  local args="$(phase_args $phase)"
  local logfile="$LOG_DIR/phase_${phase}_$(basename $script .py).log"

  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  START $label ($(date -u +%H:%M:%SZ))"
  echo "  script: $script"
  echo "  args:   $args"
  echo "  log:    $logfile"
  echo "═══════════════════════════════════════════════════════════════════"

  if [ "$COMMIT" != "1" ]; then
    echo "  (dry-run — not executing; use --commit to run)"
    return 0
  fi

  if ! "$PYTHON_BIN" "$script" $args 2>&1 | tee "$logfile"; then
    notify_fail "$label" "See $logfile"
  fi
  local rc=${PIPESTATUS[0]}
  [ "$rc" -ne 0 ] && notify_fail "$label" "Non-zero exit $rc. See $logfile."
  echo "  DONE $label ($(date -u +%H:%M:%SZ))"
}

shape_audit() {
  local label="$1"
  local out="$LOG_DIR/shape_audit_${label}.txt"
  {
    echo "=== Shape audit ($label) — $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    "$DUCKDB" -readonly "$WIKI/db/kastner.duckdb" -c "
      SELECT
        (SELECT COUNT(*) FROM v_studies) AS studies,
        (SELECT COUNT(*) FROM v_observations) AS observations,
        (SELECT COUNT(*) FROM v_entities) AS entities,
        (SELECT COUNT(*) FROM v_technologies) AS technologies,
        (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience,
        (SELECT COUNT(*) FROM v_prescience_sh) AS sh_scores,
        (SELECT COUNT(*) FROM v_studies_with_sh_verdicts) AS sh_verdicts;
    "
  } | tee "$out"
}

# ─────────────────────────────────────────────────────────────────────────────
# Preflight
# ─────────────────────────────────────────────────────────────────────────────

if [ "$COMMIT" = "1" ]; then
  mkdir -p "$LOG_DIR"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  KASTNER PIPELINE — $STAMP"
echo "  Mode: $([ "$COMMIT" = "1" ] && echo COMMIT || echo DRY-RUN)"
[ -n "$ONLY" ] && echo "  ONLY: $ONLY"
[ -n "$SKIP" ] && echo "  SKIP: $SKIP"
[ -n "$RESUME_FROM" ] && echo "  RESUME FROM: $RESUME_FROM"
echo "  Python: ${PYTHON_BIN:-<NONE FOUND>}"
echo "═══════════════════════════════════════════════════════════════════"

# Fail fast (both dry-run and commit) if no interpreter can import the deps.
# This is read-only, so it is safe to run in dry-run mode.
if [ -z "$PYTHON_BIN" ]; then
  echo ""
  echo "  ✗ No Python interpreter found that can import pandas + pyarrow + duckdb."
  echo "    Probed: /usr/local/bin/python3, /opt/homebrew/bin/python3, \$(command -v python3), /usr/bin/python3"
  echo "    Fix one of:"
  echo "      • install the deps into an existing python:  <python> -m pip install pyarrow pandas duckdb"
  echo "      • or point at a known-good interpreter:       PYTHON_BIN=/usr/local/bin/python3 bash $0 ..."
  echo "    (2026-07-09: Homebrew python3 3.14 lacked pyarrow; /usr/local/bin/python3 had it.)"
  exit 1
fi

# Verify all canonical scripts exist (only for phases we plan to run)
MISSING=0
for phase in "${PHASE_ORDER[@]}"; do
  phase_included "$phase" || continue
  SCRIPT=$(phase_script "$phase")
  if [ ! -f "$SCRIPT" ]; then
    echo "  ✗ MISSING: $SCRIPT"
    MISSING=$((MISSING+1))
  fi
done
[ "$MISSING" -gt 0 ] && { echo "Preflight failed: $MISSING scripts missing"; exit 1; }
echo "✓ All canonical scripts present"

# Print the plan
echo ""
echo "→ Phases to run (in order):"
for phase in "${PHASE_ORDER[@]}"; do
  if phase_included "$phase"; then
    echo "  ✓ $(phase_label $phase) — $(basename $(phase_script $phase))"
  else
    echo "  ⊘ $(phase_label $phase) — SKIPPED"
  fi
done

# Shape audit BEFORE (only if DuckDB exists AND we're committing; a dry-run
# writes nothing to disk).
if [ "$COMMIT" = "1" ] && [ -f "$WIKI/db/kastner.duckdb" ]; then
  shape_audit "BEFORE"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Execute phases in order
# ─────────────────────────────────────────────────────────────────────────────

for phase in "${PHASE_ORDER[@]}"; do
  phase_included "$phase" && run_phase "$phase"
done

# Shape audit AFTER
if [ "$COMMIT" = "1" ] && [ -f "$WIKI/db/kastner.duckdb" ]; then
  shape_audit "AFTER"
fi

# Refresh canonical counts (single source of truth) — ARCHIVE_STATS.md
if [ "$COMMIT" = "1" ] && [ -f "$WIKI/db/kastner.duckdb" ]; then
  echo "[stats] regenerating ARCHIVE_STATS.md from live DuckDB"
  "${PYTHON_BIN:-python3}" "$ARCHIVE/scripts/generate_archive_stats.py" \
    --db "$WIKI/db/kastner.duckdb" \
    --out "$ARCHIVE/ARCHIVE_STATS.md" || echo "[stats] WARN: stats generation failed (non-fatal)"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Success
# ─────────────────────────────────────────────────────────────────────────────

if [ "$COMMIT" != "1" ]; then
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  DRY-RUN COMPLETE — no commits, no writes"
  echo "  Re-run with --commit to execute"
  echo "═══════════════════════════════════════════════════════════════════"
  exit 0
fi

{
  echo "PIPELINE SUCCESS"
  echo "Timestamp:   $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Started:     $STAMP"
  echo "Log dir:     $LOG_DIR"
  echo ""
  echo "Phases run:"
  for phase in "${PHASE_ORDER[@]}"; do
    if phase_included "$phase"; then
      echo "  ✓ $(phase_label $phase)"
    fi
  done
  echo ""
  echo "Shape audits: $LOG_DIR/shape_audit_*.txt"
  echo "Phase 0 report: $LOG_DIR/07_audit_report.md"
} > "$STATUS_OK"

osascript -e "display notification \"Pipeline complete — all phases green\" with title \"Kastner pipeline\" sound name \"Glass\"" 2>/dev/null || true

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  ✓ PIPELINE COMPLETE"
echo "  Status: $STATUS_OK"
echo "═══════════════════════════════════════════════════════════════════"
