#!/usr/bin/env bash
# prep_overnight_v1.sh — one-shot prep for the 2026-07-07 overnight cleanse.
# Idempotent: safe to re-run if partway through.
#
# 1. git pull in the archive repo
# 2. Copy today's cleanse artifacts from repo into runtime locations
# 3. Verify all overnight_v1.sh preflight paths exist
# 4. Print the next command to run
#
# Then: bash ~/Desktop/Archive/scripts/overnight_v1.sh (or via caffeinate)

set -euo pipefail

ARCHIVE=~/Desktop/Archive
REPO=$ARCHIVE/aberdeen-group-archive

echo "═══════════════════════════════════════════════════════════════════"
echo "  PREP FOR OVERNIGHT RUN"
echo "═══════════════════════════════════════════════════════════════════"

echo ""
echo "→ git pull in $REPO"
cd "$REPO"
git pull

echo ""
echo "→ Copying cleanse artifacts into runtime locations"

# Scripts (5 files → ~/Desktop/Archive/scripts/)
cp -v scripts/apply_tech_mislabel_v1.py         "$ARCHIVE/scripts/apply_tech_mislabel_v1.py"
cp -v scripts/apply_entity_metadata_v1.py        "$ARCHIVE/scripts/apply_entity_metadata_v1.py"
cp -v scripts/apply_entity_aliases_v1_sap.py     "$ARCHIVE/scripts/apply_entity_aliases_v1_sap.py"
cp -v scripts/generate_baseline_v1.py            "$ARCHIVE/scripts/generate_baseline_v1.py"

# Phase 0 harness → scripts/build/
cp -v scripts/build/07_audit_masters_v1.py       "$ARCHIVE/scripts/build/07_audit_masters_v1.py"

# Candidates CSVs (3 files → ~/Desktop/Archive/scripts/)
cp -v tech_mislabel_candidates_v1.csv            "$ARCHIVE/scripts/tech_mislabel_candidates_v1.csv"
cp -v entity_metadata_candidates_v1.csv          "$ARCHIVE/scripts/entity_metadata_candidates_v1.csv"
cp -v entity_alias_map_v1_sap_only.csv           "$ARCHIVE/scripts/entity_alias_map_v1_sap_only.csv"

# Phase 0 baseline JSON → Perplexity_Only/
cp -v Perplexity_Only/audit_masters_baseline.json  "$ARCHIVE/Perplexity_Only/audit_masters_baseline.json"

# Also copy the overnight runner itself if not already present
if [ ! -e "$ARCHIVE/scripts/overnight_v1.sh" ]; then
  echo ""
  echo "NOTE: $ARCHIVE/scripts/overnight_v1.sh not found — paste it into place, then run:"
  echo "  chmod +x $ARCHIVE/scripts/overnight_v1.sh"
fi

echo ""
echo "→ Verifying preflight"
MISSING=0
for p in \
  "$REPO/_master_studies.csv" \
  ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb \
  "$ARCHIVE/scripts/apply_tech_mislabel_v1.py" \
  "$ARCHIVE/scripts/apply_entity_metadata_v1.py" \
  "$ARCHIVE/scripts/apply_entity_aliases_v1_sap.py" \
  "$ARCHIVE/scripts/tech_mislabel_candidates_v1.csv" \
  "$ARCHIVE/scripts/entity_metadata_candidates_v1.csv" \
  "$ARCHIVE/scripts/entity_alias_map_v1_sap_only.csv" \
  "$ARCHIVE/scripts/build/07_audit_masters_v1.py" \
  "$ARCHIVE/Perplexity_Only/audit_masters_baseline.json" \
  "$ARCHIVE/scripts/build/01_load_csvs_v3.py" \
  "$ARCHIVE/scripts/build/02_build_data_layer_v5.py" \
  "$ARCHIVE/scripts/build/03_generate_vault_v3.py" \
  "$ARCHIVE/scripts/build/04_generate_indices_v6.py" \
  "$ARCHIVE/scripts/build/05_compute_embeddings_v3.py" \
  "$ARCHIVE/scripts/build/06_emit_scaffolding_v2.py"; do
  if [ ! -e "$p" ]; then
    echo "  ✗ MISSING: $p"
    MISSING=$((MISSING + 1))
  fi
done

if [ "$MISSING" -gt 0 ]; then
  echo ""
  echo "═══════════════════════════════════════════════════════════════════"
  echo "  ✗ PREP FAILED — $MISSING file(s) missing"
  echo "═══════════════════════════════════════════════════════════════════"
  exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  ✓ PREP COMPLETE — ready for overnight run"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "Next command (run before you go to bed):"
echo ""
echo "  caffeinate -dim bash ~/Desktop/Archive/scripts/overnight_v1.sh"
echo ""
echo "This will:"
echo "  • Keep the Mac awake (-d) with display sleep prevented (-i, -m)"
echo "  • Run all cleanse phases (A, B, C-narrow) with --commit"
echo "  • Run full SH pipeline (01_v3 → 02_v5 → Phase 0 audit → 03_v3 → 04_v6 → 05_v3 → 06_v2)"
echo "  • Log to ~/Desktop/Archive/logs/wiki_rebuild_<UTC>/"
echo "  • Fire a macOS notification on success OR first failure"
echo ""
echo "In the morning, check:"
echo "  cat ~/Desktop/Archive/logs/OVERNIGHT_STATUS_*.OK  (success)"
echo "  cat ~/Desktop/Archive/logs/OVERNIGHT_STATUS_*.FAIL (failure)"
