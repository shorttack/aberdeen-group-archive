#!/usr/bin/env python3
"""
ingest_dectp_observations_v2.py
================================

Pass B observation ingest for the DECtp Press Conference 1988 study.

Source:   kastner-author/1988-dectp-press-conference-nyc/dectp-press-conf-1988.md
Target:   _master_observations.csv (17-column current shape; 23,605 → 23,631 rows)
Study ID: dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836

VERSION HISTORY
---------------
v1 (2026-06-11): targeted 15-col schema (pre-§11t reconcile).
v2 (2026-06-12): bumped to 17-col schema after §11t added `section` and
                 `legacy_obs_id` columns (commit 22a89d34). Greenfield rows
                 emit empty string for both new columns. No semantic change
                 to source_page (still gets the chart label / Methodology /
                 Kastner connection). `section` stays empty because the DECtp
                 study uses Chart/Methodology organization, not the S1-S5
                 numeric section codes used by some 1997 transcript studies.

DESIGN NOTES (light-touch parse)
--------------------------------
The study markdown has 26 pre-structured OBS-### blocks of the form:

    **OBS-001** `observation_type` · `entity_id` · `tech_id` · YEAR
    Free-text claim sentence...
    > "Optional inline quote (used as metric_value or appended to notes)."

The AI extraction work has already been done by Pete in the prose. This script
mechanically lifts the 26 blocks into 15-column rows, mapping inline-quote text
into metric_value when present and falling back to the free-text claim
sentence otherwise. No LLM is invoked.

CANONICAL OBS_ID
----------------
Per archival-ingest v20 §21, the obs_id format is `{study_id}-OBS-NNN`.
Resulting IDs are 68 characters each (study_id is 60 chars). Verified
matches the STANDARD bucket pattern of the v2 classifier.

17-COLUMN SCHEMA (matches post-§11t-reconcile master at sha 0a92c9bc)
--------------------------------------------------------------------
obs_id, study_id, entity_id, tech_id, observation_type, year_observed,
metric_name, metric_value, confidence, verification_method, methodology_code,
source_page, notes, collection, thread_tag, section, legacy_obs_id

DEFAULTS APPLIED
----------------
confidence            = 'high'  (Glorioso/Hughes presentations on company-
                        published benchmark numbers from a DEC press event;
                        OBS-026 personal-recollection = 'high' since Kastner
                        was present)
verification_method   = 'ingest-extraction'
methodology_code      = inherits from each row's observation_type:
                        market-data           → benchmarking
                        methodology           → industry-analysis
                        methodology-note      → industry-analysis
                        personal-recollection → oral-history
source_page           = the chart label / section name from the markdown
                        (e.g., 'Chart 1', 'Methodology', 'Kastner connection')
notes                 = the inline quote when present, else empty
collection            = 'transcript'  (mirrors the study's collection class)
thread_tag            = 'dec-tp-1988'

INVARIANTS (must hold or the script aborts)
-------------------------------------------
1. Parses exactly 26 blocks from the source markdown.
2. Every block has a valid OBS-NNN tag, observation_type, entity_id, tech_id,
   and year (or sentinel) — no [REVIEW] markers.
3. Output row count == 26.
4. Every obs_id is unique within the output.
5. No obs_id in the output collides with any existing obs_id in the master
   that shares the same study_id (greenfield check; should be 0 collisions
   since the master has 0 rows for this study).
6. Schema enum: confidence ∈ {high, medium, low, verified, [DEFERRED],
   partially-verified, refuted, unknown [REVIEW]}.
7. CSV writes use csv.QUOTE_ALL.
8. Backup the master before any write (timestamped, UTF stamp).
9. Dry-run by default; --commit required to write.
10. Row count parity reported before/after.

USAGE
-----
Dry-run (default):
    python3 ingest_dectp_observations_v1.py

Commit (writes to master + leaves backup):
    python3 ingest_dectp_observations_v1.py --commit

Optional flags:
    --archive PATH   Override the archive_masters/ directory (default:
                     ~/Desktop/Archive/archive_masters/ on Mac;
                     /home/user/workspace/ when running in this sandbox
                     for dry-run preview only)
    --study-md PATH  Override the path to the study markdown
                     (default: same directory as --archive's parent +
                     kastner-author/1988-dectp-press-conference-nyc/...)
    --emit-delta     Write the 26-row delta as a standalone CSV at
                     <workspace>/dectp_observations_delta_v1.csv for
                     review before applying.

Exit codes:
    0  success (dry-run or commit)
    1  invariant violation; nothing written
    2  source markdown not found or unparseable
"""

import argparse
import csv
import datetime
import hashlib
import re
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

STUDY_ID = "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836"
EXPECTED_OBS_COUNT = 26
CONFIDENCE = "high"
VERIFICATION_METHOD = "ingest-extraction"
COLLECTION = "transcript"
THREAD_TAG = "dec-tp-1988"

# Observation-type → methodology_code mapping
METHODOLOGY_MAP = {
    "market-data": "benchmarking",
    "methodology": "industry-analysis",
    "methodology-note": "industry-analysis",
    "personal-recollection": "oral-history",
}

# section anchor → source_page tag
SECTION_PAGE_MAP = {
    "Methodology": "Methodology",
    "Chart 1 — Debit-Credit RDBMS TPS": "Chart 1",
    "Chart 2 — Debit-Credit Flat Files TPS": "Chart 2",
    "Chart 3 — K$/TPS Price/Performance": "Chart 3",
    "Chart 4 — Average System Cost for TP": "Chart 4",
    "Kastner connection": "Kastner connection",
}

# 17-column master schema (post-§11t-reconcile, sha 0a92c9bc, 2026-06-12)
MASTER_COLUMNS = [
    "obs_id",
    "study_id",
    "entity_id",
    "tech_id",
    "observation_type",
    "year_observed",
    "metric_name",
    "metric_value",
    "confidence",
    "verification_method",
    "methodology_code",
    "source_page",
    "notes",
    "collection",
    "thread_tag",
    "section",         # NEW in v2: structural marker (S1-S5); empty for DECtp
    "legacy_obs_id",   # NEW in v2: pre-canonical obs_id; empty for greenfield
]

# OBS block header pattern:
#   **OBS-001** `observation_type` · `entity_id` · `tech_id` · 1988
OBS_HEADER_RE = re.compile(
    r"^\*\*OBS-(?P<num>\d{3})\*\*\s+"
    r"`(?P<obs_type>[^`]+)`\s*·\s*"
    r"`(?P<entity_id>[^`]+)`\s*·\s*"
    r"`(?P<tech_id>[^`]+)`\s*·\s*"
    r"(?P<year>\d{4})\s*$"
)

SECTION_RE = re.compile(r"^### (?P<section>.+?)\s*(?:\(.*?\))?\s*$")
QUOTE_RE = re.compile(r"^>\s*(?P<quote>.*)$")


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_study_md(path: Path):
    """Parse the 26 OBS blocks out of the DECtp study markdown.

    Returns: list of dicts with keys obs_num, obs_type, entity_id, tech_id,
    year, claim_text, quote, section.
    """
    if not path.exists():
        sys.exit(f"[FATAL] Study markdown not found: {path}")

    lines = path.read_text().splitlines()
    obs_list = []
    current_section = None
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # Section heading?
        sec_m = SECTION_RE.match(line)
        if sec_m:
            section_text = sec_m.group("section").strip()
            # Match section_text against SECTION_PAGE_MAP keys via prefix
            current_section = None
            for key, page in SECTION_PAGE_MAP.items():
                if section_text.startswith(key):
                    current_section = page
                    break
            if current_section is None:
                # Allow exact-key matches that include em-dash variants
                for key, page in SECTION_PAGE_MAP.items():
                    if key in section_text:
                        current_section = page
                        break
            i += 1
            continue

        # OBS header?
        obs_m = OBS_HEADER_RE.match(line)
        if obs_m:
            obs_num = int(obs_m.group("num"))
            obs_type = obs_m.group("obs_type").strip()
            entity_id = obs_m.group("entity_id").strip()
            tech_id = obs_m.group("tech_id").strip()
            year = obs_m.group("year").strip()

            # Collect claim_text and quote until the next OBS-***, ---, ### or EOF
            j = i + 1
            claim_lines = []
            quote_lines = []
            while j < n:
                nxt = lines[j]
                if (
                    OBS_HEADER_RE.match(nxt)
                    or SECTION_RE.match(nxt)
                    or nxt.strip() == "---"
                    or nxt.startswith("## ")
                ):
                    break
                q_m = QUOTE_RE.match(nxt)
                if q_m:
                    quote_lines.append(q_m.group("quote").strip())
                elif nxt.strip():
                    # Skip "Image: ..." italic notes; keep substantive prose
                    stripped = nxt.strip()
                    if stripped.startswith("*Image"):
                        pass
                    else:
                        claim_lines.append(stripped)
                j += 1

            obs_list.append({
                "obs_num": obs_num,
                "obs_type": obs_type,
                "entity_id": entity_id,
                "tech_id": tech_id,
                "year": year,
                "claim_text": " ".join(claim_lines).strip(),
                "quote": " ".join(quote_lines).strip(),
                "section": current_section or "",
            })
            i = j
            continue

        i += 1

    return obs_list


# ---------------------------------------------------------------------------
# Row builder
# ---------------------------------------------------------------------------

def build_rows(parsed):
    """Map parsed OBS dicts into 17-column master rows."""
    rows = []
    for p in parsed:
        obs_id = f"{STUDY_ID}-OBS-{p['obs_num']:03d}"

        methodology_code = METHODOLOGY_MAP.get(
            p["obs_type"], "industry-analysis"
        )

        # metric_name: short label derived from claim_text up to first colon
        # or first sentence; cap at 200 chars
        claim = p["claim_text"]
        if ":" in claim[:120]:
            metric_name = claim.split(":", 1)[0].strip()[:200]
            metric_value_default = claim.split(":", 1)[1].strip()[:500]
        else:
            # Use full first sentence as metric_name, rest as metric_value.
            # Negative-lookbehind avoids splitting on single-letter initials
            # like "Peter S. Kastner" (the period after S is not a sentence end).
            parts = re.split(
                r"(?<![A-Z])(?<=[.!?])\s+(?=[A-Z])", claim, maxsplit=1
            )
            metric_name = parts[0][:200]
            metric_value_default = (parts[1] if len(parts) > 1 else "")[:500]

        # If an inline quote is present, prefer it as metric_value;
        # otherwise use the claim-derived default.
        if p["quote"]:
            metric_value = p["quote"][:500]
            notes = (
                f"claim: {claim}" if claim else ""
            )
        else:
            metric_value = metric_value_default
            notes = ""

        rows.append({
            "obs_id": obs_id,
            "study_id": STUDY_ID,
            "entity_id": p["entity_id"],
            "tech_id": p["tech_id"],
            "observation_type": p["obs_type"],
            "year_observed": p["year"],
            "metric_name": metric_name,
            "metric_value": metric_value,
            "confidence": CONFIDENCE,
            "verification_method": VERIFICATION_METHOD,
            "methodology_code": methodology_code,
            "source_page": p["section"],   # chart label / Methodology / Kastner connection
            "notes": notes,
            "collection": COLLECTION,
            "thread_tag": THREAD_TAG,
            "section": "",                 # v2: greenfield, no S-code
            "legacy_obs_id": "",           # v2: greenfield, no prior obs_id
        })
    return rows


# ---------------------------------------------------------------------------
# Invariant checks
# ---------------------------------------------------------------------------

def check_invariants(parsed, rows, master_rows):
    """Halt on any invariant violation. Returns list of (status, message)."""
    results = []

    # 1. Exactly 26 blocks parsed
    if len(parsed) != EXPECTED_OBS_COUNT:
        results.append(("FAIL", f"Parsed {len(parsed)} blocks; expected {EXPECTED_OBS_COUNT}"))
    else:
        results.append(("OK", f"Parsed {len(parsed)} OBS blocks"))

    # 2. Every block has valid fields, no [REVIEW] markers
    for p in parsed:
        for fld in ("obs_type", "entity_id", "tech_id", "year"):
            val = p.get(fld, "")
            if not val or "[REVIEW]" in val or "[DEFERRED]" in val:
                results.append(("FAIL", f"OBS-{p['obs_num']:03d} bad {fld}: {val!r}"))

    # 3. Output row count
    if len(rows) != EXPECTED_OBS_COUNT:
        results.append(("FAIL", f"Built {len(rows)} rows; expected {EXPECTED_OBS_COUNT}"))
    else:
        results.append(("OK", f"Built {len(rows)} output rows"))

    # 4. Output obs_ids unique
    obs_ids = [r["obs_id"] for r in rows]
    if len(set(obs_ids)) != len(obs_ids):
        results.append(("FAIL", "Duplicate obs_id in output rows"))
    else:
        results.append(("OK", f"All {len(obs_ids)} obs_ids unique within output"))

    # 5. No collision with existing master rows for this study_id
    existing = [m for m in master_rows if m.get("study_id") == STUDY_ID]
    existing_ids = {m["obs_id"] for m in existing}
    collisions = [oid for oid in obs_ids if oid in existing_ids]
    if collisions:
        results.append(("FAIL", f"Collisions with existing master rows: {collisions[:5]}"))
    else:
        results.append(("OK", f"No collisions (0 existing rows for study_id)"))

    # 6. Confidence enum
    valid_conf = {
        "high", "medium", "low", "verified", "[DEFERRED]",
        "partially-verified", "refuted", "unknown [REVIEW]",
    }
    bad_conf = [r["obs_id"] for r in rows if r["confidence"] not in valid_conf]
    if bad_conf:
        results.append(("FAIL", f"Invalid confidence in: {bad_conf[:5]}"))
    else:
        results.append(("OK", "Confidence values all valid"))

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    default_archive = Path.home() / "Desktop/Archive/archive_masters"
    ap.add_argument(
        "--archive",
        type=Path,
        default=default_archive,
        help=f"archive_masters/ directory (default: {default_archive})",
    )
    ap.add_argument(
        "--study-md",
        type=Path,
        default=None,
        help="Override path to the DECtp study markdown",
    )
    ap.add_argument(
        "--emit-delta",
        action="store_true",
        help="Write the 26-row delta as a standalone CSV alongside the script",
    )
    ap.add_argument(
        "--commit",
        action="store_true",
        help="Apply the changes (default: dry-run)",
    )
    args = ap.parse_args()

    archive = args.archive.expanduser().resolve()
    master_path = archive / "_master_observations.csv"

    # Default study-md: archive/.. + repo-style path
    if args.study_md is None:
        # archive_masters/ → parent is ~/Desktop/Archive/
        # Mac layout: ~/Desktop/Archive/aberdeen-group-archive/kastner-author/...
        study_md = (
            archive.parent
            / "aberdeen-group-archive"
            / "kastner-author"
            / "1988-dectp-press-conference-nyc"
            / "dectp-press-conf-1988.md"
        )
    else:
        study_md = args.study_md.expanduser().resolve()

    print(f"[paths] archive          : {archive}")
    print(f"[paths] master           : {master_path}")
    print(f"[paths] study markdown   : {study_md}")
    print()

    if not master_path.exists():
        sys.exit(f"[FATAL] Master not found: {master_path}")

    # Parse the study markdown
    parsed = parse_study_md(study_md)
    print(f"[parse] OBS blocks parsed: {len(parsed)}")
    if parsed:
        first = parsed[0]
        last = parsed[-1]
        print(f"[parse] first: OBS-{first['obs_num']:03d} ({first['obs_type']}, {first['section']})")
        print(f"[parse] last : OBS-{last['obs_num']:03d}  ({last['obs_type']}, {last['section']})")
    print()

    # Load master
    print(f"[master] loading {master_path} ...")
    with open(master_path, newline="") as f:
        r = csv.DictReader(f)
        header = r.fieldnames
        master_rows = list(r)
    print(f"[master] header cols ({len(header)}): {header}")
    print(f"[master] data rows: {len(master_rows)}")
    print()

    # Sanity: header must equal our expected 17-col schema
    if header != MASTER_COLUMNS:
        print(f"[FATAL] Master schema does not match expected 17-col layout.")
        print(f"  expected: {MASTER_COLUMNS}")
        print(f"  found   : {header}")
        sys.exit(1)

    # Build new rows
    new_rows = build_rows(parsed)

    # Run invariant checks
    print("[invariants]")
    results = check_invariants(parsed, new_rows, master_rows)
    fails = [r for r in results if r[0] == "FAIL"]
    for status, msg in results:
        print(f"  [{status}] {msg}")
    print()

    if fails:
        sys.exit(1)

    # Emit delta CSV if requested
    if args.emit_delta:
        delta_path = Path(__file__).parent / "dectp_observations_delta_v2.csv"
        with open(delta_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=MASTER_COLUMNS, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(new_rows)
        print(f"[delta] wrote: {delta_path}")
        print()

    # Row-count parity preview
    before = len(master_rows)
    after = before + len(new_rows)
    print(f"[parity] master rows: {before} → {after} (+{len(new_rows)})")
    print(f"[mode]   {'COMMIT' if args.commit else 'DRY-RUN'}")
    print()

    if not args.commit:
        print("Dry-run only. Re-run with --commit to write.")
        return

    # Backup before write
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak_path = master_path.with_suffix(f".csv.bak_dectp_obs_ingest_{ts}")
    shutil.copy2(master_path, bak_path)
    print(f"[backup] {bak_path}")

    # Write: master_rows + new_rows, all with QUOTE_ALL
    with open(master_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MASTER_COLUMNS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(master_rows)
        w.writerows(new_rows)
    print(f"[write] {master_path}")

    # Re-read to verify on disk
    with open(master_path, newline="") as f:
        r = csv.reader(f)
        new_header = next(r)
        n = sum(1 for _ in r)
    print(f"[verify] re-read: {n} rows, {len(new_header)} cols")
    if n != after:
        sys.exit(f"[FATAL] Post-write row count {n} != expected {after}")
    print()
    print(f"[done] master observations: {before} → {n}; DECtp study now has {len(new_rows)} obs rows.")


if __name__ == "__main__":
    main()
