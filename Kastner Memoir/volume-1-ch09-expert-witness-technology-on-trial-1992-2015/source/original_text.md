# Chapter 9: Expert Witness — Technology on Trial (1992–2015)

> Archived from: MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 9: Expert Witness — Technology on Trial (1992-2015))
> Original publication date: 2026-05-14
> Author: Peter S. Kastner

---

## Original Document Text

# Chapter 9: Expert Witness — Technology on Trial
### *(1992–2015)*

---

At some point in the early Aberdeen years, I received a phone call from a law firm I had never heard of.

They were looking for an expert witness in a complex commercial litigation involving enterprise database technology. The case required someone who understood relational databases at both the architectural and market level — not just what the technology did, but what it was worth, what it should have cost, and whether the claims being made about it in a contract dispute were technically credible.

I said yes. That decision opened a parallel career that would run alongside the Aberdeen research practice for more than two decades.

---

## What an Expert Witness Actually Does

Expert witness work is poorly understood outside the legal profession, and worth explaining before the cases themselves.

In American commercial litigation, parties to a dispute can retain qualified experts to provide two types of assistance: *consulting expert* work (confidential analysis and strategy advice to the attorneys, not disclosed to the opposing side) and *testifying expert* work (formal opinions presented in written reports, subjected to deposition, and potentially introduced as trial testimony). The distinction matters enormously. A consulting expert can be completely candid about weaknesses in a client's position — that's the job. A testifying expert must be prepared to defend every opinion under rigorous cross-examination, which means the analysis must be bulletproof.

The career path into expert witness work in technology cases ran through a small number of routes in the 1990s: former senior engineers with direct technical experience, former CIOs who had made major technology purchasing decisions, and — increasingly — technology analysts whose research credentials gave them recognized expertise in market standards and industry practice. Aberdeen's published research and my TPC work gave me credentials that courts found credible. I was an analyst, not an engineer, which turned out to be an advantage in many cases: I could speak to what the industry knew, what the market expected, and what competent technology practice looked like — the standards by which a disputed technology decision would be judged.

Over twenty-plus years I worked on a variety of cases. The subject matter ranged from database licensing disputes to software project failures to antitrust claims in the storage market. Several stand out for their complexity, their stakes, or what they taught.

---

## The Safeway Data Warehouse Case

The most significant litigation engagement of my expert witness career was a major antitrust and breach-of-contract dispute involving Safeway, one of the largest supermarket chains in North America, and a technology vendor. The dispute centered on data warehousing technology: what had been promised, what had been delivered, whether the competitive market analysis that had informed the deal was sound, and what damages were appropriate if it was not. i was second-seat to novice expert Hugh Bishop.

> **Sidebar: Data Warehousing as Legal Battleground**
>
> By the mid-1990s, data warehouses had become strategic infrastructure for large retailers. A properly designed warehouse could consolidate sales data from thousands of point-of-sale terminals, combine it with supplier and inventory data, and produce analytical reports enabling decisions about product placement, promotional pricing, and inventory management.
>
> For a chain the size of Safeway, the competitive implications were significant. Better analytical capability could translate directly into better purchasing negotiations, more effective promotions, and reduced inventory costs — all of which affected margins in a notoriously thin-margin business.
>
> When a data warehouse project failed or underperformed, the damages were calculable — but only with expert analysis that could quantify what a properly functioning system would have enabled versus what the failed system actually delivered. This required someone who understood both the technical architecture of data warehouses and the economics of the retail market they were intended to serve.

Our role in the Safeway engagement was as a damages expert. This required building an analytical model that could credibly answer: what was the market value of the technology that was contracted for, how did it differ from what was delivered, and what was the economic consequence of that gap? In this case, Safeway's Teradata data warehouse machine was effectively destroyed when the fire extinguishing system exploded into the closed computer room.

The work was technically demanding and methodologically rigorous. We drew directly on Aberdeen's research frameworks — the competitive landscape analysis, the TCO models, the performance benchmarking methodology — and applied them to the specific facts of the dispute. The research practice and the litigation practice were not separate disciplines; they used the same analytical tools in different contexts.

The Safeway engagement ran over three years, involved dozens of depositions, and produced hundreds of pages of expert reports. The technical and economic analysis was eventually admitted into evidence. 

The settlement terms were confidential. What I can say is that the case established the market value of enterprise data warehousing capabilities in terms that courts could understand and apply — which is the fundamental contribution of expert testimony in technology disputes.

---

## The Anatomy of a Software Project Failure

A different category of engagement involved post-mortem analysis of failed software projects. These cases were almost always disputes between an enterprise client who had paid a vendor to build or implement a system and a vendor who claimed the system had been delivered per specification.

The forensic methodology I had developed at ADL — the habit of keeping detailed records, the instinct for spotting scope creep and governance failures, the ability to read a project log the way a doctor reads a chart — proved directly applicable to expert witness work.

The pattern in failed IT projects was remarkably consistent across industries and decades:

**Scope was never locked.** The initial contract described a system at a level of abstraction that both parties could agree to, but left implementation details undefined. As development proceeded, the client's understanding of "what the system should do" diverged from the vendor's understanding of "what we contracted to deliver." Neither party was necessarily acting in bad faith; they were operating from different mental models of the same document.

**Requirements changed faster than the contract could accommodate.** Business environments change. A healthcare system under development in 2001 faced a different regulatory environment by 2003. An enterprise resource planning implementation that started in 1999 encountered the Y2K remediation priority in late 1998. Change orders were the legal mechanism for handling requirement changes, but change order negotiations consumed enormous energy and introduced adversarial dynamics into what should have been a collaborative relationship.

**Integration was underspecified.** The system being built almost always had to connect to existing systems that the new system's contract never adequately described. The data formats, transaction volumes, error handling requirements, and performance expectations of those integrations were discovered during implementation, not defined upfront. Integration scope became the site of the most damaging disputes.

**Testing was inadequate.** User acceptance testing was frequently rushed to meet contractual go-live dates. Defects that would have been caught in proper testing were discovered in production, where they were far more expensive to remediate and where they had already caused operational damage.

> **Sidebar: Why IT Projects Fail at Such Consistent Rates**
>
> The Standish Group has been tracking IT project outcomes since 1994. Their CHAOS Report findings have been remarkably consistent over three decades: roughly 30% of IT projects succeed as defined (delivered on time, on budget, with required features), 50% succeed partially (significant cost overruns, delays, or reduced scope), and 20% fail completely.
>
> These rates have improved modestly with agile methodologies, cloud deployment, and SaaS platforms, but the fundamental challenge persists: complex software development involves translating imprecise human requirements into precise machine instructions, under conditions of technical uncertainty, changing business environments, and organizational politics.
>
> Expert witnesses in software project disputes frequently find that the technical failure was real but not the root cause. The root cause was usually a governance failure: inadequate requirements definition, insufficient change management, misaligned incentives between client and vendor, or executive pressure that overrode technical judgment at critical decision points.
>
> In twenty years of expert witness work on software project failures, I encountered genuine technical incompetence perhaps five times. I encountered governance and organizational failures in every single case.

My expert reports in software project failures typically addressed three questions:

1. **What did the contract actually require?** This required careful reading of the contract documents, change orders, requirements specifications, and the contemporaneous communications between parties during negotiation. Contracts are frequently ambiguous; the question is what an objective, reasonable reader would understand the contract to mean given industry standards and practices.

2. **What was actually delivered?** This required technical assessment of the system as built: what functions it performed, where it failed to perform specified functions, and how the observed deficiencies compared to the contracted specification.

3. **What were the consequences?** Damages in failed IT projects typically include: the cost of the work paid for but not received; the cost of remediation; operational losses during the period when the system underperformed; and, in some cases, competitive disadvantage if the system failure affected market position.

The third question was the most analytically demanding and the one where Aberdeen's market research background was most directly valuable. Quantifying the competitive consequences of a technology failure required understanding what properly functioning technology would have enabled — which was exactly the kind of comparative analysis our research practice had performed for advisory clients.

---

## The Florida Welfare Bid
This is an incomplete account that I need to flesh out with more factual data to document the case in the state archives. The gist is EDS and IBM bid on a massive $200 million human services statewide client services application. The Request for Proposal (RFP) required specific terminal response times on average. Unisys, a losing bidder, contacted me to serve as an expert witness in proving a three-tier IBM mainframe system could not meet the RFP specifications. IBM delivered a box of computer paper with 525 performance simulation runs and nothing. I found the needle in the haystack, testified that IBM's own performance estimator said this system would have 20-30 second average response times. The protest lost and I went back to my day to day. What I have recently uncovered while preparing these memoirs is that: several state officials were indicted over the bid; the system was built at a $200 million cost; it failed acceptance tests with 20-30 second response times. Congress, which put up most of the lost millions, was very unhappy, held hearings, and passed two laws that prevent unfettered contracts like Florida's. I was vindicated.

---

## What the Courtroom Taught About Technology Markets

Expert witness work provided an unusual vantage point on technology markets. Most market participants — vendors, buyers, investors, analysts — experience markets through transactions that succeed. The work goes forward, the system gets built, the deal closes. Courts see markets through transactions that failed: the disputes, the misunderstandings, the governance breakdowns, the places where the standard practices of an industry proved inadequate to the specific circumstances of a particular deal.

Several observations recurred across cases spanning two decades:

**Contracts describe aspirations, not obligations.** Enterprise technology contracts are frequently written in language that both parties understand differently. The ambiguity is not always inadvertent — sometimes it is how deals get done when detailed specification would reveal irreconcilable disagreements about scope. The cost of that ambiguity is paid at implementation time, or in court.

**Technical credibility is the scarcest resource in technology disputes.** Most attorneys handling technology litigation understand the legal concepts deeply and the technology superficially. Most technology experts understand the technology deeply and the legal concepts superficially. The value of an expert who genuinely understands both the technical and the economic dimensions of a market is disproportionate to their fee.

**Organizational failure precedes technical failure.** In software project disputes, the technical problems that ended up in court were almost never the first sign of trouble. Before the code was bad, the governance was bad. Before the system failed, the communication between client and vendor had failed. Technology markets would generate fewer disputes if organizations paid the same attention to project governance that they pay to technical specification.

**Market research and litigation analysis use the same tools.** The analytical frameworks that Aberdeen used to advise clients on technology decisions — market definition, competitive comparison, TCO modeling, performance benchmarking — were the same frameworks courts needed to evaluate technology disputes. The translation was methodological: research conclusions are presented with confidence levels; legal opinions are presented with certainty. The underlying analysis is identical.

---

## The End of the Practice

My active expert witness practice wound down around 2015, concurrent with the transition away from the independent consulting work that had followed my Aberdeen departure. The case volumes had been significant and the work had been intellectually demanding in ways that complemented the research practice rather than competing with it.

The skills are not entirely retired. Every analysis I have done since 2015 carries the discipline that expert witness work instilled: defend every number, document every assumption, anticipate every objection. When you have spent years preparing analyses that will be subjected to rigorous adversarial challenge, you bring that standard of rigor to everything else.

The legal system is an imperfect instrument for resolving technology disputes. Judges and juries are asked to make technical judgments they are rarely equipped to make. The adversarial process, while appropriate for resolving disputed facts, is poorly designed for understanding complex technical systems where the truth is not binary. The expert witness system mediates these limitations — imperfectly, but better than the alternative of technical decisions made without any independent expertise at all.

What the work taught, above all, was this: the gap between what technology is supposed to do and what it actually does is where most of the interesting problems live. In research, that gap is called an "opportunity." In litigation, it is called a "dispute." The analysis required to understand it is the same either way.

---

*Next: Chapter 10 — The Long View: What Fifty Years of Technology Markets Teach*



---




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | volume-1-ch09-expert-witness-technology-on-trial-1992-2015 |
| title | Chapter 9: Expert Witness — Technology on Trial (1992–2015) |
| author | Peter S. Kastner |
| date | 2026-05-14 |
| type | memoir |
| subject_domain | memoir/volume-1 |
| methodology | oral-history |
| source_file | MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 9: Expert Witness — Technology on Trial (1992-2015)) |
| license | CC-BY-4.0 |

### Abstract

Peter Kastner recounts a parallel career as a technology expert witness spanning 1992–2015, alongside his Aberdeen Group research practice. Key engagements include a major data-warehousing antitrust dispute involving Safeway and a Teradata machine, software project failure forensics, and a Florida statewide welfare-system bid protest in which Kastner’s IBM performance analysis was later validated by the project’s real-world failure. The chapter distills methodological lessons: governance failure almost always precedes technical failure, market-research frameworks map directly onto litigation analysis, and adversarial expert scrutiny instills a permanent standard of rigor.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | The chapter documents a two-decade expert-witness practice that intersected landmark enterprise-technology disputes and produced durable methodological insights about IT project failure and technology market valuation. |
| **Relevance** | high | Direct first-person account of applying Aberdeen’s analytical frameworks — TCO models, competitive benchmarking, market definition — in adversarial legal proceedings, illuminating how technology market expertise translates to the courtroom. |
| **Prescience** | high | Kastner’s 1990s testimony that IBM’s Florida welfare system could not meet RFP response-time specs was borne out by the system’s real-world failure and subsequent congressional hearings, demonstrating the predictive accuracy of his analytical method. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (14)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks / Aberdeen |
| Safeway | company | active |  |
| Teradata | company | active |  |
| NCR / Teradata | company | active |  |
| Hugh Bishop | person | unknown |  |
| Electronic Data Systems (EDS) | company | acquired | HP Enterprise Services |
| IBM | company | active |  |
| Unisys | company | active |  |
| Florida HRS (Department of Health and Rehabilitative Services) | agency | dissolved | Florida Department of Children and Families |
| U.S. Congress | institution | active |  |
| Arthur D. Little | firm | dissolved |  |
| Intelligent Electronics | company | dissolved |  |
| Andersen Consulting | firm | dissolved | Accenture |

### Technologies Referenced (11)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Data Warehouse | platform | Multiple (Teradata prominent) | growing | active |
| Data Warehouse Appliance | platform | Teradata | growing | legacy-supported |
| Relational Database Management | platform | Multiple | mature | active |
| IBM Mainframe | platform | IBM | mature | legacy-supported |
| Enterprise Resource Planning (ERP) | application | Multiple | growing | active |
| Agile Methodologies | framework | Open | growing | active |
| Cloud Computing / SaaS Platforms | platform | Multiple | emerging | active |
| Total Cost of Ownership (TCO) Modeling | framework | Aberdeen Group | mature | active |
| Performance Benchmarking Methodology | framework | Aberdeen Group / TPC | mature | active |
| TPC (Transaction Processing Performance Council) Benchmarks | framework | TPC | mature | active |
| Retail Enterprise Systems | application | Multiple | growing | active |

### Observation Summary

- Total observations: 70
- By type: personal-recollection: 24, topic-insight: 22, expert-opinion: 17, market-data: 7
