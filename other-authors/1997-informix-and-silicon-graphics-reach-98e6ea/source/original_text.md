# Original Text: Informix and Silicon Graphics Reach New TPC-C SMP High-Water Mark

> Source: https://web.archive.org/web/19971007160057/http://www.aberdeen.com:80/secure/profiles/1997/infsgi/body.htm

---

The Wayback Machine - https://web.archive.org/web/19971007160057/http://www.aberdeen.com:80/secure/proﬁles/1997/infsgi/body.htm
Informix Software,
Inc.
Silicon Graphics Computer
Systems
4100 Bohannon Drive
Menlo Park, CA 94025
2011 N. Shoreline Rd.
Mountain View, CA 94043-1389
Informix and Silicon Graphics Reach
New TPC-C SMP High-Water Mark
Executive Summary
Informix Software and Silicon Graphics have reached a new level of SMP
(symmetric multiprocessing) performance in the Transaction Processing
Council (TPC) TPC-C benchmark. By combining Silicon Graphics' Origin2000
Server machine with Informix-OnLine Dynamic Server 7.3, these two suppliers
achieved 25,309.20 tpmC with a price-performance of $139.04 per tpmC. The
Informix-Silicon Graphics solution's OLTP performance is the highest to date
of any non-clustered solution and ranks second among all TPC-C results. The
price-performance is the best of all $3-million-and-up systems and close to the
very best of the $1-million-and-up conﬁgurations.
SMP architectures use multiple processors sharing a single memory under the
control of a single copy of an operating system. SMP hardware platforms are
available from every hardware supplier, and are the workhorses of the open-
systems computing revolution. Thus, the Informix-Silicon Graphics
combination gives IS buyers a new and highly attractive option in meeting
ever-increasing demands for high-end OLTP and complex-decision-support
performance.
Silicon Graphics: They're Here
These results should cause IS buyers to reassess both Informix and Silicon
Graphics. In Silicon Graphics' case, Aberdeen research shows that most of the
market -- and Silicon Graphics itself -- saw SGI hardware as better used for
technical applications such as Hollywood special effects. Smart IS buyers,
however, noticed that Silicon Graphics' hardware performed well in non-
technical applications, and commercial applications are becoming a major
source of Silicon Graphics revenue.
The fact that Silicon Graphics is beginning to play the TPC benchmark game in
partnership with high-performance RDBMS suppliers like Informix shows that
it is now a serious player in the high-end commercial markets, and the new
benchmark result shows that Silicon Graphics is now a force to be reckoned
with in OLTP. The Origin2000 server used in the benchmark has 28 64-bit 195-
MHz MIPS R10000 CPUs - SMP scalability that can match most if not all
other hardware suppliers. Silicon Graphics' experience with high-bandwidth
media shows, too: it uses 576 4.2-GB SCSI disk adapters to speed up
performance-critical disk I/O.
The scalability extends as well to the number of end users: 21,500 Silicon
Graphics workstations were used in the test. BEA's Tuxedo was once again
validated as a performance enhancer: the benchmark used Tuxedo 6.1 CFS to
gain added scalability.
Informix: They're Back
If Silicon Graphics has been relatively invisible in the data-management
markets as a new commercial contender, Informix has been relatively invisible
recently by its own choice. Long known as the benchmark RDBMS of choice,
Informix over the last year has done few benchmarks. As a result, Aberdeen
research shows that Informix has often been "out of sight, out of mind" in high-
end sales situations.
The new result, coupled with a recent TPC-D result that delivered 70 % more
performance than the nearest competitive offering, clearly establishes that
Informix is back in a leadership role. Silicon Graphics' use of Informix-OnLine
7.3 shows that Informix's 7.x SMP product line continues to deliver outstanding
benchmark results. Informix-OnLine's ability to handle 21,500 end users in the
benchmark shows that Informix can handle the tens of thousands of end users

that today's IS buyers are demanding for business-critical OLTP. Moreover, the
ability to use a 28-way SMP machine efﬁciently speaks well for Informix's
scalability.
64-bit Continues To Prove Out
Aberdeen has argued for the last two years that 64-bit hardware platforms with
VLM (Very Large Memory) databases yield superior - and usable - OLTP
results when compared to 32-bit architectures that typically address less than 2
GB of memory. More memory has always been a go-faster performance aid;
but lower memory prices now make VLM practical for a wide variety of
business applications. We also predicted that Silicon Graphics with its 64-bit
chipset would be among the performance leaders once it turned its attention to
the commercial market.
The Origin2000 server uses 13 gigabytes (GB) of main memory, well beyond
the capacity of most other benchmarking hardware suppliers. As a result, the
SGI solution can scale higher without clustering and with fewer CPUs.
Table 1: Comparing Informix-Silicon Graphics To Past Results
Company/System                  Informix Online Version  Price         Performance     Price-Performance
Silicon Graphics/Origin2000 Server c/s  7.3.UC1  $3,519,012  25,309.20 tpmC  $139.04 per tpmC
Compaq/ProLiant 5000 6/200 Model        7.30     $681,754    6842.70 tpmC    $100 per tpmC
Digital/AlphaServer 8400 5/350 c/s      7.20     $3,778,989  13,646.17 tpmC  $277 per tpmC

The Overall Conﬁguration
Figure 1 shows how Silicon Graphics and Informix conﬁgured their high-
performance solution. Clearly, 28-CPU SMP, 13 GB main memory, 21,500
client SGI workstations, and Informix-OnLine 7.3's sophisticated multithreaded
parallelism all played a role in the high performance.
Other speciﬁcations of note: the Silicon Graphics/Informix system used version
6.4 S2MP of Silicon Graphics' IRIX variant of the Unix operating system.
Communications was via Fast Ethernet, and the system had 2.4237 terabytes of
disk storage.
Figure 1 - Silicon Graphics/Informix-OnLine 7.3 Benchmark
Conﬁguration
Click on graphic for higher resolution
Source: Transaction Processing Council Report, May 1997
Aberdeen Group Conclusions
The new Silicon Graphics-Informix results are good news for IS buyers. They
show that there is plenty of room for improvement left in SMP technology and
that recent market success by the largest RDBMS and hardware suppliers is not
narrowing the range of choices available to IS.
The result also signals a remarkable shift in OLTP-performance technology
leadership. In the recent past, Informix has done few benchmarks and has gone
relatively unnoticed in the OLTP space, while Silicon Graphics has done no
TPC benchmarks and has been pretty much off the OLTP market's radar screen.
With one result, Informix and Silicon Graphics have established a strong claim
to 1997 high-end performance leadership.
The result also signals the maturing of the 64-bit architecture - a ﬁeld
previously dominated by Digital Equipment, with Sun a newer entrant. The
RDBMS companies now have proved that they can actively take advantage of
these different 64-bit environments to deliver levels of system performance on
single systems that could previously only be obtained with loosely-coupled
architectures.

Finally, the Silicon Graphics-Informix result reinforces the conclusion that
systems are now scaling effectively not only in database size, but also in
numbers of end users supported, to match the new high-end needs of IS buyers.
Systems that handle more than 10,000 simultaneous end users can meet the
data-access needs of most enterprises for the vast majority of applications.
We expect this result to be the only the ﬁrst in a wave of new performance-
increasing benchmarks. These should not invalidate the central point: that
Informix and Silicon Graphics are worth careful reassessment.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
For further information on AberdeenGroup's
products and services please contact us at
info@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this
publication are the property of their respective holders. Unless otherwise noted, the entire
contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means
without prior written consent of the publisher.

---

## Frictionless Data Package Metadata

**Package Name:** 1997-informix-and-silicon-graphics-reach-98e6ea  
**Archived:** 2026-03-15  
**License:** CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)  
**Source URL:** https://web.archive.org/web/19971007160057/http://www.aberdeen.com:80/secure/profiles/1997/infsgi/body.htm  
**Observations:** 25  
**Entities:** 7  
**Technologies:** 9  

---

## Prescience Detail

### Assessment: 7/10 — Mostly Prescient

**Accurate Predictions:**

1. **64-bit VLM superiority** — Aberdeen's 2-year argument that 64-bit hardware with VLM yields superior OLTP results proved correct and enduring. The shift to 64-bit became universal by 2003–2005, and the importance of large memory proved foundational to in-memory databases like SAP HANA (launched 2010).

2. **SGI as serious commercial contender** — Partially confirmed. SGI did win some commercial database business in 1997–2001. However, the company subsequently struggled with bad strategic bets (Itanium adoption, failed enterprise pivot) and filed for bankruptcy twice (2006, 2009). Assets were sold to Rackable Systems for $42.5M, and later to HPE in 2016 for $275M.

3. **Informix technical leadership** — The technical assessment was accurate. Informix's performance capabilities were genuine. However, the company was simultaneously being rocked by accounting fraud charges in 1997, which undermined its commercial position. IBM acquired the database division in 2001 for $1 billion.

4. **10K+ concurrent users** — Aberdeen's prediction that systems handling >10,000 simultaneous users would meet most enterprise needs was confirmed; modern cloud systems far exceed this.

5. **Wave of future benchmarks** — This prediction was not realized for this vendor pair; the Informix accounting scandal and SGI's commercial difficulties curtailed their benchmark activity.

**Overall:** Strong technical analysis; accurate on hardware architecture trends; less accurate on long-term commercial viability of both vendors.
