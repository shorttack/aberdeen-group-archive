#!/usr/bin/env python3
"""
prepare_for_ingest_v3.py — Single-queue PDF ingest router for the Kastner Aberdeen Archive
==========================================================================================

Authored 2026-06-01 from the canonical principles in v2.2 (Pete Kastner).

Architectural shift from v2.x:
- v2.x had two modes (--mode new for buckets A-E, --mode existing for matching old
  PDFs to existing archive studies). The 5-bucket sort was a one-time tranche
  workflow and is retired.
- v3 is single-mode: one ingest queue, one router, three dispositions.

Architecture (locked 2026-06-01)
--------------------------------

Two repos, one wall:
- aberdeen-group-archive (public)        : TEXT ONLY (markdown + CSVs).
- kastner-restricted-sources (private)   : ALL PDFs. One PDF per study at
                                           <study_slug>.pdf. Flat layout.
                                           Image-heavy, copyrighted material.

The public archive never holds a PDF; the restricted repo never holds derived
text. v3 enforces this wall on every ingest.

Per-PDF disposition (one of three):
1. NEW
   - SHA-256 not in restricted repo + no archive title/filename match
   - ACTION: copy PDF to kastner-restricted-sources/<study_slug>.pdf
   - ACTION: extract markdown + entity/observation candidates for the public archive

2. BETTER (after manual accept in review CSV)
   - Archive title/filename match found AND incoming PDF appears stronger
     (more pages OR more images OR higher text-density per page)
   - ACTION: replace kastner-restricted-sources/<study_slug>.pdf with incoming
   - The displaced PDF is NOT retained outside git; restricted repo's git history
     is the only audit. A line is written to _decisions_log.md (caller responsibility).
   - The public archive markdown + CSVs are NOT touched — the textual work is
     considered done.

3. DUPLICATE / WORSE
   - Archive match found AND incoming is NOT better, OR you manually reject
   - ACTION: incoming PDF discarded from queue (NOT promoted anywhere)

Signals per PDF (deterministic, no AI):
- SHA-256 (exact file match -> instant DUPLICATE)
- Filename slug stem -> archive slug-token match
- Extracted title -> archive title fuzzy match (combined Levenshtein + token-set)
- Page count
- Embedded image count (rendered objects, not figure labels)
- Text-density proxy = avg chars of extracted text per page
  (low density on image-heavy PDFs vs higher density on text-layer PDFs)

Two-pass workflow:
- Pass 1: discover & propose. v3 walks the queue, computes signals, builds
  _review_<UTC>.csv with proposed_disposition for every PDF. NEW (no match)
  and AMBIGUOUS (match found but ambiguous-better) rows are surfaced for
  Pete to mark accept/reject.
- Pass 2: apply. v3 re-runs with --apply-review _review_<UTC>.csv and
  executes the (possibly Pete-modified) disposition for each row.

Repos and paths (all on Pete's Mac)
-----------------------------------

    ~/Desktop/Archive/
        _ingest_queue/                  -- input: drop PDFs here
        archive_masters/
            _known_entities.csv         -- read by entity pre-pass
        aberdeen-group-archive/         -- public archive clone (text only)
    ~/Desktop/Archive/kastner-restricted-sources/  -- private PDF vault
                                           (flat: <study_slug>.pdf per study)

Dependencies (all local, no AI):
    pip install pymupdf pymupdf4llm pandas

Author: drafted for Pete Kastner, 2026-06-01.
Lineage: principles inherited from prepare_for_ingest.py v2.2 (Mode 2 matching,
         figure rendering, entity/observation pre-pass, manifest discipline).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import re
import shutil
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("FATAL: PyMuPDF not installed. Run: pip install pymupdf")
try:
    import pymupdf4llm
except ImportError:
    sys.exit("FATAL: pymupdf4llm not installed. Run: pip install pymupdf4llm")


# =============================================================================
# Logging
# =============================================================================

log = logging.getLogger("prepare_for_ingest_v3")


def setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )


# =============================================================================
# Utilities (verbatim from v2.2)
# =============================================================================

def slugify(name: str, max_len: int = 80) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:max_len] or "untitled"


def study_slug(pdf_path: Path) -> str:
    """Idempotent slug + short hash suffix (matches archive convention)."""
    stem = pdf_path.stem
    h = hashlib.sha1(stem.encode("utf-8")).hexdigest()[:6]
    return f"{slugify(stem)}-{h}"


def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_stamp() -> str:
    """YYYYMMDDTHHMMSSZ — for filenames and decisions log."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


# =============================================================================
# Step 1 — PDF -> Markdown (verbatim from v2.2)
# =============================================================================

def step1_extract_markdown(pdf_path: Path, out_md: Path) -> dict:
    t0 = time.time()
    md_text = pymupdf4llm.to_markdown(str(pdf_path), show_progress=False)
    out_md.write_text(md_text, encoding="utf-8")
    return {
        "step": "1_extract_markdown",
        "tool": "pymupdf4llm",
        "output_md": str(out_md),
        "md_chars": len(md_text),
        "md_lines": md_text.count("\n") + 1,
        "elapsed_sec": round(time.time() - t0, 2),
    }


# =============================================================================
# Signal computation (v3-new: per-PDF features for disposition routing)
# =============================================================================

def count_embedded_images(pdf_path: Path) -> int:
    """Count embedded image objects across all pages.

    NOT the same as 'figures rendered' — this counts what PyMuPDF reports as
    raster image XObjects embedded in the PDF. Useful as a 'is this PDF
    image-heavy?' signal for the BETTER-version heuristic.
    """
    try:
        doc = fitz.open(str(pdf_path))
        count = 0
        for pno in range(len(doc)):
            count += len(doc[pno].get_images(full=False))
        doc.close()
        return count
    except Exception as e:
        log.debug(f"count_embedded_images failed for {pdf_path.name}: {e}")
        return 0


def text_density_proxy(md_chars: int, page_count: int) -> float:
    """Avg extracted-markdown chars per page.

    Heuristic proxy for scan quality:
    - Low density (< 200 chars/page) suggests image-only / OCR-poor scan.
    - High density (> 1500 chars/page) suggests proper text layer.

    Not a hard threshold — just a signal Pete weighs alongside page/image counts
    when deciding if an incoming PDF is BETTER than the archived predecessor.
    """
    if page_count <= 0:
        return 0.0
    return round(md_chars / page_count, 1)


# =============================================================================
# Step 3 — Figure extraction (v3: always-on; no bucket gating)
# =============================================================================
#
# Inherited from v2.2 step3_extract_figures, with the A/E bucket gate removed.
# Figure capture is now always on for every PDF — page rendering at 150 DPI
# of pages bearing "Figure N:" labels, SHA-1 dedup. Output is informational
# (lives in working/ alongside the markdown); the figures are NOT promoted
# to either repo. They support the manual review by giving Pete a sense of
# the document's visual character.

FIGURE_LABEL_RE = re.compile(
    r"\b(?:figure|fig\.?|chart|exhibit|table)\s*(\d+)\b[:.\s]",
    re.IGNORECASE,
)


def step3_extract_figures(pdf_path: Path, figures_dir: Path) -> dict:
    """Render PNG snapshots of pages bearing figure labels. Always on in v3."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    pages_with_labels: list[int] = []
    for pno in range(len(doc)):
        text = doc[pno].get_text() or ""
        if FIGURE_LABEL_RE.search(text):
            pages_with_labels.append(pno)

    seen_hashes: set[str] = set()
    figure_index: list[dict] = []
    fig_seq = 1
    for pno in pages_with_labels:
        mat = fitz.Matrix(150 / 72, 150 / 72)
        pix = doc[pno].get_pixmap(matrix=mat)
        png_bytes = pix.tobytes("png")
        h = hashlib.sha1(png_bytes).hexdigest()
        if h in seen_hashes:
            continue
        seen_hashes.add(h)
        out_path = figures_dir / f"figure_{fig_seq:03d}.png"
        out_path.write_bytes(png_bytes)
        page_text = doc[pno].get_text() or ""
        labels = FIGURE_LABEL_RE.findall(page_text)
        figure_index.append({
            "filename": out_path.name,
            "page": pno + 1,
            "sha1": h,
            "size_bytes": len(png_bytes),
            "labels_on_page": labels,
        })
        fig_seq += 1
    doc.close()

    if figure_index:
        idx_path = figures_dir / "figure_index.csv"
        with idx_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(
                f,
                fieldnames=["filename", "page", "sha1", "size_bytes", "labels_on_page"],
            )
            w.writeheader()
            for row in figure_index:
                w.writerow({**row, "labels_on_page": ";".join(row["labels_on_page"])})

    return {
        "step": "3_extract_figures",
        "pages_with_labels": len(pages_with_labels),
        "figures_extracted": len(figure_index),
        "figures_dir": str(figures_dir),
        "figures": figure_index,
    }


# =============================================================================
# Step 4 — Entity pre-pass (verbatim from v2.2)
# =============================================================================

_COMMON_ENGLISH_BASES = {
    "information", "data", "systems", "network", "networks", "software",
    "hardware", "computer", "computers", "computing", "digital", "electronic",
    "global", "international", "national", "general", "american", "european",
    "business", "enterprise", "corporate", "professional", "advanced",
    "technology", "technologies", "solutions", "services", "products",
    "applications", "communications", "resources", "industries",
    "management", "consulting", "research", "analytics", "associates",
    "the", "and", "new", "open", "web", "internet", "online",
}


def load_known_entities(csv_path: Path) -> list[dict]:
    entities: list[dict] = []
    with csv_path.open(encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            name = (row.get("entity_name") or "").strip()
            if not name:
                continue
            alts = {name}
            base = re.sub(
                r"\s+(?:Inc\.?|Corp\.?|Corporation|Group|Ltd\.?|LLC|Company|Co\.?)\b",
                "",
                name,
                flags=re.IGNORECASE,
            ).strip()
            base_words = base.split()
            base_lower_words = [w.lower() for w in base_words]
            if (
                base
                and base != name
                and len(base) >= 4
                and base.lower() not in _COMMON_ENGLISH_BASES
                and len(base_words) >= 2
                and base_lower_words[0] not in _COMMON_ENGLISH_BASES
                and any(w not in _COMMON_ENGLISH_BASES for w in base_lower_words)
                and not all(w in _COMMON_ENGLISH_BASES for w in base_lower_words)
            ):
                alts.add(base)
            entities.append({
                "entity_id": row.get("entity_id", ""),
                "entity_name": name,
                "entity_type": row.get("entity_type", ""),
                "sector": row.get("sector", ""),
                "alts": alts,
            })
    return entities


def step4_entity_prepass(
    md_text: str, entities: list[dict], out_csv: Path
) -> dict:
    patterns: list[tuple[dict, re.Pattern]] = []
    for ent in entities:
        for alt in ent["alts"]:
            if len(alt) < 4:
                continue
            pat = re.compile(
                r"(?<![A-Za-z0-9])" + re.escape(alt) + r"(?![A-Za-z0-9])",
                re.IGNORECASE,
            )
            patterns.append((ent, pat))

    hits_by_name: dict[str, dict] = {}
    for ent, pat in patterns:
        matches = list(pat.finditer(md_text))
        if not matches:
            continue
        key = ent["entity_name"].strip().lower()
        if key in hits_by_name:
            continue
        m = matches[0]
        start = max(0, m.start() - 60)
        end = min(len(md_text), m.end() + 60)
        ctx = md_text[start:end].replace("\n", " ").strip()
        hits_by_name[key] = {
            "entity_id": ent["entity_id"],
            "entity_name": ent["entity_name"],
            "entity_type": ent["entity_type"],
            "sector": ent["sector"],
            "hit_count": len(matches),
            "first_context": ctx,
        }

    rows = sorted(hits_by_name.values(), key=lambda r: -r["hit_count"])
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "entity_id", "entity_name", "entity_type", "sector",
                "hit_count", "first_context",
            ],
        )
        w.writeheader()
        for row in rows:
            w.writerow(row)
    return {
        "step": "4_entity_prepass",
        "candidates_found": len(rows),
        "output_csv": str(out_csv),
        "top_3": [(r["entity_name"], r["hit_count"]) for r in rows[:3]],
    }


# =============================================================================
# Step 5 — Observation pre-segmentation (v3: always-on; no bucket gating)
# =============================================================================
# Inherited from v2.2 step5_observation_prepass, bucket gate removed.

OBS_TRIGGERS = [
    (re.compile(r"\bbest[- ]in[- ]class\b", re.I), "best_in_class"),
    (re.compile(r"\b\d+(?:\.\d+)?\s*x\s+more\s+likely\b", re.I), "multiplier"),
    (re.compile(r"\bfigure\s+\d+\b", re.I), "figure_reference"),
    (re.compile(r"\bkey\s+finding(?:s)?\b", re.I), "key_finding"),
    (re.compile(r"\bfinding\s*\d+\b", re.I), "numbered_finding"),
    (re.compile(r"\b\d{1,3}\s*(?:%|percent)\s+of\b", re.I), "percentage_stat"),
    (re.compile(r"\$\d", re.I), "dollar_stat"),
    (re.compile(r"\baverage\s+(?:of\s+)?\d", re.I), "average_stat"),
]


def _split_sentences(text: str) -> list[tuple[int, str]]:
    out = []
    pos = 0
    for m in re.finditer(r"[.!?]\s+(?=[A-Z])|\n\s*[-*•]\s+|\n{2,}", text):
        sent = text[pos:m.start()+1].strip()
        if 20 <= len(sent) <= 600:
            out.append((pos, sent))
        pos = m.end()
    tail = text[pos:].strip()
    if 20 <= len(tail) <= 600:
        out.append((pos, tail))
    return out


def step5_observation_prepass(md_text: str, out_csv: Path) -> dict:
    """Always on in v3. No bucket gating."""
    sentences = _split_sentences(md_text)
    candidates: list[dict] = []
    for offset, sent in sentences:
        triggers = [label for pat, label in OBS_TRIGGERS if pat.search(sent)]
        if not triggers:
            continue
        candidates.append({
            "char_offset": offset,
            "trigger_labels": ";".join(triggers),
            "sentence": sent,
        })
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["char_offset", "trigger_labels", "sentence"]
        )
        w.writeheader()
        for row in candidates:
            w.writerow(row)
    return {
        "step": "5_observation_prepass",
        "candidates_found": len(candidates),
        "output_csv": str(out_csv),
    }


# =============================================================================
# Title extraction (verbatim from v2.2)
# =============================================================================

_TITLE_NOISE_PHRASES = {
    "aberdeen group", "aberdeen", "executive summary", "table of contents",
    "for immediate release", "press release", "copyright", "all rights reserved",
    "confidential", "for distribution",
}

_STRUCTURED_TITLE_RE = re.compile(
    r"(?:^|\n)\s*(?:#+\s*)?1\.\s*Title\s*[:\-]\s*(.+?)(?=\s*\d+\.\s*(?:Author|Publication|Date|Abstract)|\n\n|$)",
    re.IGNORECASE | re.DOTALL,
)


def _dedup_repeated_runs(text: str) -> str:
    if not text:
        return text
    words = text.split()
    out: list[str] = []
    i = 0
    while i < len(words):
        for size in (3, 2, 1):
            if i + 2 * size <= len(words) and words[i : i + size] == words[i + size : i + 2 * size]:
                out.extend(words[i : i + size])
                i += 2 * size
                break
        else:
            out.append(words[i])
            i += 1
    return " ".join(out)


def _clean_title(text: str, max_len: int = 120) -> str:
    text = re.sub(r"\s+", " ", text or "").strip(" :—–-#*")
    text = _dedup_repeated_runs(text)
    if len(text) > max_len:
        cut = text.rfind(" ", 0, max_len)
        text = text[: cut if cut > 40 else max_len].rstrip()
    return text


def extract_pdf_title(pdf_path: Path) -> tuple[str, str]:
    """Return (title, source) where source is 'metadata', 'structured', 'page1', or 'filename'."""
    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        return "", f"error:{e}"

    md = doc.metadata or {}
    candidate = (md.get("title") or "").strip()
    if (
        candidate
        and len(candidate) >= 8
        and not candidate.lower().endswith(".pdf")
        and "_" not in candidate
        and candidate.lower() not in _TITLE_NOISE_PHRASES
    ):
        doc.close()
        return _clean_title(candidate), "metadata"

    if len(doc) > 0:
        try:
            page1_raw = doc[0].get_text("text") or ""
            m = _STRUCTURED_TITLE_RE.search(page1_raw)
            if m:
                struct_title = _clean_title(m.group(1))
                if len(struct_title) >= 8:
                    doc.close()
                    return struct_title, "structured"
        except Exception:
            pass

    if len(doc) > 0:
        try:
            page = doc[0]
            text_dict = page.get_text("dict")
            all_lines: list[tuple[float, float, str]] = []
            for block in text_dict.get("blocks", []):
                if block.get("type") != 0:
                    continue
                for line in block.get("lines", []):
                    spans = line.get("spans", [])
                    if not spans:
                        continue
                    line_text = " ".join(s.get("text", "") for s in spans).strip()
                    if not line_text:
                        continue
                    max_size = max(s.get("size", 0) for s in spans)
                    y = line.get("bbox", [0, 0, 0, 0])[1]
                    if (
                        2 <= len(line_text) <= 200
                        and line_text.lower() not in _TITLE_NOISE_PHRASES
                        and not re.match(r"^\d+$", line_text)
                        and not re.match(r"^©", line_text)
                    ):
                        all_lines.append((max_size, y, line_text))

            if all_lines:
                max_font = max(a[0] for a in all_lines)
                top_lines = sorted(
                    [a for a in all_lines if a[0] >= max_font - 0.5],
                    key=lambda a: a[1],
                )
                joined = " ".join(t for _, _, t in top_lines)
                joined = _clean_title(joined)
                if len(joined) >= 15:
                    doc.close()
                    return joined, "page1"
                fallback = sorted(all_lines, key=lambda a: (-a[0], a[1]))[0][2]
                fallback = _clean_title(fallback)
                if len(fallback) >= 8:
                    doc.close()
                    return fallback, "page1"
        except Exception:
            pass

    doc.close()
    return _clean_title(pdf_path.stem.replace("_", " ").replace("-", " ")), "filename"


# =============================================================================
# Archive index (verbatim from v2.2 — walks archive-root for studies.csv)
# =============================================================================

@dataclass
class ArchiveStudy:
    study_id: str
    title: str
    directory: Path
    relative_path: str
    slug_stem: str = ""


_SLUG_HASH_RE = re.compile(r"-[0-9a-f]{6,8}$", re.IGNORECASE)


def _slug_stem_from_dir(dir_name: str) -> str:
    return _SLUG_HASH_RE.sub("", dir_name).lower()


def _filename_to_slug_stem(filename: str) -> str:
    stem = Path(filename).stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-")
    return stem


def build_archive_index(
    archive_root: Path, cache_path: Optional[Path] = None
) -> list[ArchiveStudy]:
    """Walk archive-root, find every data/studies.csv, extract title + study_id.

    Cache to cache_path (JSON) if provided; refresh when archive mtime > cache.
    """
    if cache_path and cache_path.exists():
        archive_mtime = max(
            (p.stat().st_mtime for p in archive_root.rglob("data/studies.csv")),
            default=0,
        )
        if cache_path.stat().st_mtime > archive_mtime:
            log.info(f"  Loading archive index from cache: {cache_path}")
            data = json.loads(cache_path.read_text(encoding="utf-8"))
            return [
                ArchiveStudy(
                    study_id=r["study_id"],
                    title=r["title"],
                    directory=Path(r["directory"]),
                    relative_path=r["relative_path"],
                    slug_stem=r.get("slug_stem")
                        or _slug_stem_from_dir(Path(r["directory"]).name),
                )
                for r in data
            ]

    log.info(f"  Building archive index by walking {archive_root}")
    studies: list[ArchiveStudy] = []
    for studies_csv in archive_root.rglob("data/studies.csv"):
        study_dir = studies_csv.parent.parent
        try:
            with studies_csv.open(encoding="utf-8") as f:
                rdr = csv.DictReader(f)
                for row in rdr:
                    sid = (
                        row.get("study_id")
                        or row.get("id")
                        or _slug_stem_from_dir(study_dir.name)
                    )
                    title = (row.get("title") or "").strip()
                    if not title:
                        continue
                    studies.append(ArchiveStudy(
                        study_id=sid,
                        title=title,
                        directory=study_dir,
                        relative_path=str(study_dir.relative_to(archive_root)),
                        slug_stem=_slug_stem_from_dir(study_dir.name),
                    ))
        except Exception as e:
            log.warning(f"  Failed to read {studies_csv}: {e}")

    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps(
                [
                    {
                        "study_id": s.study_id,
                        "title": s.title,
                        "directory": str(s.directory),
                        "relative_path": s.relative_path,
                        "slug_stem": s.slug_stem,
                    }
                    for s in studies
                ],
                indent=2,
            ),
            encoding="utf-8",
        )

    log.info(f"  Archive index built: {len(studies)} studies")
    return studies


# =============================================================================
# Fuzzy matching (verbatim from v2.2)
# =============================================================================

def _normalize_for_match(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _token_set_ratio(a: str, b: str) -> float:
    ta = set(_normalize_for_match(a).split())
    tb = set(_normalize_for_match(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def _levenshtein_ratio(a: str, b: str) -> float:
    return SequenceMatcher(
        None, _normalize_for_match(a), _normalize_for_match(b)
    ).ratio()


def match_filename_to_slug(
    pdf_filename: str, studies: list[ArchiveStudy]
) -> Optional[dict]:
    """Match PDF filename directly to an archive study by slug stem.

    Returns None on no slug match. Same dict shape as match_title_to_archive
    entries; 'match_via' is 'slug_exact' (combined_score=1.0) or 'slug_tokens'
    (combined_score 0.86-0.95).
    """
    needle = _filename_to_slug_stem(pdf_filename)
    if not needle or len(needle) < 6:
        return None

    for s in studies:
        if s.slug_stem and s.slug_stem == needle:
            return {
                "study_id": s.study_id,
                "title": s.title,
                "relative_path": s.relative_path,
                "directory": str(s.directory),
                "lev_ratio": 1.0,
                "token_ratio": 1.0,
                "combined_score": 1.0,
                "match_via": "slug_exact",
                "matched_stem": s.slug_stem,
            }

    needle_tokens = [t for t in needle.split("-") if t]
    needle_set = set(needle_tokens)
    if len(needle_set) < 2:
        return None

    best: Optional[dict] = None
    for s in studies:
        stem = s.slug_stem
        if not stem:
            continue
        stem_tokens = [t for t in stem.split("-") if t]
        stem_set = set(stem_tokens)
        if len(stem_set) < 2:
            continue
        if needle_tokens[0] != stem_tokens[0]:
            continue
        inter = needle_set & stem_set
        if len(inter) < 2:
            continue
        short_set, long_set = (
            (needle_set, stem_set) if len(needle_set) <= len(stem_set)
            else (stem_set, needle_set)
        )
        short_cov = len(inter) / len(short_set)
        long_cov = len(inter) / len(long_set)
        if short_cov >= 0.80 and long_cov >= 0.40:
            score = 0.80 + 0.15 * long_cov
            if best is None or score > best["combined_score"]:
                best = {
                    "study_id": s.study_id,
                    "title": s.title,
                    "relative_path": s.relative_path,
                    "directory": str(s.directory),
                    "lev_ratio": round(score, 4),
                    "token_ratio": round(short_cov, 4),
                    "combined_score": round(score, 4),
                    "match_via": "slug_tokens",
                    "matched_stem": stem,
                }
    return best


def match_title_to_archive(
    title: str, studies: list[ArchiveStudy], top_k: int = 3,
    filename_stem: str = "",
) -> list[dict]:
    """Return top_k candidate matches sorted by combined score."""
    needle_first_token = ""
    if filename_stem:
        ftoks = [t for t in filename_stem.split("-") if t]
        if ftoks:
            needle_first_token = ftoks[0]

    scored: list[dict] = []
    for s in studies:
        lev = _levenshtein_ratio(title, s.title)
        tok = _token_set_ratio(title, s.title)
        base = 0.6 * lev + 0.4 * tok
        bonus = 0.0
        if needle_first_token and s.slug_stem:
            slug_toks = [t for t in s.slug_stem.split("-") if t]
            if slug_toks and slug_toks[0] == needle_first_token and base >= 0.40:
                bonus = 0.10
        combined = min(base + bonus, 1.0)
        scored.append({
            "study_id": s.study_id,
            "title": s.title,
            "relative_path": s.relative_path,
            "directory": str(s.directory),
            "lev_ratio": round(lev, 4),
            "token_ratio": round(tok, 4),
            "combined_score": round(combined, 4),
            "anchor_bonus": round(bonus, 2),
        })
    scored.sort(key=lambda r: -r["combined_score"])
    return scored[:top_k]


# Match-confidence thresholds (inherited from v2.2)
CONFIDENCE_STRONG = 0.75
CONFIDENCE_WEAK = 0.55


# =============================================================================
# Restricted-sources index (v3-new: SHA-256 hard-dedupe + slug lookup)
# =============================================================================

def build_restricted_sha_index(restricted_root: Path) -> dict[str, Path]:
    """Map sha256 -> existing PDF path in kastner-restricted-sources.

    Used for the fast-path 'exact SHA-256 already in restricted repo' check —
    guaranteed DUPLICATE disposition with zero ambiguity.
    """
    sha_to_path: dict[str, Path] = {}
    if not restricted_root.exists():
        log.warning(f"  Restricted-sources root does not exist: {restricted_root}")
        return sha_to_path
    for pdf in restricted_root.glob("*.pdf"):
        try:
            sha_to_path[sha256_of_file(pdf)] = pdf
        except Exception as e:
            log.warning(f"  Could not hash {pdf.name}: {e}")
    log.info(f"  Restricted-sources SHA index: {len(sha_to_path)} PDFs")
    return sha_to_path


def get_restricted_pdf_stats(pdf_path: Path) -> dict:
    """Return basic stats for a PDF already in restricted-sources, for the
    BETTER-version comparison (page count, file size, image count, text density).
    """
    if not pdf_path.exists():
        return {"exists": False}
    try:
        doc = fitz.open(str(pdf_path))
        page_count = len(doc)
        image_count = 0
        text_chars = 0
        for pno in range(page_count):
            image_count += len(doc[pno].get_images(full=False))
            text_chars += len(doc[pno].get_text() or "")
        doc.close()
        return {
            "exists": True,
            "page_count": page_count,
            "image_count": image_count,
            "size_bytes": pdf_path.stat().st_size,
            "text_density": text_density_proxy(text_chars, page_count),
        }
    except Exception as e:
        log.warning(f"  get_restricted_pdf_stats failed for {pdf_path.name}: {e}")
        return {"exists": True, "error": str(e)}


# =============================================================================
# Disposition router (v3-new)
# =============================================================================

@dataclass
class PdfSignals:
    """All signals computed for one queued PDF — fed to the disposition router."""
    queue_path: Path
    filename: str
    sha256: str
    size_bytes: int
    page_count: int
    image_count: int
    title: str
    title_source: str
    md_chars: int
    text_density: float
    # Match results (filled by router):
    sha_match_in_restricted: Optional[str] = None  # path string if hit
    slug_match: Optional[dict] = None
    title_matches: list[dict] = field(default_factory=list)
    best_match_study_slug: Optional[str] = None  # the slug_stem we'd write to


def is_incoming_better(incoming: PdfSignals, archived: dict) -> tuple[bool, str]:
    """Apply the BETTER heuristic: incoming wins if any of:
      - more pages (>= +1)
      - more embedded images (>= +1)
      - notably higher text density (>= +30%)

    Returns (is_better, reason_string).
    """
    if not archived.get("exists"):
        return True, "archived PDF missing from restricted repo"
    reasons = []
    if incoming.page_count > archived.get("page_count", 0):
        reasons.append(
            f"pages {archived.get('page_count', 0)}->{incoming.page_count}"
        )
    if incoming.image_count > archived.get("image_count", 0):
        reasons.append(
            f"images {archived.get('image_count', 0)}->{incoming.image_count}"
        )
    arch_dens = archived.get("text_density", 0.0)
    if arch_dens > 0 and incoming.text_density >= arch_dens * 1.30:
        reasons.append(f"text_density {arch_dens}->{incoming.text_density}")
    elif arch_dens == 0 and incoming.text_density >= 200:
        reasons.append(f"text_density 0->{incoming.text_density} (new text layer)")
    return (len(reasons) > 0, "; ".join(reasons) if reasons else "no improvement")


def route_disposition(
    sig: PdfSignals,
    sha_index: dict[str, Path],
    archive_studies: list[ArchiveStudy],
    restricted_root: Path,
) -> dict:
    """Return a row describing the proposed disposition for one PDF.

    Disposition is one of: NEW, BETTER, DUPLICATE, AMBIGUOUS.
    - NEW       : no SHA hit, no archive match -> auto-routable
    - BETTER    : archive match + heuristic says incoming is stronger
                  -> needs Pete's accept (manual review row)
    - DUPLICATE : SHA hit, OR archive match + incoming not stronger
                  -> auto-routable (discard incoming)
    - AMBIGUOUS : title-fuzzy match in the CONFIDENCE_WEAK..STRONG band
                  -> needs Pete's accept (manual review row)
    """
    # Fast path: exact SHA-256 already in restricted repo
    if sig.sha256 in sha_index:
        sig.sha_match_in_restricted = str(sha_index[sig.sha256])
        return {
            "disposition": "DUPLICATE",
            "reason": f"sha256 already in restricted repo at {sha_index[sig.sha256].name}",
            "needs_review": False,
            "target_path": "",
        }

    # Slug match (high-confidence; combined_score 0.86-1.00)
    sig.slug_match = match_filename_to_slug(sig.filename, archive_studies)

    # Title fuzzy match (top 3 candidates)
    sig.title_matches = match_title_to_archive(
        sig.title, archive_studies, top_k=3,
        filename_stem=_filename_to_slug_stem(sig.filename),
    )

    # Pick best match across slug + title
    best_match: Optional[dict] = None
    if sig.slug_match:
        best_match = sig.slug_match
    if sig.title_matches:
        tm = sig.title_matches[0]
        if best_match is None or tm["combined_score"] > best_match["combined_score"]:
            best_match = tm

    if best_match is None or best_match["combined_score"] < CONFIDENCE_WEAK:
        # No archive match -> NEW
        sig.best_match_study_slug = None
        target_slug = study_slug(sig.queue_path)
        return {
            "disposition": "NEW",
            "reason": "no archive match",
            "needs_review": False,
            "target_path": str(restricted_root / f"{target_slug}.pdf"),
            "match_score": best_match["combined_score"] if best_match else 0.0,
            "match_via": best_match.get("match_via", "title") if best_match else "",
        }

    # Match found — derive the canonical slug to write to
    match_dir = Path(best_match.get("directory", ""))
    match_slug = _slug_stem_from_dir(match_dir.name) if match_dir.name else best_match["study_id"]
    sig.best_match_study_slug = match_slug
    target_pdf = restricted_root / f"{match_slug}.pdf"

    # Strong match -> compare with archived PDF for BETTER heuristic
    if best_match["combined_score"] >= CONFIDENCE_STRONG:
        archived_stats = get_restricted_pdf_stats(target_pdf)
        better, reason = is_incoming_better(sig, archived_stats)
        if better:
            return {
                "disposition": "BETTER",
                "reason": reason,
                "needs_review": True,
                "target_path": str(target_pdf),
                "match_score": best_match["combined_score"],
                "match_via": best_match.get("match_via", "title"),
                "archived_pages": archived_stats.get("page_count", 0),
                "archived_images": archived_stats.get("image_count", 0),
                "archived_density": archived_stats.get("text_density", 0.0),
            }
        else:
            return {
                "disposition": "DUPLICATE",
                "reason": f"archive match (score {best_match['combined_score']}); {reason}",
                "needs_review": False,
                "target_path": "",
                "match_score": best_match["combined_score"],
                "match_via": best_match.get("match_via", "title"),
            }

    # Weak-to-medium match -> AMBIGUOUS, needs Pete
    archived_stats = get_restricted_pdf_stats(target_pdf)
    return {
        "disposition": "AMBIGUOUS",
        "reason": f"archive match in weak band ({best_match['combined_score']}); needs review",
        "needs_review": True,
        "target_path": str(target_pdf),
        "match_score": best_match["combined_score"],
        "match_via": best_match.get("match_via", "title"),
        "archived_pages": archived_stats.get("page_count", 0),
        "archived_images": archived_stats.get("image_count", 0),
        "archived_density": archived_stats.get("text_density", 0.0),
    }


# =============================================================================
# Review CSV (v3-new: the manual accept/reject roundtrip)
# =============================================================================

REVIEW_CSV_COLUMNS = [
    "queue_filename",
    "sha256_short",
    "page_count",
    "image_count",
    "text_density",
    "size_bytes",
    "extracted_title",
    "title_source",
    "proposed_disposition",   # NEW / BETTER / DUPLICATE / AMBIGUOUS
    "pete_decision",          # blank by default; Pete fills "ACCEPT" / "REJECT" / "" (no-op)
    "match_score",
    "match_via",
    "matched_study_slug",
    "matched_title",
    "archived_pages",
    "archived_images",
    "archived_density",
    "reason",
    "target_path",
    "needs_review",
    "queue_path",             # absolute path on Mac (for the apply step)
    "sha256_full",
]


def write_review_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=REVIEW_CSV_COLUMNS, quoting=csv.QUOTE_ALL
        )
        w.writeheader()
        for r in rows:
            w.writerow({col: r.get(col, "") for col in REVIEW_CSV_COLUMNS})


def read_review_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


# =============================================================================
# Queue driver (v3-new: Pass 1 = discover; Pass 2 = apply)
# =============================================================================

def discover_queue(
    queue_dir: Path,
    archive_root: Path,
    restricted_root: Path,
    entities_csv: Optional[Path],
    review_out: Path,
    work_root: Path,
) -> dict:
    """Pass 1: walk queue, compute signals, propose dispositions, emit review CSV."""
    pdfs = sorted(p for p in queue_dir.glob("*.pdf") if p.is_file())
    log.info(f"Found {len(pdfs)} PDFs in queue: {queue_dir}")
    if not pdfs:
        return {"pdfs_seen": 0, "review_csv": str(review_out)}

    log.info("Building indices...")
    sha_index = build_restricted_sha_index(restricted_root)
    archive_studies = build_archive_index(
        archive_root, cache_path=work_root / "_archive_index_cache.json"
    )
    entities: list[dict] = []
    if entities_csv and entities_csv.exists():
        entities = load_known_entities(entities_csv)
        log.info(f"Loaded {len(entities)} known entities for entity pre-pass")

    work_root.mkdir(parents=True, exist_ok=True)
    review_rows: list[dict] = []
    for i, pdf in enumerate(pdfs, 1):
        log.info(f"[{i}/{len(pdfs)}] {pdf.name}")
        # Per-PDF working directory
        slug_for_work = study_slug(pdf)
        pdf_work = work_root / slug_for_work
        pdf_work.mkdir(parents=True, exist_ok=True)
        figures_dir = pdf_work / "figures"

        # Open PDF basics
        try:
            doc = fitz.open(str(pdf))
            page_count = len(doc)
            doc.close()
        except Exception as e:
            log.error(f"  Failed to open {pdf.name}: {e}")
            continue

        sha = sha256_of_file(pdf)
        size_bytes = pdf.stat().st_size
        image_count = count_embedded_images(pdf)

        # Step 1: markdown
        out_md = pdf_work / "extracted.md"
        step1 = step1_extract_markdown(pdf, out_md)
        md_text = out_md.read_text(encoding="utf-8")
        density = text_density_proxy(step1["md_chars"], page_count)

        # Title
        title, title_source = extract_pdf_title(pdf)

        # Figure render + entity + observation prepass (informational; output in working/)
        step3_extract_figures(pdf, figures_dir)
        if entities:
            step4_entity_prepass(md_text, entities, pdf_work / "entity_candidates.csv")
        step5_observation_prepass(md_text, pdf_work / "observation_candidates.csv")

        # Build signals + route
        sig = PdfSignals(
            queue_path=pdf,
            filename=pdf.name,
            sha256=sha,
            size_bytes=size_bytes,
            page_count=page_count,
            image_count=image_count,
            title=title,
            title_source=title_source,
            md_chars=step1["md_chars"],
            text_density=density,
        )
        disp = route_disposition(sig, sha_index, archive_studies, restricted_root)

        top_match = sig.title_matches[0] if sig.title_matches else {}
        review_row = {
            "queue_filename": pdf.name,
            "sha256_short": sha[:12],
            "sha256_full": sha,
            "page_count": page_count,
            "image_count": image_count,
            "text_density": density,
            "size_bytes": size_bytes,
            "extracted_title": title,
            "title_source": title_source,
            "proposed_disposition": disp["disposition"],
            "pete_decision": "",
            "match_score": disp.get("match_score", 0.0),
            "match_via": disp.get("match_via", ""),
            "matched_study_slug": sig.best_match_study_slug or "",
            "matched_title": top_match.get("title", ""),
            "archived_pages": disp.get("archived_pages", ""),
            "archived_images": disp.get("archived_images", ""),
            "archived_density": disp.get("archived_density", ""),
            "reason": disp.get("reason", ""),
            "target_path": disp.get("target_path", ""),
            "needs_review": "yes" if disp.get("needs_review") else "no",
            "queue_path": str(pdf),
        }
        review_rows.append(review_row)
        log.info(
            f"  -> {disp['disposition']} "
            f"(score={disp.get('match_score', 0.0)}; {disp.get('reason', '')[:80]})"
        )

    write_review_csv(review_rows, review_out)
    log.info(f"\nReview CSV written: {review_out}")
    log.info(f"Pete: review and mark 'pete_decision' = ACCEPT or REJECT on")
    log.info(f"      BETTER and AMBIGUOUS rows, then re-run with:")
    log.info(f"      python3 prepare_for_ingest_v3.py --apply-review {review_out}")

    # Summary
    by_disp: dict[str, int] = {}
    for r in review_rows:
        by_disp[r["proposed_disposition"]] = by_disp.get(r["proposed_disposition"], 0) + 1
    log.info(f"Summary: {by_disp}")
    return {
        "pdfs_seen": len(pdfs),
        "review_csv": str(review_out),
        "summary": by_disp,
    }


def apply_review(
    review_csv: Path,
    restricted_root: Path,
    commit: bool,
) -> dict:
    """Pass 2: execute the dispositions in the review CSV.

    Honors pete_decision overrides on BETTER and AMBIGUOUS rows:
      - ACCEPT: BETTER -> replace target; AMBIGUOUS -> treat as BETTER and replace
      - REJECT: BETTER -> demote to DUPLICATE (no action); AMBIGUOUS -> demote to NEW
      - blank on BETTER/AMBIGUOUS -> default to REJECT (safe path)
    """
    rows = read_review_csv(review_csv)
    log.info(f"Applying {len(rows)} review rows from {review_csv}")
    if not commit:
        log.warning("DRY-RUN — no PDFs will be moved or replaced. Pass --commit to apply.")

    actions: list[dict] = []
    for r in rows:
        disposition = r["proposed_disposition"]
        decision = (r.get("pete_decision") or "").strip().upper()
        queue_path = Path(r["queue_path"])
        target_path = Path(r["target_path"]) if r["target_path"] else None
        action_taken = ""

        if disposition == "DUPLICATE":
            action_taken = "DISCARD"
        elif disposition == "NEW":
            if not target_path:
                action_taken = "ERROR: no target_path for NEW"
            else:
                action_taken = f"COPY -> {target_path}"
                if commit:
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(queue_path, target_path)
        elif disposition in {"BETTER", "AMBIGUOUS"}:
            if decision == "ACCEPT":
                if not target_path:
                    action_taken = "ERROR: no target_path"
                else:
                    action_taken = f"REPLACE -> {target_path}"
                    if commit:
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(queue_path, target_path)
            elif decision == "REJECT":
                action_taken = "DISCARD (pete REJECT)"
            else:
                action_taken = "DISCARD (no decision; default reject)"
        else:
            action_taken = f"UNKNOWN disposition {disposition}"

        log.info(f"  {queue_path.name}: {action_taken}")
        actions.append({
            "queue_filename": queue_path.name,
            "disposition": disposition,
            "decision": decision,
            "action_taken": action_taken,
            "target_path": str(target_path) if target_path else "",
        })

    return {"rows_processed": len(rows), "actions": actions, "committed": commit}


# =============================================================================
# Main
# =============================================================================

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Single-queue PDF ingest router for the Kastner Aberdeen Archive (v3).",
    )
    sub = parser.add_subparsers(dest="cmd", required=False)

    # No subcommand: default to 'discover' for backwards-friendly invocation
    parser.add_argument(
        "--queue", default="~/Desktop/Archive/_ingest_queue",
        help="Input queue directory (default: ~/Desktop/Archive/_ingest_queue)",
    )
    parser.add_argument(
        "--archive-root", default="~/Desktop/Archive/aberdeen-group-archive",
        help="Public archive clone root (text only)",
    )
    parser.add_argument(
        "--restricted-root", default="~/Desktop/Archive/kastner-restricted-sources",
        help="Private PDF vault (flat layout: <slug>.pdf per study)",
    )
    parser.add_argument(
        "--entities",
        default="~/Desktop/Archive/aberdeen-group-archive/_known_entities.csv",
        help="Known-entities CSV for entity pre-pass",
    )
    parser.add_argument(
        "--work-root", default="~/Desktop/Archive/_ingest_queue/_work",
        help="Per-PDF working directory (extracted MD, figures, candidates)",
    )
    parser.add_argument(
        "--review-out", default=None,
        help="Review CSV output path (default: queue/_review_<UTC-stamp>.csv)",
    )
    parser.add_argument(
        "--apply-review", default=None,
        help="Apply a previously-emitted review CSV (skips Pass 1)",
    )
    parser.add_argument(
        "--commit", action="store_true",
        help="Required for apply-review to actually move files (default: dry-run)",
    )
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args(argv)
    setup_logging(args.verbose)

    queue_dir = Path(args.queue).expanduser().resolve()
    archive_root = Path(args.archive_root).expanduser().resolve()
    restricted_root = Path(args.restricted_root).expanduser().resolve()
    work_root = Path(args.work_root).expanduser().resolve()
    entities_csv = Path(args.entities).expanduser().resolve() if args.entities else None

    if args.apply_review:
        review_csv = Path(args.apply_review).expanduser().resolve()
        if not review_csv.exists():
            log.error(f"Review CSV not found: {review_csv}")
            return 2
        result = apply_review(review_csv, restricted_root, commit=args.commit)
        log.info(f"Done. {result['rows_processed']} rows processed, "
                 f"committed={result['committed']}")
        return 0

    if not queue_dir.exists():
        log.error(f"Queue directory not found: {queue_dir}")
        return 2
    if not archive_root.exists():
        log.error(f"Archive root not found: {archive_root}")
        return 2
    if not restricted_root.exists():
        log.error(f"Restricted-sources root not found: {restricted_root}")
        return 2

    review_out = (
        Path(args.review_out).expanduser().resolve()
        if args.review_out
        else queue_dir / f"_review_{utc_stamp()}.csv"
    )
    discover_queue(
        queue_dir=queue_dir,
        archive_root=archive_root,
        restricted_root=restricted_root,
        entities_csv=entities_csv,
        review_out=review_out,
        work_root=work_root,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
