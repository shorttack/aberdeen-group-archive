#!/bin/bash
# triage_archive_uncommitted_v1.sh
# Read-only classifier for uncommitted work in aberdeen-group-archive.
# Buckets every M/?? path into: TODAY_COMPCHEM | V1_8_RESEARCH | JUNK | UNKNOWN
# Plus mtime + size for each file.

REPO="$HOME/Desktop/Archive/aberdeen-group-archive"
cd "$REPO" || exit 1

echo "=================================================================="
echo "  TRIAGE: $REPO"
echo "  $(git log -1 --format='HEAD: %h %ci')"
echo "=================================================================="

# Capture all uncommitted paths from git status --porcelain
git status --porcelain > /tmp/_status.txt

classify() {
    local path="$1"
    case "$path" in
        # Today's CompChem work
        *promote_compchem*) echo "TODAY_COMPCHEM" ;;
        *survey_mac_state*) echo "TODAY_COMPCHEM" ;;
        project_examples/*compchem*|project_examples/*conflicting-trends*) echo "TODAY_COMPCHEM" ;;
        # The literal junk filename
        '"\\012"'|*'\012'*) echo "JUNK" ;;
        # v1.8.0 quotations research outputs
        Perplexity_Only/quality_decline_*) echo "V1_8_RESEARCH" ;;
        Perplexity_Only/sh_calibration_*) echo "V1_8_RESEARCH" ;;
        Perplexity_Only/sh_sweep_*) echo "V1_8_RESEARCH" ;;
        kastner-author/quotations/*) echo "V1_8_RESEARCH" ;;
        scripts/audit_abandoned_qwen*) echo "V1_8_RESEARCH" ;;
        scripts/qwen_master_kappa*) echo "V1_8_RESEARCH" ;;
        # Reconcile script
        scripts/eod_quotations_reconcile_batch_commit*) echo "V1_8_RESEARCH" ;;
        # Logs with bracketed-paste-mangled names
        logs/phase*_.log012|logs/phases_*_done_.log012) echo "JUNK" ;;
        logs/phase*.log) echo "TODAY_COMPCHEM" ;;
        # Modified observations master = pre-existing drift; needs review
        _master_observations.csv) echo "PREEXISTING_MASTER_DRIFT" ;;
        # Legacy folder relocation
        scripts/v3_obsolete/*) echo "V1_7_LEGACY_MOVE" ;;
        scripts/v3_obsolete) echo "V1_7_LEGACY_MOVE" ;;
        *) echo "UNKNOWN" ;;
    esac
}

mtime_of() {
    if [ -e "$1" ]; then
        stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$1"
    else
        echo "(missing)"
    fi
}

size_of() {
    if [ -f "$1" ]; then
        stat -f "%z" "$1" | awk '{
            if ($1 > 1048576) printf("%.1fMB", $1/1048576)
            else if ($1 > 1024) printf("%.1fKB", $1/1024)
            else printf("%dB", $1)
        }'
    elif [ -d "$1" ]; then
        echo "(dir)"
    else
        echo "-"
    fi
}

# Read each line, classify, collect
declare -a TODAY_LINES V18_LINES JUNK_LINES PREEXIST_LINES LEGACY_LINES UNKNOWN_LINES

while IFS= read -r line; do
    # git status --porcelain format: " M path"  or  "?? path"
    flag="${line:0:2}"
    path="${line:3}"
    # Strip surrounding quotes if present (git quotes paths with special chars)
    path="${path%\"}"; path="${path#\"}"
    bucket=$(classify "$path")
    mt=$(mtime_of "$path")
    sz=$(size_of "$path")
    rec="  [$flag]  $sz  $mt  $path"
    case "$bucket" in
        TODAY_COMPCHEM)  TODAY_LINES+=("$rec") ;;
        V1_8_RESEARCH)   V18_LINES+=("$rec") ;;
        JUNK)            JUNK_LINES+=("$rec") ;;
        PREEXISTING_MASTER_DRIFT) PREEXIST_LINES+=("$rec") ;;
        V1_7_LEGACY_MOVE) LEGACY_LINES+=("$rec") ;;
        *)               UNKNOWN_LINES+=("$rec") ;;
    esac
done < /tmp/_status.txt

print_bucket() {
    local label="$1"; shift
    local arr=("$@")
    local n=${#arr[@]}
    echo
    echo "------------------------------------------------------------------"
    echo "  $label  ($n)"
    echo "------------------------------------------------------------------"
    if [ "$n" -eq 0 ]; then
        echo "  (none)"
    else
        printf '%s\n' "${arr[@]}"
    fi
}

print_bucket "TODAY_COMPCHEM (commit with EOD)"             "${TODAY_LINES[@]}"
print_bucket "PREEXISTING_MASTER_DRIFT (REVIEW before commit)" "${PREEXIST_LINES[@]}"
print_bucket "V1_7_LEGACY_MOVE (commit or skip)"             "${LEGACY_LINES[@]}"
print_bucket "V1_8_RESEARCH (defer for separate triage)"     "${V18_LINES[@]}"
print_bucket "JUNK (delete)"                                 "${JUNK_LINES[@]}"
print_bucket "UNKNOWN (manual review)"                       "${UNKNOWN_LINES[@]}"

# Special diagnostic: _master_observations.csv drift
echo
echo "=================================================================="
echo "  DIAGNOSTIC: _master_observations.csv pre-existing drift"
echo "=================================================================="
echo
echo "  HEAD blob row count (committed):"
git show HEAD:_master_observations.csv | wc -l | awk '{print "    "$1" lines"}'
echo
echo "  Working tree row count (live):"
wc -l _master_observations.csv | awk '{print "    "$1" lines"}'
echo
echo "  diff --stat (HEAD vs working tree):"
git diff --stat HEAD -- _master_observations.csv | sed 's/^/    /'
echo
echo "  Header diff (HEAD vs working tree):"
diff <(git show HEAD:_master_observations.csv | head -1 | tr ',' '\n') \
     <(head -1 _master_observations.csv | tr ',' '\n') \
     | head -30 || echo "    (no header diff)"

echo
echo "=================================================================="
echo "  Done."
echo "=================================================================="
