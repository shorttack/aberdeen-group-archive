#!/bin/bash
# drop_duplicate_3910_v1.sh
# =========================
# One-time move of a duplicate prepared/ directory out of the Pass C work queue.
#
# Both ra-web-site-search-3910-5f9297 and ra-web-site-search-3910-sli-16eb05
# ingested identically (71 obs / 61 scoreable / 10 skipped each) from the same
# source study 3910. The -sli suffix indicates a second-look re-ingest.
# Forever-archive principle: never delete, just relocate.
#
# Decision (Pete, 2026-05-25): keep the canonical no-suffix dir, drop the -sli
# duplicate to prepared_dropped_dups/ so it remains recoverable but is excluded
# from the Pass C scoring queue.
#
# Run once on the Mac. Idempotent: if already moved, this is a no-op.
set -euo pipefail

ARCHIVE_ROOT="${ARCHIVE_ROOT:-$HOME/Desktop/Archive}"
SRC="$ARCHIVE_ROOT/prepared/ra-web-site-search-3910-sli-16eb05"
DST_DIR="$ARCHIVE_ROOT/prepared_dropped_dups"
DST="$DST_DIR/ra-web-site-search-3910-sli-16eb05"

mkdir -p "$DST_DIR"

if [[ -d "$SRC" ]]; then
    echo "Moving $SRC → $DST"
    mv "$SRC" "$DST"
    date -u +"%Y-%m-%dT%H:%M:%SZ" > "$DST/.moved_at_utc.txt"
    echo "Dropped duplicate of study 3910 (kept ra-web-site-search-3910-5f9297)" \
        > "$DST/.reason.txt"
    echo "Done."
elif [[ -d "$DST" ]]; then
    echo "Already moved — $DST exists, nothing to do."
else
    echo "WARNING: neither source nor destination found. Manual investigation needed."
    exit 1
fi
