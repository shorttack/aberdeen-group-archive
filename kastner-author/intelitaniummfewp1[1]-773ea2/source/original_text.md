# Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads

> Archived from: intelitaniummfewp1[1].txt
> Original publication date: 2004-03
> Author: Peter S. Kastner

---

## Original Document Text

AberdeenGroup





















Intel’s Itanium:  Ready and Desirable for Mainframe-Class Workloads 



March 2004













Aberdeen Group, Inc.

One Boston Place

Boston, Massachusetts 02108 USA

Telephone: 617 723 7890

Fax: 617 723 7897

www.aberdeen.com





Intel’s Itanium:  Ready and Desirable for Mainframe-Class Workloads

Executive Summary

This Aberdeen Executive White Paper examines the readiness of platforms
based on Intel’s Itanium processors to handle mainframe-class
workloads, and their strengths and weaknesses compared to today’s
mainframes, such as the IBM z990.  

Over the past year, Aberdeen’s user research has raised significant
questions about the commitment of mainframe customers to their platforms
in the long term, and has begun to indicate that Intel-based platforms
are a credible alternative.  These baseline findings are:

 1.	  Enterprise customers are increasingly focused on their
applications’, and therefore their platforms’, overall total cost of
ownership(TCO), return on investment (ROI), and scalability over time,
rather than simply on an existing commitment to a particular platform. 
In many cases, Aberdeen interviewees indicate that mainframe hardware
and associated software licensing costs are perceived as being more
expensive that open system architecture alternatives.

 2.	  Over the last year, IBM has increasingly discounted mainframe
prices to maintain a strong position with its customers, as these
customers add applications and increase the workloads of existing
applications.

 3.	  The absolute performance and scalability of systems based on
Intel’s Itanium 2 processors, as demonstrated by TPC and other
industry benchmarks, have now met or surpassed nearly all commercial
application workload requirements.

 4.	  Other critical application requirements, such as platform
reliability and manageability, are being more adequately addressed by
Intel-system suppliers and Intel than ever before.

 5.	  The growth of the Itanium “ecosystem” (core applications,
tools, and enabling software for supporting commercial business
applications) has been accelerating.  Nearly all major enterprise
business applications (EBAs) provide support, with customers in
production.

This study, therefore, seeks to answer the following questions:

·	Are Intel-based platforms in general, and Itanium in particular, able
to handle mainframe-class workloads in real-world situations — as
opposed to benchmarks?

·	What classes of mainframe users are willing to consider moving to an
Itanium-type platform?

·	What approaches are best if users do choose to move — for example,
replacement of existing applications, migration of existing applications
to the Itanium platform, or leaving existing applications as is and
putting new mainframe-class applications on the Itanium platform?

·	What key criteria should users consider in making an
Itanium-vs-mainframe decision?  What other factors should platform
buyers consider?

·	What benefits in TCO, ROI, or performance/scalability can the
mainframe user expect from moving, if any?

·	What types of applications are best suited for Itanium rather than
the mainframe?

We conclude that Intel Itanium-based platforms not only are ready to
handle mainframe-class workloads, but also in many cases are the
desirable platform for these workloads — some interviewees find them
to be more scalable, equally robust and manageable, more cost-effective,
more flexible, and more programmer-productive.  Specifically, we find
that:

 1	 Real-world users report success in moving typical mainframe-class
workloads from IBM zSeries mainframes to Pentium Xeon-based platforms. 
Itanium is superior in performance and scalability to Xeon on the same
platforms, with other characteristics (especially robustness)
approximately equivalent to Xeon.  Therefore, Itanium can handle most if
not all mainframe-class workloads.

 2	 Interviewees report that migrating the majority of their
applications from the mainframe to an Intel-based platform is
straightforward, and does not require changes to code.  Most of the rest
of their applications can also be migrated with significant but doable
effort.

 3	 Users may also “surround” their mainframes by implementing all
new mainframe-class applications on Itanium platforms, “offload” by
having a new Intel-based application take over some of the workload of
the mainframe one, or “replace” by writing a new Itanium-based
application to replace the old.

 4	 Interviewees report that Intel-based platforms are typically more
performant per processor, more scalable, more cost-effective, more
flexible (standards-based, open, and able to adapt to new technologies
and to integrate with other platforms), more programmer-productive, and
smaller footprint.  Interviewees found the Intel platform equally robust
and manageable.  Interviewees cited performance and cost-effectiveness
as especially marked advantages of Intel-based platforms.

 5	 Interviewees do not view alternatives other than Intel-based
platforms as comparable in value.  Linux on the mainframe is seen as
less manageable and less performant.  AMD’s 64-bit Opteron technology
is seen as less real-world-tested.

 6	 CPU-intensive, rather than I/O-intensive, applications deliver the
largest immediate payback on Itanium-based platforms compared to
mainframe ones.  These applications include not only
technical/scientific and batch functions, but also many large-database
applications such as data warehousing.

 7	 Although the majority of mainframe users are unlikely to change
platforms in the near future, a large minority (approximately 40%) are
open to shifting to an Itanium-based platform.  These users are
attracted especially to Itanium-based platforms’ perceived total cost
of ownership advantages, due particularly to their price/performance,
and flexibility.

Section I: The State of the Market in Mainframe and Intel-Based
Platforms

Key Competitor:  The Mainframe

The mainframe market is overwhelmingly dominated by IBM’s zSeries,
although suppliers such as Unisys continue to offer mainframe-class
machines.  IBM positions the z990, the latest version, primarily as a
database server — IBM quotes Computerworld as stating that “the
majority of data [in the world is] on mainframes.”  The IBM zSeries
chipsets use their own proprietary technology.

Mainframe applications today are primarily written in COBOL, with
significant dependence on the CICS TP (transaction processing) monitor,
as well as flavors of data management tools such as VSAM, IMS, DL/1, and
DB2.  The primary operating system is z/OS, with strong encouragement by
IBM for Linux in virtual machines on the mainframe.  Aberdeen survey
results indicate that approximately 24% of mainframe users now have
Linux on their mainframes.  However, some users indicate that Linux is
not used for mainframe-class workloads.

Presently, IBM is adding support on the zSeries for the development of
“mixed workload” or “composite” applications.  These
applications attempt to speed “on demand” delivery of new
functionality by reuse of existing code.  Moreover, IBM’s “autonomic
computing” initiative is attempting to automate and/or hasten
mainframe-application monitoring and repair.  “Capacity on demand”
initiatives allow customers greater flexibility in adding or
“leasing” temporary mainframe capacity as needed, with more
flexibility in pricing. 

SAP offers an R/2 version of its ERP solution for the mainframe, but is
steadily migrating its customers away from SAP R/2.

Key Competitor:  Intel

Key Intel chips for mainframe-class processing are the Pentium Xeon and
Itanium.  Xeon is a 32-bit architecture, with indications that Intel
will provide upwardly-compatible extensions to 64 bits in the near
future.  Itanium was built “from the ground up” for 64-bit
processing.  Intel estimates Itanium 2 has approximately 30 to 100%
better performance than Xeon, especially in enterprise and technical
application performance.  A new IA-32 Execution Layer for 32-bit Windows
application emulation delivers 50-70% of the performance of a native
Itanium application.

In 2003, Itanium showed strong improvements in breadth of solutions,
including support for more than one thousand key business applications,
implementation on more than 50 platforms, industry-leading performance
in TPC-C, TCP-H, and Linpack benchmarks and implementation at major
users such as British Petroleum, CompUSA, and Proctor & Gamble.  Users
of Xeon and Itanium also primarily use Windows (the “Wintel”
architecture).

Intel plans to improve performance of Itanium by more than seven times
over the next three years.  Intel also aims to achieve cost parity
between Xeon and Itanium.  The multiprocessor-capable Madison Itanium
chip with achieve more than 1.5 GHz speed.

Key suppliers of Xeon and Itanium-based systems include Dell, Unisys,
and HP.

Dell

Dell positions Itanium use mainly for high-performance computing,
technical computing, and mainframe replacement via scale-out clustering.
 It also notes Itanium’s strengths in non-clustered scale-out vertical
applications such as financial services and rendering, as well as for
business applications.  Particular operating systems supported include
Windows and Red Hat Linux.  Particular Dell Itanium-based systems
include the Dell PowerEdge 3250 dual-processor system.

Dell supports migration from mainframes to multiple “scale-out-type”
Itanium-based servers, with the benefits cited as less hardware expense
and lower software licensing costs.  Dell also resells ES7000
Itanium-based servers from Unisys, for those who want 8-processor or
16-processor systems.

Unisys

Unisys offers both mainframe and Itanium systems.  ClearPath is a
“Unix mainframe”, while the ES7000 series is a Wintel architecture
with 8-processor and 16-processor support.  Particular Itanium-based
systems include the Unisys ES7000 Aries 410 (up to 8 processors), 420
(up to 16 processors), 430 (up to 32 processors), and 560 (up to 64
processors).

Unisys finds that those of its customers opting for the mainframe do so
primarily because of its applications, with security, ability to handle
high-volume transactionns, reliability, and capacity on demand
significant inducements as well.  Some of these customers choose to
rehost less-critical applications on a commodity” environment such as
Wintel.  The primary reasons cited are performance and
price/performance.

In March, 2003, Unisys polled its customers about their datacenter
plans.  32 % of Unisys customers said they planned to standardized on a
single operating system in their data center; of these, 56 % said they
plan to standardize on Windows — and therefore, typically, on Intel. 
Moreover, 90 % of those who are consolidating platforms will include
Windows as one of them — and therefore Intel.

HP

HP offers both the HP Integrity and Integrity Superdome solution sets,
which operate on Xeon and Itanium.  Operating systems supported include
Linux, Windows, and HP-UX.  Particular Itanium-based systems include the
HP Integrity rx 1600 and rx2600 servers (up to 2 processors), HP
Integrity rx 4640 and rx5670 servers (up to 4 processors), HP Integrity
rx7620 server (up to 8 processors), HP Integrity rx 8620 server (up to
16 processors), HP Integrity Superdome (up to 64 servers), and the HP
xc6000 cluster of up to 256 HP Integrity rx2600 servers.

HP offers an extensive set of planning services, migration services, and
support services for mainframe users considering moving to HP
Intel-based platforms.  It offers a wide array of industry partnerships,
including Microsoft, Oracle, SAP, SAS, PeopleSoft, and Siebel.  It sees
the primary reasons for mainframe users to move to Intel as performance,
“agility” or flexibility (e.g., the ability to add new functionality
for increased efficiency), and reduced TCO.  HP cites four strategies
for moving from mainframe to Intel:

 1.	  “Surround”, or deploying a new application on HP/Intel instead
of choosing a mainframe

 2.	  “Offload”, or deploying a new application on HP/Intel and then
integrating it with an existing mainframe

 3.	  “Rehost”, or rehosting a mainframe application on HP/Intel

 4.	  “Replace”, or deploying web-based versions of existing
mainframe applications and then discarding the mainframe

Microsoft

Microsoft positions the Wintel architecture against the mainframe as
more performant.  It cites its own internal benchmarking aimed at
assessing Linux-on-mainframe performance.  Microsoft carried out the
NetBench 7.01 file serving benchmark on the WebBench 4.1 Web serving
benchmark on two systems:  a dedicated z/900 with 2 CPUs and 24 GB of
memory, and a dual-900 MHz-processor Wintel machine with 4 GB of
memory..  These benchmarks do not target large-database applications.  

In the NetBench benchmark, Microsoft finds that a single Linux image has
20% less throughput than Wintel.  Wintel Web server performance is at
least 50% better.  Microsoft claims that annual TCO of mainframes used
is 10-20 times greater than the Wintel machine.

 Section II:  The Users Speak

To test the feasibility of implementing mainframe workloads on
Itanium-based servers, Aberdeen interviewed several users who had
implemented these applications, typically on Xeon-based machines. 
Below, we describe their experiences.

Environment

The typical environment for these users is “mixed”, including both
Windows and mainframe servers.  Applications include “ERP-type”
(SAP, PeopleSoft) for one user, and 1000-2900 in-house-developed COBOL
programs for others.  Databases typically include IBM DB2, with some use
of Microsoft SQL Server (for ported applications) and IBM DL/1.  

Changeover to Intel

The typical target platform chosen was Wintel, with Xeon processors. 
Some users chose migration of programs, aided by use of Microfocus COBOL
and DB2, which allowed porting without recompilation; others chose to
implement new applications in Windows in preference to the mainframe
(the “surround” strategy).

The experience of migraters was surprisingly positive, given the
difficulties that migration always imposes.  One user was able to
migrate all 2900 programs — and all end users — over the course of
only a year and a quarter.  By contrast, another found that migrating
CICS applications and moving from DB2 to SQL Server were “hard
ports.”  Web-servicizing mainframe applications before porting
apparently did not make migration easier.

The main barriers to changeover cited were “cultural resistance” and
difficulty of migrating some applications.  Cultural concerns about the
new Wintel platform centered on concerns over its reliability and
security — so far, in all cases, these concerns have proven unfounded.
 Other cultural barriers included a shift to a new programming
environment, which could be counteracted with training.

Over the last few years, they have been moving some of the COBOL-based
applications to Windows servers running Xeon 900 MHz.  They considered
moving to Unix instead, but “Windows won.”  The typical migration
used Microfocus COBOL, which allowed the programs to run on the new
servers without rewrite.  Likewise, programs based on DB2 could be moved
without rewrite.  

Benefits and Concerns

Users stressed the following benefits from their new Intel-based servers
compared to mainframes:

 1	 Performance/”throughput”.  In many cases, they achieved double
or more the performance on the same workload, or the same performance
with double the workload.  Users noted that batch-job performance was
especially good.  Another noted that performance advantages varied by
application, with “the more I/O intensive, the less the benefit.”

 2	 Scalability.  Specifically, with the new multi-processor machines
from HP and others, some users believed they had greater “headroom”
than with their mainframes.

 3	 Cost/MIPS or price/performance.  One user cited an improvement of
“close to an order of magnitude.”

 4	 Cost of ownership.  This related not only to acquisition costs, but
also to the fact that many software licenses tied to the number of
processors on a machine, fewer processors for the same workload meant
lower software license costs.  One user indicated that their cost of
ownership per year with a Wintel platform was one-third that of the
equivalent mainframes.  That same user indicated that despite migration
costs, their payback period was three months.

 5	 Footprint.  For users with high data-center square-footage costs,
the smaller footprint of Wintel was a clear advantage.

 6	 Open standards support/Flexibility.  Some users mentioned their
comfort with a de-facto standard chip whose suppliers provided a clear
roadmap to key platform standards.  

Interestingly, no user expressed concerns about his or her Intel-based
solutions in any area, except security, which related more to Windows
than Intel.  In fact, users reported that their systems had reliability,
availability, programmer productivity, and manageability at least
equivalent to the mainframe.  Security, while a concern, has not yet
proved inferior to the mainframe.

Itanium vs. Other Alternatives

While no users have yet implemented Itanium-based systems in a
production environment, all viewed them favorably and saw few if any
risks in moving from Xeon or (in one case) NonStop to Itanium.  Much of
this assurance can be credited to trust in their supplier’s roadmap
and compilers.  

All users believed that Itanium would deliver better performance per
processor than their present chipset when they began to use it.  Some
indicated that they believed Itanium would be especially suited to
applications involving large databases — the heart of the IBM
zSeries’ image as a database server.  One user noted that the
Itanium’s addressability is larger, so they will require fewer I/Os.

Interviewees typically did not feel that Linux on the mainframe was
ready to handle their challenges, nor did it affect the perceived
benefits of Intel-based platforms.  AMD’s 64-bit Opteron technology is
seen as less real-world-tested.

Section III:  Findings from Mainframe User Survey

Survey respondents comprised a wide range of businesses, with
significant representation from banking/financial services, government,
retail, and consulting.  40% of respondents were from organizations with
over $1 billion in revenues, and 56 were from global organizations (in
more than 2 countries), with 25% non-U.S. respondents.  Most respondents
(88%) had significant influence over their organizations’ hardware
acquisitions.  Respondents’ organizations averaged 5-6 mainframes.  

Primary mainframe applications were ERP and data warehousing, with CRM,
sales force automation, and vertical/in-house-developed applications
also running at 18-25% of organizations.  88% of mainframes were running
z/OS, OS/390, or OS/370, with 25% also running Linux.  

Mainframe users clearly value robustness above all, and scalability
second (see Figure 1).  

Figure 1:  Importance of Various User Criteria to Mainframe Users

     

 

6. 



Please rate what is most important to you about your mainframe(s) in
order of importance. 

 

 



 

1Most important 

2Important 

3Neutral 

4Not as important 

5Least important 



1. Performance and scalability 

49% 48 

37% 36 

6% 6 

7% 7 

1% 1 



2. Robustness (reliability, availability) 

62% 61 

29% 28 

8% 8 

1% 1 

0% 0 



3. Administrative costs and ease 

15% 15 

47% 46 

29% 28 

7% 7 

2% 2 



4. Flexibility and ease of upgrade 

16% 16 

46% 45 

21% 21 

10% 10 

6% 6 



5. Overall cost of ownership 

32% 31 

36% 35 

18% 18 

5% 5 

9% 9 







 

 

 



Source:  Aberdeen Group, March 2004

60% of respondents were satisfied with their mainframes, but 40% were
neutral or dissatisfied.  The area of greatest satisfaction is
robustness (48% satisfied, 4% concerned.  The area of greatest concern
is cost of ownership (3% satisfied, 49% concerned).  Mainframe
flexibility is another area of concern (21% satisfied, 4% satisfied),
while performance/scalability is an area of both satisfaction (36%) and
concern (16%).

Mainframe Users Consider Itanium

Respondents were in general positive towards Itanium (64% believe they
can handle mainframe-class workloads, 36% believe they can’t).  Not
surprisingly, mainframe users were in general reluctant to migrate
existing applications to Itanium or “rip and replace” to
Itanium-based systems (see Figure 2).  Keys to successful migration were
COBOL, CICS, and DB2 migration support (more than 53% wanted these), and
support for other data management systems (39%) and other types of code
such as assembler and FORTRAN ( (45%) were also cited.

Figure 2:  Likelihood of Various Strategies for Itanium Use by Mainframe
Users

     

 

12. 



Please rank the following approaches in order of likelihood if you were
to use Itanium for a mainframe-class workload. 

 

 



 

1Most likely 

2Second most likely 

3Third most likely 

4Least likely 



1. Replace – implement the same application on an Itanium machine,
discard the mainframe 

12% 12 

11% 11 

26% 25 

51% 50 



2. Migrate – move the existing application to an Itanium machine,
discard the mainframe 

16% 16 

18% 18 

36% 35 

30% 29 



3. Surround – implement a new application on Itanium, leave existing
mainframe(s) as is 

31% 30 

31% 30 

26% 25 

13% 13 



4. Extend – implement the existing application on Itanium as well as
running on existing mainframe 

28% 27 

27% 26 

19% 19 

27% 26 







 

 

 



Source:  Aberdeen Group, March 2004

At least 27% of respondents saw an Itanium-class machine as able to
handle all mainframe-class workloads, and 40% as able to handle both
technical/scientific and OLTP workloads (see Figure 3).

Figure 3:  Perceived Ability of Itanium to Handle Mainframe Workloads

     

 

13. 



What kind of mainframe workloads are best suited for an Itanium-class
machine? (check all that apply) 



 



 

 

 



 Heavy computation (technical and scientific CPU-bound) 





  

 39 

 40% 



Heavy computation (non-technical CPU-bound) 





 

35 

36% 



Batch (e.g., extract, sort, report) 





 

31 

32% 



DB2 





 

33 

34% 



Linux 





 

42 

43% 



Online transaction processing 





 

41 

42% 



Security (e.g., authentication, single sign-on) 





 

29 

30% 



WebSphere (e.g., Java applications, middleware) 





 

47 

48% 



Tivoli (network management) 





 

26 

27% 



Application development 





 

40 

41% 







 

 

 



Source:  Aberdeen Group, March 2004

When asked what would induce them to use Itanium for a mainframe-class
workload, respondents overwhelmingly cited cost of ownership (43%, all
other alternatives 12% or less).  32 % of respondents indicated both
that cost of ownership was their greatest mainframe concern and also
that this was their main reason for considering Itanium.  When asked
what would cause them to hesitate to use Itanium for mainframe-class
workloads, respondents overwhelmingly cited risk — migration risk
(30%) and technology roadmap risk (26%).

Xeon vs. Itanium

Xeon as an alternative to Itanium made little difference to respondents
— 66% were indifferent between the two.  Of the rest, 24% saw the
Itanium as preferable, and 9 % saw the Xeon as preferable.  Those seeing
the Xeon as preferable cited wider availability and lower cost.

Overall Survey Findings

 1	 A surprising number of mainframe users — up to 40 % — are uneasy
about their mainframes and considering what to do about them.

 2	 A key source of dissatisfaction is cost of ownership, related to
both hardware acquisition and software license costs.

 3	 Mainframe users fear the risks of migration to Itanium, but readily
concede that Itanium has significant strengths in price/performance, and
many believe (around 40%) that it can handle most if not all
mainframe-class workloads.

 4	 Mainframe flexibility, including ability to handle upcoming Web
standards, is an area of strong mainframe user concern, and Itanium is
perceived as having significant strengths in this area by some mainframe
users.

 5	 In implementing Itanium-based systems for mainframe-class workloads,
mainframe users are more likely to opt for a “surround” or
“extend” strategy than a “migrate” or “replace” one.

 6	 Itanium has a slightly better reputation than Xeon among mainframe
users.

Section 3: Aberdeen Conclusions and Recommendations

Based on its research, Aberdeen concludes:

 8	 Enterprises considering using Itanium for mainframe-class workloads
— including batch, OLTP, data warehousing, enterprise application
support, and technical/scientific — can rest assured that, in most
cases, Itanium-based machines can handle the load.  

 9	 Moreover, Itanium-based machines can deliver major additional
benefits in performance/scalability, flexibility, footprint in data
centers, programmer productivity, and cost of ownership.  At the same
time, these machines can match mainframes in robustness, manageability,
and ability to act as a database server.  

 10	 CPU-intensive applications such as batch and technical/scientific
jobs deliver the largest immediate payback on Itanium-based platforms
compared to mainframe ones.  

 11	 Migration of mainframe applications to Itanium-based platforms —
especially Windows ones — is surprisingly easy, with no need for
recompilation, but a minority of programs remains difficult to migrate,
requiring extensive effort to rewrite.

 12	 “Replace” strategies that require users to rewrite mainframe
applications from scratch take a long time to implement, with
significant cultural resistance to new programming and administrative
practices.  Mainframe users therefore logically tend to prefer a
strategy of “surrounding” their mainframes by implementing all new
mainframe-class applications on Itanium platforms, “offloading” by
having a new Intel-based application take over some of the workload of
the mainframe one, or migration.

 13	 A large minority of mainframe customers (30-40 %) are clearly
motivated to choose choosing Itanium-based systems in preference to more
mainframes.  These are dissatisfied especially with the mainframe’s
cost of ownership (due especially to both hardware acquisition and
software license costs), as well as its flexible support for upcoming
open standards and in some cases its performance.



 14	 The major barrier to these mainframe users choosing Itanium-based
systems is perceived concerns about risk — risk of migration and
technology roadmap risk.  Aberdeen research and real-world user
experiences indicate that these concerns are overblown.

 15	 If Intel, as it has pledged, offers cost parity between Xeon and
Itanium lines and improves Itanium performance steadily, Itanium offers
clear value-add in scalability and price/performance over Xeon for
mainframe-class workloads.

 16	 Alternatives to Itanium such as Linux on the mainframe and AMD
64-bit chips are not viewed by interviewees as comparable in value-add.

 17	 Major suppliers such as HP and Unisys offer a substantial suite of
Itanium-based servers and Itanium-compatible applications, with good
support for migration from 32-bit to 64-bit processing.

Aberdeen therefore recommends that users considering implementing
mainframe-class workloads place Itanium on an equal footing with the
mainframe in their buying decisions, and that existing mainframe users
set up a task force to investigate the possibility of migrating to
Itanium at a strategic level.





---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | intelitaniummfewp1[1]-773ea2 |
| title | Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads |
| author | Peter S. Kastner |
| date | 2004-03 |
| type | white-paper |
| subject_domain | Server Hardware / Mainframe Migration / Intel Itanium |
| methodology | User interviews; mainframe user survey (n~100); secondary market data; vendor briefings |
| source_file | intelitaniummfewp1[1].txt |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Executive White Paper examining readiness of Intel Itanium-based platforms to handle mainframe-class workloads vs. IBM zSeries mainframes. Based on user interviews with Xeon/Itanium adopters and a survey of ~100 mainframe users. Finds Itanium ready and often desirable for mainframe-class workloads including batch, OLTP, data warehousing, and ERP; 40% of mainframe users open to migration. Key advantages: price/performance, flexibility, programmer productivity, lower TCO. Key barriers: migration risk and technology roadmap risk.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Significant piece of Intel-era enterprise computing research; quantitative survey data on mainframe user attitudes; documents the mainframe-to-Intel migration wave at a critical inflection point. |
| **Relevance** | high | Directly relevant to Intel Itanium coverage across the collection; complements the IA Continuum paper; documents the enterprise mission-critical server market dynamics. |
| **Prescience** | medium | Somewhat prescient: correctly identified that 30-40% of mainframe users would eventually move, and that cost of ownership would be the primary driver. However, Itanium ultimately failed as a platform (discontinued 2021), not because mainframes won, but because x86/Xeon proved sufficient for most workloads, which the paper did not fully anticipate. |

### Prescience Detail


**Prediction 1:** Itanium performance improvement over 3 years
- **Claimed:** 7x improvement planned
- **Year:** 2004
- **Confidence at time:** medium

**Actual Outcome 1:** Itanium 7x performance improvement
- **Result:** [UNVERIFIED]
- **Confidence:** refuted
- **Notes:** 

**Prediction 2:** Xeon-Itanium cost parity
- **Claimed:** Intel aims to achieve cost parity
- **Year:** 2004
- **Confidence at time:** medium

**Actual Outcome 2:** Itanium 7x performance improvement
- **Result:** [UNVERIFIED]
- **Confidence:** refuted
- **Notes:** 

**Prediction 3:** Itanium long-term platform viability
- **Claimed:** ready and desirable for mainframe-class workloads; 30-40% of users will migrate
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 3:** Xeon-Itanium cost parity achieved
- **Result:** [UNVERIFIED]
- **Confidence:** refuted
- **Notes:** 


### Entities Referenced (19)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Intel Corporation | company | active |  |
| IBM | company | active |  |
| Unisys | company | active |  |
| Hewlett-Packard (HP) | company | renamed | HP Inc. + Hewlett Packard Enterprise (split 2015) |
| Dell | company | active |  |
| Microsoft | company | active |  |
| SAP | company | active |  |
| PeopleSoft | company | acquired | Oracle Corporation (2005) |
| Oracle | company | active |  |
| AMD | company | active |  |
| British Petroleum (BP) | company | renamed | BP p.l.c. (rebranded as 'BP' in 2001) |
| CompUSA | company | dissolved | Gordon Brothers Group (liquidated 2007–2008); brand/16 stores sold to Systemax/TigerDirect |
| Procter & Gamble | company | active |  |
| Micro Focus International | company | acquired | OpenText (acquired January 2023) |
| Siebel Systems | company | acquired | Oracle (acquired 2006) |
| SAS Institute | company | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks Communications (2006); later spun off as Aberdeen Strategy & Research |
| Computerworld | institution | renamed | Part of IDG/Foundry (IDG acquired by Blackstone 2017; digital brand continues under Foundry/IDG Communications) |

### Technologies Referenced (30)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Intel Itanium 2 Processor | hardware | Intel | growing | {'lifecycle_current': 'discontinued', 'notes': 'Intel discontinued Itanium shipments July 29, 2021. HPE ended Itanium/Integrity server support December 31, 2025. Architecture is fully discontinued.', 'source': 'https://www.theregister.com/2019/02/01/intel_kills_itanium_again/'} |
| Intel Pentium Xeon Processor | hardware | Intel | mature | {'lifecycle_current': 'active', 'notes': 'Intel Xeon server platform remains active. Current generations include Granite Rapids (Xeon 6). Diamond Rapids in development. Core enterprise server CPU line.', 'source': 'https://www.servethehome.com/intel-cancels-its-mainstream-next-gen-xeon-server-processors/'} |
| IBM zSeries z990 Mainframe | hardware | IBM | mature | {'lifecycle_current': 'discontinued', 'notes': 'IBM zSeries z990 hardware reached end of support. IBM Z platform continues as z15/z16/z17, but z990 itself is long discontinued.', 'source': 'https://www.ibm.com/support/pages/product-end-service-dates'} |
| IBM z/OS | platform | IBM | mature | {'lifecycle_current': 'active', 'notes': 'IBM z/OS is actively developed and current. IBM z/OS 3.2 announced for Q3 2025 release to support the new z17 mainframe. IBM continues strategic investment in mainframe platform with AI capabilities, hybrid cloud integration.', 'source': 'https://www.crn.com/news/cloud/2025/ibm-sets-june-date-for-ai-agent-era-z17-mainframes'} |
| IBM OS/390 | platform | IBM | declining | {'lifecycle_current': 'discontinued', 'notes': 'IBM OS/390 sales ended December 2002; support ended September 2004. Succeeded by z/OS, which continues actively. OS/390 itself is discontinued.', 'source': 'https://www.computerworld.com/article/1332439/ibm-to-stop-os-390-sales.html'} |
| IBM DB2 | application | IBM | mature | {'lifecycle_current': 'active', 'notes': 'IBM Db2 (rebranded from DB2) is an actively supported, commercial database product. Db2 for z/OS and Db2 for Linux/Unix/Windows both actively supported through 2027+ with extended support options.', 'source': 'https://www.ibm.com/support/pages/db2-distributed-end-support-eos-dates'} |
| COBOL | language | Various | mature | {'lifecycle_current': 'legacy-supported', 'notes': "COBOL remains in heavy use in banking, insurance, and government, processing ~70-80% of world's business transactions. Not used for new projects but actively maintained on mainframes. Reached TIOBE Top 10 in 2024.", 'source': 'https://zmainframes.com/zlog/cobol-in-2024-is-it-still-relevant-or-a-dying-language/'} |
| IBM CICS TP Monitor | platform | IBM | mature | {'lifecycle_current': 'active', 'notes': 'IBM CICS Transaction Server for z/OS is actively developed (v6.2 released June 2024 with continuous delivery updates). CICS for IBM i is being sunsetted (defect support until Oct 2025), but CICS TS for z/OS remains active.', 'source': 'https://www.ibm.com/support/pages/ibm-cics-transaction-server-zos-56-61-and-62-are-updated-october-2024'} |
| IBM VSAM | application | IBM | mature | {'lifecycle_current': 'legacy-supported', 'notes': 'IBM VSAM (Virtual Storage Access Method) remains supported as a core z/OS data management facility. Not used for new systems but maintained for existing mainframe workloads.', 'source': 'https://www.ibm.com/docs/en/zos'} |
| IBM IMS | application | IBM | mature | {'lifecycle_current': 'active', 'notes': 'IBM IMS (Information Management System) is actively supported. IMS 15.4 released June 2023. IBM continues to invest in IMS modernization for mainframe environments.', 'source': 'https://www.ibm.com/support/pages/ibm-information-management-system-ims154x'} |
| IBM DL/1 | application | IBM | legacy | {'lifecycle_current': 'legacy-supported', 'notes': 'DL/1 (Data Language/1) is the database access language for IMS. Still supported as part of IMS, but not used for new development. Legacy mainframe technology.', 'source': 'https://www.ibm.com/docs/en/ims'} |
| Microsoft Windows Server (Wintel) | platform | Microsoft | mature | {'lifecycle_current': 'active', 'notes': 'Microsoft Windows Server actively developed. Windows Server 2025 is current release. Core enterprise server OS for Microsoft ecosystem.', 'source': 'https://learn.microsoft.com/en-us/windows-server/'} |
| Linux | platform | Open Source | growing | {'lifecycle_current': 'active', 'notes': 'Linux kernel and operating system actively developed. Linux 6.x kernel series current. Dominant OS for servers, cloud, embedded, and supercomputing.', 'source': 'https://www.kernel.org/'} |
| Red Hat Linux | platform | Red Hat | growing | {'lifecycle_current': 'active', 'notes': 'Red Hat Enterprise Linux (RHEL) is actively developed and supported. RHEL 9 is current; RHEL 10 in development. Red Hat (IBM subsidiary) remains dominant in enterprise Linux.', 'source': 'https://access.redhat.com/support/policy/updates/errata'} |
| HP Integrity Servers | hardware | Hewlett-Packard | growing | {'lifecycle_current': 'end-of-life', 'notes': 'HP Integrity servers (Itanium-based) reached end of support December 31, 2025. HP-UX on HP 9000 EOL was March 2021. Platform is fully end-of-life.', 'source': 'https://www.stromasys.com/resources/hp-ux-end-of-support/'} |
| Dell PowerEdge 3250 | hardware | Dell | current | {'lifecycle_current': 'discontinued', 'notes': "Dell PowerEdge 3250 is a circa-2002 server model, long discontinued. Dell's current PowerEdge generation (16th gen) completely supersedes it.", 'source': 'General Dell product lifecycle'} |
| Unisys ES7000 (Itanium) | hardware | Unisys | current | {'lifecycle_current': 'discontinued', 'notes': 'Unisys ES7000 was a 32-way Intel Xeon-based server. Business Information Server software for ES7000 was discontinued (UnixWare edition discontinued Nov 30, 2005). The hardware is no longer sold or supported. Compaq dropped the ES7000 in 2001.', 'source': 'https://public.support.unisys.com/mapper/docs/discontinuance/78321270-011.pdf'} |
| Unisys ClearPath | hardware | Unisys | mature | {'lifecycle_current': 'active', 'notes': 'Unisys ClearPath Forward (MCP and OS 2200 platforms) is actively marketed and supported. Q4 2024 major release delivered. Clients making long-term commitments. Roadmap updated through 2024.', 'source': 'https://www.investing.com/news/transcripts/earnings-call-transcript-unisys-q4-2024-sees-eps-beat-revenue-dip-93CH-3877606'} |
| SAP R/2 | application | SAP | declining | {'lifecycle_current': 'discontinued', 'notes': 'SAP R/2 (mainframe-based predecessor to R/3) was discontinued decades ago. SAP R/3 evolved to SAP ECC/S/4HANA. SAP R/2 has no active support.', 'source': 'General SAP product history'} |
| TPC-C Benchmark | benchmark | Transaction Processing Council | current | {'lifecycle_current': 'active', 'notes': 'TPC-C remains an active benchmark used to measure OLTP performance. Widely used by database vendors (DoltHub 2024 update, YugabyteDB active use).', 'source': 'https://www.tpc.org/information/benchmarks5.asp'} |
| TPC-H Benchmark | benchmark | Transaction Processing Council | current | {'lifecycle_current': 'active', 'notes': 'TPC-H (decision support benchmark) remains active and widely used for analytical query performance measurement.', 'source': 'https://www.tpc.org/information/benchmarks5.asp'} |
| Linpack Benchmark | benchmark | Netlib | current | {'lifecycle_current': 'active', 'notes': "Linpack (HPL - High Performance Linpack) is the standard benchmark used by the TOP500 supercomputer list. Actively used to rank the world's fastest computers.", 'source': 'https://documentation.sigma2.no/jobs/arm-perf/linpack.html'} |
| NetBench 7.01 File Serving Benchmark | benchmark | Ziff Davis | current | {'lifecycle_current': 'discontinued', 'notes': 'NetBench was a file serving benchmark from Ziff Davis; the benchmark program has been discontinued and is no longer actively maintained or used for current systems.', 'source': 'General benchmark history'} |
| WebBench 4.1 Web Serving Benchmark | benchmark | Ziff Davis | current | {'lifecycle_current': 'discontinued', 'notes': 'WebBench 4.1 was a Ziff Davis/Intel web serving benchmark from the late 1990s/early 2000s; discontinued and superseded by SPECweb and other modern benchmarks.', 'source': 'General benchmark history'} |
| IA-32 Execution Layer (for Itanium) | platform | Intel | current | {'lifecycle_current': 'discontinued', 'notes': 'The IA-32 Execution Layer was a software layer for running 32-bit code on Itanium. Intel removed hardware x86 support from Itanium 2 (Montecito) in 2006. Itanium itself discontinued 2021.', 'source': 'https://www.channelinsider.com/tech-companies/intel-drops-hardware-based-32-bit-capabilties-in-itanium/'} |
| Microsoft SQL Server | application | Microsoft | growing | {'lifecycle_current': 'active', 'notes': 'Microsoft SQL Server is actively developed and supported. SQL Server 2022 is the current major release. Mainstream support continues through 2028.', 'source': 'https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-life-overview'} |
| IBM WebSphere | platform | IBM | growing | {'lifecycle_current': 'legacy-supported', 'notes': 'IBM WebSphere Application Server Traditional (tWAS) v8.5.5 and v9.0 remain supported through 2030 (no v10 planned). IBM pushing migration to WebSphere Liberty. Actively receiving fix packs but not new features.', 'source': 'https://www.ibm.com/support/pages/recommended-updates-websphere-application-server'} |
| IBM Autonomic Computing | framework | IBM | emerging | {'lifecycle_current': 'evolved', 'notes': 'IBM Autonomic Computing (self-managing IT concept) evolved into modern AIOps, self-healing infrastructure, and AI-driven operations. The original IBM initiative/brand has been subsumed into AI/ML-driven IT management.', 'source': 'https://www.ibm.com/docs/en/db2/11.5.x?topic=servers-autonomic-computing-overview'} |
| IBM Capacity on Demand (CoD) | platform | IBM | growing | {'lifecycle_current': 'active', 'notes': 'IBM Capacity on Demand (CoD) for mainframes remains an active feature of IBM Z systems, allowing dynamic CPU/memory activation.', 'source': 'https://www.ibm.com/docs/en/zos'} |
| Intel Madison (Itanium 2 chip) | hardware | Intel | current | {'lifecycle_current': 'discontinued', 'notes': 'Intel Madison was the Itanium 2 chip codename (2003). Itanium is fully discontinued with final shipments in July 2021.', 'source': 'https://www.theregister.com/2019/02/01/intel_kills_itanium_again/'} |

### Observation Summary

- Total observations: 36
- By type: benchmark-result: 12, competitive-position: 6, market-sizing: 4, technology-adoption: 4, viability-prediction: 3, actual-outcome: 3, trend-analysis: 2, risk-assessment: 1, recommendation: 1
