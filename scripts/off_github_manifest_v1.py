#!/usr/bin/env python3
"""off_github_manifest_v1.py — register archival files that are NOT on GitHub.

Read-only on everything except its two outputs. Python standard library only.

What it registers
  Every archival-format file (PDF, Office, ZIP, audio/video; images with
  --include-images) found in
    (a) the archive repo, among files git ignores (too large, or derived), and
    (b) extra roots outside the repo (default: Memoirs/FLORIDA-documents, and only the
    top level of /tmp/FLORIDA, where originals land; its subfolders are OCR scratch),
  whose SHA-256 is NOT in the latest GitHub release manifest
  (releases/MANIFEST_v*.sha256). Files identical to something on GitHub are
  counted but not registered.

Scatter search
  With --scan-home it walks /Users/scott (skipping Library, .Trash, .git,
  caches, Time Machine) for files whose byte size equals a registered file, hashes
  them, and adds every identical copy as another location. iCloud placeholders
  (dataless files) are listed but not hashed, so nothing is downloaded.

Outputs (in --out-dir, default the repo root)
  OFF-GITHUB-MANIFEST.csv  one row per (sha256, location)
  OFF-GITHUB-MANIFEST.md   one entry per distinct file, with all its locations
If a previous CSV exists it is compared first: NEW, GONE, and CHANGED
locations are reported in the .md and on screen. Nothing is moved or deleted.

Usage
  cd /Users/scott/Desktop/Archive/aberdeen-group-archive
  python3 scripts/off_github_manifest_v1.py --scan-home
  python3 scripts/off_github_manifest_v1.py --dry-run      # print only, write nothing
"""
import argparse, csv, datetime as dt, glob, hashlib, os, re, stat, subprocess, sys

VERSION = "1.0"
HOME = "/Users/scott"
REPO = f"{HOME}/Desktop/Archive/aberdeen-group-archive"
EXTRA_ROOTS = [f"{HOME}/Desktop/Memoirs/FLORIDA-documents", "/private/tmp/FLORIDA"]
TRANSIENT = ("/private/tmp/", "/tmp/")
DOCS = r"pdf|zip|docx?|pptx?|xlsx?|rtf|odt|epub|mp4|mov|m4v|mp3|m4a|wav|aiff?"
IMAGES = r"tiff?|jpe?g|png|gif|heic"
ARCHIVAL = re.compile(rf"\.({DOCS})$", re.I)  # images added with --include-images
SHALLOW_ROOTS = ("/private/tmp/FLORIDA",)  # only top-level files: where originals land; subfolders are OCR scratch
SKIP_PARTS = {".git", "Library", ".Trash", "__pycache__", "node_modules", ".venv", "venv",
              "Perplexity_Only", "_local_backups", "_master_backups", ".cache", ".Spotlight-V100",
              ".DocumentRevisions-V100", ".fseventsd"}
SF_DATALESS = 0x40000000
MIN_SCATTER = 1_000_000  # only size-match files >= 1 MB during the home scan


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(8 << 20), b""):
            h.update(b)
    return h.hexdigest()


def dataless(st):
    return bool(getattr(st, "st_flags", 0) & SF_DATALESS)


def github_hashes(repo):
    files = sorted(glob.glob(os.path.join(repo, "releases", "MANIFEST_v*.sha256")),
                   key=lambda p: [int(x) for x in re.findall(r"\d+", os.path.basename(p))])
    if not files:
        sys.exit("BLOCKED: no releases/MANIFEST_v*.sha256 found; cannot tell what is on GitHub")
    hs = set()
    with open(files[-1], encoding="utf-8") as f:
        for line in f:
            if len(line) > 66:
                hs.add(line[:64])
    return files[-1], hs


def ignored_files(repo):
    out = subprocess.run(["git", "-C", repo, "ls-files", "-o", "-i", "--exclude-standard", "-z"],
                         capture_output=True, check=True).stdout
    for rel in out.decode("utf-8", "surrogateescape").split("\0"):
        if not rel or any(p in SKIP_PARTS for p in rel.split("/")):
            continue
        p = os.path.join(repo, rel)
        if os.path.isdir(p):
            for d, dirs, fs in os.walk(p):
                dirs[:] = [x for x in dirs if x not in SKIP_PARTS]
                for fn in fs:
                    yield os.path.join(d, fn)
        else:
            yield p


def walk(root):
    for d, dirs, fs in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_PARTS and not x.startswith(".Trash")]
        for fn in fs:
            yield os.path.join(d, fn)


def kind(path, repo):
    if path.startswith(repo + "/"):
        return "archive-repo (git-ignored)"
    if path.startswith(TRANSIENT):
        return "TRANSIENT /tmp (macOS may delete)"
    if "/Memoirs/FLORIDA-documents/" in path:
        return "Memoirs preservation area"
    return "elsewhere on Mac (scatter)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=REPO)
    ap.add_argument("--root", action="append", default=None, help="extra root (repeatable)")
    ap.add_argument("--scan-home", action="store_true")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--include-images", action="store_true",
                    help="also register images (off by default: page renders and OCR crops are not archival)")
    a = ap.parse_args()
    repo = os.path.realpath(a.repo)
    roots = a.root if a.root is not None else EXTRA_ROOTS
    out_dir = a.out_dir or repo
    global ARCHIVAL
    if a.include_images:
        ARCHIVAL = re.compile(rf"\.({DOCS}|{IMAGES})$", re.I)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    gh_file, gh = github_hashes(repo)
    cands = set(p for p in ignored_files(repo) if ARCHIVAL.search(p))
    for r in roots:
        if not os.path.isdir(r):
            continue
        if r in SHALLOW_ROOTS:
            cands.update(os.path.join(r, f) for f in os.listdir(r)
                         if ARCHIVAL.search(f) and os.path.isfile(os.path.join(r, f)))
        else:
            cands.update(p for p in walk(r) if ARCHIVAL.search(p))

    rows, on_github = {}, 0  # path -> dict
    for p in sorted(cands):
        try:
            st = os.stat(p)
        except OSError:
            continue
        if not stat.S_ISREG(st.st_mode):
            continue
        if dataless(st):
            rows[p] = dict(sha256="", size=st.st_size, note="iCloud placeholder, not hashed")
            continue
        h = sha256(p)
        if h in gh:
            on_github += 1
            continue
        rows[p] = dict(sha256=h, size=st.st_size, note="")

    scanned = 0
    if a.scan_home:
        sizes = {r["size"] for r in rows.values() if r["sha256"] and r["size"] >= MIN_SCATTER}
        want = {r["sha256"] for r in rows.values() if r["sha256"]}
        for p in walk(HOME):
            if p in rows:
                continue
            try:
                st = os.lstat(p)
            except OSError:
                continue
            if not stat.S_ISREG(st.st_mode) or st.st_size not in sizes:
                continue
            scanned += 1
            if dataless(st):
                rows[p] = dict(sha256="", size=st.st_size, note="iCloud placeholder with matching size, not hashed")
                continue
            try:
                h = sha256(p)
            except OSError:
                continue
            if h in want:
                rows[p] = dict(sha256=h, size=st.st_size, note="")

    for p, r in rows.items():
        r["mtime"] = dt.datetime.fromtimestamp(os.stat(p).st_mtime, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        r["kind"] = kind(p, repo)

    # compare with previous register
    csv_path = os.path.join(out_dir, "OFF-GITHUB-MANIFEST.csv")
    md_path = os.path.join(out_dir, "OFF-GITHUB-MANIFEST.md")
    changes = []
    if os.path.exists(csv_path):
        with open(csv_path, newline="", encoding="utf-8") as f:
            old = {r["path"]: r for r in csv.DictReader(f)}
        for p in sorted(set(old) | set(rows)):
            if p not in rows:
                changes.append(("GONE", p, old[p]["sha256"]))
            elif p not in old:
                changes.append(("NEW", p, rows[p]["sha256"]))
            elif old[p]["sha256"] != rows[p]["sha256"]:
                changes.append(("CHANGED", p, rows[p]["sha256"]))

    groups = {}
    for p, r in rows.items():
        groups.setdefault(r["sha256"] or f"unhashed:{p}", []).append(p)

    def safe(g):
        ks = {rows[p]["kind"] for p in g}
        durable = [k for k in ks if not k.startswith("TRANSIENT")]
        return "OK: 2+ durable copies" if len([p for p in g if not rows[p]["kind"].startswith("TRANSIENT")]) >= 2 \
            else ("SINGLE durable copy" if durable else "AT RISK: only in /tmp")

    lines = [f"# Off-GitHub Archival Files — Register",
             "",
             f"Generated {now} by `scripts/off_github_manifest_v1.py` v{VERSION}. Read-only scan; nothing was moved or deleted.",
             "",
             "Archival files (PDF, Office, ZIP, audio/video" + (", images" if a.include_images else "") + ") whose bytes are **not** in the latest GitHub release. "
             f"\"On GitHub\" means the SHA-256 appears in `{os.path.relpath(gh_file, repo)}`.",
             "",
             f"- Distinct files registered: **{len(groups)}**, total {sum(rows[g[0]]['size'] for g in groups.values()):,} bytes (one copy each)",
             f"- Locations registered: {len(rows)}",
             f"- Candidates skipped because identical to a file on GitHub: {on_github}",
             f"- Roots: git-ignored files in `{repo}`; " + "; ".join(f"`{r}`" for r in roots)
             + (f"; home-folder size-match search of `{HOME}` ({scanned} same-size files checked)" if a.scan_home else "; home-folder search not run"),
             "- Backup status is **not** asserted here. Time Machine or iCloud copies count only after a separate check.",
             ""]
    if changes:
        lines += ["## Changes since the previous register", "", "| Change | Path | SHA-256 |", "|---|---|---|"]
        lines += [f"| {c} | `{p}` | `{h[:16]}…` |" for c, p, h in changes] + [""]
    lines += ["## Files", ""]
    for key, g in sorted(groups.items(), key=lambda kv: -rows[kv[1][0]]["size"]):
        r0 = rows[g[0]]
        lines += [f"### {os.path.basename(g[0])}", "",
                  f"- SHA-256: `{r0['sha256'] or 'not hashed'}`",
                  f"- Size: {r0['size']:,} bytes",
                  f"- Copies: {len(g)} — {safe(g)}"]
        for p in sorted(g):
            n = f" ({rows[p]['note']})" if rows[p]["note"] else ""
            lines.append(f"  - {rows[p]['kind']}: `{p}`{n}")
        lines.append("")

    print(f"registered {len(groups)} distinct files at {len(rows)} locations; {on_github} skipped as on GitHub")
    for c, p, h in changes:
        print(f"  {c}: {p}")
    for key, g in groups.items():
        s = safe(g)
        if not s.startswith("OK"):
            print(f"  {s}: {os.path.basename(g[0])}")
    if a.dry_run:
        print("dry-run: nothing written")
        return
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sha256", "size", "path", "kind", "mtime_utc", "note", "generated_utc"])
        for p in sorted(rows, key=lambda p: (rows[p]["sha256"], p)):
            r = rows[p]
            w.writerow([r["sha256"], r["size"], p, r["kind"], r["mtime"], r["note"], now])
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {csv_path}\nwrote {md_path}")


if __name__ == "__main__":
    main()
