"""
§16 validation gate run against the consolidated batch CSVs.
"""
import csv
import sys
from pathlib import Path

ROOT = Path("/home/user/workspace/passb_output")

CHECKS = {
    "batch_studies_REPLACE_v1.csv": {
        "expected_cols": 16,
        "enum_columns": {
            # Default archive posture is CC-BY-4.0. Broadcast-news transcripts
            # (e.g. SARS CNBC/NBC Nightly 2003-04-03) are archived under
            # CC-BY-NC-SA-4.0 because the source video is third-party news
            # content; non-commercial share-alike is the safer posture.
            "license": {"CC-BY-4.0", "CC-BY-NC-SA-4.0"},
            "importance": {"high", "medium", "low"},
            "relevance": {"high", "medium", "low"},
            "prescience": {"high", "medium", "low", "not-applicable", "[DEFERRED]"},
        },
    },
    "batch_entities_APPEND_v1.csv": {"expected_cols": 9, "enum_columns": {}},
    "batch_technologies_APPEND_v1.csv": {"expected_cols": 9, "enum_columns": {}},
    "batch_observations_APPEND_v1.csv": {
        "expected_cols": 12,
        "enum_columns": {
            "confidence": {
                "high", "medium", "low", "verified", "[DEFERRED]",
                "partially-verified", "refuted", "unknown [REVIEW]",
            },
        },
    },
}

passes = 0
fails = 0


def check_plain_text(path):
    # Widened read window to 1000 bytes: QUOTE_ALL on a 16-column studies.csv
    # header runs ~250 bytes before the first newline; the original 200-byte
    # window produced a false-positive FAIL on legitimate per-study files
    # the moment they were assembled into batch form.
    with open(path, "rb") as f:
        head = f.read(1000)
    if b"," not in head or b"\n" not in head:
        return False
    text = head.decode("utf-8", errors="replace")
    alnum = sum(c.isalnum() or c in "+/=" for c in text)
    return alnum / max(len(text), 1) <= 0.85


def check_columns(path, expected):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        if len(header) != expected:
            return False, f"header {len(header)} != {expected}", header
        for i, row in enumerate(r, start=2):
            if len(row) != expected:
                return False, f"row {i} has {len(row)} cols", header
    return True, "ok", header


def check_enums(path, header, enums):
    issues = []
    name_to_idx = {h: i for i, h in enumerate(header)}
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for i, row in enumerate(r, start=2):
            for col, allowed in enums.items():
                if col not in name_to_idx:
                    continue
                v = row[name_to_idx[col]]
                if v not in allowed:
                    issues.append((i, col, v))
                    if len(issues) > 5:
                        return issues
    return issues


def quote_all_check(path):
    with open(path, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
    if not first_line:
        return False
    fields = first_line.split(",")
    return all(f.startswith('"') and f.endswith('"') for f in fields)


for fname, cfg in CHECKS.items():
    path = ROOT / fname
    print(f"\n=== {fname} ===")

    # Check 1: plain text
    if check_plain_text(path):
        print("  Check 1 (plain-text)         PASS")
        passes += 1
    else:
        print("  Check 1 (plain-text)         FAIL")
        fails += 1

    # Check 2: columns
    ok, msg, header = check_columns(path, cfg["expected_cols"])
    if ok:
        print(f"  Check 2 (column-count={cfg['expected_cols']})    PASS")
        passes += 1
    else:
        print(f"  Check 2 (column-count)       FAIL: {msg}")
        fails += 1

    # Check 3: enums
    issues = check_enums(path, header, cfg["enum_columns"])
    if not issues:
        print("  Check 3 (enums)              PASS")
        passes += 1
    else:
        print(f"  Check 3 (enums)              FAIL: {issues[:5]}")
        fails += 1

    # Check 4: QUOTE_ALL
    if quote_all_check(path):
        print("  Check 4 (QUOTE_ALL header)   PASS")
        passes += 1
    else:
        print("  Check 4 (QUOTE_ALL header)   FAIL")
        fails += 1

print(f"\n======================================================================")
print(f"SUMMARY: {passes} checks PASS, {fails} checks FAIL")
if fails == 0:
    print("Batch §16 validation gate: GREEN. Safe to ship to Mac.")
    sys.exit(0)
else:
    print("Batch §16 validation gate: RED. Fix before shipping.")
    sys.exit(1)
