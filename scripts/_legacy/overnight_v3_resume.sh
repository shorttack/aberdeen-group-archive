#!/usr/bin/env bash
# overnight_v3_resume.sh — Resume the 2026-07-07 pipeline from Phase 3.
#
# CONTEXT: The 18:54:29Z run of overnight_v2.sh completed Phases A/B/C cleanse
# + Phase 1 + Phase 2 + Phase 0 audit cleanly. Phase 3 ran for ~2 hours then
# was interrupted by a power failure at ~17:00 EDT before Phase 4/5/6 could
# start. The masters, parquets, and DuckDB are all in the correct post-cleanse
# state (verified: entities=3288, tech=4368, sh_scores=17030, sh_verdicts=792;
# all 8 tech mislabels and all 5 SAP aliases are removed; entity metadata
# fixes are in place).
#
# This resume script SKIPS the cleanse phases (which would fail with a
# "already applied, nothing to do" error) and starts fresh from Phase 3.
#
# Sequence:
#   1. Idempotency check: confirm the cleanse actually landed (fail fast if not)
#   2. Shape audit BEFORE_RESUME (should show post-cleanse counts)
#   3. Phase 3 — 03_generate_vault_v3.py  (~3h tier-1 LLM)
#   4. Phase 4 — 04_generate_indices_v6.py
#   5. Phase 5 — 05_compute_embeddings_v3.py (bge-m3, ~15-19 min)
#   6. Phase 6 — 06_emit_scaffolding_v2.py (SH-aware README/AGENTS)
#   7. Shape audit AFTER
#   8. STATUS file + macOS notification

set -euo pipefail

ARCHIVE=~/Desktop/Archive
REPO=$ARCHIVE/aberdeen-group-archive
WIKI=~/Repos/kastner-aberdeen-wiki
BUILD=$ARCHIVE/scripts/build
DUCKDB=/opt/homebrew/bin/duckdb

STAMP=$(date -u +"%Y%m%dT%H%M%SZ")
LOG_DIR="$ARCHIVE/logs/wiki_rebuild_resume_$STAMP"
STATUS_OK="$ARCHIVE/logs/OVERNIGHT_STATUS_${STAMP}.OK"
STATUS_FAIL="$ARCHIVE/logs/OVERNIGHT_STATUS_${STAMP}.FAIL"

mkdir -p "$LOG_DIR"
echo "Logs: $LOG_DIR"

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

notify_fail() {
  local phase="$1"; local extra="${2:-}"
  {
    echo "OVERNIGHT RESUME FAILED"
    echo "Timestamp:  $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "Failed at:  $phase"
    echo "Log dir:    $LOG_DIR"
    echo "Latest log: $(ls -t "$LOG_DIR"/*.log 2>/dev/null | head -1)"
    echo ""; echo "$extra"
    echo ""; echo "To inspect: cat $LOG_DIR/*.log | tail -100"
  } > "$STATUS_FAIL"
  osascript -e "display notification \"Overnight resume failed at $phase\" with title \"Kastner overnight\" sound name \"Basso\"" 2>/dev/null || true
  osascript -e 'display dialog "Kastner overnight RESUME FAILED. Check ~/Desktop/Archive/logs/OVERNIGHT_STATUS_*.FAIL" buttons {"OK"} default button 1 with icon stop' 2>/dev/null || true
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  OVERNIGHT RESUME FAILED at $phase"
  echo "  Status: $STATUS_FAIL"
  echo "═══════════════════════════════════════════════════════════════════"
  exit 1
}

trap 'notify_fail "unexpected error (line $LINENO)" "Command that failed: $BASH_COMMAND"' ERR

run_phase() {
  local name="$1"; local logfile="$LOG_DIR/${name}.log"; shift
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  START $name  ($(date -u +%H:%M:%SZ))"
  echo "  cmd: $*"
  echo "  log: $logfile"
  echo "═══════════════════════════════════════════════════════════════════"
  if ! "$@" 2>&1 | tee "$logfile"; then
    notify_fail "$name" "See $logfile for details"
  fi
  local rc=${PIPESTATUS[0]}
  if [ "$rc" -ne 0 ]; then
    notify_fail "$name" "Non-zero exit $rc from $*. See $logfile."
  fi
  echo "  DONE $name  ($(date -u +%H:%M:%SZ))"
}

shape_audit() {
  local label="$1"; local out="$LOG_DIR/shape_audit_${label}.txt"
  {
    echo "=== Shape audit ($label) — $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    "$DUCKDB" -readonly "$WIKI/db/kastner.duckdb" -c "
      SELECT
        (SELECT COUNT(*) FROM v_studies)                        AS studies,
        (SELECT COUNT(*) FROM v_observations)                   AS observations,
        (SELECT COUNT(*) FROM v_entities)                       AS entities,
        (SELECT COUNT(*) FROM v_technologies)                   AS technologies,
        (SELECT COUNT(*) FROM v_studies WHERE pub_year IS NOT NULL) AS studies_with_pub_year,
        (SELECT COUNT(DISTINCT (CAST(pub_year AS INTEGER)//10)*10) FROM v_studies WHERE pub_year IS NOT NULL) AS decades_covered,
        (SELECT COUNT(*) FROM v_studies_with_high_prescience)   AS high_prescience,
        (SELECT COUNT(*) FROM v_prescience_sh)                  AS sh_scores,
        (SELECT COUNT(*) FROM v_studies_with_sh_verdicts)       AS sh_verdicts;
    "
  } | tee "$out"
}

# ─────────────────────────────────────────────────────────────────────────────
# Preflight + idempotency check
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  KASTNER OVERNIGHT RESUME — $STAMP"
echo "  Skipping Phases A/B/C (already applied 18:54:29Z)"
echo "  Skipping Phase 1+2+0 (already ran cleanly at 18:54:32Z)"
echo "  Starting from Phase 3 (page regeneration)"
echo "═══════════════════════════════════════════════════════════════════"

# Preflight paths
for p in "$WIKI/db/kastner.duckdb" \
         "$BUILD/03_generate_vault_v3.py" \
         "$BUILD/04_generate_indices_v6.py" \
         "$BUILD/05_compute_embeddings_v3.py" \
         "$BUILD/06_emit_scaffolding_v2.py"; do
  [ -e "$p" ] || notify_fail "preflight" "$p is missing"
done
echo "✓ All 5 preflight paths present"

# Idempotency check: cleanse actually landed?
echo ""
echo "→ Idempotency check: verifying Phases A/B/C are already applied"
IDEM=$("$DUCKDB" -readonly "$WIKI/db/kastner.duckdb" -c "
SELECT
  (SELECT COUNT(*) FROM v_technologies WHERE tech_id IN ('data-mining','microsoft-backoffice','sun-ultrasparc','audio-conferencing','webex-training-center','titanium','t2-04','tech-01')) AS a_left,
  (SELECT COUNT(*) FROM v_entities WHERE entity_id IN ('sap','ENT-SAP','ENT-SAP-001','ENT-BO-002','ENT-IRP-003')) AS c_left,
  (SELECT COUNT(*) FROM v_prescience_sh) AS sh,
  (SELECT successor FROM v_entities WHERE entity_id='informix-software') AS informix;
")
echo "$IDEM"
A_LEFT=$(echo "$IDEM" | awk '/^│/ && !/int64|varchar|a_left/{gsub(/│/, ""); print $1; exit}')
if [ "$A_LEFT" != "0" ]; then
  notify_fail "idempotency" "Phase A aliases still present in v_technologies (expected 0, got $A_LEFT). The cleanse did NOT complete before the resume. Do NOT proceed."
fi
echo "✓ Idempotency confirmed: cleanse is fully applied"

# Backup .gitignore before Phase 6 v2 regresses it
[ -f "$WIKI/.gitignore" ] && cp "$WIKI/.gitignore" "$WIKI/.gitignore.bak_resume_${STAMP}"

shape_audit "BEFORE_RESUME"

# ─────────────────────────────────────────────────────────────────────────────
# Phases 3-6 (resume from where the power failure hit)
# ─────────────────────────────────────────────────────────────────────────────

run_phase "03_generate_vault_v3"     python3 "$BUILD/03_generate_vault_v3.py"    --wiki "$WIKI"
run_phase "04_generate_indices_v6"   python3 "$BUILD/04_generate_indices_v6.py"  --wiki "$WIKI"
run_phase "05_compute_embeddings_v3" python3 "$BUILD/05_compute_embeddings_v3.py" --wiki "$WIKI"
run_phase "06_emit_scaffolding_v2"   python3 "$BUILD/06_emit_scaffolding_v2.py"  --wiki "$WIKI"

shape_audit "AFTER"

# ─────────────────────────────────────────────────────────────────────────────
# Success
# ─────────────────────────────────────────────────────────────────────────────

{
  echo "OVERNIGHT RESUME SUCCESS"
  echo "Timestamp:   $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Started:     $STAMP"
  echo "Log dir:     $LOG_DIR"
  echo ""
  echo "Shape audits:"
  echo "  BEFORE_RESUME: $LOG_DIR/shape_audit_BEFORE_RESUME.txt"
  echo "  AFTER:         $LOG_DIR/shape_audit_AFTER.txt"
  echo ""
  echo "Expected after resume:"
  echo "  entities=3288, technologies=4368 (same as before — cleanse was already applied)"
  echo "  wiki study pages carry SH content (prescience_3y_enum + Short-horizon section)"
  echo ""
  echo "Next steps (in the morning):"
  echo "  1. cat $LOG_DIR/shape_audit_AFTER.txt"
  echo "  2. kw ask 'which studies were prescient at 3 years'"
  echo "  3. Restore hardened .gitignore if desired:"
  echo "     cp $WIKI/.gitignore.bak_resume_${STAMP} $WIKI/.gitignore"
  echo "  4. EOD batch commit (archive + wiki repo)"
} > "$STATUS_OK"

osascript -e "display notification \"Overnight resume complete — all phases green\" with title \"Kastner overnight\" sound name \"Glass\"" 2>/dev/null || true

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  ✓ OVERNIGHT RESUME COMPLETE"
echo "  Status: $STATUS_OK"
echo "═══════════════════════════════════════════════════════════════════"
