#!/usr/bin/env python3
"""patch_orchestrator_stats_v1.py — wire generate_archive_stats.py into the
pipeline orchestrator so ARCHIVE_STATS.md refreshes on every committed rebuild.

Inserts a stats-generation block immediately after the 'Shape audit AFTER' block
in pipeline_canonical_v3.sh. Idempotent (skips if already patched). Backs up first.
"""
import shutil, datetime, sys
from pathlib import Path

ORCH = Path.home()/"Desktop/Archive/scripts/pipeline_canonical_v3.sh"
MARK = "generate_archive_stats.py"   # idempotency sentinel

txt = ORCH.read_text()
if MARK in txt:
    print("Already patched (generate_archive_stats.py present). No change.")
    sys.exit(0)

anchor = '# Shape audit AFTER\nif [ "$COMMIT" = "1" ] && [ -f "$WIKI/db/kastner.duckdb" ]; then\n  shape_audit "AFTER"\nfi\n'
if anchor not in txt:
    sys.exit("ERROR: could not find the 'Shape audit AFTER' anchor block; aborting (no change).")

block = anchor + '''
# Refresh canonical counts (single source of truth) — ARCHIVE_STATS.md
if [ "$COMMIT" = "1" ] && [ -f "$WIKI/db/kastner.duckdb" ]; then
  echo "[stats] regenerating ARCHIVE_STATS.md from live DuckDB"
  "${PYTHON_BIN:-python3}" "$ARCHIVE/scripts/generate_archive_stats.py" \\
    --db "$WIKI/db/kastner.duckdb" \\
    --out "$ARCHIVE/ARCHIVE_STATS.md" || echo "[stats] WARN: stats generation failed (non-fatal)"
fi
'''
commit = "--commit" in sys.argv
if not commit:
    print("DRY-RUN: would insert stats block after the 'Shape audit AFTER' block.")
    print("Re-run with --commit to write.")
    sys.exit(0)

ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
bak = ORCH.with_suffix(f".sh.bak_stats_{ts}")
shutil.copy2(ORCH, bak)
ORCH.write_text(txt.replace(anchor, block, 1))
print(f"Backup: {bak.name}")
print(f"PATCHED {ORCH.name} — stats generation wired in after Shape audit AFTER.")
