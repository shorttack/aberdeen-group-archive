#!/usr/bin/env bash
# overnight_v1.sh — 2026-07-07 evening cleanse + full SH-chain rebuild.
#
# Sequence:
#   1. Shape audit BEFORE (paste-ready output for _decisions_log)
#   2. Phase A — apply_tech_mislabel_v1.py --commit
#   3. Phase B — apply_entity_metadata_v1.py --commit
#   4. Phase C-narrow — apply_entity_aliases_v1_sap.py --commit
#   5. Phase 1 — 01_load_csvs_v3.py (SH-aware, loads _master_prescience_short_horizon.csv)
#   6. Phase 2 — 02_build_data_layer_v5.py (adds 5 SH views)
#   7. Phase 0 — 07_audit_masters_v1.py (regression harness — must PASS)
#   8. Shape audit MID (paste-ready)
#   9. Phase 3 — 03_generate_vault_v3.py (SH-aware page rendering) — LONGEST STEP (~3h tier-1 LLM)
#  10. Phase 4 — 04_generate_indices_v6.py
#  11. Phase 5 — 05_compute_embeddings_v3.py (bge-m3, ~15-19 min)
#  12. Phase 6 — 06_emit_scaffolding_v2.py (SH-aware README/AGENTS)
#  13. Shape audit AFTER
#  14. Emit STATUS file + macOS notification (success or first-failure)
#
# On any failure: halt immediately (set -e), emit STATUS_FAIL file, macOS popup + sound.
# On success: STATUS_OK file, macOS popup.

set -euo pipefail

# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────
ARCHIVE=~/Desktop/Archive
REPO=$ARCHIVE/aberdeen-group-archive
WIKI=~/Repos/kastner-aberdeen-wiki
SCRIPTS=$ARCHIVE/scripts
BUILD=$SCRIPTS/build
DUCKDB=/opt/homebrew/bin/duckdb

STAMP=$(date -u +"%Y%m%dT%H%M%SZ")
LOG_DIR="$ARCHIVE/logs/wiki_rebuild_$STAMP"
STATUS_DIR="$ARCHIVE/logs"
STATUS_OK="$STATUS_DIR/OVERNIGHT_STATUS_${STAMP}.OK"
STATUS_FAIL="$STATUS_DIR/OVERNIGHT_STATUS_${STAMP}.FAIL"

mkdir -p "$LOG_DIR"
echo "Logs: $LOG_DIR"

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

# On failure: write STATUS_FAIL file, fire macOS notification with sound, then exit
notify_fail() {
  local phase="$1"
  local extra="${2:-}"
  {
    echo "OVERNIGHT RUN FAILED"
    echo "Timestamp:  $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "Failed at:  $phase"
    echo "Log dir:    $LOG_DIR"
    echo "Latest log: $(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)"
    echo ""
    echo "$extra"
    echo ""
    echo "To inspect:"
    echo "  cat $LOG_DIR/*.log | tail -100"
    echo "  bash $REPO/scripts/monitor_phases_3to6_v1.sh"
  } > "$STATUS_FAIL"
  osascript -e "display notification \"Overnight run failed at $phase — see $STATUS_FAIL\" with title \"Kastner overnight\" sound name \"Basso\"" 2>/dev/null || true
  osascript -e 'display dialog "Kastner overnight run FAILED. Check ~/Desktop/Archive/logs/OVERNIGHT_STATUS_*.FAIL" buttons {"OK"} default button 1 with icon stop' 2>/dev/null || true
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  OVERNIGHT RUN FAILED at $phase"
  echo "  Status file: $STATUS_FAIL"
  echo "═══════════════════════════════════════════════════════════════════"
  exit 1
}

# Trap: any unhandled error triggers notify_fail
trap 'notify_fail "unexpected error (line $LINENO)" "Command that failed: $BASH_COMMAND"' ERR

# Wrapper: run phase with tee, halt on non-zero
run_phase() {
  local name="$1"
  local logfile="$LOG_DIR/${name}.log"
  shift
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  START $name  ($(date -u +%H:%M:%SZ))"
  echo "  cmd: $*"
  echo "  log: $logfile"
  echo "═══════════════════════════════════════════════════════════════════"
  if ! "$@" 2>&1 | tee "$logfile"; then
    notify_fail "$name" "See $logfile for details"
  fi
  # Check pipefail — if the child inside the pipe failed, PIPESTATUS[0] is nonzero
  local rc=${PIPESTATUS[0]}
  if [ "$rc" -ne 0 ]; then
    notify_fail "$name" "Non-zero exit $rc from $*. See $logfile."
  fi
  echo "  DONE $name  ($(date -u +%H:%M:%SZ))"
}

# Shape audit — writes paste-ready output to a log file AND stdout
shape_audit() {
  local label="$1"
  local out="$LOG_DIR/shape_audit_${label}.txt"
  {
    echo "=== Shape audit ($label) — $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    "$DUCKDB" -readonly "$WIKI/db/kastner.duckdb" -c "
      SELECT
        (SELECT COUNT(*) FROM v_studies)                          AS studies,
        (SELECT COUNT(*) FROM v_observations)                     AS observations,
        (SELECT COUNT(*) FROM v_entities)                         AS entities,
        (SELECT COUNT(*) FROM v_technologies)                     AS technologies,
        (SELECT COUNT(*) FROM v_studies WHERE pub_year IS NOT NULL) AS studies_with_pub_year,
        (SELECT COUNT(DISTINCT (CAST(pub_year AS INTEGER)//10)*10) FROM v_studies WHERE pub_year IS NOT NULL) AS decades_covered,
        (SELECT COUNT(*) FROM v_studies_with_high_prescience)     AS high_prescience;
    "
  } | tee "$out"
}

# ─────────────────────────────────────────────────────────────────────────────
# Preflight
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  KASTNER OVERNIGHT RUN — $STAMP"
echo "═══════════════════════════════════════════════════════════════════"
echo "  Archive:  $ARCHIVE"
echo "  Repo:     $REPO"
echo "  Wiki:     $WIKI"
echo "  Scripts:  $BUILD"
echo ""

# Preflight: everything we depend on exists
for p in "$REPO/_master_studies.csv" \
         "$WIKI/db/kastner.duckdb" \
         "$SCRIPTS/apply_tech_mislabel_v1.py" \
         "$SCRIPTS/apply_entity_metadata_v1.py" \
         "$SCRIPTS/apply_entity_aliases_v1_sap.py" \
         "$SCRIPTS/tech_mislabel_candidates_v1.csv" \
         "$SCRIPTS/entity_metadata_candidates_v1.csv" \
         "$SCRIPTS/entity_alias_map_v1_sap_only.csv" \
         "$BUILD/07_audit_masters_v1.py" \
         "$ARCHIVE/Perplexity_Only/audit_masters_baseline.json" \
         "$BUILD/01_load_csvs_v3.py" \
         "$BUILD/02_build_data_layer_v5.py" \
         "$BUILD/03_generate_vault_v3.py" \
         "$BUILD/04_generate_indices_v6.py" \
         "$BUILD/05_compute_embeddings_v3.py" \
         "$BUILD/06_emit_scaffolding_v2.py"; do
  if [ ! -e "$p" ]; then
    echo "PREFLIGHT FAIL: $p not found"
    notify_fail "preflight" "$p is missing — did you `git pull` and copy the new scripts + candidates from the repo?"
  fi
done
echo "✓ All 16 preflight paths present"

# Backup .gitignore in the wiki BEFORE Phase 6 v2 (which regresses to 3-line minimal)
if [ -f "$WIKI/.gitignore" ]; then
  cp "$WIKI/.gitignore" "$WIKI/.gitignore.bak_${STAMP}"
  echo "✓ Backed up $WIKI/.gitignore → .gitignore.bak_$STAMP"
fi

# ─────────────────────────────────────────────────────────────────────────────
# Phase pre-audits
# ─────────────────────────────────────────────────────────────────────────────

shape_audit "BEFORE"

# ─────────────────────────────────────────────────────────────────────────────
# Cleanse phases (masters edit)
# ─────────────────────────────────────────────────────────────────────────────

cd "$ARCHIVE"

run_phase "phase_A_tech_mislabel_DRYRUN"    python3 "$SCRIPTS/apply_tech_mislabel_v1.py"
run_phase "phase_A_tech_mislabel_COMMIT"    python3 "$SCRIPTS/apply_tech_mislabel_v1.py" --commit

run_phase "phase_B_entity_metadata_DRYRUN"  python3 "$SCRIPTS/apply_entity_metadata_v1.py"
run_phase "phase_B_entity_metadata_COMMIT"  python3 "$SCRIPTS/apply_entity_metadata_v1.py" --commit

run_phase "phase_C_sap_alias_DRYRUN"        python3 "$SCRIPTS/apply_entity_aliases_v1_sap.py"
run_phase "phase_C_sap_alias_COMMIT"        python3 "$SCRIPTS/apply_entity_aliases_v1_sap.py" --commit

# ─────────────────────────────────────────────────────────────────────────────
# Pipeline rebuild (SH-aware chain)
# ─────────────────────────────────────────────────────────────────────────────

run_phase "01_load_csvs_v3"          python3 "$BUILD/01_load_csvs_v3.py"        --archive "$REPO" --wiki "$WIKI"
run_phase "02_build_data_layer_v5"   python3 "$BUILD/02_build_data_layer_v5.py" --wiki "$WIKI"

# Phase 0 regression audit — must PASS before running expensive Phases 3-6
run_phase "07_audit_masters_v1"      python3 "$BUILD/07_audit_masters_v1.py" \
                                       --db "$WIKI/db/kastner.duckdb" \
                                       --baseline "$ARCHIVE/Perplexity_Only/audit_masters_baseline.json" \
                                       --write-report "$LOG_DIR/07_audit_report.md"

shape_audit "MID_after_phases_1_2_0"

# Long-running phases
run_phase "03_generate_vault_v3"     python3 "$BUILD/03_generate_vault_v3.py"    --wiki "$WIKI"
run_phase "04_generate_indices_v6"   python3 "$BUILD/04_generate_indices_v6.py"  --wiki "$WIKI"
run_phase "05_compute_embeddings_v3" python3 "$BUILD/05_compute_embeddings_v3.py" --wiki "$WIKI"
run_phase "06_emit_scaffolding_v2"   python3 "$BUILD/06_emit_scaffolding_v2.py"  --wiki "$WIKI"

shape_audit "AFTER"

# ─────────────────────────────────────────────────────────────────────────────
# Success
# ─────────────────────────────────────────────────────────────────────────────

{
  echo "OVERNIGHT RUN SUCCESS"
  echo "Timestamp:   $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Started:     $STAMP"
  echo "Log dir:     $LOG_DIR"
  echo ""
  echo "Shape audits:"
  echo "  BEFORE: $LOG_DIR/shape_audit_BEFORE.txt"
  echo "  MID:    $LOG_DIR/shape_audit_MID_after_phases_1_2_0.txt"
  echo "  AFTER:  $LOG_DIR/shape_audit_AFTER.txt"
  echo ""
  echo "Phase 0 audit report: $LOG_DIR/07_audit_report.md"
  echo ""
  echo "Expected deltas:"
  echo "  entities: 3293 -> 3288 (Phase C-narrow SAP merge, -5)"
  echo "  technologies: 4376 -> 4368 (Phase A merges, -8)"
  echo "  studies + observations + high_prescience: unchanged"
  echo ""
  echo "Next steps (in the morning):"
  echo "  1. cat $LOG_DIR/shape_audit_AFTER.txt"
  echo "  2. cat $LOG_DIR/07_audit_report.md"
  echo "  3. kw ask 'what is the shape of the Kastner archive' — should return post-cleanse counts"
  echo "  4. Restore .gitignore if desired: cp $WIKI/.gitignore.bak_$STAMP $WIKI/.gitignore"
  echo "  5. Commit the archive+wiki changes via EOD batch commit"
} > "$STATUS_OK"

# macOS notification
osascript -e "display notification \"Overnight run complete — all phases green\" with title \"Kastner overnight\" sound name \"Glass\"" 2>/dev/null || true

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  ✓ OVERNIGHT RUN COMPLETE"
echo "  Status: $STATUS_OK"
echo "═══════════════════════════════════════════════════════════════════"
