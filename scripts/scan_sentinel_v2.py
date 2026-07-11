#!/usr/bin/env python3
"""scan_sentinel_v2.py — READ-ONLY. TIGHTENED classifier for the image-stripper
ingest defect. v1 over-matched on any '&' in a title (legitimate ampersands like
'Digital & Oracle', 'AS&E', 'Q&A'). v2 uses precise, non-overlapping signatures:

  SIG_ABSTRACT : abstract contains 'text lost' OR 'image-stripper' OR
                 'intentionally omitted'   (the real boilerplate lie)
  SIG_TITLE_PLACEHOLDER : title contains 'intentionally omitted' or 'picture ['
  SIG_TITLE_URLENC      : title contains '%20' or '%25' (URL-encoded filename)
  SIG_TITLE_SLUG        : title matches the filename-slug pattern
                          '<token> ... (Aberdeen, YYYY)' where the doc title was
                          never recovered (leading token often a quarter code or
                          the study stem, e.g. 'Q206 Tasslick (Aberdeen, 2006)')

A study is DEFECTIVE if SIG_ABSTRACT OR any SIG_TITLE_*. A bare '&' is NOT a
signal. Reports counts by signature and by prepared-source availability.
"""
import csv, re
from pathlib import Path

A = Path.home() / "Desktop/Archive/aberdeen-group-archive"
PREP = Path.home() / "Desktop/Archive/prepared"

studies = list(csv.DictReader(open(A / "_master_studies.csv")))

SLUG = re.compile(r'\(Aberdeen,\s*\d{4}\)\s*$')  # trailing '(Aberdeen, YYYY)'

def has_source(sid):
    d = PREP / sid / "source"
    return any((d / fn).exists() for fn in ("_raw_text.txt","original_text.md","original.pdf"))

rows_out = []
c_abs = c_ph = c_url = c_slug = 0
for r in studies:
    sid = r["study_id"]; t = r.get("title") or ""; tl = t.lower(); ab = (r.get("abstract") or "").lower()
    sig_abs = ("text lost" in ab or "image-stripper" in ab or "intentionally omitted" in ab)
    sig_ph  = ("intentionally omitted" in tl or "picture [" in tl)
    sig_url = ("%20" in t or "%25" in t)
    # slug: trailing '(Aberdeen, YYYY)' AND the title looks like a filename stem
    # (heuristic: contains no lowercase sentence words before the paren, i.e.
    #  it's Title-Cased filename tokens). Use presence of the trailing marker plus
    #  a leading cap/quarter token.
    sig_slug = bool(SLUG.search(t)) and bool(re.match(r'^[0-9A-Za-z]', t))
    if not (sig_abs or sig_ph or sig_url or sig_slug):
        continue
    c_abs += sig_abs; c_ph += sig_ph; c_url += sig_url; c_slug += sig_slug
    sigs = ",".join(s for s,on in [("ABS",sig_abs),("PH",sig_ph),("URL",sig_url),("SLUG",sig_slug)] if on)
    rows_out.append([sid, "YES" if has_source(sid) else "no", sigs, t[:65]])

with_src = sum(1 for x in rows_out if x[1]=="YES")
print(f"TOTAL scanned: {len(studies)}")
print(f"DEFECTIVE (tightened): {len(rows_out)}   [with source: {with_src}  no-source: {len(rows_out)-with_src}]")
print(f"  by signature: ABS={c_abs}  TITLE_PLACEHOLDER={c_ph}  TITLE_URLENC={c_url}  TITLE_SLUG={c_slug}")
print()
# how many are ABS-only (would be pure light-fix if no source) vs slug/url (need title work)
abs_only = [x for x in rows_out if x[2]=="ABS"]
print(f"ABS-only (abstract lie, title already fine): {len(abs_only)}")
print()
print("study_id\tsrc\tsignatures\ttitle")
for x in sorted(rows_out, key=lambda r:(r[1], r[0])):
    print("\t".join(x))
