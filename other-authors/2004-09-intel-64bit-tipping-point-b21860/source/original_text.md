# The 64-bit Tipping Point: Optimizing Performance, Flexibility, and Value with Intel Itanium Architecture and Intel EM64T

> Archived from: The-64-bit-Tipping-Point-6.pdf
> Original publication date: 2004-09-01
> Author: Intel Corporation

---

## Original Document Text

PAGES=14
---
=== p1 ===
With the launch of the new Intel Xeon™processor
with Intel Extended Memory 64 Technology (Intel
EM64T), the industry is poised for a large-scale
migration to 64-bit computing. Intel EM64T
delivers dramatic benefits for some applications,
while others are better suited for 32-bit computing,
and still others for the more robust 64-bit
capabilities of Intel Itanium architecture. With
leading support for all three options, Intel
processor-based platforms offer unparalleled
flexibility for optimizing capacity, performance, 
and business value across the full range of
enterprise and technical computing environments.
Intel® Solutions White Paper
Technology Planning
September 2004
The 64-bit Tipping Point
Optimizing Performance, Flexibility, and Value with 
Intel® Itanium® Architecture and Intel® Extended Memory 
64 Technology (Intel® EM64T) 

=== p2 ===
2
Table of Contents
Executive Summary
2
Advantages of 64-bit Solutions
3
The Value of Choice for 64-bit Migration
3
Intel® Itanium® Architecture
4
Intel Extended Memory 64 Technology (Intel EM64T)
5
Understanding the Tradeoffs
7
General Recommendations for Platform Selection
9
Optimizing ROI for Selected Enterprise Workloads 11
Intel Software Tools and Developer Programs
11
Keeping the Focus on Business Value
12
Moving Away from Expensive and Inflexible 
Proprietary Solutions
12
Conclusion
12
Additional Resources
13
Case Studies
Matching the Platform to the Workload: 
BEA WebLogic* on Intel Architecture
4
Matching the Platform to the Workload: 
SAS* on Intel Architecture
8
Matching the Platform to the Workload: 
High-Performance Computing on Intel Architecture
10
Sidebars 
Test Drive Your 64-bit Solutions
3
The Intel Xeon™Processor with Intel EM64T
—More Than Just Extended Memory
6
The Power of Parallelism
9
Intel EM64T and High-Performance Workstations
11
Executive Summary
“… New system shipments based on 32-bit x86
processors will be swept away, over time, by
refreshed designs built around x86-64 processors as
these are released into the marketplace. Meanwhile,
IDC’s Server group forecasts that the Itanium-based
server market will grow from less than $1 billion in
2003 to more than $8 billion in 2008.” 
– What Impact Will 64-Bit Computing Have on the x86
Software World?, Al Gillen and Jean S. Bozman, 
IDC Analysts, June 2004.
For more than a decade, 64-bit architectures have played 
an important role at the high-end of enterprise and technical
computing. Intel Itanium architecture shifted the market
dynamics in that space, lowering the cost of entry and
challenging high-end RISC-based systems in scalability,
capacity, performance, and RAS (reliability, availability,
serviceability). The new Intel Xeon processor with Intel Extended
Memory Technology (Intel EM64T) will trigger a broader shift
toward 64-bit solutions. Servers and workstations based 
on this new processor offer reliable and exceptionally cost-
effective 64-bit support, while simultaneously providing
leading performance for existing 32-bit applications. They deliver 
a valuable addition to the high-end capabilities of Itanium
architecture, and will help reduce 64-bit migration costs for 
a wide variety of general-purpose enterprise and technical
applications.
The move toward 64-bit computing for mainstream applications,
will initially focus on applications that are already constrained
by 32-bit memory limitations. The challenge for IT organizations
is to determine the best architecture for specific solutions,
while taking into account total cost and value within the
broader IT and business environments. Itanium architecture
remains the platform of choice for the most demanding,
business-critical data tier applications, such as high-end
database and business intelligence solutions. Platforms based
on the Intel Xeon processor with Intel EM64T are preferable
for general purpose applications, such as Web and mail
infrastructure, digital content creation, mechanical computer-
aided design, and electronic design automation; and for
mixed environments in which optimized 32-bit performance
remains critical. For some mid-tier enterprise applications, the
best choice may not be obvious, and will require a close look
at software availability, business drivers, and workloads.

=== p3 ===
1 The maximum physical memory supported by an Intel architecture-based platform depends on the processor: Intel Xeon processor (64 gigabyte); 
Intel Xeon processor MP (1 terabyte); Intel Itanium 2 processor (1 petabyte).
2 As reported by Giga Research, “RFID has the potential to explode data volumes and message traffic.” IT Trends 2004: Application Architecture and Design, Randy
Heffner, Giga Research, a wholly owned subsidiary of Forrester Research, Inc., November 25, 2003.
3 Itanium 2 processor-based platforms are also capable of simultaneously running 32-bit and 64-bit applications. However, they do not run 32-bit applications natively,
so there is some degradation of performance in comparison with leading Intel Xeon processor-based platforms. In many 64-bit environments this is not an issue. Either
all components are available in 64-bit versions, or some 32-bit components are required, but are not performance-critical to the core application.   
This paper explores the increasing importance of 64-bit capable
platforms, and offers guidelines for planning a cost-effective
transition. It also discusses the importance of platform and
software synergy, and describes Intel’s industry-wide efforts 
to assist software developers in tuning their software for 
best performance on Intel architecture. These efforts will be
increasingly important as Intel EM64T and future architectural
innovations (such as multi-core processors) become promi-
nent in the marketplace, providing IT organizations with
additional options for increasing the business value of their 
IT investments.
Advantages of 64-bit Solutions
There are two key advantages to platforms with 64-bit
capabilities. First, a 64-bit processor transcends the 4GB
memory limit encountered with 32-bit processors, and can
directly access virtually unlimited physical memory.1 This
allows an application to store vast amounts of data in main
memory, which is several orders of magnitude faster than
today’s fastest mass-storage subsystems. Large, memory-
intensive applications that can take advantage of this extra
capacity can see dramatic performance increases. Secondly, 
a 64-bit processor can manipulate data and execute
instructions in chunks that are twice as large (64-bits 
versus 32-bits). This can be a key advantage for complex
calculations that require a high-level of precision. 
Although most existing 32-bit applications have no immediate
need for additional memory, many scientific, engineering, and
design applications will benefit. So will an increasing percentage
of enterprise business solutions, such as security applications
and real-time transactional systems that rely on large data
sets. The availability of highly affordable 64-bit platforms will
simplify migration for many of these applications, and fuel 
the development of additional 64-bit software solutions.
Over the next few years, a variety of additional factors 
will accelerate the move toward 64-bit computing. The most
important is the ongoing explosion in data storage and 
access requirements, along with the growing need for near-
real-time processes to improve customer service, productivity,
regulatory compliance, and business transparency. The rise 
of Web Services and Service Oriented Architecture (SOA) 
is accelerating these developments, by simplifying integration
across businesses and supply chains. High-volume business
transactions are increasingly taking place interactively and 
in real-time, requiring both high security and fast server
response times. 
The impact of these trends is magnified by the ongoing
proliferation of high-performance client devices, including
smart phones, wireless-enabled notebooks, and PDAs. 
Non-user end-points, such as radio frequency identification
(RFID) tags and point of sale devices, are causing a quantum
leap in processing, capacity, and data requirements that 
may ultimately dwarf the end-user-related workloads we 
know today.2 As these trends converge, 64-bit computing
capabilities will become increasingly important for a growing
number of mainstream enterprise applications.
The Value of Choice for 64-bit
Migration
All 64-bit applications and workloads are not the same. Data,
processing, and RAS requirements can vary dramatically. 
For example, a complex engineering application may access
terabytes of data and consume vast processing resources.
Yet response times are typically not critical and an isolated
system failure may not be catastrophic. An enterprise resource
planning (ERP) application, on the other hand, may require
less total compute and data resources, yet failure or slow
response times may impact thousands of users and cost
millions of dollars per minute. In any implementation, it is
therefore vital to clearly determine workload and business
needs, and to craft a best-fit solution that balances reliability,
cost, and performance.
Intel offers two complementary architectural choices that
cover the full range of 64-bit requirements. One is Intel
Itanium architecture, which is designed for the most
demanding and business-critical enterprise and technical
applications. The other is the family of Intel Xeon processor-
based systems with Intel EM64T. Though not equivalent to
Itanium architecture in terms of capacity, performance, and
RAS, these platforms enable a more gradual migration to 
64-bit solutions, since they provide native support for existing,
legacy 32-bit applications.3 In most enterprise computing
environments, both platforms will be needed.
3
Test DriveYour 64-bitSolutions
Find out how your software performs in a 64-bit
environment, by test driving it for 30 days on Intel
architecture based enterprise platforms. For details, 
visit the Intel Web site at: http://www.intel.com/cd/ids/
developer/asmo-na/eng/microprocessors/itanium/
171236.htm

=== p4 ===
4 Itanium 2-Based Servers: Perspective, Gartner Technology Overview, June 8, 2004.
5 Intel’s Itanium: Ready and Desirable for Mainframe-Class Workloads, Peter Kastner, Aberdeen Group, May 14, 2004.
6 Firms Stay The Course On Server Technologies, Brad Day and Frank E. Gillett, Forrester Research, Inc., July 14, 2004.
Intel Itanium Architecture
“Itanium stands out as a processor technology 
that firms want…”
Firms Stay The Course On Server Technologies, 
Brad Day and Frank E. Gillett, Forrester Research, Inc.,
July 14, 2004.
Itanium architecture was built from the ground up for high-end
64-bit computing in business-critical environments. It is based
on Explicitly Parallel Instruction Computing (EPIC) technology,
which incorporates highly parallel processing and innovative,
compiler-based optimization that greatly improves performance
for compute-intensive applications. With these capabilities,
Itanium 2 processor-based systems are delivering outstanding
performance for some of today’s largest and most demanding
workloads, and for technical and scientific applications requiring
high-performance floating-point calculations. According to
analysts at Aberdeen, they “consistently outperform 64-bit
applications running on 64-bit RISC-based servers,”4 and do
so at substantially lower costs.
Itanium architecture is also designed to support the highest
levels of reliability, availability, and serviceability for business-
critical environments. The RAS features of Intel Itanium 2
processor-based systems are comparable, and in some cases
superior, to those found in leading, proprietary platforms.
Because of its enhanced parallelism, large cache configurations,
and massive execution resources, Itanium architecture-based
systems also tend to scale exceptionally well in large SMP
configurations. 
This combination of features makes Itanium architecture an
attractive, standards-based alternative to high-end RISC 
and mainframe systems. According to the Aberdeen Group,
“Intel-based platforms are typically better performing per
processor, more scalable, more cost-effective, and more
flexible (standards-based, open, and able to adapt to new
technologies and integrate with other platforms). They also
are more programmer-productive and feature a smaller
footprint.”5 In other words, they are comparable or superior to
high-end, proprietary architectures on virtually all levels, and
provide extremely powerful and cost-effective alternatives to
aging RISC-based systems for business-critical, data tier
applications. 
Businesses are responding to these capabilities, and to the
wide and growing choice of compatible operating systems (5)
and applications (more than 2,000). As reported by Forrester
Research, Inc., “94% of current Itanium-installed firms plan to
buy more over the next three years, and 50% of those that
haven't yet bought 10 or more Itanium-based servers list it in
their future spend plans.”6
4
Matching the Platform to the
Workload: BEA WebLogic*
on Intel® Architecture
“Then we worked with BEA and Intel to optimize our
code for BEA WebLogic Server on the Intel Itanium 2
processor…It blew away anything else we looked at.” 
– Hans Cobben, Managing Partner, Omicronn,
discussing internal benchmark results for BEA
WebLogic Server on Intel Itanium 2 processor-
based platforms.
At the time this paper was published, the leading
SpecjAppServer2002 benchmark results for both
absolute performance and price/performance were all
achieved using Intel architecture, and the majority using
Intel Itanium® 2 processors. A key reason for this result is
BEA JRockit Java Virtual Machine* (JVM), which was 
co-developed by Intel and BEA and is optimized for both
IA-32 and Itanium architectures. This does not mean
Itanium architecture should be used for all BEA WebLogic
deployments. Front-end Web applications and medium-
size or smaller mid-tier applications may run better 
on Intel Xeon™processor-based platforms. However,
Itanium architecture is the clear choice for server-side
Java applications that have complex business logic or
require large memory resources. 
A case in point is Omicronn’s Trax* software suite, a
platform used by financial organizations that need to
process millions of complex transactions per hour. The
company turned to BEA WEbLogic on Intel Itanium 2
processor-based platforms when it could not achieve
desired performance levels on RISC-based systems. 
In internal benchmark tests, the platform performed 
5 million messages per hour, at only 50-60 percent
utilization, leaving extra capacity for fail-over of another
WebLogic instance—all on a platform that is far 
more cost-effective than RISC-based alternatives.a
a For detailed information, see the full Omicronn case study at:
http://www.intel.com/products/services/intelsolutionservices/success/
casestudies/omicronn.pdf

=== p5 ===
7 Actual performance will depend on specific applications and platform configurations. Intel has seen performance gains well above 50 percent for selected applications
in internal tests. Typical gains have been in the 10 to 40 percent range. 
8 What Impact Will 64-Bit Computing Have on the x86 Software World, Al Gillen, Jean S. Bozman, IDC Analysts, June, 2004.
9 IA-32 supports Physical Address Extensions (PAE), which enables virtual memory of up to 64GB in a 32-bit system (with appropriate OS support). However, this
approach is subject to performance penalties that do not exist with Intel EM64T. 
Operating Modes
for Platforms based on the Intel® Xeon™ Processor
with Intel Extended Memory 64 Technologya (Intel® EM64T)
Legacy Mode
Performance boost of up to 50 
percent for existing 32-bit 
applications. b
Requirements:
•  32-bit OS
•  32-bit applications
•  32-bit drivers
Compatibility Modec
Performance gains for selected
32-bit workloads via increased 
memory addressability (up to 
4GB per application). 
Requirements:
•  64-bit OS
•  32-bit applications
•  64-bit drivers
64-Bit Mode
Performance gains for memory-
and compute-intensive 
applications when ported and
optimized for 64-bit platforms.
Requirements:
•  64-bit OS
•  64-bit applications
•  64-bit drivers
a Intel EM64T ingredients include:
• Extended memory addressability (64-bit pointers & registers).
• Additional registers (8 SSE + 8 general purpose registers).
 
• Double precision (64-bit) integer support.
 b Compared with previous Intel Xeon processor-based platforms. Actual performance will depend on specific applications and platform 
 
configurations. Intel has seen performance gains well above 50 percent for selected applications in internal tests. Typical gains have 
 
been in the 10 to 40 percent range.
c CPU can switch between modes on a code-segment by code-segment basis, enabling 32- and 16-bit applications to run under a 64-bit 
 
OS without recompile. Re-certification of applications may be required.
5
Intel Extended Memory 64 Technology 
(Intel EM64T)
“This change opens up a viable path for customers to
begin their move from 32-bit computing to 64-bit
computing in earnest—and across the board.” 
– What Impact Will 64-Bit Computing Have on the x86
Software World?, Al Gillen and Jean S. Bozman, 
IDC Analysts, June, 2004. 
Intel EM64T is a natural migration of Intel’s 32-bit server
architecture to 64-bits, with additional architectural features
(including instructions and registers) that enable Intel Xeon
processor-based platforms to expand memory addressability
and to run both 32-bit and 64-bit operating systems and
applications. These new platforms deliver leading performance
for existing 32-bit workloads, while eliminating many of the
barriers organizations face in moving one or more critical
applications to 64-bit platforms. 
Intel is currently integrating Intel EM64T into all of its IA-32
processor lines. This will allow businesses to establish an
extremely flexible 32/64-bit infrastructure at very little cost, 
so they can migrate operating systems and applications as
needed without new hardware purchases. According to IDC,
this strategy provides “Excellent investment protection and
additional headroom, all with few or no drawbacks.”8 It is
likely to initiate a broad move toward 64-bit capable platforms
as companies strive to future proof their infrastructure against
unpredictable business requirements. 
Three operating modes are possible, and platforms can
switch modes on a code-segment by code-segment basis
(Figure 1).
• Legacy Mode for Traditional IA-32 Deployments 
(32-bit OS/32-bit Applications)—This is the traditional 
IA-32 mode of operation and requires no changes to
existing 32-bit applications. The processor supports a
maximum of 4GB of virtual memory, which is shared 
among the OS and all applications.9 In most cases, the OS
allocates approximately 2GB of memory to itself, leaving
2GB to the application stack. Since the Intel Xeon processor
Figure 1.  With a performance boost of up to 50 percent or more for existing 32-bit applications, and multiple options for
extending memory addressability7, these platforms deliver exceptional flexibility for cost-effective performance scaling.

=== p6 ===
10 Actual performance will depend on specific applications and platform configurations. Intel has seen performance gains well above 50 percent for selected applications
in internal tests. Typical gains have been in the 10 to 40 percent range. 
11 Most existing 32-bit workloads are optimized for 32-bit operating systems, and are likely to show little or no performance gain in Compatibility Mode. Performance
may even decrease slightly for some (typically less than 5%), because of the increased overhead of the 64-bit operating system.
12  Intel's Enterprise Processor Plans: Positioning the Xeon Processor and the Itanium Processor, by Vernon Turner, IDC, April 2004.
13  Strategic Platforms—The Shift Continues, Richard Fichera, Forrester Research, Inc., June 22, 2004.
with Intel EM64T is the most recent IA-32 processor, it
includes a variety of innovations that can improve performance
for existing 32-bit workloads by as much as 50 percent or
more, even in Legacy Mode 10 (see Sidebar p. 6, The Intel
Xeon Processor with Intel EM64T—More Than Just
Extended Memory). 
• Compatibility Mode for Running 32-bit Applications in
64-bit Environments (64-bit OS/32-bit Applications)—
In this mode, a 64 bit operating system manages system
resources for a 32-bit application. Depending on the
particular OS, each application can be allocated up to 
4GB of memory. No code changes are needed for the
application itself, but 64-bit device drivers are required.
Migration flexibility is the key advantage of this mode. It
enables 32- and 64-bit applications to run concurrently 
on the same platform. Migrations to 64-bits can therefore
be performed incrementally, component by component, 
based on performance and cost.11
• Full 64-bit Mode for Running 64-bit Applications 
(64-bit OS/64-bit applications)—This mode delivers the
full memory advantages of a 64-bit solution, but existing
32-bit applications must be ported to 64-bits and optimized
to achieve full benefits. For those applications that will
ultimately require more robust 64-bit support, this can be
seen as an interim stage in moving toward the higher-
performance, scalability, and RAS of an Itanium architecture-
based solution. As reported by IDC, “Software revised 
and recompiled for 64-bit Xeon processors will be an
important step closer to running on platforms using Itanium
processors.”12 Once an application is ported to 64-bits, 
it is relatively easy to port between the two architectures.
In effect, these three modes of operation establish a pathway
for migrating incrementally and very cost-effectively toward
64-bit solutions. As noted by Forrester Research, Inc., “…the
impact is compelling. Now they [businesses] can deploy
32/64-bit systems at almost no cost penalty, which will allow
them to gradually migrate to 64-bit through a three-stage
process involving a progression from pure 32-bit software, 
to 32-bit applications under 64-bit operating systems, and
ending with pure 64-bit environments with minimal disruption
and risk.”13 Given the flexibility of this approach, the industry
migration to 64-bits is likely to be a gradual and selective
process. Most software developers will begin by validating their
existing 32-bit applications for 64-bit operating environments.
They will then migrate their code if and when it makes sense
based on workload requirements and market demand.
6
The Intel® Xeon™Processor
with Intel EM64T—More
Than Just Extended Memory
“With its host of new memory and I/O technologies,
Intel’s latest server platform…has the potential to help
us continue to meet rapidly growing trading demands.”
– Steve Randich, CIO and Executive Vice President,
NASDAQ Stock Market.
Intel EM64T is one of many new features introduced in
the latest Intel Xeon processor, which is not only 64-bit
capable, but has been shown to deliver performance
boosts of up to 50 percent or more for existing 32-bit
applications.a These performance gains are enabled 
by a wide variety of processor and platform advances,
including higher clock frequency, enhanced multi-threading
capabilities, dramatically improved I/O bandwidth, a
faster system bus and a faster memory subsystem. 
Platforms based on this new processor also benefit from
Intel’s extensive work with leading server manufacturers
and software vendors to develop balanced systems that
not only boost performance, but also help to drive down
total cost of ownership. For example, with this processor
and related chipsets, Intel has introduced new memory
and manageability features that can improve total platform
availability and reduce operating costs. Demanded
Based Switching with Intel SpeedStep® Technology is
also supported, and can reduce platform power
consumption by as much as 25%. In addition, platforms
are available with an integrated Intel IOP332 Storage 
I/O Processor that improves RAID storage performance.
By working with industry leaders to advance the entire
platform, Intel helps to ensure that its processor
innovations deliver better value in a wider range of 
real-world implementations.
a Actual performance will depend on specific applications and platform
configurations. Intel has seen performance gains well above 50 percent
for selected applications in internal tests. Typical gains have been in the
10 to 40 percent range.  

=== p7 ===
Table 1. Understanding the Tradeoffs between Intel’s 64-bit Solutionsa
Intel® Xeon™Processor 
with Intel® EM64T-based
Platforms
Intel Itanium® 2 Processor-
based Platforms
Advantages of Itanium Versus IA-32
Architecture
Performance
• Outstanding price/
performance for 32-bit
applications
• Ideal for gradual, pay-as-
you-go migrations to 64-bits
• Exceptional performance for
high-end 64-bit applications
• Compatible with 32-bit
applications
• Itanium architecture typically delivers 
30-50 percent better performance.b The
advantage tends to be greatest for
floating-point-intensive and business-
critical data tier workloads
Scalability
• Scales to 16-way
• Scales to 512-way, with
larger platforms on the way
The performance advantage of Itanium
architecture increases substantially in large,
SMP configurations:
• 4-way servers: ~ 35% better
• 32-way servers: ~140% better
Memory
Addressability
• Up to 1TB
• Up to 1PB (1,000TB)
• Itanium architecture scales to support the
largest platforms and enterprise data sets
RAS
• High reliability, with on-chip
features such as memory
spares, Chipkill* memory,
and error correction (ECC)
• Additional on-chip reliability
features, such as Enhanced
Machine Check Architecture
(MCA); Pellston technology
will be supported in next-
generation processors
• Itanium architecture delivers high-end
RAS for core, business-critical
applications, making it ideal for mainframe
and high-end RISC replacement
Platforms
• Balanced bandwidth and
high performance for a wide
variety of workloads
• Greater bus bandwidths and
enhanced support for large
symmetric multiprocessing
(SMP) configurations
• Platform manufacturers tend to offer more
advanced platform options for Itanium
architecture-based systems, targeting
high-end, business-critical data tier
environments
7
a This table is based, in part, on information reported in Intel’s Enterprise Processor Plans: Positioning the Xeon Processor and the Itanium Processor, by Vernon
Turner, IDC, April 2004; available on the Intel Web site at: http://www.intel.com/technology/64bitextensions/4071_intel_xeon_rev3.pdf
b Though this is generally true, actual performance will depend on specific workloads and configurations, and Intel Xeon processor-based systems may deliver better
performance in select cases.
Understanding the Tradeoffs
“Key differences in performance, scalability, and
reliability lead to different optimal workloads for
workstations and servers built with Xeon versus
Itanium processors.” 
– Intel’s Enterprise Processor Plans: Positioning 
the Xeon Processor and the Itanium Processor,
Vernon Turner, IDC, April 2004.
In simple terms, Itanium architecture offers better perform-
ance, scalability, and RAS for high-end environments (Table 1).
As described by IDC, “Scaling advantages for SMP servers
using the Itanium processor versus the new Xeon processor
increase sharply when moving to 8-way and higher SMP
configurations.”14 It can therefore be useful to think of Itanium
architecture as best for “scaling up” on large, high-RAS,
multiprocessor platforms for the business-critical data tier; 
and to think of Intel Xeon processor-based platforms as 
best for “scaling out” on clustered server architectures. Of
course, specific business or technical considerations may
take precedence in a particular implementation, and both
architectures can be used successfully to scale up and out.
The availability of compatible applications should also be
monitored. Multiple operating systems and thousands of
applications are now available for Itanium architecture. The
Linux* environment currently includes a 64-bit operating
system for Intel Xeon processor-based platforms with Intel
EM64T, and Microsoft expects to deliver a compatible
operating system in the first half of 2005.15 Application
availability is also beginning to ramp up, and Intel is working
extensively with leading ISVs to accelerate delivery and
optimize performance. 
14 Intel’s Enterprise Processor Plans: Positioning the Xeon Processor and the Itanium Processor, by Vernon Turner, IDC, April 2004.
15 Microsoft has announced plans to release two 64-bit operating systems in the first half of 2005, both of which will be compatible with Intel Xeon processors with Intel
EM64T. Windows Server 2003, Standard x64 Edition, will support servers with up to 4 processors and up to 32 GB of RAM. Windows Server 2003, Enterprise x64
Edition, will support servers with up to 8 processors and 64 GB of RAM. For more information, including application recommendations, see the Microsoft Web site at:
http://www.microsoft.com/windowsserver2003/64bit/extended/standard.mspx and http://www.microsoft.com/windowsserver2003/64bit/extended/enterprise.mspx

=== p8 ===
Matching the Platform 
to the Workload: SAS* 
on Intel® Architecture
“We continue to view Itanium as our strategic platform for
providing high-end enterprise computing on Intel
architecture. The Xeon processor is a viable platform for
many SAS solutions, with Itanium offering the growth path
for advanced Analytic Intelligence.”
– Keith Collins, CTO, SAS
Intel and SAS have been working together for nearly 
a decade to optimize performance for SAS solutions on 
both Intel Itanium® 2 and Intel Xeon™processor based
platforms, and continue to do so at the SAS and Intel
Advanced Research Center (SIARC). With the release of
SAS 9, these efforts are delivering increasingly dramatic
gains for customers, such as the U.S. Census Bureau. The
bureau is now moving from legacy, RISC-based systems to
Itanium architecture, after tests showed they could reduce
their processing time for two years’ workload—48 million
records—from an average of 5 days to just over 7 hours. 
SAS is a global leader in business intelligence solutions.
SAS workloads can vary dramatically between and within
customer implementations, response times can be critical,
and solutions may have to support anywhere from a single
user to thousands of mobile users in distributed locations.
IA-32 solutions may deliver better performance for simpler
workloads with fewer users, especially if individual jobs are
not threaded. As processing and memory requirements
increase, larger platforms and Intel Itanium 2 processors
can deliver essential benefits. 
• For a detailed discussion of workload and platform
considerations for SAS solutions, see Sizing and
Performance Considerations for Intel® Architecture-
Based SAS® Solutions, available at:
http://www.intel.com/business/bss/solutions/
alliances/sas/sizing_guide.pdf
• For more information about the U.S. Census Bureau’s
SAS implementation, see SAS® Performance Exceeds
the U.S. Census Bureau’s Expectations, available at:
http://www.intel.com/business/bss/solutions/alliances/
sas/census.pdf
8
SAS* on Intel® Architecture System Configuration Matrix
Threading Used
Memory Size
Individual Jobs
Fully Threaded
Large Data Sets (TB)
Individual Jobs
Not Threaded
Many
Operations
CPU Load
Few
Operations
•  Intel Xeon™ Processor DP/MP
•  2-way Workstations or Servers
•  Up to 3.6GHz, 4GB RAM
•  Microsoft Windows*, Linux*
•  SAS 9
Single User, 1 Job/CPU
Single User, 1 Job/CPU
•  Intel Pentium® 4 Processor Desktop
•  Up to 3.6GHz, 2GB RAM
•  Notebooks based on Intel Centrino™
mobile technology† up to 2GHz, 
 2GB RAM
•  Microsoft Windows
•  SAS 9
•  Intel Itanium® 2 Processor
•  4- to 64-way Servers
•  Over 1.5GHz, 4GB/CPU RAM
•  Microsoft Windows, HP-UX11i*, Linux
•  SAS 9
Multi-User, 8-10 Jobs/CPU
Multi-User, 2-4 Jobs/CPU
•  Intel Xeon Processor MP
•  4- to 32-way Servers
•  Up to 3GHz, 2GB/CPU RAM
•  Microsoft Windows, Linux
•  SAS 9
GB/Sec
Memory
Bus Load
MB/Sec
Small Data Sets (MB)
High-end SAS implementations will typically run substantially better on Itanium architecture, but a close look at
workload characteristics can be important in making the best platform choices for any given implementation. 

=== p9 ===
It will also be important to monitor platform evolution. Intel is
moving toward a common platform architecture for IA-32 and
Itanium 2 processor-based systems by 2007. At that time, it
is expected that Intel Itanium 2 processors will be delivering
approximately 1.5 to 2 times the performance of Intel Xeon
processors and platform prices should be roughly equivalent.
With these developments, customers will have even greater
flexibility for customizing 64-bit solutions to match their
specific workload and business requirements.
General Recommendations for
Platform Selection
“Know your applications well, know what resources are
required, and identify where the ‘bottlenecks’ occur.”
– 64-Bit Extensions Complicate Server Selection, 
J. Encjk, A. Butler, G. Weiss, Gartner Research Note,
March 19, 2004.
Enterprise computing solutions are complex, and there will
always be exceptions to general recommendations. With that
caveat, the following rules of thumb provide a useful starting
point for planning migrations and selecting platforms. When in
doubt about the need for 64-bits, consider deploying 64-bit
capable platforms to lay the foundation for migrating if and
when needed.
• Front-end Workloads and General Purpose
Infrastructure Applications—Many front-end applications
do not require 64-bit capabilities and scale very well across
multiple servers. This tends to be true for Web, email,
customer relationship management, and some supply
chain management solutions. Depending on processing
loads and data sets, it may also be true for more demanding
applications, such as digital content creation, mechanical
computer-aided design, and electronic design automation.
In general, unless there are specific workload considerations,
Intel Xeon processor-based systems are likely to provide
the most cost-effective solution in these categories.
• Mid-Tier Workloads—These applications are more varied
in their requirements. Many will benefit from both 64-bit
capabilities and from the migration flexibility of Intel Xeon
processor-based platforms with Intel EM64T. Some will
require the greater capacity and compute power of Itanium
architecture. Software availability and vendor optimizations
will likely be deciding factors for packaged applications. For
custom code, it will be especially important to look closely at
transaction loads, data requirements, growth expectations,
and migration costs. Be aware that the performance of
application infrastructure solutions, such as BEA WebLogic*
Platform, IBM WebSphere*, and Oracle Application Server*,
will impact a wide assortment of applications, and may see
substantial performance gains on 64-bit platforms.
• Data Tier Workloads—Large data sets and heavy pro-
cessing loads are more usual for these types of applications.
Examples include enterprise databases, enterprise resource
planning (ERP), supply chain management (planning),
computer assisted engineering, and business intelligence. 
In general, these applications will perform and scale more
effectively on Intel Itanium 2 processor-based systems and
will also benefit from the enhanced set of RAS features.
Applications currently running on mainframes and RISC-
based systems should be considered prime candidates 
for migration to Itanium architecture.
9
The Power of Parallelism
“Essentially, the design paradigm has shifted at Intel, 
and all the resources we have are dedicated to 
multi-core [processors].”
– Paul Otellini, President and Chief Operating Officer,
Intel Corporationa
64-bit computing is not the only way to increase
application performance. The simultaneous processing
of multiple instructions, otherwise known as parallelism,
is another strategy that is also gaining importance in
both 32-bit and 64-bit environments. There are many
ways to increase parallelism, from Intel® Hyper-Threading
Technology‡, to Explicitly Parallel Instruction Computing
(the foundation of Itanium architecture), to symmetric
multiprocessing (SMP) servers, to clustered architectures
and grid computing. 
Intel will soon add to these options by delivering multi-
core processors that will take per-processor parallelism
to a new level. It will be important to consider these
options as part of the broader picture when evaluating
32-bit versus 64-bit solutions. Here again, software
optimization will be critical, and it will be essential to
understand workloads to determine the best solution 
for any given application. 
a Intel Shoots for Dual Cores, Wireless Profits, John G. Spooner, 
CNET News.com, May 13, 2004.

=== p10 ===
Matching the Platform 
to the Workload: 
High-Performance Computing
on Intel® Architecture
In recent years, the growing price and performance
advantages of COTS (common-off-the-shelf) systems and
components have fueled a shift away from purpose-built
high performance computing (HPC) platforms. In fact, Intel
processors are now used in more than 50% of the world’s
500 most powerful systems, including a 20 teraflop
supercomputer based on Intel Itanium processors that went
from concept to deployment in just 5 months at the
Lawrence Livermore National Laboratory.a
The new Intel Xeon processor with Intel EM64T introduces
additional options for price-sensitive HPC deployments that
can benefit from a 64-bit address space. For example,
Amber (Assisted Model Building with Energy Refinement) 
is a suite about 50 applications that are used to explore
molecular structures and energies. In recent internal tests,
Intel engineers compared the performance of 7 key Amber
applications using the legacy (32-bit) and 64-bit modes of a
platform based on pre-production versions of the Intel Xeon
processor with Intel EM64T. The performance benefits in 
64-bit mode were dramatic, ranging from 20% to 73%, with
an average gain of 64%.b Given the low cost of Intel Xeon
processor-based platforms, these results highlight their value
for scaling the performance of many real-world HPC
applications.
10
0
200
250
300
50
100
150
Top 500 Super
Computers
Adoption of Intel
® Processor-Based Systems for
High-Performance Computing
Intel Xeon™ Processor
Intel Itanium® Processor
June 2000
June 2003
June 2002
June 2001
June 2004
Source: Latest Top500 List, June 2004, www.top500.org
Driven by rapid performance increases, Intel processor-based systems have become the leading choice
for high-performance computing, and now account for more than 50% of the world’s 500 most 
powerful systems.
a See "Thunder – N. America's Fastest Linux Supercomputer, May 13, 2004. Available on the LinuxWorld Web site at: http://www.linuxworld.com/story/44799.htm
b Intel performed internal benchmarking tests on Intel Xeon processor-based systems with Intel EM64T, in a 3.6GHz single cpu configuration, running AMBER
molecular modeling code v.8 distributed as source code (under license) from the University of California. The operating system used was 64-bit Linux.
Application code was compiled with Intel Fortran compilers (LinuxCompiler 8.0 for 32 bit testing; 8.1 for 64 bit testing). Performance was measured on 7
workloads that utilized serial processes.

=== p11 ===
Optimizing ROI for Selected
Enterprise Workloads
“Intel is at the forefront of publishers providing quality
software for cross platform development and
performance enhancement.” 
– Jeff Largiader, Vice President of Marketing, 
Programmer’s Paradise, Inc.
Optimized software can dramatically improve application
performance on any platform, and is all the more important
following a major platform transition, such as the introduction
of Intel EM64T. For these reasons, Intel invests heavily in
software-enabling initiatives that help to deliver the best
possible performance on Intel architecture. Much of this 
work takes place in collaboration with leading independent
software vendors (ISVs). 
Intel works closely with ISVs to select meaningful and
representative workloads, rather than artificial benchmarks, to
ensure that optimization efforts deliver real value in production
environments. Code performance is then profiled on test
systems, bottlenecks are identified and resolved, and both
software and platforms are optimized for best performance.
The goal is a balanced system design in which processor,
cache, bus, memory, and I/O resources are optimized to
efficiently support a wide range of workloads at low cost. 
Intel Software Tools and Developer Programs
“Intel's 32-bit compiler is the gold standard for
optimizing compilers.”16
— Nathan Brookwood, Insight64 Analyst
Intel has been involved in software optimization for decades,
and now has over 2,000 software engineers supporting 
more than a thousand ISVs. In the course of these efforts,
Intel has created a complete set of software optimization
tools—compilers, performance primitives, tuning analyzers,
threading, and clustering tools, etc. These tools are designed
to deliver very deep code optimizations, while integrating
seamlessly with leading development environments. They 
can dramatically improve application performance on Intel
architecture. A variety of resources are also available for
supporting and simplifying 64-bit migrations to Intel Itanium
Architecture and Intel EM64T (see the additional resources
listed at the end of this paper).
11
Intel® EM64T and High-
Performance Workstations 
“...the most demanding jobs ran best on the dual-[Intel]
Xeon processor with its ability to run hyperthreading.”a
From advanced computer-aided design (CAD), to digital
content creation, to sophisticated manufacture and 
test modeling, to high-end visualization and analysis,
today’s engineers, scientists, and designers are dealing
with more complex problems and rapidly growing data
sets. In many cases, they habitually divide complex
problems into smaller, more manageable parts, and then
undertake the time consuming task of integrating the
results. In other cases, they rely on expensive, proprietary
64-bit workstations, and then require a second PC for
productivity applications.
Workstations based on the Intel Xeon™processor with 
Intel EM64T offer an ideal solution to these challenges.
With excellent performance and greatly enhanced memory
addressability, they offer a far more cost-effective
alternative to UNIX workstations for 64-bit applications.
Since they also deliver leading performance for existing 
32-bit applications, they can handle a wide variety of mixed
workloads, including standard productivity applications.
Over the past decade, complex scientific, technical, 
and design applications have thrived on rapid increases
in processor performance. By letting these applications
store more data in main memory, workstations based on
the Intel Xeon processor with Intel EM64T will help fuel
the next decade of progress.
a Workstation Showdown: Xeon vs. Opteron, Wayne Rash, 
Randall C. Kennedy, InfoWorld.com, August 13, 2004.
16 As quoted by Stephen Shankland, in his article, Intel Earns Programmer Tool A Linux Foothold, CNET News.com, August 4, 2004. The full article is available on the
ZDNet Web site at: http://zdnet.com.com/2100-1104-5296761.html

=== p12 ===
17 Internal tests by Intel IT indicate this technology will reduce desk-side and depot repair costs in Intel's environment by 41.5 percent, while reducing the cost of
maintenance contracts and improving employee productivity. Total benefits are conservatively estimated at more than $16M/year. For more information, see Intel®
Active Management Technology Reduces IT Costs with Improved PC Manageability, available at http://www.intel.com/update/contents/it09042.htm.
18 Strategic Platforms—The Shift Continues, R. Fichera, Forrester Research, Inc., June 22, 2004.
19 Hardware Kingpin Intel Beefs Up Software Business, John G. Spooner, Staff Writer, CNET News.com, June 30, 2004.
Keeping the Focus on 
Business Value
“Find the right balance between the best choice of server
for a given application and the number of supportable
platforms maintained in the computing infrastructure.”
– 64-Bit Extensions Complicate Server Selection, 
J. Encjk, A. Butler, and G. Weiss, Gartner Research
Note, March 19, 2004.
IT organizations continue to face intense scrutiny from business
executives regarding new investments, so successful 64-bit
migrations will require attention to business justification as well
as technological considerations. Assessments should include
issues of risk mitigation (including the risk of migrating to 64-
bits as well as the risk inherent in retaining 32-bit solutions),
change management, and transition planning to ensure good
alignment with actual costs and potential impacts.
To be successful, it is best to take a consistent approach across
the enterprise, by classifying your applications and workloads
and developing appropriate criteria for migration based on
business, as well as technical, variables. Understand vendor
roadmaps and compare the cost impact of: 1) retaining 32-bit
applications; 2) a single port to Itanium architecture; 3) a port 
to 64-bits on Intel Xeon processor-based platforms followed,
potentially, by a second round of optimization for Itanium
architecture. To fully understand the issues, implement pilot
programs, with gated costs to evaluate and compare options.
As always, work to standardize your infrastructure solutions, 
to simplify future migrations and reduce operating costs.
In evaluating your options, consider evolving platform costs
and capabilities. Intel is committed to advancing both Itanium
and IA-32 architectures, to provide customers with better
choices and tools for managing escalating IT costs. This
commitment includes ongoing advances in both processor
families, including the integration of critical capabilities that 
will help to improve not only performance, but also power
management, virtualization, security, and platform management.
It also includes ongoing collaboration with industry leaders to
deliver increasingly flexible platforms that are easier and less
costly to deploy and manage. As one example, Intel Active
Management Technology is being integrated into a wide
variety of next-generation platforms, to provide enhanced
asset management and remote troubleshooting for all
business computing systems, from enterprise servers to PCs
and cell phones.17
Moving Away from Expensive and
Inflexible Proprietary Solutions
“... in the future, the balance will alter further and
further in favor of Intel-based platforms for hardware,
and choices for server OS will favor an increase in
market share for Microsoft OS and Linux...” 
– Strategic Platforms—The Shift Continues, R. Fichera,
Forrester Research, Inc., June 22, 2004.
The value of industry-standard computing solutions continues
to drive their wide acceptance as a powerful and cost-effective
alternative to proprietary architectures (Figure 2). Itanium
architecture has extended this value into high-end computing
environments, and Intel EM64T is now filling in the gap,
providing high-volume, cost-effective support for entry-level
and mid-range 64-bit solutions.
This transition can be expected to continue, since the
cumulative investment in industry-standard platforms and
technologies is “at least an order of magnitude greater than
investment in proprietary RISC technology, and the gap will
probably widen over time.”18 The enormous ecosystem of
hardware and software developers drives rapid innovation 
and competitive pricing, producing solutions that continue to
displace expensive and limiting proprietary alternatives. 
It takes a complete ecosystem to drive innovations that fully
address business needs and opportunities. Intel is deeply
involved in virtually all major developments, from processor
and platform innovation, to standards development and
evolving usage models. This broad participation is essential to
continuously increase the business value of Intel architecture.
As noted recently by an industry analyst, “Increasingly, ‘Intel
inside’ means Intel software, as well as hardware, in a host 
of computing devices.”19 It also means a level of value and
investment protection that is unparalleled in the 
computing industry.
Conclusion
By providing 64-bit capabilities at little or no additional cost—
and providing a bridge to the more robust capabilities of
Itanium architecture—the Intel Xeon processor with Intel
EM64T represents an inflection point for the computing
industry. Within a relatively short time, 64-bit capability will
likely be a baseline expectation for virtually all new platform
purchases, and IT organizations will be able to migrate their
applications as needed, while maintaining optimized
performance for 32-bit workloads.
12

=== p13 ===
The challenge for IT organizations will be to maximize the
business value of these 64-bit capabilities, while minimizing
the cost, risk, and disruption caused by software migration. 
To do this, they will need to understand current and future
workload requirements for their key business applications, to
ensure they neither miss critical 64-bit opportunities nor invest
in upgrades for which the benefits do not justify the costs. 
They will also need to develop a consistent enterprise-wide
migration strategy based on business and technical drivers,
and contain operating costs by standardizing on a limited
number of vendors and platform configurations. As a rule of
thumb, Itanium architecture will remain the platform of choice
for business-critical data tier applications, while Intel Xeon
processor-based platforms will deliver better value for scaling
out mid-tier and general purpose applications. 
By making intelligent platform choices, IT organizations can
increase the value of their IT investments. By relying on Intel
architecture, they can be assured of staying in the vanguard
of industry developments, reducing their risk, and taking
advantage of affordable, high-volume platforms for even 
their most demanding applications.
Additional Resources
Intel Developer Services—Products, services, and recom-
mendations for optimizing software performance on Intel
architecture: http://www.intel.com/cd/ids/developer/
asmo-na/eng/index.htm
• Intel Itanium Architecture Resource Center:
http://www.intel.com/cd/ids/developer/asmo-na/eng/
microprocessors/itanium/index.htm
• Intel EM64T Resource Center:
http://www.intel.com/cd/ids/developer/asmo-na/eng/
technologies/64bit/index.htm
• Intel 64-bit Test Drive Web Site:
http://www.intel.com/cd/ids/developer/asmo-na/eng/
microprocessors/itanium/171236.htm
• Intel Software Tools:
http://www.intel.com/software/products/
• Intel Early Access Program: A variety of business,
marketing, and technical resources that can help software
vendors stay at the cutting edge of Intel architecture-based
solutions: http://www.intel.com/ids/eap
Intel Solution Services—For more information about Intel
Solution Services, visit our Web site at http://www.intel.com/
go/intelsolutionservices, or contact us at www.intel.com/info/
intelsolutionservices. To contact us by telephone, call toll free
in the U.S. at 866-268-9812; Europe, Middle East, and Africa
at +44 118 944 7931; Asia Pacific at +852 2844 4555; and
Japan at +81 3 5208 5375.
13
0%
Q1’96
Q1’97
Q1’98
Q1’99
Q1’00
Q1’01
Q1’02
Q1’03
Q1’04
Source: IDC Q1’O4 “Worldwide Server Quarterly Tracker,” June 10, 2004
20%
40%
60%
80%
100%
Other (legacy
UNIX* and 
proprietary)
Microsoft
Windows*
Linux*
Figure 2.  The move away from proprietary, RISC-based servers continues in both 32-bit and 64-bit
environments, as Intel processor-based systems increasingly deliver comparable or better
performance and RAS at a fraction of the cost.

=== p14 ===
Copyright ©2004, Intel Corporation. All Rights Reserved. 
Intel, the Intel logo, Intel Xeon, Intel SpeedStep, and Intel Itanium are trademarks or
registered trademarks of Intel Corporation or its subsidiaries in the United States and
other countries. 
*Other names and brands may be claimed as the property of others. Information
regarding third-party products is provided solely for educational purposes. Intel is not
responsible for the performance or support of third-party products and does not make
any representations or warranties whatsoever regarding quality, reliability, functionality 
or compatibility of these devices or products.
‡Hyper-Threading Technology requires a computer system with an Intel® Xeon™processor,
a chipset and BIOS that utilize this technology, and an operating system that includes
optimizations for this technology. Performance will vary depending on the specific
hardware and software you use. See http://www.intel.com/info/hyperthreading/ for more
information, including details on which processors support HT Technology.
304267-001



---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 2004-09-intel-64bit-tipping-point-b21860 |
| title | The 64-bit Tipping Point: Optimizing Performance, Flexibility, and Value with Intel Itanium Architecture and Intel EM64T |
| author | Intel Corporation |
| date | 2004-09-01 |
| type | white-paper |
| subject_domain | processor-architecture |
| methodology | technology-analysis, vendor-positioning |
| source_file | The-64-bit-Tipping-Point-6.pdf |
| license | CC-BY-4.0 |

### Abstract

Intel's September 2004 white paper positions two complementary 64-bit architectures—Itanium for high-end business-critical applications and Intel Xeon with EM64T for general-purpose computing—as the optimal 64-bit migration path. Citing IDC forecasts of Itanium server market growth from under $1 billion (2003) to $8 billion (2008), and Aberdeen Group's Peter Kastner on Itanium outperforming RISC, the paper argues that EM64T will trigger broad mainstream 64-bit migration while Itanium holds the data-tier niche. BEA WebLogic and SAS case studies illustrate platform selection tradeoffs.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Intel's white paper marks a transitional moment in server computing as x86-64 supplanted both 32-bit x86 and proprietary RISC; also cites Peter Kastner/Aberdeen Group Itanium assessment, providing a cross-reference point. |
| **Relevance** | low | The x86-64 transition is complete and Itanium was discontinued in 2021; the market sizing and vendor positioning are historically interesting but not actionable today. |
| **Prescience** | high | Correctly forecasted x86-64 (EM64T) dominance for general workloads and Itanium's relegation to a high-end niche; 32-bit x86 displacement prediction fully vindicated; Itanium discontinued 2021 confirming the niche-to-obsolete trajectory. |

### Prescience Detail


**Prediction 1:** IDC Itanium server market forecast 2008
- **Claimed:** IDC forecasts Itanium-based server market to grow from less than $1 billion (2003) to more than $8 billion in 2008
- **Year:** 2004
- **Confidence at time:** high

**Prediction 2:** 32-bit x86 displacement prediction
- **Claimed:** IDC: New system shipments based on 32-bit x86 processors will be swept away over time by x86-64 designs
- **Year:** 2004
- **Confidence at time:** high

**Prediction 3:** SOA and Web Services accelerating 64-bit need
- **Claimed:** Rise of Web Services and Service Oriented Architecture (SOA) simplifying integration across businesses and supply chains; high-volume transactions in real-time; driving 64-bit demand
- **Year:** 2004
- **Confidence at time:** high

**Prediction 4:** x86-64 dominance for general workloads
- **Claimed:** EM64T/x86-64 will dominate general-purpose and mainstream enterprise applications; Itanium relegated to high-end business-critical niche
- **Year:** 2004
- **Confidence at time:** high


### Entities Referenced (7)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Intel Corporation | company | active |  |
| SAS Institute Inc. | company | active |  |
| BEA Systems, Inc. | company | dissolved | acquired by Oracle 2008 |
| International Data Corporation (IDC) | firm | active |  |
| Aberdeen Group, Inc. | company | dissolved | acquired by Harte-Hanks 2001 |
| Forrester Research, Inc. | company | active |  |
| Omicronn | company | [DEFERRED] |  |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Intel Xeon Processor with Intel EM64T (Extended Memory 64 Technology) | platform | Intel | current | legacy-evolved |
| Intel Itanium 2 Processor / Itanium Architecture | platform | Intel | current | obsolete |
| Intel x86 32-bit Architecture (IA-32) | platform | Intel | current | legacy |
| x86-64 / AMD64 (64-bit extension of x86) | platform | Intel/AMD | current | active |
| Intel EM64T (Extended Memory 64 Technology) | platform | Intel | current | legacy-evolved |
| IPF — Itanium Processor Family | platform | Intel/HP | current | obsolete |
| Linux Operating System | platform | community | current | active |
| Microsoft Windows (32-bit and 64-bit) | platform | Microsoft | current | active |

### Observation Summary

- Total observations: 23
- By type: expert-opinion: 12, market-data: 4, viability-prediction: 4, actual-outcome: 3
