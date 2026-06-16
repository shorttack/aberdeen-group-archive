#!/bin/bash
# check_sh_sweep_v1.sh — SH short-horizon sweep status snapshot
# Parallel of check_tier_b_v1.sh, sized for the 8,659-obs ≤2015 sweep.
# Usage: bash ~/Desktop/Archive/scripts/check_sh_sweep_v1.sh

PID_FILE="$HOME/Desktop/Archive/logs/sh_sweep_le_2015.pid"
LOG_FILE="$HOME/Desktop/Archive/logs/sh_sweep_le_2015_run.log"
OUT_FILE="$HOME/Desktop/Archive/aberdeen-group-archive/Perplexity_Only/sh_sweep_le_2015_results.csv"
TARGET_ROWS=8659

echo "=================================================="
echo "  SH ≤2015 Sweep Check — $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "=================================================="

# Process status
if [ ! -f "$PID_FILE" ]; then
    echo "❌ PID file missing: $PID_FILE"
    exit 1
fi
PID=$(cat "$PID_FILE")
echo ""
echo "[process]"
if ps -p "$PID" > /dev/null 2>&1; then
    echo "  PID $PID: RUNNING"
    ps -p "$PID" -o pid,etime,pcpu,pmem,rss,command | tail -1 | sed 's/^/  /'
else
    echo "  PID $PID: NOT RUNNING (done or died)"
fi

# Output file progress
echo ""
echo "[output]"
if [ -f "$OUT_FILE" ]; then
    # NOTE: rationale fields contain embedded newlines — count CSV records, not lines
    DATA_ROWS=$(python3 -c "import csv; print(sum(1 for _ in csv.DictReader(open('$OUT_FILE'))))")
    PCT=$(awk -v r="$DATA_ROWS" -v t="$TARGET_ROWS" 'BEGIN{printf "%.1f", 100*r/t}')
    MTIME=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$OUT_FILE" 2>/dev/null || stat -c "%y" "$OUT_FILE" 2>/dev/null | cut -d. -f1)
    echo "  rows: $DATA_ROWS / $TARGET_ROWS (${PCT}%)"
    echo "  last modified: $MTIME"
    SIZE=$(ls -lh "$OUT_FILE" | awk '{print $5}')
    echo "  size: $SIZE"
else
    echo "  (no output yet — first batch still in flight)"
fi

# Log tail
echo ""
echo "[log tail — last 8 lines]"
if [ -f "$LOG_FILE" ]; then
    tail -8 "$LOG_FILE" | sed 's/^/  /'
else
    echo "  ❌ log missing: $LOG_FILE"
fi

# Throughput
echo ""
echo "[throughput]"
if [ -f "$LOG_FILE" ]; then
    LAST_API=$(grep '^\[api\]' "$LOG_FILE" | tail -1)
    if [ -n "$LAST_API" ]; then
        echo "  $LAST_API"
    else
        echo "  (no [api] progress lines yet — first batch still in flight)"
    fi
    DONE=$(grep '^\[done\]' "$LOG_FILE" | tail -1)
    if [ -n "$DONE" ]; then
        echo "  ✅ $DONE"
    fi
fi

# Score distribution if there's data
echo ""
echo "[score distribution so far]"
if [ -f "$OUT_FILE" ] && [ "$(wc -l < "$OUT_FILE")" -gt 1 ]; then
    python3 - << PY
import csv
from collections import Counter
try:
    rows = list(csv.DictReader(open("$OUT_FILE")))
    print(f"  total rows: {len(rows)}")
    # Parse-fail sentinel (-1) tally — separate from score distribution
    pf3 = sum(1 for r in rows if r.get('prescience_3y') == '-1')
    pf5 = sum(1 for r in rows if r.get('prescience_5y') == '-1')
    print(f"  parse_fail sentinel (-1):  3y={pf3}  5y={pf5}  ({100*pf3/len(rows):.2f}% / {100*pf5/len(rows):.2f}%)")
    # 3y window (excluding parse_fail)
    c3 = Counter(r.get('prescience_3y','') for r in rows
                 if r.get('prescience_3y') and r.get('prescience_3y') != '-1')
    if c3:
        tot = sum(c3.values())
        print(f"  --- 3y window ({tot} valid scores) ---")
        for k in sorted(c3, key=lambda x: int(x) if x.lstrip('-').isdigit() else 99):
            pct = 100*c3[k]/tot
            print(f"    score={k:>3}: {c3[k]:5d} ({pct:5.1f}%)")
    # 5y window (excluding parse_fail)
    c5 = Counter(r.get('prescience_5y','') for r in rows
                 if r.get('prescience_5y') and r.get('prescience_5y') != '-1')
    if c5:
        tot = sum(c5.values())
        print(f"  --- 5y window ({tot} valid scores) ---")
        for k in sorted(c5, key=lambda x: int(x) if x.lstrip('-').isdigit() else 99):
            pct = 100*c5[k]/tot
            print(f"    score={k:>3}: {c5[k]:5d} ({pct:5.1f}%)")
    # Divergence count (over valid-score pairs only)
    valid = [r for r in rows
             if r.get('prescience_3y') and r.get('prescience_3y') != '-1'
             and r.get('prescience_5y') and r.get('prescience_5y') != '-1']
    div = sum(1 for r in valid if (r.get('windows_diverge') or '').lower() in ('true','1','yes'))
    if valid:
        print(f"  --- divergence: {div}/{len(valid)} valid pairs ({100*div/len(valid):.1f}%) ---")
except Exception as e:
    print(f"  error: {e}")
PY
fi

echo ""
echo "=================================================="
