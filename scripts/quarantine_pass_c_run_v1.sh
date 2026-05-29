#!/bin/bash
# quarantine_pass_c_run_v1.sh
# ---------------------------
# Move the abandoned 2026-05-26 Pass C run artifacts out of the live archive
# into a quarantine directory. Idempotent. Default mode: dry-run.
#
# Per Pete's 2026-05-29 decision:
#   - Forever-archive principle: no destructive operations now
#   - Quarantine into /Users/scott/Desktop/Archive/_pass_c_abandoned_runs/20260526/
#   - Schedule hard-delete for 2026-06-05 (separate cron, not this script)
#
# What moves:
#   1. prepared/pass_c_checkpoint_v1.json
#   2. archive_masters/_master_prescience_scores.csv
#   3. 309 x prepared/*/working/prescience_scores_27b_passC_v1.csv
#   4. 309 x prepared/*/working/pass_c_log_v1.jsonl
#   5. 309 x prepared/*/working/{scoreable,skipped}_obs_v1.csv
#   6. 309 x prepared/*/working/filter_summary_v1.json
#
# What stays put (intentional):
#   - prepared/_bucket_audit_v2.csv  (input artifact, useful reference)
#
# Usage:
#   bash quarantine_pass_c_run_v1.sh             # dry-run (default)
#   bash quarantine_pass_c_run_v1.sh --commit    # actually move files

set -euo pipefail

COMMIT=false
if [[ "${1:-}" == "--commit" ]]; then
    COMMIT=true
fi

ARCHIVE="/Users/scott/Desktop/Archive"
PREPARED="$ARCHIVE/prepared"
MASTERS="$ARCHIVE/archive_masters"
QUARANTINE="$ARCHIVE/_pass_c_abandoned_runs/20260526"

echo "=================================================="
echo "Pass C abandoned-run quarantine"
echo "Mode: $([ "$COMMIT" = true ] && echo COMMIT || echo DRY-RUN)"
echo "Destination: $QUARANTINE"
echo "=================================================="
echo ""

# Pre-flight: verify the abandoned artifacts exist
if [[ ! -f "$PREPARED/pass_c_checkpoint_v1.json" ]]; then
    echo "[INFO] No checkpoint file — nothing to quarantine. Already clean?"
    exit 0
fi

# Count what we'll move
N_CSV=$(find "$PREPARED" -name "prescience_scores_27b_passC_v1.csv" 2>/dev/null | wc -l | tr -d ' ')
N_LOG=$(find "$PREPARED" -name "pass_c_log_v1.jsonl" 2>/dev/null | wc -l | tr -d ' ')
N_SCO=$(find "$PREPARED" -name "scoreable_obs_v1.csv" 2>/dev/null | wc -l | tr -d ' ')
N_SKI=$(find "$PREPARED" -name "skipped_obs_v1.csv" 2>/dev/null | wc -l | tr -d ' ')
N_FSM=$(find "$PREPARED" -name "filter_summary_v1.json" 2>/dev/null | wc -l | tr -d ' ')

echo "Inventory:"
echo "  checkpoint              : 1 file"
echo "  master rollup           : 1 file ($(ls -la "$MASTERS/_master_prescience_scores.csv" 2>/dev/null | awk '{print $5}') bytes)"
echo "  per-study scored CSVs   : $N_CSV files"
echo "  per-study log JSONL     : $N_LOG files"
echo "  per-study scoreable CSV : $N_SCO files"
echo "  per-study skipped CSV   : $N_SKI files"
echo "  per-study filter summary: $N_FSM files"
echo "  bucket audit (KEEP)     : $(ls -la "$PREPARED/_bucket_audit_v2.csv" 2>/dev/null | awk '{print $5}') bytes — staying in place"
echo ""

if [[ "$COMMIT" = false ]]; then
    echo "[DRY-RUN] Would create quarantine tree at:"
    echo "  $QUARANTINE/"
    echo "  $QUARANTINE/archive_masters/"
    echo "  $QUARANTINE/prepared/<study_id>/working/   (x $N_CSV)"
    echo ""
    echo "[DRY-RUN] Would move:"
    echo "  - $PREPARED/pass_c_checkpoint_v1.json -> $QUARANTINE/"
    echo "  - $MASTERS/_master_prescience_scores.csv -> $QUARANTINE/archive_masters/"
    echo "  - $N_CSV scored CSVs into per-study working/ subdirs"
    echo "  - $N_LOG log JSONLs"
    echo "  - $N_SCO scoreable_obs_v1.csv"
    echo "  - $N_SKI skipped_obs_v1.csv"
    echo "  - $N_FSM filter_summary_v1.json"
    echo ""
    echo "[DRY-RUN] No changes made. Re-run with --commit to execute."
    exit 0
fi

# === COMMIT MODE ===
echo "[COMMIT] Creating quarantine root: $QUARANTINE"
mkdir -p "$QUARANTINE/archive_masters"

# 1. Checkpoint
echo "[COMMIT] Moving checkpoint"
mv "$PREPARED/pass_c_checkpoint_v1.json" "$QUARANTINE/"

# 2. Master rollup
if [[ -f "$MASTERS/_master_prescience_scores.csv" ]]; then
    echo "[COMMIT] Moving master rollup"
    mv "$MASTERS/_master_prescience_scores.csv" "$QUARANTINE/archive_masters/"
fi

# 3-6. Per-study artifacts — preserve directory structure
echo "[COMMIT] Moving per-study artifacts (preserving structure)..."
MOVED=0
for f in $(find "$PREPARED" -type f \( \
    -name "prescience_scores_27b_passC_v1.csv" -o \
    -name "pass_c_log_v1.jsonl" -o \
    -name "scoreable_obs_v1.csv" -o \
    -name "skipped_obs_v1.csv" -o \
    -name "filter_summary_v1.json" \
\) 2>/dev/null); do
    # Compute relative path from prepared/
    REL="${f#$PREPARED/}"
    DEST="$QUARANTINE/prepared/$REL"
    mkdir -p "$(dirname "$DEST")"
    mv "$f" "$DEST"
    MOVED=$((MOVED + 1))
    if [[ $((MOVED % 100)) -eq 0 ]]; then
        echo "  ... $MOVED files moved"
    fi
done

echo "[COMMIT] Total per-study files moved: $MOVED"
echo ""
echo "=================================================="
echo "Quarantine complete."
echo "  Location: $QUARANTINE"
echo "  Scheduled hard-delete: 2026-06-05 (one week)"
echo ""
echo "Verify with:"
echo "  ls -la $QUARANTINE/"
echo "  find $QUARANTINE -type f | wc -l   # expect ~1547"
echo "=================================================="
