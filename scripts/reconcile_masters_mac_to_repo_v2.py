#!/usr/bin/env python3
"""
reconcile_masters_mac_to_repo_v2.py
====================================

Job 1 of the 2026-06-11 §11t Mac↔repo masters reconcile.

Ships 5 master CSVs from Mac (~/Desktop/Archive/aberdeen-group-archive/) to repo
(shorttack/aberdeen-group-archive, flat at root) in ONE atomic commit via
the Git Data API multi-file batch pattern (kastner-github skill).

Files SHIPPED Mac→repo:
  1. _master_observations.csv         (overwrite — 23,605×17 v20 normalized)
  2. _master_entities.csv             (overwrite — 3,207×8 normalized form)
  3. _master_technologies.csv         (overwrite — 4,312×8 normalized form)
  4. _master_codes.csv                (overwrite — 1,293×4 rebuilt)
  5. _master_entity_field_conflicts.csv (CREATE — Mac-only diagnostic 3,711×5)

Backup tree (same atomic commit, preserves repo's pre-reconcile state):
  archive_masters_pre_reconcile_<UTCstamp>Z/_master_observations.csv
  archive_masters_pre_reconcile_<UTCstamp>Z/_master_entities.csv
  archive_masters_pre_reconcile_<UTCstamp>Z/_master_technologies.csv
  archive_masters_pre_reconcile_<UTCstamp>Z/_master_codes.csv
  archive_masters_pre_reconcile_<UTCstamp>Z/_README.md     (rollback guide)

(NOTE: backup blobs are inserted into the tree by *referencing* the repo's
existing blob shas at new paths — no re-upload, no risk of content drift.)

Also included in the same commit:
  WORKLIST.md                                            (refresh)
  _decisions_log.md                                      (append §11t entry)

Files NOT touched in this reconcile:
  _master_studies.csv     (already IN_SYNC)
  _known_entities.csv     (deferred — negligible drift)
  _known_technologies.csv (deferred — negligible drift)

Usage:
    # 1. Dry-run first — prints planned operations, no API writes.
    python3 reconcile_masters_mac_to_repo_v2.py
    # 2. Inspect output, confirm pre-flight passes.
    # 3. Commit:
    python3 reconcile_masters_mac_to_repo_v2.py --commit

Pre-flight halt conditions (any one → no commit):
  - Mac file missing or unreadable
  - Mac file row/col count drifted from the documented audit snapshot
  - Repo file's current blob sha changed since audit (concurrent commit)
  - Workspace WORKLIST.md / decisions log entry / decisions log master missing
  - WORKLIST_<date>.md and WORKLIST.md not byte-identical
  - gh CLI unavailable or unauthenticated

The pre-flight check protects against the scenario where masters have been
edited between the audit and the reconcile, OR where someone else pushed to
main between probe runs and reconcile.

Mandatory invariants (kastner-archive-pipeline skill §16.5, kastner-github):
  - csv.QUOTE_ALL on every CSV write (we don't re-write here — we ship bytes
    as they live on disk; the Mac files were already written QUOTE_ALL)
  - --commit is opt-in; dry-run is default
  - Row/col counts printed before and after for every shipped file
  - One atomic commit per repo (Git Data API tree + commit + ref update)
"""

from __future__ import annotations

import base64
import csv
import datetime as dt
import hashlib
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

# -------------------------------------------------------------------------
# CONFIGURATION — locked to the audit snapshot
# -------------------------------------------------------------------------

MAC_ROOT = Path.home() / "Desktop/Archive/aberdeen-group-archive"
WORKSPACE_HINT = "Files staged from workspace are inlined as content (not paths)."
REPO = "shorttack/aberdeen-group-archive"
REPO_BRANCH = "main"

# Audit-locked Mac-side expected shape. If any of these don't match what we
# read live, halt — masters have drifted since the audit.
MAC_EXPECTED = {
    "_master_observations.csv": {"rows": 23605, "cols": 17},
    "_master_entities.csv": {"rows": 3207, "cols": 8},
    "_master_technologies.csv": {"rows": 4312, "cols": 8},
    "_master_codes.csv": {"rows": 1293, "cols": 4},
    "_master_entity_field_conflicts.csv": {"rows": 3711, "cols": 5},
}

# Files that have a pre-reconcile repo blob to preserve. Excludes the Mac-only
# _master_entity_field_conflicts.csv (no repo state to preserve).
BACKUP_FILES = [
    "_master_observations.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_codes.csv",
]

# Audit-locked repo-side blob shas. From _audit_schema_overlap_20260612T005802Z.json
# (sample shared rows showed these as the prefix of the blob sha printed). We
# do NOT halt if these don't match (gh api will tell us live); but we print
# the delta so the user can confirm the audit snapshot is still current.
EXPECTED_REPO_BLOB_SHA_PREFIX = {
    "_master_observations.csv": "814f8215",  # from earlier turn
    "_master_entities.csv":     "2e5f5575",  # from probe 2
    "_master_technologies.csv": "e9363ced",
    "_master_codes.csv":        "305b7d5a",
}

# Workspace artifacts (read from workspace; this script runs on the Mac with
# a workspace mount OR a copy made into ~/Desktop/Archive/staging/).
WORKSPACE_ARTIFACTS = {
    # repo path                 : workspace path on Mac
    "WORKLIST.md":               Path("/home/user/workspace/WORKLIST.md"),
    "decisions_log_entry":       Path(
        "/home/user/workspace/decisions_log_entry_2026_06_11_11t_masters_reconcile_v1.md"
    ),
    "scripts/reconcile_masters_mac_to_repo_v2.py": Path(__file__).resolve(),
}

# Fallback workspace path on Pete's Mac if /home/user/workspace isn't mounted.
# Pete can `cp` workspace files to ~/Desktop/Archive/staging/ and re-run.
MAC_STAGING_DIR = Path.home() / "Desktop/Archive/staging"

# -------------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------------


def utc_compact() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def count_rows_cols(path: Path) -> tuple[int, int]:
    """Returns (data_row_count, header_col_count). QUOTE_ALL-safe via csv.reader."""
    with open(path, "r", newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        cols = len(header)
        rows = sum(1 for _ in r)
    return rows, cols


def gh_check() -> None:
    if shutil.which("gh") is None:
        die("`gh` CLI not on PATH")
    # Quick auth check
    p = subprocess.run(
        ["gh", "auth", "status"], capture_output=True, text=True
    )
    if p.returncode != 0:
        die(f"gh not authenticated: {p.stderr.strip()[:200]}")


def gh_get_contents_meta(filename: str) -> dict | None:
    """Returns the file's metadata dict, or None on 404."""
    p = subprocess.run(
        ["gh", "api", f"/repos/{REPO}/contents/{filename}?ref={REPO_BRANCH}"],
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        if "404" in (p.stderr or "").lower() or "not found" in (p.stderr or "").lower():
            return None
        die(f"gh api /contents/{filename} failed: {p.stderr.strip()[:200]}")
    return json.loads(p.stdout)


def gh_get_ref_sha(branch: str) -> str:
    p = subprocess.run(
        ["gh", "api", f"/repos/{REPO}/git/refs/heads/{branch}"],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api ref failed: {p.stderr.strip()[:200]}")
    return json.loads(p.stdout)["object"]["sha"]


def gh_get_commit_tree_sha(commit_sha: str) -> str:
    p = subprocess.run(
        ["gh", "api", f"/repos/{REPO}/git/commits/{commit_sha}"],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api commit failed: {p.stderr.strip()[:200]}")
    return json.loads(p.stdout)["tree"]["sha"]


def _safe_label_for_path(label: str) -> str:
    """v2 fix: labels can contain '/' (e.g. 'scripts/foo.py'). Sanitize to
    a tmpfile-safe basename so /tmp/_blob_req_<label>.json doesn't try to
    create a non-existent intermediate directory."""
    return label.replace("/", "__").replace("\\", "__")


def gh_create_blob_from_file(path: Path, label: str) -> str:
    """Creates a blob from a local file. Uses --input pattern for any file
    >150 KB to avoid E2BIG. Returns the blob sha."""
    size = path.stat().st_size
    # Build JSON request via Python (handles large files safely)
    req = {
        "content": base64.b64encode(path.read_bytes()).decode("ascii"),
        "encoding": "base64",
    }
    tmp = Path(f"/tmp/_blob_req_{_safe_label_for_path(label)}.json")
    tmp.write_text(json.dumps(req))
    p = subprocess.run(
        ["gh", "api", "--method", "POST", f"/repos/{REPO}/git/blobs",
         "--input", str(tmp)],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api create blob for {label} failed: {p.stderr.strip()[:300]}")
    sha = json.loads(p.stdout)["sha"]
    tmp.unlink(missing_ok=True)
    print(f"  blob({label:<60}) sha={sha[:10]}  size={size:>9} bytes")
    return sha


def gh_create_blob_from_bytes(data: bytes, label: str) -> str:
    """Same as above but from in-memory bytes."""
    req = {
        "content": base64.b64encode(data).decode("ascii"),
        "encoding": "base64",
    }
    tmp = Path(f"/tmp/_blob_req_{_safe_label_for_path(label)}.json")
    tmp.write_text(json.dumps(req))
    p = subprocess.run(
        ["gh", "api", "--method", "POST", f"/repos/{REPO}/git/blobs",
         "--input", str(tmp)],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api create blob for {label} failed: {p.stderr.strip()[:300]}")
    sha = json.loads(p.stdout)["sha"]
    tmp.unlink(missing_ok=True)
    print(f"  blob({label:<60}) sha={sha[:10]}  size={len(data):>9} bytes (in-memory)")
    return sha


def gh_create_tree(base_tree_sha: str, tree_entries: list[dict]) -> str:
    req = {"base_tree": base_tree_sha, "tree": tree_entries}
    tmp = Path("/tmp/_tree_req.json")
    tmp.write_text(json.dumps(req))
    p = subprocess.run(
        ["gh", "api", "--method", "POST", f"/repos/{REPO}/git/trees",
         "--input", str(tmp)],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api create tree failed: {p.stderr.strip()[:500]}")
    return json.loads(p.stdout)["sha"]


def gh_create_commit(message: str, tree_sha: str, parent_sha: str) -> str:
    req = {"message": message, "tree": tree_sha, "parents": [parent_sha]}
    tmp = Path("/tmp/_commit_req.json")
    tmp.write_text(json.dumps(req))
    p = subprocess.run(
        ["gh", "api", "--method", "POST", f"/repos/{REPO}/git/commits",
         "--input", str(tmp)],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api create commit failed: {p.stderr.strip()[:500]}")
    return json.loads(p.stdout)["sha"]


def gh_update_ref(branch: str, new_commit_sha: str) -> None:
    req = {"sha": new_commit_sha}
    tmp = Path("/tmp/_ref_req.json")
    tmp.write_text(json.dumps(req))
    p = subprocess.run(
        ["gh", "api", "--method", "PATCH",
         f"/repos/{REPO}/git/refs/heads/{branch}", "--input", str(tmp)],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        die(f"gh api update ref failed: {p.stderr.strip()[:500]}")


def die(msg: str) -> None:
    print(f"\nFATAL: {msg}", file=sys.stderr)
    sys.exit(2)


def resolve_workspace_artifact(repo_path: str, ws_path: Path) -> Path:
    """If workspace path doesn't exist on Mac, try ~/Desktop/Archive/staging/."""
    if ws_path.is_file():
        return ws_path
    # Try Mac-staged copy under filename basename
    # v2 fix: also fall back to ws_path basename (the original workspace
    # filename, e.g. 'decisions_log_entry_2026_06_11_11t_masters_reconcile_v1.md'),
    # not just Path(repo_path).name (which for a logical key like
    # 'decisions_log_entry' produces an unhelpful candidate).
    candidates = [
        MAC_STAGING_DIR / ws_path.name,
        MAC_STAGING_DIR / Path(repo_path).name,
        MAC_STAGING_DIR / repo_path,
    ]
    for c in candidates:
        if c.is_file():
            return c
    die(
        f"Workspace artifact not found for repo path {repo_path!r}.\n"
        f"  Looked at: {ws_path}\n"
        + "".join(f"  Also: {c}\n" for c in candidates) +
        f"\nFix: copy from sandbox workspace into {MAC_STAGING_DIR}/ and rerun.\n"
        "  cp /sandbox/workspace/<file> ~/Desktop/Archive/staging/<file>"
    )
    return ws_path  # unreachable


# -------------------------------------------------------------------------
# PRE-FLIGHT
# -------------------------------------------------------------------------


def preflight() -> dict:
    """Returns a dict of facts the commit phase will use. Halts on any failure."""
    print("=" * 72)
    print("PRE-FLIGHT")
    print("=" * 72)

    # 1. gh CLI
    gh_check()
    print("  [ok] gh CLI authenticated")

    # 2. Mac archive_masters/ exists
    if not MAC_ROOT.is_dir():
        die(f"MAC_ROOT not found: {MAC_ROOT}")
    print(f"  [ok] MAC_ROOT exists: {MAC_ROOT}")

    # 3. Mac master files exist + match audit-locked shape
    mac_files = {}
    for fn, expected in MAC_EXPECTED.items():
        p = MAC_ROOT / fn
        if not p.is_file():
            die(f"Mac file missing: {p}")
        rows, cols = count_rows_cols(p)
        if rows != expected["rows"] or cols != expected["cols"]:
            die(
                f"Mac file SHAPE DRIFT since audit: {fn}\n"
                f"  Expected: {expected['rows']}r x {expected['cols']}c\n"
                f"  Got     : {rows}r x {cols}c\n"
                f"  Halting. Re-run audit_mac_vs_repo_v1.py to diagnose."
            )
        sha = sha256_file(p)
        mac_files[fn] = {"path": p, "rows": rows, "cols": cols, "sha256": sha,
                         "size": p.stat().st_size}
        print(f"  [ok] {fn:<42} {rows:>6}r x {cols}c  sha256={sha[:10]}")

    # 4. Workspace artifacts exist + WORKLIST mirror byte-identical
    ws_artifacts = {}
    for repo_path, ws_path in WORKSPACE_ARTIFACTS.items():
        actual = resolve_workspace_artifact(repo_path, ws_path)
        ws_artifacts[repo_path] = actual
        print(f"  [ok] workspace artifact: {repo_path:<55} <- {actual}")

    # WORKLIST mirror integrity: dated mirror should match undated mirror.
    dated_candidates = sorted(
        Path("/home/user/workspace").glob("WORKLIST_*.md")
    ) if Path("/home/user/workspace").is_dir() else []
    dated_candidates += sorted(MAC_STAGING_DIR.glob("WORKLIST_*.md")) \
        if MAC_STAGING_DIR.is_dir() else []
    worklist_undated = ws_artifacts["WORKLIST.md"]
    if dated_candidates:
        # Pick the lexically latest WORKLIST_YYYY_MM_DD.md (today's)
        dated = dated_candidates[-1]
        if dated.read_bytes() == worklist_undated.read_bytes():
            print(f"  [ok] WORKLIST mirror byte-identical: {dated.name} == WORKLIST.md")
        else:
            die(
                f"WORKLIST mirror DRIFTED:\n"
                f"  Dated: {dated}\n"
                f"  Undated: {worklist_undated}\n"
                f"  Re-mirror before retry."
            )
    else:
        print("  [warn] no WORKLIST_<date>.md found — skipping mirror check")

    # 5. Repo state: fetch current main ref + tree, and per-file blob shas
    main_sha = gh_get_ref_sha(REPO_BRANCH)
    tree_sha = gh_get_commit_tree_sha(main_sha)
    print(f"  [ok] repo HEAD: {main_sha[:10]}  tree: {tree_sha[:10]}")

    repo_blobs = {}
    for fn in BACKUP_FILES:
        meta = gh_get_contents_meta(fn)
        if meta is None:
            die(f"Repo file unexpectedly absent: {fn}")
        blob_sha = meta["sha"]
        repo_blobs[fn] = {"blob_sha": blob_sha, "size": meta["size"]}
        expected_prefix = EXPECTED_REPO_BLOB_SHA_PREFIX.get(fn, "")
        if expected_prefix and not blob_sha.startswith(expected_prefix):
            die(
                f"Repo blob sha DRIFTED for {fn}:\n"
                f"  Expected prefix: {expected_prefix}\n"
                f"  Got: {blob_sha}\n"
                f"  Repo HEAD likely moved since audit. Re-run audits."
            )
        print(f"  [ok] repo blob preserved-by-ref: {fn:<42} sha={blob_sha[:10]}")

    # 6. _master_entity_field_conflicts.csv should NOT be in repo
    meta = gh_get_contents_meta("_master_entity_field_conflicts.csv")
    if meta is not None:
        die(
            "Repo unexpectedly has _master_entity_field_conflicts.csv — "
            "this reconcile plans to CREATE it, but it already exists.\n"
            f"Repo blob: {meta['sha'][:10]}. Investigate before retry."
        )
    print("  [ok] _master_entity_field_conflicts.csv confirmed absent from repo (CREATE)")

    # 7. Decisions-log master file exists in repo (we'll append to it)
    dl_meta = gh_get_contents_meta("_decisions_log.md")
    if dl_meta is None:
        die("Repo missing _decisions_log.md")
    print(f"  [ok] _decisions_log.md exists at repo root (sha={dl_meta['sha'][:10]})")

    print()
    return {
        "mac_files": mac_files,
        "ws_artifacts": ws_artifacts,
        "main_sha": main_sha,
        "tree_sha": tree_sha,
        "repo_blobs": repo_blobs,
        "dl_meta": dl_meta,
    }


# -------------------------------------------------------------------------
# DECISIONS-LOG APPEND PREP
# -------------------------------------------------------------------------


def build_appended_decisions_log(dl_meta: dict, entry_path: Path) -> bytes:
    """Fetches the current _decisions_log.md, appends the entry, returns bytes."""
    # The contents API returns base64 content directly for files < ~1 MB.
    # _decisions_log.md is well under that.
    content_b64 = dl_meta.get("content", "")
    if content_b64:
        existing = base64.b64decode(content_b64)
    else:
        # Larger file — fetch via blob API
        p = subprocess.run(
            ["gh", "api", f"/repos/{REPO}/git/blobs/{dl_meta['sha']}"],
            capture_output=True, text=True,
        )
        if p.returncode != 0:
            die(f"could not fetch _decisions_log.md blob: {p.stderr[:200]}")
        existing = base64.b64decode(json.loads(p.stdout)["content"])

    entry_bytes = entry_path.read_bytes()

    # Ensure existing ends with newline, then append entry with separator.
    sep = b"" if existing.endswith(b"\n") else b"\n"
    appended = existing + sep + b"\n" + entry_bytes
    print(f"  decisions log: existing {len(existing)} bytes + entry "
          f"{len(entry_bytes)} bytes = {len(appended)} bytes")
    return appended


# -------------------------------------------------------------------------
# BACKUP TREE README CONTENT
# -------------------------------------------------------------------------


def build_backup_readme(timestamp: str, repo_blobs: dict, main_sha: str) -> bytes:
    lines = [
        f"# archive_masters_pre_reconcile_{timestamp}",
        "",
        "**Created:** " + dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        f"**Source repo HEAD at time of backup:** `{main_sha}`",
        "",
        "## Purpose",
        "",
        "This directory preserves the repo's pre-reconcile state of four master CSVs",
        "as they existed on `main` before the §11t Mac↔repo masters reconcile",
        "(2026-06-11 PM EDT).",
        "",
        "The reconcile shipped the Mac's canonical post-May-24 state (v20 obs_id",
        "normalizer + namespace cleanup + codes rebuild) to the repo, where the",
        "files had been frozen since 2026-05-21 (`11670e87`) / 2026-05-26 (`0d48d9a8`).",
        "",
        "## Contents",
        "",
        "| File | Repo blob sha (pre-reconcile) | Size (bytes) |",
        "|---|---|---|",
    ]
    for fn in BACKUP_FILES:
        info = repo_blobs[fn]
        lines.append(f"| `{fn}` | `{info['blob_sha']}` | {info['size']} |")
    lines += [
        "",
        "## Rollback",
        "",
        "To restore the pre-reconcile state of any single file:",
        "",
        "```bash",
        f"# Replace WHICH with one of: " + ", ".join(BACKUP_FILES),
        "WHICH=_master_observations.csv",
        f"cd ~/Desktop/Archive/aberdeen-group-archive",
        "git checkout <RECONCILE_COMMIT_SHA>~1 -- $WHICH",
        "git commit -m \"Revert §11t reconcile of $WHICH\"",
        "git push origin main",
        "```",
        "",
        "Or directly from this backup tree:",
        "",
        "```bash",
        f"cp archive_masters_pre_reconcile_{timestamp}/$WHICH ./$WHICH",
        "git add $WHICH",
        "git commit -m \"Restore $WHICH from pre-§11t backup\"",
        "git push origin main",
        "```",
        "",
        "## Forever-archive principle",
        "",
        "These blobs are referenced into the §11t commit tree by sha, not re-uploaded.",
        "They are byte-identical to the repo's pre-reconcile state and remain reachable",
        "in git history regardless of future `main` movements.",
        "",
        "## Related",
        "",
        "- Decisions log entry: `_decisions_log.md` (§11t entry, 2026-06-11)",
        "- Audit artifacts (on Pete's Mac, not committed):",
        "  - `~/Desktop/Archive/_audit_mac_vs_repo_20260612T005318Z.csv`",
        "  - `~/Desktop/Archive/_audit_schema_overlap_20260612T005802Z.json`",
        "- Audit scripts (in repo):",
        "  - `scripts/audit_mac_vs_repo_v1.py` (commit `71ed3165`)",
        "  - `scripts/audit_schema_and_overlap_v1.py` (commit `187be686`)",
        "",
    ]
    return ("\n".join(lines)).encode("utf-8")


# -------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------


def main() -> int:
    commit_mode = "--commit" in sys.argv

    print(f"\nreconcile_masters_mac_to_repo_v2.py — "
          f"mode={'COMMIT' if commit_mode else 'DRY-RUN'}\n")

    facts = preflight()

    timestamp = utc_compact()
    # v2 fix: utc_compact() already returns trailing 'Z' — do not double it.
    backup_dir = f"archive_masters_pre_reconcile_{timestamp}"
    print(f"Backup tree path: {backup_dir}/")
    print()

    # ---------------------------------------------------------------------
    # Plan the tree entries
    # ---------------------------------------------------------------------

    # We need to know each new blob's sha. In COMMIT mode we create blobs;
    # in DRY-RUN we just compute local sha256 for visibility.

    plan_rows: list[dict] = []

    # (1) Masters to overwrite at repo root (4) + 1 new file
    for fn in [
        "_master_observations.csv",
        "_master_entities.csv",
        "_master_technologies.csv",
        "_master_codes.csv",
        "_master_entity_field_conflicts.csv",
    ]:
        mac_info = facts["mac_files"][fn]
        plan_rows.append({
            "op": "CREATE" if fn == "_master_entity_field_conflicts.csv" else "OVERWRITE",
            "repo_path": fn,
            "source": str(mac_info["path"]),
            "size": mac_info["size"],
            "rows": mac_info["rows"],
            "cols": mac_info["cols"],
            "sha256_local": mac_info["sha256"],
            "blob_sha": "(pending blob upload)",
        })

    # (2) Backup tree entries — preserve repo blob shas by reference
    for fn in BACKUP_FILES:
        info = facts["repo_blobs"][fn]
        plan_rows.append({
            "op": "PRESERVE_BY_REF",
            "repo_path": f"{backup_dir}/{fn}",
            "source": f"(repo's existing blob {info['blob_sha'][:10]})",
            "size": info["size"],
            "rows": "n/a",
            "cols": "n/a",
            "sha256_local": "(unchanged from repo)",
            "blob_sha": info["blob_sha"],
        })

    # (3) Backup README (new content built from repo_blobs + timestamp)
    # v2 fix: timestamp already has trailing 'Z' from utc_compact()
    backup_readme_bytes = build_backup_readme(timestamp, facts["repo_blobs"],
                                              facts["main_sha"])
    plan_rows.append({
        "op": "CREATE",
        "repo_path": f"{backup_dir}/_README.md",
        "source": "(generated in-memory)",
        "size": len(backup_readme_bytes),
        "rows": "n/a",
        "cols": "n/a",
        "sha256_local": sha256_bytes(backup_readme_bytes),
        "blob_sha": "(pending blob upload)",
    })

    # (4) WORKLIST.md refresh
    worklist_path = facts["ws_artifacts"]["WORKLIST.md"]
    plan_rows.append({
        "op": "OVERWRITE",
        "repo_path": "WORKLIST.md",
        "source": str(worklist_path),
        "size": worklist_path.stat().st_size,
        "rows": "n/a",
        "cols": "n/a",
        "sha256_local": sha256_file(worklist_path),
        "blob_sha": "(pending blob upload)",
    })

    # (5) Decisions log append
    entry_path = facts["ws_artifacts"]["decisions_log_entry"]
    appended_dl_bytes = build_appended_decisions_log(facts["dl_meta"], entry_path)
    plan_rows.append({
        "op": "APPEND_OVERWRITE",
        "repo_path": "_decisions_log.md",
        "source": f"(existing + workspace entry: {entry_path.name})",
        "size": len(appended_dl_bytes),
        "rows": "n/a",
        "cols": "n/a",
        "sha256_local": sha256_bytes(appended_dl_bytes),
        "blob_sha": "(pending blob upload)",
    })

    # (6) Ship this script itself for reproducibility
    self_path = Path(__file__).resolve()
    plan_rows.append({
        "op": "CREATE",
        "repo_path": "scripts/reconcile_masters_mac_to_repo_v2.py",
        "source": str(self_path),
        "size": self_path.stat().st_size,
        "rows": "n/a",
        "cols": "n/a",
        "sha256_local": sha256_file(self_path),
        "blob_sha": "(pending blob upload)",
    })

    # ---------------------------------------------------------------------
    # Print the plan
    # ---------------------------------------------------------------------

    print("=" * 100)
    print("RECONCILE PLAN")
    print("=" * 100)
    print(f"{'OP':<18} {'REPO PATH':<58} {'SIZE':>9}  rows/cols  notes")
    print("-" * 100)
    for r in plan_rows:
        rc = f"{r['rows']}r/{r['cols']}c" if r['rows'] != 'n/a' else ""
        print(f"{r['op']:<18} {r['repo_path']:<58} {r['size']:>9}  {rc:<10}")
    print("-" * 100)
    print(f"Total tree entries: {len(plan_rows)}")
    print(f"Atomic commit on {REPO} branch {REPO_BRANCH}")
    print(f"Parent commit: {facts['main_sha'][:10]}")
    print()

    if not commit_mode:
        print("DRY-RUN — no API writes performed.")
        print("Run again with --commit to execute.")
        return 0

    # ---------------------------------------------------------------------
    # COMMIT MODE: create blobs, tree, commit, update ref
    # ---------------------------------------------------------------------

    print("=" * 72)
    print("COMMIT: creating blobs")
    print("=" * 72)

    tree_entries: list[dict] = []

    # 1. Masters (5)
    for fn in [
        "_master_observations.csv",
        "_master_entities.csv",
        "_master_technologies.csv",
        "_master_codes.csv",
        "_master_entity_field_conflicts.csv",
    ]:
        mac_info = facts["mac_files"][fn]
        label = f"master:{fn}"
        blob_sha = gh_create_blob_from_file(mac_info["path"], label)
        tree_entries.append({
            "path": fn, "mode": "100644", "type": "blob", "sha": blob_sha
        })

    # 2. Backup tree by sha reference (no new blob upload)
    for fn in BACKUP_FILES:
        info = facts["repo_blobs"][fn]
        tree_entries.append({
            "path": f"{backup_dir}/{fn}",
            "mode": "100644",
            "type": "blob",
            "sha": info["blob_sha"],
        })
        print(f"  tree-entry(preserve-by-ref): "
              f"{backup_dir}/{fn:<42} sha={info['blob_sha'][:10]}")

    # 3. Backup README (new blob)
    readme_sha = gh_create_blob_from_bytes(backup_readme_bytes, "backup-readme")
    tree_entries.append({
        "path": f"{backup_dir}/_README.md",
        "mode": "100644", "type": "blob", "sha": readme_sha,
    })

    # 4. WORKLIST
    worklist_sha = gh_create_blob_from_file(worklist_path, "WORKLIST.md")
    tree_entries.append({
        "path": "WORKLIST.md", "mode": "100644", "type": "blob",
        "sha": worklist_sha,
    })

    # 5. Decisions log (appended)
    dl_sha = gh_create_blob_from_bytes(appended_dl_bytes, "_decisions_log.md")
    tree_entries.append({
        "path": "_decisions_log.md", "mode": "100644", "type": "blob",
        "sha": dl_sha,
    })

    # 6. This script
    self_sha = gh_create_blob_from_file(self_path, "scripts/reconcile_masters_mac_to_repo_v2.py")
    tree_entries.append({
        "path": "scripts/reconcile_masters_mac_to_repo_v2.py",
        "mode": "100644", "type": "blob", "sha": self_sha,
    })

    print()
    print("=" * 72)
    print("COMMIT: building tree")
    print("=" * 72)
    new_tree_sha = gh_create_tree(facts["tree_sha"], tree_entries)
    print(f"  new tree sha: {new_tree_sha[:10]} ({len(tree_entries)} entries)")

    print()
    print("=" * 72)
    print("COMMIT: creating commit object")
    print("=" * 72)

    commit_message = (
        "§11t Mac↔repo masters reconcile — ship Mac canonical state to repo\n\n"
        "Reconciles 5 master CSVs from ~/Desktop/Archive/aberdeen-group-archive/ to repo:\n"
        "  - _master_observations.csv         23,605×17  (v20 obs_id normalizer, 2026-05-24)\n"
        "  - _master_entities.csv             3,207×8    (normalized; dropped study_id col)\n"
        "  - _master_technologies.csv         4,312×8    (normalized; dropped study_id col)\n"
        "  - _master_codes.csv                1,293×4    (rebuilt/extended, dedup + cleanup)\n"
        "  - _master_entity_field_conflicts.csv 3,711×5  (NEW — Mac-only diagnostic)\n\n"
        f"Pre-reconcile repo blobs preserved at {backup_dir}/ "
        "(by sha reference — no re-upload).\n\n"
        "Mac state is canonical per:\n"
        "  - archival-ingest v20 §20.5 reference state (23,605×17 + verification_method)\n"
        "  - documented case-merge backup at "
        "Archive_legacy_2026_May/archive_masters_pre_case_merge_backup/\n"
        "  - single-writer invariant (Pete confirmed iPad has no GitHub/Archive access)\n"
        "  - codes rebuild confirmed by Pete (\"we rebuilt/extended codes at some point\")\n\n"
        "Diagnostic chain in _decisions_log.md §11t.\n"
        "Audit scripts: scripts/audit_mac_vs_repo_v1.py + audit_schema_and_overlap_v1.py.\n\n"
        "WORKLIST.md refreshed + _decisions_log.md appended in same atomic commit."
    )

    new_commit_sha = gh_create_commit(commit_message, new_tree_sha, facts["main_sha"])
    print(f"  new commit sha: {new_commit_sha}")

    print()
    print("=" * 72)
    print("COMMIT: updating refs/heads/main")
    print("=" * 72)
    gh_update_ref(REPO_BRANCH, new_commit_sha)
    print(f"  refs/heads/main -> {new_commit_sha}")

    print()
    print("=" * 72)
    print("DONE")
    print("=" * 72)
    print(f"Commit: https://github.com/{REPO}/commit/{new_commit_sha}")
    print(f"Backup tree: {backup_dir}/")
    print()
    print("Next on Mac (NOT this script's job — manual):")
    print(f"  cd ~/Desktop/Archive/aberdeen-group-archive && git pull")
    print("  # verify HEAD matches", new_commit_sha[:10])

    return 0


if __name__ == "__main__":
    sys.exit(main())
