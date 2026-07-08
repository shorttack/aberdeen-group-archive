#!/usr/bin/env bash
# change_local_model_v2.sh — Install Qwen 3.6-27B (MLX) and verify before any script refactor.
#
# Pete Kastner Aberdeen archive — §11q (2026-06-02)
# Standing rules honored:
#   - Pete runs ALL commands (script never auto-commits, never auto-removes).
#   - "Abort if no MLX" — pre-flights the registry for the MLX tag and exits non-zero if absent.
#   - "Keep both for a week" — does NOT `ollama rm qwen3.5:27b-mlx`; only adds the new model.
#   - "Do not sacrifice KW retrieval accuracy" — target tag is MLX-native (same family as current).
#   - Forever archive — never overwrite an older script; this is _v1.
#
# Target model:  qwen3.6:27b-mlx  (Apache 2.0, ~20 GB, Apple Silicon-native)
# Current model: qwen3.5:27b-mlx  (preserved, untouched)
#
# Why MLX over MTP-GGUF (Q8): MLX preserves Apple Silicon-native matmul paths; GGUF quantization
# loses 2-5% accuracy at equivalent footprint. The KW-ask synthesis path quality is downstream of
# this choice; bge-m3 (1024-dim retrieval embeddings) is NOT affected by this lane.
#
# Usage:
#   bash ~/Desktop/Archive/scripts/change_local_model_v1.sh           # dry-run (default)
#   bash ~/Desktop/Archive/scripts/change_local_model_v1.sh --commit  # actually pulls the model

set -euo pipefail

NEW_MODEL="qwen3.6:27b-mlx"
OLD_MODEL="qwen3.5:27b-mlx"
OLLAMA_BASE="${OLLAMA_BASE:-http://localhost:11434}"
COMMIT=0

for arg in "$@"; do
  case "$arg" in
    --commit) COMMIT=1 ;;
    -h|--help)
      sed -n '1,30p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 2
      ;;
  esac
done

echo "================================================================"
echo "  change_local_model_v1.sh  —  Qwen 3.6-27B MLX install"
echo "================================================================"
echo "Mode:        $([ "$COMMIT" = "1" ] && echo COMMIT || echo DRY-RUN)"
echo "New model:   $NEW_MODEL"
echo "Old model:   $OLD_MODEL  (kept; will NOT be removed)"
echo "Ollama base: $OLLAMA_BASE"
echo

# ---------- Pre-flight 1: Ollama daemon up ----------
echo "[1/5] Pre-flight: Ollama daemon..."
if ! curl -fsS --max-time 3 "$OLLAMA_BASE/api/version" > /dev/null; then
  echo "  FAIL: Ollama not reachable at $OLLAMA_BASE"
  echo "  Start it with:  ollama serve   (or open the Ollama.app)"
  exit 1
fi
echo "  ok: $(curl -fsS "$OLLAMA_BASE/api/version" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("version",""))')"
echo

# ---------- Pre-flight 2: old model is actually present (sanity) ----------
echo "[2/5] Pre-flight: confirm current model is installed..."
if ollama list 2>/dev/null | awk '{print $1}' | grep -qx "$OLD_MODEL"; then
  echo "  ok: $OLD_MODEL is installed (will be preserved per 'keep both for a week')"
else
  echo "  WARN: $OLD_MODEL not found by 'ollama list'. Proceeding anyway, but verify after install."
fi
echo

# ---------- Pre-flight 3: ABORT IF NO MLX on registry ----------
# v2 fix: download the HTML to a temp file FIRST, then grep the file. Piping curl -> grep -q under
# `set -o pipefail` causes a spurious failure: grep -q closes the pipe on the first match, curl
# exits 23 (write error, surfaces as code 56 on macOS), pipefail propagates that as the pipeline's
# exit. v1 of this script falsely reported "tag missing" because of this. Fix: decouple I/O.
echo "[3/5] Pre-flight: verify $NEW_MODEL exists on the Ollama registry..."
TAG_PAGE_URL="https://ollama.com/library/qwen3.6/tags"
TAG_PAGE_TMP="$(mktemp -t qwen36_tags.XXXXXX)"
trap 'rm -f "$TAG_PAGE_TMP"' EXIT
if ! curl -fsS --max-time 10 "$TAG_PAGE_URL" -o "$TAG_PAGE_TMP"; then
  echo "  FAIL: could not fetch $TAG_PAGE_URL (network or DNS)."
  exit 3
fi
if ! grep -q "$NEW_MODEL" "$TAG_PAGE_TMP"; then
  echo "  FAIL: $NEW_MODEL was NOT found in the registry listing at $TAG_PAGE_URL"
  echo "  Per standing rule: 'abort if there is no MLX'. Exiting WITHOUT pulling anything."
  echo "  If you want to override and pull a GGUF tag instead, edit NEW_MODEL at the top of this script."
  exit 3
fi
echo "  ok: $NEW_MODEL is present on the registry ($(grep -c "$NEW_MODEL" "$TAG_PAGE_TMP") references in tag page)."
echo

# ---------- Pre-flight 4: disk-space sanity ----------
echo "[4/5] Pre-flight: disk space..."
FREE_GB=$(df -g "$HOME/.ollama" 2>/dev/null | awk 'NR==2 {print $4}')
if [ -n "$FREE_GB" ] && [ "$FREE_GB" -lt 30 ]; then
  echo "  FAIL: only ${FREE_GB} GB free under $HOME/.ollama; need >=30 GB headroom for a 20 GB pull."
  exit 4
fi
echo "  ok: ${FREE_GB:-unknown} GB free under $HOME/.ollama"
echo

# ---------- Action: pull the model ----------
if [ "$COMMIT" = "1" ]; then
  echo "[5/5] Pulling $NEW_MODEL (~20 GB; can take 5-30 min depending on bandwidth)..."
  ollama pull "$NEW_MODEL"
  echo
  echo "  Verifying installation..."
  if ollama list | awk '{print $1}' | grep -qx "$NEW_MODEL"; then
    echo "  ok: $NEW_MODEL is installed."
  else
    echo "  FAIL: 'ollama list' does not show $NEW_MODEL after pull. Investigate manually."
    exit 5
  fi

  echo
  echo "  Smoke test: 1-token generation through $NEW_MODEL..."
  SMOKE_RESPONSE=$(curl -fsS --max-time 60 "$OLLAMA_BASE/api/generate" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$NEW_MODEL\",\"prompt\":\"Reply with the single word OK.\",\"stream\":false,\"options\":{\"num_predict\":4,\"temperature\":0,\"think\":false}}" \
    | python3 -c 'import sys,json; print(json.load(sys.stdin).get("response","").strip())')
  if [ -n "$SMOKE_RESPONSE" ]; then
    echo "  ok: model responded with: ${SMOKE_RESPONSE}"
  else
    echo "  WARN: smoke test returned empty response. Model installed but may need 'ollama run $NEW_MODEL' once interactively to warm up."
  fi
else
  echo "[5/5] DRY-RUN: would run 'ollama pull $NEW_MODEL' (~20 GB)."
  echo "       Re-run with --commit to actually pull."
fi

echo
echo "================================================================"
echo "  Done with install phase."
echo "================================================================"
echo
echo "Both models are now usable:"
echo "  - $OLD_MODEL   (current; preserved for 7-day transition)"
echo "  - $NEW_MODEL   (new; default after refactor)"
echo
echo "NEXT (script refactor — §11q follow-up, NOT done by this script):"
echo
echo "  cd ~/Desktop/Archive/aberdeen-group-archive && git pull"
echo
echo "  Then drop the v2/v4/v5 refactor pack into ~/Desktop/Archive/scripts/:"
echo "    cp scripts/build/_llm_helper_v2.py             ~/Desktop/Archive/scripts/build/"
echo "    cp scripts/build/04_generate_indices_v4.py     ~/Desktop/Archive/scripts/build/"
echo "    cp scripts/build/06_emit_scaffolding_v2.py     ~/Desktop/Archive/scripts/build/"
echo "    cp scripts/pre_filter_scoreable_obs_v5.py      ~/Desktop/Archive/scripts/"
echo "    cp scripts/run_prescience_calibration_v4.py    ~/Desktop/Archive/scripts/"
echo
echo "  Then test in this order (matches kastner-archive-pipeline Workflow C):"
echo "    1. python3 ~/Desktop/Archive/scripts/build/06_emit_scaffolding_v2.py --wiki ~/Desktop/kastner_wiki --dry-run"
echo "    2. python3 ~/Desktop/Archive/scripts/build/04_generate_indices_v4.py --wiki ~/Desktop/kastner_wiki --dry-run  # if --dry-run supported"
echo
echo "  Wiki repo (kw_ask) is shipped separately — see the README."
echo
echo "ROLLBACK (within 7 days, no questions asked):"
echo "  Edit ~/Desktop/Archive/scripts/build/_llm_helper_v2.py and change"
echo "    LOCAL_MODEL = \"$NEW_MODEL\""
echo "  back to"
echo "    LOCAL_MODEL = \"$OLD_MODEL\""
echo "  The old model is still installed; nothing else needs to change."
echo
echo "AFTER 7 DAYS of stable use (~2026-06-09):"
echo "  ollama rm $OLD_MODEL    # frees ~20 GB"
echo "  (Do NOT run this command unless KW ask quality is confirmed acceptable on the new model.)"
echo
