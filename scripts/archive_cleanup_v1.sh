#!/bin/bash
# archive_cleanup_v1.sh
#
# Move late-May 2026 one-time backup and staging directories from
# ~/Desktop/Archive/ to ~/Desktop/Archive_legacy_2026_May/.
#
# Forever-archive principle: nothing is deleted from disk except
# __pycache__ (regenerable Python cache). Everything else is MOVED
# to the legacy tree, which preserves it but unclutters the live
# Archive root.
#
# Dry-run is the default. Pass --commit to actually move/delete.
#
# Usage:
#   bash ~/Desktop/Archive/scripts/archive_cleanup_v1.sh
#   bash ~/Desktop/Archive/scripts/archive_cleanup_v1.sh --commit
#
# v1.0  2026-06-04  Pete Kastner / Computer

set -eu

ARCHIVE="${HOME}/Desktop/Archive"
LEGACY="${HOME}/Desktop/Archive_legacy_2026_May"

COMMIT=0
for arg in "$@"; do
  case "$arg" in
    --commit) COMMIT=1 ;;
    -h|--help)
      sed -n '2,18p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 2
      ;;
  esac
done

if [ ! -d "$ARCHIVE" ]; then
  echo "ERROR: $ARCHIVE not found" >&2
  exit 1
fi

# Entries to MOVE to legacy (relative to $ARCHIVE)
TO_MOVE=(
  "incoming-bucket-B"
  "incoming-bucket-C"
  "incoming-bucket-D"
  "incoming-bucket-E"
  "incoming-existing"
  "bucket-A-processed"
  "archive_masters_pre_fix_v2_backup"
  "archive_masters_pre_fix_v3_backup"
  "archive_masters_pre_namespace_v2_backup"
  "archive_masters_pre_case_merge_backup"
  "archive_masters_pre_rewrite_quoting_20260525_213720Z"
  "archive_masters_pre_year_observed_apply_20260525_211909Z"
  "v1.5_workspace"
  "kastner_duckdb_build"
  "prepared_dropped_dups"
  "logs/zip_test2"
)

# Entries to DELETE outright (regenerable cache only)
TO_DELETE=(
  "__pycache__"
)

# Mode banner
if [ "$COMMIT" -eq 1 ]; then
  echo "===== archive_cleanup_v1.sh  MODE: COMMIT ====="
else
  echo "===== archive_cleanup_v1.sh  MODE: DRY-RUN  (pass --commit to actually move) ====="
fi
echo "ARCHIVE: $ARCHIVE"
echo "LEGACY:  $LEGACY"
echo

# Pre-flight: counts so we can audit deltas
COUNT_MOVE_FOUND=0
COUNT_MOVE_MISSING=0
COUNT_DELETE_FOUND=0
COUNT_DELETE_MISSING=0

# Ensure legacy root exists (commit only)
if [ "$COMMIT" -eq 1 ]; then
  mkdir -p "$LEGACY"
fi

echo "--- MOVE_TO_LEGACY ---"
for rel in "${TO_MOVE[@]}"; do
  src="$ARCHIVE/$rel"
  dst="$LEGACY/$rel"
  if [ ! -e "$src" ]; then
    echo "  [skip - not present]   $rel"
    COUNT_MOVE_MISSING=$((COUNT_MOVE_MISSING + 1))
    continue
  fi
  COUNT_MOVE_FOUND=$((COUNT_MOVE_FOUND + 1))
  # Block any clobber of an existing legacy entry — would lose data
  if [ -e "$dst" ]; then
    echo "  [BLOCK - dst exists]   $rel  (legacy already has this; manual review)"
    continue
  fi
  if [ "$COMMIT" -eq 1 ]; then
    mkdir -p "$(dirname "$dst")"
    mv "$src" "$dst"
    echo "  [moved]                $rel  ->  $dst"
  else
    echo "  [would move]           $rel  ->  $dst"
  fi
done

echo
echo "--- DELETE ---"
for rel in "${TO_DELETE[@]}"; do
  src="$ARCHIVE/$rel"
  if [ ! -e "$src" ]; then
    echo "  [skip - not present]   $rel"
    COUNT_DELETE_MISSING=$((COUNT_DELETE_MISSING + 1))
    continue
  fi
  COUNT_DELETE_FOUND=$((COUNT_DELETE_FOUND + 1))
  if [ "$COMMIT" -eq 1 ]; then
    rm -rf "$src"
    echo "  [deleted]              $rel"
  else
    echo "  [would delete]         $rel"
  fi
done

echo
echo "--- Summary ---"
echo "MOVE   found: $COUNT_MOVE_FOUND   missing: $COUNT_MOVE_MISSING"
echo "DELETE found: $COUNT_DELETE_FOUND   missing: $COUNT_DELETE_MISSING"
if [ "$COMMIT" -eq 0 ]; then
  echo
  echo "Dry-run only. Re-run with --commit to apply."
fi
