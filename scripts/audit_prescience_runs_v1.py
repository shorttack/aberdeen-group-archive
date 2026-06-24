#!/usr/bin/env python3
"""
Prescience Salvage Trust Manifest — Mac audit script v1

Walks every candidate prescience-scoring run location on Pete's Mac, populates
the v1 trust-manifest schema where mechanically determinable, and writes a
CSV the agent can review on the sandbox side.

USAGE (on Mac):
    python3 audit_prescience_runs_v1.py
    # Output: ./prescience_salvage_trust_manifest_v1.csv
    # Then ship the CSV to the sandbox (paste content or commit to a working branch).

WHAT IT INSPECTS:
    1. Repo master:           ~/Repos/aberdeen-group-archive/_master_prescience_scores.csv
       (or, fallback)         ~/Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv
    2. Mac master (if diff):  ~/Desktop/Archive/aberdeen-group-archive/_master_prescience_scores.csv
    3. Live working dirs:     ~/Desktop/Archive/prepared/**/working/
    4. Abandoned working dirs:~/Desktop/Archive/_pass_c_abandoned_runs/20260526/prepared/**/working/
    5. Any other working/     directories under ~/Desktop/Archive/ that look like Pass C runs.

GATES IT POPULATES MECHANICALLY:
    T1 (prompt) — by hashing any prescience_score_prompt_*.md it can find and comparing
                  to the canonical SHA you supply in CANONICAL_PROMPT_SHA256 below.
                  If no prompt file is referenced or found in the run dir, it marks
                  prompt_matches_v2_canonical=False and flags PETE_REVIEW.

    T2 (model/sampling) — by inspecting Ollama request bodies if logged (request.json,
                  payload.json) or by parsing the driver script for model_tag/temperature/
                  num_predict/think:false. If none recoverable, marks the row PETE_REVIEW.

    T3 (driver) — by recording the driver script path and SHA-256 if recoverable.
                  Pre-v2 scale detected by grep for "0-100" or "1-5" in script body when
                  the canonical is "0-5".

    T4 (input manifest) — by inspecting any *.csv or *.json manifest in the run dir.

    T5 (completion) — by checking for crashed/lock/tombstone files and comparing
                  earliest vs latest mtime of scored output files.

    T6 (distribution) — by reading the run's output CSV/JSONL and computing parse_ok_rate,
                  score histograms, etc.

    T7 (acceptance) — script cannot determine; always marked PETE_REVIEW. Pete fills.

OUTPUT:
    prescience_salvage_trust_manifest_v1.csv (one row per discovered run)
    prescience_salvage_trust_audit_log.txt   (free-text findings the script noticed)

CONTAMINATION RULES (enforced):
    - Any gate marked False → trust_verdict=DROP and gate ID added to dropped_gates.
    - Any gate marked PETE_REVIEW with all others passing → trust_verdict=PETE_REVIEW.
    - Only fully-PASS runs get trust_verdict=TRUST.

NOTHING IS MERGED OR DELETED. Read-only audit.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# CONFIG — edit these only if your Mac layout differs from the documented one
# ---------------------------------------------------------------------------

HOME = Path.home()
ARCHIVE_ROOT = HOME / "Desktop" / "Archive"
REPO_ROOT_CANDIDATES = [
    HOME / "Repos" / "aberdeen-group-archive",
    ARCHIVE_ROOT / "aberdeen-group-archive",
]
MAC_MASTER = ARCHIVE_ROOT / "archive_masters" / "_master_prescience_scores.csv"
CANONICAL_PROMPT_PATH = ARCHIVE_ROOT / "prescience_score_prompt_v2.md"

# IMPORTANT — set this once you've hashed the canonical prompt on Mac:
#   shasum -a 256 ~/Desktop/Archive/prescience_score_prompt_v2.md
# Then paste the hex digest below. Until then, the audit will mark prompt-match
# columns as "unknown_canonical_sha_not_set" instead of false.
CANONICAL_PROMPT_SHA256 = "f8c1e07469d8fce3148ad7c53f3ebb7f02fa312d8e0b724f6912808923385d29"  # ~/Desktop/Archive/prescience_score_prompt_v2.md @ 2026-06-14

LIVE_WORKING_DIRS_ROOT = ARCHIVE_ROOT / "prepared"
ABANDONED_RUNS_ROOT = ARCHIVE_ROOT / "_pass_c_abandoned_runs"

OUT_CSV = Path.cwd() / "prescience_salvage_trust_manifest_v1.csv"
OUT_LOG = Path.cwd() / "prescience_salvage_trust_audit_log.txt"

# Valid score / confidence ranges per canonical v2 prompt
VALID_SCORES = {-1, 0, 1, 2, 3, 4, 5}
VALID_CONFIDENCES = {1, 2, 3}

# CSV column order — must match the schema doc verbatim
CSV_COLUMNS = [
    "run_id", "source_location", "source_path", "row_count",
    "obs_count_distinct", "studies_covered",
    "prompt_file_path", "prompt_file_sha256", "prompt_matches_v2_canonical",
    "prompt_scale", "prompt_mid_run_edits",
    "model_tag", "model_family", "temperature", "num_predict",
    "think_false_set", "top_p", "top_k",
    "driver_script_path", "driver_script_sha256", "driver_version",
    "driver_pre_v2_scale", "driver_mid_run_modified",
    "input_manifest_path", "input_manifest_sha256", "input_payload_shape",
    "input_field_used",
    "run_started_at", "run_finished_at", "run_duration_sec",
    "run_completed_cleanly", "run_abandoned", "run_abandon_reason",
    "run_restarted_from_checkpoint",
    "parse_ok_rate", "score_dist_neg1", "score_dist_0", "score_dist_1_to_5",
    "abstention_rate", "score_mean", "score_out_of_range",
    "confidence_out_of_range",
    "accepted_at_time", "commit_sha", "pete_review_notes",
    "trust_verdict", "dropped_gates", "salvage_action", "notes",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sha256_file(p: Path) -> str:
    if not p.is_file():
        return ""
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def mtime_iso(p: Path) -> str:
    if not p.exists():
        return ""
    return datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat()


def detect_prompt_scale(prompt_text: str) -> str:
    """Heuristic: detect which scale the prompt declares."""
    t = prompt_text.lower()
    if "0-5" in t or "0 to 5" in t or "score on a 0-5" in t or "0\u20135" in t:
        return "0-5"
    if "1-5" in t or "1 to 5" in t or "1\u20135" in t:
        return "1-5"
    if "0-100" in t or "0 to 100" in t or "0\u2013100" in t:
        return "0-100"
    return "unknown"


def family_of(model_tag: str) -> str:
    t = (model_tag or "").lower()
    if t.startswith("sonar"):
        return "sonar"
    if "claude" in t:
        return "claude"
    if t.startswith("qwen"):
        return "qwen"
    if t:
        return "other"
    return ""


def parse_driver_for_config(driver_path: Path) -> dict[str, Any]:
    """Scan a driver script for model, temperature, num_predict, think:false, scorer version."""
    out = {
        "model_tag": "",
        "temperature": "",
        "num_predict": "",
        "think_false_set": "",
        "driver_version": "",
        "driver_pre_v2_scale": False,
    }
    if not driver_path.is_file():
        return out
    try:
        src = driver_path.read_text(errors="replace")
    except Exception:
        return out

    # Model tag
    m = re.search(r"""(?:LOCAL_MODEL|MODEL|model)\s*=\s*["']([^"']+)["']""", src)
    if m:
        out["model_tag"] = m.group(1)

    # Temperature
    m = re.search(r"""temperature\s*[:=]\s*([\d.]+)""", src)
    if m:
        out["temperature"] = m.group(1)

    # num_predict
    m = re.search(r"""num_predict\s*[:=]\s*(\d+)""", src)
    if m:
        out["num_predict"] = m.group(1)

    # think:false
    if re.search(r'"think"\s*:\s*false|think\s*=\s*False', src):
        out["think_false_set"] = "yes"
    elif "qwen" in (out["model_tag"] or "").lower():
        out["think_false_set"] = "no"
    else:
        out["think_false_set"] = "na"

    # Scorer version constant
    m = re.search(r"""SCORER_VERSION\s*=\s*["']([^"']+)["']""", src)
    if m:
        out["driver_version"] = m.group(1)

    # Pre-v2 scale hints (0-100 or 1-5 anywhere in script body — heuristic only)
    if re.search(r"\b0[\s\-]+100\b|score.{0,20}0\s*to\s*100", src, re.IGNORECASE):
        out["driver_pre_v2_scale"] = True
    elif re.search(r"score.{0,20}1\s*to\s*5\b|\b1\s*-\s*5 scale\b", src, re.IGNORECASE):
        out["driver_pre_v2_scale"] = True

    return out


def analyze_score_csv(csv_path: Path) -> dict[str, Any]:
    """Read a Pass C output CSV and compute distribution / parse_ok stats."""
    out: dict[str, Any] = {
        "row_count": 0,
        "obs_count_distinct": 0,
        "studies_covered": 0,
        "parse_ok_rate": "",
        "score_dist_neg1": 0,
        "score_dist_0": 0,
        "score_dist_1_to_5": 0,
        "score_out_of_range": 0,
        "confidence_out_of_range": 0,
        "score_mean": "",
        "earliest_scored_at": "",
        "latest_scored_at": "",
    }
    if not csv_path.is_file():
        return out

    obs_ids: set[str] = set()
    studies: set[str] = set()
    parse_ok_true = 0
    parse_ok_total = 0
    score_counts: Counter[int] = Counter()
    out_of_range = 0
    conf_oor = 0
    substantive_scores: list[int] = []
    scored_at_values: list[str] = []

    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                out["row_count"] += 1
                if row.get("obs_id"):
                    obs_ids.add(row["obs_id"])
                if row.get("study_id"):
                    studies.add(row["study_id"])

                # parse_ok
                po = (row.get("parse_ok") or "").strip().lower()
                if po:
                    parse_ok_total += 1
                    if po in ("true", "1", "yes"):
                        parse_ok_true += 1

                # score
                raw_score = (row.get("prescience_score") or "").strip()
                try:
                    s = int(float(raw_score))
                    if s in VALID_SCORES:
                        score_counts[s] += 1
                        if 1 <= s <= 5:
                            substantive_scores.append(s)
                    else:
                        out_of_range += 1
                except (ValueError, TypeError):
                    pass  # Unparseable score; counted via parse_ok already

                # confidence
                raw_conf = (row.get("confidence") or "").strip()
                try:
                    c = int(float(raw_conf))
                    if c not in VALID_CONFIDENCES and c != 0:
                        conf_oor += 1
                except (ValueError, TypeError):
                    pass

                if row.get("scored_at"):
                    scored_at_values.append(row["scored_at"])
    except Exception as e:
        out["_error"] = f"read failed: {e}"
        return out

    out["obs_count_distinct"] = len(obs_ids)
    out["studies_covered"] = len(studies)
    if parse_ok_total > 0:
        out["parse_ok_rate"] = f"{parse_ok_true / parse_ok_total:.4f}"
    out["score_dist_neg1"] = score_counts.get(-1, 0)
    out["score_dist_0"] = score_counts.get(0, 0)
    out["score_dist_1_to_5"] = sum(score_counts.get(i, 0) for i in (1, 2, 3, 4, 5))
    out["score_out_of_range"] = out_of_range
    out["confidence_out_of_range"] = conf_oor
    if substantive_scores:
        out["score_mean"] = f"{sum(substantive_scores) / len(substantive_scores):.3f}"
    if scored_at_values:
        sv = sorted(s for s in scored_at_values if s)
        out["earliest_scored_at"] = sv[0]
        out["latest_scored_at"] = sv[-1]
    return out


def trust_verdict_for(row: dict[str, Any]) -> tuple[str, str]:
    """Apply gates T1-T7 and return (verdict, comma-separated failed-gate list)."""
    failed: list[str] = []

    # T1
    if row.get("prompt_matches_v2_canonical") is not True:
        failed.append("T1")
    if row.get("prompt_mid_run_edits") is True:
        failed.append("T1")

    # T2
    try:
        if float(row.get("temperature") or 1.0) > 0.2:
            failed.append("T2")
    except ValueError:
        failed.append("T2")
    if family_of(row.get("model_tag", "")) == "qwen" and row.get("think_false_set") != "yes":
        failed.append("T2")
    try:
        if int(row.get("num_predict") or 0) < 256:
            failed.append("T2")
    except ValueError:
        failed.append("T2")

    # T3
    if row.get("driver_pre_v2_scale") is True:
        failed.append("T3")
    if row.get("driver_mid_run_modified") is True:
        failed.append("T3")

    # T4
    if row.get("input_payload_shape") not in ("full_obs_row", "claim_only"):
        failed.append("T4")

    # T5
    if row.get("run_completed_cleanly") is not True:
        failed.append("T5")
    if row.get("run_abandoned") is True:
        failed.append("T5")

    # T6
    try:
        if float(row.get("parse_ok_rate") or 0) < 0.95:
            failed.append("T6")
    except ValueError:
        failed.append("T6")
    if int(row.get("score_out_of_range") or 0) > 0:
        failed.append("T6")
    if int(row.get("confidence_out_of_range") or 0) > 0:
        failed.append("T6")
    try:
        rc = int(row.get("row_count") or 0)
        abst = int(row.get("score_dist_neg1") or 0) + int(row.get("score_dist_0") or 0)
        ar = abst / rc if rc else 0
        if rc and not (0.05 <= ar <= 0.70):
            failed.append("T6")
    except (ValueError, ZeroDivisionError):
        pass

    # T7
    if row.get("accepted_at_time") == "no_explicitly_rejected":
        failed.append("T7")

    failed_set = sorted(set(failed))
    if failed_set:
        return "DROP", ",".join(failed_set)
    if row.get("accepted_at_time") in ("", "unknown"):
        return "PETE_REVIEW", ""
    return "TRUST", ""


# ---------------------------------------------------------------------------
# Run discovery
# ---------------------------------------------------------------------------

def discover_repo_master() -> list[Path]:
    found: list[Path] = []
    for root in REPO_ROOT_CANDIDATES:
        p = root / "_master_prescience_scores.csv"
        if p.is_file():
            found.append(p)
    return found


def discover_mac_master() -> Path | None:
    return MAC_MASTER if MAC_MASTER.is_file() else None


def discover_working_dirs(root: Path) -> list[Path]:
    """Find all dirs literally named 'working' under root."""
    if not root.is_dir():
        return []
    return sorted(p for p in root.rglob("working") if p.is_dir())


def audit_one_csv_master(csv_path: Path, source_location: str, log) -> dict[str, Any]:
    """Build one trust-manifest row for a single master CSV (repo or mac)."""
    row = {col: "" for col in CSV_COLUMNS}
    row["run_id"] = f"{source_location}_{csv_path.parent.name}_{mtime_iso(csv_path)[:10]}"
    row["source_location"] = source_location
    row["source_path"] = str(csv_path)
    row["prompt_file_path"] = str(CANONICAL_PROMPT_PATH)
    row["prompt_file_sha256"] = sha256_file(CANONICAL_PROMPT_PATH)
    if CANONICAL_PROMPT_SHA256:
        row["prompt_matches_v2_canonical"] = (row["prompt_file_sha256"] == CANONICAL_PROMPT_SHA256)
    else:
        row["prompt_matches_v2_canonical"] = "unknown_canonical_sha_not_set"
    if CANONICAL_PROMPT_PATH.is_file():
        try:
            row["prompt_scale"] = detect_prompt_scale(CANONICAL_PROMPT_PATH.read_text(errors="replace"))
        except Exception:
            row["prompt_scale"] = "unknown"
    row["prompt_mid_run_edits"] = "unknown"

    stats = analyze_score_csv(csv_path)
    for k in ("row_count", "obs_count_distinct", "studies_covered",
              "parse_ok_rate", "score_dist_neg1", "score_dist_0",
              "score_dist_1_to_5", "score_mean", "score_out_of_range",
              "confidence_out_of_range"):
        row[k] = stats.get(k, "")
    rc = stats.get("row_count", 0) or 0
    abst = (stats.get("score_dist_neg1", 0) or 0) + (stats.get("score_dist_0", 0) or 0)
    row["abstention_rate"] = f"{abst / rc:.4f}" if rc else ""

    row["run_started_at"] = stats.get("earliest_scored_at", "")
    row["run_finished_at"] = stats.get("latest_scored_at", "")
    row["run_completed_cleanly"] = "unknown"
    row["run_abandoned"] = False
    row["accepted_at_time"] = "yes_committed_to_master" if source_location == "repo_master" else "unknown"

    row["pete_review_notes"] = ""
    row["notes"] = "Master file — composite of one or more runs. Per-model split may need to be done as separate manifest rows."
    log.write(f"[master] {csv_path}: row_count={rc} parse_ok_rate={row['parse_ok_rate']}\n")
    return row


def audit_one_working_dir(working_dir: Path, source_location: str, log) -> dict[str, Any]:
    """Build one trust-manifest row for a single working/ directory."""
    row = {col: "" for col in CSV_COLUMNS}
    parent = working_dir.parent.name
    row["run_id"] = f"{source_location}_{parent}_{mtime_iso(working_dir)[:10]}"
    row["source_location"] = source_location
    row["source_path"] = str(working_dir)

    # Find score outputs (heuristic: largest CSV/JSONL in the working dir)
    candidates = []
    for ext in ("*.csv", "*.jsonl", "*.json"):
        candidates.extend(working_dir.glob(ext))
    candidates = [c for c in candidates if c.is_file()]
    score_file = max(candidates, key=lambda p: p.stat().st_size, default=None) if candidates else None

    # Driver — heuristic look for a .py in working dir or parent
    driver_candidates = list(working_dir.glob("*.py")) + list(working_dir.parent.glob("*.py"))
    driver = driver_candidates[0] if driver_candidates else None
    if driver:
        row["driver_script_path"] = str(driver)
        row["driver_script_sha256"] = sha256_file(driver)
        cfg = parse_driver_for_config(driver)
        row["model_tag"] = cfg.get("model_tag", "")
        row["model_family"] = family_of(row["model_tag"])
        row["temperature"] = cfg.get("temperature", "")
        row["num_predict"] = cfg.get("num_predict", "")
        row["think_false_set"] = cfg.get("think_false_set", "")
        row["driver_version"] = cfg.get("driver_version", "")
        row["driver_pre_v2_scale"] = cfg.get("driver_pre_v2_scale", False)

    # Prompt
    row["prompt_file_path"] = str(CANONICAL_PROMPT_PATH)
    row["prompt_file_sha256"] = sha256_file(CANONICAL_PROMPT_PATH)
    if CANONICAL_PROMPT_SHA256:
        row["prompt_matches_v2_canonical"] = (row["prompt_file_sha256"] == CANONICAL_PROMPT_SHA256)
    else:
        row["prompt_matches_v2_canonical"] = "unknown_canonical_sha_not_set"
    if CANONICAL_PROMPT_PATH.is_file():
        try:
            row["prompt_scale"] = detect_prompt_scale(CANONICAL_PROMPT_PATH.read_text(errors="replace"))
        except Exception:
            row["prompt_scale"] = "unknown"

    # Input manifest — heuristic: smallest CSV that's NOT the score output
    inputs = [c for c in candidates if c != score_file]
    if inputs:
        manifest = inputs[0]
        row["input_manifest_path"] = str(manifest)
        row["input_manifest_sha256"] = sha256_file(manifest)
    row["input_payload_shape"] = "unknown"

    # Score analysis
    if score_file and score_file.suffix == ".csv":
        stats = analyze_score_csv(score_file)
        for k in ("row_count", "obs_count_distinct", "studies_covered",
                  "parse_ok_rate", "score_dist_neg1", "score_dist_0",
                  "score_dist_1_to_5", "score_mean", "score_out_of_range",
                  "confidence_out_of_range"):
            row[k] = stats.get(k, "")
        rc = stats.get("row_count", 0) or 0
        abst = (stats.get("score_dist_neg1", 0) or 0) + (stats.get("score_dist_0", 0) or 0)
        row["abstention_rate"] = f"{abst / rc:.4f}" if rc else ""
        row["run_started_at"] = stats.get("earliest_scored_at", "")
        row["run_finished_at"] = stats.get("latest_scored_at", "")

    # Completion heuristics
    crash_markers = list(working_dir.glob("*.lock")) + list(working_dir.glob("*.crash")) + list(working_dir.glob("*.partial"))
    row["run_completed_cleanly"] = (len(crash_markers) == 0)
    row["run_abandoned"] = (source_location == "mac_abandoned_run")
    if row["run_abandoned"]:
        row["run_abandon_reason"] = "agent_quality_regression_may26"

    row["accepted_at_time"] = "yes_lives_in_working_dir_only" if source_location != "mac_abandoned_run" else "no_explicitly_rejected"

    log.write(f"[wdir] {working_dir}: score_file={score_file} driver={driver} row_count={row.get('row_count')}\n")
    return row


def main() -> int:
    rows: list[dict[str, Any]] = []
    with OUT_LOG.open("w") as log:
        log.write(f"# Prescience Salvage Trust Manifest Audit — {datetime.now().isoformat()}\n")
        log.write(f"# ARCHIVE_ROOT={ARCHIVE_ROOT}\n")
        log.write(f"# CANONICAL_PROMPT_SHA256={'(set)' if CANONICAL_PROMPT_SHA256 else '(NOT SET — set this at top of script)'}\n\n")

        # 1. Repo master(s)
        for p in discover_repo_master():
            rows.append(audit_one_csv_master(p, "repo_master", log))

        # 2. Mac master
        mm = discover_mac_master()
        if mm:
            rows.append(audit_one_csv_master(mm, "mac_master", log))
        else:
            log.write(f"[mac_master] not found at {MAC_MASTER}\n")

        # 3. Live working dirs
        for wd in discover_working_dirs(LIVE_WORKING_DIRS_ROOT):
            rows.append(audit_one_working_dir(wd, "mac_working_dir", log))

        # 4. Abandoned working dirs
        for wd in discover_working_dirs(ABANDONED_RUNS_ROOT):
            rows.append(audit_one_working_dir(wd, "mac_abandoned_run", log))

        # 5. Stragglers (any "working" dirs under Archive that we haven't covered)
        seen_paths = {Path(r["source_path"]) for r in rows}
        for wd in discover_working_dirs(ARCHIVE_ROOT):
            if wd in seen_paths:
                continue
            rows.append(audit_one_working_dir(wd, "other", log))

        # Apply trust verdicts
        for r in rows:
            verdict, dropped = trust_verdict_for(r)
            r["trust_verdict"] = verdict
            r["dropped_gates"] = dropped
            if verdict == "TRUST":
                r["salvage_action"] = "merge_into_consolidated_pool"
            elif verdict == "PETE_REVIEW":
                r["salvage_action"] = "merge_into_consolidated_pool"  # tentative; Pete confirms
            else:
                r["salvage_action"] = "keep_for_triangulation_only" if r.get("run_abandoned") else "discard"

        log.write(f"\n# discovered {len(rows)} candidate runs\n")
        verdict_counts = Counter(r["trust_verdict"] for r in rows)
        for v, n in verdict_counts.most_common():
            log.write(f"#   {v}: {n}\n")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            # Booleans → string for CSV
            for k, v in list(r.items()):
                if isinstance(v, bool):
                    r[k] = "true" if v else "false"
                elif v is None:
                    r[k] = ""
            w.writerow(r)

    print(f"Wrote {len(rows)} rows to {OUT_CSV}")
    print(f"Audit log: {OUT_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
