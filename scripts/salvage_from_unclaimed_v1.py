#!/usr/bin/env python3
"""
salvage_from_unclaimed_v1.py

Second-pass article salvage from `_pdf_segments_unclaimed_v1.json`.

Background (2026-06-19 AM): the first union script admitted 105 articles to
`article_corpus_v1.json` by requiring the detector-extracted headline to
exactly match a CSV row's normalized headline. 425 PDF segments went
unclaimed (328 ARTICLE_HEAD + 69 ARTICLE_CONTINUATION + 26 UNKNOWN + 2 EMPTY).

This script re-mines those 425 segments using FOUR salvage strategies:

  S1 — ARTICLE_HEAD with truthy headline_attempted: probe the segment body
       for any CSV row's first-6-words. If a CSV headline appears in the
       body even though the detector's extracted headline didn't match,
       admit the article. (Covers the D6 "wrong headline detected" bucket:
       Wired + E-Commerce Times articles where the detector pulled a mid-
       paragraph quote as the headline.)

  S2 — UNKNOWN segments: probe body for any CSV row's first-6-words.
       (Covers Kastner Blog where there's no Page+Date anchor but the
       headline lives inside the body text.)

  S3 — ARTICLE_HEAD where headline_attempted *itself* contains a CSV
       headline as substring (rare; catches headline-extraction near-miss).

  S4 — ARTICLE_CONTINUATION: skip. The original detector already merged
       these into adjacent articles' body_text; salvaging them standalone
       would double-count.

For each salvaged segment, we emit a new article record with
`salvage_source` set to S1/S2/S3 and `headline` set to the matched CSV
headline (NOT the detector's wrong guess). Body is the segment raw text.

Reads:
  - kastner-author/quotations/article_corpus_v1.json  (existing 105)
  - kastner-author/quotations/_pdf_segments_unclaimed_v1.json  (425 segs)
  - kastner-author/quotations/quote_only_rows_v1.csv  (712 P2 rows)
  - kastner-author/quotations/kastner_quotes_clean.csv  (1087 CSV rows)

Writes (under --commit):
  - article_corpus_v1.json (UPDATED — 105 + N salvaged)
  - _pdf_segments_unclaimed_v1.json (UPDATED — minus the claimed segments)
  - quote_only_rows_v1.csv (UPDATED — minus rows now served by Pipeline 1)

Backup written for each output: `<file>.bak_salvage_v1_<utc-stamp>Z`.

Dry-run by default.
"""
import csv, json, re, shutil, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
CORPUS = QUOTATIONS_DIR / "article_corpus_v1.json"
UNCLAIMED = QUOTATIONS_DIR / "_pdf_segments_unclaimed_v1.json"
QUOTE_ONLY = QUOTATIONS_DIR / "quote_only_rows_v1.csv"
CSV_PATH = QUOTATIONS_DIR / "kastner_quotes_clean.csv"


def normalize_text(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower().strip("'\"").rstrip(";,.:").strip()


def first_n_words_norm(s: str, n: int = 6) -> str:
    return normalize_text(" ".join((s or "").split()[:n]))


def backup(path: Path, tag: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    b = path.with_suffix(path.suffix + f".bak_salvage_v1_{tag}_{stamp}")
    shutil.copy2(path, b)
    return b


def main(commit: bool = False):
    print(f"[salvage_from_unclaimed_v1] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # ----- Load -----
    corpus = json.loads(CORPUS.read_text())
    unclaimed = json.loads(UNCLAIMED.read_text())
    print(f"  current corpus articles : {corpus['article_count']}")
    print(f"  unclaimed segments      : {unclaimed['unclaimed_segment_count']}")

    with open(CSV_PATH) as f:
        csv_rows = list(csv.DictReader(f))
    print(f"  CSV rows                : {len(csv_rows)}")

    with open(QUOTE_ONLY) as f:
        quote_only_rows = list(csv.DictReader(f))
    quote_only_fieldnames = list(quote_only_rows[0].keys()) if quote_only_rows else []
    print(f"  quote-only rows         : {len(quote_only_rows)}")

    # ----- Build CSV indexes (target population for probing) -----
    # Probe needles: first-6-words normalized, drop headlines under 15 chars
    # (too short to discriminate). Map: probe -> set of normalized full headlines.
    probe_to_norm = {}
    norm_to_csv_meta = {}
    for r in csv_rows:
        h = (r.get("headline") or "").strip()
        if not h:
            continue
        nh = normalize_text(h)
        probe = first_n_words_norm(h, 6)
        if len(probe) < 15:
            continue
        probe_to_norm.setdefault(probe, set()).add(nh)
        if nh not in norm_to_csv_meta:
            norm_to_csv_meta[nh] = {
                "headline": h,
                "publication": (r.get("publication") or "").strip(),
                "date": (r.get("date") or "").strip(),
            }
    print(f"  CSV probe needles       : {len(probe_to_norm)}")

    # Only probe needles for headlines NOT already in the corpus
    served_norms = {a["headline_norm"] for a in corpus["articles"]}
    target_probes = {p: norms for p, norms in probe_to_norm.items()
                     if not (norms & served_norms)}
    print(f"  unserved probe needles  : {len(target_probes)}")
    print()

    # ----- Apply S1/S2/S3 to each unclaimed segment -----
    salvaged = []
    still_unclaimed = []
    s_counter = Counter()

    for seg in unclaimed["segments"]:
        cls = seg["classification"]
        body = seg.get("raw_preview", "")  # 600-char preview is our window
        # Segment body normalized once for substring probing
        body_norm = normalize_text(body)

        hit_norm = None
        salvage_source = None

        # S3: detector's headline_attempted IS or CONTAINS a CSV headline
        attempted = seg.get("headline_attempted") or ""
        if attempted:
            anorm = normalize_text(attempted)
            if anorm in served_norms:
                # Already served — but salvage script ran after admission?
                # Should not happen with current corpus. Skip.
                pass
            else:
                # Check if attempted appears verbatim in any unserved norm
                # or vice versa (substring)
                for nh in (probe_to_norm.get(first_n_words_norm(attempted, 6)) or set()):
                    if nh not in served_norms:
                        hit_norm = nh
                        salvage_source = "S3_attempted_first6"
                        break

        # S1: ARTICLE_HEAD with body probe (independent of S3 hit)
        if not hit_norm and cls == "ARTICLE_HEAD":
            for probe, norms in target_probes.items():
                if probe in body_norm:
                    # Pick the first un-served norm
                    cand = next((n for n in norms if n not in served_norms), None)
                    if cand:
                        hit_norm = cand
                        salvage_source = "S1_head_body_probe"
                        break

        # S2: UNKNOWN with body probe
        if not hit_norm and cls == "UNKNOWN":
            for probe, norms in target_probes.items():
                if probe in body_norm:
                    cand = next((n for n in norms if n not in served_norms), None)
                    if cand:
                        hit_norm = cand
                        salvage_source = "S2_unknown_body_probe"
                        break

        if hit_norm:
            meta = norm_to_csv_meta[hit_norm]
            salvaged.append({
                "source": "pdf_salvage",
                "salvage_source": salvage_source,
                "source_idx": seg["segment_idx"],
                "headline": meta["headline"],
                "headline_norm": hit_norm,
                "publication": meta["publication"],
                "date": meta["date"],
                "body": body,  # NB: 600-char preview only; full body requires re-reading PDF
                "body_chars": len(body),
                "spans_segments": [seg["segment_idx"]],
                "classification": cls,
                "detector_headline_attempted": attempted or None,
            })
            served_norms.add(hit_norm)
            s_counter[salvage_source] += 1
            # Re-prune target_probes so later segments can't claim the same headline
            stale_probes = [p for p, norms in target_probes.items()
                            if norms.issubset(served_norms)]
            for p in stale_probes:
                del target_probes[p]
        else:
            still_unclaimed.append(seg)

    print("=== Salvage results ===")
    for src, cnt in sorted(s_counter.items()):
        print(f"  {src:32s}: {cnt}")
    print(f"  TOTAL salvaged          : {len(salvaged)}")
    print(f"  still unclaimed         : {len(still_unclaimed)} / {len(unclaimed['segments'])}")
    print()

    # ----- Build updated corpus -----
    new_corpus_articles = list(corpus["articles"]) + salvaged
    new_corpus = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_pdf": corpus.get("source_pdf"),
        "source_rtf": corpus.get("source_rtf"),
        "source_csv": corpus.get("source_csv"),
        "article_count": len(new_corpus_articles),
        "rtf_admitted": corpus.get("rtf_admitted"),
        "pdf_admitted_new": corpus.get("pdf_admitted_new"),
        "salvage_admitted": len(salvaged),
        "salvage_breakdown": dict(s_counter),
        "articles": new_corpus_articles,
    }

    # ----- Updated unclaimed -----
    new_unclaimed = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_pdf": unclaimed.get("source_pdf"),
        "total_segments": unclaimed["total_segments"],
        "claimed_segment_count": unclaimed["total_segments"] - len(still_unclaimed),
        "unclaimed_segment_count": len(still_unclaimed),
        "salvage_pass": "v1",
        "segments": still_unclaimed,
    }

    # ----- Updated quote_only_rows -----
    # Rows whose headline is in the NEW corpus move from quote_only to Pipeline 1
    new_quote_only = []
    promoted_count = 0
    new_served_norms = {a["headline_norm"] for a in new_corpus_articles}
    for r in quote_only_rows:
        h = (r.get("headline") or "").strip()
        if h and normalize_text(h) in new_served_norms:
            promoted_count += 1
            continue
        new_quote_only.append(r)

    print("=== Pipeline routing delta ===")
    print(f"  Pipeline 2 → Pipeline 1 promotions: {promoted_count}")
    print(f"  Pipeline 2 rows remaining          : {len(new_quote_only)}")
    print(f"  Pipeline 1 corpus articles         : {len(new_corpus_articles)}")
    print()

    # ----- Sanity -----
    # Partition: pipeline_1_rows + pipeline_2_rows should still == total CSV rows
    # We don't recompute pipeline_1_rows from scratch here, just confirm
    # promoted_count == (old_qonly - new_qonly).
    assert len(quote_only_rows) - len(new_quote_only) == promoted_count

    if not commit:
        print("→ DRY-RUN — no files written. Pass --commit to write.")
        return

    # ----- Backup + write -----
    print("=== Writing ===")
    print(f"  backup: {backup(CORPUS, 'corpus')}")
    print(f"  backup: {backup(UNCLAIMED, 'unclaimed')}")
    print(f"  backup: {backup(QUOTE_ONLY, 'quote_only')}")

    CORPUS.write_text(json.dumps(new_corpus, indent=2, default=str))
    print(f"→ WROTE: {CORPUS} ({CORPUS.stat().st_size:,} bytes)")

    UNCLAIMED.write_text(json.dumps(new_unclaimed, indent=2, default=str))
    print(f"→ WROTE: {UNCLAIMED} ({UNCLAIMED.stat().st_size:,} bytes)")

    with open(QUOTE_ONLY, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=quote_only_fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in new_quote_only:
            w.writerow(r)
    print(f"→ WROTE: {QUOTE_ONLY} ({QUOTE_ONLY.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
