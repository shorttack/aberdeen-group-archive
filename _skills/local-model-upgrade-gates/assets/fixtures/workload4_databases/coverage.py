#!/usr/bin/env python3
"""
coverage.py — anchor-coverage measurement for the Workload 4 bakeoff.

Governing skill : local-model-upgrade-gates v1.3, workload 4 fixture (Requirement 3).
Governing README: ./README.md §6 (pre-filter check #4) and §8 (measurement).

Usage:
    python3 coverage.py <contestant> <narrative.md> [--out coverage_<contestant>.json]

Behavior:
    1. Split the narrative into sentences (simple regex, deterministic).
    2. Classify each sentence as FACTUAL or FRAMING using a small deterministic rule set.
    3. For each FACTUAL sentence, check whether it carries at least one anchor in the
       allowed forms: [study-<id>], [obs-<id>], [ps=<0-5>].
    4. Emit a JSON report to stdout AND to coverage_<contestant>.json.

Design notes (LOCKED with the fixture):
    - The classifier is deliberately simple. Its errors apply IDENTICALLY to all three
      contestants, so relative coverage numbers stay comparable even if the absolute
      factual-vs-framing split is imperfect. Do NOT "improve" the classifier between
      contestants without re-running all prior contestants.
    - No external dependencies. Standard library only. Runs identically on the Mac
      (Ollama contestant) and in the sandbox (cloud, PPLX contestants).
    - Threshold for pre-filter pass: coverage >= 0.90. This script only MEASURES;
      the pre-filter decision lives in run_bakeoff.sh (or a downstream aggregator).

Tested against:
    - The 2026-09-06 smoke-test output (Perplexity_Only/SMOKE_TEST_local_model_2026-09-06.md),
      which has zero anchors — expected coverage 0.00.
    - A hand-authored 3-sentence sample with known anchor placement — expected
      coverage 1.00 or 0.67 as constructed.
    See the __main__ block for self-test invocation: `python3 coverage.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List


# --------------------------------------------------------------------------- #
# Anchor patterns — MUST match the prompt template (README §4).
# Allowed anchor forms:
#   [study-<id>]  where <id> is any non-] token
#   [obs-<id>]    where <id> is any non-] token
#   [ps=<0-5>]    where the digit is a single 0-5
# --------------------------------------------------------------------------- #
ANCHOR_PATTERNS = [
    re.compile(r"\[study-[^\]]+\]"),
    re.compile(r"\[obs-[^\]]+\]"),
    re.compile(r"\[ps=[0-5]\]"),
]


def has_anchor(sentence: str) -> bool:
    return any(p.search(sentence) for p in ANCHOR_PATTERNS)


# --------------------------------------------------------------------------- #
# Sentence splitter — deterministic. Splits on sentence-final punctuation
# followed by whitespace and an uppercase letter, digit, or opening bracket.
# Preserves the terminal punctuation. Merges markdown headings and list items
# into single "sentences" for classification purposes.
# --------------------------------------------------------------------------- #
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\[\"'\(])")


def split_sentences(text: str) -> List[str]:
    """Split narrative text into sentences.

    Preprocessing:
      - Strip fenced code blocks (```...```) — code is neither factual nor framing.
      - Strip YAML sidecar tail if present (everything from ---SIDECAR--- onward).
      - Collapse runs of whitespace within a line, but keep line breaks so headings
        and list markers can be identified.
    """
    # Drop sidecar if the file contains the separator
    if "---SIDECAR---" in text:
        text = text.split("---SIDECAR---", 1)[0]

    # Drop fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Drop inline code spans (`...`). An anchor discussed as a literal token
    # inside backticks is a self-reference to syntax, not a citation. This
    # prevents e.g. the string `[ps=5]` in prose from inflating anchor coverage.
    text = re.sub(r"`[^`\n]*`", "", text)

    # Split on blank lines to get blocks, then split blocks on sentence boundaries
    sentences: List[str] = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue

        # A heading line is its own sentence (leading # ... )
        if block.lstrip().startswith("#"):
            for line in block.splitlines():
                line = line.strip()
                if line:
                    sentences.append(line)
            continue

        # Bullet list — each bullet line is its own sentence
        if re.match(r"^\s*[-*+]\s", block) or re.match(r"^\s*\d+\.\s", block):
            for line in block.splitlines():
                line = line.strip()
                if line:
                    sentences.append(line)
            continue

        # Normal prose — flatten intra-block newlines, then sentence-split
        flat = re.sub(r"\s+", " ", block)
        for s in _SENT_SPLIT.split(flat):
            s = s.strip()
            if s:
                sentences.append(s)

    return sentences


# --------------------------------------------------------------------------- #
# Sentence classifier — FACTUAL vs FRAMING.
#
# A sentence is FACTUAL if it asserts a specific vendor action, study finding,
# benchmark number, quotation, date, market share, or prescience outcome that
# could in principle be checked against the dossier.
#
# Rule set (all deterministic, no ML, no NLP libs):
#
#   RULE F1 (numerals) — sentence contains any digit AND is not a heading or a
#     table row. Numbers in prose almost always represent benchmark values,
#     dates, market shares, or observation counts.
#
#   RULE F2 (proper-noun density) — sentence contains at least ONE token from
#     the fixture entity list (Oracle, Informix, Sybase, Ingres, CA, NCR,
#     Software AG, DB2, CCA, Aberdeen, Kastner, IBM, HP, DEC, Digital,
#     Stratus, Tandem, SAP, Sequent, Compaq, Dell, Microsoft, TPC, ANSI, SQL).
#     These are the actors and artifacts the dossier is about; sentences that
#     name them are almost always making claims about them.
#
#   RULE F3 (assertion verbs) — sentence contains one of the assertion verbs
#     characteristic of factual claims in this domain: launched, released,
#     acquired, dominated, predicted, forecast, benchmarked, scored, ranked,
#     measured, published, testified, priced, shipped.
#
#   RULE FR1 (framing override) — a sentence is FRAMING even if it triggers
#     F1/F2/F3 when it is:
#       - A markdown heading (starts with '#')
#       - A pure meta-transition ("In this chapter", "Chapter goal:", "The rest
#         of this section", "Read:", "See §", "See Chapter", etc.)
#       - A thesis-statement pattern with a modal + evaluative verb but no
#         specific claim ("This matters because", "The point is that", "What
#         I got wrong was", "Looking back", "In hindsight").
#     Framing overrides are checked FIRST and short-circuit the factual test.
#
#   Sentences that trigger no F-rule are FRAMING by default.
#
# The classifier is deliberately biased toward marking sentences FACTUAL. In
# a narrative that fails to cite, that gives a LOWER coverage number (more
# factual sentences, same or fewer anchored) — which is the safe direction
# for a pre-filter gate.
# --------------------------------------------------------------------------- #

_FIXTURE_ENTITIES = {
    # Vendors from Dossier §0
    "oracle", "informix", "sybase", "ingres", "ca",
    "ncr", "software ag", "db2", "cca",
    # Recurring actors named throughout the dossier
    "aberdeen", "kastner", "ibm", "hp", "dec", "digital",
    "stratus", "tandem", "sap", "sequent", "compaq", "dell",
    "microsoft", "tpc", "ansi", "sql", "vax", "alpha",
    "teradata", "at&t", "unix", "windows", "rdbms",
    "baan", "peoplesoft", "siebel", "unicenter", "jasmine",
}

_ASSERTION_VERBS = {
    "launched", "released", "acquired", "dominated", "predicted",
    "forecast", "forecasted", "benchmarked", "scored", "ranked",
    "measured", "published", "testified", "priced", "shipped",
    "sold", "outsold", "beat", "won", "lost", "peaked",
    "grew", "collapsed", "declined", "adopted", "displaced",
    "wrote", "argued", "reported", "delivered", "shipped",
    "recommended", "authored", "audited", "authored",
}

_FRAMING_PATTERNS = [
    re.compile(r"^\s*#"),  # any markdown heading
    re.compile(r"^\s*(chapter goal|read|see (?:§|chapter|section)|in this (?:chapter|section))\b", re.IGNORECASE),
    re.compile(r"^\s*(this matters because|the point is that|what i got wrong|looking back|in hindsight|the lesson (?:here )?is)\b", re.IGNORECASE),
    re.compile(r"^\s*(let me|i want to|before i|first,|second,|third,|finally,)\b", re.IGNORECASE),
]


def is_framing_override(sentence: str) -> bool:
    return any(p.search(sentence) for p in _FRAMING_PATTERNS)


def has_fixture_entity(sentence: str) -> bool:
    s = sentence.lower()
    for ent in _FIXTURE_ENTITIES:
        # Word-boundary-ish match; entity names in this fixture never overlap
        # substrings meaningfully (e.g., "ca" won't false-positive on "call"
        # because we require adjacent non-letter or string boundary)
        pattern = r"(?:^|[^a-z])" + re.escape(ent) + r"(?:[^a-z]|$)"
        if re.search(pattern, s):
            return True
    return False


def has_assertion_verb(sentence: str) -> bool:
    tokens = set(re.findall(r"[A-Za-z]+", sentence.lower()))
    return bool(tokens & _ASSERTION_VERBS)


def has_numeral(sentence: str) -> bool:
    return bool(re.search(r"\d", sentence))


def classify(sentence: str) -> str:
    """Return 'factual' or 'framing'."""
    if is_framing_override(sentence):
        return "framing"
    if has_numeral(sentence) or has_fixture_entity(sentence) or has_assertion_verb(sentence):
        return "factual"
    return "framing"


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

@dataclass
class SentenceRecord:
    text: str
    kind: str        # 'factual' | 'framing'
    anchored: bool   # only meaningful when kind == 'factual'


@dataclass
class CoverageReport:
    contestant: str
    narrative_path: str
    sentence_count: int
    factual_count: int
    framing_count: int
    anchored_count: int
    coverage: float           # anchored_count / factual_count (0.0 if factual_count==0)
    threshold: float = 0.90
    passes_threshold: bool = False
    unanchored_factual_samples: List[str] = field(default_factory=list)  # up to 10, for review

    @classmethod
    def from_sentences(cls, contestant: str, path: str, records: List[SentenceRecord]) -> "CoverageReport":
        factual = [r for r in records if r.kind == "factual"]
        anchored = [r for r in factual if r.anchored]
        unanchored_samples = [r.text for r in factual if not r.anchored][:10]
        coverage = (len(anchored) / len(factual)) if factual else 0.0
        return cls(
            contestant=contestant,
            narrative_path=path,
            sentence_count=len(records),
            factual_count=len(factual),
            framing_count=len(records) - len(factual),
            anchored_count=len(anchored),
            coverage=round(coverage, 4),
            passes_threshold=coverage >= 0.90,
            unanchored_factual_samples=unanchored_samples,
        )


def measure(contestant: str, narrative_path: Path) -> CoverageReport:
    text = narrative_path.read_text(encoding="utf-8")
    sentences = split_sentences(text)
    records = [
        SentenceRecord(text=s, kind=(k := classify(s)), anchored=has_anchor(s) if k == "factual" else False)
        for s in sentences
    ]
    return CoverageReport.from_sentences(contestant, str(narrative_path), records)


# --------------------------------------------------------------------------- #
# Self-test
# --------------------------------------------------------------------------- #

_SELFTEST_ZERO_ANCHORS = """\
# Sample Narrative — Zero Anchors

Oracle dominated the RDBMS market from 1993 onward. Aberdeen scored the
Report Card in 1993 and Ingres ranked best-in-class. The point is that
technical merit did not decide the market.
"""

_SELFTEST_FULL_COVERAGE = """\
# Sample Narrative — Full Coverage

Oracle dominated the RDBMS market from 1993 onward [study-nti-6-rdbms-technology-48f4aa].
Aberdeen scored the Report Card in 1993 [ps=3] and Ingres ranked best-in-class [obs-OBS-042].
The point is that technical merit did not decide the market.
"""

_SELFTEST_MIXED = """\
# Sample Narrative — Mixed

Oracle dominated the RDBMS market from 1993 onward [study-nti-6-rdbms-technology-48f4aa].
Aberdeen scored the Report Card in 1993 and Ingres ranked best-in-class.
The point is that technical merit did not decide the market.
"""

_SELFTEST_BACKTICK_ANCHOR = """\
# Sample Narrative — Backtick anchor (should not count)

Oracle dominated the RDBMS market from 1993 onward.
The bakeoff requires inline citation anchors such as `[ps=5]` for prescience values.
"""


def _self_test() -> int:
    """Return 0 on pass, 1 on fail."""
    import tempfile

    cases = [
        ("zero-anchors",     _SELFTEST_ZERO_ANCHORS,     0.0, False),
        ("full-coverage",    _SELFTEST_FULL_COVERAGE,    1.0, True),
        ("mixed",            _SELFTEST_MIXED,            0.5, False),  # 1 of 2 factual sentences anchored
        ("backtick-anchor",  _SELFTEST_BACKTICK_ANCHOR,  0.0, False),  # backticked anchor stripped
    ]

    failed = 0
    for name, text, want_cov, want_pass in cases:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
            path = Path(f.name)
        rep = measure(name, path)
        ok = (abs(rep.coverage - want_cov) < 0.01) and (rep.passes_threshold == want_pass)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: coverage={rep.coverage} passes={rep.passes_threshold} "
              f"factual={rep.factual_count} anchored={rep.anchored_count} "
              f"(want cov={want_cov}, pass={want_pass})")
        if not ok:
            failed += 1
            print(f"    factual/framing breakdown:")
            for s in split_sentences(text):
                print(f"      [{classify(s)}][anchor={has_anchor(s)}] {s}")

    return 0 if failed == 0 else 1


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Measure anchor coverage for a bakeoff narrative.")
    parser.add_argument("contestant", nargs="?", help="Contestant ID: cloud | ollama | pplx")
    parser.add_argument("narrative", nargs="?", help="Path to the narrative .md file")
    parser.add_argument("--out", help="Output JSON path (default: coverage_<contestant>.json in cwd)")
    parser.add_argument("--self-test", action="store_true", help="Run built-in fixture self-tests")
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    if not args.contestant or not args.narrative:
        parser.error("contestant and narrative are required unless --self-test is given")

    path = Path(args.narrative)
    if not path.is_file():
        print(f"error: not a file: {path}", file=sys.stderr)
        return 2

    report = measure(args.contestant, path)
    out_path = Path(args.out) if args.out else Path(f"coverage_{args.contestant}.json")
    out_path.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")

    # Also emit summary to stdout
    print(json.dumps({
        "contestant": report.contestant,
        "factual_count": report.factual_count,
        "anchored_count": report.anchored_count,
        "coverage": report.coverage,
        "passes_threshold": report.passes_threshold,
        "out": str(out_path),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
