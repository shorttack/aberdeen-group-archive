#!/usr/bin/env bash
# monitor_phases_3to6_v1.sh — non-blocking status check for Phases 3-6
# Run this any time during the unattended regen. Safe to run repeatedly.
# Pete's runbook: paste output here and Computer interprets state.

set -u

LOGS=~/Desktop/Archive/logs
WIKI=~/Repos/kastner-aberdeen-wiki

echo "=== monitor_phases_3to6_v1 @ $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo ""

echo "--- running python3 build processes ---"
ps -ax -o pid,etime,command | grep -E "scripts/build/0[3-6]_" | grep -v grep || echo "(no build phase processes running)"
echo ""

echo "--- caffeinate process ---"
ps -ax -o pid,etime,command | grep "caffeinate -dim" | grep -v grep || echo "(no caffeinate process)"
echo ""

echo "--- latest log file per phase (newest first) ---"
for n in 3 4 5 6; do
  latest=$(ls -t "$LOGS"/phase${n}_*.log 2>/dev/null | head -1)
  if [ -z "$latest" ]; then
    echo "  phase${n}: (no log yet)"
  else
    size=$(wc -c < "$latest" | tr -d ' ')
    lines=$(wc -l < "$latest" | tr -d ' ')
    mtime=$(stat -f '%Sm' -t '%H:%M:%S' "$latest")
    echo "  phase${n}: $latest"
    echo "          ${lines} lines, ${size} bytes, last modified ${mtime}"
  fi
done
echo ""

echo "--- tail (last 8 lines) of newest phase log ---"
newest=$(ls -t "$LOGS"/phase*_*.log 2>/dev/null | head -1)
if [ -n "$newest" ]; then
  echo "    file: $newest"
  echo ""
  tail -8 "$newest" | sed 's/^/    /'
else
  echo "    (no phase logs found yet)"
fi
echo ""

echo "--- 'ALL PHASES COMPLETE' banner? ---"
banner=$(ls -t "$LOGS"/phases_3to6_done_*.log 2>/dev/null | head -1)
if [ -z "$banner" ]; then
  echo "  NO — phases still running or in between phases"
else
  echo "  YES:"
  cat "$banner" | sed 's/^/    /'
fi
echo ""

echo "--- wiki tree state (sample counts) ---"
if [ -d "$WIKI/wiki" ]; then
  echo "  $WIKI/wiki/studies/      : $(ls "$WIKI/wiki/studies" 2>/dev/null | wc -l | tr -d ' ') files"
  echo "  $WIKI/wiki/entities/     : $(ls "$WIKI/wiki/entities" 2>/dev/null | wc -l | tr -d ' ') files"
  echo "  $WIKI/wiki/technologies/ : $(ls "$WIKI/wiki/technologies" 2>/dev/null | wc -l | tr -d ' ') files"
  echo "  $WIKI/wiki/decades/      : $(ls "$WIKI/wiki/decades" 2>/dev/null | wc -l | tr -d ' ') files"
else
  echo "  ($WIKI/wiki not found)"
fi
echo ""

echo "--- embeddings parquet state ---"
emb="$WIKI/data/embeddings.parquet"
if [ -f "$emb" ]; then
  size=$(wc -c < "$emb" | tr -d ' ')
  mtime=$(stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' "$emb")
  echo "  embeddings.parquet: ${size} bytes, mtime ${mtime}"
else
  echo "  (no embeddings.parquet yet)"
fi
echo ""

echo "=== end monitor ==="
