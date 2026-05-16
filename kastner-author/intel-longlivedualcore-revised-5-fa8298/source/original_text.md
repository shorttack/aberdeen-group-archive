# Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)

> Archived from: Intel-LongLiveDualCore-Revised-5.pdf
> Original publication date: 2004-09-16
> Author: Nathan Brookwood (Insight 64)

---

## Original Document Text

Fall IDF: Megahertz is Dead, Long Live Dual-Core (Revised) 
Page 1 
© 2004, Insight 64 
 
Intel’s Fall Developer Forum (IDF): 
 
Megahertz is Dead, Long Live Dual-Core 
 
Nathan Brookwood 
 
Nathan@Insight64.com 
 
(408)257-5124 
 
September 16, 2004 (Revised) 
 
 
At last week’s semi-annual gathering of Intel’s ecosystem partners, Paul Otellini officially lowered the 
curtain on two decades of ever-increasing clock frequencies as the principal tactic for increasing the 
speed of personal computers and servers. Henceforth, those who need more performance in their 
desktop, mobile and server systems must exploit parallelism (i.e., multiple processors, often on a sin-
gle silicon die), rather than relying on the brute force approach of making the processor’s circuits op-
erate faster and faster. Some may wonder if anyone needs more performance than today’s high-end 
systems deliver. Many users do. Others may wonder whether this means the end of Moore’s law, the 
key driver of the microelectronics revolution that has propelled our economy for the past four decades. 
It does not. Still others may wonder how this shift might impact the positions of the two principal sup-
pliers of x86 processors, Intel and AMD. The two companies remain locked in a bitter dogfight, al-
though Insight 64 believes AMD may have a technology advantage over the next six quarters if it con-
tinues the smooth execution that has marked its recent operations. 
 
Does anyone really need more performance? 
Today’s computer users fall into two broad groups with regard to their performance requirements. The 
first (roughly 70 percent of the population) uses computers for basic productivity applications, internet 
access and e-mail. Even the least expensive systems on the market today can satisfy these users’ 
needs, although some customers may buy pricier systems for their looks or status. The second group 
depends on applications that truly benefit from increased processor performance. Such users now 
spend eighteen hours updating a database, but could generate more revenue if they could finish the 
update in just ten hours. Or they run risk arbitrage calculations that take two minutes, but have only 
one minute to make investment decisions. Or they engage in multi-player games over the internet, 
where the fastest system confers on its owner the same advantage the fastest sailboat gives its owner 
in a yacht race. Or they edit video and produce DVDs, a task that takes at least three hours on today’s 
fastest systems. Improved performance also enables new applications and opens new markets, al-
though the “if we build it they will come” approach has proven problematic as a market driver over the 
past five years. 
 
Is Moore’s Law Dead? 
Many people believe that Moore’s law dictates a doubling of processor performance every two years or 
so. Since much of this additional performance traditionally has come via increases in megahertz, they 
assume that Moore must have had something to say about clock frequency. Strict constructionists 
agree that the enabling 1965 legislation for Moore’s law never mentioned frequency; it only addressed 
transistor density. Moore projected that improved lithography techniques (i.e., the process of transfer-
ring the image of a chip onto a silicon wafer) would allow manufacturers to double the number of 
transistors on a chip of constant size every two years. Moore never specified what chip designers 
should do with that surfeit of transistors. Basic economics dictated that if chip designers could not fig-
ure out a way to add value to their chips (via enhanced performance or function), their employers 
probably deserved to wind down their business. 
 
Until recently, Moore’s law provided one of the few free lunches known to nature. Each new generation 
of process technology offered transistors that were smaller, faster, and used less power than the one 
it replaced. Like all good things, this had to come to an end; with the advent of the 90 nanometer 
generation, chip designers could only get two out of three of these benefits. If they wanted smaller 
and faster transistors, they needed more power. If they wanted smaller, more power efficient transis-
tors, they needed to relax their (transistor) performance requirements. This means that in the future, 
products that depend on architectural techniques (like parallelism) to drive improved performance will 
have inherent advantages over products that rely on brute force (i.e. megahertz) to gain performance. 
 
 
 
 
 


Fall IDF: Megahertz is Dead, Long Live Dual-Core (Revised) 
Page 2 
© 2004, Insight 64 
Are Two Cores Better Than One?  
Parallelism is rapidly becoming the preferred way to increase microprocessor performance, and dual 
core approaches are one of the easiest ways to achieve parallelism. As the chart below illustrates, 
over the past four years, processors based on Intel’s NetBurst architecture have increased in perform-
ance by a factor of 3.2, while maximum power consumption (known as the chip’s “Thermal Design 
Power” or TDP) has increased by a factor of 2.1. On average, each 100MHz increase in clock frequency 
adds 2.5W to the chip’s appetite for power. The fastest P4’s today consume almost 110 Watts. Nobody 
would complain if processor performance was to go up and to the right forever, but increased power 
consumption is a different story. Chips that use more power need bigger, faster and noisier fans. Be-
yond 150 Watts, air cooling becomes problematic and liquid cooling may be required; this adds cost 
and complexity to desktop systems, and should be avoided if at all possible. For offices or datacenters 
with many systems, bringing power into the facility and getting heat out have become important con-
siderations in system deployments. 
 
Not all Intel 90nm processors 
require 
vast 
amounts 
of 
power to deliver competitive 
computational 
performance. 
The latest Pentium M, based 
on the Dothan core, runs at 
2GHz, but needs only 21 
Watts to match the perform-
ance of a 3.2GHz Pentium 4 
that uses 82 Watts. Dothan 
contains 
more 
transistors 
(140 million) than Prescott 
(125 million), but uses only 
one 
fourth 
the 
power. 
Dothan’s designers opted to 
use slightly slower transistors 
than Prescott’s, a decision 
that makes a dramatic differ-
ence in overall power con-
sumption. If Intel’s dual-core 
desktop processors drop their 
clock frequency to 2.5GHz, 
each core will consume ap-
proximately 40 Watts and 
will 
score 
approximately 
1200 on the SPECint test, for 
a combined performance of 
2400 on SPECint at 100 Watts. A single core design that performs at this level would have to operate 
at 4.6GHz, and at that frequency, the chip would consume at least 130 Watts.  
 
The transition to multi-core processors raises few software visible issues. Virtually all applications can 
run on these new processors without modification, but to gain a dual-core performance advantage, 
programs must be (re)structured to run in a multithreaded manner. Many computationally intensive 
applications have already been modified in this way, since software programs cannot distinguish be-
tween multiprocessing (i.e., multiple threads running on two separate processors), HyperThreading 
(i.e., multiple threads running on two logical processors in a single core) and dual-core operation (i.e., 
multiple threads running on separate cores on one chip). Intel has spent many millions of dollars over 
the past three years to assist software developers in their efforts to adapt their programs for Hyper-
Threaded execution, and all of those investments apply directly to dual-core systems as well. All the 
major x86-based operating systems (e.g., Windows, Linux and UNIX) already support multiprocessor 
configurations, so there’s no need for application developers to sit on their hands while the OS devel-
opers get their acts together. Unlike the move to 64-bit x86 computing, which remains on hold pend-
ing the final release of Windows for 64-bit Extended x86 Systems, there’s little Microsoft can do (other 
than raise the prices it charges for multi-processor versions of its operating systems) to slow the mi-
gration to dual-core. 
0
200
400
600
800
1000
1200
1400
1600
1800
1.0
1.5
2.0
2.5
3.0
3.5
4.0
CPU Frequency (GHz)
SPECint Score
0
20
40
60
80
100
120
140
160
180
Max Power (Watts)
        P4 Power (TDP)
Centrino Power (TDP)
Centrino 
Performance
P4
Performance
So urce: SP EC.o rg (P erfo rmance),  Intel (P o wer)


Fall IDF: Megahertz is Dead, Long Live Dual-Core (Revised) 
Page 3 
© 2004, Insight 64 
All Dual-Core Processors Are Not Created Equal 
Unlike a rising tide, dual-core technology will not lift all boats equally. Performance of these new chips 
depends both on the cores themselves, and the techniques used to meld two cores into a single die. 
These techniques can vary from the elegant (shared level three caches and sophisticated algorithms 
that assure each core gets equal access to external buses) to the inelegant (placing two single-core 
processors on the same die, and then connecting all the input and output signals coming from the bus 
to each on-die processor in parallel). Architectural elegance does not always correlate with superior 
performance, but it often helps in this regard. 
 
Dual-core approaches are not new to the processor world. IBM delivered its dual-core Power 4-based 
systems three years ago and launched a second generation dual-core system this past spring. Sun 
and HP began deliveries of their dual-core RISC systems in February. AMD suggested that dual-core 
would be part of its 64-bit line when it first unveiled the architecture in 1999, and demonstrated its 
first working dual-core chip a few weeks ago. Intel put dual-core Itanium and Xeon processors on its 
roadmaps a year ago, and demonstrated its dual-core Itanium (Montecito) at IDF last week. All of 
these designs feature a system interface of one form or another that ties directly to the chip’s external 
interfaces, and relays the information from those interfaces to or from the intended core. Both AMD 
and IBM started with dual-core chip designs (Hammer and Power 4, respectively), although AMD had 
room for only one core on its initial 130nm Opteron. The shaded areas in the AMD block diagram 
below indicate the functional elements already in place in AMD’s single-core Opteron. AMD needed 
only to replicate the two boxes labeled “CPU0” and “1MB L2 Cache,” and tie the new copies into inputs 
that had previously gone unused on its “System Request Interface” unit. A project of this complexity 
could probably have been completed by a few graduate students during a one semester course, 
although we suspect AMD assigned a slightly larger and more mature staff to this task. Sun and Intel, 
on the other hand, took the approach of adapting their single core CPUs (UltraSPARC III and Madison) 
for dual-core operation. They had a more complex design task, since they needed first to separate 
those portions of their designs that interfaced with the external system from those parts that 
interfaced with the single core, and then to add arbitration logic that allowed both cores to share that 
external interface. Either of these projects could have qualified as a PhD thesis at most major 
universities. 
 
 
Intel’s Montecito Design 
Source: Intel 
AMD’s Dual-Core Opteron Design 
Source: AMD 
 
At last week’s Developer Forum, Intel was uncharacteristically silent about the design approach it has 
taken with regard to its forthcoming dual-core Pentium and Xeon processors, due to hit the market in 
the second half of 2005. To meet this schedule, Intel’s chip designers must be close to handing their 
design off to manufacturing, a milestone known in the industry as “taping out.” (Given Intel’s newly 
rediscovered religion with regard to meeting development schedules, we sincerely hope the designers 
can and do meet the externally declared date.) This means Intel knows what its design looks like, but 
doesn’t want to talk about it in public.  
 


Fall IDF: Megahertz is Dead, Long Live Dual-Core (Revised) 
Page 4 
© 2004, Insight 64 
Industry rumors abound that the company’s initial dual-core chips may be based on the inelegant ap-
proach of collocating two single core processors on a single piece of silicon. Such an approach would 
be feasible, given Intel’s use of shared frontside buses to link discrete CPUs together in dual-processor 
and multiprocessor configurations. A dual-core chip would then appear to the system’s core logic, and 
to the software, exactly like two discrete single core-processors. Although there’s nothing fundamen-
tally wrong with such an approach, designers would have to overcome at least one tricky physics 
problem. If Intel connects both on-die cores directly to the external bus that links processors to the 
system’s core logic, then that bus will see the circuit capacitance of two CPUs, rather than one. Two 
socket systems (the sweet spot of the x86 server market) will see the capacitance of four CPUs, and 
four socket systems will behave electrically as if the bus was loaded with eight CPUs. Unfortunately, 
there’s a direct correlation between the number of capacitive loads on a shared bus and the frequency 
at which that bus can operate. Today’s DP systems have three bus loads (the north bridge and two 
single-core CPUs), and their buses operate at 800MHz. Today’s four-way systems have five bus loads 
(the north bridge and four single-core CPUs), and can only operate at 400MHz. Under this scenario, a 
two-socket, four core Xeon system would have only enough bus bandwidth to accommodate a total of 
3.2GB/second of memory and I/O traffic. This would be a step down from Intel’s current two-socket 
systems that provide 6.4GB/second of bus bandwidth, and would place Intel at a severe competitive 
disadvantage to AMD, which can deliver up to 13.2GB/second of memory and I/O bandwidth per proc-
essor in two-socket and four-socket configurations now and with its dual-core platforms. We certainly 
hope Intel has not gone down this path, or if they have, that they have a solution to this bus loading 
problem. 
 
What Was Under the Hood in Last Week’s Dual-Core Demo? 
At last week’s Developer Forum, Intel demonstrated how its Digital Office vision might enable three 
workers in different locations to collaborate to solve a complicated problem. (You can watch this demo 
on the web at http://developer.intel.com/idf/us/fall2004/daily/webcast.htm. It’s about 28 minutes into 
the video for the September 8th keynote.) One of the workers (“Jason”) had to juggle several com-
pute-intensive tasks on his system, but the work flowed easily without the sorts of fits and starts that 
would plague many contemporary systems. At the conclusion of the demo, Bill Siu, the General Man-
ager of Intel’s Desktop Platforms Group, casually noted that “Jason was using a dual-core system on a 
915 [i.e., Grantsdale] platform.” When asked about it later during a Q&A session, Siu smiled coyly, 
and added only that the system used “an engineering prototype” of a dual core processor with “real 
silicon.” This begs the question of what was really inside the box. Let’s explore the possibilities, going 
from least to most likely. 
 
The least likely scenario is that the demo used the first silicon samples of the dual-core product 
planned for release next year. Intel did demo the first silicon for its dual-core Itanium, and AMD had 
just demonstrated the first silicon for its Opteron processor the week prior to IDF. We believe that if 
Intel actually had achieved this milestone, it would have trumpeted the news far more loudly and 
widely; their awesome PR machine would have made sure everyone on the planet was aware of this 
accomplishment. So we discount this theory completely. 
 
It’s a bit more likely that Intel crammed two of its current Pentium chips into a single package that 
could be plugged into the socket of a 915 motherboard. (This is known as a multi-chip package (MCP), 
and has been used for years in certain applications.) The standard P4 package measures about 30mm 
on a side, and could conceivably hold many discrete processors that only measure about 11mm on a 
side. Intel wouldn’t do this just for an IDF demo, but the resulting MCP might be useful for evaluating 
dual-core platforms, especially if the initial dual-core design follows the scheme we outlined above. 
The system would certainly be consistent with Siu’s claims of “dual core,” “915,” and “real silicon.” 
 
It’s even more likely that Intel merely designed a dual-processor motherboard around its 915 chipset. 
The 915 is normally used only in uniprocessor designs, but there’s no reason why engineers inside 
Intel couldn’t circumvent the restrictions that prevent Intel’s customers from using the 915 in DP 
configurations. Designing a unique motherboard is clearly less expensive and takes less time than 
creating a multi-chip package, and the resulting system would come close to replicating the 
performance of the eventual dual-core product. Like the MCP scenario, this system would fit with Siu’s 
claims of “dual core,” “915,” and “real silicon.” 
 
In any event, we are merely outlining the options. We leave it to our readers to decide which version 
they prefer. 


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | intel-longlivedualcore-revised-5-fa8298 |
| title | Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised) |
| author | Nathan Brookwood (Insight 64) |
| date | 2004-09-16 |
| type | market-study |
| subject_domain | microprocessors/multicore-transition |
| methodology | industry-analysis, competitive-profiling, expert-opinion |
| source_file | Intel-LongLiveDualCore-Revised-5.pdf |
| license | CC-BY-4.0 |

### Abstract

Insight 64 analyst report by Nathan Brookwood on Intel Fall 2004 IDF. Paul Otellini officially closed two decades of MHz-driven CPU scaling and announced the shift to multi-core parallelism. Analyzes the NetBurst power/performance trend, Pentium M Dothan (2GHz/21W, 140M transistors) versus Prescott (3.2GHz/82W, 125M) as exemplars of architecture over brute-force frequency, and the competitive bus-bandwidth disadvantage (3.2GB/s versus AMD's 13.2GB/s) if Intel used an inelegant dual-core design. Preserved in the Kastner archive as external reference material.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First-class contemporaneous analyst interpretation of the industry-defining 2004 pivot from frequency scaling to multi-core parallelism. Brookwood's framing ('Megahertz is Dead, Long Live Dual-Core') became a widely adopted shorthand for the transition. |
| **Relevance** | medium | Technical detail is historical, but the architectural lessons (parallelism over frequency, power/thermal ceilings, bus capacitance in multi-CPU designs) remain foundational for modern CPU and GPU design. |
| **Prescience** | high | Predictions proved highly accurate: multi-core became universal 2005-2010, AMD's bandwidth advantage held for ~18 months, and Intel's Core microarchitecture (2006) confirmed the design-over-frequency thesis. |

### Prescience Detail


**Prediction 1:** intel-dual-core-projection
- **Claimed:** Projection: Intel dual-core desktop at 2.5GHz per core @ 40W each → combined ~2400 SPECint at 100W. A single-core equivalent would need 4.6GHz and 130W+.
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 1:** intel-dual-core-actual
- **Result:** Intel's first-generation dual-core (Pentium D/Paxville) delivered disappointing performance-per-watt. Pentium D ran hot and power-inefficient under 90nm process. Core 2 Duo (Conroe/Merom, July 2006) delivered the significant performance-per-watt improvement. The prediction that dual-core would bring meaningful efficiency gains was validated by Core 2, though the first-gen Pentium D was inefficient.
- **Confidence:** partially-verified
- **Notes:** Verify Pentium D / Core Duo 2005-2006 actual performance-per-watt. | Performance-per-watt validation came with Core 2 Duo (July 2006), not first-gen Pentium D (2005). Source: https://phys.org/news/2006-05-intel-core-microarchitecture-energy-efficiency.html

**Prediction 2:** bus-capacitance-risk
- **Claimed:** Physics concern: if Intel connects both on-die cores to the external bus directly, a two-socket four-core Xeon sees capacitance of 4 CPUs and a four-socket eight-core system sees 8 CPUs. Today's DP (3 loads) runs at 800MHz; 4-way (5 loads) runs at 400MHz. Two-socket four-core Xeon may see only 3.2GB/s bus bandwidth — step down from current 6.4GB/s; AMD can deliver 13.2GB/s.
- **Year:** 2004
- **Confidence at time:** high

**Actual Outcome 2:** intel-dual-core-actual
- **Result:** Intel's first-generation dual-core (Pentium D/Paxville) delivered disappointing performance-per-watt. Pentium D ran hot and power-inefficient under 90nm process. Core 2 Duo (Conroe/Merom, July 2006) delivered the significant performance-per-watt improvement. The prediction that dual-core would bring meaningful efficiency gains was validated by Core 2, though the first-gen Pentium D was inefficient.
- **Confidence:** partially-verified
- **Notes:** Verify Pentium D / Core Duo 2005-2006 actual performance-per-watt. | Performance-per-watt validation came with Core 2 Duo (July 2006), not first-gen Pentium D (2005). Source: https://phys.org/news/2006-05-intel-core-microarchitecture-energy-efficiency.html


### Entities Referenced (12)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Nathan Brookwood | person | active |  |
| Insight 64 | firm | active |  |
| Intel Corporation | company | active |  |
| Advanced Micro Devices (AMD) | company | active |  |
| Paul Otellini | person | deceased |  |
| Bill Siu | person | unknown |  |
| IBM | company | active |  |
| Sun Microsystems | company | acquired | Oracle (2010) |
| Hewlett-Packard | company | active |  |
| Microsoft Corporation | company | active |  |
| PCI Special Interest Group | institution | active |  |
| Gordon Moore | person | deceased |  |

### Technologies Referenced (13)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Intel NetBurst Architecture | platform | Intel | mature | obsolete |
| Intel Pentium 4 Prescott | platform | Intel | mature | obsolete |
| Intel Pentium M Dothan | platform | Intel | mature | obsolete |
| Intel Itanium Montecito (dual-core) | platform | Intel | emerging | obsolete |
| Intel Xeon (dual-processor) | platform | Intel | mature | active |
| Intel 915 (Grantsdale) chipset | platform | Intel | emerging | obsolete |
| AMD Opteron | platform | AMD | emerging | obsolete |
| AMD Hammer (K8) architecture | platform | AMD | emerging | obsolete |
| IBM POWER4 | platform | IBM | mature | obsolete |
| Sun UltraSPARC III (dual-core) | platform | Sun | mature | obsolete |
| Intel HyperThreading Technology | platform | Intel | emerging | active |
| PCI Express (PCI-E) | protocol | PCI-SIG | emerging | active |
| Moore's Law | framework | Industry | mature | mature |

### Observation Summary

- Total observations: 18
- By type: expert-opinion: 10, metric-value: 2, viability-prediction: 2, actual-outcome: 2, strategy-classification: 1, framework-factor: 1
