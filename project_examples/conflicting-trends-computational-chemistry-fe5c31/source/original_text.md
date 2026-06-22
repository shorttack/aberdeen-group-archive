# Conflicting Trends In Computational Chemistry

> Archived from: CompChem.pdf
> Original publication date: 1989-01
> Author: Charles T. Casale

---

## Original Document Text



--- Page 1 ---

^he
Charles


--- Page 2 ---



--- Page 3 ---

Conflicting
Trends In
Computational
Chemistry
Charles T. Casale
Aberdeen Group, Inc.
92 State Street
Boston, Massachusetts 02109
(617) 723-7890
May 1989


--- Page 4 ---



--- Page 5 ---

Aberdeen Group
Aberdeen Group is a Boston-based, internationally recognized computer 
consulting and research organization.
Aberdeen Group performs specific projects for a select group of domestic 
and international clients requiring strategic and tactical advice and prag­
matic, experience-based action plans. Assignments range from strategic 
audits and implementation plans to corporate and product positioning to 
in-depth market, acquisition/divestiture, and feasibility studies to 
benchmarking verification. In carrying out its assignments, Aberdeen uses 
a proprietary, comprehensive analytical framework providing fresh insight 
into the complex future of computing.
Aberdeen's principals — Charles T. Casale, Peter S. Kastner and John R. 
Logan — are recognized industry figures with over 70 years of combined 
high-tech industry and financial community experience among them. 
They are quoted extensively in industry and business publications.
In addition to client-related research and consulting, Aberdeen publishes 
several periodicals — Viewpoints — summarizing its analysis and research 
findings. Executive, Product, Market, and Technology Viewpoints analyze 
their respective topics for executives and practitioners.
Viewpoints are published monthly for Aberdeen clients and other execu­
tives; they are not available on a subscription basis. Aberdeen has 
reprinted numerous of its Viewpoints at client request for reasonable fees.
Aberdeen also publishes in-depth market studies of topical interest which 
are sold individually. Current reports include Conflicting Trends In Com­
putational Chemistry and Transaction Processing: Into the 1990s.
Copyright 1989 Aberdeen Group, Inc., Boston, Massachussetts
AberdeenGroup i


--- Page 6 ---



--- Page 7 ---

Aberdeen Group
Aberdeen Group is a Boston-based, internationally recognized computer 
consulting and research organization.
Aberdeen Group performs specific projects for a select group of domestic 
and international clients requiring strategic and tactical advice and prag­
matic, experience-based action plans. Assignments range from strategic 
audits and implementation plans to corporate and product positioning to 
in-depth market, acquisition/divestiture, and feasibility studies to 
benchmarking verification. In carrying out its assignments, Aberdeen uses 
a proprietary, comprehensive analytical framework providing fresh insight 
into the complex future of computing.
Aberdeen's principals — Charles T. Casale, Peter S. Kastner and John R. 
Logan — are recognized industry figures with over 70 years of combined 
high-tech industry and financial community experience among them. 
They are quoted extensively in industry and business publications.
In addition to client-related research and consulting, Aberdeen publishes 
several periodicals — Viewpoints — summarizing its analysis and research 
findings. Executive, Product, Market, and Technology Viewpoints analyze 
their respective topics for executives and practitioners.
Viewpoints are published monthly for Aberdeen clients and other execu­
tives; they are not available on a subscription basis. Aberdeen has 
reprinted numerous of its Viewpoints at client request for reasonable fees.
Aberdeen also publishes in-depth market studies of topical interest which 
are sold individually. Current reports include Conflicting Trends In Com­
putational Chemistry and Transaction Processing: Into the 1990s.
Copyright 1989 Aberdeen Group, Inc., Boston, Massachussetts
AberdeenGroup i


--- Page 8 ---

Charles T. Casale
Charles T. Casale is President and co-founder of Aberdeen Group, Inc.
Mr. Casale is a business executive with a diversified 33-year background in 
corporate development, strategy, finance, marketing, communications, 
and international operations. He is also a securities analyst.
Mr. Casale's operational experience includes being a founding officer of 
three high-technology companies (Taxon; Encore Computer; DQ 
Securities), architect of a major computer system (the CDC 3600) and 
director of corporate development at Prime Computer. He began his 
career as a large-scale computer systems architect after earning a BSEE. 
He is a Chartered Financial Analyst, and holds a basic computer patent.
Mr. Casale's professional affiliations include the ACM; the IEEE, where he 
is a senior member; the National Investor Relations Institute, where he 
has achieved national honors; The Institute for Chartered Financial 
Analysts; and the New York Society of Securities Analysts.
Information contained in this publication is based on the best available sources, 
but its accuracy cannot be guaranteed. Opinions reflect judgement at the time 
and are subject to change without notice. Unless otherwise noted, the entire 
contents of this publication are copyrighted by Aberdeen Group, Inc., and may 
not be reproduced, stored in a retrieval system, or retransmitted in whole or in 
part without express written permission.
The trademarks and registered trademarks of the corporations mentioned in 
this publication, including those of Alliant Computer Systems Corporation, 
Apple Computer, Inc., Apollo Computer Inc., Ardent Computer Corp., Bio- 
Design, Inc., BIOSYM Technologies, Inc., Chemical Design Ltd, Convex Com­
puter Corporation, Cray Research, Inc., Digital Equipment Corporation, Evans & 
Sutherland Computer Corporation, FPS Computing, Inc., International Business 
Machines Corporation, Molecular Design Limited, Multiflow Computer, Inc., 
Polygen Corporation, Silicon Graphics, Inc., Star Technologies, Inc., Stellar Com­
puter Inc., Sun Microsystems, Inc., Tripos Associates, Inc., and others, are the 
property of their respective holders.
AberdeenGroup ii


--- Page 9 ---

Conflicting Trends In
Computational Chemistry
TABLE OF CONTENTS
Chapter 1 Executive Summary
1
Chapter 2 - What Is Computational Chemistry
7
Chapter 3 - Market Size and Growth
17
Chapter 4 - 
Computational Chemistry Applications
25
Chapter 5 - User Profile: The Computational Chemist
29
Chapter 6 - Computational Chemistry Software Suppliers
33
BioDesign, Inc.
37
BIOSYM Technologies, Inc.
40
Chemical Design Ltd
44
Molecular Design Limited
47
Polygon Corporation
50
Quantum Chemistry Program Exchange
53
Tripos Associates, Inc.
54
Chapter 7 - Computational Chemistry Hardware Suppliers
56
Alliant Computer Systems Corporation
58
Apollo Computer, Inc.
61
Ardent Computer Corp.
64
Convex Computer Corporation
66
Cray Research, Inc.
69
Digital Equipment Corporation
72
Evans & Sutherland Computer Corporation
75
FPS Computing, Inc.
77
International Business Machines Corporation
79
Multiflow Computer, Inc.
82
Silicon Graphics, Inc.
85
Star Technologies, Inc.
88
Stellar Computer Inc.
91
Appendix A - The Chemical Industry
93
Appendix B - Science Issues
105
Appendix C - Investment Issues
110
AberdeenGroup iii


--- Page 10 ---

Appendix D — The Drug Development Process 
Appendix E - The Roles of Digital, IBM, and Cray 
Appendix F - Spoke-Node-Ring - The New Topology
117
122
147
AberdeenGroup iv


--- Page 11 ---

Conflicting Trends In
Computational Chemistry
1-1
Growth of Computational Chemistry Market
2
2-1
Changing Scientific Methodology
8
2-2
Chemistry Discovery and Development Process
9
2-3
Components of Computational Chemistry
10
2-4
Computational Chemistry Methods and Platforms
12
2-5
Computational Chemistry Platforms
13
3-1
Computational Chemistry Estimated Revenues
17
3-2
Computational Chemistry Market Mechanism
18
3-3
1987 Market Shares - Molecular Modeling Suppliers
20
4-2 
Technological Advancement 
27
3-4
1988 Market Shares - Molecular Modeling Suppliers
21
3-5
1988 Hardware Market Shares - Equipment Type
23
4-1
Polymer Development Process
26
5-1 
Graduate Degrees in Chemistry 
32
A-1 
Flow of Chemicals 
94
A-3 
1989 U. S. Chemical Shipments by Usage 
96
A-2 
Chemical View of Industry 
95
A-4
1988 U.S. Chemical Shipments by Type
97
A-5
1988 U.S. Inorganic Chemical Shipments
98
A-6
1988 U.S. Organic Chemical Shipments
99
A-7
1988 U.S. Organic Plastics Shipments
100
A-8
Accelerating Rate of New Chemical Discovery
104
B-1
State of Chemistry Knowledge
108
D-1
Drug Discovery and Development Process
118
E-1
Developmental Stage - 1983-87
123
E-2
Cheaper Computing and Databases - 1984-89
124
E-3
Graphics Intensity - 1987-90
125
E-4
Industrial Strength Computing - 1990-93
126
E-5
Competing Enterprise-Wide Ideologies
128
AberdeenGroup v


--- Page 12 ---

E-6
Spoke-Node-Ring Topology
129
E-7
Digital's System Topology
131
E-8
Digital's Integrated Laboratory Automation Topology
134
E-9
Digital's Scientific Visualization Model
135
E-10
IBM's Computer Chemistry Connectivity
138
E-11
IBM's Computer Chemistry System Approach
139
E-12
IBM's Scientific Computing Support Structure
140
E-13
Cray Computing Topology
144
F-1
Forces Driving Spoke-Node-Ring
150
AberdeenGroup vi


--- Page 13 ---

Conflicting Trends In
Computational Chemistry
PREFACE
CONFLICTING, COMPLEX TRENDS
Computational chemistry is currently a small field, relative both to its bil­
lion-dollar potential and to the current level of general interest.
During Aberdeen's extensive study of computational chemistry, we visited 
and interviewed dozens of people, and found that with rare exceptions, 
each participant had a view of computational chemistry that was in conflict 
with virtually every other participants' view. And, we found that the 
market, business, and technical trends within computational chemistry are 
extremely complex, overlap, and often conflict with each other.
Further, because the field is so new (and technically complex), the depth 
and breadth of understanding of interested parties ranges widely — from 
highly-trained, computational chemistry-practicing Ph.D. chemists to cor­
porate executives who, according to leading users, "get their science from 
the Wall Street Journal," and to seasoned but chemistry-deficient hardware 
producers. Also included in the range are chemistry-shy operating execu­
tives at some molecular modeling software producers, opportunistically- 
motivated venture capitalists, and nontechnical journalists.
To address both the issue of complexity and the wide range of readership, 
we have organized the report at three complementary levels.
Three-Level Approach
At the highest level, we identify the many trends and show where they over­
lap and conflict. This is presented in Chapter 1, Executive Summary.
At the second level, in four brief chapters (Chapters 2 through 5), we 
review and analyze all the major issues. General readers and non-decision- 
makers need not read beyond this level. We follow this with individual 
analyses of 20 computational chemistry enterprises: seven software sup­
pliers (Chapter 6) and 13 hardware producers (Chapter 7). The introduc­
tory pages to Chapters 6 and 7 are of general interest, while few readers 
will be concerned with all the company profiles.
At the third level, we present detailed supporting analyses in the form of 
six appendices. Each appendix covers a specific topic, as described in the 
next section.
AberdeenGroup vii


--- Page 14 ---

Chapter Overview
Following the Executive Summary, we summarize in Chapter 2 what com­
putational chemistry is — excluding the hyperbole typically found in cur­
rent survey articles and reports. Our conclusion is that while 
computational chemistry is an exciting field, it is neither a "sure thing," 
nor about to "revolutionize chemistry" by tomorrow afternoon.
Chapter 3 succinctly summarizes basic market figures and facts, concentrat­
ing on molecular modeling software suppliers and computer manufac­
turers. For detailed supporting analyses, three appendices are relevant: 
The ultimate consumers and industrial beneficiaries of computational 
chemistry are the worldwide chemical industries; statistical data is 
presented in Appendix A, The Chemical Industry. A number of knotty 
scientific issues are lost in much of the fanfare over computational 
chemistry, which we analyze in Appendix B, Science Issues. A third 
market issue relates to funding the rapid growth of computational 
chemistry. We analyze two competing investment models in Appendix C, 
Investment Issues.
In Chapter 4 we review major computational chemistry applications, cur­
rently dominated by pharmaceuticals ("drugs" in the trade). A more 
detailed discussion of the drug development process can be found in Ap­
pendix D, The Drug Development Process.
The world's approximately 2,000 computational chemists play the crucial 
role in development of the field, and we profile them in Chapter 5 based 
upon extensive field and telephone interviews.
Chapter 6 first surveys the collective product emphasis of the molecular 
modeling software suppliers, and is followed by detailed reviews of each 
supplier. This chapter is of particular relevance to decision makers. Here 
we profile corporate background and statistics, technical source of new 
ideas, product approach, products and pricing, computer hardware 
partners, and Aberdeen's assessment of the supplier. Chapter 7 is a com­
panion to Chapter 6, but analyzes hardware suppliers.
Three major manufacturers — Digital Equipment, IBM and Cray Research — 
are quietly, expensively, and with firm determination, launching plans to 
permanently win the hearts and minds of the entire scientific computing 
community at each other's expense. Accordingly, we include in Appendix 
E an expansive analysis of their ambitions. However, major enterprises 
are adopting a new computing paradigm which does not mesh exactly with 
any of the suppliers' plans. Called Spoke-Node-Ring (SNR), we summarize 
its usage and implications in Appendix F.
^berdeenGroup viii


--- Page 15 ---

Conflicting Trends In
Computational Chemistry
CHAPTER!
EXECUTIVE SUMMARY
Leverage
For such a relatively small field — 1988 combined software and hardware 
revenues of $237 million — computational chemistry has generated tremen­
dous excitement, enthusiasm, and expectations. The commercial reasons 
can be summed up in a single word: Leverage.
The world's chemical and allied industries annually invest hundreds of mil­
lions of dollars, deutschemarks, francs, yen, and other currencies in an at­
tempt to discover and develop new products using time-consuming, 
labor-intensive, repetitious methods little changed from the 19th Century. 
That is the nature of chemical discovery. If and when computers can 
reduce those efforts by even a few percentage points, the payoff will be 
measured in hundreds of millions and even billions of dollars. Equally, if 
not more importantly, if and when computers can assist in discovering and 
developing new chemicals significantly more quickly than using existing 
methods, the developer has a nearly insuperable market lead and the op­
portunity, through patents, for monopoly profits.
That's what's driving computational chemistry commercially, worldwide. 
Equally important are the scientific driving forces.
New Academic Frontiers
Independent of commercial benefits, computational chemistry is in the 
vanguard of modern science — new discoveries in pharmaceuticals, semi­
conductors, biologicals, superconductors, and industrial materials and 
processes are beginning to be delivered through computational chemistry. 
Even if there were no commercial market for the gains of computational 
chemistry, academics would continue pursuing the field just as relentlessly 
— excitement is high. Science is being made, Nobel Prizes are to be won, 
and international honor is at stake.
Size, Shape, Direction, and Growth
To quantify the opportunity for those supplying computational chemistry 
tools, in 1988, five molecular modeling companies had total revenues of 
approximately $27 million, up 65 percent from 1987. Leveraging these
AberdeenGroup 1


--- Page 16 ---

Conflicting Trends In
Computational Chemistry
Long-Term Hardware Segment Outlook
The overall computational chemistry hardware market is far more sensi­
tive to users' budgetary constraints than to variations among individual 
software offerings, because computational chemistry, in the final analysis, 
is a computationally intensive activity. Price/performance is increasingly a 
major purchasing issue, and users at any one time have the option to 
choose among shared supercomputers, powerful workstations, and 
departmental minisupercomputers.
However, there will be no consistent trend in which type of computing 
vehicle will provide the best value — Aberdeen expects the computer in­
dustry to continue its 40-year pattern of computing momentum shifting 
noisily among shared large systems, single-user smaller systems, and 
departmental systems.
Exhibit 3-5: 1988 Hardware Market Shares — Equipment Type
Minisupers 25.6%
Mainframes 4.0%
Superminis 16.7%
Supers 7.1%
Other 5.2%
Workstations 41.4%
$210 Total Revenues
Source: 
Aberdeen Group
AberdeeiiGroup 23


--- Page 17 ---

Aberdeen expects the revenue mix among local-compute servers, central- 
site computers, and workstations to vary substantially from year to year, 
with each segment capturing 15 percent to 40 percent of overall hardware 
sales in any given year. Aberdeen expects aggregate hardware sales in 
computational chemistry to range even more widely than software sales, 
with growth rates in individual years varying as much as 10 or more per­
centage points around a 35 percent average.
AberdeenGroup 24


--- Page 18 ---

Conflicting Trends In
Computational Chemistry
COMPUTATIONAL CHEMISTRY APPLICATIONS
Drug design has been the principle focus of all computational chemistry 
companies, even though the projected payoff period for drug companies 
is typically a decade. Major drug companies are now in their second 
round of equipment and software usage, expanding beyond a few dozen 
very early adopters to about 350 innovators.
Why Pursue Drugs?
The simplest view of why so many are chasing such an elusive goal is 
summed up in legendary bank robber Willie Sutton's apocryphal remark, 
"Because that's where the money is!"
The economic rationale for drug companies to use computational 
chemistry is based on the CAD/CAM model of computational chemistry. 
(See Appendix C, Investment Issues.) With some $16 billion invested in 
R&D each year by the drug industry as a whole, 1) potential cost reduc­
tions are enormous; 2) labor displacement is attractive; and 3) time-to- 
market factors are highly appealing. (See Appendix D, Drug Development 
Process.)
However, these three promised benefits, while accepted in principle by vir­
tually all who are computational chemistry practitioners, are also viewed 
as difficult to quantify and heavily oversold.
A fourth promised benefit is obtaining otherwise-unobtainable new 
products. It has not been generally realized, although genetic engineering 
companies have had some modest success.
A fifth promised benefit — better science — has seen polarized results. Posi­
tively, most researchers say that they are indeed better scientists and have 
gained valuable insights through computational chemistry. At the opposite 
end, these same people are increasingly uneasy that computers are racing 
far ahead of underlying scientific theories, leading to potential fiascoes. In 
a management push for quicker results in face of industry consolidation, 
drug industry computational chemistry users are increasingly nervous.
AberdeenGroup 25


--- Page 19 ---

More Recent Applications — Polymers
In the search for new markets beyond the drug industry, polymers top the 
list. Tires, paints, basic chemicals (and many chemicals that are not 
biologicals) are typically polymers (both inorganic and organic), as are 
semiconductors and high-temperature superconducting materials.
Polymer chemistry is difficult because there are so many more possible 
combinations of chemical elements with which to experiment. Whereas 
biochemicals deal with organic molecules — based upon atoms of 
hydrogen, oxygen, nitrogen, and carbon — inorganics deal with the entire 
'periodic table of 108 known atoms.
The polymer discovery-to-rollout process differs from drugs in a number 
of ways and with differing economics. No FDA trials are required, which 
greatly compresses the time from discovery to rollout. Toxicity testing is 
less time consuming and far less expensive. Fewer numbers of experimen­
tal molecules are required, but each variant can cost many times more 
than in drug experimentation. Typically, the process is composed of four 
stages, as illustrated in Exhibit 4-1.
Each stage typically costs ten times more than the prior stage, hence the 
great premium placed on improving the odds of choosing which ex­
perimental chemicals to build during the pilot stage.
The Computational Chemistry Frontier — Materials Applications
If drugs are where the money is, and polymers are the next potential ap­
plications wave, then new materials are the technological frontier and a 
potential source of new industries, not just new products. Materials have 
been worked on computationally, but the chemistry is not as well ad-
Exhibit: 4-1: Polymer Development Process
Piloting
Scaling 
Up
Market 
Study
Discovery
Source: 
AberdeenGroup
AberdeenGroup 26


--- Page 20 ---

Conflicting Trends In
Computational Chemistry
vanced, sending chemists back to heavy-duty ab initio methods before they 
become confident in less computationally intensive methods.
At any stage in technological development, materials are a major factor 
limiting further growth. The electronics industry had peaked out in the 
1950s, not from lack of ideas or demand, but because the materials avail­
able (vacuum tubes) could not be advanced any further. The same has oc­
curred in aircraft design and other fields. Exhibit 4-2 shows the iterative 
process of technological advancement and the role of materials.
In automotive engine design, for example, engineers are bumping into the 
heat dissipation limits of traditional metals, and are looking to ceramics for 
developing more efficient engines. In the more traditional area of sheet - 
metal forming, complex curvatures are pushing at the edge of structural in­
tegrity, and computational chemistry is supplementing cut-and-try 
methods.
In semiconductors, surfaces are near their limits for conventional lithog­
raphy techniques, and computational chemistry is being used to improve 
them. Beyond process and materials improvements, computational
Exhibit 4-2: Technological Advancement
Source:
Theory
Production
Scientific 
discovery
Appiied 
enginering
Material & 
process 
limits
AberdeeiiGroup 27


--- Page 21 ---

chemistry is being used to explore quantum effects that, if successful, will 
extend the life of semiconductor technology 10 to 15 years beyond current 
limits.
The newly discovered class of low-temperature superconductors is poorly 
understood chemically, forcing experiments into a series of scattered 
hunches covering a significant fraction of the periodic table. Practitioners 
are using computational chemistry to narrow the search.
Other materials applications include:
• Better adhesion — not just making new adhesives, but 
understanding the surface chemistry of the materials 
being bonded.
• Optoelectronics — moving from the current conductivity 
method of achieving results to quantum effects.
• New alloys — computational chemistry is being used to 
explore different classes of metallic alloys.
• Films and coatings — part of the circular process of new 
materials requiring new chemicals and processes.
• Fibers — process limits are being reached in extruding 
manmade fibers.
AberdeenGroup 28


--- Page 22 ---

Conflicting Trends In
Computational Chemistry
CHAPTERS
USER PROFILE: THE COMPUTATIONAL
CHEMIST
Today there are approximately 2,000 academic and industrial chemists 
practicing computational chemistry in all its forms, at about 350 sites 
worldwide. Members of this small, cross-disciplinary group of pioneering 
scientists are continually in contact with each other individually and in 
various symposiums, conferences, research consortiums, and academic 
gatherings.
During the course of its computational chemistry field work, Aberdeen 
met with or spoke with many of these scientists. The following profile 
emerges:
Personal Profile
Today's computational chemist is a 35- to 50-year old Ph.D. chemist whose 
graduate work was in organic or physical chemistry. During graduate 
school (or later on the job), he or she learned sufficient mathematics, 
statistics, quantum mechanics, and FORTRAN to develop a strong 
preference for quantitative (versus experimental) methods.
Computational chemists have an insatiable natural curiosity for discover­
ing new science, and, within the bounds of their employers' proprietary 
confines, communicate their conceptual findings and methods to peers fre­
quently and often profusely.
A handful of currently late-career computational chemists were the actual 
pioneers of the field, working on first-generation supercomputers, primari­
ly the CDC 3600 and CDC 6600. Mid-career chemists typically started in 
experimental chemistry or in academia and discovered the rewards of the 
computational approach, while the youngest practitioners have started im­
mediately upon graduation by joining existing computational chemistry 
groups.
Organizational and Work Profile
About half of today's computational chemists work in drug and other in­
dustrial laboratories in two- to four-person groups, and about half
AberdeenGroup 29


--- Page 23 ---

Overseas sales offices 
Overseas distributors 
Array processors installed
10
112
4,000+
Computational Chemistry Profile
FPS is a long-time player in computational chemistry — virtually every 
major molecular modeling installation has an FPS array processor on site.
Computational chemistry software supported includes: QUANTRA, 
CHARMm, X-PLOR, DISCOVER, Lab One NMR1/NMR2, SpectIR, GAMESS, 
MIDAS, AMBER, AMPAC, MM2, ECEPP, MOPAC, CNDO, BIGSTRN3, and 
PCIL03.
Computational Chemistry Products
For computational chemistry, FPS offers integrated compute servers, mini- 
supercomputers, and a superworkstation.
The FPS M64/60 Compute server is targeted at computationally intensive 
scientific and engineer applications, and is integrated into Digital's VAX; 
the M64/60 provides the computational power while the VAX handles pro­
gram development, terminal support, and administrative functions. The 
M64/60 has peak performance of 38 Mflops, and FORTRAN matrix multi­
ple of 10 Mflops. A less powerful version, the M64/35, can deliver 12 peak 
Mflops.
The FPS Model 500 minisupercomputer is a mix-and-match system of up 
to four scalar and/or vector processors, up to seven I/O subsystems and 
memory ranging from 16 MB to 1 GB of memory. Scalar processors can 
deliver 33 MIPS and up to 16.5 peak Mflops, while vector processors can 
deliver 66.7 peak MFLOPS. Prices for systems range from $225,000 to 
$1.5 million.
FPS offers an entry-level minisupercomputer, the Model 300, priced from 
$100,000 to $200,000, which can deliver up to 25 MIPS and 40 Mflops.
The Model 300 is also available packaged with a Stellar superworkstation 
as the Model 350.
Analysis
During FPS Computing's recent stumble, it lost considerable presence and 
momentum in computational chemistry markets, although its array proces­
sors are well regarded. Aberdeen questions whether FPS can recoup its 
position in face of the current minisupercomputer shakeout.
AberdeenGroup 78


--- Page 24 ---

Conflicting Trends In
Computational Chemistry
International Business Machines Corporation
Computer Aided Chemistry Applications
44 South Broadway
White Plains, NY 10601
(914) 686-6352
Corporate Profile
IBM is the world's largest computer manufacturer, with its nearest rivals 
less than a quarter of its size. Founded in the late 19th century as a 
producer of tabulating and other business equipment, IBM was a relative 
latecomer to the computer business, preferring instead to concentrate on 
its impressively profitable (95 percent marketshare!) punch-card-based 
tabulating systems business. Although late to the computer market, IBM 
nonetheless offered several types of computers — including impressive 
scientific ones — during the late 1950s and early 1960s.
Then, as now, users complained about disparate systems unable to com­
municate with each other, but with a major difference: different lines from 
the same manufacturer were incompatible. With an investment estimated 
at $5 billion (in 1960 dollars), IBM undertook to solve this problem.
In April 1964, in the largest single computer industry media event of all 
time, IBM revolutionized the computer business by introducing the Sys­
tem/360. The System/360 offered a comprehensive, fully compatible line 
of computers with a single operating system spanning the widest range of 
prices, performance, and applications that the industry had ever seen, and 
with the successor System/370, has ever seen.
Although currently known primarily for its commercial applications, IBM 
computers are used in a wide variety of technical applications. Over its 
three decades in the computer business, IBM occasionally has offered tech­
nically-oriented systems, and has recently stated its intentions to increase 
its marketshare in the technical sector.
IBM currently has installed 16 of its Vector Facilities in computational 
chemistry applications, and may well double that number within the next 
15 months. IBM also has shown a keen interest in computational 
chemistry by purchasing a minority position in Polygen, the largest ship­
per of molecular modeling software.
AberdeenGroup 79


--- Page 25 ---

Statistics
Revenues
$59.7 billion
Profits
$5.8 billion (9.8%)
Assets
$73.0 billion
R&D investments
$5.9 billion (9.9%)
Overseas revenues
58%
Five-year CAGR
7%
Employees
387,000
Sales offices
2,000 (Aberdeen estimate)
Computers Installed
300,000+ (Aberdeen estimate;
excludes personal computers)
Computational Chemistry Profile
Preferring the more encompassing term of Computer Aided Chemistry to 
computational chemistry, IBM is promoting an enterprise-wide approach 
(See Appendix E), integrating the best of IBM and the best of non-IBM solu­
tions.
Computational Chemistry Products
IBM's principal computational chemistry product is its Vector Facility (VF), 
an integrated optional extension to each 3090-class central processor. The 
six-processor Model 6005 can have six Vector Facilities. The VF has 171 
vector instructions, operates on 32-bit and 64-bit floating point numbers, 
has 16 KB of high-speed vector register storage, performs pipelined arith­
metic in one 15 ns cycle, and works in concert with the base processors 
and up to 2.5 GB of extended storage.
The Vector Facility costs $300,000, and for the incremental price, is the 
least expensive source of number-crunching power.
IBM supports every virtually known computer language and application, 
and is aggressively porting computational chemistry packages, including 
AMBER, AMPAC, BIGSTRN, Discover, ECEPP/2, Electra, Forticon 8, Gaus­
sian 86, Gromos, Hondo?, FLO82, FLO83, FLO87, FLO103, Harwell- 
FLOW3D, INS3D, NEKTON, Passage, Phoenics, Thanes, and TWING.
AberdeenGroup 80


--- Page 26 ---

Conflicting Trends In
Computational Chemistry
In addition, Polygon has announced that it will port its product line to 
IBM's workstation line, the PC RT.
Analysis
Aberdeen views IBM as a real sleeper in computational chemistry markets. 
Under heavy pressure to reverse modestly declining revenues in domestic 
markets caused by mainframe market saturation, IBM is gearing up for a 
lengthy assault on technical markets, with computational chemistry as one 
of its key markets. Using a Trojan horse tactic of delivering first-rate-bar­
gain Mflops attached to top-of-the-line 3090 mainframes, IBM is quietly in­
sinuating scientific processing into corporate data centers, many of which 
pass the computational costs on to computational chemists at very low in­
ternal prices.
Currently, by offering the Polygen products on the PC RT, IBM continues 
bolstering its PC RT line, one of the least respected workstation lines in the 
industry. Other additions were made in April 1988.
IBM's strategy is a long-term one, and will take several years to ac­
complish; there is a distinct risk that as in the past, IBM will not stay the 
course because of its inability to keep up competitively with technical 
product offerings — they have substantially shorter life cycles and require a 
degree of corporate nimbleness not usually present in the world's largest 
computer organization.
For a full analysis of IBM's role in computational chemistry, see Appendix 
E.
AberdeenGroup 81


--- Page 27 ---

Multiflow Computer, Inc.
175 North Main Street
Branford, CT 06405
(203) 488-6090
Corporate Profile
Multiflow was founded in 1984 to take advantage of a novel architectural 
approach to achieving faster, delivered-to-user computer system perfor­
mance — and without the need to recode users' programs. Traditional ar­
chitectures have compartmentalized hardware and software design, often 
with conflicting design goals and results. Multiflow started with repre­
sentative "dusty decks" of user FORTRAN, and designed an overall system 
to deliver the most bang for the buck without the user doing anything 
more than recompiling.
Multiflow's processor uses a very long instruction word (VLIW), executing 
from 7 to 28 instructions per machine cycle, depending upon the com­
puter model. This would normally result in inefficient hardware use, but 
Multiflow has developed a unique compiler technology, called Trace, that 
analyzes user code for packing the right instructions into the wide word at 
the right time. Sophisticated in its use of statistical techniques to assess 
which direction branch commands will likely take. Trace charges on ahead 
through most branch decisions, leaving "traces" of where to unravel and 
retrace when the branch decision grows awry.
In addition to improving vector-like performance in numerically intensive 
problems. Multiflow's Trace architecture, unlike that of most supercom­
puters and minisupercomputers, improves scalar performance as well. 
Consequently, Multiflow insists that it not be classed with the thinning 
ranks of minisupercomputer companies that were founded in the mid- 
1980s and are now facing hard times.
Statistics
Privately held. Multiflow chooses for competitive reasons not to disclose 
financial information for publication; however, for customers it will review 
financial data under a nondisclosure agreement. The company has sub­
stantial cash, has been backed by $42 million in three rounds of risk capi­
tal from an increasing number of sources (with early round investors 
stepping up for more on successive rounds), and is expected to break 
even in 1989 — a quite respectable showing. The company is currently ex­
AberdeenGroup 82


--- Page 28 ---

Conflicting Trends In
Computational Chemistry
ploring additional financing sources and a merger with a suitable partner; 
an announced merger with Adage was called off after shareholder 
problems indepently arose with Adage.
Revenues
$15 million (Aberdeen estimate)
Overseas revenues
30%
Employees
140
Domestic sales offices
12
Overseas sales offices
1
Overseas distributors
3
Computers installed
70 (Aberdeen estimate)
Computational Chemistry Profile
Multiflow is aggressively pursuing computational chemistry, with Ph.D. 
chemists on staff, including Dr. Michael Frisch, co-author of GAUSSIAN 86. 
In a surprising move for a startup, in June 1988 Multiflow began a six- 
month program of donating $6 million worth of its computers to up to 25 
qualified members of the academic community. Such seeding operations 
usually are conducted only by much larger companies, and this early Multi­
flow move signals a strong commitment to numerically intensive science.
Multiflow supports GAUSSIAN 86, GAUSSIAN 88, MOPAC, HONDO, 
AMPAC, GAMESS, CHARMm, BIGSTRN3, Mephisto, CHELP and AMBER.
Multiflow has joint marketing agreements with Silicon Graphics, 
Tektronix, and Apollo for handing the computationally intensive aspects of 
applications run on these graphics workstations.
Computational Chemistry Products
In February 1989, Multiflow introduced its second generation of mini- 
supercomputers, the Trace 300 family, offering three times the perfor­
mance of its earlier models. The Trace 7/300 delivers 30 Mflops and 53 
MIPS, the Trace 14/300 delivers 107 Mflops and 60 MIPS, and the Trace 
28/300 delivers 120 Mflops and 215 MIPS. Prices on the systems are 
$500,000, $600,000, and $1 million respectively. The new systems use a 
compiler that is substantially improved from earlier Trace systems, but 
users must recompile to take advantage of newer features.
Analysis
Multiflow has survived and gained marketshare during the minisupercom­
puter shakeout process, as one of the two suppliers in the budget-super­
AberdeenGroup 83


--- Page 29 ---

computer field to grow in 1988. (Convex is the other). Multiflow ranks 
third in shipments, after Convex and Alliant. With additional financing, 
Aberdeen expects Multiflow to be a survivor in the thinning minisupercom­
puter ranks.
AberdeenGroup 84


--- Page 30 ---

Conflicting Trends In
Computational Chemistry
Silicon Graphics, Inc.
2011 North Shoreline Road
Mountain View, CA 94039-7311
(415) 960-1980
Corporate Profile
Silicon Graphics was founded in 1981 to produce high-performance 
workstations, and is now the clear but recently challenged leader in 3-D 
graphics. With over 250 applications ported to its IRIS series, a $69 mil­
lion cash infusion in March 1988 from Control Data (its largest OEM), and 
IBM's September 1988 agreement to purchase IRIS graphics cards and 
license Silicon Graphics' IRIS Graphics library — all done fairly quietly — 
Silicon Graphics has outdistanced its competitors in less than two years.
Silicon Graphics has no small ambitions, comparing itself to the world's 
two premier computer companies: "Our strategy since inception has 
remained the same: To push prices lower, and performance still higher. 
Compatibility will be the key. Similar to what IBM did in the 60s with its 
360 series and what DEC did in the 70s with the VAX line — we are develop­
ing a family of workstations that we believe will reshape an entire in­
dustry."
Statistics
Revenues
$198.5 million
Profits
$10.5 million (5.3%)
Assets
$220.9 million
R&D investments
$26.6 million (13.4%)
Overseas revenues
30%
Five-year CAGR
125%
Employees
1,250
Domestic sales offices
35
Overseas sales offices
16
Workstations installed
6,500
AberdeenGroup 85


--- Page 31 ---

Computational Chemistry Profile
Unlike Ardent, Stellar, Multiflow, Convex, IBM, and Cray, Silicon Graphics 
does not have Ph.D. chemists on staff, relying instead on its independent 
software vendors ('geometry partners") to work with Silicon Graphics in 
porting and directly selling computational chemistry applications. So far 
the approach has paid off — Silicon Graphics' systems are the preferred 3- 
D graphics platforms for most molecular modeling software companies 
and users.
Computational Chemistry Products
Silicon Graphics' fully binary compatible line of superworkstations — 
based on MIPS Computer Systems' RISC processor and Silicon Graphics' 
proprietary Graphics Engine — begins with the $16,000 Personal IRIS and 
continues through the higher priced Power Series, with prices up to 
$150,000.
The Personal IRIS — in entry and extended versions — delivers 10 RISC 
MIPS, has 8 MB of memory and 155 MB of disk, and graphically has 8 
color bitplanes, plus 2 additional bitplanes for overlay/underlay (for 12 
bits/pixel). The extended version ("Super") can double the disk capacity, 
has 24 bitplanes, and a 24-bit Z-buffer for 56 bits/pixel. A 12 MHz floating- 
point processor is optional on the entry level system and standard on the 
super.
Silicon Graphics' multiprocessor 4D Power Series comes in three worksta- 
ion models (4D/120GTX, 4D/220GTX 4D/240GTX) and three cor- 
-esponding compute servers (4D/120S, 4D/220S 4D/240S). The 120 
models have two 10-MIPS (RISC) processors, the 220 models have two 20- 
MIPS (RISC) processors, and the 240 models have four 20-MIPS (RISC) 
processors. Upgrades are accomplished by board swaps. Computer 
memory is available in 8 MB increments to 128 MB. Image memory is 
forty-eight 1280 x 1024 image bitplanes (8 bits each for red, green, and 
blue; double buffered), and sixteen 1280 x 1024 image bitplanes for 
double-buffered alpha (optional), 24-bit Z-buffer (1280 x 1024), four 1280 
x 1024 overlay and underlay bitplanes, and four user-inaccessible window 
ID bitplanes.
Numerous communications linkages and software are available.
Analysis
As a broad-gauge supplier of advanced graphics workstations, Silicon 
Graphics has the advantage of scale economies, which it has exploited by 
being the most popular molecular modeling graphics workstation supplier 
AberdeenGroup 86


--- Page 32 ---

Conflicting Trends In
Computational Chemistry
in 1988. Aberdeen expects Silicon Graphics to continue its momentum at 
least through 1989, after which it is an open question whether it can 
retain its profitable market share as price-slashing newstarts Ardent and 
Stellar jostle with a hot new workstation from a Hewlett-Packard backed 
Apollo.
AberdeenGroup 87


--- Page 33 ---

Star Technologies, Inc.
515 Shaw Road
Sterling, VA 22170
(703) 689-4400
Corporate Profile
Star Technologies is the marketshare and performance leader in high- 
speed scientific attached processors, and a major factor in high-perfor­
mance 3-D graphics processors. Founded in 1981, it initially targeted 
seismic processing markets with the ST-100 (a 100 peak-Mflop, ECL-based 
array processor) introduced in 1983. Spending heavily on R&D and sales, 
Star did not achieve first profitability until 1986-87. Since then, it has been 
caught in the worst oil exploration slump in history, as well as a decline in 
revenues for General Electric, which incorporates the processor in its 
OEM Cat scanner business. Star is expanding into other applications, in­
cluding molecular modeling, and General Electric's Graphicon line of 
high-performance, 3-D processors, acquired in April 1988. In January 
1989, Star joined Glen Culler & Associates in an R&D project for advanced 
processors. With all these changes, quarterly revenues plateaued a year 
ago, forcing Star back into red ink in 1988.
Statistics
Revenues
$36.8 million
Profits
$3.8 million loss
Assets
$32.8 million
R&D investments
$6.8 million (18.5%)
Overseas revenues
5%
Five-year CAGR
32%
Employees
260
Domestic sales offices
10
Overseas sales offices
3
Processors installed
2,000
AberdeenGroup 88


--- Page 34 ---

Conflicting Trends In
Computational Chemistry
Computational Chemistry Profile
Star Technologies' vector processors are found in numerous installations, 
usually attached to Digital VAX computers. There is a Star users group that 
contributes computational chemistry programs.
Star Technologies supports ANL molecular dynamics, Discover, GEMM, 
NMR2, ST-CRY, Del Phi and CHARMm.
Computational Chemistry Products
Attached Vector Processors
Star's attached vector processors offload — and process concurrently — 
computationally intensive and graphics-specific portions of scientific ap­
plications from general-purpose computers manufactured by IBM, Gould, 
Concurrent, Sun, Alliant, and Digital's VAXBI-, Q-Bus-, and Unibus-based 
processors.
Introduced in October 1988, the VP series is CMOS-based, permitting air 
cooling and a small (rack-mounted) footprint. The VP-1 delivers 50 peak 
Mflops, and the PP-2 (a dual compute head version of the VP-1) delivers 
100 peak Mflops. The VP processors are Star's second-generation systems, 
and are based on its initial architecture. The first-generation ST series is 
ECL-based, and takes a larger footprint and more cooling capacity than the 
VP series.
The VP series is three-ported, and the processors can be shared concur­
rently between one host computer and two other dissimilar units — 
whether disks, tapes, I/O, computers, or other Star units. Peak data trans­
fer rates are 50 MB per second.
3-D Graphics Processors
The Graphicon processors can substitute for graphics supercomputers, 
with the Graphicon 1700 (G1700) rendering and manipulating 30,000 
Gouraud-shaded polygons or 225,000 anti-aliased 3-D vectors per second.
For motion applications, the Graphicon 1700 Simulator (G1700S) renders 
2,000 shaded polygons at 30 frames per second, 600 shaded polygons at 
60 frames per second, or 60,000 polygons per second, or 225,000 anti- 
aliased 3-D vectors per second. The G1700S supports out-the-window 
simulations with smooth motion and fast response.
The G1700 and G1700S are variations on the same architecture and can 
work with workstations, minicomputers, and mainframes from Sun, Digi­
tal, Convex, Gould, Harris, and Concurrent.
AberdeenGroup 89


--- Page 35 ---

Analysis
Star Technologies has displaced FPS Computing as recent marketshare 
leader in array processors, but has become caught up in internal difficul­
ties while computational chemistry markets have shifted towards the roller- 
coaster minisupercomputer market. To become a major participant in the 
computational chemistry market, Star Technologies must go beyond being 
a back-end processor to the Digital VAX — minisupercomputer companies 
are playing that role much more effectively — and invest in comprehensive 
hardware and software packaged solutions.
AberdeenGroup 90


--- Page 36 ---

Conflicting Trends In
Computational Chemistry
Stellar Computer Inc.
85 Wells Avenue
Newton, MA 02159 
(617) 964-1000
Corporate Profile
Stellar was founded in 1985 by Dr. William Poduska (CEO), the founder of 
Apollo Computer and cofounder of Prime Computer, and Arthur Carr 
(president, COO), former president of Codex. Stellar is in the super- 
workstation business, and is a strong rival of Ardent Computers. Both 
companies are challenging the leadership of Silicon Graphics.
As is Ardent, Stellar is targeting advanced, interactive high-performance ap­
plications that are computationally intensive.
Statistics
Privately held. Stellar Computer chooses for competitive reasons not to dis­
close financial information for publication; however, for customers it will 
review financial data under a nondisclosure agreement. The company has 
raised $48 millon in risk capital in three equity offerings. Stellar also has 
bank lines available.
Revenues
$12.7 million
Overseas revenues
44%
Employees
Domestic sales offices
210
14
Overseas sales offices
3
Overseas distributors
2
Systems installed
120
Computational Chemistry Profile
Stellar has 15 computational chemistry installations, and has ambitions to 
double this figure in 1989 and again in 1990. Stellar has staff and consult­
ing chemists, and has molecular modeling software supplier Polygen as a 
Stellar value-added reseller.
AberdeenGroup 91


--- Page 37 ---

Computational Chemistry Products
Stellar's Graphics GSIOOO minisupercomputer provides high-performance 
display of 3-D anti-aliased, depth cue lines for displaying true spheres with 
Phong shading. Representation of large molecules can be wireframe, ball- 
and-stick, or space-filling. Peak computer performance is 25 MIPS and 40 
Mflops double precision. Peak graphics performance is 600,000 3-D 10- 
pixel vectors per second, and 150,000 3-D 100-pixel Z-buffered, Gouraud- 
shaded polygons per second. Prices begin at $105,000.
Stellar also is offering its system as a compute server (CSIOOO), priced 
from $95,000 to $120,000,
FPS Systems is a value-added marketer for Stellar, selling both the GSIOOO 
and the CSIOOO systems to its customers. (Also, see the FPS Systems 
profile in Chapter 7).
Computational chemistry programs that Stellar supports, or that are 
scheduled to be available in the second quarter of 1989, are: QUANTA, 
CHARMm, LAB ONE, NMR1/NMR2, SpectIR, GAUSSIAN 86, MIDAS, 
AMBER, MOPAC, CNDO, BIGSTRN3, and PCILO3.
Analysis
Stellar is consciously pursuing computational chemistry, but not quite to 
the degree as its archrival Ardent. However, venture funds permitting. Stel­
lar is in a good position to gain hardware marketshare in the computation­
al chemistry market against more established rivals.
AberdeenGroup 92


--- Page 38 ---

Conflicting Trends In
Computational Chemistry
APPENDIXA
THE CHEMICAL INDUSTRY
Chemicals are everywhere and in everything. Chemicals are basic. Chemi­
cals are not only involved in every single product manufactured, but are 
constituent parts of every living being. Chemicals of some sort are 
produced by every nation in the world.
Chemical competition is global and sophisticated. Major suppliers operate 
in many different countries, shifting their sources of supply and produc­
tion, changing their import/export tactics, and balancing all of their resour­
ces to gain marketshare, overcome trade barriers, take advantage of 
currency fluctuations, and accommodate fluctuating economic and 
geopolitical conditions. By one estimate, there are over 300, $1 billion- 
plus chemical enterprises worldwide.
Production and trade figures are awesome — all measured in tens and 
hundreds of billions of dollars and in megatons of shipments. Three one- 
quarter trillion dollar examples alone illustrate the size: The USA annually 
produces $250 billion a year worth of chemicals; the USA petrochemical in­
dustry produces another $250 billion; and worldwide chemical export 
trade among all nations is $250 billion.
Exhibit A-1 schematically illustrates the basic flow of chemicals from raw 
materials to consumer and industrial products, and Exhibit A-2 shows the 
world as viewed by the chemical industry.
Exhibit A-3 shows simplified market shares of U.S. production classed by 
generic use, recognizing that over half the output is intermediate in nature. 
While these chemical products (and those shown in subsequent exhibits) 
are mostly chemicals of long standing, they are the bread and butter of the 
chemical industry and the ultimate provider of means and stimulation for 
chemical research and development
Exhibit A-4 shows shipment data in chemical terms — the bulk of shipments 
is inorganics, organics, and plastics.
Exhibits A-5, A-6, and A-7 break out the three major categories shown in Ex­
hibit A-4.
AberdeenGroup 93


--- Page 39 ---

sales were over 20 hardware companies covering the entire spectrum of 
computing platforms with estimated computational chemistry revenues of 
$210 million in 1988, up 31 percent from 1987.
Future growth for the entire sector is estimated at 35 percent per year, 
plus or minus several percentage points in any particular year, and with 
shifting marketshare mixes among several hardware and software seg­
ments. Aberdeen's growth projections are shown in Exhibit 1-1.
Contrary to the public expectation that computational chemistry will be 
"the next CAD/CAM market" and become a billion-dollar industry over­
night, Aberdeen believes computational chemistry will more closely
Exhibit 1-1: Growth of Computational Chemistry Market
1.5
.5-
0
Hardware
1.0-
1987 
1988 
1989 
1990 
1991 
1992 
1993 
1994
Software Revenues in $Billions
Source: 
AberdeenOoup 
AberdeenGroup 2


--- Page 40 ---

chemistry is complex, expensive, time consuming, of low yield, difficult to 
structure, and often highly hazardous.
To find the chemical compound that will meet the developer's needs, the 
process requires systematic trial-and-error testing of thousands and even 
tens of thousands (and occasionally, a hundred thousand) variations that 
are created experimentally to determine which ones work and have the 
least toxicity. (See Exhibit 2-2.) This process involves fluids (rather than 
solids and gasses). The experimental compounds are sprayed in small 
quantities onto test objects and subjects, and hopefully, one of them will 
eventually produce the desired results. Hence the industry cliche: "spray 
and pray!"
Chemists who perform this type of work, and those who research new 
chemicals, are typically trained in classic chemical methodology and 
theory, which use traditional mathematics and minimal computers.
Exhibit 2-1: Changing Scientific Methodology
1960s — 1970s
1980s ->
Pre-1960
Theory
Theory
Computer
Experiment
Experiment
Experiment
Source; National Academy Press 
AberdeenGroup 
AberdeenGroup 8


--- Page 41 ---

are practicing in academia.
Since the inception of computational chemistry, the typical computational 
facility has shifted dramatically about every two to three years. New super­
computers are being introduced approximately every two years, and new 
ways of delivering computer power every five or more years. Currently, 
practitioners have their own advanced desktop graphics workstations at­
tached to a local-area network, connected to local or remote compute ser­
vers ranging from array processors to Digital VAXclusters to 
minisupercomputers to timeshared Cray supercomputer services to IBM 
mainframes with Vector Facilities.
The typical computational chemist uses molecular modeling, supplement­
ing it with one of the more computationally intensive methodologies. The 
chemist develops little original computational chemistry software, but is 
forced to adapt commercial or exchange software because interface and in­
terchange standards are rudimentary.
Buying Profile
Computational chemists are highly trained, motivated, and skilled in their 
field. They are dedicated to their work, and are not particularly enamored 
with tools technology — whether it is the latest superworkstation, 
molecular modeling software, lab instrument, or integration scheme. They 
are loyal to what works, not to a particular hardware or software vendor. 
Computational chemists are conservative, but also are early adopters — 
they must be to advance their own science. Computational chemists do 
not suffer fools (or technically unqualified salespeople) lightly. They have 
severe budget constraints, as well as pressure to use existing corporate 
MIS facilities, often at highly attractive transfer prices.
Managers of computational chemists, given the hard choice between hiring 
another chemist and purchasing a computer, will tilt slightly toward the 
chemist.
Academic computational chemists are accustomed to paying 5 percent to 
10 percent of the list price for computational chemistry software, and no 
more than 50 percent of list price for hardware.
The Politics of Purchase
Computational chemistry purchases often place the research director (or 
laboratory manager) in a vise between the competing demands of chemists 
and executive management. Chemists want the latest computational 
chemistry software and equipment to enrich their own work and to better 
achieve a breakthrough, independent of budget issues. If management
AberdeeiiGroup 30


--- Page 42 ---

• Chemistry. The race is on to expand the types of 
specific molecules covered, including polymers and 
organics, and specific classes of molecules within these 
broad categories. Competition for developing new 
applications is intense, with the best and brightest 
academic and industrial chemists working on the 
problems.
• Productization. Most of the products do not yet 
present a comprehensive, consistent user interface, and 
documentation is typically subpar. Both are the result 
of the suppliers' small size and poor profitability levels, 
and the newness of the field.
• linkages. Molecular modeling can obtain better results 
when incorporating parameters and data from ab initio 
and semiempirical codes, and when linked to existing 
"force field" and other databases. Work continues on 
simplifying this process, with "integration" currently a 
hot topic. However, integration as a concept has never 
proven to be as sales-boosting as initially expected in 
any computational field, largely because the concept 
cannot in practice accommodate the very large variety 
and sources of disparate codes and packages, and 
because complex choices must be made during 
operation requiring skills beyond those readily 
incorporated into integrated schemes.
Product Differentiation and User Selection
With increasingly impressive hardware platforms available to all computa­
tional chemists, successful future software product differentiation must in­
clude either proprietary chemistry or data, or offer a quantifiable leadtime 
advantage to the user, or come with superior support.
Hence, companies that rely heavily on hardware markups while buying 
(or renting) their chemistry, can expect a profit squeeze.
Users have consistently told Aberdeen that each user organization must 
evaluate each commercial program on the user's suite of benchmarks. 
This can be a major investment in time and resources, with one leading 
pharmaceutical firm setting up five three-person teams, each taking a week 
to test and evaluate offerings from the five molecular modelers. Users also 
tell Aberdeen that there is no consistent winner, and that no one molecular 
modeling supplier can meet all needs. Many potential users do not pur-
AberdeenGroup 34


--- Page 43 ---

CHAPTER?
COMPUTATIONAL CHEMISTRY HARDWARE
SUPPLIERS
In this chapter Aberdeen profiles 13 suppliers that are active in serving the 
computational chemistry and molecular modeling markets: three mini- 
supercomputer suppliers (Alliant, Convex, Multiflow), one array proces­
sor supplier (FPS Computing), two full-line system suppliers (IBM, 
Digital), five high-performance graphics workstation suppliers (the Apollo 
Division of H-P, Ardent, Evans & Sutherland, Silicon Graphics, Stellar), the 
domestic supercomputer supplier (Cray Research), and one supplier of 
array processors and graphics workstations (Star Technologies). Com­
panies profiled range from IBM ($60 billion) to startups Ardent and Stellar 
(both with revenues under $20 million).
While others are present in the market, those profiled are either the most 
current active participants, had pioneering roles in the market, or are 
poised to re-enter.
Product Focus
With few exceptions, hardware products are not designed specifically for 
computational chemistry. Rather, hardware suppliers make as many allian­
ces as they can support with computational chemistry software suppliers — 
including supporting programs in the public domain. Marketing alliances 
between computer suppliers and graphics workstation suppliers are com­
mon and change frequently.
Product Differentiation and User Selection
Hardware is driving part of the two-step cyclic computational chemistry 
process in which new hardware permits software application advances, 
which in turn generate demand for even more powerful hardware. 
Hardware advances are uneven among suppliers, and price/performance 
among directly competing suppliers can vary by as much as a multiple of 
three-to-one, or more when total cost of ownership is considered.
Far more so than in commercial markets, computational chemistry users 
have little allegiance to hardware suppliers that have failed to keep pace
AberdeenGroup 56


--- Page 44 ---

As an integral part of the economic cycle, the chemical industry typically 
grows at the rate of the economy as a whole. As populations increase, as 
consumers demand more or different products, and as plants reach full 
capacity, new plants must be built. Few chemical companies will sit out an 
upcoming boom, so the typical expansion phase results in industry over­
capacity, followed by price cutting (and sometimes red ink), and sub­
sequent industry consolidation. This most recently occurred — worldwide 
— in the early-to-mid 1980s.
Current Demand
The chemical industry now operates at its highest level of plant utilization 
in 30 years, and profits subsequently are soaring — overall chemical 
demand is relatively insensitive to price. The memory of the painful 1980s 
industry consolidation is fresh in executives' minds, and massive expan­
sion in 1989 is unlikely, particularly in the face of what many economists 
believe will be a slowdown in the longest business expansion in modern 
history.
Exhibit A-1: Flow of Chemicals
on
Coal 
Mlncrmlm
Intel— 
mediate 
and 
Induatrlal 
Chemical.
Industrial 
and 
Consumer 
Goods
Basic 
Chemicals
Source: 
AberdeenGroup
AberdeenGroup 94


--- Page 45 ---

Much of the work of Science is routine, or in the words of an earlier 
astronomer, "filling in the decimal places." As incremental gains are made, 
the prevailing paradigms are reinforced, causing a natural conservatism 
which chills the "market for ideas" for new, often radical theories. 
Breakthroughs, by definition, mean changes in paradigms — which in­
variably threaten careers, stature, honors and funding. Thus, the oc­
casional breakthrough — genuine, imagined, bumbling, or even fraudulent 
— is accompanied by noisy public debate, acrimony, name calling and bom­
bast usually reserved for the sports pages or tabloids. This is particularly 
so if the potential breakthrough is made by someone not from the dis­
cipline — chemists, for example, claiming advances in what would ordinari­
ly be the private preserve of physicists.
The current controversy over cold fusion is a typical example of a poten­
tial shift in paradigm and the public spectacle accompanying it. Under the 
current paradigm, cold fusion, according to physicists, can't work the way 
the University of Utah chemists say it does. And, with hundreds of millions 
of dollars and dozens of multi-decade careers invested in pursuing the 
elusive goal of high-temperature fusion, it is no surprise that the cold­
fusion claims continue (at the time this report was going to press) to meet 
with such acrimony and rejection. With such predictable tar-and-feather- 
ing awaiting public announcement of paradigm-threatening potential new 
discoveries, few scientists are willing to casually "go public" with them, ad­
ding to Science's conservatism. Further impeding quick scientific progress 
is specialization.
Scientific Splintering
Reflecting the prevailing, 19th-century-based scientific paradigm of reduc­
tionism (reducing everything to irreducible parts). Science itself continual­
ly splinters into branches and sub-sub-sub-sub-branches. Computers 
reinforce reductionism by permitting microscopic examination of what in 
prior stages of science was thought irreducible. While reductionism has 
led to breakthroughs, it intrinsically forces researchers to "know more and 
more about less and less." The inevitable consequence is increasingly 
poor interdisciplinary exchange of ideas and results, reinforcing the no­
tion that incrementalism is the major source of gains.
Making Scientific Progress
Sustainable scientific progress has historically occurred from four sources:
• A conventional scientist, building on Science's 
accumulating body of knowledge, finds a way to project 
past results into new areas. Most scientific progress has 
been made this way, reinforcing current practice.
AberdeenGroup 106


--- Page 46 ---

THE ROLES OF DIGITAL, IBM, AND CRAY
Market Confusion and Opportunity
A pivotal element in computational chemistry development is the ever- 
changing availability and relative merits of competing and usually conflict­
ing hardware choices.
In this appendix, Aberdeen sketches the development of key stages in the 
conflict, showing that the early 1990s will witness a major struggle for com­
putational chemistry customer allegiance between system suppliers Digital 
and IBM, with Cray Research fighting equally as hard for machine place­
ments independent of which system supplier is chosen.
In addition to the "big three" suppliers, new classes of specialized 
hardware will keep pricing pressures and market confusion at all-time 
highs: superworkstations, reinvigorated minisupercomputer and parallel 
processing manufacturers.
The ongoing hardware war is being fought along three distinct lines:
• Point solutions versus systems. As computational 
chemistry moves beyond research laboratories and 
technically advanced practitioners, what should be the 
mix between the latest-and-hottest spot products 
(usually from unseasoned suppliers) and 
comprehensive (and typically less powerful or 
economic on an isolated unit basis) system products 
and integration schemes?
• Topology and integration. What, where, how, and to 
what degree should various software, hardware, and 
presentation systems and organizational elements be 
interconnected?
• Decision and control. Who finally determines 
topology and equipment choice — senior management 
and/or MIS, or technical management and scientists?
The impact that all this change will have on computational chemistry users 
and their enterprises is clear: fast-paced, often confusing change in 
AberdeenGroup 122


--- Page 47 ---

Conflicting Trends In
Computational Chemistry
resemble the finite element analysis market: after a period of quite respect­
able but unspectacular growth — accompanied by hardware and software 
vendor shakeouts — the field should become highly profitable for those 
with deep enough pockets to stay the course. Aberdeen projects that com­
putational chemistry revenues will not reach the billion-dollar level until 
1993. The conflict between these two views of the direction of computa­
tional chemistry has made investing in the field a controversial decision, 
and one that tends to be questioned continually.
Conflicting Trends and Issues
Several overlapping forces are driving and impeding computational 
chemistry. Those forces fall into six broad categories and are reviewed in 
the balance of this chapter.
User Profile
As a scientific discipline, computational chemistry is in its infancy. Only 
about 2,000 practitioners are active, and virtually all are Ph.D. chemists 
versed not only in chemistry, but in quantum physics and statistical techni­
ques. They are fairly to highly computer literate. About half are 
academics and the balance work in industrial research laboratories. They 
work in several industrialized economies and communicate frequently 
with each other.
While many computational chemists use commercial computational 
chemistry software packages, many do not, citing user-hostile interfaces, in­
consistent results from competing packages, and the availability of public- 
domain software. Dedicated primarily to science, computational chemists' 
requirements and "wish lists" occasionally conflict with those of their 
management, particularly in industrial settings. Research directors typical­
ly are caught between management-imposed time-to-market and budgetary 
pressures, and the needs and desires of chemists, causing tense political 
situations.
Selling to the computational chemist is a formidable challenge. Because 
they are first and foremost scientists, chemists have little inclination or 
time to keep up to date on the latest computer product lines, molecular 
modeling software packages, or supporting equipment and services. Yet, 
when in a purchasing mode, computational chemists are rarely exceeded 
in their ability to analyze product offerings and send packing those who do 
not pass muster. Commercial computational chemistry software suppliers 
overwhelmingly employ Ph.D. scientists as salespeople, and a surprising 
number of hardware companies do the same. Because of this user profile.
AberdeenGroup 3


--- Page 48 ---

Conflicting Trends In
Computational Chemistry
Promise of New Methods
Into this tradition-steeped environment comes computational chemistry, 
which promises to substitute mathematical techniques for at least part of 
the experimentation. If computer-implemented mathematical techniques 
can alleviate any of the experimental burdens, it obviously has great value. 
It is these fundamental observations that drive all participants in the com­
putational chemistry industry. And, with the unit-cost of computer power 
steadily declining year after year, specific applications continue to cross 
the cost-justification threshold, increasing the awareness and excitement 
level of chemical industrialists.
Computational chemistry can be roughly divided into several overlapping 
components, as illustrated in Exhibit 2-3, and described in more detail 
below:
• Preprocessing, database, instrumentation, and graphics 
elements — An array of front-end data sources, graphical 
manipulation techniques, and assorted programs.
• Molecular modeling — The heart of computational 
chemistry. Molecules are represented mathematically
Exhibit 2-2: Chemistry Discovery and Development Process
Next
molecule
No
Toxic 
?
Desired 
properties?
Source: AberdeenGroup
AberdeenGroup 9


--- Page 49 ---

Conflicting Trends In
Computational Chemistry
chronically deprives the chemist of what he or she believes is essential, the 
chemist may well move on to a more enlightened employer.
Executive management wants instant, or at least this-year, results, and con­
tinually pressures lab managers and research directors to be quicker 
about their business. New tools are fine, but management hasn't seen 
much correlation with prior new products. Yet, senior executives have 
been told (particularly by computer hardware salespeople) that computa­
tional chemistry is a real breakthrough, a sentiment amplified by glowing 
reports in the business press.
The research director, held to tough performance and budgetary stand­
ards, knows that results from new equipment and techniques typically are 
long in coming, and by adding new computational chemistry systems, he 
runs the dual risks of inducing unrealistic management expectations while 
diverting funds away from other activities that may have a quicker payoff.
Resolving the politics of purchase is handled differently by each 
enterprise, often with the help of objective outsiders who can dispas­
sionately analyze and quantify alternatives.
Availability of Trained Ph.D.s
An obvious factor that limits the growth of computational chemistry is the 
relative lack of trained chemists.
According to the National Science Foundation, each year the U.S. univer­
sity system graduates about 2,000 Ph.D. chemists, 1,000 Ph.D. physicists, 
and 2,000 Masters in chemistry. Science education tends towards lengthy 
cycles (see Exhibit 5-1), and quantum increases in technology graduates 
do not occur in the absence of a major national program, such as the 
space race of the 1960s. Also, science currently is out of favor at the secon­
dary education level, limiting the growth of potential graduate-degree com­
putational chemists available in the 1990s to less than 3,000 per year.
Sources of New Computational Chemists
Computational chemistry as a science is barely adolescent, but a handful 
of universities are making formal efforts to dramatically increase the num­
ber of Ph.D. chemists prepared to become computational chemists upon 
graduation. And, the U.S. graduates about 10,000 Bachelor-level chemists 
each year who eventually may be able to practice computational chemistry.
The pioneering computational chemistry educational effort began in 1988 
at the North Carolina School of Pharmacy, which has a modem computa­
tional lab (thanks in part to generous equipment and software donations) 
and a full interdisciplinary curriculum covering the three essential dis- 
AberdeenGroup 31


--- Page 50 ---

Conflicting Trends In
Computational Chemistry
chase commercial molecular modeling software because of the resources 
required to evaluate commercial offerings, the discrepancy of results from 
one supplier's package to another, and the lack of standard interfaces for 
operating with public-domain codes.
Quasi-public Software
While seldom competing directly with commercial software, various com­
putationally intensive public-domain chemistry codes (ab initio and semi- 
empirical) limit the size of the computational chemistry market, reducing 
the base for spreading out the high costs of product design and support. 
(For a more complete discussion of the financial implications, see Appen­
dix C, Investment Issues.)
Internal Proprietary Software
Successful use of computational chemistry provides the user with an im­
mense competitive advantage, well beyond those typical in computer ap­
plications. Because much of the advantage comes from easily transmitted 
and duplicated intellectual property, virtually no commercial user or­
ganization will admit to breakthroughs obtained from computational 
chemistry. Just as widespread, however, are user and vendor convictions 
that computational chemistry breakthroughs have occurred and have been 
based upon public-domain and commercial codes adapted for proprietary 
use. The impact on molecular modeling is both positive and negative.
On the plus side, proprietary success acts as a strong motivation to acquire 
even better computational chemistry programs as they become available, 
stimulating industry growth. On the minus side, internally developed 
codes limit the size of the available market.
Supplier Profiles
The five molecular modeling suppliers range in size from $2 million to $9 
million (1988 revenues). Revenue mix varies substantially among them: 
Tripos and BioDesign provide software and software support. Chemical 
Design and Polygen also sell hardware, and BIOSYM adds consulting and 
technical contract revenues on top of these.
For each of the six commercial organizations each profile contains:
• Corporate Profile — company background.
• Statistics — size, profitability, number of customers, and 
number of employees. Data is company supplied 
unless otherwise noted. Financial data is as of January 
1, 1989 and other data as of April 1989.
AberdeenGroup 35


--- Page 51 ---

Conflicting Trends In
Computational Chemistry
with technical product offerings. This is particularly true in compute ser­
vers, where this year's hottest box is seldom next year's.
Aberdeen recommends that users seeking to gain a competitive advantage 
through computational chemistry consider all but Cray-class hardware pur­
chases as having two-year useful lives (regardless of accounting conven­
tions), to be disposed of regularly. This requires users to systematically 
maintain a stable program development environment and a well-planned, 
evolving network scheme, each of which can minimize cut-over disrup­
tions.
As with software selection, each user organization must evaluate hardware 
purchases using its own suite of benchmarks and the computational 
chemistry programs they will run.
Supplier Profiles
For each of the 13 organizations, each profile contains:
• Corporate Profile — company background.
• Financial Statistics — revenues for the 12-month period 
ending on or closest to December 31, 1988, profits (and 
as a percent of revenues), assets, R&D investments (and 
as a percent of revenues), percent overseas revenues, 
five-year compound annual growth rate (CAGR). For 
the three privately-held companies — Ardent, Multiflow 
and Stellar — financial data typically is not fully available.
• Operating Statistics — number of domestic and overseas 
sales offices and distributors, number of employees and 
number of units installed.
• Computational chemistry profile, including 
relationships with software and other hardware 
suppliers.
• Computational chemistry products.
• Analysis — Aberdeen's view of the supplier's strengths 
and weaknesses.
In addition to individual profiles. Appendix E presents an extensive review 
of Digital, IBM, and Cray Research.
AberdeenGroup 57


--- Page 52 ---

Conflicting Trends In
Computational Chemistry
Exhibit A-2: Chemical View of Industry
Extractive 
Industries 
o Oil, Gas 
o Minerals 
o Coal 
o Metals
Transportation
Not-For-Profit 
Institutions 
o Laboratories 
o Education
Agricultural 
o Pesticides 
o Germicides 
o Herbicides 
o Fertilizers
Environmental 
Detection and 
Compliance
Basic
Finished
Gasses
Fine
CHEMICALS
Specialty
Solvents
Adhesives
Intermediate
Life Sciences 
o Pharmaceuticals 
o Vitamins 
o Diagnostics 
o Botanicals 
o Veterinary 
o Biologicals
Petroleum
Refining
Source:
AberdeenGroup
Manufacturing 
Industries 
o Automotive 
o Aircraft 
o Textiles 
o Defense
Transportation 
Equipment 
o Autos, Trucks 
o Aircraft 
o Ships 
Trains
Process Industries 
o Food o Paper 
oRubber o Plastics 
oPaints o Metals 
o Construction materials
AberdeenGroup 95


--- Page 53 ---

Conflicting Trends In
Computational Chemistry
• A conventional scientist, either young or otherwise 
having minimal vested interest in prevailing theory, is 
disturbed by the stubborn accumulation of actual 
observations — worldwide — that either do not fit well 
with the prevailing paradigm or contradict it. Taking a 
"clean piece of paper," the scientist derives a new theory 
or alters an existing one that accommodates more of the 
observations than did the prior theory. (Virtually no 
current theory in any scientific field can accommodate 
all known observations). This is the second most 
important way that science has progressed.
• An individual — sometimes not a scientist — with interests 
in more than one discipline, steps back from 
microscopic details and integrates at a higher, 
conceptual level what has been learned in other fields. 
Because paradigms are threatened in more than one 
field, the public aspects are even noisier than within a 
single discipline. Few discoveries are made this way, 
but when they do occur, they are typically blockbusters.
• Apart from Science itself, scientific progress is made by 
engineers and business people. Setting aside theory and 
paradigms, engineers design and build new products 
that work, with business people funding and marketing 
them. Much of what the news media has called science 
has in fact been engineering and technology — space 
exploration, computers, semiconductors, and chemical 
production.
Chemistry Issues
Research chemistry is the practice of science; it is not an engineering dis­
cipline — reducing to practice what has already been discovered. Of what 
scientists think could be known about chemistry, only a minute fraction of 
a percent is known. And that sparse body of knowledge is spattered across 
an alphabet soup of disciplines and subdisciplines, each with its own set of 
practitioners, special rules, ad hoc theories, approximations, jargon, and 
esoterica. Much of this knowledge is empirical, with theory often lagging 
observation. Leading chemists typically sketch this state of uneven chemi­
cal knowledge as shown in Exhibit B-1.
AberdeenGroup 107


--- Page 54 ---

Conflicting Trends In
Computational Chemistry
hardware, systems, and topologies will remain the rule, necessitating in­
creasing investments of time and resources in evaluating future choices for 
their own specific enterprise needs.
For vendors, the message is one of increasing business risk, where system 
topology and other vendors' software play increasingly heavy roles, and 
where today's hot product can fall out of favor overnight.
For both users and vendors, there is the distinct but nonquantifiable 
chance that as a direct result of this hardware ferment a major chemistry 
breakthrough will occur, reducing management's current skepticism. If 
so, aggregate hardware demand will increase, while specific demand for 
types of hardware will shift once again, mirroring that demand required in 
the breakthrough.
Four Stages of Conflicting Hardware and Topologies
The choice and range of hardware platforms available for computational 
chemistry has changed dramatically over a scant six years, progressing 
through three overlapping stages and now entering a fourth, as analyzed 
below and schematically illustrated in Exhibits E-1 through E-4.
Stage 1 - Digital Equipment: A Pioneer in Computational Chemistry 
From 1983 to 1987, Digital Equipment overwhelmingly dominated the 
scene, and even now, VAXes are in 80 percent of some 300 molecular 
modeling installations. Digital's early dominance was based on several key 
strengths:
Exhibit E-1: Developmental Stage - 1983-87
Network
Digital
Cray
Source:
AberdeenGroup
AberdeenGroup 123


--- Page 55 ---

selling into (or investing in) the computational chemistry sector can be full 
of surprises.
Competing Methodologies
Computational chemistry is far from a uniform approach to using com­
puters in chemical discovery and development. Rather, it is an ever-shift­
ing aggregation of overlapping and underlapping techniques spanning an 
enormous 10,000-to-1 range of computational intensity. This creates con­
tinuing tension in the industry as practitioners juggle the need for ac­
curacy (best obtainable from computationally massive calculations) with 
the need for speedy results (modest computational requirements).
Each of three predominant computational techniques (ab initio, semiem- 
pirical, molecular modeling) has its benefits and limitations, with various 
hybrid techniques and integration schemes being developed to make 
progress more predictable.
Only the most computationally intensive method (ab initio) yields results 
that track closely with the real world, but unfortunately, not all the super­
computers in the world can tackle even a simple drug problem using the 
method. Thus, the tension and voracious search for other methods, which 
represent varying degrees of scientific compromise and reproducibility of 
results.
With the recent advent of 3-D graphic superworkstations and new 
molecular modeling programs, computational chemists are gaining new in­
sights into the underlying science. This introduces the possibility of major 
chemical breakthroughs, since new ways of viewing the world historically 
have led to new inventions. However, the very nature of science makes 
the what/when/where/who impossible to pinpoint; only after the fact 
does it all appear "obvious."
Science Reaches Limits
Computational chemistry methodological trends are in flux not only be­
cause the underlying science is far from understood, but because new dis­
coveries in allied fields have stretched current theory to (and often 
beyond) its ability to explain experimental results. For example, the recent 
potential breakthroughs in high-temperature superconductors using 
ceramics and in cold fusion using palladium have no theoretical bases, 
and, lacking them, scientists have no ready way to narrow their search for 
further advances. As expressed in a cartoon posted in a leading 
practitioner's office, one white-smocked scientist says to another, "Yes, yes, 
it works in practice, but can it work in theory!"
AberdeenGroup 4


--- Page 56 ---

in three-dimensional form with a series of chemical and 
physical properties, and manipulated both in numerical 
form (in high-performance computers) and graphically 
(on graphics workstations) to investigate specific 
properties and to obtain overall insight into the 
molecule's structure. Three basic methods are used — 
ab initio, semiempirical and molecular mechanics.
• Post processing — quantitative, statistical, and graphical 
techniques for refinement and extension of the 
modeling work. Molecular dynamics — a technique for 
simulating molecular behavior in microsecond or even 
picosecond steps — sometimes is included in 
postprocessing, and sometimes as part of modeling.
Exhibit 2-3: Components of Computational Chemistry
Preprocessing
Graphics
Molecular Modeling
Semiempirical methods
Molecular Mechanics
Ab initio methods
Databases
Experimental and 
Analytical data
Molecular 
Dynamics
Post­
processing
Source: AberdeenGroup
AberdeenGroup 10


--- Page 57 ---

ciplines of chemistry, physics, and computer science, as well as life scien­
ces and pharmacology.
The American Chemical Society is actively pursuing advanced training 
courses for experienced chemists who wish to switch to computational 
chemistry.
Over the next five years, a new group of lesser-trained (often not Ph.D. 
level) computational chemists will begin applying the pioneering advances 
in a semi-mechanized manner, particularly in drugs. This will free the ad­
vanced practitioner from routine work, allowing further progress in under­
lying science, which in turn can be semi-mechanized for lesser-skilled 
practitioners.
Exhibit 5-1: Graduate Degrees In Chemistry
2000 -
2200
1400 ■
1800 ■
1600 -
i
i
74 
75 
76 
77 
78 
79 
80 
81 
82 
83 
84 
85
8
8
Doctorate
Masters
Source: 
National Science Foundation
AberdeenGroup
AberdeenGroup 32


--- Page 58 ---

• Science — source of the company's ongoing academic 
insight and knowledge.
• Computational Chemistry Products and Prices.
• Hardware Partners — significant relationships with 
computer system and high-performance graphics 
workstation suppliers.
• Analysis — Aberdeen's assessment of the supplier's 
strengths and weaknesses.
AberdeenGroup 36


--- Page 59 ---

Alliant Computer Systems Corporation
One Monarch Drive
Littleton, MA. 01460
(508) 486-4950
Corporate Profile
Founded in 1982 by former Data General superminicomputer architect 
Ronald Gruner, and others, to develop its scientifically-oriented parallel 
processing minisupercomputers, Alliant has been racing neck-and-neck 
with Convex for first place in this roller coaster market. At last count, Al­
liant had 350 computers installed (to Convex's 400). In 1987, both com­
panies made respectable profits and were poised for 50 percent growth in 
1988.
However, Alliant faltered in 1988, with its revenues declining 12 percent 
(versus Convex's 52 percent increase), triggering a massive $36 million 
loss. Troubles began in the first quarter when the company barely broke 
even, and posted red ink each quarter thereafter. Contributing to Alliant's 
problems is the digestion of Raster Technologies which Allied acquired in 
mid-1988, as well as a major restructuring of its sales operations.
Statistics
Revenues
$68.8 million
Profits
$36.2 million loss
Assets
$96.9 million
R&D investments
$13.7 million (21.0%)
Overseas revenues
32%
Five-year CAGR
114%
Employees
350
Domestic sales offices
16
Overseas sales offices
9
Overseas distributors
3
Computers installed
350
AberdeenGroup 58


--- Page 60 ---

Exhibit A-3: Estimated 1989 U.S. Chemical Shipments by Use
Chemical Preparations 3.2%
Polishes & Sanitation 2.7%
Adhesives & Sealants 2.1%
Surface ActIvants 1.6%
Alkalles & Chlorine 1.5%
Synthetic Rubber, Other 2.1%
Plastics & Resins 12.5%
Industrial Organic 16.5%
Pharmaceuticals, 
Medicals 14.8%
Industrie!
Inorganic 7.2%
Cyclic Crudes & Intermediates 3.8%
Soap & Detergents 5.0%
Toilet Preparstlons 5.6%
Fibers 6.1% -
Paints, Inks, 
Pigments 7.5%
Agricultural, 
Fertilizers 7.9%.
Total: $209 Billion (1982 dollars)
Source:
U.S. Department of Commerce 
AberdeenGroup
AberdeenGroup 96


--- Page 61 ---

Lack of Unified Theory
Chemistry has no unified theory, rather it consists of a broad scattering of 
underlapping and overlapping theories applicable to ad hoc situations, 
and rules-of-thumb (many of which are called "laws") developed over cen­
turies. For example, the theoretical basis of commercial dyes is thorough­
ly understood, while entire areas — including biologicals, "cold fusion", 
and high-temperature superconductivity — are poorly understood, if under­
stood at all.
Maturity
In spite of the limits of scattered knowledge, chemistry and pharmacology 
are paradoxically mature fields, with the "easy" discoveries well in the past 
and the easy-to-cure diseases already cured. New discoveries cost more, 
take longer, and typically are accompanied by side effects often undis­
covered for years.
Institutionalized Inertia
The process of bringing a significant new chemical to market requires sift­
ing out from tens of thousand of similar chemicals the one best one, if any,
Exhibit B-1: State of Chemistry Knowledge
AberdeenGroup
3-Source:
Dots represent areas of' 
chemical knowledge.
AberdeenGroup 108


--- Page 62 ---

• The best VMS program development tools in the industry
• Strong dedication to technical and academic markets
• Unsurpassed networking, permitting interconnection 
with heterogeneous systems
• The best price /performance from a full-line, 
general-purpose computer manufacturer
• Pioneering of molecular modeling predominantly done 
on VAXes
While development was done predominantly on VAXes, computationally 
intensive ab initio work was performed on Cray or Control Data super­
computers. Because of the relative novelty of computational chemistry, no 
industrial users had yet purchased these $5 million to $24 million com­
puters for dedicated computational chemistry use. Instead, Crays could 
be timeshared by VAX users requiring occasional high-intensity comput­
ing.
Stage 2 - Minisupercomputers and Chemical Databases — 1984-89
The very flexible networking that Digital offered permitted startup 
specialist manufacturers such as Alliant, Convex, Multiflow, Scientific Com­
puting Systems, and Star Technologies, as well as established technical sup­
pliers such as FPS, to deliver "compute servers" into existing
Exhibit E-2: Cheaper Computing and Databases - 1984-89
Source: 
AberdeenGroup
Network
Cray
Digital
Databases
Minisupercomputers
AberdeenGroup 124


--- Page 63 ---

Conflicting Trends In
Computational Chemistry
Commercial Software Trends
Computational chemistry software trends are diverse and conflicting. Be­
cause chemistry is a highly fragmented and diverse field, molecular model­
ing software suppliers compete vigorously with each other by adding new 
modules or new programs that can work with types of chemicals not pre­
viously modeled. Five commercial suppliers are targeting some 350 sites 
in a fairly noisy competition, all claiming product superiority. Users must 
invest significant efforts to choose the right package. Not only is there no 
clear "best buy," but many users buy $100,000 packages from multiple sup­
pliers and compare results because each package uses different simplify­
ing assumptions which cause differing results.
Complicating the lives of commercial molecular modeling software sup­
pliers is tangential competition from public-domain software, although 
most of it is in the more computationally intensive methods. Lacking com­
mercial backing, these codes typically have erratic support and documenta­
tion, with authors continuing to refine and extend the packages in a 
bewildering array of interface and notational conventions.
Hardware Trends
Concurrent with changing trends in science, software, and methodologies, 
are continually shifting and conflicting trends in which computer 
hardware is used to solve computational chemistry problems.
At the high end, supercomputers promise definitive solutions through mas­
sive ab initio and semiempirical computations, but for relatively few chemi­
cals of commercial interest. However, with each new round of 
supercomputing power, more chemicals can be tackled. And, supercom­
puters are used increasingly to derive parameters that can then be applied 
with less computationally intensive methods.
At the opposite end of the spectrum are the new 3-D graphic superworksta­
tions with impressive power on the desktop applied to the less computa­
tionally intensive molecular modeling approach. The large difference in 
price/performance, and under-$100,000 price tags, are driving the rapid 
1988-89 growth in sales of these units.
In the middle range, both minisupercomputers and superminicomputers 
have slackened in their market penetration relative to workstations, but 
each for different reasons. Superminicomputers pioneered molecular 
modeling in the early-to-mid 1980s, offering unprecedented price/perfor­
mance and a superior software development environment compared to 
mainframes. However, in the mid-to-late 1980s, minisupercomputers
AberdeenGroup 5


--- Page 64 ---

Conflicting Trends In
Computational Chemistry
Theoretical Underpinnings
The practice of computational chemistry is based on a number of theoreti­
cal assumptions and hypotheses, some of which bear good to excellent 
conformity to experimental results. The most fundamental of these are the 
third law of thermodynamics and the theory of quantum mechanics — com­
plex and abstruse mathematical and physical concepts used to describe 
and predict behavior at the atomic level. Before the advent of modem 
computers, there was no way to effectively test these theories.
However, no single theory accounts for all chemical behavior, and every 
day new chemical behavior is discovered for which there is no explanatory 
theory. Because of the uncertainties in the underlying science, there is no 
single method of practicing the three general methods of computational 
chemistry. Further, there are some major scientific hurdles facing the in­
dustry, as detailed in Appendix B, Science Issues.
Computational Requirements
Each of the three computational methods differs substantially in computa­
tional requirements, which in turn limits the types of molecules that can be 
studied computationally. Hybrid methods also are beginning to be used, 
but meshing results from the three standard methods is mostly an 
embryonic art. As computer power increases (and costs per unit of com­
putation decrease), larger molecules can be studied using the more inten­
sive methods. Exhibit 2-4 summarizes current practice, and Exhibit 2-5 
maps the typical type of platform used onto the computational chemistry 
component diagram shown in figure 2-4.
Ab Initio Method
Ab initio ("from the beginning") computer codes operate from "first prin­
ciples" — the molecule is explored at the electron/proton level as 
described by "Schroedinger's Equation," the theoretical mathematical 
description of molecules at the subatomic level. This is the area of quan­
tum mechanics, in which few chemists have been trained. Ah initio calcula­
tions are used in exploring electro-optical properties of molecules and in 
spectroscopy, and were first used in the 1960s without any simplifying in­
structions.
Ab initio calculations are computationally massive, and could consume all 
supercomputers ever built without scratching the surface of what re­
searchers would like to know. Consequently, researchers seek alternative 
methods.
AberdeenGroup 11


--- Page 65 ---

Conflicting Trends In
Computational Chemistry
CHAPTER 6
COMPUTATIONAL CHEMISTRY SOFTWARE
SUPPLIERS
In this chapter, Aberdeen profiles the five small molecular modeling 
software suppliers: BioDesign, BIOSYM, Chemical Design, Polygen, and 
Tripos Associates. These firms compete with each other, but not with the 
two other organizations profiled: the chemical information management 
system company (Molecular Design), and the largest not-for-profit 
software distributor. Quantum Chemistry Program Exchange (QCPE).
All seven organizations are either privately held, not-for-profit, or units of 
larger companies, which reduces the availability of statistical data. Unless 
otherwise indicated, remarks about the group apply only to the five 
molecular modeling software suppliers.
The five molecular modeling companies are in various stages of corporate 
development, and collectively have more staff, products, and facilities than 
the market can profitably support. Aberdeen and software suppliers an­
ticipate an incipient one- to two-year shakeout that each supplier plans to 
survive.
Product Focus
Because computationally intensive ab initio and semiempirical codes are 
impracticable today for the large molecules that are of commercial inter­
est, and because the bulk of these codes are in the public domain, commer­
cial computational chemistry software product emphasis is on molecular 
modeling, which can accommodate molecules up to about 20,000 atoms 
(which covers chemicals of current interest).
Each of the five suppliers offers similar products, with only moderate 
degrees of differentiation, connectability to other types of computational 
chemistry codes, user-friendly interfaces, and operating features. While 
molecular modeling itself is inaccurate, it has delivered some real results 
and considerable insight to working chemistry.
Supplier product emphasis is threefold:
AberdeenGroup 33


--- Page 66 ---

Conflicting Trends In
Computational Chemistry
BioDesign, Inc.
199 South Los Robles Avenue, Suite 615
Pasadena, CA 91101
(818) 793-0151
Corporate Profile
BioDesign was founded in 1984 by leading computational chemistry prac­
titioners and visionaries Professor William A Goddard III, Dr. Barry D. 
Olafson, and Dr. Stephen L. Mayo. BioDesign has continuing scientific 
connections to Caltech, where Dr. Goddard is a full-time professor.
BioDesign is the smallest of the molecular modeling suppliers. While bare­
ly out of the startup stage (with sales and marketing only recently begun), 
BioDesign has ambitions to become the leading supplier of integrated 
molecular modeling systems.
BioDesign's vision of computational chemistry goes beyond the current in­
tensity in the biological sciences and into the polymer and materials areas.
Statistics
Privately held, BioDesign chooses for competitive reasons not to disclose 
financial information for publication; for customers, however, it will 
review financial data under a nondisclosure agreement. The company is 
financed by the founders, and recently by some venture capitalists. It is 
operating at a nominal profit and has doubled in size every year. 
Revenues to date reflect license and maintenance fees and include no 
hardware sales.
Revenues
$2 million (Aberdeen estimate)
Domestic customers
60
Overseas customers
20
Employees
23
Computational Chemistry Profile
BioDesign is ramping up to become a hardware supplier, as well as 
molecular modeling software supplier, and has developed with Ardent a 
joint product, the Molecular Simulator.
AberdeenGroup 37


--- Page 67 ---

Conflicting Trends In
Computational Chemistry
Computational Chemistry Profile
Alliant has a working relationship with BioDesign for its molecular model­
ing software, and is technically aggressive in scientific visualization (com­
bining Alliant's technology with Raster's).
Computational Chemistry Products
Alliant markets both minisupercomputers and graphics workstations.
Alliant's FX/Series of 64-bit minisupercomputers combines parallel 
processing, multiprocessing, and vector processing to act as departmental 
compute servers in computationally intensive applications. While not fault- 
tolerant, the FX/Series has a degree of high availability through parallel 
design.
The FX/Series runs standard FORTRAN, Ada, and C programs in parallel 
with little or no reprogramming (including those running on VAX). 
Alliant's FX/FORTRAN detects the potential for vector and parallel process­
ing and generates instructions to take advantage of these hardware fea­
tures. Up to eight parallel processors can work on a single application 
simultaneously. Concentrix, Alliant's operating system, is a variant of 
Berkeley UNDC.
The FX/8 had eight processors and the FX/1 a single processor, based on 
Alliant's Computational Element (CE). CE's can deliver up to 5 M- 
Whetstones single-precision and 4.27 MWhetstones double-precision, and 
peak vector performance of 11.8 Mflops.
In early 1988, Alliant began shipping its second-generation systems based 
on a newer processing element, the Advanced Computational Element 
(ACE). New FX models FX/80, FX/82, and FX/40 incorporate 8, 16, and 4 
ACE units, respectively. Each ACE can deliver up to 14 MWhetstones using 
Alliant's FX/FORTRAN compiler and 23.5 Mflops.
Alliant's (formerly Raster's) Visualization Series tightly integrate the 
FX/Series of processors with the Raster GX4000 series of four types of 
graphics accelerator boards to deliver high-performance computation and 
graphics when connected to Sun Microsystems' Sun-3 and Sun-4 worksta­
tions.
Analysis
With a strong cash position, the return to profitability in the first quarter of 
1989, and with seasoned West Coast venture capitalist (and board chair­
man) Thomas Perkins now active in the company, Alliant has the 
wherewithal to get back on its revenue and profit track, but has missed the
AberdeenGroup 59


--- Page 68 ---

Conflicting Trends In
Computational Chemistry
Exhibit A-4: Estimated 1988 U.S. Chemical Shipments by Type
Synthetic Fibers 2.2%
Organic Chemicals 29.5%
Inorganic Chemicals 58.1%
Estimated total: 200 Megatons
Source:
Chemical & Engineering News 
AberdeenGroup
AberdeenGroup 97


--- Page 69 ---

Conflicting Trends In
Computational Chemistry
that works effectively, has no major undesirable side effects, and yet is non­
toxic. The inefficiency of research is so well imbedded in industry lore 
that new tools typically are greeted with skepticism. Also, corporate in­
frastructures built on traditional experimental methods will not quietly 
turn over authority — or jobs — to what most employees view as theoretical 
exercises.
Niche Specificity
The computational and theoretical requirements for reducing the number 
of compounds that must be built experimentally cover a wide range and 
are molecule-type specific. Because the computational requirements for 
fully modeling (with any degree of confidence) all aspects of even a 
medium-sized molecule exceed the world's theoretical computing 
capacity, approximations are used with highly variable rates of success.
This is summed up by a report from the National Academy of Sciences:
A conventional 100-picosecond molecular dynamics simulation of 
a small protein in water would require about 100 hours on a VAX 
11/780 or 10 hours on an IBM 3033. Calculations of the rate 
constant for a simple activated process require a sequence of 
dynamical simulations to determine the free energy barrier, and 
additional simulations to determine nonequilibrium 
contributions; the times can now reach 1,000 hours on a DEC 
VAX 11/780. More complicated processes or longer simulations 
become impossible without the much higher speeds of 
supercomputers.
Fragility
The process of extrapolating computational chemistry techniques beyond 
known results is tenuous. Knowing how far a computational technique 
can be pushed is, at best, an art. The risk of pushing too far is that the 
programs will spit out seemingly precise answers, which are then pursued 
experimentally. If wrong, they will have consumed irreplaceable time-to- 
market and valuable resources. Current computational chemistry techni­
ques are slightly biased towards retention of "uninteresting" molecules.
Expertise
Because the computational chemistry algorithms only mirror the underly­
ing theoretical chemistry and its approximations, computational chemistry 
itself is still too chemist-dependent to be made into an off-the-shelf bench 
tool.
AberdeenGroup 109


--- Page 70 ---

Conflicting Trends In
Computational Chemistry
computational chemistry networks. The smaller companies primarily sell - 
- relative to the VAX — raw performance, price/performance, or both. 
While Digital continued to grow impressively in the overall computational 
chemistry hardware market, it was increasingly sharing the market with 
newcomers.
Concurrent with minisupercomputer deployment for cheaper computa­
tion was the steady increase in use of superminicomputer-based chemical 
database management systems, increasingly dominated by Molecular 
Design. Databases are the hidden tip of the computational chemistry 
iceberg: as the number of known chemicals increases exponentially, keep­
ing track of what's already been discovered — and keeping proprietary dis­
coveries secret — is vitally important. Accordingly, much database activity 
never appears in public, or simply is not discussed. Database systems typi­
cally are split between public domain and proprietary internal, and they 
are far more important than depicted on hardware or topology diagrams.
Stage 3 - Enter the Workstations
Molecular modeling (but not ab initio calculations) demands interactive, 
or at least, high-quality presentation graphics. First-round workstations 
from Apollo, Evans & Sutherland, and Silicon Graphics effectively enabled 
the existence of molecular modeling. A second round of superworksta-
Exhibit E-3: Graphics Intensity - 1987-90
Network
Digital
Databases
WorRotation a
Minisupercomputers
Source: 
AberdeenGroup
AberdeenGroup 125


--- Page 71 ---

eclipsed superminis through even better price/performance. By 1988, 
however, minisupercomputer supply far exceeded demand, and all but a 
few manufacturers are currently experiencing difficulties.
Shift in Computing Purchasing and Computing Paradigms
At the enterprise level, two distinct and overlapping trends are affecting 
computer purchases and usage at all levels.
Purchasing decisions have been and will continue to shift away from being 
vendor-dominated to user-specified. In a pattern that Aberdeen identifies 
as polarized buying, users are increasingly working with large suppliers of 
record (IBM, Digital) for setting enterprise-wide computer and com­
munications architectures, and at the departmental and local level, work­
ing with robust specialists (top-ranked specialist companies), such as 
workstation suppliers Ardent and Stellar.
The second trend is what Aberdeen identifies as Spoke-Node-Ring (SNR), 
where the equipment, software, and systems purchased through polarized 
buying are deployed in a pragmatic, non-traditional manner that is inde­
pendent of (and, from the user's viewpoint, superior to) any proprietary 
schemes.
While many computational chemistry users currently are insulated from 
paradigm and purchasing trends, many are not, and are frustrated by the 
delay and change that these changes impose upon them.
Complicating these trends, specifically in the scientific computing sector, 
are Digital, IBM, and Cray Research's large ambitions to impose their own 
sophisticated integrated computing paradigms onto enterprises.
Conclusion
Computational Chemistry is an exciting field fraught with conflicting and 
overlapping trends, but one in which practitioners will make major scien­
tific breakthroughs within the next decade. For nimble but patient sup­
pliers to the field, there are ample opportunities for markets and profits.
AberdeenGroup 6


--- Page 72 ---

Typical ab initio codes are GAUSSIAN, HONDO, and GAMESS, and are 
available in versions from various academic and commercial sources.
Semiempirical Method
Semiempirical codes are also based on quantum mechanics, but substitute 
for some of the mathematical terms experimentally-derived results 
("parameters," "force fields"), thereby reducing the intensity of calculations 
and permitting the study of larger molecules.
Semiempirical (partly empirical, partly rigorous) codes produce less 
rigorous results than ab initio calculations, but are more rigorous than 
those obtained by simple molecular modeling. Semiempirical methods 
are treacherous in that it is impossible to predict how far from an existing
Exhibit 2-4: Computational Chemistry Methods and Platforms
* Computational intensity increases with the power of N, where N 
is the number of active "orbits" in the molecule. Thus, an ab initio 
calculation of a 40-element molecule using an N' computational 
code would require 40' calculations g64 billion), compared to a 
molecular mechanics code using an n" program that would re­
quire a mere 1,600 calculations. The exponential rate of increase 
yields totally impracticable numbers of calculations for the ab in­
itio method, such as 100 trillion calculations for a 100-element 
molecule and 7.8 quintillion calculations (7.8 followed by 18 
zeroes) for a modestly sized 500-element molecule.
Method
Computational 
Intensity*
Number of Atoms
In Molecule
Typical
Platform
Ab initio
n4 to n7
20
Super
2
Semiempirical 
N
200
Minisuper
Molecular
Mechanics
N2 to n1
20,000
Graphics
Workstation
Source: AberdeenGroup
AberdeenGroup 12


--- Page 73 ---

Science
BioDesign has an in-house staff of 13 Ph.D.s in theoretical/computational 
chemistry. In November 1988, BioDesign announced formation of a con­
sortium to stimulate and speed the development of new polymer materials.
Computational Chemistry Products
BioDesign markets two versions (Biograf and Polygraf) of its menu-driven 
comprehensive display, modeling, and simulation program for biological, 
chemical, and materials simulations, covering different chemical needs. 
Both versions can handle up to 20,000 atoms, and can work with small 
molecules, macromolecules, and crystals. The system explicitly treats the 
entire chemical spectrum of energies, forces, geometries, and dynamics. 
Both products come with Dreiding, AMBER, MM2 and CHARMm force 
fields (energy expression and parameter sets), and calculate various chemi­
cal and physical properties.
Biograf is customized for peptides, DNA, lipids, and carbohydrates.
Polygraf is customized for polymers and related materials and solvents.
Products are sold on the basis of a perpetual license and an annual main­
tenance fee of 18% (average) of the license, which entitles users to all up­
dates. Individual product prices vary with the size of the platforms on 
which the products run. System prices range from $35,000 (for a Sun­
based system), to $65,000 to $95,000 (for a typical system), to $150,000 
(for a maximum system).
Platforms
BioDesign software runs on Sun, Digital's VAX, Silicon Graphics, Ardent, 
and Alliant platforms.
Hardware Partners
In December 1988, BioDesign and Silicon Graphics signed a VAR agree­
ment allowing BioDesign to package Silicon Graphics' complete line of 
IRIS workstations with BioDesign's software.
In June 1988, Ardent Computer and BioDesign introduced The Molecular 
Simulator, a packaged research tool aimed at theoretical and experimental 
chemists. Using Ardent's Titan superworkstation and BioDesign's Biograf, 
the system is priced at $130,000 for a single processor version and 
$165,000 for a dual processor system. Three- and four-processor versions 
are now being delivered.
AberdeenGroup 38


--- Page 74 ---

opportunity to achieve first place in computational chemistry minisuper­
computers. With 25 computational chemistry installations (and more on 
order), Alliant is a respected player in the market, but leadership is in the 
hands of Convex, which has over 60 sites.
AberdeenGroup 60


--- Page 75 ---

Exhibit A-5: Estimated 1988 U.S.Inorganic Chemical Shipments
Chlorine gas 10.1%
Oxygen 7.1%
Ammonia 15.0%
Sodium hydroxide 10.5%
Phosphoric 
acid 10.4%
Nitric 
acid 7.0%
Hydrochloric acid 2.6% 
\
Inorganic chemicals — 115 megatons
Source: 
Chemical & Engineering News
AberdeenGroup
AberdeenGroup 98


--- Page 76 ---

APPENDIXC
ROLE MODEL AND INVESTMENT ISSUES
The Importance of Industry Role Models
Far from being an esoteric issue, the way in which the computational 
chemistry industry and its financial backers view the industry has an imme­
diate impact on their conduct of the business. Vendor products, support, 
and survival — and their impact on users — are determined directly by 
answers to these kinds of questions:
Gradual, steady, but demand-limited growth? Or rapid, resource-limited 
growth?
Easy entry into the business (inviting many players)? Or costly access, 
promising healthy profits to those that survive?
Opportunities for software profits? Or price pressures induced by pro­
gram exchanges?
Open exchange of software and algorithms and data? Or highly secure 
proprietary methods and databases?
These questions are still debated by industry participants and backers 
alike. In the several layers of computational chemistry, the key layer for 
determining answers is the numerically smallest one: computational 
chemistry software. For $1 spent on software, $5 to $10 will be spent on 
hardware, and $2 to $4 on supporting services.
Investors and Aberdeen use two role models to describe and predict in­
dustry growth and prospects: CAD/CAM and finite element analysis. We 
analyze each from the viewpoint of the investor, as virtually all of the new 
software and many of the hardware companies are either privately held by 
venture capitalists (who have a vital concern about size and timing of 
profits, if any) or are newly public companies requiring continual access 
to fresh capital.
AberdeenGroup 110


--- Page 77 ---

tions (also called personal supercomputers) from Ardent and Stellar (and 
upgrades from the others) now are pushing molecular modeling 
programs to uncomfortable chemistry-theoretic limits. In the process, 
however, they also are stimulating interest from a new and necessary 
audience — the user's senior management.
Stage 4 - Industrial Strength Computing
In the flurry of excitement over superworkstations, RISC versus CISC, and 
other industry artifacts of the late 1980s, two important factors have been 
largely overlooked: industrial giant IBM and dominant supercomputer 
supplier Cray Research. These two companies are readying major cam­
paigns to increase their marketshares during each of the next several years.
The Sleeping Giant Awakens
IBM, traditionally viewed as strictly a supplier of commercial systems (busi­
ness is its middle name), has very quietly crept back into the large-scale 
computational market after years of neglect. In August 1988, IBM's in­
stalled base of Vector Facilities (attached as an integral part of System/370, 
model ES/3090s) passed Cray Research both in number of units installed 
and number of customers.
Exhibit E-4: Industrial Strength Computing - 1990-93
Network
Databases
Digital
Cray
Parallel 
Processors
Workstations
Minisupercomputers
Source: 
AberdeenGroup
AberdeenGroup 126


--- Page 78 ---

Conflicting Trends In
Computational Chemistry
WHAT IS COMPUTATIONAL CHEMISTRY?
Computational chemistry is an exciting but technically challenging field 
that promises, but not yet fully delivers, impressive cost reduction, time-to- 
market, and new product opportunities to the world's multibillion dollar 
drug, chemical, and materials industries. Computational chemistry's basic 
premise is that the processes of discovering, developing, and testing new 
drugs, chemicals, and materials (generically called "molecules" or "com­
pounds") can be streamlined by various forms of computer simulation and 
graphical manipulation at the molecular level.
Computational chemistry is the use of a variety of sophisticated mathemati­
cal, statistical, and modeling techniques applied to quantum physics' 
methods of representing chemistry. The intent is to complement, and, 
eventually, supplant experimental methods for solving chemistry 
problems. Computational chemistry was not technically possible until the 
advent of supercomputers in the early 1960s, and not economically pos­
sible for more than advanced research projects before the introduction of 
superminicomputers in the early 1980s.
New Science
In the broadest sense, computational chemistry is part of the ongoing 
scientific revolution in scientific methodology as shown in Exhibit 2-1. 
The 18th through mid-20th century two-phase development process is 
yielding to a pair of interlinked processes in which the computer is increas­
ingly the pacing element.
Current Practice
To appreciate computational chemistry, one must understand current 
methodology, which overwhelmingly dominates — in both the numbers of 
chemists and sites — the practice of chemistry today.
Traditional new product development in the many chemical industries in­
volves "wet chemistry" — easily envisioned as the stereotypical chemists in 
long white coats mixing and cooking beakers of fluids in equipment-pack­
ed laboratories. For new molecules of any commercial interest, wet 
AberdeenGroup 7


--- Page 79 ---

Conflicting Trends In
Computational Chemistry
base of actual laboratory-provided results the empirical factors can be 
used and still obtain meaningful results; precious time and resources can 
be expended pursuing promising leads that experimentation subsequently 
proves false.
Semiempirical codes are intermediate in computational intensity and can 
be run on Digital's VAX-class systems, but increasingly are run on mini- 
supercomputers and supercomputers.
Typical semiempirical codes are MOPAC and AMPAC, and are available in 
versions from various academic and commercial sources.
Molecular Modeling Method
In molecular modeling, atoms are treated as simple physical elements — 
balls interconnected by springs. In this simplified model, forces among 
elements of the molecule under study are computed using classical
Exhibit 2-5: Computational Chemistry Platforms
Databases
SupermlnIs
Mainframes
Graphics 
Workstations
Preprocessing
SupermlnIs
Ab initio methods
Supercomputers 
MlnIsupers
Semiempirical methods
Supercomputers 
MlnIsu pers
Molecular Mechanics
MlnIsupers
SupermlnIs
Experimental and 
Analytical data
C- Realtime, minis ^^=„
MlnIsupers
Molecular 
Dynamics
Source: AberdeenGroup
AberdeenGroup 13


--- Page 80 ---

Conflicting Trends In
Computational Chemistry
Analysis
BioDesign has two driving technical thrusts: software integration and 
materials (typically inorganic polymers). The first is a major challenge, 
but, for starters, the company has standardized on its own user interfaces — 
the advantage of no product history.
The second thrust is based on strong BioDesign convictions that drugs, 
while currently the area of interest, eventually will be rivaled or even 
eclipsed in scientific and financial potential by the molecular modeling of 
polymers. Goddard and his team are strongly attracted to the materials 
area, and Aberdeen expects BioDesign to concentrate its technical efforts 
on materials.
The severe challenge in materials, particularly in inorganic polymers, is 
that dozens of chemical elements must be considered (versus the handful 
in organics). However, recent experimental breakthroughs in high- 
temperature superconductors (where Professor Goddard is a leading prac­
titioner) and in claimed room-temperature fusion are but two recent 
examples of advances in materials science. Neither phenomenon is readi­
ly explained by current theories, making them ripe for innovative 
molecular modeling approaches.
Rather than compete with the four other molecular modelers, BioDesign 
seeks sales situations where it can be compared more with equally-new 
Polygon and BIOSYM than with established Chemical Design and Tripos 
Associates. As the smallest entrant with a break-even approach to busi­
ness, BioDesign must remain nimble to survive the coming shakeout.
AberdeeiiGroup 39


--- Page 81 ---

Conflicting Trends In
Computational Chemistry
Apollo Computer, Inc..
330 Billerica Road
Chelmsford, MA 01824
(508) 256-6600
Corporate Profile
Apollo was founded in 1980 by Dr. William Poduska and others to create a 
new type of computer product — the engineering workstation. The con­
cept was a winner, so much so that over the past nine years Apollo has 
been joined by dozens of others (most of whom have disappeared), in one 
frenzied round of competition after another. Apollo achieved its current 
$500 million size by using its own proprietary operating system and net­
working scheme, only to find a few years later that customers preferred 
more open systems. Apollo had a choppy 1988, with red ink and cor­
porate internal restructuring, but reannounced in February 1989 its 
lOOOOVS Series of superworkstations. In April 1989, Apollo agreed to be 
acquired by Hewlett-Packard, catapulting H-P into first place in worksta­
tions.
Statistics
Revenues
$653.5 million
Profits
$2.1 million
Assets
$496.7 million
R&D investments
$77.0 million (11.8%)
Overseas revenues
54%
Five-year CAGR
17%
Employees
4,500
Domestic sales offices
42
Overseas sales offices
61
Workstations installed
85,000
AberdeenGroup 61


--- Page 82 ---

Conflicting Trends In
Computational Chemistry
Exhibit A-6: Estimated 1988 U.S. Organic Chemical Shipments
Acrylonllrle 2.2%
Butadiene 2.7%
Acetic acid 2.9%
Phenol 3.1%
Cumene 3.9%
Ethylene 4.6%
p-Eylene 4.8%
Formaldehyde 5.4
Methanol 5.9%
Styrene 7.5%
Cyclohexane 2.0%
Acetone 1.7%
Benzene 1.4%
Other 2.9%
Propylene 17.1%
Ethylene 31.8%
Organic chemicals — 60 megatons
Source: 
Chemical & Engineering News
AberdeenGroup
AberdeenGroup 99


--- Page 83 ---

Conflicting Trends In
Computational Chemistry
CAD/CAM Industiy Model
The model for currently investing in computational chemistry is that it is 
another CAD/CAM industry expected to achieve operating profits in the 15 
percent to 20 percent range within the next few years. Supporters of this 
vision are relatively new hardware entrants, some venture capitalists, and 
the news media.
However, the CAD/CAM model of the computational chemistry market is 
generally disbelieved by most software providers and users, and by Aber­
deen; the comparison is too simplistic.
Because of the controversy surrounding the validity of CAD/CAM as the 
correct model for computational chemistry, we will review its assump­
tions, and in the second half of this appendix, the alternative finite element 
model.
Five Arguments Favoring CAD/CAM
The CAD/CAM model as applied to computational chemistry has three es­
sential elements:
1. Cost reduction. A large, tradition-bound technical area (drug/chemi­
cal "design and development") was not using modem (i.e., computer) 
tools, and was wasting billions of dollars in experimental manufacture of 
drugs/chemicals that would be scrapped, also presenting a socially costly 
disposal problem. The use of computational chemistry can be justified on 
hard-dollar savings alone.
2. Labor displacement. The shortage of skilled practitioners (Ph.D. 
chemists) can be solved by using machines and lesser-skilled chemists for 
routine tasks.
3. Time to market. Old-fashioned methods seriously delay new product 
introductions thus postponing profits and reducing investment returns.
The CAD/CAM model has two additional elements that complete the com­
putational chemistry rationale:
4. New products. Computational chemistry can assist in "designing" new 
drugs/chemicals that can't otherwise be developed using older methods. 
This yields a large bonanza to the first forward-looking firms to employ the 
new techniques.
AberdeenGroup 111


--- Page 84 ---

Conflicting Trends In
Computational Chemistry
While not a computational equal of the Cray systems, and at $300,000 a 
fraction of the price, IBM's Vector Facility is a "best buy" for users already 
steeped in IBM's cumbersome operating system protocols — provided that 
chemists can readily port their applications to it.
Because underlying IBM System/370 architecture is optimized for a broad 
mix of commercial and scalar scientific jobs, Aberdeen does not expect 
IBM to offer its own supercomputer version of an S/370 rivaling Cray.
But, IBM has an equity investment in Supercomputer Systems, Inc., with 
both parties racing technically towards a product that could challenge Cray 
as early as 1993.
Supercomputers Discover New Markets
With the literally frenzied hardware activity of the last two years devoted to 
the graphical aspects of molecular modeling, there has been a quiet but 
equally serious push in more computationally intensive aspects of com­
putational chemistry. Cray Research has installed four systems specifically 
for chemistry, hardly a large number. However, Aberdeen estimates that 
Cray will double that number within the next 15 to 18 months, thereafter 
increasing its annual number of machine placements between 40 percent 
and 50 percent per year over the next five years.
The Role of Enterprise-Wide Topologies
Each of the four hardware stages has not only built upon its predecessors, 
but has broadened the horizons of chemists who are in pursuit of new dis­
coveries and chemical development. With the enormous financial stakes 
involved, both Digital and IBM are telling major enterprises that computa­
tional chemistry is simply too important to be kept as isolated departmen­
tal or individual worker activities. Digital and IBM in their own ways are 
articulating comprehensive enterprise-wide topologies. Reinforcing their 
traditional technical and marketing traditions, each plays to its corporate 
strengths. Their respective strategies, and that of Cray, are analyzed in sub­
sequent sections of this appendix.
The Topology Wars
The topology battle between Digital and IBM, schematically shown in Ex­
hibit E-5, is far more than a battle for marketshare or profits. It is a battle 
of ideologies, pitting IBM's autocratic, hierarchical, central-control ap­
proach against Digital's democratic, organizationally flat, peer-to-peer ap­
proach. Each directly mirrors the companies' operating practices, sales 
tactics, and organizational structures.
For Digital, the user's workgroup/department is where work is per­
formed, results are accomplished, and the ultimate fate of die enterprise is 
AberdeenGroup 127


--- Page 85 ---

mechanics (Newtonian physics); Hence the name molecular mechanics. 
As seen in Exhibits 2-4 and 2-5, computational requirements are relatively 
modest, with most molecular modeling now done on superworkstations 
or workstations with a superminicomputer, minisupercomputer, or at­
tached-processor.
Typical molecular modeling codes are CHARMm, AMBER, DISCOVER, and 
GROMOS, and are available in versions from various commercial and 
academic sources.
Computational Chemistry Development
Within only 15 years, computational chemistry has gone through four over­
lapping stages of development with a fifth expected within the next year or 
so. As development proceeded, commercial software and hardware sup­
pliers began targeting the area.
Stage 1: 1970s through early 1980s — Early Explorations
Using supercomputers, chemists explored how molecules work through 
brute-force simulation of atoms using ab initio calculations. Because the 
calculations are impracticable for molecules of commercial size, chemists 
(mostly academic) relentlessly pursued alternative methods. Computa­
tions were performed on supercomputers and graphics were rudimen­
tary, when used at all.
The area was not targeted by hardware or software suppliers.
Stage 2: 1980 through 1987 — Graphics and Early Molecular Modeling 
Beginning with display terminals, chemists used computer graphics to 
visualize what previously had constituted masses of computer printouts 
supplemented by time-consuming ball-and-stick (Dreiding) models. Tech­
nical emphasis was on how to represent various atomic and molecular at­
tributes in 3-D and how to manipulate them on the screen. The process 
was largely static, yielding results that could then be processed more 
rigorously with computationally intensive chemistry software, with results 
which in turn could be modified and viewed again on the screen.
VAX-class superminicomputers provided an initial price/performance 
breakthrough for molecular modeling. Higher quality displays were 
employed, typified by Evans & Sutherland systems introduced in 1985. 
Hardware sales were brisk, while aggregate molecular modeling revenues 
were produced at breakeven. Few hardware suppliers targeted the area.
AberdeenGroup 14


--- Page 86 ---

BIOSYM Technologies, Inc.
10065 Barnes Canyon Road
San Diego, CA 92121
(619) 458-9990
Corporate Profile
BIOSYM, one of three second-generation computational chemistry 
software suppliers, was founded in 1984 by Dr. Arnold T. Hagler, head of 
the biophysics department at the Agouron Institute and consultant to 
major drug companies, and by Dr. Donald MacKay. Of the five molecular 
modeling companies, BIOSYM takes the longest view, heavily emphasizing 
science and joint projects over quarterly profits, a strategy it believes will 
make it the survivor in the anticipated molecular modeling shakeout. With 
rapid 1988 sales growth and a freshly-recruited new management team, 
BIOSYM plans to continue its rapid pace and to broaden its markets.
BIOSYM's key strength is its comprehensive grounding in science.
Statistics
Privately held, BIOSYM chooses for competitive reasons not to disclose 
financial information for publication; for customers, however, it will 
review financial data under a nondisclosure agreement. The company is 
backed by venture capitalists, is operating at a loss, and plans to break 
even by the end of 1989.
Revenues
$6 million (Aberdeen estimate)
Domestic customers
70
Overseas customers
76
Employees
72
Computational Chemistry Profile
BIOSYM places heavy emphasis on developing the frontier of computation­
al chemistry. It does this through contract work, the Potential Energy Func­
tions Consortium (see Science, below), and related "teaching of 
techniques" rather than just delivering tools. The approach is more of 
delivering "strategies for drug design." BIOSYM's product approach is 
slanted towards more rigorous molecular modeling tools (such as Dis­
cover) which become more rigorous as each round of results is received
AberdeenGroup 40


--- Page 87 ---

Computational Chemistry Profile
Apollo, by virtue of having created the workstation market, has placed its 
systems in many computational chemistry installations. As a broad-gauge 
supplier, however, Apollo has not targeted computational chemistry as a 
major market segment for specialized marketing. Apollo does have a $10 
million equipment donation program, and a significant portion of that 
goes into chemistry.
Computational Chemistry Products
The Apollo lOOOOVS superworkstation combines high-speed graphics with 
one or two processors and varying amounts of memory and I/O to solve 
computationally intensive problems locally. The lOOOOVS links with 
DECnet, TCP/IP, LU 6.2 and SNA, OSI and Apollo XNS-based systems. The 
lOOOOVS has new graphics features and functions that may help it rebound 
in molecular modeling, and is available in 40-plane and 80-plane graphics 
display models.
Selected peak graphics rates of the lOOOOVS are: 1.1 million 3-D-trans- 
formed 10-pixel vectors per second; 108,000 24-bit linear-shaded, Z-buf­
fered 100-pixel polygons per second; 24.2 million pixels per second 24-bit 
Z-buffered draw rate (41.3 ns per pixel), and 8.2 million pixels per second 
32-plane BLT (122 ns per pixel). Peak one-CPU processing performance 
is: 3.886 msec, single-precision, 1024-point complex fast Fourier trans­
form, 15 VAX MIPS, 36 double-precision Mflops, 1.5 4x4 graphic trans­
forms per second, 27,027 Dhrystones per second, and 16,954 
double-precision KWhetsones per second. Prices for the lOOOOVS range 
from $95,000 to $165,000.
Apollo has signed, but not yet announced, an agreement with one of the 
five molecular modeling software companies for supporting its products. 
Some QCPE and other public-domain code computational chemistry is 
available on Apollo systems.
Analysis
Having pioneered the engineering workstation market with a proprietary 
operating system, Apollo saw Sun Microsystems overtake it in sales, 
profits, and market share within the past two years. The new lOOOOVS su­
perworkstation is currently the top-spec'd workstation, and is Apollo's op­
portunity to make a mark in computational chemistry. Given Apollo's 
current attempts to rejuvenate itself in its base markets and return to mean­
ingful profitability, it will be hard pressed to compete on price against Stel­
lar and Ardent, who are waging a price war to gain new accounts. And, 
with Apollo's lack of focus on computational chemistry relative to its super-
AberdeenGroup 62


--- Page 88 ---

Exhibit A-7: Estimated 1988 U.S. Organic PLastics Shipments
Polypropylene 18.6%
Polyvinyl chi 21.3%
Polystyrene 13.0%
Plastics — 20 megatons
Hlgh-densIty
Polyethylene, 212%
Low-density
Polyethylene 25.9%
Source:
Chemical & Engineering News 
AberdeenGroup
AberdeenGroup 100


--- Page 89 ---

5. Better science. Computer-based interactive drug/chemical design can 
yield better scientific insights, in turn resulting in even better computation­
al chemistry programs and results.
Questionable Assumptions
On the surface, the CAD/CAM model makes sense. However, when some 
of the initial impressions are peeled away, the model is less persuasive. 
Four specific issues arise:
1. More complexity. Peeling away the outer layer of the CAD/CAM 
model, drug/chemical design and development is far more varied, com­
plex, scientifically fragmented (and of widely differing specific economics) 
than basic mechanical engineering and drafting processes. For example, 
improving part of the pesticide development process through computation­
al chemistry may not speed up the rest of it, save that much (if any) 
money, or get the product on the market any sooner. However, the con­
cept of automating science is valid; the question is to what degree in each 
specific instance and when. So far, the case remains unproven.
2. Art versus engineering. Stripping away another layer, there is a much 
more fundamental difference. Drug/chemical design and development is 
a misnomer, implying that introducing new drugs and chemicals is essen­
tially an applied engineering discipline. It is not. Rather, it is an unpre­
dictable mixture of "black art," basic science, serendipity, applied science, 
and chemical engineering and technology. The opportunity for automat­
ing these aspects, while real, is minimal.
3. Unpredictable results. Computational chemistry programs deliver ap­
proximations with unpredictable validity and accuracy, requiring skilled 
practitioners to interpret the results. Until this hurdle is overcome, large 
CAD/CAM-like markets cannot be achieved.
4. Better science. While the rationale is correct, stories of breakthrough 
insights are not forthcoming. The rationale assumes that science knows 
much more that it actually does, and that science will progress significantly 
faster through computational chemistry. The latter may occur, but most 
likely as a result of a new way of looking at chemist^? rather than auto­
mating the old.
Finite Element Analysis Model
In contrast to the CAD/CAM industry model, molecular modeling software 
suppliers and Aberdeen believe that finite element analysis is a more ap­
propriate model. Industry profits were postponed for many years, but the 
AberdeenGroup 112


--- Page 90 ---

determined. Digital works from the bottom up, and in doing so has built a 
$12 billion company in only 32 years, strictly through internal growth. As 
the second-largest supplier in the industry, it has passed by dozens of 
firms once larger and seemingly more promising.
IBM works from the top down. Enterprise strategy is out of necessity 
made at the top, and tactical decisions and goals are delegated downward. 
Communications — whether by persons or equipment — observe a chain of 
command not only for the sake of order, discipline, and accountability, 
but because IBM has found it gets better results. With its operating 
philosophy IBM, too, has grown through internal means to truly impres­
sive size — it is now a $60 billion company, and although recent growth has 
slowed, it still exceeds that of similar sized companies in other industries.
Meanwhile, Cray Research eschews ideological wars — its systems fit with 
any topology and the high price tags require Cray to obtain approval from 
all levels of the buying organization.
Exhibit E-5: Competing Enterprise-Wide Ideologies
IBM
Digital 
Equipment
/ Executives \ 
/Finance\ 
MIS
Lines of Business 
Departments 
Knowledge Workers
Source: 
AberdeenGroup
AberdeenGroup 128


--- Page 91 ---

Conflicting Trends In
Computational Chemistry
Stage 3: 1984 through 1990+ — Interactive Simulation
Overlapping Stage 2, newly developed software goes beyond symbol 
manipulation to provide rudimentary, interactive simulation of molecules 
for more timely feedback.
This still requires computationally intensive software, but is much more 
economic using minisupercomputers and workstations, both of which are 
typically displacing superminicomputers. Display systems shift heavily 
towards 3-D, with users continually changing displays; in 1988, for ex­
ample, Silicon Graphics was the display of the year.
Software introduced by three startup (1984-85) companies (BioDesign, 
Biosym, Polygen), and upgraded offerings from established suppliers 
(Chemical Design, Tripos Associates) spurs a new hardware round in 
1988-89.
Hardware sales continue briskly but erratically, with workstations claiming 
a larger market share than either minisupercomputers or superminicom­
puters. Individual software suppliers operate from modest profits to 
heavy losses. A shakeout occurs in minisupercomputers.
Stage 4: 1989 through 1990+ — Molecular Simulations
Until this stage, computational chemistry has been largely static, where in 
reality molecules are dynamic — for example, drugs often take minutes to 
fully interact with hosts. Enhanced dynamic software begins operating on 
new superworkstations (Silicon Graphics, Ardent, Stellar, Apollo) to initial­
ly perform "simulations" of molecular models.
Chemistry software will be supplied by the current molecular modeling 
companies, which begin consolidating.
Hardware emphasis is on superworkstations, the supercomputers used to 
supplement them, and minisupercomputers.
Initial attempts are made to mechanize computational chemistry along the 
lines of CAD/CAM.
Stage 5: 1992 through 2000 — Potential Scientific Breakthroughs
Using a new generation of systems incorporating the latest in small-pack­
aged minisupercomputer-class hardware and 3-D graphic workstations, 
emphasis will be on predicting chemical behavior, a goal that is thus far 
highly elusive. The "Aha! factor" — gaining insights through new methods 
of realtime graphic interaction with simulated molecules — is expected to 
produce breakthrough results in changing the way scientists understand 
and view chemistry, and in shortening the development process.
AberdeenGroup 15


--- Page 92 ---

Conflicting Trends In
Computational Chemistry
well as in foods, specific medicines, and agricultural products (insec­
ticides, herbicides).
Science
Of the five molecular modeling suppliers, BIOSYM is by far the most ag­
gressive in pursuit of new science applicable to computational chemistry, 
formally delineating it as follows:
BIOSYM 
Technologies, 
Inc.
FUNDED 
BASIC/APPLIED 
RESEARCH
1 
-------
-Potential -Trypsin 
Energy 
Functions 
Consortium -ANF
—Electrostatic L-Beta
Charges' 
Polymer Project
Thalessemia
SOFTWARE 
DEVELOPMENT
— Discover
_ Insight
— Database Structures
— Homologous Structures
— Delphi
—DMOL
Consortium Programs
CONTRACT 
RESEARCH
r Protein Engineering
— Drug Design
— Polymer Structure 
Property Prediction
Source: 
Biosym
AberdeenGrozip
In February 1986, BIOSYM created its three-year (since extended to five- 
year) Potential Energy Functions Consortium to derive and validate ac­
curate second-generation potential energy surfaces for organic, phar­
macologic, and other biomedicals. In exchange for a $30,000 annual fee 
($40,000 for recent members), members pool efforts and have exclusive 
use of the project's cumulative results for six months before the data is 
released to the public. There are currently 24 Consortium members, in­
cluding pharmaceutical firms (Abbott, Merck, Sandoz, Upjohn), hardware 
suppliers (Cray, Convex), chemical companies (Dow, DuPont, Monsanto, 
Takeda) and others.
AberdeenGroup 41


--- Page 93 ---

Conflicting Trends In
Computational Chemistry
workstation competitors, and with the delays attendant with being digested 
by Hewlett-Packard, Aberdeen does not expect Apollo to be a significant 
factor in computational chemistry before the early 1990s.
AberdeenGroup 63


--- Page 94 ---

Conflicting Trends In
Computational Chemistry
Change Now and More Change Coining
Chemical demand and supply is losing its once reasonably accurate pre­
dictability. While in dollar figures the changes are relatively small, new fac­
tors are making plant planning far more difficult, investment returns far 
less certain, and operating procedures less predictable.
Demand for some traditional chemicals is shrinking while accelerating for 
others, and in virtually all instances, the industry is under heightened pres­
sure for improved or substitute chemicals to reduce pollution, improve 
yields, reduce toxicity or side effects, and achieve competitive 
breakthroughs for using industries.
Fundamental changes are from four major sources:
• problems of overpopulation
• productivity demands
• changing consumer tastes
• scientific discoveries
Problems of Overpopulation
Population increases are the boon and the bane of producing industries. 
Obviously, more people means more markets, but not nearly as obvious is 
that more people means more waste products, less land for food, and 
dramatically changing lifestyles and workstyles to accommodate popula­
tion-induced effects.
Beneath a certain threshold, chemical and other wastes (of all kinds, in­
cluding pollution) are readily reabsorbed into local economies. 
Worldwide, and country by country, more economies are reaching ab­
solute or socially-mandated thresholds of waste tolerance. Legislation to 
correct these problems increases in complexity, severity, and implementa­
tion costs. Specific changes in related chemical demand include die follow­
ing:
Improving environmental quality. Demand for environmental improve­
ment ranges from local (smokestack emissions, industrial waste disposal) 
to regional (auto emissions, river contamination) to national (acid rain, 
deforestation) to global (greenhouse effect, ocean contamination, nuclear 
waste). The solutions to these problems are essentially chemical in nature: 
AberdeenGroup 101


--- Page 95 ---

Conflicting Trends In
Computational Chemistry
leading supplier (MacNeal-Schwendler, now 25 years old), currently 
achieves an astonishing 35 percent operating profits.
The finite element analysis model bears similarities to computational 
chemistry in several areas:
1. Limited early market. Like finite element analysis, the early computa­
tional chemistry market is limited by the scarcity of skilled practitioners. 
Worldwide, there only about 2,000 people skilled in the productive use of 
computational chemistry programs. Second-round practitioners will 
develop in 1990 onward.
2. Leading-edge technology. Computational chemistry, like finite ele­
ment analysis before it, is on the "bleeding edge" of science. This typically 
means false starts, long investment periods, and academic thrashing. How­
ever, much of the thrashing can be compressed by assuring that the 
chosen leader is able continuously to tap new academic insights as they 
occur. Unlike finite element analysis, computational chemistry could ex­
perience a dramatic conceptual breakthrough, such as (but not limited to) 
finding a way to apply the self-similarity concepts of fractals to chemistry.
3. Public sector origins. A NASA-sponsored effort nearly 30 years ago 
spawned NASTRAN, which was subsequently commercialized by a number 
of consulting companies and startups. It took many years for the industry 
to sort itself out since there was "no one in charge."
In computational chemistry, there is no direct equivalent of NASTRAN, but 
Carnegie Mellon-created GAUSSIAN is analogous. With some 300,000 lines 
of code applied to quantum mechanic (ab initio) calculations, GAUSSIAN 
is available in multiple versions but with minimal support. This severely 
limits its market, which in turn makes industrial-strength support un­
economic. GAUSSIAN users get just what early NASTRAN users did: no 
cost, but no benefits. Thus far, no one has broken the chicken-and-egg 
syndrome, making molecular modeling (as opposed to ab initio calcula­
tions) more popular than it might be otherwise.
The pressure of academically- and user-interchanged software adds to the 
uncertainty of major software profits, consequently causing venture 
capitalists to hesitate investing in computational chemistry.
4. Consulting dependency. Like finite element analysis, computational 
chemistry will require vendor-supplied expertise for many years, at mar­
gins that can be more attractive than hardware or system sales. Consulting 
sales are limited by the availability of experts.
AberdeenGroup 113


--- Page 96 ---

Conflicting Trends In
Computational Chemistry
The Users Speak
Competing for topological marketshare is a third computing paradigm — 
formalized as Spoke-Node-Ring (SNR) by Aberdeen Group, as the result of 
extensive field studies. Sketched in Exhibit E-6, Spoke-Node-Ring is not 
vendor sponsored, but a heavily user-oriented topology. Users are steadily 
moving towards SNR because it is pragmatic — it allows users to pick and 
choose among the industry's best offerings for meeting the unique needs 
of their own enterprises, while preserving integrity and continuity.
The essence of SNR is its ability to interconnect enterprise organizational 
and computational elements (where and when needed) while preserving 
relative independence of various corporate and organizational units. This 
recognizes the fact that different parts of the enterprise grow or decline at 
different rates, have widely differing technical assimilation rates, and, be­
cause of intense industry competition, vendors are seldom in step with
Exhibit E-6: Spoke-Node-Ring Topology
Spoke
Corporate 
Data Node
Productivity 
Ring
Middle
<Manager 
\Rlng
Source: 
AberdeenGroup
AberdeenGroup 129


--- Page 97 ---

Hardware offerings will cover a wide range of price and performance, and 
those still serving the market will have established profitable niches. Sur­
viving software suppliers will be modestly to quite profitable.
System integrators similar to those operating in the finite element analysis 
and CAD/CAM make real gains in mechanizing routine design problems, 
increasing the number of users by at least five times.
AberdeenGroup 16


--- Page 98 ---

BIOSYM's Polymer Project, announced in September 1988, consists of 
eight members paying $60,000 annually to support 12 BIOSYM scientists 
and programmers to collect and package the best available property predic­
tion methods for strengthening their theoretical base, thereby broadening 
their applicability. Sponsoring members will receive a suite of state-of-the- 
art modeling tools.
BIOSYM has additional contract research projects in progress, all with the 
intent of being the first-ranked in CAMD (computer-aided molecular 
design) technology.
Computational Chemistry Products
Discover is a molecular mechanics and dynamics simulation package with 
built-in applications strategies designed for simulating biological 
molecules and other polymers.
Insight is a 3-D graphics package for large-molecule systems capable of dis­
playing molecular structures in both vector and solid forms with interac­
tive manipulation in real time.
Drnol is based on local density functional theory for use in the accurate 
modeling of metal clusters, surfaces, catalysts, polymers, and large organic 
and organometallic compounds.
Delphi calculates the electrostatic field of proteins using finite difference 
methods to solve the general Poisson-Boltzmann equation.
Structure Databases Coordinates of peptide structures are modeled with 
Insight and Discover: Atrial Natriuretic Factor, Bradykinin, Endothelin, 
Substance P.
Homologous Structures are modeled with Insight and Discover: Amyloid, 
NPY (Neuropeptide Y), PYY (Pancreatic Tyrosine Tyrosine).
Products are sold on the basis of a perpetual license and an annual main­
tenance fee of 15% (average) of the license, which entitles users to all up­
dates. Individual product prices vary with the size of the platforms on 
which the products run.
Product
Price ($000) Intro
Platforms
Discover
30-100 
8/86
All following
Insight
40 
8/86
VAX, E&S, Sun/E&S,
Silicon Graphics
AberdeenGroup 42


--- Page 99 ---

Ardent Computer Corp.
880 West Maude Avenue
Sunnyvale, CA 94086
(408) 732-0400
Corporate Profile
Ardent Computer was founded in 1985 to pioneer what it calls a single- 
user supercomputer, otherwise known as a superworkstation — a high-per­
formance graphics workstation. With number two upstart Stellar, Ardent 
is challenging the high-performance graphics workstation market leader, 
Silicon Graphics. Ardent is headed by West Coast entrepreneur Alien H. 
Michaels; R&D is headed by technical guru C. Gordon Bell, father of 
Digital's VAX architecture; manufacturing is done in Japan by one of the 
company's heavy backers, Kubota Ltd.
Ardent is focusing on six specific, computationally intensive applications: 
chemistry, mechanical engineering, image processing, computational fluid 
dynamics, geography and geology.
Statistics
Privately held. Ardent Computer chooses for competitive reasons not to 
disclose financial information for publication. However, the company has 
been backed by $57 millon in three rounds of risk capital from an increas­
ing number of sources, including $44 million from Kubota Ltd. of Japan, a 
worldwide industrial equipment manufacturer.
Revenues
$15 million (Aberdeen estimate)
Overseas revenues
30% (Aberdeen estimate)
Employees
160
Domestic sales offices
13
Overseas sales offices
5
Overseas distributors
3
Systems installed
300 (Aberdeen estimate)
Computational Chemistry Profile
Ardent Computer is quite serious about computational chemistry, one of 
its top sales generators. In addition to marketing a packaged molecular 
AberdeenGroup 64


--- Page 100 ---

reduce the amounts used, change to different chemicals, or alter existing 
ones.
Not only are new chemicals and chemical processes required for improv­
ing environmental quality, but more are needed to detect potential con­
taminants that increasingly interact with each other, and to detect finer 
levels of concentration.
More effective food production. The best land was put into production 
decades ago. With increasing populations, not only is productive farm 
land being developed, but marginal or submarginal land is drafted into 
agricultural use. The rate of improvements is decreasing in "green revolu­
tion" gains made through improved herbicides and pesticides, growth hor­
mones and regulators, and fertilizers. Demand for better, safer, and less 
complex versions of these chemical tools continues to be high.
More efficient energy recovery and sources. In the complex global 
energy equation, new chemicals and chemical processes are required for 
petroleum refining, secondary crude oil recovery, and conversions of 
biomass, solar, and hydrocarbon sources to standard forms of delivery.
Productivity Demands
The global economy offers few hiding places for the inefficient — modern 
communications, transport, and financial engineering have seen to that. 
The quest for increased productivity at all levels of society ultimately rests 
on new products based on new materials (made through new processes) 
made from new or improved chemicals and feedstock, including the fol­
lowing:
New materials. An area of new demand that potentially rivals that of exist­
ing health demand (see below) is in new materials and the products achiev­
able from them. Still in early stages, demand will be strong for better 
plastics, polymers, composites, liquid crystals, optical materials, ceramics, 
and semiconductors. A further demand is for similar materials that per­
form well under wider environmental conditions. If and when low- 
temperature superconductors become a reality, demand for this segment 
alone will be massive.
New processes. All of the new demands strain current chemical engineer­
ing processes, requiring in turn new chemicals — particularly catalysts -- to 
turn laboratory discoveries into delivered products.
AberdeenGroup 102


--- Page 101 ---

5. Initially crowded field. Computational chemistry software, like the 
early finite element analysis field, has a second tier of several minor sup­
pliers who will shake out as the large firms fail or succeed in becoming 
robust corporations. Currently, the second tier is selling software on per­
sonal computers, in effect stimulating earlier second-level scientist par­
ticipation on which the larger firms can capitalize.
Finite Element Analysis A More likely Outcome
Aberdeen Group finds the finite element analysis more compelling than 
CAD/CAM, which assumes that computational chemistry is an engineering 
process (i.e., predictable outcomes within reasonable bounds). In reality, 
the computational chemistry process is one of scientific search and dis- 
coveo?.
Investment Issues
Independent of which industry model is viewed as appropriate, the com­
putational chemistry sector has a very uneven financial profile — a strong 
sign of potential instability and shakeout. The sectors are listed in order of 
increasing financial stability:
Molecular Modeling Software Suppliers — Too Many Too Soon
There are five commercial molecular modeling suppliers collectively sell­
ing $27 million (1988 revenues) in products and services. That level of 
sales normally would provide a decent living for one software company, 
and an inadequate return if spread among three. Unsurprisingly, the 
group as a whole is losing money, and will not collectively break even 
prior to one or more dropping out (or combining) or until they achieve a 
solid $50 million to $70 million in sales.
The consolidation process is just underway, with Polygen strengthening its 
hand by accepting a minority investment from IBM.
Two major factors are working against near-term profits: incomplete 
products (the nature of the business), and very few fresh buyers (early 
adopters all have computational chemistry systems and the next wave 
doesn't know how to use the mostly handcrafted systems).
Superworkstations — Betting on Advanced Scientific Software 
Assuming that powerful, single-user, high-performance graphics worksta­
tions would generate quick sales, superworkstation suppliers have tar­
geted less than a handful of very advanced scientific applications to make 
their own fortunes. Computational chemistry is key among them. With 
AberdeenGroup 114


--- Page 102 ---

each other. SNR combines elements of IBM's and Digital's topologies 
without endorsing either.
For computational chemistry, Spoke-Node-Ring is slower in being adopted 
— the need for interconnectivity is less compelling than in commercial ap­
plications, and traditionally strong rivalries between MIS and technical 
users have slowed adoption. However, the Digital-IBM topology wars will 
force the issue, beginning as early as 1989 in sophisticated enterprises.
Digital: Total Technical Integration
From Hardware to Software to Systems Integration
Having pioneered affordable, low- to medium-priced technical computing 
for the entire spectrum of engineering and scientific disciplines. Digital is 
expanding its role to that of a seamless systems integrator. It is a lengthy, 
more difficult process than making and selling program development tools 
or faster processors. Digital's ambitious goal is nothing less than what it 
terms Computer Integrated Research (CIR) — "a comprehensive computing 
approach designed to integrate laboratory and research activities from the 
lab bench to the supercomputer." If successful, this strategy will not only 
allow Digital to remain a preeminent supplier to the technical community, 
but will deflect some of its intense competition with startup "hot box" sup­
pliers who have increasingly been winning molecular modeling bids.
Digital's Vision of Computer Integrated Research
As a very large technical organization itself. Digital sees two pragmatic for­
ces driving CIR:
First, over the lengthy course from research to product development to 
production to sales and support, information must be shared by others 
within and without the enterprise, shared at the right time in the right form 
with the appropriate people. Further, organizational synergies are better 
achieved by cooperation among working groups than by isolation. Digital 
is a leading practitioner of this philosophy, and thus strongly believes that 
it can help achieve similar productivity gains for its users.
Second, heterogeneous aggregations of computer equipment obtained 
over as many as two decades work poorly together, if at all, unless careful 
attention has been devoted to making it happen. This is one of 
management's more difficult challenges, one which can make the dif­
ference between the enterprise's success and mediocrity.
AberdeenGroup 130


--- Page 103 ---

Conflicting Trends In
Computational Chemistry
CHAPTERS
MARKET SIZE AND GROWTH
Overall Market Size and Growth
The overall computational chemistry market for direct hardware and 
software sales in 1988 was $237 million, up 35 percent from 1987. In 
1989, it is expected to increase 31 percent to $311 million.
Over the next five years, Aberdeen estimates overall annual market growth 
at 35 percent, with annual variations as much as 15 percentage points 
around that average, for reasons discussed below. Aberdeen expects 1993 
combined sales to be at the billion dollar level. Our market estimates are 
shown in Exhibit 3-1.
Five molecular modeling suppliers (profiled in Chapter 5) and over 20 
hardware suppliers (13 profiled in Chapters 6 and 7) are pursuing the 
computational chemistry market, each with its own strategy and tactics. 
Other market participants — commercial as well as not-for-profit — are 
primarily timeshared supercomputer centers, which are not discussed in 
this study.
Exhibit 3-1: Computational Chemistry Estimated Revenues
Suppliers
1987 1988 1989 1990 1991 1992 1993
1994
Software
16
27
36
50
70
95
125
170
Hardware
160
210
275
380
500
650
900
1,200
Total
176
237
311
430
570
745
1,025
1,370
Source:
AberdeenGroup
AberdeenGroup 17


--- Page 104 ---

Conflicting Trends In
Computational Chemistry
DMol 
50/75/100 2/88
Cray, Digital VAXcluster,
Silicon Graphics
Delphi 
20-30 
4/89
VAX, E&S, Convex, Silicon Graphics
Structure
Databases 10 
4/88
VAX
Homologous
Structures 10 
12/88
VAX
Hardware Partners
In March 1988, BIOSYM became a Digital CMP partner, as well as a Silicon 
Graphics Geometry partner.
Analysis
BIOSYM recently recruited a new management team from the CAD/CAM 
and medical electronics sector to make the transition from technical start­
up to commercial supplier, a necessary move. By using a three-part sales 
mix of software, hardware, and consulting, the company is spreading out 
its risk while investing heavily in new science.
BIOSYM's key strength is its comprehensive grounding in science.
Aberdeen views BIOSYM as a long-term computational chemistry supplier, 
external financing permitting.
AberdeenGroup 43


--- Page 105 ---

Conflicting Trends In
Computational Chemistry
modeling product (Titan Chemistry Server — see below), Ardent has hired 
Ph.D. chemists and is exhibiting at chemistry conferences.
Computational Chemistry Products
Ardent's Titan family of computers integrates 64-bit minisupercomputer 
power with high-performance 3-D graphics in an interactive processing en­
vironment. The Titan is a multiprocessor system, with up to four proces­
sors. Each processor can deliver 16 Mflops peak performance in a single 
unit, while the vector/scalar processor can deliver 16 MIPS per unit. Up to 
128 MB of storage are available. Prices range from $75,000 to $200,000.
Graphics performance peak rates are 200,000 Gouraud-shaded Z-buffered 
triangles per second per system; animation of 10,000 Gouraud-shaded tri­
angles per frame at 15 frames per second; shading rate of 50 million pixels 
per second.
Ardent's high-level graphics software tool, Dore, interfaces to PHIGS, and 
PHIGS-I-. The Titan supports networking media and protocols Ethernet, 
TCP/IP, and others.
Ardent has a VAR relationship with BioDesign to offer Biograf and 
Polygraf, in the Chemistry Server. Prices begin at $130,000. Ardent sup­
ports BioDesign's Biograf, Polygraf, AMBER, ESS, Gaussian88, and 
NMR1/NMR2. Available software includes "0," XPLOR, AMPAC, MOPAC, 
and Hare Research's FTNMR and DSPACE.
Analysis
Ardent is aggressively pursuing computational chemistry, with many staf­
fers having connections to the industry. With impressive technical depth 
as well as financial backing from very deep Japanese pockets. Ardent is 
well positioned to gain hardware market share in computational chemistry.
AberdeenGroup 65


--- Page 106 ---

Conflicting Trends In
Computational Chemistry
Changing Consumer Tastes
While changing consumer tastes have always affected specific chemical and 
product demand, modern mass communications have shortened product 
life cycles. Further, mature economies such as North America and 
Europe, in aggressively seeking out export markets, are finding local condi­
tions and demand profiles less predictable than domestic. Some specific 
changes in consumer demand include the following.
Improved food quality. The search for safer, less intrusive food addi­
tives and preservatives for processed food is intense. Emotionally more 
immediate (we all eat every day) than environmental issues (more abstract 
unless the pollution is in our backyards), demand is high for chemicals 
that can meet increasingly stringent government regulations.
Better health. In no other area of new demand has the search for new 
chemicals been as intense, nor more in the forefront of new technologies 
and computational methods, than in the health-related fields of phar­
maceuticals, disease detection, prevention and control, and in wellbeing re­
search and application. The intensity is a result of newly overlapping 
discoveries and scientific paradigms among biology and chemistry subdis­
ciplines. Computational chemistry in general, and molecular modeling in 
particular, has driven, and in turn is driven by, pharmaceutical discovery 
and design.
Scientific Discoveries
Both independent of (and often funded by) economic and geopolitical fac­
tors, science relentlessly pursues new discoveries. The unknown in 
science far exceeds the known, academic posturing and press agentry 
aside, and is exemplified by the current acrimony and confusion over 
whether fusion has been discovered at room temperatures. Further, at 
any given moment, science cannot readily distinguish between what will 
remain forever beyond our grasp and what simply is unknown through 
lack of suitable instrumentation or theory. The consequence is that 
science provides an open-ended, nonquantifiable source of new chemi­
cals, processes, products, techniques, and solutions to the challenges 
listed above. (See Appendix B, Science Issues).
AberdeenGroup 103


--- Page 107 ---

Conflicting Trends In
Computational Chemistry
the volatility of molecular modeling software, and the seriously limited 
resources of molecular modelers to port the large number of packages, su­
perworkstation placements have been tougher than suppliers expected.
Currently, Silicon Graphics dominates this market, having quietly taken it 
away from Evans & Sutherland, who was just as dominant a few years ago. 
Newcomers Stellar and Ardent have jumped into the fray, and in February 
1989 Apollo reentered an already crowded field.
Collectively, Ardent and Stellar — just beginning product shipments in 
1988 — are losing money, with users asking for, and receiving, substantial 
discounts for running the risk of purchasing potential orphan systems. 
(This type of user behavior has been known to induce a self-fulfilling 
result).
Minisupercomputers — The Shakeout Nearly Over
Minisupercomputers are well into the shakeout phase. Convex is growing 
profitably and Multiflow is growing as it seeks a merger partner or fresh 
capital, while the rest have plateaued and/or are operating at losses, with 
Scientific Computer Systems the latest to quit the business in February 
1989.
Digital, IBM, and Cray — The Big Get Bigger
These three firms are collectively healthy, earning good to excellent 
profits, and have massive asset bases to both ride through economic and 
industry downturns and help weather the shakeouts of smaller firms and 
gain marketshare from the experience.
How Long Will Instability Last?
Near and medium term, the following factors are a drag on earnings, 
which in turn place financial backers in the position of abandoning their in­
vestments, or doling out a few more dollars in hopes that their individual 
company will survive:
• High selling costs. Current buyers are Ph.D. chemists 
who typically will buy only from other Ph.D. chemists. 
The state of the software makes this a necessity.
• High support costs. Program and algorithm 
development is never complete in science (in contrast to 
engineering, where refinements can be made and 
features added).
AberdeenGroup 115


--- Page 108 ---

Conflicting Trends In
Computational Chemistry
Implementing CIR
Digital's overall system framework is its continually evolving architectural 
elements: VAX architecture, VMS operating system and tools, and DECnet 
communications, illustrated in Exhibit E-7.
Exhibit E-7: Digital's System Topology
Enterprise
Workgroup
IBM 
Mainframe
Central 
Databaae
VAX 8800
Other brand 
Workstation
Other brand 
Supermini
Cray 
Supercomputer
VAXatatlon
Other brand 
Workstation
MicroVAX
Departmental 
Server.
Source:
Digital Equipment
AberdeenGroup
AberdeenGroup 131


--- Page 109 ---

Other established companies are waiting on the sidelines, and venture 
capitalists would consider funding new operations provided there were 
substantial product differentiation or a more profitable approach than cur­
rently exists.
Market Mechanism
The market for computational chemistry is a three-stage, interactive 
process (illustrated schematically in Exhibit 3-2), in which fundamental 
science drives software producers to incorporate the latest discoveries, 
which in turn drives hardware manufacturers to deliver new and better 
equipment to run the latest applications, which leads to new scientific dis­
coveries.
The process is uneven and choppy because science is uneven in its rate of 
progress and dissemination of results. Computational chemistry software 
and hardware markets also have been uneven. And with several complex 
and often conflicting trends (detailed in Appendices A through F), overall
Exhibit 3-2: Computational Chemistry Market Mechanism
Scientific 
progress
New 
computers 
and 
displays
New 
software 
and 
applications
Source: 
AberdeenGroup
AberdeenGroup 18


--- Page 110 ---

Chemical Design Ltd
7 West Way, Unit 12
Oxford 0X2 OJB, England
(0865) 251483
Corporate Profile
200 Route 17, Suite 120
Mahwah, NJ 07430
(201) 529-3323
Founded in 1983 by Keith Davies, an Oxford chemistry postgraduate, 
Chemical Design was one of the first commercial molecular modeling 
irms and currently has the largest installed base.
Tie company's Chem-X modeling software is used in a wide range of re­
search areas, including petrochemicals, agrichemicals, protein engineer­
ing, and polymer modeling, as well as drug design. The software is
► updated regularly (currently four times a year) and new modules focusing 
on developing areas of chemistry interest are released about twice a year. 
Chemical Design also sells and supports a range of turnkey systems, and 
offers training and consulting services.
Statistics
Chemical Design is privately owned but makes available audited financial 
statements upon request. The company was financed by its founders and 
funds its growth through profits. The company has been profitable for
several years.
Revenues
$6 million
Domestic customers
125
Overseas customers
175
Employees
60
Computational Chemistry Profile
Chemical Design's modeling software covers a broad spectrum of applica­
tions, from small molecules to proteins and polymers. The company 
recently expanded into chemical information management products.
Science
Chemical Design has a staff of 15 home-office and field-based Ph.D.
chemists who collaborate in software development with scientists at its 189
AberdeenGroup 44


--- Page 111 ---

Convex Computer Corporation
701 North Plano Road
P.O. Box 833851
Richardson, TX 75083-3851
(214) 952-0200
Corporate Profile
Convex was founded in 1982 to produce "affordable supercomputers," 
shipped its first C-l systems in 1984, and began shipments of its second 
generation C-2 series in mid-1988. With an installed base of over 400 sys­
tems by 275 customers in 24 countries with a value of $200 million. Con­
vex is now the clear frontrunner in sales, profits, and installed base of 
minisupercomputers.
In 1988, Convex grew 52 percent in the vicious price-cutting minisuper­
computer business (only much smaller Multiflow did the same), and in­
creased its marketshare in computational chemistry. Convex leads all 
other minisupercomputer suppliers in this field by a two-to-one margin, 
with over 65 installations worldwide.
Statistics
Revenues
$105.6 million
Profits
$5.7 million (5.4%)
Assets
$161.1 million
R&D investments
$13.6 million (12.9%)
Overseas revenues
50%
1988 revenue growth
52%
Employees
700
Worldwide sales offices
42
Overseas distributors
17
Computers installed
400+
AberdeenGroup 66


--- Page 112 ---

Science is making exponential progress in discovering and producing new 
chemicals. This is evident in the reduction of the time between doublings 
of known chemical compounds (see Exhibit A-8).
While the number of known compounds went from 2 million to 4 million 
between 1950 and 1970, the number doubled again only 10 years later.
Modem development tools and techniques promise doublings at no more 
than 10-year intervals, despite the laborious and time-consuming proces­
ses required for developing each individual chemical.
One such example of demand from scientific discoveries is biotechnology.
Biotechnology. The emerging and financially-troubled biotechnology in­
dustry is a potential major factor in new chemicals and processes, but has 
been hampered by the enormous complexity of DNA as well as increasing 
societal concerns over potential runaway artifacts. Protein and enzyme re­
search, as well as bioengineering, are expected to eventually stimulate 
enormous demand for new chemicals; however, timing is conjectural.
Exhibit A-8: Accelerating Rate of New Chemical Discovery
AberdeenGroup
Source:
1940
+
1960
1980
National Academy of Sciences
Number of Known 
Compounds in 
Millions
U---I— 
1920
2000
10
8-
6-
4-
2-
AberdeenGroup 104


--- Page 113 ---

• Limited staff. There is a chronic shortage of Ph.D.s 
skilled in computational techniques. Many Ph.D.s are 
being recruited (and bid up) by software and hardware 
makers. The graduation rate of all new Ph.D.s has been 
declining since the post-Sputnik boom of the 1960s.
• Market Saturation. The first-round drug-researcher 
market is saturated. New science is not generated 
overnight, new tools notwithstanding. Junior-level 
chemists are not up to speed, and unless trained in 
physics (a minority) and mathematics (another 
minority), a second round will not boom immediately 
with the exception of superworkstation supply-driven 
upgrades of first-round sites.
Longer term, the shakeouts will end, second and third tiers of users will be 
developed and satisfied, and profitable growth will surge. Until that time, 
in the 1990s, the computational chemistry industry will be one of the 
haves and the have nots, and one where investment capital is at extraordi­
nary risk.
AberdeenGrozip 116


--- Page 114 ---

In implementing its CIR strategy within the framework, Digital continues 
developing and deploying numerous programs, products, and practices — 
short-, medium- and long-term — to assure eventual acceptance and 
dominance of its vision. These are of two overlapping classes: those 
covering a broad range of technical applications and markets, and those 
specific to research, laboratories, and computational chemistry. These 
cost money, and accordingly few are offered by smaller suppliers, and are 
rivaled only by IBM and Cray. Current programs, products and practices 
include:
• Data interchange. Accomplishing transparent data 
flow among diverse parts and locations of the 
enterprise, based on DECnet and OSI (including X.25) 
standards.
• Cooperative marketing partners. Third-party 
hardware and software manufacturers who meet 
stringent financial, technical, and operating standards, 
and who commit substantial resources to working 
closely with Digital in optimizing solutions for Digital 
platforms.
• Applications For Science (AFS). A program that 
integrates into the Digital environment key applications 
developed by academic and government 
laboratory-sponsored research projects.
• Applications for Science Program (AFS). Selected 
third parties who port their applications to Digital, but 
under somewhat less exacting conditions.
• VAXlab data acquisition and analysis systems.
Integrated laboratory systems as part of the CIR system.
• VAX LIMS/SM sample tracking system. Also 
integrated into CIR.
• Gateways to Cray supercomputers, which treat the 
Cray computers as compute servers.
• Gateways to IBM, which make corporate data available 
to the system as required, and vice versa.
• Digital-sponsored university research programs.
Funded projects conducted by technical universities or 
departments worldwide in computational chemistry, 
scientific visualization, supercomputing technology, and 
networking.
AberdeenGroup 132


--- Page 115 ---

Conflicting Trends In
Computational Chemistry
computational chemistry for some years will remain both difficult to quan­
tify and to anticipate.
Software Segment Market Base
Worldwide, molecular modeling software installations numbers about 
350, and are growing modestly. About 120 are industrial and 230 are not- 
for-profit, including various governmental agencies. This is a small base 
market that consists almost entirely of early adopters.
The five molecular modeling companies (BioDesign, BIOSYM, Chemical 
Design, Polygen, Tripos Associates) are planning to expand beyond early 
adopters to less sophisticated users within the same buying institutions, ex­
pecting to at least double the number of sites within three years. Ac­
complishing this requires continuing software development to make 
molecular modeling usable by less than Ph.D.-level chemists.
The market for first-round molecular modeling products was dominated 
by Chemical Design and Tripos Associates, who are in varying stages of 
product upgrade and expansion as they compete with relative newcomers 
BioDesign, BIOSYM, and Polygen. All five tend to target the same cus­
tomers, with high expectations that early adopters will induce others 
within their organizations to try the new technology, thereby multiplying 
the overall sales potential. There are a few signs that this may occur by 
late 1989.
Software Segment Size and Growth
Software, consulting, and hardware sales by the five molecular modeling 
companies totalled an estimated $27 million in 1988, an estimated 65 per­
cent increase from 1987. The estimated market shares of the five 
molecular modeling companies for 1987 are shown in Exhibit 3-3, and es­
timated 1988 shares are shown in Exhibit 3-4.
Aberdeen estimates that 1989 growth will be 30 percent to 35 percent, with 
a single-figure estimate of $36 million; growth in 1990 and beyond is es­
timated at 35 percent, plus or minus five percentage points in any given 
year.
The large 65 percent gain in 1988 was the direct result of newly available 
second-generation molecular modeling programs, and indirectly the result 
of several hardware startups that offered new platforms to early-adopting 
but conservative buyers.
Near term, the software market is heavily hardware driven. A new genera­
tion of displays, graphics workstations, and compute servers was intro- 
AberdeenGroup 19


--- Page 116 ---

Conflicting Trends In
Computational Chemistry
installed academic/research sites over a very broad range of modeling ap­
plications.
Computational Chemistry Products
Chemical Design's Chem-X modeling system is modular in structure, per­
mitting users to purchase only those elements needed. The basic system 
of five modules (ChemCore, ChemGuide, ChemModel, ChemMovie and 
ChemDBS-1) provides the ability to build, display, and manipulate virtual­
ly any chemical structure in 3-D, and also offers advanced facilities for con­
formational analysis, spatial analysis, and energy calculations.
Specialized add-on modules include ChemQM, a transparent interface to a 
range of quantum mechanics programs; ChemProtein, which provides 
tools for protein modeling including proprietary protein-building 
routines; ChemStat, designed for studying structure/activity relationships; 
ChemLab, which allows Chem-X to be readily interfaced to other 
programs and to be customized; and a transparent interface to public- 
domain AMBER.
Products are sold on the basis of a perpetual license and an annual main­
tenance fee (12 percent average) of the license which entitles users to 
regular updates. Pricing varies with the number of modules purchased 
and the number of simultaneous users. The suite of five basic modules 
for four users is priced at $56,000. Add-on specialist modules ChemQM, 
ChemProtein, ChemStat, and ChemLab are priced at $13,200 each, and 
ChemProtein for $26,400. A site-wide license for most modules costs 
about $55,000 each. Academic discounts are available.
Chem-X runs on all Digital VAX/VMS systems. Graphics platforms include 
Star Technology's Graphicon raster graphics system and Tektronix and Sig- 
mex raster-scan systems. Chemical Design is the first computational 
chemistry supplier to adopt Digital's new high-resolution 3-D VAXstations 
3520 and 3540. The company has also developed the first Transputer- 
based parallel processing system for molecular modeling (MITIE), with 
performance ranging up to 360 MIPS. Prices range from $80,000 to 
$300,000. Chemical Design offers fully integrated computational 
chemistry workstations running Chem-X with discounted software 
bundled in.
Analysis
Chemical Design was one of the two pioneering commercial molecular 
modeling companies, with a continually strong European presence 
derived from its United Kingdom base of operations. It has since seen new
AberdeenGroup 45


--- Page 117 ---

Conflicting Trends In
Computational Chemistry
Computational Chemistry Profile
Convex pursues a wide range of computational chemistry applications 
from quantum chemistry through semiempirical to molecular modeling. 
It does this by collaborating with leading software authors at the scientific 
and algorithmic stages of computational chemistry development, and has 
installations in numerous universities, although these are less profitable 
than commercial sales.
Convex's aggressiveness has paid off, with 65 to 70 computational 
chemistry installations (many with multiple computers) that increasingly 
are won in competition against IBM and Cray rather than other minisuper­
computer suppliers.
Convex believes that computational chemistry is the potential black hole of 
computing — there are not enough CPU cycles in the universe to solve all 
problems rigorously. In frustration, many algorithms have been 
developed for the vast installed base of VAX-class machines, but with 
results that Convex believes have been severely compromised. Convex 
believes that improved algorithms can reduce computational requirements 
by a factor of ten, but with considerably less reduction in chemistry in­
tegrity. By positioning itself somewhat beneath supercomputers, but well 
above superminicomputers. Convex is in an excellent position to reap the 
fruits of such algorithmic refinements. To turn this into computational 
chemistry system sales, Convex has several scientists, including three 
Ph.D.s, on its central technical staff and is adding more.
Available computational chemistry software on Convex systems includes 
molecular modeling: Amber, Brugel, Cedar, CHARMm, Discover, 
Gromos, and X-plor; conformational search: MacroModel, SYBYL/MEN- 
DYL; ab initio: Cadpac, GAMESS, GAUSSIAN 86; semiempirical: 
MOPAC/AMPAC, V-Amp; crystallography: Protein, Refinement; nuclear 
magnetic resonance: D-Space, FTNMR; other: MM2, Cambridge crystal­
lographic Database, Corels, Disgeo. In 1989, Convex will announce 
several other packages.
Computational Chemistry Products
Convex offers the C Series of minisupercomputers, 64-bit integrated 
scalar/vector processors executing concurrently. Using 20K CMOS and 
Fujitsu lOK ECL gate arrays, the machines are air cooled, minimizing floor- 
space requirements. Multiple processors, up to 2 GB of memory, and 
I/O, are interconnected by high-speed busses, and are accessible by inter­
faces to standard busses and protocols — Multibus and VME, Ethernet, 
TCP/IP, NFS, and Hyperchannel.
AberdeenGroup 67


--- Page 118 ---

Conflicting Trends In
Computational Chemistry
APPENDIXB
SCIENCE ISSUES
Computational chemistry is advancing quickly and unevenly. In spite of 
impressive progress, there are several factors that impede, given today's 
imperfect state of knowledge. These are often overlooked in popularized 
news articles and unwary marketing plans. Indeed, there is a sharp con­
trast between the ebullient hopes, expectations, and beliefs of computation­
al chemistry evangelists (typically hardware and some software vendors) 
and those of leading practitioners. A major difference lies in their respec­
tive understanding of science and its subdisciplines of biology, chemistry 
and physics.
The Practice of Science
Science is the combination of the process of searching for the unknown, 
the accumulation of a steadily increasing body of knowledge, and the 
presence of a large community of skilled and motivated practitioners. In 
practice. Science also has a belief structure, holding certain tenets and 
propositions to be true, or at least preferable to contrary views. Collective­
ly, the scientific community calls these "Science" — colloquially with a capi­
tal "S".
Science operates under rigidly prescribed rules for experimental 
protocols, methods, forms and timing of publication of results, and ways 
of testing whether new results conform to current theory.
Ruling Paradigms Foster Conservatism
Development of new scientific knowledge tends to follow a model 
(adapted from one of the variants of modem biological evolutionary 
theory) known as punctuated equilibrium: progress consists of long 
periods of quiet, incremental progress (building on prior discoveries), in­
terspersed with occasional periods of major breakthroughs. Incremental 
progress is fostered and made possible by Science's adoption of common­
ly-agreed to sets of theories — called paradigms. Some paradigms cover all 
of science, others cover specific disciplines.
AberdeenGroup 105


--- Page 119 ---

Conflicting Trends In
Computational Chemistry
APPHYDIXD
THE DRUG DEVELOPMENT PROCESS
The drug development (discovery) process is extremely costly and time 
consuming, with success odds so low that oil wildcatters have "sure things" 
by comparison. The reason is inherent to chemistry as we know it, as 
reviewed in Appendix B. Even though the drug industry is enormously 
profitable, it has been consolidating worldwide for some years to reduce 
costs and achieve better economies of scale, the most recent example 
being the merger of Smith-Kline and Beecham Group.
In spite of intrinsic difficulties, the goal of drug discovery is to produce a 
new molecule (the generic name for a bewildering array of proteins, en­
zymes, polymers, peptides, and other assemblages of atoms) that will 
produce a desired chemical effect accompanied by acceptably low levels of 
toxicity. (Any molecule is toxic if applied in sufficient dosage under cer­
tain conditions).
Four-Stage Process
The discovery process is essentially one of continual trial and error, begin­
ning with a highly educated and debated guess. Typically, molecule 
design/discovery consists of four successively more costly stages as il­
lustrated in Exhibit D-1.
At any stage, the process can be stopped if positive results are improbable.
Stage 1. The researcher targets an area of chemical "activity" (the proper­
ties or reactions being sought), so that (in Stage 2) he/she can build some 
experimental variations to see if they confirm their predictions. Since the 
Stage 2 process of building the molecule in the lab can take from a few 
days to a year or more, the researcher prepares a short-list of molecules to 
build, trading off turnaround time with predicted probabilities of activity. 
(In Stage 3, the candidate molecule is refined further, hopefully yielding a 
marketable product).
In Stage 1, the researcher faces a fundamental choice, one with continuing 
downstream implications: start with a fresh slate and build a brand new 
molecule, or examine variations on known molecules, hoping to take ad- 
AberdeenGroup 117


--- Page 120 ---

Conflicting Trends In
Computational Chemistry
scientific visualization, supercomputing technology, and 
networking.
• Application Centers for Technology (ACT). Over 40 
centers providing applications support by science 
consultants in several scientific disciplines, with 
molecular modeling supported in Atlanta, Chicago, 
Houston, Philadelphia, and Santa Clara.
• Sales support specialists. Over 100 persons in sales 
offices throughout the world, offering additional 
scientific application support.
• Conference and training seminars. Conducted both 
in vertical applications including molecular modeling, 
and in concert with professional organizations including 
the Quantum Chemistry Program Exchange (QCPE).
Integrated Laboratory Automation (ILA)
Reaching beyond individual applications. Digital is quietly but firmly 
promoting its ILA program, which interconnects all aspects of laboratory 
computation and processing (see Exhibit E-8). ILA is more than marketing 
flash — Digital has a steadily increasing number of instrumentation com­
panies adopting its standard. Within the lab automation community. Digi­
tal is as much as five years ahead of such instrumentation stalwarts as 
Hewlett-Packard and Perkin Elmer.
For computational chemistry practitioners, ILA will become a serious con­
sideration once computational chemistry moves from its current pioneer­
ing stage into product development.
Scientific Visualization
Digital's CIR vision — specifically including molecular modeling — includes 
scientific visualization, both as an intellectual process and as embodied in 
specific software and hardware tools. More than "hot graphics," Digital 
views scientific visualization as the fundamental way in which science will 
be conducted in the 1990s. Digital is supporting numerous research ef­
forts to bring this about, but, to date, its efforts have been publicly eclipsed 
by the considerable fanfare surrounding superworkstations.
Digital's model of scientific visualization (See Exhibit E-9) pictorially sum­
marizes the research process:
• Conceptualization — problem definition and problem 
formulation 
AberdeenGroup 133


--- Page 121 ---

duced during 1987 and 1988. As a result, each of the molecular modeling 
companies should achieve some growth in 1989.
There is a real but unquantifiable risk of user indigestion in 1990, fol­
lowed by a buying pause in late 1990 or 1991. With each of the five expect­
ing growth in the 40 percent to 100 percent range, it is unlikely that all five 
molecular modeling companies will meet their 1989 sales projections.
Software Pricing Practices and Sales Volume
Two specific pricing practices have limited overall software revenues: 
deep discounting to not-for-profit institutions, and the use of perpetual 
licenses.
The typical molecular modeling package sells for about $100,000 for a per­
petual license, with an annual maintenance fee of 12 percent to 17 percent.
Exhibit 3-3: 1987 Market Shares-Molecular Modeling Suppliers
BIOSYM 18.3%
Chemical Design 30.5%
BioDesign 6.1%
Tripos 11.6%
Polygen 33.5% I
$16.4 Million Total Revenues 
Source:
Aberdeen Group
AberdeenGroup 20


--- Page 122 ---

entrants crowd into the field and has responded by adding new types of 
modules and by branching into allied areas.
Chemical Design's approximately semi-annual new product releases 
generate profitable incremental sales to existing customers and expand the 
segments where the company can win new business. However, with the 
industry's largest installed base, and with the computational chemistry 
market still in the early-adopter stage, adding new accounts is neither easy 
nor voluminous. Hence the second stratagem of branching out into other 
areas.
Chemical Design now sells in the United States the ORAC reaction database 
and the OSAC structure database, both U.K.-based products. Expanding 
further, in mid-1989 the company plans to introduce a corporate-level 
chemical information database and report generator product. These ven­
tures place Chemical Design in direct competition not only with the other 
five molecular modeling companies, but with heavyweight Molecular 
Design, and, depending upon the details of the mid-1989 announcement, 
system suppliers Digital and IBM. The contest may well be more than 
Chemical Design expects.
Chemical Design's key strengths are its large installed base of worldwide 
customers, the wide-ranging functionality of its software, and the 
program's modular structure, which makes it inexpensive and easy to ex­
pand.
AberdeeriGroup 46


--- Page 123 ---

Processors range in performance from 20 to 200 Mflops, and range in 
price from $275,000 to $1.3 million.
Convex supports the Oracle relational database, X Windows, Ada, 
FORTRAN 77, VAX FORTRAN, and Cray CFT.
To blend into Digital VAX/VMS/DECnet environments. Convex provides 
COVUE, a set of system software products featuring a VAX/VMS command 
shell (COVUEshell) for language compatibility and COVUEnet for DECnet 
compatibility. Additional shell programs provide editing and batch 
capabilities.
Convex supports the required industry standards for connecting worksta­
tions, and Convex customers are running Convex systems with worksta­
tions from Silicon Graphics, Evans & Sutherland, Digital, Sun, Apollo, 
Ardent, and Stellar. Connections to the Macintosh are in the works.
Analysis
Convex is the clear frontrunner in minisupercomputers applied to com­
putational chemistry, which it aggressively pursues. Aberdeen expects 
Convex to maintain its momentum and be one of the few survivors in the 
minisupercomputer market.
AberdeenGroup 68


--- Page 124 ---

vantage of known positive effects and minimize or even avoid known nega­
tive effects (and hopefully turn up few new ones).
The molecular-variant approach obviously has the advantages of working 
with fewer unknowns and the availability of far more workers familiar with 
details of similar molecules. Typically, chemistry-intensive companies use 
this approach 80 percent of the time.
The fresh-slate approach takes much more initial effort, simply to attempt 
to bring up to an acceptable level the knowledge of how the molecule 
might behave under a variety of circumstances.
At the end of Stage 1 the researcher has a general idea of what he/she 
would like to experiment with. However, since the molecules in question 
consist of perhaps a few hundred atoms, and since the number of 
legitimate combinations of these (under various rules of chemistry) are 
astronomical, a short list must be produced.
Stage 2. In Stage 2, the researcher must narrow and prioritize the list of 
target molecules. There are literally billions of combinations of possible 
experimental results, but because this is impracticable, the researcher ap­
plies experience, intuition, and experimental science to shape the working
Exhibit D-1: Drug Discovery and Development Process
No
Positive 
resuits
Field trials, 
Production, 
Marketing
Experimentation
Choose 
research 
area
Refine 
theory and 
experiments
Source: 
AberdeenGronp
AberdeenGrozzp 118


--- Page 125 ---

• Simulation and experimentation
• Analysis and interpretation
• Presentation
Exhibit E-8: Digital's Integrated Laboratory Automation
LABORATORY 
MANAGEMENT
DATA ACQUISITION 
AND ANALYSIS
Source:
Digital Equipment 
AberdeenGroup
DATA ACQUISITION 
AND ANALYSIS
VAX 
VT Series 
VAX LIMS 
ALL-IN-1 
WPS-PLUS 
VAXmail 
Applications
Professional 
Series 
MicroPDP-11 
MicroVAX 
Applications 
Instrument 
Interfaces
Networking
LABORATORY 
MANAGEMENT
Professional 
Series
MicroPDP-11 
MicroVAX 
Applications 
Instrument 
Interfaces
Networking
VAX 
VT Series 
VAX LIMS 
ALL-IN-1 
WPS-PLUS 
VAXmail 
Applications
INTEGRATED 
LABORATORY 
AUTOMATION
AberdeenGroup 134


--- Page 126 ---

Conflicting Trends In
Computational Chemistry
Two-thirds of the aggregate molecular modeling customers (not-for-profit 
institutions) pay only nominal fees for software — as little as 5 percent to 
10 percent of list. This near-term profit sales depressant is leveraged posi­
tively with each subsequent year for two reasons. First, the academic user 
community, with essentially free software, is nearly saturated, thus limiting 
suppliers' financial exposure. Second, the industrial market will expand 
naturally from early adopters to second-level and eventually third-level 
practitioners, all of whom can be expected to pay commercial rates.
The motivation for such deep discounting for academics is obvious: to 
win the hearts and minds of graduate students who soon will become 
specifiers and purchasers in industry; professors consulting to industry 
will be similarly influenced.
Perpetual licenses tend to lock users into a particular supplier for a rela­
tively long period — four to five years — and provide the supplier with a
Exhibit 3-4: 1988 Market Shares-Molecular Modeling Suppliers
BIOSYM 22.2%
Chemical Design 25.9%
BioDesign 8.1%
Polygen 34.1% /
$27 Million Total Revenues
Source: 
Aberdeen Group
AberdeenGroup 21


--- Page 127 ---

Conflicting Trends In
Computational Chemistry
Molecular Design Limited
2132 Farallon Road
San Leandro, CA 94577
(415) 895-1313
Corporate Profile
While not strictly a supplier of computational chemistry programs, 
Molecular Design is the preeminent supplier of comprehensive, integrated 
chemical information management systems for the storage, retrieval, 
and communication of chemical information and associated data.
Molecular Design's products have been designed not only to communicate 
with chemists in their own language — including graphics — but to com­
municate with a myriad of other scientific software systems — from biologi­
cal database management systems to statistical analysis packages.
The company is present in all major geographic markets, and has an es­
timated 90-plus percent marketshare. The company is about the size of 
the five molecular modeling companies combined, and all of its revenues 
are from software. Molecular Design is well respected, is professionally 
and competently managed, and is continually extending and refining its 
products.
Molecular Design has strategic relationships with major system suppliers 
including Digital Equipment, IBM, Hewlett-Packard, Fujitsu, the Institute 
for Scientific Information, Oracle, Chemical Design, and Interleaf.
In December 1987, Maxwell Communications Corporation, a multibillion 
dollar U.K.-based group, purchased Molecular Design, infusing cash to 
enable Molecular Design to pursue its long-term ambition to become the 
leader for the world's chemical information needs. The match is a good 
one, as other Maxwell units that work with Molecular Design include Per­
gamon Journals (a worldwide leader in scientific and technical journal 
publishing), and Pergamon Orbit Infoline (online scientific databases).
Statistics
As a unit of Maxwell Communications Corporation, Molecular Design 
does not release detailed financial information. Molecular Design is 
profitable, growing, and has a healthy balance sheet.
AberdeenGroup 47


--- Page 128 ---

Conflicting Trends In
Computational Chemistry
Craj Research, Inc.
1333 Northland Drive
Mendota Heights, MN 55120
(612) 681-3605
Corporate Profile
Cray Research was founded in April 1962 by the computer industry's 
legendary Seymour Cray and a small group of associates to lead the world 
in development and marketing of supercomputers. In this mission the 
company has been eminently successful, overtaking recently-exiting-from- 
supercomputers rival Control Data (which Seymour Cray also 
cofounded), besting occasional startups or corporate giants, and seriously 
challenged only by Japanese semiconductor/computer manufacturers in 
the Japanese market. Former Cray Research computer designer Steve 
Chen also is mounting a technically aggressive challenge (Supercomputer 
Systems, Inc.), backed by IBM and private investors.
Statistics
Revenues
$756.3 million
Profits
$156.6 million (20.7%)
Assets
$991.4 million
R&D investments
$117.8 mUlion (15.6%)
Overseas revenues
35%
Five-year CAGR
38%
Employees
5,200
Domestic sales offices
32
Overseas sales offices
19
Computers installed
240
AberdeenGroup 69


--- Page 129 ---

Conflicting Trends In
Computational Chemistry
list. Odds are placed on areas with preliminary promise, and experimenta­
tion begins.
Stage 3. The heavy investment in iterative trial-and-error building and test­
ing begins. As many as 100,000 variants are made in the laboratory and 
tested for several chemical criteria in addition to "activity" and toxicity. 
Throughout this multiyear process, the question is continually asked, 
"Does this molecule have the potential to go to market?" As long as the 
answer remains "yes," the iterative process continues. It is during this 
stage that most potential new molecules fail.
Stage 4. The final set of hurdles for the candidate molecule: animal and 
human testing (if a drug, pesticide, or a substance that might reasonably 
come in contact with them). Many candidate molecules pass the animal 
tests, only to fail on humans — species are indeed different.
Stage 5. The ultimate in computational chemistry. The potential payoff is 
large: if the odds of which variations will succeed and which ones will fail 
can be better predicted, priorities can be arranged accordingly. The ul­
timate hope — and the fundamental investment premise of computational 
chemistry — is that the computers will say, "Make this, it'll work; don't 
make this, it won't."
Having invested (conservatively) from $50 million to $100 million dollars, 
and from 5 to 10 years in the process, the molecule comes to market.
Applying Computers
Where in the process can computational chemistry be of most use, and 
when?
At first glance, the clean-slate research of Stage 1 might appear amenable 
to computational methods, and it is. Users apply industrial-strength com­
puters supplied by IBM (3090VF), Cray, Multiflow, Convex, and even Digi­
tal (VAXcluster), to perform ab initio calculations to determine molecular 
properties.
Three Computational Methods
Because ab initio calculations vary with the fifth to seventh power of the 
number of atoms under study, molecules of any meaningful size quickly 
fall outside the range of computability.
Alternatively, semiempirical methods, which vary with the third to fourth 
power of the number of atoms, can be used for less accurate (and less pre­
dictable results.
AberdeenGroup 119


--- Page 130 ---

Conflicting Trends In
Computational Chemistry
Because each stage of the research process differs in level of abstraction, 
mathematical density, skills of the researcher, degree of interaction re­
quired, computational intensity, range of audience viewing results, and 
form of output required for further work, different technologies are used 
for representing intermediate and final results. While 3-D graphics can im­
press casual observers, they are far more expensive than required for 
many intermediate steps.
Exhibit E-9: Digital's Scientific Visualization Model
Application
Complexity of 
Technology
Other 
Astrophysics
Computational Fluid Dynamics 
High Energy Physics
Meteorology & Oceanography
Molecular Modeling
Holography
3D Volumetric 
Animation
3D Volumetric 
Static
3D Animation
3D Static
2D Animation
2D Static
Concep. 
tualiza- 
tion
Simulatton/ 
Expenmen­
tation
Analysis/ 
Interpre- 
tatron
Presen­
tation
Source: 
Digital Equipment
Scientific Research Process
AberdeenGroup 
AberdeenGroup 135


--- Page 131 ---

ready-made market for the sale of additional related packages. The 12 per­
cent plus maintenance fee is high for the software industry, but represents 
the special customer support required during computational chemistry's 
infancy. Maintenance fees should drop to 10 percent by 1993.
Long-Term Software Outlook
Long-term market-potential scenarios (detailed in Appendix C) are split 
along two distinct lines.
One scenario envisions computational chemistry as the next CAD/CAM 
market with several characteristics: single-digit billions in revenues; re­
spectable and near-term profits; many suppliers; quick passage from "early 
adopters" to second-level and third-level users to fuel growth; moderate 
technological hurdles.
The other scenario is less ambitious, and sees computational chemistry as 
resembling more closely the finite element analysis market with these char­
acteristics: double-digit millions in revenues; protracted industry losses 
followed by gradually building very high profits; slow passage to second- 
level users; high technological hurdles.
Aberdeen Group believes the correct outlook is much closer to the finite 
element analysis model than the CAD/CAM one, but that some CAD/CAM- 
like packages aimed at less-than-Ph.D. practitioners will be on the market 
in 1990-91.
Hardware Segment Size and Growth
Hardware sales both drive and are driven by software sales, depending 
upon the relative product maturity of each. Within the hardware segment 
(for the first time in 1988), workstations are challenging compute servers 
as vehicles for providing industrial-strength computer power.
Currently, Ardent, Stellar and Silicon Graphics are selling a new round of 
technically impressive 3-D graphics workstations which are stimulating 
software sales and causing mixed results for compute servers. The power 
of the new superworkstations exceeds that of superminicomputers and of 
some minisupercomputers. Users typically have limited hardware budgets 
and are choosing the new graphics systems after a round of minisupercom­
puter purchases in 1986-88.
Hardware sales by equipment manufacturers totalled approximately $210 
million in 1988, up 31 percent over estimated 1987 sales of $160 million. 
Sales in 1989 are expected to increase 31 percent to $275 million. Es­
timated market shares by equipment category for 1988 are shown in Ex­
hibit 3-5.
AberdeenGroup 22


--- Page 132 ---

Revenues
$25 million (Aberdeen estimate)
Domestic customers
160 (Aberdeen estimate)
Overseas customers
100 (Aberdeen estimate)
Overseas distributors
2
Employees
PC-based customers
220
1,100 (Aberdeen estimate)
Computational Chemistry Profile
Molecular Design has many scientists on its staff, is quite active in computa­
tional chemistry, community technical activities, and is continually in con­
tact with leading computational chemistry users to anticipate new product 
development needs and opportunities. Virtually every computational 
chemistry installation is a Molecular Design user.
Computational Chemistry Products
Molecular Design provides two database products — MACCS-II and 
REACCS. MACCS-II (Molecular ACCess System) is an integrated chemical 
information management system operating at corporate, divisional, 
departmental, and individual levels. Designed for mini/mainframe com­
puters, it offers convenient, user-familiar graphical input for building, 
maintaining, and accessing libraries of chemical structures and related 
data, and for preparing reports. MACCS-II can perform structure, sub­
structure, or textual data searches of databases, and can be customized 
with a series of modules for building even more comprehensive systems 
through interconnection with Oracle and other database systems.
REACCS (Reaction Access System) does for reactions what MACCS-II does 
for structures. Reactions and their associated data are searchable over any 
field, including graphical structure and substructure searches for reactant, 
products or both, in either proprietary or commercially available 
databases. Searches may be conducted over several databases simul­
taneously. Molecular Design makes available several available REACCS- 
searchable databases covering different types of chemistry. These include 
FCD (from ChemQuest), ORGSYN (from Organic Synthesis), Theilheimer 
(from Synthetic Methods of Organic Chemistry), REACCS-JSM (Derwent's 
Journal of Synthetic Methods), CLF (Current Literature File), FCD (Fine 
Chemicals Directory) and pK File.
Molecular Design also offers the CPSS (Chemist's Personal Software 
Series) for operating on personal computers. CPSS products are fully in­
tegrated, permitting work with more than one program concurrently and
AberdeenGroup 48


--- Page 133 ---

Computational Chemistry Profile
Cray Research has installed four dedicated systems in computational 
chemistry (with additional units on order) as part of a multiyear, well- 
financed plan to place systems with the leading industrial firms in phar­
maceuticals, diversified chemicals, materials sciences, biomedicals, and 
petrochemicals. If successful, Cray believes that others within those in­
dustries also will buy. Numerous other Cray systems are used for com­
putational chemistry in time-shared environments.
Cray has 25 specialists worldwide who provide computational chemistry 
support, and participates in most major computational chemistry trade 
shows and conferences. Cray also publishes a quarterly technical journal 
of scientific results achieved on Cray supercomputers; most issues have an 
article on computational chemistry.
Computational Chemistry Products
Cray Research markets three hardware product lines — the CRAY EA, ($2.5 
million to $14.0 million), the CRAY-2 ($12.0 million to $17.5 million), and 
the CRAYY-MP ($5.0 to $23.7 million). All lines are supported by a full 
line of peripheral devices, system software, compilers, text editors, 
graphics software, and a variety of network interfaces and software. Cray 
will integrate its systems into virtually any computer environment, and ex­
tensively supports its systems and software in the field.
Entry-level systems begin with the CRAYX-MP EA/14SE and the CRAY-2S- 
64. From these, Cray provides compatible hardware and software paths to 
high-end machines CRAYX-MP EA/464, CRAY-MP/832, CRAY-2S/4-128, 
and CRAY-2/4-512. Cray signals well in advance the targeted capabilities 
and models of systems under development, and plans to introduce the 
CRAY-90 and the CRAY-3 for the 1990s.
In March 1989, Cray began a planned six-month transition from its X-MP 
line to the Y-MP line by introducing nineteen additional models in the Y- 
MP series. The new series ranges in price from $5 million for an entry- 
level model with a single processor (Y-MP2/116) to $23.7 million for an 
eight-processor, 128 megaword unit (Y-MP/8128).
Cray Research markets and supports MPGS (Multipurpose Graphics Sys­
tems) for use on Cray systems under UNICOS, and is developing Chem- 
Tool, a graphics interface allowing UNIX workstation users to interactively 
build, simulate, and analyze molecular systems invoking a variety of third- 
party computational chemistry programs running on a Cray supercom-
AberdeenGroup 70


--- Page 134 ---

For even faster (and less accurate and predictable) results, the current 
trend is molecular modeling, where atoms are treated simply as balls con­
nected by springs. Using classical (Newtonian) mechanics, results can be 
calculated that vary only with the second power of the number of atoms.
Computational Limitations
Computational chemistry, and particularly molecular modeling, is not a 
golden key that suddenly and cheaply opens the locks of difficult 
chemistry. Rather, it is an aggregation of ad hoc research tools with rather 
brittle operating properties. Because chemistry theory is dramatically 
simplified to make computation possible, the results are unpredictable out­
side of very narrow boundaries. Unfortunately, the limits of these boun­
daries seldom are known until after the resulting chemicals have been 
experimentally made and tested.
Second-Stage Potential
The second stage of the chemical discovery process is highly leverageable. 
If the odds of the chemist's short list can be substantially improved, then 
Stage 3 can be substantially cut in time and expense. Currently, this is the 
major area of computational chemistry, with both ab initio and molecular 
modeling methods used extensively. However, for the software to deliver 
good results, it must "understand" subtle nuances of chemistry that 
chemists themselves don't understand. Interactive computationally inten­
sive graphics hold promise here (improved molecular modeling), but the 
results are not in yet.
Third-Stage Payoff Large
The third stage holds the most potential:
o The variations within each iteration are relatively small and more 
amenable to computerized approximations. And, requiring less variations 
on unknown chemistry, small variations are supposedly more amenable to 
automation.
o Graphics can yield insight into why some variants work while others 
don't. Pages of computer printouts, besides being awkward and numbing, 
are not succinct enough in representation.
o There are at least ten times as many potential installations in the develop­
ment-through-pilot-production stages as there are in research.
Fourth-Stage Glimmerings
The fourth stage of the drug development process is not even being 
dreamed about for computational chemistry, since there are no current
AberdeeiiGroup 120


--- Page 135 ---

IBM: Total Corporate Integration
IBM's Ambitious Computational Chemistry Goals
IBM's compounded annual rate of growth for the past five years has 
averaged a scant 7 percent, respectable for a $60 billion industrial 
megalith, but insufficient to keep IBM's typical high profit margins from 
being severely squeezed. IBM has consequently induced early retire­
ments, transferred home office and manufacturing people to the field, and 
has seen product leadership in its newest market — personal computers — 
taken over by others.
With these pressures, IBM is seeking to reestablish itself in scientific 
markets, an area in which it distinguished itself during the early 1960s, but 
was overtaken by then startup Control Data, and later, Cray Research. IBM 
not only sees its potential growth in scientific processing two to three 
times that of commercial processing, but sees no one outside of itself and 
selected Japanese semiconductor/computer manufacturers who possesses 
the fundamental technology for building the most advanced supercom­
puters; even Cray Research relies on outsiders for its components.
IBM's hurdles in regaining a meaningful presence in technical markets 
hinge on five factors:
• Product superiority, price/performance parity, and 
sufficient flexibility to accommodate third-party 
hardware, software, and communications products.
• ISV applications running smoothly on IBM machines, 
with applications support in the field as well as in the 
home office.
• Access to Digital-only accounts.
• Sales people motivated and committed to call upon 
users, respond to specific user needs, close sales, and 
follow through on scientific accounts at the technical 
level.
• Enterprise issues that can preempt all of the above.
Product Issues
IBM is addressing the product superiority, price/performance parity, and 
flexibility issues with three specific programs:
AberdeenGroup 136


--- Page 136 ---

Conflicting Trends In
Computational Chemistry
use of a common directory and other facilities. CPSS products include 
ChemBase, a chemical structure and reaction database program; Chem- 
Talk/ChemHost, PC-to-mini/mainframe linkage programs, and terminal 
emulators; and ChemText, an image and word processor designed specifi­
cally for the chemical and pharmaceutical industries. Chemtext works 
with Interleaf's TPS for professional production of large-scale, complex 
chemical documents.
Late in 1988, Molecular Design entered into a three-way partnership with 
Digital Equipment and pharmaceutical supplier Glaxo to design new 
chemists' workstation software for chemical information management and 
communication. Based on Molecular Design's successful CPSS and run­
ning on a VAX, the software will be transparently distributed among the ap­
propriate mini/mainframes and workstations. A single graphical user 
interface will be used. Molecular Design has entered a similar agreement 
with Hewlett-Packard for HP's 9000 high-performance graphics worksta­
tions (Series 300 and 800).
Hardware Partners
Molecular Design has been a Digital CMP since 1982, and was one of the 
first software suppliers to participate in the CMP program. Molecular 
Design has been an IBM Marketing Partner for two years.
Analysis
Molecular Design, with dominant market coverage of the chemical 
database market, a deep-pocketed parent company, and a strong manage­
ment, technical and marketing team, has been a consistent winner in com­
putational chemistry. Aberdeen expects its success to continue.
AberdeenGroup 49


--- Page 137 ---

Conflicting Trends In
Computational Chemistry
puter. Cray supports graphics systems from Ardent, Apollo, Digital, E&S, 
Hewlett-Packard, IBM, Apple, Silicon Graphics, Stellar, and Sun.
Cray also supports the network hardware and software required to work 
with various other computers. Proprietary protocols supported include: 
SNA, DECnet, TCP/IP, NSC Hyperchannel, CDCNeat, and HSX-1 high- 
speed channel.
Cray supports molecular modeling packages supported from BIOSYM, 
Polygen and Tripos Associates, and support is being discussed for Bio- 
Design and Chemical Design.
Specific computational chemistry codes running on, and optimized for, 
Cray supercomputers, are comprehensive and far too many to list here. 
They range from those supplied by the five commercial molecular model­
ing developers to QCPE and the National Energy Software Center (NESC) 
to various industry and academic groups.
Analysis
Cray is the ultimate winner in the computational chemistry hardware 
market, even if it were to ignore the field. Computational chemistry will 
remain computationally intensive for the indefinite future and Cray has no 
domestic rivals for supplying supercomputers. Far from neglecting the 
area, Cray is one of the most pervasive marketers in the computational 
chemistry field. And, with the computer industry's highest hardware profit 
margins, Cray can easily afford any technical and marketing programs it 
may choose to launch.
For a full analysis of Cray Research's role in computational chemistry, see 
Appendix E.
AberdeenGroup 71


--- Page 138 ---

Conflicting Trends In
Computational Chemistry
theories to predict how new chemicals will behave outside the laboratory 
and in living beings. Further, chemicals that affect one type of life can 
have different (or no) effect on others. Obviously, if chemical affects 
could be predicted with accuracy, it would truly revolutionize the entire 
chemistry industry.
AberdeenGroup 121


--- Page 139 ---

Conflicting Trends In
Computational Chemistry
• The joint development partnership with 
Supercomputing, Inc. is a full two-way street. IBM 
provides base technology, which SCI is pushing to the 
limits, and SCI will provide a supercomputer engine that 
both parties hope will deliver higher performance than 
obtainable from either the Japanese or Cray Research. 
(At this point, there is no marketing agreement between 
SCI and IBM). More so than the Japanese, IBM must be 
able to have a worldwide, fully competent 
supercomputer market presence to regain user respect 
— and close sales.
• IBM is handling the flexibility issue by suggesting a 
mix-and-match approach, as shown in Exhibit E-10, 
whereby equipment from Digital, Cray, workstation 
manufacturers, and LAN suppliers combine to take 
advantage of IBM's 3090 and Vector Facilities to form a 
powerful computational network.
• As an umbrella for all of IBM's scientific processing, it is 
promoting a systems concept similar to Digital's 
Integrated Lab Automation, but extending all the way to 
the mainframe, as shown in Exhibit E-11.
Applications and Support
Of all the system suppliers Aberdeen has interviewed on computational 
chemistry, IBM has a much deeper and broader understanding of the ap­
plications issues involved. However, IBM is continuing to experience dif­
ficulty translating its understanding into deliverable products and 
programs. Much like the classic tortoise and hare, IBM is steadily im­
plementing programs and resources to serve the computational chemistry 
marketplace. Examples include:
• IBM has identified and classified (along lines similar to 
those independently developed by Aberdeen — see 
Chapter 2, Exhibit 2-3) several types of computational 
chemistry programs. It has established priorities for 
porting these to IBM systems and for marketing them 
under specific tactical programs. These plans are 
comprehensive, internally championed, and, until 
released, quite proprietary.
• IBM has been putting into place a pyramid of support 
(see Exhibit E-12) for scientific applications. The
AberdeenGroup 137


--- Page 140 ---

Polygen Corporation
200 Fifth Avenue
Waltham, MA 02254
(617) 890-2888
Corporate Profile
Polygen was founded in 1984 by entrepreneur Jeffrey M. Wales, scientists 
Andrew Ferrara and Dr. Frank Momany, and Jean-Loup Fayolle. In March 
1989, IBM took a minority investment position in Polygen. It was a sig­
nificant industry event.
Polygen is currently the largest of the five molecular modeling software 
suppliers, selling both software and hardware. Of the five, Polygen also is 
the most sales- and marketing-oriented, and, within the past two years has 
become a science leader.
Polygen has large ambitions, using what it terms Chemical Design Automat­
ion, to leverage the company into the much larger field of research auto­
mation — mechanizing the entire research process. Polygen plans to 
accomplish this through Centrum, a technically ambitious, integrated com­
puter and data interchange product announced in March 1989 for use on 
personal computers.
Statistics
Privately held, Polygen chooses for competitive reasons not to disclose 
financial information for publication; for customers, however, it will 
review financial data under a nondisclosure agreement. The company is 
backed by venture capitalists and IBM, and is operating at a substantial but
planned loss.
Revenues
$9 million (Aberdeen estimate)
Domestic customers
125 (Aberdeen estimate)
Overseas customers
75 (Aberdeen estimate)
Employees
85 (Aberdeen estimate)
Computational Chemistry Profile
In addition to marketing what it plans to be an ever-widening range of com­
putational chemistry software, Polygen envisions itself as a comprehensive 
supplier of integrated information systems.
AberdeeiiGroup 50


--- Page 141 ---

Digital Equipment Corporation
146 Main Street
Maynard, MA 01754
(508) 493-5111
Corporate Profile
Digital is the world's second-largest computer manufacturer. Founded in 
1957 by Kenneth H. Olsen, an MIT graduate engineer, Digital began by 
making electronic modules that could be made into computers by others, 
but quickly began making computers under its own label. From inception. 
Digital emphasized low-priced, affordable computers for the individual 
technical worker (and later for departments), upsetting the established 
financial mechanics of computer industry pricing and profits. Assuming 
that Digital's small units were mere toys, the industry, then dominated by 
mainframe manufacturers, failed to take Olsen and his crusaders serious­
ly. Digital has overtaken each of those rivals, as well as all others who 
started minicomputer companies in the early 1970s.
Digital has borrowed a chapter from IBM's System/360 book, and now of­
fers a very wide range of prices, performance, and applications, rivaling 
IBM's in breadth and superior in its ability to interconnect its own and 
others' systems.
Statistics
Revenues
$12.3 billion
Profits
$1.2 billion (9.8%)
Assets
$10.2 billion
R&D investments
$ 1.5 billion (11.9%)
Overseas revenues
52%
Five-year CAGR
21%
Employees
124,800
Worldwide sales offices
875
Computers installed
300,000 VAXes (Aberdeen estimate)
AberdeenGroup 72


--- Page 142 ---

AberdeenGroup 138
AberdeenGroup
Source: 
IBM
Computer Aided Chemistry: 
Connectivity Requirements
IBM
3090
3090 VF
PS/2'
ASCII graphics
Non-IBM
4381
9370
NSF 
TCP/IP
€3?
OEM 
devices
Cray
VAX cluster™
(Ethernet™) 
't—f' ^/ DECnet™
MicroVax™ 
Apollo 
Sun
OEM devices
(lan)
RT
5080
Exhibit E-10: IBM's Computer Chemistry Connectivity


--- Page 143 ---

Conflicting Trends In
Computational Chemistry
In a field far more technically oriented than sales oriented, Polygen's 
blanket coverage of customers initially resulted in sales beyond what 
Polygon's products themselves might merit. However, Polygen sub­
sequently invested heavily in science and is now the "one to beat." By con­
tinuing to pour substantial resources into sales and marketing, Polygen is 
effectively raising the stakes of staying in the molecular modeling game, 
hopefully shaking off some of the other players. IBM's recent financial 
backing should strengthen this resolve.
Science
Polygen, with an undisclosed number of Ph.D. scientists that Aberdeen es­
timates at 20, increasingly does its own science. It has working relation­
ships with several academic centers, including York University in England, 
and Harvard's computational chemistry department headed by Professor 
Martin Karplus, whose group developed CHARMm, which Polygen now 
markets.
Computational Chemistry Products
CHARMm is a simulation and analytical package for modeling the dynamic 
behavior of small and large molecules on high-performance computer sys­
tems.
QUANTA is an integrated system combining interactive chemical sketching, 
molecular graphics, molecular mechanics and dynamics, and analysis for 
use on high-performance graphics workstations.
XPLOR is a macromolecular structure refinement package that combines 
molecular dynamics with x-ray diffraction data to improve the efficiency of 
the crystal structure determination process.
Products are sold on the basis of a perpetual license and an annual main­
tenance fee of 17% (average) of the license, which entitles users to all up­
dates. Individual product prices vary with the size of the platforms on 
which the products run. Most products are sold bundled, and those tabu­
lated are for commercial customers. There are less expensive prices for 
academic and government customers.
Centrum is a new chemical information and document preparation system 
and is part of Polygen's move to expand beyond molecular modeling.
AberdeenGroup 51


--- Page 144 ---

Conflicting Trends In
Computational Chemistry
Computational Chemistry Profile
Digital is the quintessential broad-gauge supplier of low to midrange com­
putational power to scientists and engineers. It's VAX/VMS environment is 
the industry standard in technical circles, far more so than UNIX, which 
Digital also heavily supports. It should be no surprise, then, that Digital 
has been in computational chemistry from the very beginning, with many, 
many codes developed on the VAX.
Computational Chemistry Products
Digital's general-purpose VAX product line spans a performance range of 
.9 VUPs (MicroVAX 2000) to 22 VUPs (VAX 8840), and a price range from 
$7,000 to $1.5 million. (A VUP is defined as a VAX Unit of Processing, ap­
proximately one MIPS.) VAXes can be clustered for additional perfor­
mance with a side benefit of higher availability.
For computational chemistry and other numerically intensive applications. 
Digital offers the VAX Supercomputer Gateway — a high-speed intercon­
nect for integrating Cray supercomputers into a VAXcluster environment. 
Based on a VAX 8250 or 8350 processor, the Gateway interconnect can 
operate at 70 Mb per second with a VAXcluster, and 10 Mb per second 
over Ethernet It attaches to a single Cray channel, operates under VMS, 
has communication and file management software, and generally lets ad­
vanced users combine the power of Cray supercomputers with the wealth 
of VAX system and development software. The Supercomputer Gateway in­
cludes configuration analysis and planning, installation, and programs, 
and is priced at about $80,000; additional units are priced at about 
$40,000.
Also available for Cray users is the VAX/VMS Station, a general-utility 
workstation for offloading noncomputationally intensive tasks from the 
Cray.
Computational chemistry programs available on the VAX include the 
software available from the five molecular modeling suppliers (BioDesign, 
BIOSYM, Chemical Design, Polygen, and Tripos Associates), chemical 
databases from Molecular Design, and public-domain software from NASA, 
NESC, and QCPE.
Analysis
Digital is a winner in computational chemistry, even if it currently does not 
have the "hottest box." The preponderance of technical software is 
developed on VAX systems, and virtually all mid-1980s computational 
chemistry was developed on VAXes. With increasing linkages to computa-
AberdeeiiGroup 73


--- Page 145 ---

Source:
Computer Aided Chemistry: 
information System Requirements
IBM 
AberdeenGroup
-VF-]..
rKOW#'}/;^
Intelligent g 
workstations
Mid-range <----------► Large
AberdeenGroup 139
• Integrated information flow Data
• Support of similar/ 
dissimilar devices
• Common user 
interface
• International 
standards and 
protocols
re.
|Communications ,,' 
pate';:
EApiJljcations .
^4<
0
Exhibit E-11: IBM's Computational Chemistry System Topology
Conflicting Trends In 
Computational Chemistry


--- Page 146 ---

Product
Price ($000) 
Intro 
Platforms
CHARMm
$20-150 
11/86 
All (a FORTRAN
program)
Quanta
$25- 
11/87 
Stellar, Silicon
Graphics (HP, Sun)
XPLOR
$10-75 
2/88 
Digital VAX, Convex,
Cray, Silicon 
Graphics, Stellar
Centrum
$5/seat 
3/89 
PCs
Hardware Partner
Polygen has entered into a CMP agreement with Digital.
Corporate Partner
In March 1989, IBM purchased a minority interest in Polygen, and Polygen 
is porting its software to several IBM platforms.
Analysis
Polygen's key strengths are its marketing and products. Acting more like a 
first-tier computer systems supplier than a small software supplier, 
Polygen smothers prospective customers with attention and existing cus­
tomers with ongoing support. The result is first place in sales coming 
from a relatively late corporate start, but at the price of postponed profits. 
Because IBM recently has invested in the company, Polygen's otherwise 
questionable financial viability is not a current issue. With the IBM invest­
ment, Polygen is well-positioned to win a war of attrition.
AberdeenGroup 52


--- Page 147 ---

tional servers and superworkstations via its comprehensive networking 
scheme, Digital can couple its development environment to the hottest-box- 
of-the-month. And, if Digital later in 1989 introduces its anticipated higher 
performing uniprocessors, it is poised once again to sell computers for 
running computational chemistry production codes.
For a full analysis of Digital's role in computational chemistry, see Appen­
dix E.
AberdeenGroup 74


--- Page 148 ---

Source:
Computer Aided Chemistry:
Support Structure
AberdeenGroup
IBM
Integrated 
enterprise
Marketing reps 
Systems engineers
Area specialists
Application specialists
E/S Natl. 
Support Ctr.
Scientific Centers
Systems Ctn
NIC Centers
Exhibit E-12: IBM's Scientific Computing Support Structure
field-based Science & Technology Specialists — which 
Aberdeen estimates by the end of 1989 will number
it HI 1nu ii n|
Research arid development


--- Page 149 ---

Conflicting Trends In
Computational Chemistry
Quantum Chemistry Program Exchange
Department of Chemistry
Indiana University
Bloomington, IN 47405
(812) 335-4784
Organizational Profile
The Quantum Chemistry Program Exchange (QCPE) was organized during 
the first major wave of numerically intensive computing in the early 1960s, 
when such top-of-the-line scientific computers (epitomized by the CDC 
3600) were radically transforming the way science was about to be done. 
With massive computing power suddenly available, there were few prac­
titioners skilled in transforming traditional science methodology into com­
putational form. The excitement level was extraordinary, but so was the 
frustration over the need to harness the new technology without diverting 
scientists from science. Thus, various scientific exchange organizations 
were formed to minimize duplication of algorithmic development and to 
share results.
QCPE was formed in 1962 by chemists interested primarily in quantum 
chemistry, but since then has expanded to cover the entire spectrum of 
computational chemistry. QCPE is a not-for-profit organization with a 
minuscule staff, serving as both a depository and a distribution point for 
thousands of researchers throughout the world.
QCPE does not develop, document, or maintain software.
Computational Chemistry Products
QCPE covers the full computational chemistry spectrum from quantum 
mechanics through molecular modeling to crystallography, spectroscope, 
NMR, and chemical reactions. Currently, QCPE offers 565 programs for 
nominal prices covering costs.
Analysis
QCPE offers bargains for chemists able and willing to use software not 
meeting industrial documentation, interface, testing and support stand­
ards, and where ongoing program development and upgrade depends 
upon the limited resources found in academia.
AberdeenGroup 53


--- Page 150 ---

Conflicting Trends In
Computational Chemistry
Evans & Sutherland Computer Corporation
580 Arapeen Way
Salt Lake City, UT 84108
(801) 582-5847
Corporate Profile
Evans & Sutherland was founded in 1968 to develop high-performance 
graphics and supporting computer systems. For years it had few com­
petitors for its top-of-the-line systems, most of which were sold into simula­
tion markets. The company is developing a full-fledged supercomputer 
which, after a six-month slip in 1988, is scheduled for beta test in mid- 
1989. For Evans & Sutherland, 1988 was a difficult year. Sales slipped 
four percent from 1987, the supercomputer slippage hurt financially, its 
VAXstation 8000 was written off, and the company barely broke even. 
However, the company has regrouped, has a good cash position, and 
plans to bounce back.
Statistics
Revenues
$129.6 million
Profits
$1.9 million (1.4%)
Assets
$195.1 million
R&D investments
$37.1 million (28.6%)
Overseas revenues
35%
Five-year CAGR
19%
Employees
1,300 (Aberdeen estimate)
Domestic sales offices
(Not available)
Overseas sales offices
(Not available)
Computers installed
(Not available)
AberdeenGroup 75


--- Page 151 ---

Conflicting Trends In
Computational Chemistry
nearly 500 in the United States alone — are supported by 
decreasing numbers of technologists as the pyramid 
reaches the home office. This heavy field orientation 
plays to IBM's traditional customer-support and 
customer-access strengths, and, when fully supported 
by products, will pose a formidable obstacle to all but 
Digital, Cray, and the more robust of the smaller 
product specialists.
Cracking the All-Digital Accounts
In what is shaping up as a massive example of "the grass looking greener 
on the other side" for both IBM and Digital, IBM is coveting Digital's techni­
cal markets while Digital has been coveting — and enjoying — IBM's com­
mercial markets.
Further, in a manner that was once unthinkable. Digital heavily dominates 
so many technical accounts that IBM cannot even get sales appointments, 
let alone sell equipment or services into them.
Is Digital vulnerable to IBM, and if so, where?
Until Digital reestablishes unequivocal leadership in technical markets (it 
has been preempted by minisupercomputer and workstation startups who 
are no longer starting up), IBM has the opportunity to reopen closed 
doors with its Vector Facility and all of the programs mentioned above. 
Closing sales is another matter, but one in which IBM should not be under­
estimated. IBM's executives are all seasoned veterans of the scientific com­
puting wars of the 1960s, and would like nothing better than to see 
themselves reestablished in what is once again becoming a hot growth
area.
The Selling Obstacle
In Aberdeen's view, the single largest hurdle that faces IBM in capturing 
significant technical sales is field sales. With no first-rate technical 
products to sell for many years, there are no field people to sell new ones. 
And the difficulty in selling to technical end users — virtually all of whom 
are articulate and savvy in the ways of computer purchases, if not the 
details of the latest gadget — is legendary. Further, technical end users 
have far more control over what they buy, and from whom, than their com­
mercial counterparts do.
In solving the selling challenge, IBM faces a chicken-and-egg situation 
(runaway technical product versus experienced technical salespeople)
AberdeenGroup 141


--- Page 152 ---

Tripos Associates, Inc.
1699 South Hanley, Suite 303
St. Louis, MO 53144
(314) 647-1099
Corporate Profile
Tripos is the original molecular modeling software supplier, founded in 
1979 by Washington University (St. Louis) professor Garland Marshal. 
Tripos began as a consulting and then hardware operation during the 
pioneering days of graphic displays. Tripos founders had close personal 
connections with the MIT research group to which Dr. Sutherland (of 
Evans & Sutherland) belonged. Later, Tripos went into the software busi­
ness as Dr. Marshall developed his computational chemistry programs.
Statistics
As a unit of publicly-held Evans & Sutherland (see profile in Chapter 7), 
Tripos Associates does not disclose financial information for publication.
Revenues
$ 2.5 million (Aberdeen estimate)
Domestic customers
100
Overseas customers
100
Employees
42
Computational Chemistry Profile
Tripos is an increasingly broad supplier of tools, having the advantage of 
an early customer base (in small molecules) to upgrade with an enhanced 
and expanded product line completed in April 1989.
Science
Tripos has formal collaborations with chemists at several universities, in­
cluding Pomona College (the Medchem Project), Purdue University, 
Scripps Institute, University of North Carolina, Duke University, University 
of South Florida, Birkbeck College (London), University of Texas, Univer­
sity of Utah, and Washington University. Tripos also has scientific advisory 
boards.
AberdeenGroup 54


--- Page 153 ---

Computational Chemistry Profile
Evans & Sutherland is a long-time player in computational chemistry, and 
until two years ago was the preferred workstation supplier for molecular 
modelers — that role has since passed to Silicon Graphics. On the applica­
tion side, in 1987 Evans & Sutherland purchased one of the five molecular 
modeling software suppliers. Tripos Associates (also see profile on Tripos 
Associates in Chapter 5). Evans & Sutherland currently markets its unan­
nounced ES-1 supercomputer against supercomputer and minisupercom­
puter suppliers, and intends to pursue computational chemistry as one of 
its application areas.
Computational Chemistry Products
E&S has been a long-term supplier of computational chemistry displays, 
and currently offers the PS 390 high-performance, 3-D graphics terminal. 
Using proprietary technology providing calligraphic line quality on a 
raster display, the model PS 390 has anti-aliasing, depth-cueing, perspec­
tive, and color blending at the intersection of different colored vectors, 
producing a highly accurate model image. Static, smooth-shaded images 
are rendered locally with a choice of wash, flat, Gourard, or Phong shad­
ing. The PS 390 performance specifications include 365,000 double 
precision vector transformations per second, 8,292 x 8,292 image quality 
addressability, 127 selectable hardware-generated line textures, 1,801 
colors available for wireframe images, and 24 bitplanes double buffered. 
The unit is connectable via Ethernet, IBM 3278 and 5080 interfaces, and 
Digital's Unibus parallel interface.
Analysis
Evans & Sutherland has seriously slipped in computational chemistry 
markets. It has been overtaken in graphics workstations by Silicon 
Graphics, and lost market share in molecular modeling during its acquisi­
tion of Tripos Associates. Currently, E&S's major corporate technical ef­
fort — the ES-1 supercomputer — is its major hope for regaining a strong 
computational chemistry market presence. If the ES-1 is successful, an 
open question at this time, Aberdeen does not expect significant results 
before 1991.
AberdeenGroup 76


--- Page 154 ---

which it has, at most, two years to resolve before Digital and its tough 
band of technical competitors keep IBM from closing the gap.
Enterprise Issues
In the topology wars, the ultimate question is "account control" — which 
system vendor can dictate or influence long-term equipment decisions its 
way. In promoting computational chemistry. Digital and IBM offer similar, 
but different approaches:
• IBM controls the corporate data node of virtually every 
major user, whereas Digital has the largest marketshare, 
but not control over, the middle-manager ring and is 
strongly represented in selected productivity nodes.
(See Exhibit E-6, Spoke-Node-Ring Topology.) Ongoing 
guerrilla warfare over who controls which part of which 
database is essentially an organizational issue rather 
than a technical issue.
• IBM offers the widest performance range of any system 
supplier, with emphasis on high-end, general-purpose 
commercial computing, while Digital offers a less wide 
range emphasizing midrange, specific-application 
computing. So far, users have overwhelmingly chosen 
scientifically-oriented computers for computational 
chemistry over IBM's broader (but more expensive) line.
• IBM's connectivity scheme — based on Systems Network 
Architecture (SNA) — suffers from specifications and 
orientation too tightly defined in another era, that of 
1960s/early 1970s batch computing. Digital's DECnet is 
based on more modem technical concepts and is far 
superior and less expensive to implement. DECnet and 
SNA live in uneasy coexistence in many computational 
chemistry installations.
• IBM's conceptual scheme for integrating all relevant 
organizational elements, from laboratory to finance to 
factory to marketing, is more generic than Digital's. 
This appeals to corporate executives, but not to line 
managers. Digital's scheme targets the technical 
manager and the individual user, sidestepping the 
corporate politics where possible.
With two competing sets of ideologies, topologies, products, sales and sup­
port tactics, and differing stages in product cycles, users are in a difficult 
position to decide which (if either) to choose. As shown in Appendix A,
AberdeenGroup 142


--- Page 155 ---

Conflicting Trends In
Computational Chemistry
Computational Chemistry Products
SYBYL is a comprehensive toolkit for molecular modeling and analysis, 
and is available with several modules. SYBYL databases store complete 
molecular information. Users can choose between command- or menu- 
driven operations. Optional modules currently available include a 
polymer package (Polymer), a biopolymer package (Biopolymer), a com­
putational package (Advanced Computation), and a QSAR analysis pro­
gram (QSAR). Prices on these modules range from $25,000 to $70,000.
Other products include a 3-D structure program (Concord, from the 
University of Texas and priced from $10,000 to $14,000), and two pack­
ages for PCs: molecular modeling (Alchemy H, priced at $750) and a 
graphics enhancement package (Nitro, priced at $995).
Products are sold on the basis of a perpetual license and an annual main­
tenance fee of 15 percent of the license, which entitles users to updates. 
Licenses vary in price depending upon the number of users, the number 
of modules, and the computers operated on. Academic customers pay 
about 5% of list price.
Platforms
Tripos' programs run on Cray, Convex, Digital, E&S, Silicon Graphics, 
Sun, PCs and Macintoshes.
Hardware Partners
Tripos has various cooperative marketing agreements with several 
hardware and software suppliers.
Analysis
Tripos is completing the process of establishing itself as an independent 
subsidiary of Evans & Sutherland, which acquired Tripos in mid-1987. 
During the transition period. Tripos did not have its own sales force, 
which coincided with the new marketing efforts of the 1984-85 startups 
who were aggressively seeking marketshare. With its newly revamped and 
expanded product line, Aberdeen expects Tripos to vigorously seek 
marketshare gains in 1989 and 1990.
AberdeenGroup 55


--- Page 156 ---

Conflicting Trends In
Computational Chemistry
FPS Computing, Inc.
Box 23489
Portland, OR 97223
(503) 641-3151
Corporate Profile
FPS Computers (formerly Floating Point Systems) was founded in 1972 to 
build array processors and other high-performance computers for numeri­
cally intensive computing. A technical pioneer, FPS had been the leading 
supplier of array processors since 1975, was the first to introduce a 64-bit 
minisupercomputer in 1981, and was ahead of others in hypercube-like 
processor designs in the 1980s.
Once the acknowledged leader in scientific minisupercomputers, FPS fell 
on hard times by not responding quickly enough to minisupercomputer 
startups, pursuing instead a costly and ultimately discontinued new line of 
supercomputers (T Series). FPS currently markets the Celerity minisuper­
computer line (as the FPS 500) which it acquired in mid-1988.
FPS and Digital have a joint sales agency agreement under which Digital of­
fers FPS' M64 attached computers to Digital's VAX customers. In October 
1988, FPS and Stellar Computer began a joint marketing program of each 
other's products, and since have extended the agreement to cover selected 
joint developments.
Statistics
Revenues
$70.8 million
Profits
$27.8 million loss
Assets
$85.7 million
R&D investments
$14.0 million (19.8%)
Overseas revenues
22%
Five-year
9%
Employees
550
Domestic sales offices
20
AberdeenGroup Tl


--- Page 157 ---

Conflicting Trends In
Computational Chemistry
they increasingly are saying "Neither!", and opting for Spoke Node Ring 
which lets them control their destiny.
Given these circumstances, the third of the "big three" in computational 
chemistry has an entirely different approach.
Cray Research: The Power Play
Going For Market Dominance
While Digital and IBM are laying groundwork for impressive enterprise- 
wide and laboratory-wide ^sterns and topologies that can absorb consider­
able products over several years, Cray Research is aiming directly at the 
computational aspects of chemistry. Cray plans to dominate the computa­
tionally-intensive aspects of computational chemistry, just as it currently 
dominates other computationally-intensive fields such as fluid dynamics 
and simulation. To Cray, it is relatively unimportant which topology a cus­
tomer chooses — it can readily adapt to any. Exhibit E-13 shows a typical 
example.
Supercomputer Demand Issues
How will Cray accomplish its plan of dominance?
In the simplest case, Cray relentlessly strives to be the first-with-the-fastest, 
knowing that every supercomputer user either becomes quickly compute 
bound, or that more technical progress can be made with another dou­
bling or quadrupling of power, or both. With computational chemistry a 
potential black hole of computing, nature should take its course. How­
ever, it thus far has not done so in computational chemistry — Cray has in­
stalled only four systems in the field. There is, however, more than meets 
the eye, and these factors have impeded demand:
• In new technical applications, newly placed 
supercomputers do not lead demand, they react to it. 
The applications were first developed at supercomputer 
centers or otherwise shared use of supercomputers, or 
on minisupercomputers or superminicomputers, or all 
three.
• Because of their steep initial cost, industrial 
organizations look for ways to defer purchases of 
supercomputers. Once one or two in an industry 
acquire them, there is both a "bandwagon" effect and a 
fear of being left behind competitively. Computational 
chemistry is a relatively new use for supercomputers.
AberdeenGroup 143


--- Page 158 ---

AberdeenGroup 144
Source: 
Cray Research
AberdeenGroup
SUN 2/170 
File Servers
SUN 3/180 
File Servers
'Backbone" Ethernel
Worksiabons
SUN 3/180'S 
"Gateways"
WorkslaiKins
PYRAMID 
98x 
UNIX 4.2/V
I
VAX 11/750 
UNIX
VAX 8200 
ULTRIX
SUN 3-160
VME
TCP / IP Internet
Cray Research, Inc. - Mendota Heights
1
PYRAMID 
90X
UNIX 4.2/V
SUN 3/180 
File Server
IBM 4381 
MVS
VAX 8250 
VMS
Amdahl 
470/V8 
VM/CMS
SUN 3-160
VME
VAX 11/785 
VMS
CRAY X.MP/48
CRAY X.MP/14se
UNICOS / COS - Dedicated 
SN 501
CRAY X-MP EA/464
UNICOS - Development
' SN 1101
HYPERchannel
ETHERNET
CRAY.2/1.16
UNICOS - Development UNICOS - Production'.
SN 951 (0-1) 
SN 236
Hix 
Channol
TI Remote 
Link
o! CRAY X.MP/416 
CRAY X.MP/22
UNICOS Pre-Production COS - Development
i SN 218 
SN 101
CRAY Y.MP/832 
CRAY.2S/4.128
UNICOS - Development UNICOS 
SN 1001 
SN 2012
CRAY X.MP/48
COS - Production 
SN 228
VAX 11/785
VMS
AT&T3B20 
UNIX V
IRIS 3030 
Workstation
HP-9000 
350 SRX 
Workstation
|vme|
SUN 3-160C
T
IRIS 4-D 
Workstation
Macintosh tlx 
Workstation
SUN 3/280
File Servers
PIXAR
Apollo 
580 Turbo
Workstations
SUN 3/180
File Servers
12/22/88
Marketing Communications
Symbolics 
3640
DEC 
GPX
Workstations
University of 
Minnesota
]------- | x/50
Workstations
CRAY.2/4.256
UNICOS - Production
SN 2003
Exhibit E-13: Cray Computing Topology


--- Page 159 ---

Conflicting Trends In
Computational Chemistry
and in business terms, no CEO or CFO has yet stood up 
and bragged about how a $20 million laboratory 
instrument just bought them a year-to-market advantage 
over rivals. By early 1990, some are expected to.
• Freewheeling, poorly documented, user-hostile, and 
continually splintering computational chemistry 
software development has hindered full and robust use 
of supercomputers for all but seasoned programs. That 
state of affairs is changing for the better.
Demand Implications
Demand is not a one-way street, and Cray systems impact the overall 
hardware market in several ways:
• For large user organizations, newly installed Crays 
temporarily dampen demand for minisupercomputers.
• As the Crays yield new chemistry, some of the resulting 
calculations can be shifted downstream to less 
expensive (and far superior price/performance) 
systems, either for departmental use or simply for cost 
savings where time-to-completion is less critical.
• Computational chemistry development under UNICOS 
(Cray's version of UNIX) becomes more important, even 
though Digital's VMS — not UNIX — is the preferred 
development system for most chemists.
• Playing to its supercomputing strength, Aberdeen 
expects Cray Research to aggressively promote the 
"quality of results" obtainable only from ab initio 
methods, and to a somewhat lesser extent, 
semi-empirical methods, challenging all suppliers of 
molecular modeling.
• Finer-grain calculations and speed force a demand for 
even better ways of thinking about and viewing 
problems — generically scientific visualization — an area 
of current research and one in which Digital Equipment 
is investing heavily.
Investing in Computational Chemistry Leadership
Cray Research has the highest profit margins of any computer manufac­
turer, and, paying no cash dividend to shareholders, invests those profits 
in products and new markets. In new markets, Cray has targeted three 
AberdeenGroup 145


--- Page 160 ---

specific areas of computational chemistry: pharmaceutical, diversified 
chemicals and materials science, and a set of others including biomedical 
and petrochemical.
Cray is doing far more than targeting prestige accounts. In addition to 
working with leading commercial and academic computational chemistry 
software developers, and developing its own unified computational 
chemistry computing environment, Cray specifically is:
• Collaborating with industrial scientists on 
industry-critical R&D problems where Cray computers 
can assist in a solution
• Organizing and sponsoring computational chemistry 
conferences, symposia, and forums, such as the Biosym 
Consortium
• Pursuing and implementing joint technical ventures 
with industry leaders, as well as participating in and 
funding industry technical consortia
• Funding academic research in computational chemistry, 
and sponsoring and supporting computational 
chemistry scientists in a variety of programs at the cost 
of $1 million per year
• Working with supercomputer centers and other 
governmental supercomputer users on computational 
chemistry application and algorithm development
AberdeenGroup 146


--- Page 161 ---

Conflicting Trends In
Computational Chemistry
APPENDIXF
SPOKE-NODE-RING: THE NEW TOPOLOGY
Executive Summary
Enterprises are evolving their information networks into a new topology 
that Aberdeen describes as Spoke-Node-Ring (SNR). The old models of 
two- and three-tier computing are too restrictive in a world where the dif­
ference between success and failure depends upon harnessing the 
enterprise's full information resources.
Spoke-Node-Ring has evolved out of the unrelenting competitive pressure 
to meet the enterprise's objectives or face extinction.
Spoke-Node-Ring is a road map for integrating heterogeneous computing 
systems into an information network, yet it is also a business planning tool 
to allows MIS to quickly respond to strategic and structural changes.
Those enterprises skilled in integrating different computer systems, dif­
ferent software applications and different communications systems have 
made the greatest progress in implementing Spoke Node Ring. In con­
trast, many suppliers have maintained a one-box-for-one-application 
strategy, each an island unto itself, and are falling farther behind in the 
competitive race. We explore the impact on specific suppliers in the next 
issue.
Executives who understand the organizational, technical and competitive 
implications of implementing Spoke-Node-Ring can provide their 
enterprises with a competitive advantage today. Those that cannot are al­
ready being left behind.
Spoke-Node-Ring
Aberdeen research shows that many enterprises are evolving their existing 
systems into an information network topology that we have identified as 
Spoke-Node-Ring (SNR). (See Exhibit E-6, Appendix E.)
At the heart of SNR is the corporate data node. Here reside the 
mainframes with their banks of mass storage maintaining the sacrosanct 
corporate data. MIS (Management Information Systems) controls this en­
vironment — limiting access and ensuring that the data is auditable and 
secure.
AberdeenGroup 147


--- Page 162 ---

To allow authorized data to be extracted from the corporate data node and 
to assure that only auditable, sanitized data is allowed in, communications 
paths, or spokes, extend from the corporate data node to other areas of the 
enterprise.
The next layer out is the middle-manager ring, where organizational 
productivity applications are run at the enterprise's departmental or line- 
of-business level. The middle-manager level uses peer-to-peer communica­
tions: the organization's success very often depends upon the ability to 
communicate information quickly and efficiently. The middle-manager's 
ability to support outlying sites and enhance customer relations is one of 
the major objectives of organizing an enterprise's information network to 
beat the competition.
Accessing computers on the middle-manager ring are individual produc­
tivity nodes. Typically, similar productivity nodes within a department are 
grouped together in a productivity ring with a LAN (local area network). 
Productivity nodes are the right-tools-for-the-right job. They may be auto­
matic teller machines for retail bank customers, bar code readers for 
manufacturing operations, powerful graphic workstations for designers, 
PCs for clerical workers and terminals for data entry clerks.
To be fully effective, spokes, middle-manager rings and productivity nodes 
are implemented to reflect the enterprise's organizational structure.
Advantages
SNR offers enterprises many advantages over the current helter skelter ap­
proach of implementing applications where the complaining is the 
loudest. Executives tell us that SNR provides:
• Rational information network planning guidelines for 
organizing their enterprise's computing and 
communications resources.
• Synergy gained by specifying how existing 
heterogeneous computing systems can be linked 
together to move data from where it is generated to 
where it is needed.
• The flexibility to react to enterprise structure and 
strategy changes.
• Greater responsiveness to end-user needs and requests 
while upholding MIS' responsibility to protect important 
corporate data.
AberdeenGroup 148


--- Page 163 ---

Conflicting Trends In
Computational Chemistry
• The capability to plan for the implementation of new 
tools, such as powerful workstations with very cheap 
MIPS, that can provide the enterprise with unique, 
competitive advantages.
Impetus For The New Topology
The #1 reason for adopting Spoke-Node-Ring is competitive pressure. 
There is no place for any 1980s-1990s enterprise to hide. Pressure may be 
worldwide for products and services or it might be intradepartmental for 
budget monies. Spoke-Node-Ring can provide an enterprise with greater 
organizational responsiveness to external competitive pressures than two- 
tier, three-tier or everybody-for-themselves topologies.
The #2 reason is the need by MIS executives to resolve the bitter conflict 
between the corporate need for information security and line management 
demands for information dispersion. Lack of security has cost several 
enterprises millions of dollars in embezzlement and unauthorized trading 
losses. Even more frightening is the damaging affect that viruses, whether 
released maliciously or as pranks, can have on the enterprise — destroying 
nonrecoverable data or grinding the enterprise to a halt.
On the other hand, knowledge workers often must access specialized data 
to perform their jobs competently. For example, what good is a high- 
priced financial analyst who does not have access to the cost accounts of 
the enterprise? By isolating access to the corporate data node in middle 
manager nodes, by interconnecting nodes with spokes and by creating 
audit trails from outer nodes to inner nodes, MIS executives can manage 
the constant conflict between strict security and free access of data.
A subtle and little publicly discussed reason for switching to SNR is the 
restructuring of global industry. Lines-Of-Business (LOB) are routinely 
traded; aggressive, financially-managed enterprises are buying and selling 
enterprises of all sizes. Spoke-Node-Ring provides for the separability of 
the LOB information management resource from the corporate data node. 
A monolithic MIS with LOB application integration occurring within a glass- 
walled, central data processing shop can prove to be a corporate liability.
The last major reason why Spoke-Node-Ring is being adopted is that it 
matches the changing role of MIS within enterprises. The very success of 
mainstream applications has meant a slowing of central MIS growth, with 
maintenance of existing applications dominating the software budget.
And, the spectrum of users' real and perceived information needs is grow­
ing beyond MIS' ability to satisfy. Within Spoke-Node-Ring, MIS goes 
beyond the relatively simple task of being the provider of applications to 
AberdeenGroup 149


--- Page 164 ---

that of being the enterprise-wide integrator of applications. This changing 
role makes MIS the catalyst for improving the enterprise's daily effective­
ness.
Driving Forces
Technology and user trends have been converging over the last several 
years to accelerate the adoption of Spoke-Node-Ring. Four major forces 
are driving the trend (See Exhibit F-2).
Exhibit F-1: Forces Driving Spoke-Node-Ring Topology
Easy-to-Implement 
Applications
Line-of-Business 
Applications
Source:
Cheap 
Productivity- 
Node Mips
Computer 
Literacy
Spoke 
Node- 
Ring
Low-Cost 
Communications
Higher Customer 
Service Levels
Supplier 
Standards
User Protection 
of Investments
AberdeenGroup
AberdeenGroup 150


--- Page 165 ---

Conflicting Trends In
Computational Chemistry
The most significant driving force has been the emergence of easy-to-imple- 
ment applications at a time when line-of-business and departmental 
managers have been given the discretion to invest major funds with mini­
mal corporate review. The result has been a power shift in decision 
making from MIS to line managers. As a result, the corporate data node is 
often viewed as an overhead cost center while the middle-manager ring is 
considered part of a revenue-producing profit-and-loss center.
The second driving force has been the incorporation of cheap MIPS on the 
desktop at a time when user familiarity with computers is at an all time 
high. Thirty years after the war on computer illiteracy started in response 
to the Spumik launching, many individuals can pick up a PC or a Macin­
tosh and operate it without a data processing guru. More to the point, it is 
typically less expensive to run applications on desktop computers at 
$2,000-3,000 per MIPS (Million Instructions Per Second) than on 
midrange computers at $50,000 per MIPS or mainframes at $150,000 per 
MIPS. Applications are migrating from mainframes to workstations with 
middle manager rings to productivity nodes — and often back up again — 
depending upon complexity, capacity, security, training, and other require­
ments. In this driving force, middle manager nodes are increasingly acting 
as organizational coordinators among all entities and databases.
The third driving force has been the over supply of lower-cost communica­
tions and enterprises' use of higher service levels as a competitive tool. 
For example, an overnight delivery service's ability to locate a package 
anywhere in its distribution system has increased its customer satisfaction 
and created a very real, high barrier to entry for potential rivals. The tacti­
cal distribution of information to increase an enterprise's quality of service 
— adding value to a product or service by coupling to it information al­
ready captured within the enterprise — can be implemented best using the 
Spoke-Node-Ring topology.
The fourth driving force has been suppliers' willingness to sit together and 
propose meaningful common standards in such vital areas as operating 
systems, database services and communications protocols, just as users 
are desperately searching for mechanisms to protect their investments in 
computer and communications products. Spoke-Node-Ring recognizes 
that all major enterprises already have in place numerous different sys­
tems based on proprietary architectures. To many MIS executives, future 
open systems based on standards represent just another class of comput­
ing platforms that may have severe functional deficiencies. But by using 
the Spoke-Node-Ring guidelines, standard, open systems can be used 
where appropriate while proprietary systems can be kept in places where 
they best serve the organization.
AberdeenGroup 151


--- Page 166 ---

The Future
Spoke-Node-Ring topology will continue to evolve within enterprises well 
into the next decade — the acceleration of technological innovation and in­
creasing global competition will assure that.
The result is that the executives within an enterprise will find themselves 
more responsible — and accountable — for proactively managing their infor­
mation networks in the future than they have in the past.
Who can provide the necessary Spoke-Node-Ring guidance? While in­
dividual equipment and software vendors offer it, they lack the objectivity 
and the breadth of knowledge required to provide an enterprise with a 
comprehensive and fully competitive information system. Third-party 
providers increasingly fill the gap.
p 152


--- Page 167 ---



--- Page 168 ---

Exhibit E-6: Spoke-Node-Ring Topology
Spoke
Corporate 
Data Node
Middle
<Manager 
\ Ring
Productivity 
Ring
Source:
AberdeenGroup


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | conflicting-trends-computational-chemistry-fe5c31 |
| title | Conflicting Trends In Computational Chemistry |
| author | Charles T. Casale |
| date | 1989-01 |
| type | market-study |
| subject_domain | computational-chemistry |
| methodology | industry-analysis, competitive-profiling, market-sizing, expert-opinion |
| source_file | CompChem.pdf |
| license | CC-BY-4.0 |

### Abstract

First Aberdeen Group full-length market research report. Quantifies the 1988 computational chemistry market at $237 million combined software/hardware revenues and profiles seven molecular modeling software firms and twelve hardware suppliers. Argues that the field's commercial leverage — accelerating drug, polymer, and materials discovery — will drive sustained 35-65% growth, while predicting that no single hardware platform (supercomputers, workstations, or minisupers) will dominate as computing momentum cyclically shifts. Notes original publication January 1989; cover of recovered copy reads May 1989 (likely reprint).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First Aberdeen Group full-length market research report (January 1989). Researched 1988, published January 1989 with May 1989 reprint. Exemplar of the firm's founding methodology; one of very few Aberdeen full-length studies recovered. Defined the computational chemistry market category. |
| **Relevance** | medium | Specific revenue figures and vendor lineups are dated, but the framework (leverage thesis, cyclic hardware platform shifts, scientific + commercial drivers) remains analytically useful and prefigures later in silico drug discovery booms. |
| **Prescience** | [DEFERRED] | Predictions about cyclic computing platform dominance, sustained sector growth, and IBM's emergence as a sleeper in technical markets require Phase 3 outcome verification against 1990-2010 history. |

### Prescience Detail


**Prediction 1:** Industry leverage thesis
- **Claimed:** Computational chemistry payoff in chemical industry measured in hundreds of millions to billions of dollars if discovery time reduced even modestly
- **Year:** 1989-1993
- **Confidence at time:** medium

**Prediction 2:** Hardware sales projection
- **Claimed:** $275 million (up 31 percent over 1988)
- **Year:** 1989
- **Confidence at time:** high

**Prediction 3:** Billion-dollar revenue milestone
- **Claimed:** Computational chemistry revenues will not reach the billion-dollar level until 1993
- **Year:** 1989-2000
- **Confidence at time:** medium

**Prediction 4:** Hardware platform oscillation
- **Claimed:** Revenue mix among local-compute servers, central-site computers, and workstations to vary substantially year-to-year; each segment capturing 15-40 percent of overall hardware sales in any given year
- **Year:** 1989-1995
- **Confidence at time:** high

**Prediction 5:** Hardware growth volatility
- **Claimed:** Aggregate hardware sales growth rates in individual years varying as much as 10+ percentage points around a 35 percent average
- **Year:** 1989-1995
- **Confidence at time:** medium

**Prediction 6:** Software maintenance fee trend
- **Claimed:** 12 percent plus maintenance fees should drop to 10 percent by 1993
- **Year:** 1989-1993
- **Confidence at time:** medium

**Prediction 7:** IBM positioning in technical markets
- **Claimed:** Casale calls IBM a real sleeper gearing up for a lengthy assault on technical markets including computational chemistry
- **Year:** 1989-1995
- **Confidence at time:** medium

**Prediction 8:** IBM execution risk
- **Claimed:** Distinct risk that IBM will not stay the course because of inability to keep up competitively with technical product offerings - shorter life cycles and corporate nimbleness usually absent
- **Year:** 1989-1995
- **Confidence at time:** medium

**Prediction 9:** PC RT bolstering strategy
- **Claimed:** IBM offering Polygen products on PC RT to bolster one of the least respected workstation lines in the industry
- **Year:** 1988-1989
- **Confidence at time:** medium

**Prediction 10:** Three-way hardware war
- **Claimed:** Early 1990s will witness a major struggle for computational chemistry customer allegiance between Digital and IBM, with Cray Research fighting for machine placements independent of which system supplier is chosen
- **Year:** 1990-1993
- **Confidence at time:** high

**Prediction 11:** Multiflow break-even projection
- **Claimed:** expected to break even in 1989
- **Year:** 1989
- **Confidence at time:** medium

**Prediction 12:** Drug industry focus
- **Claimed:** Drug design has been principal focus of all computational chemistry companies; projected payoff period typically a decade
- **Year:** 1988-1998
- **Confidence at time:** high

**Prediction 13:** Semiconductor life extension
- **Claimed:** Computational chemistry quantum-effects work will extend semiconductor technology 10-15 years beyond current limits if successful
- **Year:** 1988-2003
- **Confidence at time:** medium

**Prediction 14:** Software differentiation imperative
- **Claimed:** Successful future software differentiation must include proprietary chemistry or data, quantifiable leadtime advantage, or superior support; vendors relying on hardware markups can expect a profit squeeze
- **Year:** 1989-1995
- **Confidence at time:** medium

**Prediction 15:** Market scenario assessment
- **Claimed:** Aberdeen believes the correct outlook is much closer to the finite element analysis model (double-digit millions revenue, protracted losses then high profits, slow scale-up, high tech hurdles) than the CAD/CAM model (single-digit billions, faster profits, many suppliers)
- **Year:** 1989-1995
- **Confidence at time:** high

**Prediction 16:** CAD/CAM-like packages timing
- **Claimed:** Some CAD/CAM-like packages aimed at less-than-PhD practitioners will be on the market in 1990-91
- **Year:** 1990-1991
- **Confidence at time:** medium

**Prediction 17:** System integrator role
- **Claimed:** System integrators similar to those in FEA and CAD/CAM will mechanize routine design problems, increasing user count by at least 5x
- **Year:** 1990-2000
- **Confidence at time:** medium

**Prediction 18:** Spoke-Node-Ring adoption
- **Claimed:** SNR will be the topology that accommodates different growth/decline/assimilation rates across enterprise units
- **Year:** 1989-1995
- **Confidence at time:** low

**Prediction 19:** Cyclic computing momentum thesis
- **Claimed:** Computer industry will continue its 40-year pattern of computing momentum shifting noisily among shared large systems, single-user smaller systems, and departmental systems
- **Year:** 1989-2005
- **Confidence at time:** high

**Prediction 20:** Survivor profitability
- **Claimed:** After a period of respectable but unspectacular growth accompanied by hardware and software vendor shakeouts, field should become highly profitable for those with deep enough pockets to stay the course
- **Year:** 1995-2000
- **Confidence at time:** medium


### Entities Referenced (24)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Charles T. Casale | person | [DEFERRED] | [DEFERRED] |
| Peter S. Kastner | person | active | [DEFERRED] |
| John R. Logan | person | [DEFERRED] | [DEFERRED] |
| Aberdeen Group, Inc. | company | dissolved | Harte-Hanks (later acquired) |
| BioDesign, Inc. | company | [DEFERRED] | [DEFERRED] |
| BIOSYM Technologies, Inc. | company | [DEFERRED] | Acquired by MSI -> Accelrys -> Dassault Systemes BIOVIA |
| Chemical Design Ltd | company | [DEFERRED] | [DEFERRED] |
| Molecular Design Limited | company | [DEFERRED] | Acquired by MDL Information Systems -> Elsevier MDL -> Symyx -> Accelrys |
| Polygen Corporation | company | [DEFERRED] | Merged with Molecular Simulations Inc. |
| Quantum Chemistry Program Exchange | institution | [DEFERRED] | [DEFERRED] |
| Tripos Associates, Inc. | company | [DEFERRED] | Tripos -> Certara |
| Alliant Computer Systems Corporation | company | dissolved | [DEFERRED] |
| Apollo Computer, Inc. | company | dissolved | Acquired by Hewlett-Packard 1989 |
| Ardent Computer Corp. | company | dissolved | Merged with Stellar to form Stardent 1989; dissolved 1991 |
| Convex Computer Corporation | company | dissolved | Acquired by Hewlett-Packard 1995 |
| Cray Research, Inc. | company | dissolved | Acquired by SGI 1996, sold to Tera/Cray Inc. |
| Digital Equipment Corporation | company | dissolved | Acquired by Compaq 1998 -> HP 2002 |
| Evans & Sutherland Computer Corporation | company | active | [DEFERRED] |
| FPS Computing, Inc. | company | dissolved | Acquired by Cray Research 1991 |
| International Business Machines Corporation | company | active | [DEFERRED] |
| Multiflow Computer, Inc. | company | dissolved | Defunct 1990 |
| Silicon Graphics, Inc. | company | dissolved | Bankrupt 2009; assets acquired by Rackable -> HPE |
| Star Technologies, Inc. | company | dissolved | [DEFERRED] |
| Stellar Computer Inc. | company | dissolved | Merged with Ardent to form Stardent 1989; dissolved 1991 |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Computational Chemistry | application | multi-vendor | emerging | mature |
| Molecular Modeling | application | multi-vendor | emerging | mature |
| Quantum Chemistry Codes | application | academic+commercial | mature | mature |
| Minisupercomputer | platform | Alliant/Convex/Multiflow | growing | obsolete |
| Supercomputer | platform | Cray/IBM | mature | niche |
| Graphics Workstation | platform | SGI/Apollo/Stellar/Ardent/E&S | growing | obsolete-or-superseded |
| Superminicomputer | platform | DEC/HP/IBM | mature | obsolete |
| Mainframe | platform | IBM | mature | niche |
| IBM PC RT (RT/PC) | platform | IBM | introduced | obsolete |
| Array Processor | platform | FPS/Star Technologies | mature | obsolete |

### Observation Summary

- Total observations: 64
- By type: market-data: 26, viability-prediction: 20, market-size: 4, expert-opinion: 4, user-base: 2, market-mechanism: 2, framework: 2, growth-rate: 1, scientific-significance: 1, user-profile: 1, document-review: 1
