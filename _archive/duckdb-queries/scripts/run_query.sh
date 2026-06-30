#!/usr/bin/env bash
# run_query.sh — read-only DuckDB query against the Kastner archive on the Mac.
#
# Designed to be run THROUGH `pc bash` (non-login shell) on Pete's Mac mini.
# Opens kastner.duckdb strictly read-only. Pass SQL as $1, or pipe SQL on stdin.
#
# Examples (from the workspace):
#   pc bash -- 'bash /Users/scott/Repos/mac_mcp_bridge/run_query.sh "SELECT COUNT(*) FROM v_studies;"'
#   printf "%s" "SELECT * FROM v_top_prescient_studies LIMIT 10;" | pc files write /tmp/q.sql
#   pc bash -- 'bash /Users/scott/Repos/mac_mcp_bridge/run_query.sh --file /tmp/q.sql'
#
# This script lives in the skill bundle; copy it to the Mac (e.g. via pc files
# write) if you want it resident there, or inline the duckdb call directly.
set -euo pipefail

DUCKDB="${DUCKDB_BIN:-/opt/homebrew/bin/duckdb}"
DB="${KASTNER_DB:-/Users/scott/Repos/kastner-aberdeen-wiki/db/kastner.duckdb}"

if [[ ! -x "$DUCKDB" ]]; then
  echo "ERROR: duckdb CLI not found at $DUCKDB" >&2; exit 2
fi
if [[ ! -f "$DB" ]]; then
  echo "ERROR: DB not found at $DB" >&2; exit 2
fi

if [[ "${1:-}" == "--file" ]]; then
  SQLFILE="${2:?--file needs a path}"
  exec "$DUCKDB" -readonly "$DB" -c ".read $SQLFILE"
elif [[ -n "${1:-}" ]]; then
  exec "$DUCKDB" -readonly "$DB" -c "$1"
else
  # read SQL from stdin
  SQL="$(cat)"
  exec "$DUCKDB" -readonly "$DB" -c "$SQL"
fi
