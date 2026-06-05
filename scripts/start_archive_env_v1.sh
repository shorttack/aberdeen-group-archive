#!/bin/bash
# start_archive_env_v1.sh
#
# Start the Kastner Aberdeen Archive query environment.
#
# What this does:
#   1. Ensures Ollama is running (starts it if not)
#   2. Confirms the canonical local model is loaded
#   3. Opens the Obsidian wiki vault
#   4. Opens a Terminal window scoped to ~/Desktop/Archive/ with kw ask ready
#   5. Prints a one-screen reminder of common commands
#
# It does NOT open Perplexity, paste a thread prompt, or talk to the cloud.
# For Perplexity threads, copy ~/Desktop/Archive/_archive_thread_prompt_v1.md
# into the first message of any new thread.
#
# v1.0  2026-06-05  Pete Kastner / Computer

set -eu

ARCHIVE="${HOME}/Desktop/Archive"
WIKI="${HOME}/Repos/kastner-aberdeen-wiki"
LOCAL_MODEL="qwen3.5:27b-mlx"
EMBED_MODEL="bge-m3:latest"
KW_BIN="${HOME}/bin/kw"

echo "===== Kastner Archive Query Environment v1.0 ====="
echo

# --- 1. Ollama: is it running? ---------------------------------------------

OLLAMA_HEALTH_URL="http://localhost:11434/api/version"

if curl -fsS --max-time 3 "$OLLAMA_HEALTH_URL" >/dev/null 2>&1; then
  echo "[ok]    Ollama already running on :11434"
else
  echo "[start] Ollama not running — launching in background"
  # Ollama on macOS installs as an .app; launch it via open
  if [ -d "/Applications/Ollama.app" ]; then
    open -ga Ollama
  elif command -v ollama >/dev/null 2>&1; then
    nohup ollama serve >"${HOME}/Library/Logs/ollama_start.log" 2>&1 &
  else
    echo "[FAIL]  Cannot find Ollama. Install from https://ollama.com or via brew." >&2
    exit 1
  fi
  # Wait up to 15s for it to come up
  for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    sleep 1
    if curl -fsS --max-time 2 "$OLLAMA_HEALTH_URL" >/dev/null 2>&1; then
      echo "[ok]    Ollama up after ${i}s"
      break
    fi
  done
  if ! curl -fsS --max-time 2 "$OLLAMA_HEALTH_URL" >/dev/null 2>&1; then
    echo "[FAIL]  Ollama did not start within 15s — check Activity Monitor and Console logs" >&2
    exit 1
  fi
fi

# --- 2. Canonical models present? ------------------------------------------

INSTALLED=$(curl -fsS --max-time 5 http://localhost:11434/api/tags 2>/dev/null | grep -o '"name":"[^"]*"' | sed 's/"name":"//; s/"$//')

check_model() {
  local model="$1"
  local purpose="$2"
  if echo "$INSTALLED" | grep -qx "$model"; then
    echo "[ok]    $purpose model present: $model"
  else
    echo "[warn]  $purpose model NOT installed: $model"
    echo "        Pull with:  ollama pull $model"
  fi
}

check_model "$LOCAL_MODEL" "Chat/scoring"
check_model "$EMBED_MODEL" "Embedding   "

# --- 3. Obsidian: open the wiki vault --------------------------------------

if [ -d "$WIKI" ]; then
  echo "[open]  Obsidian -> $WIKI"
  # Use Obsidian's URI scheme to open the specific vault
  VAULT_NAME=$(basename "$WIKI")
  open "obsidian://open?vault=${VAULT_NAME}" 2>/dev/null || open -a Obsidian "$WIKI" 2>/dev/null || \
    echo "[warn]  Could not open Obsidian automatically — open it manually"
else
  echo "[warn]  Wiki not found at $WIKI — skipping Obsidian launch"
fi

# --- 4. Terminal window scoped to the archive root --------------------------

# If we're already in a Terminal (most likely), don't spawn a second one.
# If invoked from Finder or via a .command file, spawn one.
if [ -z "${TERM_PROGRAM:-}" ]; then
  osascript -e "tell application \"Terminal\" to do script \"cd $ARCHIVE && clear && echo 'Archive env ready. Try: kw ask \\\"what is the shape of the Kastner archive\\\"'\"" >/dev/null 2>&1 || true
fi

# --- 5. Reminder card ------------------------------------------------------

cat <<EOF

----------------------------------------------------------------------
  Kastner Archive — common commands
----------------------------------------------------------------------

  Ask the archive (local, free):
      kw ask "what is the shape of the Kastner archive"
      kw ask "find studies on ERP ROI from 2003-2005"
      kw ask "what predictions did Aberdeen make about cloud ERP"

  Note-take into the wiki (local, free):
      kw note "<your note>"

  Shape audit (truth check before/after any masters edit):
      duckdb $WIKI/db/kastner.duckdb -c \\
        "SELECT (SELECT COUNT(*) FROM v_studies) AS studies,
                (SELECT COUNT(*) FROM v_observations) AS observations;"

  Start a new Perplexity thread with archive context:
      Copy:  $ARCHIVE/_archive_thread_prompt_v1.md
      Paste into the first message. Add your topic seed at the bottom.

  End of day, ship to GitHub:
      bash $ARCHIVE/scripts/eod_ship_v1.sh

----------------------------------------------------------------------
EOF

echo "[done]  Environment ready."
