#!/usr/bin/env python3
"""
seq-196 cleanup: re-attribute 26 mis-labeled rows (row_ids 462, 468, 471-494, excluding 469/470
already fixed in Batch 14) to their true 2003-2005 source articles.

Authoritative mapping established by verbatim quote match against Batch 14 webarchive extracts
and corroborating web searches. Rows with uncertain publications are flagged with [REVIEW].

Columns edited (indices): 2=date, 3=headline, 4=publication, 5=author, 6=content_type.
kastner_quotation (7), immediate_context (8), is_predictive (9), prescience fields (10-12)
are preserved as-is.
"""
import csv
import os

CSV_PATH = "/home/user/workspace/aberdeen-group-archive/kastner-author/quotations/kastner_quotes_clean.csv"

# row_id -> (date, headline, publication, author, content_type)
UPDATES = {
    # 462 — TechNewsWorld / Jay Lyman / 2004-06-08 (identified from quote's embedded byline)
    "462": (
        "2004-06-08",
        "AMD's Semprons Spare Athlon from Low-End Market",
        "TechNewsWorld",
        "Jay Lyman",
        "online-article",
    ),
    # 468 — Citation of Kastner's own Aberdeen report (mid-2003); quote is IN an article,
    # but the report itself is the identified source. Mark as authored-column.
    "468": (
        "2003-06-01",
        "Why You Need To Replace Those Windows 98 And NT Machines",
        "Aberdeen Group (report)",
        "Peter S. Kastner",
        "authored-column",
    ),
    # 471, 488 — Forbes.com / Pinnacor-AFX News / 2003-11-14 Dell 3Q
    "471": (
        "2003-11-14",
        "Dell 3Q Net Up 21%",
        "Forbes.com",
        "Pinnacor / AFX News",
        "online-article",
    ),
    "488": (
        "2003-11-14",
        "Dell 3Q Net Up 21%",
        "Forbes.com",
        "Pinnacor / AFX News",
        "online-article",
    ),
    # 472, 473, 474 — ServerWatch / Clint Boulton / 2004-06-08 Dell Itanium
    "472": (
        "2004-06-08",
        "Dell Debuts 64-bit Itanium Server",
        "ServerWatch",
        "Clint Boulton",
        "online-article",
    ),
    "473": (
        "2004-06-08",
        "Dell Debuts 64-bit Itanium Server",
        "ServerWatch",
        "Clint Boulton",
        "online-article",
    ),
    "474": (
        "2004-06-08",
        "Dell Debuts 64-bit Itanium Server",
        "ServerWatch",
        "Clint Boulton",
        "online-article",
    ),
    # 475 — PC World / Tom Krazit (IDG News Service) / 2002-08-15 Dell Drops Windows
    "475": (
        "2002-08-15",
        "Dell Drops Windows From Some PCs",
        "PC World",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    # 476 — MarketWatch / Rex Crum / 2003-08-15
    "476": (
        "2003-08-15",
        "Dell buoyed by growth outlook",
        "MarketWatch (CBS.MarketWatch.com)",
        "Rex Crum",
        "online-article",
    ),
    # 477, 478, 479, 483 — Computerworld / Tom Krazit (IDG News Service) / 2003-03-25 Dell printers
    "477": (
        "2003-03-25",
        "Dell launches personal and workgroup printers",
        "Computerworld",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    "478": (
        "2003-03-25",
        "Dell launches personal and workgroup printers",
        "Computerworld",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    "479": (
        "2003-03-25",
        "Dell launches personal and workgroup printers",
        "Computerworld",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    "483": (
        "2003-03-25",
        "Dell launches personal and workgroup printers",
        "Computerworld",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    # 482 — Dell cartridge chip quote, likely same Computerworld 2003-03-25 printers article
    "482": (
        "2003-03-25",
        "Dell launches personal and workgroup printers",
        "Computerworld",
        "Tom Krazit (IDG News Service)",
        "online-article",
    ),
    # 480, 481 — Dell diversification piece (2003-08 after Dell Inc. rename); publication uncertain
    "480": (
        "2003-08-01",
        "Dell diversification into consumer electronics [REVIEW]",
        "[REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    "481": (
        "2003-08-01",
        "Dell diversification into consumer electronics [REVIEW]",
        "[REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    # 484, 485, 486 — Dell asset-recovery / Tod Arbogast / 2003 shareholder meeting
    "484": (
        "2003-08-01",
        "Dell asset-recovery program with Tod Arbogast [REVIEW]",
        "Computerworld [REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    "485": (
        "2003-08-01",
        "Dell asset-recovery program with Tod Arbogast [REVIEW]",
        "Computerworld [REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    "486": (
        "2003-08-01",
        "Dell asset-recovery program with Tod Arbogast [REVIEW]",
        "Computerworld [REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    # 487 — Dell blade/modular server flexibility quote, 2003-2004 [REVIEW]
    "487": (
        "2003-01-01",
        "Dell modular / blade server strategy [REVIEW]",
        "[REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    # 489 — CRN / ChannelWeb / 2003-06-02 Xeon/Itanium faster chips
    "489": (
        "2003-06-02",
        "Faster Intel Xeon and Itanium chips anticipated within 60-90 days",
        "CRN (Computer Reseller News)",
        "[REVIEW]",
        "online-article",
    ),
    # 490 — E-Commerce Times single-data-point semiconductor turnaround, ~2003
    "490": (
        "2003-01-01",
        "No sign of a global semiconductor turnaround yet [REVIEW]",
        "E-Commerce Times [REVIEW]",
        "[REVIEW]",
        "online-article",
    ),
    # 491, 492 — E-Commerce Times / Keith Regan / 2004-05 Cisco CRS-1 HFR
    "491": (
        "2004-05-25",
        "Cisco Unveils CRS-1 Huge Fast Router",
        "E-Commerce Times",
        "Keith Regan",
        "online-article",
    ),
    "492": (
        "2004-05-25",
        "Cisco Unveils CRS-1 Huge Fast Router",
        "E-Commerce Times",
        "Keith Regan",
        "online-article",
    ),
    # 493 — E-Commerce Times / 2004-05-17 Cisco source code leak
    "493": (
        "2004-05-17",
        "Cisco Probes Potential Source Code Leak",
        "E-Commerce Times",
        "[REVIEW]",
        "online-article",
    ),
    # 494 — E-Commerce Times supercomputing piece, ~2003-2004, likely Keith Regan
    "494": (
        "2003-01-01",
        "Supercomputing accessibility [REVIEW]",
        "E-Commerce Times [REVIEW]",
        "Keith Regan [REVIEW]",
        "online-article",
    ),
}


def main() -> None:
    # Read all rows
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    assert header == [
        "row_id", "article_seq", "date", "headline", "publication", "author",
        "content_type", "kastner_quotation", "immediate_context", "is_predictive",
        "prescience_score", "prescience_rationale", "forecast_horizon_years",
    ], f"Unexpected header: {header}"

    updated = 0
    updated_ids: list[str] = []
    for row in rows:
        rid = row[0]
        if rid in UPDATES:
            date, headline, pub, author, ct = UPDATES[rid]
            row[2] = date
            row[3] = headline
            row[4] = pub
            row[5] = author
            row[6] = ct
            updated += 1
            updated_ids.append(rid)

    # Write back with QUOTE_ALL
    tmp = CSV_PATH + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(rows)
    os.replace(tmp, CSV_PATH)

    print(f"Updated {updated} rows")
    print(f"Updated row_ids: {sorted(updated_ids, key=int)}")
    expected = set(UPDATES.keys())
    actual = set(updated_ids)
    missing = expected - actual
    if missing:
        print(f"WARNING: expected row_ids not found in CSV: {sorted(missing, key=int)}")


if __name__ == "__main__":
    main()
