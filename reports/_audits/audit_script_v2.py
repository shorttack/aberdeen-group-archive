#!/usr/bin/env python3
"""v18 Referential-Integrity Audit — v2.

Fixes false-positive base64 check (original §16 rule triggers on any CSV
whose header exceeds 200 bytes — this widens the read to 2 KB while
preserving the base64-density heuristic).

Aggregates full counts (not just first-20-studies slice).
"""
from __future__ import annotations
import csv
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

REPO = Path("/tmp/aberdeen-group-archive")

EXPECTED_COLS = {
    "studies.csv": 16,
    "entities.csv": 9,
    "technologies.csv": 9,
    "observations.csv": 12,
    "codes.csv": 4,
}
EXPECTED_HEADERS = {
    "studies.csv": ["study_id","title","author","date","type","subject_domain",
                    "methodology","source_file","abstract","license","importance",
                    "importance_rationale","relevance","relevance_rationale",
                    "prescience","prescience_rationale"],
    "entities.csv": ["entity_id","entity_name","entity_type","sector","status",
                     "successor","years_active","study_id","notes"],
    "technologies.csv": ["tech_id","tech_name","category","vendor","era",
                         "lifecycle_at_study","lifecycle_current","study_id","notes"],
    "observations.csv": ["obs_id","study_id","entity_id","tech_id","observation_type",
                         "year_observed","metric_name","metric_value","confidence",
                         "methodology_code","source_page","notes"],
}
RATING_VALID = {"high","medium","low","not-applicable","[DEFERRED]"}
IMP_REL_VALID = {"high","medium","low"}
CONF_VALID = {"high","medium","low","verified","[DEFERRED]",
              "partially-verified","refuted","unknown [REVIEW]"}


def is_plain_text(path: Path) -> tuple[bool, str]:
    # Widened to 2 KB to avoid false positives on wide studies.csv headers
    with open(path, "rb") as f:
        head = f.read(2048)
    if b"," not in head:
        return False, "missing comma in first 2KB"
    if b"\n" not in head:
        # file shorter than 2KB or truly one-line: allow if plain-text ASCII
        pass
    text = head.decode("utf-8", errors="replace")
    alnum = sum(c.isalnum() or c in "+/=" for c in text)
    ratio = alnum / max(len(text), 1)
    if ratio > 0.92:  # base64 is ~100%; ours ~55-65% due to commas and quotes
        return False, f"base64-density {ratio:.2f} > 0.92"
    return True, ""


def check_column_count(path: Path, expected: int) -> tuple[bool, str]:
    with open(path, "r", newline="", encoding="utf-8") as f:
        rdr = csv.reader(f)
        try:
            header = next(rdr)
        except StopIteration:
            return False, "empty file"
        if len(header) != expected:
            return False, f"header has {len(header)} cols, expected {expected}"
        for i, row in enumerate(rdr, start=2):
            if len(row) != expected:
                return False, f"row {i}: {len(row)} cols (expected {expected})"
    return True, ""


def check_header_match(path: Path, expected_header: list[str]) -> tuple[bool, str]:
    with open(path, "r", newline="", encoding="utf-8") as f:
        rdr = csv.reader(f)
        try:
            header = next(rdr)
        except StopIteration:
            return False, "empty file"
    if header != expected_header:
        for i, (got, want) in enumerate(zip(header, expected_header)):
            if got != want:
                return False, f"col {i}: got {got!r}, want {want!r}"
        return False, f"length mismatch: got {len(header)}, want {len(expected_header)}"
    return True, ""


def check_quote_all(path: Path) -> tuple[bool, str]:
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline().rstrip("\r\n")
    if not first:
        return False, "empty header line"
    fields = first.split(",")
    for fld in fields:
        fld = fld.strip()
        if not (fld.startswith('"') and fld.endswith('"')):
            return False, f"unquoted header field: {fld!r}"
    return True, ""


def check_enums_studies(path: Path) -> list[str]:
    errs = []
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            if row.get("license") != "CC-BY-4.0":
                errs.append(f"row {i}: license={row.get('license')!r}")
            if row.get("importance") not in IMP_REL_VALID:
                errs.append(f"row {i}: importance={row.get('importance')!r}")
            if row.get("relevance") not in IMP_REL_VALID:
                errs.append(f"row {i}: relevance={row.get('relevance')!r}")
            if row.get("prescience") not in RATING_VALID:
                errs.append(f"row {i}: prescience={row.get('prescience')!r}")
    return errs


def check_enums_observations(path: Path) -> list[str]:
    errs = []
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            c = row.get("confidence", "")
            if c and c not in CONF_VALID:
                errs.append(f"row {i}: confidence={c!r}")
    return errs


def check_abstract(path: Path) -> list[str]:
    errs = []
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            a = row.get("abstract", "") or ""
            if len(a) < 30:
                errs.append(f"row {i}: abstract too short ({len(a)} chars)")
                continue
            if "/" in a and len(a.split()) <= 3 and re.search(r"\.[A-Za-z0-9]{2,5}$", a.split("/")[-1]):
                errs.append(f"row {i}: abstract looks like file path")
                continue
            if a.startswith("data:") or a[-4:].endswith("=="):
                errs.append(f"row {i}: abstract looks like base64")
    return errs


def discover_studies() -> list[Path]:
    studies = []
    for parent in (REPO / "kastner-author", REPO / "other-authors"):
        if not parent.exists():
            continue
        for d in sorted(parent.iterdir()):
            if d.is_dir() and (d / "data").is_dir():
                studies.append(d)
    return studies


def layer_a(study: Path) -> tuple[list[str], Counter]:
    errs = []
    cats = Counter()
    data = study / "data"
    def load(name):
        p = data / name
        if not p.exists():
            errs.append(f"{name}: MISSING"); cats["missing_file"] += 1
            return []
        with open(p, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    ents = load("entities.csv")
    techs = load("technologies.csv")
    codes = load("codes.csv")
    obs = load("observations.csv")
    studies = load("studies.csv")

    ent_ids = {r.get("entity_id","") for r in ents}
    tech_ids = {r.get("tech_id","") for r in techs}
    # codes.csv schema varies across legacy batches. Collect every value from
    # any column that plausibly holds the obs_type label.
    code_ids = set()
    for r in codes:
        for col in ("code_id", "code", "code_value", "code_label", "label"):
            if col in r and r[col]:
                code_ids.add(r[col])

    for o in obs:
        oid = o.get("obs_id","?")
        if o.get("entity_id") and o["entity_id"] not in ent_ids:
            errs.append(f"obs[{oid}] entity_id={o['entity_id']!r} not in entities.csv")
            cats["entity_missing"] += 1
        if o.get("tech_id") and o["tech_id"] not in tech_ids:
            errs.append(f"obs[{oid}] tech_id={o['tech_id']!r} not in technologies.csv")
            cats["tech_missing"] += 1
        if o.get("observation_type") and o["observation_type"] not in code_ids:
            errs.append(f"obs[{oid}] observation_type={o['observation_type']!r} not in codes.csv")
            cats["obs_type_missing"] += 1

    if studies:
        row = studies[0]
        for field in ("study_id","title","author","date","type"):
            if not row.get(field):
                errs.append(f"studies.csv row 0: empty required field {field!r}")
                cats["empty_required"] += 1
    else:
        errs.append("studies.csv: no rows"); cats["no_studies_rows"] += 1
    return errs, cats


def layer_b(study: Path) -> tuple[list[str], Counter]:
    errs = []
    cats = Counter()
    data = study / "data"
    for name in ("studies.csv", "entities.csv", "technologies.csv", "observations.csv"):
        path = data / name
        if not path.exists():
            errs.append(f"{name}: MISSING"); cats["missing_file"] += 1
            continue
        ok, msg = is_plain_text(path)
        if not ok:
            errs.append(f"{name}: base64-guard FAIL ({msg})")
            cats["base64"] += 1
            continue
        ok, msg = check_column_count(path, EXPECTED_COLS[name])
        if not ok:
            errs.append(f"{name}: column-count FAIL ({msg})"); cats["column_count"] += 1
        ok, msg = check_header_match(path, EXPECTED_HEADERS[name])
        if not ok:
            errs.append(f"{name}: header FAIL ({msg})"); cats["header_mismatch"] += 1
        ok, msg = check_quote_all(path)
        if not ok:
            errs.append(f"{name}: QUOTE_ALL FAIL ({msg})"); cats["quote_all"] += 1
        if name == "studies.csv":
            for e in check_enums_studies(path):
                errs.append(f"{name}: enum {e}"); cats["enum_studies"] += 1
            for e in check_abstract(path):
                errs.append(f"{name}: abstract {e}"); cats["abstract"] += 1
        elif name == "observations.csv":
            for e in check_enums_observations(path):
                errs.append(f"{name}: enum {e}"); cats["enum_obs"] += 1
    return errs, cats


def layer_c(studies: list[Path]) -> dict:
    out = {
        "missing_entities": [],
        "missing_techs": [],
        "cache_dup_entities": [],
        "cache_dup_techs": [],
        "cache_empty_entities": 0,
        "cache_empty_techs": 0,
        "known_entities_count": 0,
        "known_techs_count": 0,
    }
    def load_cache(path):
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    ents_cache = load_cache(REPO / "_known_entities.csv")
    techs_cache = load_cache(REPO / "_known_technologies.csv")
    out["known_entities_count"] = len(ents_cache)
    out["known_techs_count"] = len(techs_cache)
    ent_id_key = list(ents_cache[0].keys())[0] if ents_cache else "id"
    tech_id_key = list(techs_cache[0].keys())[0] if techs_cache else "id"
    seen_ent = {}
    for r in ents_cache:
        eid = r.get(ent_id_key, "")
        if not eid:
            out["cache_empty_entities"] += 1; continue
        if eid in seen_ent:
            out["cache_dup_entities"].append(eid)
        seen_ent[eid] = True
    seen_tech = {}
    for r in techs_cache:
        tid = r.get(tech_id_key, "")
        if not tid:
            out["cache_empty_techs"] += 1; continue
        if tid in seen_tech:
            out["cache_dup_techs"].append(tid)
        seen_tech[tid] = True
    cache_ents = set(seen_ent)
    cache_techs = set(seen_tech)
    for s in studies:
        ep = s / "data" / "entities.csv"
        tp = s / "data" / "technologies.csv"
        if ep.exists():
            with open(ep, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    eid = r.get("entity_id", "")
                    if eid and eid not in cache_ents:
                        out["missing_entities"].append((eid, str(s.relative_to(REPO))))
        if tp.exists():
            with open(tp, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    tid = r.get("tech_id", "")
                    if tid and tid not in cache_techs:
                        out["missing_techs"].append((tid, str(s.relative_to(REPO))))
    return out


def main():
    studies = discover_studies()
    print(f"Discovered {len(studies)} studies")

    a_total_errs = 0
    b_total_errs = 0
    a_failed = []
    b_failed = []
    a_cats = Counter()
    b_cats = Counter()
    per_study_errs = {}

    for s in studies:
        ea, ca = layer_a(s)
        eb, cb = layer_b(s)
        if ea:
            a_total_errs += len(ea)
            a_failed.append(str(s.relative_to(REPO)))
            a_cats.update(ca)
        if eb:
            b_total_errs += len(eb)
            b_failed.append(str(s.relative_to(REPO)))
            b_cats.update(cb)
        if ea or eb:
            per_study_errs[str(s.relative_to(REPO))] = {"A": ea, "B": eb}

    c = layer_c(studies)

    lines = []
    def p(x=""):
        print(x); lines.append(x)

    p("═" * 78)
    p("v18 REFERENTIAL-INTEGRITY AUDIT — Aberdeen Group Archive (v2)")
    p("═" * 78)
    p(f"Repo: {REPO}")
    p(f"Studies scanned: {len(studies)}")
    p(f"  kastner-author: {sum(1 for s in studies if 'kastner-author' in str(s))}")
    p(f"  other-authors:  {sum(1 for s in studies if 'other-authors' in str(s))}")
    p(f"Cache: _known_entities.csv={c['known_entities_count']} rows,"
      f" _known_technologies.csv={c['known_techs_count']} rows")
    p("")

    p("─── LAYER A  Per-study referential integrity ───────────────────────────")
    p(f"  Studies with failures: {len(a_failed)} / {len(studies)}")
    p(f"  Total failures: {a_total_errs}")
    p(f"  Failure breakdown:")
    for k, v in a_cats.most_common():
        p(f"    {k}: {v}")
    p("  First few failed studies:")
    for sid in a_failed[:5]:
        p(f"    - {sid}")
        for err in per_study_errs[sid]["A"][:3]:
            p(f"        {err}")
    p("")

    p("─── LAYER B  §16 CSV Write Validation Gate ─────────────────────────────")
    p(f"  Studies with failures: {len(b_failed)} / {len(studies)}")
    p(f"  Total failures: {b_total_errs}")
    p(f"  Failure breakdown:")
    for k, v in b_cats.most_common():
        p(f"    {k}: {v}")
    p("  First few failed studies:")
    for sid in b_failed[:5]:
        p(f"    - {sid}")
        for err in per_study_errs[sid]["B"][:3]:
            p(f"        {err}")
    p("")

    p("─── LAYER C  Cross-study cache integrity ───────────────────────────────")
    p(f"  Entities missing from cache: {len(c['missing_entities'])}")
    for eid, sp in c['missing_entities'][:15]:
        p(f"    {eid!r}  in  {sp}")
    p(f"  Technologies missing from cache: {len(c['missing_techs'])}")
    for tid, sp in c['missing_techs'][:15]:
        p(f"    {tid!r}  in  {sp}")
    p(f"  Duplicate IDs in _known_entities.csv: {len(c['cache_dup_entities'])}")
    p(f"  Duplicate IDs in _known_technologies.csv: {len(c['cache_dup_techs'])}")
    p(f"  Empty ID rows in _known_entities.csv: {c['cache_empty_entities']}")
    p(f"  Empty ID rows in _known_technologies.csv: {c['cache_empty_techs']}")
    p("")

    total = a_total_errs + b_total_errs + len(c['missing_entities']) + len(c['missing_techs']) \
            + len(c['cache_dup_entities']) + len(c['cache_dup_techs']) \
            + c['cache_empty_entities'] + c['cache_empty_techs']

    p("═" * 78)
    if total == 0:
        p("RESULT: ALL CHECKS PASSED ✓")
    else:
        p(f"RESULT: {total} TOTAL FAILURES")
    p("═" * 78)

    # Write full failure list to a side file
    with open("/tmp/ref_int_failures_full.txt", "w") as fh:
        fh.write("LAYER A failures (by study)\n" + "="*78 + "\n")
        for sid, errs in per_study_errs.items():
            if errs["A"]:
                fh.write(f"\n{sid}\n")
                for e in errs["A"]:
                    fh.write(f"  {e}\n")
        fh.write("\n\nLAYER B failures (by study)\n" + "="*78 + "\n")
        for sid, errs in per_study_errs.items():
            if errs["B"]:
                fh.write(f"\n{sid}\n")
                for e in errs["B"]:
                    fh.write(f"  {e}\n")

    Path("/tmp/ref_int_audit_report.txt").write_text("\n".join(lines))
    sys.exit(0 if total == 0 else 1)


if __name__ == "__main__":
    main()
