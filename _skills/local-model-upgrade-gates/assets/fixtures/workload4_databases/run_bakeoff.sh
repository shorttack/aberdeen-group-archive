#!/usr/bin/env bash
# run_bakeoff.sh — Workload 4 (Kastner-voice narrative) bakeoff dispatcher.
#
# Governing skill : local-model-upgrade-gates v1.3, workload 4, Gate 6
# Governing README: ./README.md (fixture inputs, prompt, sidecar, pre-filter,
#                   blind ranking mechanics — read that first if you have not)
#
# What this script does:
#   1. Assembles the LOCKED prompt from the LOCKED dossier fixture.
#   2. Dispatches each ENABLED contestant with the identical prompt.
#   3. Splits each contestant's output into narrative_<c>.md + sidecar_<c>.yaml.
#   4. Runs coverage.py against each narrative and writes coverage_<c>.json.
#   5. Writes a prefilter_report.md summarizing pass/fail per contestant.
#   6. Builds the blind bundle in blind/ (A.md, B.md, C.md + key.json).
#   7. Records the run itself in run_<UTC>.log for cross-hardware comparability.
#
# What this script deliberately does NOT do:
#   - Modify any fixture input (dossier, prompt template, sidecar schema).
#   - Delete or overwrite prior runs (each run writes to a timestamped subdir).
#   - Push, commit, or tag anything in git.
#   - Judge narrative quality. Pete does that.
#
# --------------------------------------------------------------------------- #
# WHY THIS IS PARAMETERIZED
# --------------------------------------------------------------------------- #
# The archive faces two known events after 2026-09-06 that would obsolete a
# hard-coded dispatcher:
#
#   1. October 2026 — 64GB M5 Pro Mac mini cutover. The Ollama contestant's
#      model ceiling jumps from ~27B to ~40-70B; the PPLX Hybrid model may
#      also change. Every fixture will be re-run for a fresh baseline.
#
#   2. Ongoing — new local model releases (Qwen, Gemma, Llama, Mistral) trigger
#      the Gates 0-6 flow. If a candidate clears Gates 0-5, the bakeoff is how
#      it gets fitted into Gate 6 for workload 4.
#
# Every contestant model and its invocation is therefore configurable via
# environment variables with documented defaults. The defaults capture the
# 2026-09-06 baseline. To re-run under new hardware or new candidates, set
# the relevant env vars — do NOT edit this script. The script is fixture
# infrastructure and its behavior is meant to be identical across runs.
#
# When a run's config diverges from the last one, run_<UTC>.log captures the
# full env-var snapshot so cross-run diffs stay reconstructible.
# --------------------------------------------------------------------------- #

set -euo pipefail

# --------------------------------------------------------------------------- #
# Location bootstrap
# --------------------------------------------------------------------------- #
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DOSSIER="$SCRIPT_DIR/DB_LONGITUDINAL_DOSSIER_v2.md"
COVERAGE="$SCRIPT_DIR/coverage.py"
README="$SCRIPT_DIR/README.md"

for f in "$DOSSIER" "$COVERAGE" "$README"; do
  [[ -f "$f" ]] || { echo "FATAL: missing required fixture file: $f" >&2; exit 2; }
done

# --------------------------------------------------------------------------- #
# Run identity — timestamped, no overwrites
# --------------------------------------------------------------------------- #
RUN_ID="${RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)}"
RUN_DIR="$SCRIPT_DIR/outputs/run_${RUN_ID}"
BLIND_DIR="$RUN_DIR/blind"
LOG="$RUN_DIR/run_${RUN_ID}.log"

mkdir -p "$RUN_DIR" "$BLIND_DIR"

# --------------------------------------------------------------------------- #
# Contestant config (env-var driven, all overridable)
# --------------------------------------------------------------------------- #
# Five contestants are supported. Enable / disable each for a given run by
# flipping its ENABLE var. Defaults enable the original three (cloud, ollama
# incumbent, pplx) so the M4 baseline run is unchanged. The two Qwen 3.6
# Ollama variants are disabled by default and become one env-var flip away
# whenever Pete wants to isolate runtime effect from model effect (same base
# model, different runtime: PPLX vs Ollama).
#
# Useful invocation patterns:
#   - Dry-run:                BAKEOFF_ENABLE_OLLAMA=0 BAKEOFF_ENABLE_PPLX=0 bash run_bakeoff.sh
#   - Full 3-contestant M4:   bash run_bakeoff.sh   (default)
#   - Full 5-contestant M4:   BAKEOFF_ENABLE_OLLAMA_Q36_A3B=1 BAKEOFF_ENABLE_OLLAMA_Q36_MLX=1 bash run_bakeoff.sh
#   - M5 Pro re-baseline:     everything enabled; override *_MODEL vars for any tags that changed
BAKEOFF_ENABLE_CLOUD="${BAKEOFF_ENABLE_CLOUD:-1}"
BAKEOFF_ENABLE_OLLAMA="${BAKEOFF_ENABLE_OLLAMA:-1}"
BAKEOFF_ENABLE_OLLAMA_Q36_A3B="${BAKEOFF_ENABLE_OLLAMA_Q36_A3B:-0}"
BAKEOFF_ENABLE_OLLAMA_Q36_MLX="${BAKEOFF_ENABLE_OLLAMA_Q36_MLX:-0}"
BAKEOFF_ENABLE_PPLX="${BAKEOFF_ENABLE_PPLX:-1}"

# Model tags. Defaults capture the 2026-09-06 baseline. Override to test a
# candidate model without editing the script.
CLOUD_MODEL_LABEL="${CLOUD_MODEL_LABEL:-cloud-frontier-2026-09-06}"    # informational; cloud invocation is agent-mediated
OLLAMA_MODEL="${OLLAMA_MODEL:-qwen3.5:27b-mlx}"                        # incumbent; matches _llm_helper_v4.py LOCAL_MODEL as of 2026-09-06
OLLAMA_Q36_A3B_MODEL="${OLLAMA_Q36_A3B_MODEL:-qwen3.6:35b-a3b}"        # Qwen 3.6 35B active-3B (non-MLX build)
OLLAMA_Q36_MLX_MODEL="${OLLAMA_Q36_MLX_MODEL:-qwen3.6:35b-mlx}"        # Qwen 3.6 35B MLX build (same base as PPLX Hybrid; runtime differs)
PPLX_MODEL_LABEL="${PPLX_MODEL_LABEL:-pplx-computer-qwen-3-6-35b-a3b-mlx-20260709}"  # informational; PPLX invocation is agent-mediated

# Invocation surfaces. See README §3 for how each contestant is actually run.
# The three Ollama contestants are invoked directly by this script; cloud and
# PPLX are dispatched by the orchestrating agent (this script writes their
# prompt to a file and pauses for the operator to drop their raw outputs
# into the expected paths).
OLLAMA_HOST="${OLLAMA_HOST:-http://localhost:11434}"
OLLAMA_TIMEOUT_SEC="${OLLAMA_TIMEOUT_SEC:-14400}"  # 4 h ceiling per model; unattended 27B/35B long-form generation

# Pre-filter threshold — MUST match README §6 and workload-4 fixture note
# Requirement 3. Overrideable only for calibration; production runs use 0.90.
COVERAGE_THRESHOLD="${COVERAGE_THRESHOLD:-0.90}"

# Narrative length window — MUST match README §6 check #1.
MIN_WORDS="${MIN_WORDS:-2000}"
MAX_WORDS="${MAX_WORDS:-3500}"

# --------------------------------------------------------------------------- #
# Log helpers
# --------------------------------------------------------------------------- #
log() { printf "[%s] %s\n" "$(date -u +%FT%TZ)" "$*" | tee -a "$LOG"; }
die() { log "FATAL: $*"; exit 1; }

log "=== Workload 4 bakeoff run ${RUN_ID} ==="
log "script_dir=$SCRIPT_DIR"
log "run_dir=$RUN_DIR"
log "dossier_bytes=$(wc -c < "$DOSSIER" | tr -d ' ')"
log "coverage_threshold=$COVERAGE_THRESHOLD"
log "word_window=[$MIN_WORDS, $MAX_WORDS]"
log "contestants: cloud=$BAKEOFF_ENABLE_CLOUD ollama=$BAKEOFF_ENABLE_OLLAMA ollama-q36-a3b=$BAKEOFF_ENABLE_OLLAMA_Q36_A3B ollama-q36-mlx=$BAKEOFF_ENABLE_OLLAMA_Q36_MLX pplx=$BAKEOFF_ENABLE_PPLX"
log "cloud_model_label=$CLOUD_MODEL_LABEL"
log "ollama_model=$OLLAMA_MODEL host=$OLLAMA_HOST"
log "ollama_q36_a3b_model=$OLLAMA_Q36_A3B_MODEL"
log "ollama_q36_mlx_model=$OLLAMA_Q36_MLX_MODEL"
log "pplx_model_label=$PPLX_MODEL_LABEL"
log "sha256(dossier)=$(shasum -a 256 "$DOSSIER" | awk '{print $1}')"
log "sha256(coverage.py)=$(shasum -a 256 "$COVERAGE" | awk '{print $1}')"
log "host=$(uname -a)"

# --------------------------------------------------------------------------- #
# Assemble the LOCKED prompt (README §4)
# --------------------------------------------------------------------------- #
PROMPT_FILE="$RUN_DIR/PROMPT.txt"

{
  cat <<'PROMPT_HEADER'
You are drafting Chapter 1 of "The Database Decade," Peter S. Kastner's
Phase 3 longitudinal narrative on relational database management systems,
1970–2005. Use the evidence dossier below as your ONLY source of facts.
Do not introduce any Aberdeen study, benchmark, vendor claim, prescience
score, quotation, or historical event that is not present in the dossier.

Voice: follow the specification in Perplexity_Only/kastner_voice_prompt_v1.md
(first-person where Kastner is the actor, first-person-plural where Aberdeen
is the actor, thesis-first paragraphs, the eight Kastner rhetorical moves
used only where they earn their place, honest reckoning where Kastner got
something wrong).

Output TWO artifacts, in this order, separated by a line containing only
`---SIDECAR---`:

1. The narrative itself, in Markdown. Target 2,000–3,500 words. Every
   factual claim that maps to a specific study, observation, vendor
   evidence row, or prescience value in the dossier must carry an inline
   anchor in one of these forms:
     - `[study-<study_id>]` for a claim citing a study as a whole
     - `[obs-<obs_id>]` for a claim citing a specific observation
     - `[ps=<0-5>]` for a claim referencing a prescience value
   Anchors go inline, immediately after the claim, before punctuation.

2. A YAML block containing the sidecar fields defined in the fixture README §5.
   The YAML must parse cleanly; any content not in the schema is dropped.

Do not write a preamble, an outline, or a "Here is the narrative:" header.
Start the narrative with its first paragraph. End the narrative with its
last paragraph. Emit `---SIDECAR---` on its own line. Emit the YAML.
Nothing else.

=== DOSSIER BEGINS ===

PROMPT_HEADER
  cat "$DOSSIER"
  cat <<'PROMPT_TAIL'

=== DOSSIER ENDS ===
PROMPT_TAIL
} > "$PROMPT_FILE"

log "assembled prompt: $PROMPT_FILE ($(wc -c < "$PROMPT_FILE" | tr -d ' ') bytes)"

# --------------------------------------------------------------------------- #
# Contestant driver: split_output <contestant> <raw_output.txt>
#   Splits a raw contestant output at the ---SIDECAR--- separator into
#   narrative_<c>.md and sidecar_<c>.yaml.
# --------------------------------------------------------------------------- #
split_output() {
  local contestant="$1"
  local raw="$2"
  local narrative="$RUN_DIR/narrative_${contestant}.md"
  local sidecar="$RUN_DIR/sidecar_${contestant}.yaml"

  if ! grep -q '^---SIDECAR---$' "$raw"; then
    log "  [$contestant] WARN: no ---SIDECAR--- separator; treating entire output as narrative, empty sidecar"
    cp "$raw" "$narrative"
    : > "$sidecar"
    return 0
  fi

  # Everything before the separator = narrative; everything after = sidecar YAML.
  awk 'BEGIN{s=0} /^---SIDECAR---$/{s=1; next} {if(s) print > sc; else print > nv}' \
    sc="$sidecar" nv="$narrative" "$raw"

  # Models commonly wrap the requested YAML in a ```yaml fence despite the
  # prompt. Normalize only the fence markers; do not alter YAML content.
  if [[ -s "$sidecar" ]]; then
    sed -i.bak -e '/^```\(yaml\)\?$/d' "$sidecar"
    rm -f "${sidecar}.bak"
  fi

  log "  [$contestant] split: narrative=$(wc -w < "$narrative" | tr -d ' ')w sidecar=$(wc -l < "$sidecar" | tr -d ' ')L"
}

# --------------------------------------------------------------------------- #
# Contestant driver: run_ollama_contestant <contestant_id> <model_tag>
#   Generic Ollama driver. All three Ollama contestants (`ollama`,
#   `ollama-q36-a3b`, `ollama-q36-mlx`) route through this one function so
#   invocation semantics stay identical across models — the ONLY variable
#   between them is the model tag. Cloud and PPLX are agent-mediated (see
#   the "operator-drop protocol" below).
# --------------------------------------------------------------------------- #
run_ollama_contestant() {
  local contestant="$1"
  local model_tag="$2"
  local raw="$RUN_DIR/raw_${contestant}.txt"
  local body_file="$RUN_DIR/${contestant}_body.json"
  local response_file="$RUN_DIR/${contestant}_response.json"

  log "[$contestant] invoking $model_tag at $OLLAMA_HOST"

  if ! command -v curl >/dev/null 2>&1; then
    die "curl not available"
  fi

  # Build request JSON with jq, not Python. Detached/nohup runs on this Mac
  # produced Python "Bad file descriptor" failures after the first long curl.
  # `think:false` applies the documented Qwen 3.x non-thinking discipline.
  # num_predict=6000 is ample for the locked 2,000–3,500 word target while
  # preventing an unbounded overnight generation.
  jq -n \
    --arg model "$model_tag" \
    --rawfile prompt "$PROMPT_FILE" \
    '{
      model: $model,
      prompt: $prompt,
      stream: false,
      think: false,
      options: {num_ctx: 32768, num_predict: 6000}
    }' > "$body_file"

  local http_code
  http_code=$(curl -sS -o "$response_file" -w "%{http_code}" \
    --max-time "$OLLAMA_TIMEOUT_SEC" \
    -H "Content-Type: application/json" \
    -X POST "$OLLAMA_HOST/api/generate" \
    --data-binary "@$body_file" || echo "curl_failed")

  if [[ "$http_code" != "200" ]]; then
    log "[$contestant] ERROR: HTTP $http_code — see $response_file"
    log "[$contestant] SKIPPED — contestant will be absent from pre-filter report"
    return 1
  fi

  jq -r '.response // empty' "$response_file" > "$raw"
  if [[ ! -s "$raw" ]]; then
    log "[$contestant] ERROR: HTTP 200 but response field is empty — see $response_file"
    return 1
  fi
  log "[$contestant] raw output: $(wc -c < "$raw" | tr -d ' ') bytes"

  split_output "$contestant" "$raw"
  return 0
}

# --------------------------------------------------------------------------- #
# Operator-drop protocol for cloud & PPLX contestants
#
# The cloud contestant runs in a Computer session (this thread or a fresh one).
# The PPLX contestant runs via run_local_subagent on the Mac. Neither can be
# reliably invoked from a shell script — they are agent-mediated. The pattern:
#
#   1. This script writes the LOCKED prompt to $PROMPT_FILE.
#   2. For each enabled non-Ollama contestant, the script creates an empty
#      raw_<contestant>.txt placeholder and a per-contestant INSTRUCTIONS file
#      naming the exact model tag to use and the exact output file to write.
#   3. The orchestrating agent (or Pete) dispatches each contestant with the
#      prompt, captures the raw output, and writes it to raw_<contestant>.txt.
#   4. This script is re-invoked with RESUME=1 to continue the pipeline from
#      the drop point (split → coverage → prefilter → blind bundle).
#
# Rationale: keeping cloud and PPLX invocation out of shell code means the
# dispatcher does not need to know how to authenticate to either surface, and
# stays valid across changes to how Computer or Hybrid expose their models.
# --------------------------------------------------------------------------- #

prep_operator_drop() {
  local contestant="$1"
  local model_label="$2"
  local raw="$RUN_DIR/raw_${contestant}.txt"
  local instr="$RUN_DIR/INSTRUCTIONS_${contestant}.md"

  cat > "$instr" <<INSTR
# Operator drop — contestant: ${contestant}

**Model:** ${model_label}
**Run ID:** ${RUN_ID}
**Prompt file:** ${PROMPT_FILE}

## What to do

1. Dispatch this contestant with the prompt in \`${PROMPT_FILE}\` verbatim.
   Do not add a system message, wrapping instructions, retrieval augmentation,
   or any other modification. The prompt is LOCKED.

2. Capture the contestant's ENTIRE raw response (narrative + \`---SIDECAR---\`
   + YAML). Write it, verbatim, to:

       ${raw}

3. When all enabled contestants have their raw output on disk, re-invoke this
   script with:

       RESUME=1 bash run_bakeoff.sh

   RESUME=1 skips prompt re-assembly and re-invocation and picks up at the
   split → coverage → pre-filter → blind-bundle stages.

## Model dispatch notes (${contestant})

INSTR

  case "$contestant" in
    cloud)
      cat >> "$instr" <<'CLOUD'
- Cloud contestant runs in a Computer session — either this thread or a fresh
  one. Use the default frontier model at the time of the run. Record the exact
  model string in run_<UTC>.log via `CLOUD_MODEL_LABEL=<string> RESUME=1 bash run_bakeoff.sh`
  so cross-run diffs stay reconstructible.
- No tool calls, no retrieval, no browsing. The dossier is inline in the prompt.
CLOUD
      ;;
    pplx)
      cat >> "$instr" <<'PPLX'
- PPLX contestant runs in a Hybrid session on the Mac, dispatched via
  `run_local_subagent` from an orchestrating cloud session. The local model
  named above must be the model actually invoked — verify in the subagent's
  device metadata before dispatch.
- No cloud fall-back. If the local model errors or refuses, that is the
  contestant's result; do not retry with cloud.
PPLX
      ;;
  esac

  : > "$raw"   # empty placeholder so operators can see the expected filename
  log "[${contestant}] operator-drop staged: $instr"
  log "[${contestant}] awaiting output at: $raw"
}

# --------------------------------------------------------------------------- #
# Coverage + pre-filter helpers
# --------------------------------------------------------------------------- #
count_words() { wc -w < "$1" | tr -d ' '; }

# yaml_ok <path> — 0 if PyYAML can parse it into a non-empty dict, else 1
yaml_ok() {
  python3 - "$1" <<'PY'
import sys, yaml
p = sys.argv[1]
try:
    with open(p) as f:
        d = yaml.safe_load(f)
except Exception as e:
    print(f"parse-error: {e}"); sys.exit(1)
if not isinstance(d, dict) or not d:
    print("empty-or-non-dict"); sys.exit(1)
required = {"study_id","title","subject_domain","methodology",
            "pub_year_range","entity_cluster","prescience_anchors"}
missing = required - set(d.keys())
if missing:
    print(f"missing-keys: {sorted(missing)}"); sys.exit(1)
print("ok")
PY
}

run_coverage() {
  local contestant="$1"
  local narrative="$RUN_DIR/narrative_${contestant}.md"
  local out="$RUN_DIR/coverage_${contestant}.json"
  if [[ ! -s "$narrative" ]]; then
    log "  [$contestant] SKIP coverage: no narrative on disk"
    return 1
  fi
  python3 "$COVERAGE" "$contestant" "$narrative" --out "$out" > /dev/null
  local cov
  cov=$(python3 -c "import json; print(json.load(open('$out'))['coverage'])")
  # This function is used in command substitution. Send human-readable
  # logging to stderr so stdout contains the numeric value only.
  log "  [$contestant] coverage=${cov} (threshold=$COVERAGE_THRESHOLD)" >&2
  echo "$cov"
}

# --------------------------------------------------------------------------- #
# Main flow
# --------------------------------------------------------------------------- #
RESUME="${RESUME:-0}"

if [[ "$RESUME" != "1" ]]; then
  # Fresh run — invoke each enabled Ollama contestant directly, stage
  # operator-drop for cloud & PPLX.
  [[ "$BAKEOFF_ENABLE_OLLAMA"          == "1" ]] && run_ollama_contestant "ollama"          "$OLLAMA_MODEL"         || true
  [[ "$BAKEOFF_ENABLE_OLLAMA_Q36_A3B"  == "1" ]] && run_ollama_contestant "ollama-q36-a3b"  "$OLLAMA_Q36_A3B_MODEL" || true
  [[ "$BAKEOFF_ENABLE_OLLAMA_Q36_MLX"  == "1" ]] && run_ollama_contestant "ollama-q36-mlx"  "$OLLAMA_Q36_MLX_MODEL" || true
  [[ "$BAKEOFF_ENABLE_CLOUD"           == "1" ]] && prep_operator_drop cloud "$CLOUD_MODEL_LABEL"
  [[ "$BAKEOFF_ENABLE_PPLX"            == "1" ]] && prep_operator_drop pplx  "$PPLX_MODEL_LABEL"

  # If any operator-drop contestants are enabled and their raw file is empty,
  # we cannot proceed to split/coverage/prefilter. Halt here with instructions.
  needs_drop=0
  for c in cloud pplx; do
    enable_var="BAKEOFF_ENABLE_$(echo "$c" | tr '[:lower:]' '[:upper:]')"
    if [[ "${!enable_var}" == "1" && ! -s "$RUN_DIR/raw_${c}.txt" ]]; then
      needs_drop=1
    fi
  done

  if [[ "$needs_drop" == "1" ]]; then
    log "==="
    log "PAUSED: awaiting operator drops. See INSTRUCTIONS_*.md in $RUN_DIR."
    log "Re-invoke with: RUN_ID=$RUN_ID RESUME=1 bash run_bakeoff.sh"
    log "==="
    exit 0
  fi
fi

# --------------------------------------------------------------------------- #
# RESUME path — split any raw outputs that arrived, then run coverage, then
# pre-filter, then blind bundle.
# --------------------------------------------------------------------------- #

# All contestants, in a fixed enumeration order. The enable-var mapping is
# expressed as a function of the contestant id so this loop stays single-source.
ALL_CONTESTANTS=(cloud ollama ollama-q36-a3b ollama-q36-mlx pplx)

enable_var_for() {
  # Map contestant id → env-var name. Hyphens and dots become underscores;
  # everything uppercased.
  local c="$1"
  local up
  up=$(echo "$c" | tr '[:lower:]-.' '[:upper:]__')
  echo "BAKEOFF_ENABLE_${up}"
}

is_enabled() {
  local var
  var=$(enable_var_for "$1")
  [[ "${!var:-0}" == "1" ]]
}

# Split any raws that haven't been split yet (idempotent).
for c in "${ALL_CONTESTANTS[@]}"; do
  is_enabled "$c" || continue
  raw="$RUN_DIR/raw_${c}.txt"
  narrative="$RUN_DIR/narrative_${c}.md"
  if [[ -s "$raw" && ! -s "$narrative" ]]; then
    split_output "$c" "$raw"
  fi
done

# --------------------------------------------------------------------------- #
# Pre-filter (README §6)
# --------------------------------------------------------------------------- #
PREFILTER="$RUN_DIR/prefilter_report.md"

{
  echo "# Pre-filter report — run ${RUN_ID}"
  echo ""
  echo "| contestant | words | len_ok | sidecar_ok | coverage | cov_ok | overall |"
  echo "|---|--:|:-:|:-:|--:|:-:|:-:|"
} > "$PREFILTER"

declare -a PASSED_CONTESTANTS=()

for c in "${ALL_CONTESTANTS[@]}"; do
  is_enabled "$c" || continue

  narrative="$RUN_DIR/narrative_${c}.md"
  sidecar="$RUN_DIR/sidecar_${c}.yaml"

  if [[ ! -s "$narrative" ]]; then
    echo "| $c | – | – | – | – | – | ABSENT |" >> "$PREFILTER"
    log "[$c] ABSENT — no narrative on disk; skipping"
    continue
  fi

  words=$(count_words "$narrative")
  len_ok="no"
  (( words >= MIN_WORDS && words <= MAX_WORDS )) && len_ok="yes"

  sc_status=$(yaml_ok "$sidecar" 2>&1 || true)
  sc_ok="no"
  [[ "$sc_status" == "ok" ]] && sc_ok="yes"

  cov=$(run_coverage "$c" || echo "0.0")
  cov_ok="no"
  python3 -c "import sys; sys.exit(0 if float('$cov') >= float('$COVERAGE_THRESHOLD') else 1)" && cov_ok="yes"

  overall="FAIL"
  if [[ "$len_ok" == "yes" && "$sc_ok" == "yes" && "$cov_ok" == "yes" ]]; then
    overall="PASS"
    PASSED_CONTESTANTS+=("$c")
  fi

  echo "| $c | $words | $len_ok | $sc_ok | $cov | $cov_ok | $overall |" >> "$PREFILTER"
  log "[$c] prefilter: words=$words len=$len_ok sidecar=$sc_ok/${sc_status} coverage=$cov cov_ok=$cov_ok → $overall"
done

# Count enabled contestants generically (adapts as ALL_CONTESTANTS grows).
ENABLED_COUNT=0
for c in "${ALL_CONTESTANTS[@]}"; do
  is_enabled "$c" && ENABLED_COUNT=$((ENABLED_COUNT+1))
done

{
  echo ""
  echo "**Thresholds in force:** length window [$MIN_WORDS, $MAX_WORDS] words; coverage ≥ $COVERAGE_THRESHOLD."
  echo ""
  echo "**Passed:** ${#PASSED_CONTESTANTS[@]} / $ENABLED_COUNT enabled"
  echo ""
  echo "Manual step still required (README §6 check #5): spot-check 10 random anchored"
  echo "claims per passed contestant against the dossier, disqualify any that fabricate."
} >> "$PREFILTER"

log "prefilter report: $PREFILTER"

# --------------------------------------------------------------------------- #
# Blind bundle (README §6 final paragraph)
# --------------------------------------------------------------------------- #
if (( ${#PASSED_CONTESTANTS[@]} < 2 )); then
  log "blind bundle: SKIPPED — fewer than 2 contestants passed pre-filter"
  log "(Pete cannot blind-rank a single survivor; either fix and re-run, or accept the pre-filter as the result.)"
else
  # Shuffle the passed contestants and assign labels A, B, C, D, E (adapts to
  # however many passed). Uses /dev/urandom via python for portability; the
  # mapping is written to key.json which is NOT opened by Pete until after
  # ranking.
  python3 - "$BLIND_DIR" "${PASSED_CONTESTANTS[@]}" <<'PY'
import json, random, secrets, shutil, sys, os
blind_dir = sys.argv[1]
contestants = sys.argv[2:]
rng = random.Random(secrets.randbits(64))
labels = list("ABCDEFGH")[:len(contestants)]
order = contestants[:]
rng.shuffle(order)
run_dir = os.path.dirname(blind_dir.rstrip("/"))
key = {}
for label, contestant in zip(labels, order):
    src = os.path.join(run_dir, f"narrative_{contestant}.md")
    dst = os.path.join(blind_dir, f"{label}.md")
    shutil.copy(src, dst)
    key[label] = contestant
with open(os.path.join(blind_dir, "key.json"), "w") as f:
    json.dump({"run_id": os.path.basename(run_dir), "mapping": key}, f, indent=2)
print(f"blind bundle ready: {blind_dir} ({len(contestants)} contestants)")
PY
  log "blind bundle: $BLIND_DIR"
  log "Pete: read the blind/{A,B,C,…}.md files in order — do NOT open blind/key.json until ranking is written."
fi

log "=== run ${RUN_ID} complete ==="
