#!/usr/bin/env python3
"""
build_gold_template_v1.py — pre-fill the embedding gold-set template for the
12 ORIGINAL locked probes, using the union of both models' top-6 slugs captured
in the 2026-07-01 A/B report (embed_ab_20260701.md).

Why this exists: the A/B run that produced the top-6 lists happened on the Mac.
Rather than make Pete re-run the harness just to regenerate the labeling surface
for the 12 queries we already have data for, we reconstruct the template here from
the recorded slugs. The 8 NEW probes (probes_v1.txt rows 13-20) have no recorded
slugs yet — Pete runs `embed_ab_harness_v2.py --emit-gold-template` on the Mac to
append their rows, then labels the whole file.

Output columns match the harness --gold reader contract:
  query, candidate_slug, surfaced_by, max_sim, relevant
`max_sim` is left blank here (we only recorded top-1 scores in the report, not
per-slug sims); it's a labeling convenience, not used by the recall math.
`relevant` is blank for Pete to mark 1/0.

surfaced_by: both | incumbent | candidate  (which index's top-6 contained the slug)
"""
import csv
from pathlib import Path

# (query, incumbent_top6, candidate_top6) — verbatim from embed_ab_20260701.md
DATA = [
 ("What did Aberdeen Group predict about client-server computing in the 1990s?",
  ["client-server","study-aberdeen-trends-90s-logan-1991-648c68",
   "study-aberdeen-1996-moving-effectively-next-gen-client-server",
   "study-nti-12-client-server-goals-1993-15a519","client-server-1992","t90-05"],
  ["client-server-1992","study-nti-12-client-server-goals-1993-15a519",
   "study-aberdeen-trends-90s-logan-1991-648c68","quote-946",
   "study-aberdeen-snr-architecture-three-tier-sli-abaaa5","client-server-computing"]),
 ("Which technologies were forecast to disrupt relational databases?",
  ["tech-rdbms","commercial-rdbms","relational-database","ordbms",
   "relational-database-management-systems","digital-rdb"],
  ["relational-database-1996","relational-database","tech-rdbms","databases-rdbms",
   "tech-o2-004","study-aberdeen-1996-distributed-open-rdbms-buying-guide"]),
 ("What was said about Digital Equipment Corporation's market position?",
  ["e3-07","enc-05","dec-digital-equipment","e1-05","e2-05","digital-equipment"],
  ["e3-07","dec-digital-equipment","e1-05","enc-05","ent-s2-001","quote-929"]),
 ("How did analysts view Oracle's pricing strategy?",
  ["quote-92","oracle-corp","oracle-sun-sparc","oracle-corporation","quote-913","e90-05"],
  ["quote-995","quote-913","quote-92","quote-985","quote-720",
   "study-2002-a-kinder-gentler-larry-ellison-oracle-presents-new-cb69fb"]),
 ("What predictions were made about the shift to web-based enterprise software?",
  ["open-source-software","internet","digital-unix-tru64","internet-commerce-platform",
   "enterprise-software","enterprise-soa"],
  ["quote-18","enterprise-software","web-conferencing","quote-872",
   "study-tool-vendors-neglect-intranet-computing-97bde3","quote-720"]),
 ("Which vendors were expected to lose share to open-source software?",
  ["open-source-software","netware-4x","study-tool-vendors-neglect-intranet-computing-97bde3",
   "linux-server","quote-128","quote-173"],
  ["red-flag-linux","it-suppliers","code-vendor-weakness","code-vendor-claim",
   "ent-ibm-os2","apache-software-foundation"]),
 ("What was the outlook for object-oriented databases?",
  ["object-oriented","tech-o2-003","t88-08","object-relational-db","tech-oodbms","tech-28"],
  ["object-oriented","study-1997-object-databases-such-as-o2-odmg-t-c98c72","tech-oodbms",
   "t88-08","tech-o2-003","tech-o2-001"]),
 ("How was Microsoft's entry into enterprise software assessed?",
  ["e3-03","ent-msft-001","microsoft","nt-server-enterprise","ent-nov-002","backoffice-suite"],
  ["ent-msft-001","backoffice-suite","study-1997-microsoft-the-joker-of-enterprise-158636",
   "microsoft-erp-pre-dynamics","microsoft-great-plains","microsoft"]),
 ("What did research say about ERP adoption drivers?",
  ["erp-systems","erp-suite","erp-software","study-decision-maker-erp-services-805ce8",
   "soa-erp-approach","soa-erp"],
  ["study-ee-2005-cio-research-agenda-091505a-4c85cf","study-enterprise-introduction-0fadce",
   "study-enterprise-introduction-wb060305b-fc9e4f",
   "study-enterprise-aligning-for-action-wb060305b-e14454",
   "study-2006-enterprise-integration-researchagenda-d977d6","study-2004-dellsnapshot-953527"]),
 ("Which prescient observations concerned the rise of the internet as a business platform?",
  ["internet","tech-irp-002","internet-technology","study-1998-internet-sales-report-4cde3f",
   "internet-commerce-platform","study-psk-misc-speech-agendas-5965a3"],
  ["internet","study-psk-misc-speech-agendas-5965a3","internet-retail","internet-technology",
   "quote-1148","web-platform"]),
 ("What were the short-horizon prescience verdicts for late-1990s studies?",
  ["1990s","quote-893","study-1991-apple-c-s-e9ffd7","quote-14","quote-867",
   "machine-learning-statistical"],
  ["_prescient","2030s","code-pre-001","code-pre-002","1900s","code-pre-003"]),
 ("How did Aberdeen characterize the total cost of ownership debate?",
  ["tco-model","5-year-tco","web-hosting-content-license","tco-modeling","aberdeen-ttcm",
   "aberdeen-pricing-schedule-2000"],
  ["tco-model","5-year-tco","aberdeen-ttcm","tco-modeling","aberdeen-two-day-retainer-17500",
   "total-cost-of-ownership"]),
]

OUT = Path("/home/user/workspace/embed_gold_template_prefilled_v1.csv")

def main():
    rows = []
    for q, inc, cand in DATA:
        inc_set, cand_set = set(inc), set(cand)
        # union, ordered incumbent-first then candidate-only, preserving list order
        seen = []
        for s in inc + cand:
            if s not in seen:
                seen.append(s)
        for s in seen:
            src = ("both" if s in inc_set and s in cand_set
                   else "incumbent" if s in inc_set else "candidate")
            rows.append({"query": q, "candidate_slug": s, "surfaced_by": src,
                         "max_sim": "", "relevant": ""})
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["query","candidate_slug","surfaced_by",
                                          "max_sim","relevant"],
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    nq = len({r["query"] for r in rows})
    print(f"Wrote {OUT}")
    print(f"  {len(rows)} candidate rows across {nq} queries (12 original probes).")
    print(f"  Remaining 8 probes (probes_v1.txt rows 13-20): run the harness with")
    print(f"  --emit-gold-template on the Mac and append, OR label these 12 first.")

if __name__ == "__main__":
    main()
