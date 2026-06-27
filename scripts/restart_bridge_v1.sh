#!/usr/bin/env bash
# restart_bridge.sh — full restart of the Kastner MCP bridge + ngrok tunnel.
#
# Why this exists: the launchd job `com.kastner.ngrok.bridge` ONLY supervises
# ngrok. ngrok tunnels  dolphin-washer-slush.ngrok-free.dev -> 127.0.0.1:8765,
# but the thing LISTENING on 8765 is a SEPARATE process: the Python MCP bridge
# server (run_http.sh -> python -m kastner_archive_mcp). If that Python process
# dies, ngrok stays up and every request returns 502 — the tunnel is alive but
# nothing is behind it. That is the exact failure mode this script fixes.
#
# Order matters: start the bridge server FIRST (so 8765 is listening), THEN
# (re)start ngrok so its upstream is reachable immediately.
#
# Run this in a REAL Terminal on the Mac (it uses launchctl + pkill, which the
# sandboxed pc shell blocks). Safe to re-run; it is idempotent.
#
#   bash restart_bridge.sh
#
set -uo pipefail

# ---- constants ----
BRIDGE_DIR="/Users/scott/Repos/mac_mcp_bridge"
RUN_HTTP="$BRIDGE_DIR/run_http.sh"
PLIST="$HOME/Library/LaunchAgents/com.kastner.ngrok.bridge.plist"
LABEL="com.kastner.ngrok.bridge"
PORT=8765
TUNNEL_URL="https://dolphin-washer-slush.ngrok-free.dev/mcp"
LSOF="/usr/sbin/lsof"          # full path: non-login PATH often lacks /usr/sbin
BRIDGE_OUT="/tmp/kastner_bridge.out.log"
BRIDGE_ERR="/tmp/kastner_bridge.err.log"
GUI="gui/$(id -u)"

say() { printf '\n=== %s ===\n' "$1"; }

# ---- 1. tear down both halves ----
say "1. Stopping ngrok (launchd job + any stray agents)"
launchctl bootout  "$GUI/$LABEL"  2>/dev/null || launchctl unload "$PLIST" 2>/dev/null || true
/usr/bin/pkill -9 -f ngrok 2>/dev/null || true

say "2. Stopping any existing bridge server on :$PORT"
# kill whatever is listening on 8765 (the old python -m kastner_archive_mcp)
BRIDGE_PIDS="$("$LSOF" -nP -iTCP:$PORT -sTCP:LISTEN -t 2>/dev/null || true)"
if [ -n "$BRIDGE_PIDS" ]; then
  echo "killing pid(s): $BRIDGE_PIDS"
  kill -9 $BRIDGE_PIDS 2>/dev/null || true
else
  echo "nothing listening on :$PORT (clean)"
fi
# belt-and-suspenders: kill by module name too
/usr/bin/pkill -9 -f 'python -m kastner_archive_mcp' 2>/dev/null || true
/usr/bin/pkill -9 -f 'kastner_archive_mcp' 2>/dev/null || true

sleep 2

# ---- 3. start the bridge server (the thing that LISTENS on 8765) ----
say "3. Starting bridge server (python -m kastner_archive_mcp on :$PORT)"
# nohup + & so it survives this shell; logs to /tmp so we can read them.
nohup /bin/bash "$RUN_HTTP" >"$BRIDGE_OUT" 2>"$BRIDGE_ERR" &
echo "launched run_http.sh (pid $!); logs: $BRIDGE_OUT / $BRIDGE_ERR"

# wait up to 20s for 8765 to come up
say "4. Waiting for :$PORT to listen"
up=""
for i in $(seq 1 20); do
  if "$LSOF" -nP -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; then up=1; break; fi
  sleep 1
done
if [ -n "$up" ]; then
  echo "bridge is LISTENING on :$PORT after ${i}s"
else
  echo "!! bridge did NOT come up on :$PORT within 20s"
  echo "---- tail $BRIDGE_ERR ----"; tail -n 30 "$BRIDGE_ERR" 2>/dev/null
  echo "---- tail $BRIDGE_OUT ----"; tail -n 30 "$BRIDGE_OUT" 2>/dev/null
  echo "Bridge failed to start; not starting ngrok. Fix the above and re-run."
  exit 1
fi

# ---- 5. (re)start ngrok via launchd ----
say "5. Starting ngrok via launchd ($LABEL)"
# bootstrap is the modern path; fall back to load for older macOS.
launchctl bootstrap "$GUI" "$PLIST" 2>/dev/null || launchctl load "$PLIST" 2>/dev/null || true
# force a clean (re)start of the agent regardless of prior state
launchctl kickstart -k "$GUI/$LABEL" 2>/dev/null || true

say "6. Waiting for ngrok tunnel"
ng=""
for i in $(seq 1 20); do
  if curl -s http://127.0.0.1:4040/api/tunnels 2>/dev/null | grep -q dolphin-washer-slush; then ng=1; break; fi
  sleep 1
done
if [ -n "$ng" ]; then
  echo "ngrok tunnel is UP after ${i}s"
else
  echo "!! ngrok tunnel not visible on the 4040 API within 20s"
  echo "---- tail /tmp/ngrok.bridge.err.log ----"; tail -n 20 /tmp/ngrok.bridge.err.log 2>/dev/null
fi

# ---- 7. end-to-end verification ----
say "7. Verification"
echo "-- launchd job state:"
launchctl list 2>/dev/null | grep ngrok || echo "  (job not in launchctl list)"
echo "-- local bridge listening:"
"$LSOF" -nP -iTCP:$PORT -sTCP:LISTEN || echo "  NO_BRIDGE"
echo "-- ngrok tunnels:"
curl -s http://127.0.0.1:4040/api/tunnels 2>/dev/null | python3 -c \
  'import sys,json;d=json.load(sys.stdin);[print("  ",t["public_url"],"->",t["config"]["addr"]) for t in d.get("tunnels",[])]' \
  2>/dev/null || echo "  (could not read 4040 API)"
echo "-- public endpoint HTTP status (expect 401/406, NOT 502/000):"
code="$(curl -s -o /dev/null -w '%{http_code}' "$TUNNEL_URL")"
echo "  $TUNNEL_URL -> HTTP $code"
case "$code" in
  401|403|406|200|405) echo "  OK: tunnel + bridge are both alive (auth/handshake layer responding)";;
  502|503|504)         echo "  BAD: ngrok up but bridge unreachable (502) — check $BRIDGE_ERR";;
  000)                 echo "  BAD: tunnel not reachable (DNS/ngrok down)";;
  *)                   echo "  Unexpected status; inspect logs above";;
esac

say "Done"
echo "If status is 401/406, reconnect/refresh the 'Perplexity bridge v2' connector and call bridge_info."
echo "Bearer token (if needed): cat ~/.config/kastner_mcp/token"
