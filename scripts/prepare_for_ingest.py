#!/usr/bin/env python3
"""
prepare_for_ingest.py — Local PDF pre-processing for the Kastner Aberdeen Archive
=================================================================================

Runs locally on the Mac. Performs every deterministic preparation step on PDFs
*before* the archival-ingest v20 skill ever sees them. Zero AI credits.

Two modes
---------

  --mode new       For PDFs Pete has already pre-sorted into a bucket (A/B/C/D/E).
                   Trusts the --bucket flag; runs classifier only as a sanity
                   check; flags outliers; quarantines genuine duds.

  --mode existing  For old PDFs whose studies already exist in the archive.
                   Extracts each PDF's title, fuzzy-matches against the archive
                   index, attaches PDF + figures + v20-suffixed candidates to
                   the matched study directory. Never deletes text dumps —
                   retirement is a separate one-time batch.

Six per-PDF preparation steps (shared between modes):
  1. Markdown extraction (pymupdf4llm)
  2. Bucket classifier (informational only in --mode new; written suffixed in --mode existing)
  3. Figure extraction with SHA-1 dedup (label-triggered)
  4. Entity pre-pass against _known_entities.csv
  5. Observation pre-segmentation (regex-based)
  6. Manifest + provenance

Suggested layout on the Mac:
    ~/Desktop/Archive/
        incoming-bucket-A/             ← Mode 1 input
        incoming-bucket-B/
        incoming-bucket-C/
        incoming-bucket-D/
        incoming-bucket-E/
        incoming-existing/             ← Mode 2 input
        prepared/                      ← Mode 1 output (new study dirs)
        aberdeen-group-archive/        ← clone of public archive (Mode 2 target)
        archive_masters/
            _known_entities.csv

Dependencies (all local, no AI):
    pip install pymupdf pymupdf4llm pandas

Author: drafted for Pete Kastner, 23 May 2026.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable, Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("FATAL: PyMuPDF not installed. Run: pip install pymupdf")
try:
    import pymupdf4llm
except ImportError:
    sys.exit("FATAL: pymupdf4llm not installed. Run: pip install pymupdf4llm")
try:
    import pandas as pd  # noqa: F401  (kept for ad-hoc downstream use)
except ImportError:
    sys.exit("FATAL: pandas not installed. Run: pip install pandas")


# =============================================================================
# Logging
# =============================================================================

log = logging.getLogger("prepare_for_ingest")


def setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s  %(levelname)-7s  %(message)s",
        datefmt="%H:%M:%S",
    )


# =============================================================================
# Slug + hashing helpers
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


# =============================================================================
# Step 1 — PDF -> Markdown
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
# Step 2 — Bucket classifier (sanity check / outlier detection)
# =============================================================================

BUCKET_E_PATTERNS = [
    r"\bresearch\s+calendar\b",
    r"\bresearch\s+agenda\b",
    r"\bproposed\s+stud(?:y|ies)\b",
    r"\bupcoming\s+research\b",
    r"\bfor\s+immediate\s+sponsorship\b",
]
BUCKET_A_PATTERNS = [
    r"\bbest[- ]in[- ]class\b",
    r"\bbenchmark\s+report\b",
    r"\bpressures,?\s+actions,?\s+capabilities\b",
    r"\bcompetitive\s+framework\b",
]
BUCKET_C_PATTERNS = [
    r"\bfor\s+immediate\s+release\b",
    r"\bpress\s+release\b",
    r"\bcontact:?\s+\S+@\S+",
    r"\bhot\s+topic\b",
]
BUCKET_B_PATTERNS = [
    r"\bexecutive\s+summary\b",
    r"\bsnap[- ]?shot\b",
    r"\bsector\s+insight\b",
]
BUCKET_D_PATTERNS = [
    r"\btable\s+of\s+contents\b",
    r"\bindex\s+of\s+(?:reports|studies|research)\b",
    r"\bpublication\s+list\b",
]


def _score(text: str, patterns: list[str]) -> int:
    return sum(1 for p in patterns if re.search(p, text, flags=re.IGNORECASE))


def classify_bucket(pdf_name: str, md_text: str, page_count: int) -> tuple[str, dict]:
    """Return (predicted_bucket, signals_dict)."""
    head = md_text[:4000]
    fname = pdf_name.lower()
    signals = {
        "page_count": page_count,
        "filename": fname,
        "scores": {
            "A_benchmark": _score(head, BUCKET_A_PATTERNS),
            "B_exec_summary": _score(head, BUCKET_B_PATTERNS),
            "C_press_release": _score(head, BUCKET_C_PATTERNS),
            "D_toc_index": _score(head, BUCKET_D_PATTERNS),
            "E_research_agenda": _score(head, BUCKET_E_PATTERNS),
        },
        "filename_hints": [],
    }
    if re.search(r"calendar|agenda|proposed", fname):
        signals["filename_hints"].append("E")
        signals["scores"]["E_research_agenda"] += 2
    if re.search(r"\bpr\b|press|release|hot[-_]?topic", fname):
        signals["filename_hints"].append("C")
        signals["scores"]["C_press_release"] += 1
    if re.search(r"snapshot|exec|summary", fname):
        signals["filename_hints"].append("B")
        signals["scores"]["B_exec_summary"] += 1
    if re.search(r"benchmark|best[-_]?in[-_]?class", fname):
        signals["filename_hints"].append("A")
        signals["scores"]["A_benchmark"] += 1

    scores = signals["scores"]
    if scores["E_research_agenda"] >= 1 and page_count >= 15:
        predicted = "E"
    elif scores["D_toc_index"] >= 1 and page_count <= 10:
        predicted = "D"
    elif scores["C_press_release"] >= 2 or (
        scores["C_press_release"] >= 1 and page_count <= 3
    ):
        predicted = "C"
    elif scores["A_benchmark"] >= 2 or (
        scores["A_benchmark"] >= 1 and page_count >= 15
    ):
        predicted = "A"
    elif page_count <= 6:
        predicted = "B"
    elif page_count >= 20:
        predicted = "A"
    else:
        predicted = "B"

    signals["predicted_bucket"] = predicted
    signals["decision_reason"] = (
        f"page_count={page_count}, top_score={max(scores.values())}, "
        f"hints={signals['filename_hints']}"
    )
    # "Cannot decide" = top score is 0 AND no filename hints.
    signals["is_ambiguous"] = (
        max(scores.values()) == 0 and not signals["filename_hints"]
    )
    return predicted, signals


# =============================================================================
# Step 3 — Figure extraction (page-render when "Figure N:" label present)
# =============================================================================

FIGURE_LABEL_RE = re.compile(
    r"\b(?:figure|fig\.?|chart|exhibit|table)\s*(\d+)\b[:.\s]",
    re.IGNORECASE,
)


def step3_extract_figures(
    pdf_path: Path, figures_dir: Path, bucket: str
) -> dict:
    """
    Extract page-renders for pages bearing figure labels.
    Runs only for buckets A and E (benchmark + research agenda).
    """
    if bucket not in {"A", "E"}:
        return {
            "step": "3_extract_figures",
            "skipped": True,
            "reason": f"bucket {bucket} does not require figures",
            "figures": [],
        }

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
        "skipped": False,
        "bucket": bucket,
        "pages_with_labels": len(pages_with_labels),
        "figures_extracted": len(figure_index),
        "figures_dir": str(figures_dir),
        "figures": figure_index,
    }


# =============================================================================
# Step 4 — Entity pre-pass
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
# Step 5 — Observation pre-segmentation
# =============================================================================

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


def step5_observation_prepass(
    md_text: str, bucket: str, out_csv: Path
) -> dict:
    if bucket not in {"A", "E"}:
        return {
            "step": "5_observation_prepass",
            "skipped": True,
            "reason": f"bucket {bucket} does not need observation pre-pass",
            "candidates_found": 0,
        }
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
        "skipped": False,
        "bucket": bucket,
        "candidates_found": len(candidates),
        "output_csv": str(out_csv),
    }


# =============================================================================
# Title extraction (Mode 2)
# =============================================================================

_TITLE_NOISE_PHRASES = {
    "aberdeen group", "aberdeen", "executive summary", "table of contents",
    "for immediate release", "press release", "copyright", "all rights reserved",
    "confidential", "for distribution",
}


# Detects an annotation block like:
#   #### 1. Title: Foo Bar
#   2. Author(s) & Affiliation(s): ...
#   3. Publication Date: ...
# We grab only field 1, regardless of leading hashes/whitespace.
_STRUCTURED_TITLE_RE = re.compile(
    r"(?:^|\n)\s*(?:#+\s*)?1\.\s*Title\s*[:\-]\s*(.+?)(?=\s*\d+\.\s*(?:Author|Publication|Date|Abstract)|\n\n|$)",
    re.IGNORECASE | re.DOTALL,
)


def _dedup_repeated_runs(text: str) -> str:
    """Collapse 'Foo Foo Bar Bar' -> 'Foo Bar' (font-join artefact)."""
    if not text:
        return text
    words = text.split()
    out: list[str] = []
    i = 0
    while i < len(words):
        # try doubled bigram first, then doubled unigram
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
    """Normalise whitespace, dedup font-join repeats, cap length."""
    text = re.sub(r"\s+", " ", text or "").strip(" :—–-#*")
    text = _dedup_repeated_runs(text)
    if len(text) > max_len:
        # cap at last whitespace before max_len, never break a word
        cut = text.rfind(" ", 0, max_len)
        text = text[: cut if cut > 40 else max_len].rstrip()
    return text


def extract_pdf_title(pdf_path: Path) -> tuple[str, str]:
    """
    Return (title, source) where source is 'metadata', 'structured', 'page1', or 'filename'.
    """
    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        return "", f"error:{e}"

    # 1) metadata
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

    # 1b) structured-metadata annotation block on page 1
    #     (some PDFs were re-annotated with a `#### 1. Title: ...` header).
    #     Check this BEFORE the dominant-font heuristic so the heuristic
    #     doesn't slurp the entire numbered block into a single 600-char title.
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

    # 2) page 1 text heuristic — collect ALL lines, then join consecutive
    #    lines that share the dominant (largest) font size to recover wrapped
    #    titles like "Can Parallel-Scalable" + "RDBMSs Break the Downsizing Logjam?"
    if len(doc) > 0:
        try:
            page = doc[0]
            text_dict = page.get_text("dict")
            all_lines: list[tuple[float, float, str]] = []  # (max_font, y, text)
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
                        and not re.match(r"^\d+$", line_text)  # page number
                        and not re.match(r"^©", line_text)
                    ):
                        all_lines.append((max_size, y, line_text))

            if all_lines:
                # Find dominant font size (largest). Then concatenate all lines at
                # that size that appear in the top half of the page, in y-order.
                max_font = max(a[0] for a in all_lines)
                # Allow small font-rounding tolerance (0.5pt) for joined runs
                top_lines = sorted(
                    [a for a in all_lines if a[0] >= max_font - 0.5],
                    key=lambda a: a[1],  # by y position
                )
                joined = " ".join(t for _, _, t in top_lines)
                joined = _clean_title(joined)
                # Quality gate: must be at least 15 chars after join
                if len(joined) >= 15:
                    doc.close()
                    return joined, "page1"
                # Fallback to single largest-font line if join was too short
                fallback = sorted(
                    all_lines, key=lambda a: (-a[0], a[1])
                )[0][2]
                fallback = _clean_title(fallback)
                if len(fallback) >= 8:
                    doc.close()
                    return fallback, "page1"
        except Exception:
            pass

    doc.close()
    # 3) fall back to filename stem
    return _clean_title(pdf_path.stem.replace("_", " ").replace("-", " ")), "filename"


# =============================================================================
# Archive index (Mode 2) — walk archive-root, build {title -> study_dir}
# =============================================================================

@dataclass
class ArchiveStudy:
    study_id: str
    title: str
    directory: Path
    relative_path: str  # display-friendly relative to archive root
    slug_stem: str = ""  # normalized directory name with trailing -hash stripped


_SLUG_HASH_RE = re.compile(r"-[0-9a-f]{6,8}$", re.IGNORECASE)


def _slug_stem_from_dir(dir_name: str) -> str:
    """Strip the trailing -xxxxxx hash from a study directory name.

    Example: '1988-encore-oltp-market-tps-needs-deee45' -> '1988-encore-oltp-market-tps-needs'
    """
    return _SLUG_HASH_RE.sub("", dir_name).lower()


def _filename_to_slug_stem(filename: str) -> str:
    """Normalize a PDF filename to a slug stem comparable to _slug_stem_from_dir.

    'Bull RDBMS 1990 and 2024 Metadata.pdf' -> 'bull-rdbms-1990-and-2024-metadata'
    '1991 Apple C-S.pdf'                    -> '1991-apple-c-s'
    """
    stem = Path(filename).stem.lower()
    stem = re.sub(r"[^a-z0-9]+", "-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-")
    return stem


def build_archive_index(
    archive_root: Path, cache_path: Optional[Path] = None
) -> list[ArchiveStudy]:
    """
    Walk archive-root, find every data/studies.csv, extract title + study_id.
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
                        or row.get("slug")
                        or study_dir.name
                    ).strip()
                    title = (
                        row.get("title")
                        or row.get("study_title")
                        or row.get("name")
                        or ""
                    ).strip()
                    if not title:
                        # fall back to directory name
                        title = study_dir.name.replace("-", " ")
                    studies.append(ArchiveStudy(
                        study_id=sid,
                        title=title,
                        directory=study_dir,
                        relative_path=str(study_dir.relative_to(archive_root)),
                        slug_stem=_slug_stem_from_dir(study_dir.name),
                    ))
                    break  # first row only — studies.csv is one row per study
        except Exception as e:
            log.warning(f"  Could not parse {studies_csv}: {e}")

    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps([
                {
                    "study_id": s.study_id,
                    "title": s.title,
                    "directory": str(s.directory),
                    "relative_path": s.relative_path,
                    "slug_stem": s.slug_stem,
                }
                for s in studies
            ], indent=2),
            encoding="utf-8",
        )
    log.info(f"  Archive index has {len(studies)} studies")
    return studies


# =============================================================================
# Fuzzy matching (Mode 2)
# =============================================================================

def _normalize_for_match(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _token_set_ratio(a: str, b: str) -> float:
    """Symmetric token-set overlap (1.0 = identical bag of words)."""
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
    """Try to match a PDF filename directly to an archive study by slug stem.

    Many old (1988-1992) PDFs that Pete renamed match the archive slug exactly
    once both sides are normalized (lowercase, non-alphanumeric -> '-'). The
    archive directory's trailing -xxxxxx hash is stripped before comparison.

    Returns the same dict shape as match_title_to_archive entries, with
    'match_via': 'slug' and combined_score=1.0 on exact stem match, or 0.9
    on a strong stem-prefix relationship. Returns None on no slug match.
    """
    needle = _filename_to_slug_stem(pdf_filename)
    if not needle or len(needle) < 6:
        return None

    # 1) Exact stem match
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

    # 2) Token-set overlap on slug stems. Splits 'a-b-c-d' into {a,b,c,d} on
    #    both sides; requires the intersection to be a large fraction of the
    #    shorter set AND a meaningful fraction of the longer set. Plus, both
    #    must share their first token (the year-or-keyword anchor) to avoid
    #    spurious matches like "1997-research-calendar" colliding with
    #    "2001-research-calendar".
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
        # Anchor: first token must match (year, or distinctive first word)
        if needle_tokens[0] != stem_tokens[0]:
            continue
        inter = needle_set & stem_set
        if len(inter) < 2:
            continue
        short_set, long_set = (
            (needle_set, stem_set) if len(needle_set) <= len(stem_set)
            else (stem_set, needle_set)
        )
        short_cov = len(inter) / len(short_set)   # fraction of shorter covered
        long_cov = len(inter) / len(long_set)     # fraction of longer covered
        # Require strong coverage of the shorter side (≥0.80) and at least
        # 40% coverage of the longer side. Catches "1998-10-hp-high-availability"
        # vs "1998-hp-high-availability-and-metadata".
        if short_cov >= 0.80 and long_cov >= 0.40:
            score = 0.80 + 0.15 * long_cov  # 0.86-0.95 range
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
    """
    Return top_k candidate matches sorted by combined score, each with:
        study_id, title, relative_path, lev_ratio, token_ratio, combined_score

    If filename_stem is provided and its first token matches the archive
    study's slug first token (typically a year like '1988' or a distinctive
    keyword), apply a +0.10 anchor bonus to the combined score. This lifts
    legitimate matches that score in the 0.50-0.70 range due to verbose
    archive titles vs. terse PDF cover titles, while still requiring SOME
    semantic overlap (the unbonused score must be ≥0.40).
    """
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


# Match-confidence thresholds (combined_score)
CONFIDENCE_STRONG = 0.75   # auto-process (lowered from 0.85 in v2.2 after
                           # observing legitimate 0.55-0.70 matches where
                           # archive titles are verbose academic versions
                           # of terse PDF cover titles. Anchor bonus on
                           # year-token match boosts true positives.)
CONFIDENCE_WEAK = 0.55     # ambiguous — route to cannot_decide
# below 0.55 → reject (no match)


# =============================================================================
# Manifest dataclass
# =============================================================================

@dataclass
class StudyManifest:
    mode: str  # "new" or "existing"
    slug: str
    source_pdf_original: str
    source_pdf_archived: str
    pdf_sha256: str
    pdf_size_bytes: int
    pdf_page_count: int
    bucket: str
    assigned_bucket: str  # what the user said
    predicted_bucket: str  # what the classifier said
    bucket_signals: dict
    is_outlier: bool
    prepared_at_utc: str
    # Mode 2 additions:
    extracted_title: Optional[str] = None
    title_source: Optional[str] = None
    matched_study_id: Optional[str] = None
    match_score: Optional[float] = None
    match_candidates: Optional[list] = None
    pipeline_version: str = "prepare_for_ingest v2.0"
    steps: list[dict] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, default=str)


# =============================================================================
# Shared per-PDF preparation
# =============================================================================

def _open_pdf_basics(pdf_path: Path) -> tuple[int, str, int]:
    """Return (page_count, sha256, size_bytes). Fast — no full read."""
    doc = fitz.open(str(pdf_path))
    page_count = len(doc)
    doc.close()
    return page_count, sha256_of_file(pdf_path), pdf_path.stat().st_size


def prepare_study(
    pdf_path: Path,
    study_dir: Path,
    bucket: str,
    entities: list[dict],
    mode: str,
    *,
    artifact_suffix: str = "",
    copy_pdf: bool = True,
    overwrite_pdf: bool = False,
) -> dict:
    """
    Run the six prep steps for one PDF into study_dir.

    artifact_suffix: "" for Mode 1, "_v20" for Mode 2 (so Mode 2 doesn't
                     overwrite existing CSVs in the archive study dir).
    copy_pdf:        Whether to copy the input PDF into study_dir/source/original.pdf.
                     Always True for Mode 1; True for Mode 2 unless --dry-run.
    """
    source_dir = study_dir / "source"
    working_dir = study_dir / "working"
    figures_dir = working_dir / "figures"

    source_dir.mkdir(parents=True, exist_ok=True)
    working_dir.mkdir(parents=True, exist_ok=True)

    archived_pdf = source_dir / "original.pdf"
    if copy_pdf and (not archived_pdf.exists() or overwrite_pdf):
        shutil.copy2(pdf_path, archived_pdf)
    elif not archived_pdf.exists():
        # If we're not copying and the PDF isn't there, use the input directly
        archived_pdf = pdf_path

    page_count, pdf_sha, pdf_size = _open_pdf_basics(archived_pdf)
    log.info(f"    {study_dir.name}: {page_count}pp, {pdf_size/1024:.0f}KB")

    # Step 1
    md_path = working_dir / f"extracted{artifact_suffix}.md"
    s1 = step1_extract_markdown(archived_pdf, md_path)
    md_text = md_path.read_text(encoding="utf-8")

    # Step 2 — classifier (sanity check in Mode 1; informational in Mode 2)
    predicted, signals = classify_bucket(pdf_path.name, md_text, page_count)
    bucket_txt = working_dir / f"bucket{artifact_suffix}.txt"
    bucket_txt.write_text(bucket + "\n", encoding="utf-8")
    signals_path = working_dir / f"bucket_signals{artifact_suffix}.json"
    signals_path.write_text(json.dumps(signals, indent=2), encoding="utf-8")

    is_outlier = (mode == "new") and (predicted != bucket)
    if is_outlier:
        log.warning(
            f"    OUTLIER: assigned={bucket} predicted={predicted}  "
            f"({signals['decision_reason']})"
        )
    else:
        log.info(f"    bucket={bucket} (predicted={predicted})")

    # Step 3 — figures
    s3 = step3_extract_figures(archived_pdf, figures_dir, bucket)
    if not s3["skipped"]:
        log.info(f"    figures: {s3['figures_extracted']} extracted")

    # Step 4 — entities
    ent_csv = working_dir / f"entity_candidates{artifact_suffix}.csv"
    s4 = step4_entity_prepass(md_text, entities, ent_csv)
    log.info(f"    entities: {s4['candidates_found']} candidates; top: {s4['top_3']}")

    # Step 5 — observations
    obs_csv = working_dir / f"observation_candidates{artifact_suffix}.csv"
    s5 = step5_observation_prepass(md_text, bucket, obs_csv)
    if not s5.get("skipped"):
        log.info(f"    observations: {s5['candidates_found']} candidates")

    return {
        "page_count": page_count,
        "pdf_sha256": pdf_sha,
        "pdf_size_bytes": pdf_size,
        "predicted_bucket": predicted,
        "bucket_signals": signals,
        "is_outlier": is_outlier,
        "archived_pdf": str(archived_pdf),
        "step_results": [s1, {"step": "2_classify_bucket", **signals}, s3, s4, s5],
        "step3": s3,
        "step4": s4,
        "step5": s5,
    }


# =============================================================================
# Mode 1 — new buckets
# =============================================================================

def run_mode_new(
    pdf_dir: Path,
    out_dir: Path,
    bucket: str,
    entities: list[dict],
    force: bool,
    limit: int,
) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if limit:
        pdfs = pdfs[:limit]
    log.info(f"MODE 1 (new): processing {len(pdfs)} PDF(s) as bucket {bucket}")

    summary_rows: list[dict] = []
    outliers: list[dict] = []
    cannot_decide: list[dict] = []

    for i, pdf in enumerate(pdfs, 1):
        log.info(f"[{i}/{len(pdfs)}] {pdf.name}")
        slug = study_slug(pdf)
        study_dir = out_dir / slug
        manifest_path = study_dir / "manifest.json"
        if manifest_path.exists() and not force:
            log.info(f"  [skip] manifest exists; use --force to reprocess")
            summary_rows.append({"slug": slug, "status": "skipped"})
            continue

        # Pre-check: PDF readable?
        try:
            _open_pdf_basics(pdf)
        except Exception as e:
            log.error(f"  PDF unreadable: {e}")
            cannot_decide.append({
                "pdf": pdf.name,
                "reason": f"unreadable: {e}",
                "details": "",
            })
            summary_rows.append({"slug": slug, "status": "cannot_decide", "reason": str(e)})
            continue

        try:
            r = prepare_study(
                pdf_path=pdf,
                study_dir=study_dir,
                bucket=bucket,
                entities=entities,
                mode="new",
                artifact_suffix="",
                copy_pdf=True,
                overwrite_pdf=force,
            )
        except Exception as e:
            log.exception(f"  FAILED: {e}")
            cannot_decide.append({
                "pdf": pdf.name,
                "reason": f"prep error: {e}",
                "details": "",
            })
            summary_rows.append({"slug": slug, "status": "error", "reason": str(e)})
            continue

        # Detect ambiguous / cannot-decide PDFs (no signals AND no entities AND no observations)
        if (
            r["bucket_signals"]["is_ambiguous"]
            and r["step4"]["candidates_found"] == 0
            and (r["step5"].get("candidates_found") == 0)
        ):
            cannot_decide.append({
                "pdf": pdf.name,
                "reason": "ambiguous + zero entities + zero observations",
                "details": json.dumps(r["bucket_signals"]),
            })

        if r["is_outlier"]:
            outliers.append({
                "pdf": pdf.name,
                "slug": slug,
                "assigned_bucket": bucket,
                "predicted_bucket": r["predicted_bucket"],
                "decision_reason": r["bucket_signals"]["decision_reason"],
            })

        manifest = StudyManifest(
            mode="new",
            slug=slug,
            source_pdf_original=str(pdf),
            source_pdf_archived=r["archived_pdf"],
            pdf_sha256=r["pdf_sha256"],
            pdf_size_bytes=r["pdf_size_bytes"],
            pdf_page_count=r["page_count"],
            bucket=bucket,
            assigned_bucket=bucket,
            predicted_bucket=r["predicted_bucket"],
            bucket_signals=r["bucket_signals"],
            is_outlier=r["is_outlier"],
            prepared_at_utc=datetime.now(timezone.utc).isoformat(),
            steps=r["step_results"],
        )
        manifest_path.write_text(manifest.to_json(), encoding="utf-8")

        summary_rows.append({
            "slug": slug,
            "status": "ok",
            "bucket": bucket,
            "predicted_bucket": r["predicted_bucket"],
            "is_outlier": r["is_outlier"],
            "page_count": r["page_count"],
            "figures": 0 if r["step3"]["skipped"] else r["step3"]["figures_extracted"],
            "entity_candidates": r["step4"]["candidates_found"],
            "obs_candidates": 0 if r["step5"].get("skipped") else r["step5"]["candidates_found"],
        })

    # Write summary files at out_dir
    write_csv(out_dir / f"_mode1_summary_bucket_{bucket}.csv", summary_rows)
    if outliers:
        write_csv(out_dir / f"_outliers_bucket_{bucket}.csv", outliers)
    if cannot_decide:
        write_csv(out_dir / f"_cannot_decide_bucket_{bucket}.csv", cannot_decide)

    ok = sum(1 for r in summary_rows if r.get("status") == "ok")
    log.info(f"DONE Mode 1 bucket {bucket}: {ok}/{len(summary_rows)} processed.")
    log.info(f"  Outliers: {len(outliers)}, Cannot-decide: {len(cannot_decide)}")
    return 0


# =============================================================================
# Mode 2 — existing studies (title-match into archive)
# =============================================================================

def run_mode_existing(
    pdf_dir: Path,
    archive_root: Path,
    entities: list[dict],
    force: bool,
    limit: int,
) -> int:
    cache_path = pdf_dir / ".archive_index_cache.json"
    studies = build_archive_index(archive_root, cache_path=cache_path)
    if not studies:
        log.error(f"No studies found in {archive_root}")
        return 2

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if limit:
        pdfs = pdfs[:limit]
    log.info(f"MODE 2 (existing): matching {len(pdfs)} PDF(s) against {len(studies)} archive studies")

    summary_rows: list[dict] = []
    cannot_decide: list[dict] = []

    for i, pdf in enumerate(pdfs, 1):
        log.info(f"[{i}/{len(pdfs)}] {pdf.name}")

        # Pass 1 — slug-stem match on filename. Many old PDFs were renamed
        # to mirror archive slugs; this catches them deterministically.
        slug_hit = match_filename_to_slug(pdf.name, studies)
        title = ""
        title_src = ""
        if slug_hit:
            log.info(
                f"  slug match ({slug_hit['match_via']}): "
                f"{slug_hit['study_id']!r}  -> {slug_hit['title']!r}"
            )
            candidates = [slug_hit]
            top = slug_hit
        else:
            # Pass 2 — title extraction + fuzzy match (original path)
            try:
                title, title_src = extract_pdf_title(pdf)
            except Exception as e:
                log.error(f"  title extraction failed: {e}")
                cannot_decide.append({
                    "pdf": pdf.name,
                    "reason": f"title extraction failed: {e}",
                    "extracted_title": "",
                    "top_candidates": "",
                })
                summary_rows.append({"pdf": pdf.name, "status": "cannot_decide_title_fail"})
                continue
            log.info(f"  title ({title_src}): {title!r}")

            # Pass anchor (PDF filename stem) so match_title_to_archive can
            # apply a year/keyword anchor bonus when first tokens align.
            pdf_stem_for_anchor = _filename_to_slug_stem(pdf.name)
            candidates = match_title_to_archive(
                title, studies, top_k=3, filename_stem=pdf_stem_for_anchor
            )
            top = candidates[0]
            anchor_note = " +anchor" if top.get("anchor_bonus", 0) > 0 else ""
            log.info(
                f"  top match: {top['study_id']!r} "
                f"(combined={top['combined_score']:.2f}{anchor_note}, "
                f"lev={top['lev_ratio']:.2f}, tok={top['token_ratio']:.2f})  "
                f"-> {top['title']!r}"
            )

        # Decision
        # Primary: top score ≥ CONFIDENCE_STRONG.
        # Promotion rule: a clear-winner anchor-boosted candidate is promoted
        #   to 'match' when it has the year/keyword anchor bonus AND is
        #   significantly ahead of the runner-up (gap ≥ 0.20). This catches
        #   the common case where the archive title is a verbose academic
        #   restatement of a terse PDF cover title, scoring 0.55-0.75 against
        #   a runner-up in the 0.30s. The wide gap proves it's not ambiguous.
        top_score = top["combined_score"]
        runner_up_score = candidates[1]["combined_score"] if len(candidates) > 1 else 0.0
        gap = top_score - runner_up_score
        has_anchor = top.get("anchor_bonus", 0) > 0
        clear_winner = (
            top_score >= CONFIDENCE_WEAK
            and has_anchor
            and gap >= 0.20
        )
        if top_score >= CONFIDENCE_STRONG or clear_winner:
            decision = "match"
            if clear_winner and top_score < CONFIDENCE_STRONG:
                log.info(
                    f"  promoted to match: anchor+gap rule "
                    f"(score={top_score:.2f}, gap={gap:.2f})"
                )
        elif top["combined_score"] >= CONFIDENCE_WEAK:
            decision = "ambiguous"
        else:
            decision = "no_match"

        if decision != "match":
            cannot_decide.append({
                "pdf": pdf.name,
                "reason": f"{decision} (top score {top['combined_score']:.2f})",
                "extracted_title": title,
                "top_candidates": "; ".join(
                    f"{c['study_id']}({c['combined_score']:.2f})" for c in candidates
                ),
            })
            summary_rows.append({
                "pdf": pdf.name,
                "status": f"cannot_decide_{decision}",
                "extracted_title": title,
                "top_score": top["combined_score"],
            })
            continue

        # Attach to matched study directory
        study_dir = Path(top["directory"])
        manifest_path = study_dir / "manifest.json"
        if manifest_path.exists() and not force:
            log.info(f"  [skip] manifest already at {study_dir.name}; use --force to reprocess")
            summary_rows.append({"pdf": pdf.name, "status": "skipped"})
            continue

        try:
            # In Mode 2 we don't know the bucket — use the classifier's prediction
            # but write everything with _v20 suffix so existing artifacts are
            # not overwritten.
            md_path = study_dir / "working" / "extracted_v20.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            s1_temp = step1_extract_markdown(pdf, md_path)
            md_text = md_path.read_text(encoding="utf-8")
            page_count, pdf_sha, pdf_size = _open_pdf_basics(pdf)
            predicted, signals = classify_bucket(pdf.name, md_text, page_count)
            log.info(f"  predicted bucket (v20): {predicted}")

            r = prepare_study(
                pdf_path=pdf,
                study_dir=study_dir,
                bucket=predicted,
                entities=entities,
                mode="existing",
                artifact_suffix="_v20",
                copy_pdf=True,
                overwrite_pdf=force,
            )
        except Exception as e:
            log.exception(f"  prep failed: {e}")
            cannot_decide.append({
                "pdf": pdf.name,
                "reason": f"prep error: {e}",
                "extracted_title": title,
                "top_candidates": top["study_id"],
            })
            summary_rows.append({"pdf": pdf.name, "status": "error"})
            continue

        manifest = StudyManifest(
            mode="existing",
            slug=study_dir.name,
            source_pdf_original=str(pdf),
            source_pdf_archived=r["archived_pdf"],
            pdf_sha256=r["pdf_sha256"],
            pdf_size_bytes=r["pdf_size_bytes"],
            pdf_page_count=r["page_count"],
            bucket=r["predicted_bucket"],
            assigned_bucket="(none — Mode 2)",
            predicted_bucket=r["predicted_bucket"],
            bucket_signals=r["bucket_signals"],
            is_outlier=False,
            prepared_at_utc=datetime.now(timezone.utc).isoformat(),
            extracted_title=title,
            title_source=title_src,
            matched_study_id=top["study_id"],
            match_score=top["combined_score"],
            match_candidates=candidates,
            steps=r["step_results"],
        )
        manifest_path.write_text(manifest.to_json(), encoding="utf-8")

        summary_rows.append({
            "pdf": pdf.name,
            "status": "ok",
            "matched_study_id": top["study_id"],
            "match_score": top["combined_score"],
            "extracted_title": title,
            "predicted_bucket": r["predicted_bucket"],
            "figures": 0 if r["step3"]["skipped"] else r["step3"]["figures_extracted"],
            "entity_candidates": r["step4"]["candidates_found"],
            "obs_candidates": 0 if r["step5"].get("skipped") else r["step5"]["candidates_found"],
        })

    # Summaries live alongside the input directory
    write_csv(pdf_dir / "_mode2_summary.csv", summary_rows)
    if cannot_decide:
        write_csv(pdf_dir / "_cannot_decide_mode2.csv", cannot_decide)

    ok = sum(1 for r in summary_rows if r.get("status") == "ok")
    log.info(f"DONE Mode 2: {ok}/{len(summary_rows)} matched & processed.")
    log.info(f"  Cannot-decide: {len(cannot_decide)}")
    return 0


# =============================================================================
# CSV writer helper
# =============================================================================

def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    fieldnames = sorted({k for r in rows for k in r.keys()})
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    log.info(f"  Wrote {len(rows)} rows -> {path}")


# =============================================================================
# CLI
# =============================================================================

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Prepare PDFs for archival-ingest v20 (local-only, zero credits). "
            "Two modes: --mode new (pre-bucketed PDFs) and --mode existing "
            "(match old PDFs to existing archive studies)."
        ),
    )
    p.add_argument("--mode", choices=["new", "existing"], required=True,
                   help="'new' for pre-bucketed PDFs (buckets A-E); "
                        "'existing' to match old PDFs against the archive")
    p.add_argument("--pdf-dir", type=Path, required=True,
                   help="Directory containing input PDFs (non-recursive)")
    p.add_argument("--bucket", choices=["A", "B", "C", "D", "E"], default=None,
                   help="Mode 1 only: the bucket all PDFs in --pdf-dir belong to")
    p.add_argument("--out-dir", type=Path, default=None,
                   help="Mode 1 only: where prepared study dirs are written")
    p.add_argument("--archive-root", type=Path, default=None,
                   help="Mode 2 only: root of the cloned archive repo")
    p.add_argument("--entities", type=Path, required=True,
                   help="Path to _known_entities.csv")
    p.add_argument("--force", action="store_true",
                   help="Reprocess even if a manifest already exists")
    p.add_argument("--limit", type=int, default=0,
                   help="Process at most N PDFs (0 = unlimited)")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args(argv)
    setup_logging(args.verbose)

    # Mode-specific validation
    if args.mode == "new":
        if args.bucket is None:
            log.error("--mode new requires --bucket (A/B/C/D/E)")
            return 2
        if args.out_dir is None:
            log.error("--mode new requires --out-dir")
            return 2
    else:  # existing
        if args.archive_root is None:
            log.error("--mode existing requires --archive-root")
            return 2
        if not args.archive_root.is_dir():
            log.error(f"--archive-root not a directory: {args.archive_root}")
            return 2

    if not args.pdf_dir.is_dir():
        log.error(f"--pdf-dir not a directory: {args.pdf_dir}")
        return 2
    if not args.entities.is_file():
        log.error(f"--entities not a file: {args.entities}")
        return 2

    log.info(f"Loading known entities from {args.entities}")
    entities = load_known_entities(args.entities)
    log.info(f"  loaded {len(entities)} entities")

    t0 = time.time()
    if args.mode == "new":
        rc = run_mode_new(
            pdf_dir=args.pdf_dir,
            out_dir=args.out_dir,
            bucket=args.bucket,
            entities=entities,
            force=args.force,
            limit=args.limit,
        )
    else:
        rc = run_mode_existing(
            pdf_dir=args.pdf_dir,
            archive_root=args.archive_root,
            entities=entities,
            force=args.force,
            limit=args.limit,
        )
    log.info(f"Total elapsed: {time.time()-t0:.1f}s")
    return rc


if __name__ == "__main__":
    sys.exit(main())
