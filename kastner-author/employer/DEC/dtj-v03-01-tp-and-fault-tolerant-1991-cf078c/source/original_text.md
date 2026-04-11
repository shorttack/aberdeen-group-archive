# Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)

> Archived from: dtj-v03-01-1991.pdf
> Original publication date: 1991-01-01
> Author: Digital Equipment Corporation

---

## Original Document Text

Transaction Processing, Databases, 
and Fault-tolerant Systems 
Digital Technical Journal 
Digital Equipment Corporation 
Volume 3 Number 1 
Winter 1991 
Cover Design 
Transaction processing is the common theme for papers in this 
issue. The automatic teller machine on our cover represents one 
of the many businesses that rely on TP systems. If we could look 
behind the familiar machine, we would see the products and 
technologies - here symbolized by linked databases - that 
suppo1·t reliable and speedy processing of transactions worldwide. 
The cover was designed by Dave Bryant of Digital's Media 
Communications Group. 
Editorial 
Jane C. Blake, Editor 
Kathleen M. Stetson, Associate Editor 
Ci.rculation 
Catherine M. Phillips, Administrator 
Suzanne). Babineau, Secretary 
Production 
Helen L. Patterson, Production Editor 
Nancy jones, Typographer 
Peter Woodbury, Illustrator 
Advisory Board 
Samuel H. Fuller, Chairman 
Richard W Beane 
Robert M. Glorioso 
Richard). Hollingsworth 
john W McCredie 
Alan G. Nemeth 
Mahendra R. Patel 
F. Grant Sa viers 
Robert K. Spitz 
Victor A. Vyssotsky 
Gayn B. Winters 
The Digital Tecbnicaljoumal is published quarterly by Digital 
Equipment Corporation, 146 Main Street MLO l-3/B68, Maynard, 
Massachusetts 0175 4-2571. Subscriptions to the journal are $40.00 
for four issues and must be prepaid in 
.S. funds. 
niversity and 
college professors and Ph.D. students in the electrical engineering 
and computer science fields receive complimentary subscriptions 
upon request. Orders, inquiries, and address changes should be 
sent to The Digital Tecbn.ical}oumal at the published-by address. 
Inquiries can also be sent electronically to DTJ®CRJ..DEC.COM. 
Single copies and back issues are available for $16.00 each from 
Digital Press of Digital Equipment Corporation, 12 Crosby Drive, 
Bedford, M A  01730 -1493. 
Digital employees may send subscription orders on the ENET to 
RDVAX::JOURNAI. or by interoffice mail to mailstop MLO I-3/B68. 
Orders should include badge number, cost center, site location code 
and address. All employees must advise of changes of address. 
Comn1ents on the content of any paper are welcomed and may 
be sent to the editor at the published-by or network address. 
Copyright <D 1991 Digital Equipment Corporation. Copying 
without fee is permitted provided that such copies are made for 
use in educational institutions by faculty members and are not 
distributed for commercial advantage. Abstracting with credit 
of Digital Equipment Corporation's authorship is permitted. All 
rights reserved. 
The information in this journal is subject to change without 
notice and should not be construed as a commitment by Digital 
Equipment Corporation. Digital Equipment Corporation assumes 
no responsibility for any errors that may appear in this journal. 
ISSN 0898-901 X 
Documentation Number EY-F588E-DP 
The following are trademarks of Digital Equipment Corporation: 
DEC, DECforms, DECintact, DECnet, DECserver, DECtp, Digital, the 
Digital logo, LAT, Rdb/VMS, TA, VAX ACMS, VAX CDD, VAX COBOL, 
VAX DBMS, VAX Performance Advisor, VAX RALLY, VAX Rdb/VMS, 
VAX RMS, VAX SPM, VAX SQL, VAX 6000, VAX 9000, VAXcluster, 
VA.Xft, VAXserver, VMS. 
IBM is a registered trademark of International Business Machines 
Corporation. 
TPC Benchmark is a trademark of the Transaction Processing 
Performance Council. 
Book production was done by Digital's Educational Services 
Media Communications Group in Bedford, MA. 
I Contents 
8 
Foreword 
Carlos G. Borgialli 
10 
DECdta-Digital's Distributed 
Transaction Processing Architecture 
Transaction Processing, Databases, 
and Fault-tolerant Systems 
Philip A. Bernstein, William T. Emberton, and Vi jay Trehan 
18 
Digital's Transaction Processing Monitors 
Thomas G. Speer and Mark W Storm 
33 
Transaction Management Support in the 
VMS Operating System Kernel 
William A. Laing, James E. Johnson, and Robert V Landau 
45 
Peiformance Evaluation of 
Transaction Processing Systems 
Walter H. Kohler, Yun-Ping Hsu, Thomas K. Rogers, 
and Wael H. Bahaa-EI-Di n  
58 
Tools and Techniques for Preliminary Sizing of 
Transaction Processing Applications 
William Z. Zahavi, Frances A. Habib, and Kenneth). Omahen 
65 
Database Availability for Transaction Processing 
Ananth Raghavan and T. K. Rengarajan 
70 
Designing an Optimized Transaction Commit Protocol 
Peter M. Spiro, Ashok M. Joshi, and T. K. Rengarajan 
79 
Verification of the First Fault-tolerant VAX System 
William F. Bruckert, Carlos Alonso, and James M .  Melvin 
I Editors Introduction 
Jane C. Blake 
Editor 
Digital's transaction processi ng system s are inte­
grated hardware and software products that operate 
in a distributed environment to support commer­
cial applications, such as bank cash withd rawals, 
credit card t ransactions, and global t rad i ng. For 
these applications, data integrity and continuous 
access to shared resources are necessary system 
characteristics; anything less would jeopardize the 
revenues of business operations that depend on 
these applications. Papers in this issue of the Journal 
look at some of Digital's techologies and products 
that provide these system characteristics in three 
areas: distributed transaction processing, database 
access, and system fault tolerance. 
Opening the issue is a discussion of the architec­
ture, DECdta, which ensures reliable interoperation 
in a distributed environment. Phil Bernstei n, Bill 
Emberton, and Vi jay Trehan define some transaction 
processing termi nology and analyze a TP applica­
tion to illustrate the need for separate architectural 
components. They then present overviews of each 
of the components and interfaces of the distributed 
transaction processing architecture, giving partic­
ular attention to transaction management. 
Two products, the ACMS and DECi ntact monitors, 
implement several of the functions defined by the 
DECdta architecture and are the twin topics of a 
paper by Tom Speer and Mark Storm. Although 
based on different implementation strategies, both 
ACMS and DECintact provide TP-specific services 
for developi ng, executing, and managing TP appli­
cations. Tom and Mark discuss the two strategies 
and then highlight the functional similarities and 
differences of each monitor product. 
The ACMS and DECintact monitors are layered on 
the VMS operati ng system, which provides base 
services for distributed transaction management. 
Described by Bill Lai ng, Jim Johnson, and Bob 
Landau, these VMS services, called DECdtm, are an 
2 
addition to the operating system kernel and address 
the problem of integrating data from multiple sys­
tems and databases. The authors describe the three 
DECdtm components, an optimized implementa­
tion of the two-phase commit protocol, and some 
VA.Xcluster-specific optimizations. 
The next two papers turn to the issues of measur­
i ng TP system performance and of sizing a system 
to ensure a TP appl ication will run efficient ly. Walt 
Kohler, Yun-Ping Hsu, Tom Rogers, and Wael Bahaa­
EI-Din discuss how Digital measures and models TP 
system performance. They present an overview of 
the industry-standard TPC Benchmark A and Digital's 
implementation, and then describe an alternative 
to benchmark measurement- a multilevel analyti­
cal model ofTP system performance that simplifies 
the system's complex behavior to a manageable set 
of parameters. The discussion of performance con­
tinues but takes a different perspective in the paper 
on sizing TP systems. Bill Zahavi, Fran Habib, and 
Ken Omahen have wri tten about a methodology 
for estimating the appropriate system size for a TP 
application. The tools, techniques and algorithms 
they describe are used when an appl ication is sti l l  
in i t s  early stages of development. 
High performance must extend to the database 
system. ln their paper on database avai lability, 
Ananth Raghavan and T.K. Rengarajan exami ne 
strategies and novel techniques that minimize the 
affects of downtime situations. The two databases 
referenced in their discussion are the VAX Rdb/YMS 
and VAX D BMS systems. Both systems use a database 
kernel called KODA, which provides transaction 
capabil i t ies and commit processing. Peter Spiro, 
AshokJoshi, and T.K. Rengarajan explain the impor­
tance of commit processing relative to throughput 
and describe new designs for improving the perfor­
mance of group commit processing. These designs 
were tested, and the results of these tests and the 
authors' observations are presented. 
Equal ly as important in TP systems as database 
availability is system availability. The topic of the 
final paper in this issue is a system designed to be 
continously available, the VAX.ft 3000 fault-tolerant 
system. Authors Bill Bruckert, Carlos Alonso, and 
Jim Melvin give an overview of the system and then 
focus on the four-phase verification strategy devised 
to ensure transparent system recovery from errors. 
I thank Carlos Borgialli for his help in preparing 
this issue and for writing the issue's Foreword. 
Biographies I 
Carlos Alonso 
A principal software engineer, Carlos Alonso is a team leader 
for the project to port the System-V operating system to the VAXft 3000. 
Previously, he was the project leader for various VAXft 3000 system validation 
development efforts. As a member of the research group, Carlos developed the 
test bed for evaluating concurrency control algorithms using the VMS 
Distributed Lock Manager, and he designed the prototype alternate lock 
rebuild algorithm for cluster transitions. He holds a B.S.E.E. (1979) from Tulane 
University and an M.S.C.S. (1980) from Boston University. 
Wael Hilal Bahaa-El-Din 
Wael Bahaa-EI-Din joined Digital in 1987 as a senior 
consultant to the Systems Performance Group, Database Systems. He has led a 
number of studies to evaluate performance database and transaction process­
ing systems under response time constraints. After receiving his Ph.D. (1984) in 
computer and information science from Ohio State University, Wael spent 
three years as an assistant professor at the University of Houston. He is 
a member of ACMS and IEE E ,  and he has written numerous articles for profes­
sional journals and conferences. 
Philip A. Bernstein 
As a senior consultant engineer, Philip Bernstein is both 
an architectural consultant i n  the Transaction Processing Systems Group and a 
researcher at the Cambridge Research Laboratory. Prior to joining Digital in 1987, 
he was a professor at Wang Institute of Graduate Studies and at Harvard Univer­
sity, a vice president at Sequoia System s, and a researcher at the Computer 
Corporation of America. He bas published over 60 papers and coauthored two 
books. Phi l  received a B.S. (1971) in engineering from Cornel l  University and a 
Ph.D. ( 197'5) in computer science from the University of Toronto. 
William F. Bruckert 
William Bruckert is a consulting engineer who joined 
D igital in 1969 after receiving a B.S.E.E. degree from the University of 
Massachusetts. He received an M.S.E.E./C.E. degree from the same university 
in 1981. Beginning as a worldwide product support engineer, Bill later worked 
on a number of DECsystem-10/20 designs. He developed the cache, memory, 
and 1/0 subsystem for the VA.,'( 8600 processor and was the system architect 
of the VAX 86'50 processor. His most recent role was as the architect of the VAXft 
3000 system. Bi.ll currently holds seven patents. 
3 
4 
William T. Emberton 
As a principal software engineer, William Emberton is 
currently involved in the development of Queue Management Architecture. He 
is also involved in X/Open and POS!X TP Standards work ancl is a member 
of the team that is developing the overall DECtp product architecture. Previ­
ously, he worked on the initial versions of the DEC:dta architecture. Before com­
ing to Digital in 1987, Bill held positions as Director of Software Development 
at National Semiconductor and Manager of Systems Development for Inter­
national Retail Systems at NCR. He was educated at London University. 
Frances A. Habib 
Fran Habib is a principal software engineer involved with 
the development of transaction processing workload characterization and siz­
ing tools. Previously, Fran worked at Data General and c;TE Laboratories as a 
management science consultant. She holds an M.S. in operations research from 
MIT and a B.S. in engineering and applied science from Harvard. Fran is a full 
member of ORSA ancl belongs to ACM, IEEE, and the AC:YI S!CMETRJC:S special 
interest group on modeling and performance evaluation of computer systems. 
Yun-Ping Hsu 
Yun-Ping is currently a principal software engineer in the 
Transaction Processing Systems Performance and Characterization Group. He 
joined Digital in October 1987, after receiving his master's degree in electrical 
and computer engineering from the University of Massachusetts at Amherst. In 
his position, Yun-Ping is responsible for performance modeling and bench­
mark measurement of both ACMS- and DEC:intact-based TP systems. He also 
participated in the TPC Benchmark A standardization activity during !989 He is 
a member of ACM and IEEE. 
james E. johnson 
A consulting software engineer, Jim Johnson has worked 
for the VMS Engineering Group since joining Digital in 1984. He is current!)' a 
project leader for VMS Engineering in Europe. Prior to this work, Jim led the 
RMS project, and after relocating to the UK three years ago, he was responsible 
for much of the design and implementation of the DEC:dtm services. At the same 
time, Jim was an active participant in the transaction management architecture 
review group. He has applied for a patent pertaining to the two-phase commit 
protocol optimization currently used in DECdtm services. 
Ashok M. Joshi 
Ashok Joshi is a principal software engineer interested in 
database systems, transaction processing, and object-based programming. He is 
presently working on the KODA subsystem, which provides record storage for 
Rdb/VMS and DBMS software. For the Rdb/VMS project, he developed hash 
indexing and record placement features, and he worked on optimizing the lock 
protocols. Ashok came to Digital after receiving a bachelor's degree in electrical 
engineering from the Indian Institute of Technology, Bombay, and a master's 
degree in computer science from the University of Wisconsin, Madison. 
Walter H. Kohler 
As a software engineering senior manager, Walt is respon­
sible for TP system performance measurement and analysis and leads D igital's 
TP benchmark standards activities. Before joining Digital in 1988, Walt was a vis­
iting scientist and technical consultant to Digital and a professor of electrical 
and computer engineering at the Universi ty of Massachusetts at Amherst. He 
holds B.S., M.S., and Ph.D. degrees in electrical engineering, all from Princeton 
University. Walt recently received the IEEE/CS Meritorious Service Award, and 
he has published over 25 technical articles. 
William A. Laing 
William La ing is a senior consu ltant engineer based in 
Newbury, England. He is the technical leader for production systems support 
for the VMS operating system. During five years spent in the U.S., Bi ll was 
responsible for the design and init ial development of symmetrical multi­
processing support in the VMS system. He joined Digital in 1981, after doing 
research on operating systems at Edinburgh University for nine years. Bill holds 
a B.Sc. (1972) in mathematics and computer science and an M.Phil. (1976) in 
computer science, both from Edinburgh University. 
Robert V. Landau 
Principal software engineer Robert Landau is a member of 
the VMS Engineering Group, based in Newbury, England. He is currently the 
project leader of a VMS advanced development team investigat ing a high-perfor­
mance, transaction-based, flat file system. Before joining D igital i n  1987, Bob 
worked for a variety of software houses specializing in database-related prod­
ucts. He studied botany at London University and, subsequently, obta ined a 
teaching qualification from Hereford College. 
James M. Melvin 
As a principal design engineer, Jim was responsible for the 
specification of hardware error-handling mechanisms i n  the VAXft system and is 
presently an engineering project leader for future VA.,'(ft systems. He also speci­
fied and led the implementation of t he hardware system simulation platform 
and the hardware design verification test plan. Jim joined D igital in 1984 and 
holds a B.S.E.E. (1984) and an M.S. (1989) in engineering management from 
Worcester Polytechnic Institute. He holds three patents on the VAXft 3000 sys­
tem, al l related to error handling in a fault-tolerant system. 
Kenneth]. Omahen 
A principal engineer, Kenneth Omahen is developing 
object-oriented queuing network solvers. He designed a variety of perfor­
mance tools and performed design support stud ies which influenced a number 
of Digital products. Prior to joining D igital, Ken worked at Bel l  Telephone 
Laboratories, lectured at the University of Newcastle-Upon-Tyne, and was a 
faculty member at Purdue University. He received a B.S. degree i n  science engi­
neering from Northwestern University and M.S. and Ph.D. degrees in informa­
tion sciences from the University of Chicago. 
5 
Biographies 
6 
Ananth Raghavan 
Since joining D igital i n  1988, Ananth Raghavan has been 
a software engineer who has led projects for the KODA/Rdb Group. Previous to 
this position, he was a teaching assistant in the computer science department 
of the University of Wisconsin. Anant h  holds a B.S. ( 1985) degree in mechani­
cal engineering from the I ndian Institu te of Technology, Madras, and an M.S. 
( 1987) degree in computer science from the University of Wisconsin, Mad ison. 
He has two patent applications pend i ng for his work on undo and undo/redo 
database algorithms. 
T. K. Rengarajan 
T. K. Rengarajan has been a member of the Database 
Systems Group since 1987 and works on the KODA software kernel for database 
management systems. He is involved in the support for WORM devices and 
global buffer management in the VA..'\cluster environment. His work in the areas 
of boundary element methods and database management systems is reported in 
several published papers and patent applications. Ranga holds an M.S. degree in 
computer-a ided design from the University of Kentucky and an M.S. in com­
puter science from the University of Wisconsin. 
Thomas K. Rogers 
Thomas Rogers is a project leader for the Transaction 
Processing Systems Performance ami Characterization Group. He is respon­
sible for testing the V.A.,'C 9000 Model 210 system using the TPC Benchmark A 
standard. Prior to joining D igital in January 1988, Tom worked for Sperry 
Corporation as a techn ical specialist for t he Nort heast region. He received a 
bachelor of science degree in mathematical sciences in 1979 from Johns 
Hopkins University. 
Thomas G. Speer 
As a principal software engineer i n  t he DECtp/East 
Engineering Group, T homas Speer is currently lead i ng the D ECintact V2.0 pro­
ject. In this position, his major responsi bility is defining the requirements for 
DECintact support of DECdtm services, client/server database access, and sup­
port for the DECforms product. Since joining Digital in 1981 , Tom has worked 
on several development projects, including FORTRAN-10/20 and RMS-20. He holds 
degrees from Harvard University, Rutgers University, and Simmons College. He 
is a member of Phi Beta Kappa. 
Peter M. Spiro 
Peter Spiro, a principal software engineer, is currently 
involved in optimizing database technology for RISC machines. He has worked 
on database facilities such as access methods, journali ng and recovery, trans­
action protocols, and buffer management. Peter joined D igital i n  1985, after 
receiving M.S. degrees in forest science and computer science from the 
University ofWisconsin. He has a patent pend ing for a method of database jour­
nal ing and recovery, and he authored a paper for an earlier issue of the Digital 
Technical journal. In addition, Peter enjoys the game of Ping-Pong. 
Mark W. Storm 
Consulting engineer Mark Storm was one of t he original 
designers of the ACMS monitor, and he has been involved in the development of 
TP products for more than ten years. Currently, he is acting technical d irector 
for the East Coast Transaction Processing Engineering Group, as well as manag­
ing a small advanced development group. After joining Digital i n  1976, Mark 
worked on COBOL compi lers for the PDP-11 systems and developed the first 
native COBOL compiler for the VAX computer. He holds a B.S. (with honors) in 
computer science from the University of Southern M ississippi. 
Vijay Trehan 
Since joining Digital in 1978, Vijay Trehan has contributed to 
several architecture projects. He is the technical d irector responsi ble for 
DECtp architecture, design, and standards work. Prior to this assignment, Vijay 
was the archi tect for t he DECdtm protocol, architect for the DDIS data inter­
change format, and initiator of work on the DDIF document interchange format 
and compound document strategy. He holds a B.S. ( 1972) in mechanical engi­
neering from t he Ind ian Institute of Technology and an M.S. ( 1974) in operations 
research from Syracuse University. 
William Z. Zahavi 
As an engineering manager, Bill is responsible for the 
design and development of predictive sizing tools for transaction processing 
app.lications. Before joining D igital in 1987, he was a technical consultant for 
Sperry Corporation, specializing in systems performance analysis and capacity 
planning. Bil l  received an M .B.A. from Northeastern University and a B.S. in 
mathematics from the University of Virginia. He is an active member of the 
Computer Measurement Group, and frequently presents at CMG conferences. 
7 
I Foreword 
Carlos G. Borgialli 
Senior Manager, DECtp Software 
Engineering 
Transaction p rocessing is one of the largest, most 
rapidly growing segments of the computer i ndus­
try. Digital's strategy is to be a leader in transaction 
processing, and toward that end we are making 
technological advances and delivering products to 
meet the evolving needs of businesses that rely on 
transaction processing systems. 
Because of the speed and rel iability with which 
transaction processing systems capture and dis­
play up-to-date information, they enable businesses 
to make well-informed, timely decisions. Industries 
for which transaction processing systems are a sig­
nificant asset i nclude banking, laboratory automa­
tion, manufacturing, government, and insurance. 
For these industries and others, transaction pro­
cessing is an information l ifeli ne that supports the 
achievement of da ily business objectives and in 
many instances provides a competitive advantage. 
Many older transaction processing systems on 
which businesses rely are centralized and tied to a 
particular vendor. A great deal of money and time 
has been invested in these systems to keep pace 
with busi ness expansion. As expansion continues 
beyond geographic boundaries, however, the cen­
tralized, s ingle-vendor transaction p rocessing sys­
tems are less and less likely to offer the flexibility 
needed for round-the-clock, reliable, business 
operations conducted worldwide. Transaction pro­
cessi ng technology therefore must evolve to 
respond to the new business environment and at 
the same time protect the i nvestment made in 
existing systems. 
Our research efforts and innovative p roducts 
provide the transaction processi ng systems that 
businesses need today. The demand for distributed 
8 
rather than centralized systems has focused atten­
tion on system management. Queuing services, 
highly available systems, heterogeneous environ­
ments, security services, and computer-a ided soft­
ware engineering (CASE) are a few examples of 
areas in which research and advanced develop­
ment efforts have had and will continue to have a 
major impact on the capabilities of transaction 
processing systems. 
Transaction processing solut ions require the 
application of a w ide range of technology and the 
integration of multiple software and hardware 
products: from desktop to mainframe: from presen­
tation services and user interfaces to TP monitors, 
database systems, and computer-a ided software 
eng ineeri ng tools; from optim ization of system 
performance to optimization of availability. Making 
all of this tcch.nology work well together is a great 
challenge, but a challenge D igital is uniquely posi­
tioned to meet. 
D igital ensures broad appl ication of its trans­
action p rocessing technology by defi n i ng an 
architecture, the Digital Distribu ted Transaction 
Architecture (DECdta). DE Cdta, about which you will 
read in this issue, defines the major components of 
a Digital TP systt:m and the way those components 
can form an integrated transaction processi ng sys-­
tem. The DECdta architecture describes how data 
and processing are easily d istributed among m ulti­
ple VAX processors, as well as how the components 
can interoperate in a heterogeneous environment. 
The DECdta architecture is based on the client/ 
server computing model, which allows D igital to 
apply its traditional strengths in networking and 
expandabi I ity to transaction processing system 
solutions. In the DECdta client/server computing 
model, the client portion interacts with the user to 
create processing requests, and the server portion 
performs the data manipulation and computation 
to execute the processing request. T his computing 
model facilitates the division of a TP system into 
small components in three ways. It al lows for dis­
tribut ion of functions among VA_,\: p rocessors; it 
part itions the work performed by one or more of 
the components to allow for parallel processing; 
or it repl icates functions to achieve higher ava i l­
ability goals. These options permit the customer 
to purchase the configuration that meets present 
needs, confident that the system will allow smooth 
expansion in the future. 
Further, the D ECdta architecture sets a direction 
for its evolution through different products in a 
coord inated manner. It provides for the cooper­
ation and interoperation of components imple­
mented on different platforms, and it supports the 
expansion of customer applicat ions to meet growth 
requirements. The DECdta architecture is designed 
to work with other Digital architectures such as the 
Digital Network Architecture (DNA), t he network 
application services (NAS), and the Digi tal database 
architecture (DDA). Moreover, the DECdta architec­
ture supports industry standards that enable the 
portability of applications and their interopera­
tion in a heterogeneous environment, such as the 
standard appl ication programming interfaces being 
developed by the X/Open Transaction Processing 
Working Group and the IEEE POSJX. Standard wire 
protocols that provide for systems interoperation 
in a mult ivendor, heterogeneous environment are 
being developed by the International Standards 
Organization as part of the Open System Inter­
connection activities. 
Among the products D igital has developed speci­
f ically for TP systems are the TP monitors. These 
monitors provide the system integration "glue," if 
you will. Rather than act as their own systems inte­
grators, customers who use D igital's TP monitors 
are able to spend more t ime on solving bus iness 
problems and less t ime on solving software inte­
gration problems, such as how to make forms and 
database products work together smoothly. 
Digital's TP moni tors run on all types of hard­
ware configurations, including local area networks 
(LANs), wide area networks (WAJ'\Is), and VAXcluster 
systems. The DECdta client/server computing model 
provides the necessary flexibility to change hard­
ware configurations, thus allowing reconfigura­
t ion without the need for any source code changes. 
The two TP moni tors, DECintact and VAX AG•IS, 
integrate vital D igital technologies such as the 
Digital Distributed Transaction Manager (DECcltm) 
and products such as D igital's forms systems 
(DECforms) and our Rdb/VMS or VË'\ DBMS data­
base products. DECdtm uses the two-phase com­
mit protocol to solve the complex problem of 
coordinating updates to multiple data resources 
or databases. 
Major developments in Digital's database prod­
ucts have enhanced the strengths of its overal l 
product offerings. The two mainstream database 
products noted above, Rdb/VMS and VA,"( DBMS, 
layer on top of a database kernel called KODA, thus 
providing data access independent of any data 
model. The services made available by KODA, 
besides its high performance, allow D igital's data­
base products to eff iciently support TP applica­
tions as well as to provide rich functionality for 
general-purpose database appl ications. 
For those TP systems that require user inter­
faces, DECforms provides a device-independent, 
easy-to-use human interface and perm its the sup­
port of multiple devices and users within a single 
appl ication. 
TP systems that require high ava ilability or con­
t inuous operations are supported by the VË'X fam­
ily of hardware and software. The introd uct ion of 
the fault-tolerant VAXft 3000 system, added to the 
successful V'Xcluster system, allows for a high 
level of system availability. Performance needs 
also are be ing met by a combination of hardware 
resources. including the VAX 9000 system. 
This combinat ion of architecture, software, and 
hardware technology, and support for emerging 
industry standards places D igital in an excellent 
posi t ion to become the industry leader for dis­
tributed, portable transaction processing systems. 
The papers in this issue of the Journal provide a 
view of the key elements of Digital's distributed 
transaction processing technologies. 
Many individuals, teams, organizations, and busi­
ness partners are respons ible for bringing Digi tal's 
TP vision to fru it ion. Their dedication, hard work, 
and creativity will continue to drive t he develop­
ment of new technologies t hat enhance our family 
of products and services. 
9 
I 
Philip A. Bernstein 
William T. Emberton 
Vijay Trehan 
DECdta -Digitals Distributed 
Transaction Processing 
Architecture 
Digital's Distributed Transaction Processing Architecture (DECdta) describes tfJe 
modules and interfaces that are common to Digital's transaction processing 
(DECtp) products. The architecture allows easy distribution of DECtjJ products. 
fn particular. it supports client/server style applications. Distributed transaction 
management is the main function that ties DECdta modules together it ensures 
that application programs, database systems, and other resource managers inter­
operate reliably in a distributed ystem. 
Transaction processing (TP) is the activity of execut­
ing requests to access shared resources, typical ly 
databases. A computer system that is configured to 
execute TP applications is cal led a TP system. 
A transaction is an execution of a set of opera­
tions on shared resources that has the following 
properties: 
• 
Atom ici ty. Either aJ J of the transaction ·s opera­
tions execute, or the transaction has no effect 
at all. 
• 
Serializabili ty. The set of all operations that exe­
cute on behalf of the transaction appears to 
execute serially with respect to the set of opera­
tions executed by every other transaction. 
• 
Durabi lity. The effects of the transaction's oper­
ations are resistant to fa i lures. 
A transaction terminates by executing the com­
mit or abort operation. Commit tells the system to 
install the effect of the transact ion's operations 
permanently. Abort tells the system to undo the 
effects of the transaction's operations. 
For enhanced reliabi lity and availabil ity, a TP 
application uses transactions to execute requests. 
That is, the application receives a request message 
(from a display, computer, or other device), exe­
cutes one or more transactions to process the 
request, and possibly sends a reply to the origina­
tor of the request or to some other parry specified 
by the originator. 
TP appl ications are essential to the operation 
of many industries, such as finance, reta il, health 
care, transportation, government, communications, 
10 
and manufacturing. Given the broad range of appli­
cations of TP, D igital offers a wide variety of prod­
ucts with which to build Tl' systems. 
DECtp is an u mbrel la term that refers to Digi tal's 
TP p roducts. The goal of DECtp is to offer an inte­
grated set of hardware and software products 
t hat supports the development, execution, and 
management of TP appl ications for enterprises of 
all sizes. 
DECtp systems include software components 
that are specialized for TP, notably TP monitors 
such as the ACMS and DECintacr TP monito rs, and 
transaction managers such as the DEC:dtm trans­
action manager. '' DECtp systems also req uire the 
integration of general-purpose hardware products 
(processors, storage, communications, and termi­
nals) and software products (operat ing systems, 
database systems, and com munication gateways). 
These products are typically integrated as shown 
in Figure l. 
TP APPLICATION 
TP MONITOR 
DATABASE SYSTEMS 
FORMS MANAGER 
OPERATING SYSTEM 
COMMUNICATION SYSTEM 
Figure 1 
Layering of Products to Support 
a TP Application 
Vol. .l No. I 
Willll!r J')')J 
Digital Tec!Jnical jounwl 
DECdta - Digital's Distributed Transaction Processing Architecture 
Appl ications on DECtp systems can be designed 
using a client/server paradigm. This paradigm is 
especially useful for separating the work of prepar­
ing a request from that of running transactions. 
Request preparation can be done by a front-end 
system, that is, one that is close to the user, in 
which processor cycles arc inexpens ive and inter­
active feedback is easy to obtain. Transaction 
execution can be done by a larger back-end sys­
tem, that is, one that manages large databases 
and may be far from the user. Back-end systems 
may themselves be distributed . Each back-end 
system manages a p orrion of the enterprise 
database and executes appl ications, usually ones 
that make heavy use of the database on that back 
end. DECtp products are modu larized to al low easy 
distribution across front ends and back ends, 
which enables them to support client/server style 
applications. DECtp systems thereby simplify pro­
gramming and reconfiguration in a d istributed 
system. 
Digital's Distributed Transaction Processi ng 
Architecture (DECdta) defines the modularization 
and distribution structure that is common to DI'Ctp 
products. D istributed transaction management is 
the main function that tics this structu re together. 
This paper describes the DECdta structure and 
explains how DECdta components are integrated 
by distributed transaction management. 
Current versions of DECtp products implement 
most, but not all, modu les and interfaces in the 
DECdta architecture. Gaps between the architec­
ture and products will be fi lled over time. DECtp 
products that current ly imp lement DECdta compo­
nents are referenced throughout the paper. 
TP Application Structure 
By analyzing TP applications, we can see where the 
need arises for separate D ECdta components. A 
typical TP appl ication is structured as follows: 
Step 1 :  The client application interacts with a 
user (a person or machine) to gather input, e.g., 
using a forms manager. 
Step 2 :  The client maps the user's input into a 
request, that is, a message that asks the system to 
perform some work. The client sends the request 
to a server appl ication to process the request. 
A request may he direct or queued. Jf direct, the 
client expects a server to process the request right 
away. If queued, the client deposits the request 
in a queue from which a server can dequeue the 
request later. 
Digitu/ Teclmicul jouniUI 
Vol. ,) Nu I 
Winter t'J'JI 
Step 3: A server processes the request by 
executing one or more transactions. Each trans­
action may 
a. Access multiple resources 
b. Cal. I programs, some of which may be remote 
c. Generate requests to execute other transactions 
d. Interact with a user 
e. Return a reply when the transaction finishes 
Step 4: If the transaction produces a reply, then 
the client interacts with the user to display that 
reply, e.g., using a forms manager. 
Each of the above steps involves the interaction 
of two or more programs. In many cases, it is desir­
able that these programs be distributed . To dis­
tribute them conveniently, it is important that the 
programs be in separate components. For exam­
ple, consider the fol lowing: 
• 
The presentation service that operates the dis­
play and the application that controls which 
form to display may be distributed. 
One may want to off-load presentation services 
and related functions to front ends, whi le allow­
ing programs on back ends to control which 
forms are displayed to users. This capability is 
useful in Steps 1, 3d, and 4 above to gather input 
and display output. To ensure that the presenta· 
tion service and application can be distribu ted, 
the presentation service should correspond to a 
separate DECdta component. 
• 
The cl ient appl ication that sends a request and 
the server application that processes the request 
may be distribu ted. The applications may com­
municate through a nerwork or a queue. 
In Step 2, front-end applications may want to 
send requests direct ly to back-end applicat ions 
or to place requests in queues that are managed 
on back ends. Simi larly, in Step 3c, a trans· 
action, T, may enqueue a request to run another 
t ransaction, where the queue resides on a d if­
ferent system than T. To max imize the flexibil­
ity of distributing request management, request 
management should correspond to a separate 
DECdta component. 
• 
Two transaction m anagers that want to run a 
commit protocol may be distributed. 
For a transaction to be distributed across different 
systems, as in Step 3b, the transaction management 
1 1  
Transaction Processing, Databases, and Fault-tolerant Systems 
services must be dist ributed. '1() ensure that each 
t ransaction is at omic, the t ransac tion manage rs on 
these systems must con trol t ransac tion commit­
ment using a common commit prot ocol. To com­
plicate matters, there is more t han one widely used 
protocol for t ransac ti on commit men t. To the 
extent possible, a system should allow inte ro pe ra­
t ion of these protocols. 
To ensure that t ransact ion managers can be dis­
t ributed, the t ransact ion man ager should be a 
component of DEC:dt a. Tc> ensure that they c an 
intero pe rate, the ir t ransaction prot ocol should 
also be in DECdta. To ensure that (liffe rent commit 
protocols em be supported , the part of transaction 
management that defines the protocol for inte r­
act ion with remote t ransac tion manage rs should 
be separated fro m  the part that coordinates t rans­
act ion exec ution ac ross local resources. In the 
DECdt a architecture, the forme r  is called a commu­
nicat ion manager, and the latte r is called a t rans­
act ion manager. 
Inte rope rat ion of t ransaction manage rs and 
resource managers, such as (latabasc systems, also 
affects the modularization of DEC:dta components. 
A t ransaction may involve clifferent types of 
resources, as in Step :)a. For example, it may update 
dat a  that is managed by different database systems. 
To cont rol t ransaction commit men t, the t ransac­
tion manage r must interact with d ifferent resource 
manage rs, possi bly supplied by diffe rent vendors. 
This requires that resource managers be separate 
components of DEC:dta. 
The DECdta Architecture 
Having seen whe re t he need for DECdta compo­
nents arises, we are now ready to describe the 
DECdta architecture as a whole, including the func­
t ions of and interfaces to each component. 
Most DECdta inte rfaces are rmblic . S ome of the 
public inte rfaces are cont rolled by offic ial stan­
dards bodies and ind ust ry consortia; i .e., they are 
"open " inte rfaces. Others are cont rolled sole ly by 
D igital. DECdt a interfaces and protocols wil l  be 
published and aligned with indust ry standards, as 
appropriate. 
DECdta components are abst ract entities. They 
do not necessari ly map one-t o-one to hardware 
components, software c omponents (e.g ., p ro­
g rams or products), or exec ution environments 
(e.g ., a single-threaded process, a multithreaded 
process, or an ope rating system se rvice). Rathe r, a 
DECdt a component may be implemented as multi­
ple software components, for example, as seve ral 
1 2  
processes. Alte rnatively. several DECdt a compo­
nents may be implemen ted as a sing le software 
component. For example, an operating system or 
TP monit or ty pically offers the fac il ities of more 
than one DECdt a componen t. 
The following are the components of DEC:d ta: 
• An application prog ram is any prog ram that 
uses se rv ices of DECdta component s 
• A resource manager manages resources that sup­
port t ransact ion semantics. 
• A t ransaction manage r coordinates transac tion 
terminat ion (i.e , commi t  and abort). 
• A com munication manage r supports a t rans­
action communicat ion protoc ol between Tl' 
systems. 
• A presentation manager supports dev ice-inde­
pendent interact ions with a presentation device. 
• A request manager facilitates the subm ission of 
requests to exec ute t ransactions. 
DECdt a  components are layered on serv ices that 
are provided by the underlying operating system 
and dist ributed system platform, and arc not spec i­
fic to Tl', as shmvn in Figure 2. 
Application Program 
We usc the term application prog ram to mean a 
program that uses the services provided by other 
DECd ta c omponents. An application program 
could be a c ust omcr-wri ttcn prog ram, a laye red 
prod uct . or a DfUita component . 
In the DECdt a arch itecture, we disting uish two 
special types of application prog ram: request ini­
tiators and t ransact ion se rve rs. A request in it iator 
is a DECd ta component that prepares ami submits 
a request for the exec ut ion of a t ransact ion. Tb 
create a request, the request initiator usua II y inter­
acts with a pre sent ati on manage r that provides an 
interface to a device, such as a te rminal, a work­
station, a dig it al priv ate branch exchange, or an 
automated tel e r machine . 
A t ransaction server can demarc ate a t rans­
action, interact with one or more resource man­
agers t o  access recove rable resources on behalf of 
the t ransaction, invoke ot her t ransac tion servers, 
and respond t o  calls from request initiators. 
For a simple reque st, a t ransac tion server 
receives the request, processes it, and optionally 
returns a reply t o  the request initiator. A conve r­
sational request is like a simple request, except that 
while processing the request, t he transac tion 
\̯11. j .Vu. J 
Winter 1991 
Digital Tecbuica/ jourua/ 
DECdta - Digital's Distributed Transaction Processing Architecture 
APPLICATION PROGRAMS 
TP SERVICES 
R EQUEST 
IN ITIATOR 
REQU EST 
MANAGER 
PRESENTATION 
MANAGER 
REQU EST 
MANAGER 
OPERATING SYSTEM AND DISTRI BUTED SYSTEM SERVICES 
DISTRIBUTED 
NAME SERVICE 
DISTR I BUTED 
TIME SERVICE 
THREAD 
MANAG EMENT 
SERVICE 
TRANSACTION SERVER 
RESOU RCE 
MANAG E R  
OTH ER 
COMMUNICATION 
MANAGERS 
TRANSACTION 
MANAGER 
UID SERVICE 
AUTHENTICATION 
SERVICE 
Figure 2 
DECdta Components and Interfaces 
server exchanges one or more messages with the 
user, usually through the request initiator. 
In principle, a request ini tiator coulll also execute 
transactions (not shown in Figure 2). That is, the dis­
tinction between request initiators and transaction 
servers is for clarity onl y, and does not restrict an 
appli cation from perform ing request initiation func­
t ions i n  a transaction. Architectural ly, this amounts 
to saying that request initiation fu nctions can exe­
cute in a transaction server. 
Resource 1l1anager 
A resource manager performs operations on shared 
resources. We are especially i nterested in recover­
able resource managers, those that obey transaction 
semantics. In particular, a recoverable resource 
manager undoes a transaction's updates to the 
resources if the transaction aborts. Other recover­
able resource manager activities i n  support of trans­
actions are described in the next section. In the rest 
of this paper, we use "resource manager" to mean 
" recoverable resource manager." 
In a TP system, the most common kind of 
resource manager is a database system. Some pre­
sentation managers and communication managers 
may also be resource managers. A resource man-
Digita/ 1ec1Jitical jourtƓal 
1-'11/ . .> Nu. I 
\Vinter I'J'JI 
ager may be wri tten by a customer, a third party, 
or Digital. 
Each resource manage r type offers a resource­
manager-specific interface that is used by applica­
tion programs to access and modify recoverable 
resources managed by the resource manager. A des­
cription of these resource manager i nterfaces is 
outside the scope of DECdta. However, many of 
these resource manager interfaces have archi tec­
tures defined by industry standards, such as SQL 
(e .g., t he VAX Rdb/Vtv!S product), CODASYL data man­
ipulation language (e.g., the VAX DB,'v!S product), and 
COBOL fi le operations (e.g. , RNIS i n  the VMS system). 
One type of resource manager that plays a spe­
cial role in TP systems is a queue resource manager. 
It manages recoverable queues, which are often 
used to store requests. ' It allows appl ication pro­
grams to place elements into queues and retrieve 
them, so that appl ication programs can com muni­
cate even though they execute independently and 
asynchronou sly. For example, an appl ication pro­
gram that sends elements can communicate with 
one that receives elements even if the two applica­
t ion programs are not operationai simultaneously. 
This communication arrangement improves ava i l­
abil i ty and faci litates hatch input of elements. 
1 3  
Transact ion Processing, Databases, and Fault-tolerant Systems 
A queue resource manager interface supports 
such operations as open-queue, close-queue, 
enqueue, dequeue, and read-element. The ACMS 
and DECintact TP monitors both have queue 
resource managers as components. 
Transaction Manager 
A transaction manager supports the transaction 
abstraction. It is responsible for ensuring the atom­
icity of each transaction by telling each resource 
manager in a transaction when to commit. It uses 
a two-phase commit protocol to ensure that either 
all resource managers accessed by a transaction 
commit the transaction or they all abort the trans­
action. ' To support transaction atomicity, a trans­
action manager provides the fo l lowing functions: 
• 
Transaction demarcation operations allow appli­
cation programs or resource managers to start 
and commi t  or abort a transaction. (Resource 
managers sometimes start a transaction to exe­
cute a resource operation if the caller is not 
executing a transaction. The SQL standard 
requires this.) 
• 
Transaction 
execution 
operations 
al low 
resource managers and communication man­
agers to declare themselves part of an existing 
transaction. 
• 
Two-phase commit operations allow resource 
managers and communication managers to 
change a transaction's state (to "prepared," "com­
mitted," or "aborted "). 
The serial izabi l ity of transactions is primarily 
the responsibil ity of the resource managers. 
Usual ly, a resource manager ensures serializabi lity 
by setting locks on resources accessed by each 
transaction, and by releasing t he locks after the 
transact ion manager tells the resource manager 
to commit. (The latter activity makes serializabil­
i ty partly the responsibility of the transaction 
manager.) If transactions become dead locked, a 
resource manager may detect the dead lock and 
abort one of the dead locked transactions. 
The durability of transactions is a responsibi l ity 
of transaction managers and resource managers. 
The transaction manager is responsible for the 
durabi lity of the commit or abort decision. A 
resource manager is responsible for the durabi lity 
of operations of committed transactions. Usually, 
it ensures durabil it y  by storing a description of 
each transaction's resource operations and state 
changes in a stable (e.g., disk-resident) log. It can 
14 
later use the log to reconstruct transactions' states 
while recovering from a fai lure. 
A deta i led description of the DECdta transaction 
manager component appears in the Transact ion 
Manager Architecture section. 
Communication Manager 
A com munication manager provides services for 
communication between named obj ects i n  a TP 
system, such as application programs and trans­
action managers. Some communication managers 
participate in coordinating the termi nation of a 
transaction by p ropagating the transaction man­
ager's two-phase commi t  operations as messages 
to remote communication managers. Other com­
munication managers propagate application data 
and transaction context, such as a transaction iden­
tifier, from one node to another. Some do both. 
A TP system can support multiple communica­
tion managers. These communication managers 
can interact with other nodes using different com­
mit protocols or message-passi ng protocols, and 
may be part of different name spaces, security 
doma i ns, system management doma i ns, 
etc. 
Examples are an IBM SNA LU6.2 communication 
manager or an ISO-TP communication manager. 
By supporting multiple com munication man­
agers, the DECdta architecture enhances the inter­
operability ofTP systems. Different TP systems can 
interoperate by executing a transaction using d if­
ferent commit protocols. 
A communication manager offers an interface 
for application p rograms to communicate with 
other application programs. Different communica­
tion managers may offer different communication 
paradigms, such as remote procedure call or peer­
to-peer message passing. 
A communication manager also has an interface 
to i ts local transaction manager. It uses this i n ter­
face to tel l the transaction manager when a trans­
action has spread to a new node and to obtain 
i nformation about transaction commitment, which 
it exchanges with communication managers on 
remote nodes. 
Presentation Manager 
A p resentation manager provides an application 
program with a record-oriented interface to a pre­
sentation device. Its services are used by applica­
tion programs, usually request initiators. By using 
presentation manager services, i nstead of directly 
accessing a presentation device, application pro­
grams become device independent. 
Vol. 3 No. 1 
Winter 1991 
Digital Teclmicaljournal 
DECdta - Digital's Distributed Transaction Processing A rchitecture 
A forms manager is one type of presentation 
manager. Just as a database system supports opera­
tions to define, open, close, and access databases, a 
forms m anager supports operations to define, 
enable, disable, and access forms. A form includes 
the definition 
of the 
fields 
(with different 
attributes) that make up the form. It also i ncludes 
services to map the fields into device-independent 
application records, to perform data validation, 
and to perform data conversion to map fields onto 
device-specific frames. 
One presentation manager is Digital's DEC:forms 
forms management product. The DECforms prod­
uct is the first implementation of the ANSI/ISO 
Forms Interface Management Systems standard 
(COOASYL FIMS).' 
Request Manager 
A request manager provides services to authenti­
cate the source of requests (a user ami/or a presen­
tation device), to submit requests, and to receive 
replies from the execution of requests. It supports 
such operations as send-request and receive-reply. 
Send-request must provide the identity of the 
source device, the identity of the user who entered 
the request, the identity of the appl ication pro­
gram to be invoked, and the input data to the 
program. 
A request manager can ei ther pass the request 
directly to an application program, or it can store 
requests in a queue. In the latter case, anot her 
request manager can subsequently schedule the 
request by dequeuing the request ami invoking an 
application program. The ACMS System Interface is 
an example of an existing request manager inter­
face for direct requests. The ACMS Queued Trans­
action Initiator is an example of a request manager 
that schedules queued requests.' 
Transaction Manager Architecture 
OECdta components are tied together by the trans­
action abstraction. Transactions al low application 
programs, resource m anagers, request managers 
(indirectly through queue resource managers), and 
communication managers to intemperate reliably. 
Since transactions p lay an especially important 
ro le in the OECdta archi tecture, we describe the 
transaction management functions in more detail. 
The OECdta architecture incl udes interfaces 
between transaction managers and applicat ion 
programs, resource managers, and communication 
managers, as shown in Figure 3. It also includes a 
Digital Tedmical Jour11al 
1'<>1. .i 1\i>. I 
Winler I') VI 
APPLICATION 
PROGRAM 
OTH ER 
COMMUNICATION 
MANAGERS 
Figure 3 
Transaction Manager A rchitecture 
transaction manager protocol, whose messages are 
propagated by communication managers. This pro­
tocol is used by D igital's DEC:dtm distributed trans­
action manager.' 
From a transaction manager's viewpoint, a trans­
action consists of transaction demarcation opera­
tions, transaction execution operations, two-phase 
com m it operations, and recovery operations. 
• 
The transaction demarcation operat ions are 
issued by an application program to a transac­
tion manager and incl ude operat ions to start 
and either end or abort a transaction. 
• 
Transaction execurion operations are issued by 
resource managers ami communication man­
agers to a transaction manager. They include 
operat ions 
For a resource manager or communication 
manager to join an existing transaction 
-
For a commun icat ion manager to tell a trans­
action manager to start a new branch of a 
transaction that al ready exists at another node 
• 
Two-phase commit operations are issued by a 
transaction manager to resource managers, 
communication managers, and through com­
munication managers to other transaction man­
agers, and vice-versa. They i nclude operations 
-
For a transaction manager to ask a resource 
manager or communication manager to pre­
pare, commit, or abort a transaction 
For a resource manager or communica­
tion manager to tel l a transaction manager 
whether i t  has prepared, com m itted , o r  
aborted a transaction 
1 5  
Transaction Processing, Databases, and Fault-tolerant Systems 
-
For a com munication manager to ask a trans­
action manager to p repare, commit, or abort 
a transaction 
-
For a transaction manager to tel l  a commu­
nication manager whether it has prepared, 
committed, or aborted a transaction 
• 
Recovery operations are issued by a resource 
manager to its transaction manager to deter­
m ine the state of a transaction (i.e., comm itted 
or aborted). 
In response to a start operation i nvoked by an 
application program, the transaction manager d is­
penses a unique transaction identifier for the trans­
action. The transaction manager that processes the 
start operation is that transact ion's home trans­
action manager. 
When an application program invokes an opera­
tion 
supported by a 
resource manager, 
the 
resource manager must find out the transaction 
identifier of the application program's transaction. 
This can happen in d ifferent ways. For example, the 
application program may tag the operation with 
the transaction identifier, or the resource manager 
may look up the transact ion identifier in the appli­
cation program's context. When a resource man­
ager receives its first operation on behalf of a 
transaction, T, i t  must join T, meaning that it must 
tell a transaction manager that i t  is a subordinate 
for T. AJ ternatively, the DECdta architecture sup­
ports a model in which a resource manager may ask 
to be joined automatically to all transactions man­
aged by its transaction manager, rather than asking 
to join each transaction separately. 
A transaction, T, spreads from one node, Node 1, 
to another node, Node 2, by sendi ng a message 
(through a commun ication manager) from an appli­
cation p rogram that is executing T at Node 1 to 
an application program at Node 2. When T sends 
a message fro m  Node 1 to Node 2 for the first 
time, the communication managers at Node 1 and 
Node 2 m ust perfor m  branch registration. This 
function may be performed automatically by the 
communication managers. Or, it may be done man­
ually by the application program ,  which tells t he 
communication managers at Node 1 and Node 2 
that the transaction has spread to Node 2. In either 
case, the result is as fol lows: the com munication 
manager at Node 1 becomes the subordinate of the 
t ransaction manager at Node 1 for T  and the supe­
rior of the communication manager at Node 2 
for T; and the com munication manager at Node 2 
becomes the superior of the transaction manager 
1 6  
at Node 2 for T. This arrangement allows the com­
mit protocol between transact ion managers to be 
propagated properly by communication managers. 
After the transaction is done with its application 
work, the application program that started transac­
tion T may invoke an "end" operation at the home 
transaction manager to commit T. This causes the 
home transact ion manager to ask its subordinate 
resource managers and com munication managers 
to try to commit T. The transaction manager does 
this by using a two-phase commit p rotocol. The 
protocol ensures that either all subord inate 
resource managers commit the transaction or they 
all abort the transaction. 
In phase 1 ,  the home transaction manager asks 
its subordinates for T to prepare T. A subordinate 
p repares T by doing what is necessary to guarantee 
that it can either commit T or abort T if asked to do 
so by its superior; this guarantee is valid even if 
i t  fa ils immediately after becom i ng p repared. To 
prepare T, 
• 
Each subordinate for T recmsively propagates 
the prepare request to i ts subordinates for T  
• 
Each resource manager subordi nate writes all of 
T's updates to stable storage 
• 
Each resource manager and transaction manager 
subord inate writes a prepare-record to stable 
storage 
A subordinate for T  repl ies with a "yes" vote if 
and when i t  bas completed its stable writes and all 
of its subordinates for T have voted " yes" ;  other­
wise, it votes "no.'' lf any subordinate for T  does not 
acknowledge the request to prepare within the 
timeout period, then the home transaction man­
ager aborts T; the effect is the same as issuing an 
abort operation. 
In phase 2, when the home transaction manager 
has received "yes" votes from all of its subordinates 
for T, i t  decides to comm i t  T. It writes a commit 
record for T to stable storage and tells its subordi­
nates for T to commit T. Each subordinate for T 
writes a commit record for T to stable storage and 
recursively p ropagates the commit request to i ts 
subord in2.tes for T. A subordinate for T  rep I ies with 
an acknowledgment if and when it has committed 
the transaction (in the case of a resource manager 
subord inate) and has received acknowledgments 
from all subordinates for T. When the home trans­
action manager receives acknowledgments from all 
of its subordi nates for T, the transaction commit­
ment is complete. 
v'!JI. j No. J 
Winter I':J'JJ 
Digital Technical journal 
DECdta - Digital's Distributed Transaction Processing Architecture 
To recove r from a failu re, all res ource manage rs 
that part icipated in a transaction must examine 
their logs on s table s torage to determine what to 
do. If the log contains a commit or abort record for 
T, then T completed. No action is required. If the 
log conta ins no prepare ,  com mit, or abort record 
for T, then T was active. T mus t  be aborted. If the 
log contains a prepare record for T, bur no com­
mit or abort record for T, T w as between p hases I 
and 2. The res ou rce manage r mus t ask its superior 
transaction manager whether to commit or abort 
the trans action. 
An i nhcrenr p roblem in aU two-phase commit 
protocols is that a resource manager is blocked 
between phases I and 2. that is, after voting "yes " 
and before receivi ng the commit or abort decision. 
It cannot commit or abort t he transaction u nt i l  the 
transaction manager tel ls it which to do. If i ts trans­
action manager fa i ls, the res ource manager may be 
blocked indef initely, until e ither the transaction 
manager recovers or an ex te rnal agent, such as a 
system manage r, s teps i n  to tel l  the resource man­
ager w he ther to commit or abort. 
A transaction T may s pontaneousl y abort due to 
syste m  e rrors at any rime during i rs execu tion. Or, 
an appl ication prog ram (p rior to comp leti ng its 
work) or a resource manage r (p rior to voting "yes") 
may tell its trans action manager to abort T. In 
e i ther case ,  the t ransaction manager t hen tel ls 
all of i ts subord inates for T to undo the effects 
of T's res ource manager operations . S ubord inate 
resource manage rs abort T, and su bord i nate com­
mun ication managers recursivel y prop agate the 
abort request to their subord inates for T. 
The two-phase commit proto col is optimized for 
those cases in w hich the nu mber of messages 
exchanged can be reduced below that of the gen­
eral cas e (e.g. , if the re is onl y  one su bord i nate 
res ource manage r. if a resource manager d id not 
mod ify resources, or if the presu med-abort proto­
col was used to save acknowledgments)." 
Summary 
We have presented an overview of the DECdta 
architecture. As part of this overview, we intro­
duced the components and expla ined t he fu nction 
of each i ntcrface . We als o described tile DECdta 
trans action management an:hirecrure in some 
dera i l. Over time, many i nte rfaces of the DECd ta 
model will be made pu blic via product of fering s or 
architecture pu b! ications .  
Digital Teclmical jounwl 
l'ol . .  > 
.\'u. I 
Winter I')<) I 
Acknowledgments 
T his architecture g rew from discu ssions with many 
col le agues. We thank them all for their help, espe­
cially D ieter Gawl ick, Bill La ing ,  Dave Lomet, Bruce 
Mann, B arry Rubinson, D iogenes Torres, and the TP 
architecture g roup , i nclud ing Edward Bragi nsky, 
Tony Del laFe ra, George Gajnak, Per Gyl lstrom, and 
Yoav Raz. 
References 
1 .  T. Speer and M .  Storm, " D igital's Transaction 
Processing Monitors," Digital Technical journal, 
vol. 3. no. I (Winte r 1991 , this issue): 18-32. 
2. W L1 ing, J. johnson, and R. Landau, "Transaction 
Management Support in the VMS Operati ng 
System Kernel," Digital Technical journal, vol. 3, 
no. 1 (Winter 1991 , this issue): :B-44. 
3. P Bernstein, V Hadzi lacos, and N. Goodman, 
Concurrency Control and Recouery in Database 
Systems (Read ing, MA: Add ison-Wes ley, 1987). 
4. P Bernstein, M. Hsu ,  and B. Mann, "Implement­
i ng Recoverable Reques ts Us ing 
Q ueues," 
Proceedings 1 990 ACM StG/viOD Conference on 
Management of Data (May 1990). 
5. FIMS journal of Developrnent (Norfo l k, VA: 
CODASYL FIMS Committee, Ju ly 1990). 
6. C. Mohan, B. Lindsay, and R. O bermarck, 
"Transaction Management in the R* D istribu ted 
Database M anagement System," 
ACM Trans­
actions on Database .Xvstems, 
vo l. 1 1 ,  no. 4 
(December 1986) 
1.7 
Digitals Transaction 
Processing Monitors 
Thomas G. Speer 
Mark W. Storm 
Digital provides two transaction processing (TP) monitor products - ACi\115 
(Application Control and Management System) and DECintact (Integrated Appli­
cation Control). Each monitor is a unified set of transaction processing services for 
the application environment. These services are layered on the Vi\:15 operating .\)'S­
tem. Although there is a large junctional overlap between the two, both products 
achieve similar goals by means of some significanty different implementation 
strategies. Flow control and multithreading in the ACM5 monitor is managed by 
means of a fourth-generation language (4GL) task definition language. Flow control 
and multithreading in the DECintact monitor is managed at the application level 
by third-generation language ()GL) calls to a library of services. The ACM5 monitor 
supports a deferred task model of queuing, and the DECintact monitor supports a 
message-based model. Over time, the persistent distinguishing feature between the 
two monitors will be their differeYJt application programming interfaces. 
Transaction processing is the execution of an 
application that performs an administrative func­
t ion by accessi ng a shared database. Within trans­
action processing, processing monitors provide 
the software "glue" that ties together many soft­
ware components into a transaction p rocessing 
system solution. 
A typical transaction process ing application 
involves interaction with many terminal users by 
means of a presentation manager or forms system 
to collect user requests. Information gathered by 
the presentation manager is then used to query or 
update one or more databases that reflect the cur­
rent state of the business. A characteristic of trans­
action processing systems and applications is 
many users performing a small number of similar 
functions agai nst a common database. A t rans­
action processing monitor is a system environment 
that supports the efficient development, execu­
tion, and management of such applications. 
Processing monitors are usually built on top of 
or as extensions to the operating system and other 
products such as database systems and presenta­
tion services. By so doing, addi tional components 
can be integrated into a system and can fil l  " holes" 
by providing functions that are specifically needed 
by transaction processing appl ications. Some 
examples of these functions are appl ication con­
trol 
and 
management, 
transaction-processing-
1 8  
specific execution environments, and transaction­
processing-specific programming interfaces. 
D igital provides two t ransaction processing 
monitors: the Appl ication Control and Manage­
ment System (ACMS) and the DECintact monitor. 
Both monitors are built on top of the VMS operat­
ing system .  Each mon i tor provides a unified set 
of transaction-processing-specific services to the 
application environment, and a large functional 
overlap exists between the services each monitor 
provides. The d istinguishing factor between the 
two monitors is in t he area of appl ication p rogram­
m ing styles and interfaces - fourth-generation 
language (4GL) versus third-generation language 
(3GL). This distinction represents D igital's recog­
n ition that customers have their own styles of 
application programming. Those that prefer 4GL 
styles should be able to build transaction process­
ing applications using D igital's TP monitors with­
out changing t heir style. Similarly, those t hat prefer 
3GL styles should also be able to bu ild TP applica­
tions using D igital's TP monitors without changing 
their style. 
The ACMS monitor was first introduced by D igital 
i n  1984. The ACMS monitor addresses the require­
ments of large, complex transaction processing 
applications by making them easier to develop and 
manage. The ACMS monitor also creates an efficient 
execution environment for these applications. 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
The DECintact monitor (Integrated Appl ication 
Control) was origi nal ly developed by a third-party 
vendor. Purchased and introduced by D igital i n  
1988, i t  has been instal led i n  major financial i nsti­
tut ions and manufacturi ng sites. The DECintact 
mon i to r  i ncl udes its own presentation manager, 
support for DECforms, a recoverable queu ing sub­
system. a transaction manager, and a resource man­
ager that provides its own recovery of RJV!S (Record 
Management Services) fi lcs. 
This paper highl ights the important simi lari t ies 
and differences of the r\GvJS and DEC:intact monitors 
in terms of goals and implementation strategies. 
Development Environment 
Transaction processing moni tors provide a view 
of the transaction processi ng system for appli­
cation development. 'fherefore, the ACMS and 
DEC:i ntact monitors must embody a style of pro­
gram development. 
ACMS Programming Style 
A "divide and conquer " approach was used i n  the 
ACMS monito r. The work typicall y  i nvolved in 
developing a T P  appl ication was divided i nto logi­
cally separate functions described below. Each of 
these functions was then "conquered" by a special 
util ity or approach. 
Tn the ACJ';JS moni tor, an "appl icat ion" is defined 
as a col lect ion of selectable units of work cal led 
tasks. A separate appl ication defi n i t ion faci l ity 
iso lates the system management characteristics of 
the appl ication (such as resource a l location, fi le 
location, and protection) from the logic of the 
appl ication. 
The specification of menus is also clecoupled 
from the application. A nonprocedural (4GL) 
method of defining menu layouts is used in which 
the layouts are compiled i nto form files and data 
structures to be used at run-time. Each menu entry 
points either to another menu or to an appl ication 
and a task. (Decoupl ing menus from t he appl ica­
t ion al lows user mem1s to be independent of how 
the tasks are grouped i nto applications.) 
In addi t ion to separate menu specification and 
system management characterist ics, the applica­
tion logic is broken down i nto the three logical 
parts of interact ive Tl' applications: 
• 
Exchange steps support the exchange of data 
with the end user. This exchange is typical ly 
accomplished by displaying a form on a terminal 
screen and col lecting the input. 
Digita1 1ec1JIIical jour11al 
V"l .
. i .Vu. I 
Winter I')') I 
Digital's Transaction Processing Monitors 
• 
!'>rocessing steps perform computational pro­
cessing and database or fi le l/0 through standard 
subroutines. The subroutines are written i n  
any language that accepts records passed by 
reference. 
• 
The task definition language defines the flow of 
control berween processi ng steps and exchange 
steps and specifies transaction demarcation. 
Work spaces arc special records that the ACMS 
monitor provides to pass data between the task 
definition, exchange steps, and processing steps. 
A compi ler, cal led the appl ication definition util-
i ty (ADU). is implemented in the ACMS monitor to 
compile the task defi nition language into binary 
data structures. The run-time system is table-driven, 
rather than interpreted, by these structures. 
Digital is the only vendor that suppl ies this "d ivide 
and conquer" solution to bu ilding large complex TP 
applications. We bel ieve this approach - unique in 
the industry - reduces complexity, 
thus maki ng 
applications easier to produce and to manage. 
DECintact Programming Style 
The approach to application development used in 
the DEC:intact monitor provides the appl ication 
developer with 3GL control over the transaction 
processing services required . This approach 
al lows appl ication prototyping and development 
to be done rapid ly. Moreover, the appl ication can 
make t he most efficient use of monitor services 
by selecting and contro l l i ng only those services 
required for a particular task. 
In the D ECi ntact monitor. an application is 
defined as one or more programs wri tten entirely 
in 3GL and supported by the VMS system. The code 
written by the appl ication developer manages all 
flow control, user interaction, and data manipu­
lation through the utilities and service l ibraries 
provided by the DECintact monitor. Al l DECintact 
serv ices are callable, i ncluding most services pro­
vided by the DECintact uti I ities. The DECintact 
services are as fol lows: 
• 
A library of presentation services used for all 
interaction with users. The appl ication developer 
includes calls to these services for form manip­
u lation and display. Forms are created with a 
forms editor util ity and can be updated dynami­
cally. Forms are displayed by the D ECintact 
terminal manager in emu lated block mode. 
Device- and termi nal-dependent information is 
completely separated from the implementation 
of the application. 
1 9  
Transaction Processing, Databases, and Fault-tolerant Systems 
• 
The separation of specification of menus from 
the application. DECintact menus are defined by 
means of a menu database and are compiled into 
data structures accessed at run-t ime. The menus 
are tree-structured. Each entry poi nts either to 
another menu entry or to an executable applica­
tion image. The specification of mem1s is li nked 
to the DECintact monitor's security subsystem. 
The DEC:intact terminal user sees only those 
specific menu entries for which the user has 
been granted access. 
• 
A library of services for the control of fi le and 
queue operations. In addition to layered access 
to the RMS fi le system ,  the DEC:intact monitor 
supports its own hash fi le format (a functional 
analog to single-keyed indexed files in RMS) 
which provides very fast, efficient record 
ret rieval. The application developer i ncl udes 
calls to these services for managing fu\1S and 
hash fi le 1/0 operations, demarcating recovery 
unit boundaries, creating queues, placing data 
items on queues, and removing data items from 
queues. The queuing subsystem is typically an 
integral part of appl ication design and work 
flow control. Application-defined D EC:intact 
recovery units ensure that fu\1S, hash, and queue 
operations can be comm itted or aborted ato m i­
cally; that is, either al l permanent effects of the 
recovery unit happen, or none happen. 
Because of D ECintact's 3GL development envi-
ronment, application program mers who are acctis­
tomed to calling procedure l ibraries from standard 
VMS languages o r  who are fam i l iar with other 
transaction processing monitors can easily learn 
DEC:intact's services. Appl ication prototypes can 
be produced quickly because only skills in 3CȩL 
are requ ired . Further, completed app l icat ions 
can be p roduced qu ickl y  because tra in ing time 
is m inimal. 
On-line Execution Environment 
Transaction processing monitors provide an execu­
tion environment tailored to the characteristics and 
needs of transaction processing applications. This 
environment generally has two aspects: on-line, for 
interactive applications that use terminals; and off­
line, for noninteractive applications that use other 
devices. 
Traditional VMS timesharing appl ications are 
implemented by allocating one VMS process to each 
terminal user when the user logs in to the system. 
An image activat ion is then done each time the ter-
20 
minal user invokes a new function. This method is 
most beneficial in simple transaction process ing 
appl ications that have a relat ively small number of 
users. However, as the number of users grows or as 
the application becomes larger ancl more complex, 
several p roblem areas may arise with this method: 
• 
Resource use. As the number of processes grows, 
more and more m emory is needed to run the 
system effectively. 
• 
Start-up costs. Process creation, i mage activa­
tion, file opens, and database bi nds are expen­
sive operations in terms of system resources 
util ized and time elapsed. These operations can 
degrade system performance if clone frequently. 
• 
Contention. As the number o f  users simul­
taneously accessing a database or fi le grows, 
contention for locks also increases. For many 
applications, lock contention is a significant 
factor in throughput. 
• 
Processing location. Single process implementa­
tions Jim it distribution options. 
ACMS On-line Execution 
To address the problems l isted above, Digital imple­
mented a client/server architecture in the ACMS 
monitor. (Cl ient/server is also cal led request/ 
response.) The basic run-time architecture consists 
of three types of p rocesses, as shown in Figure 1 :  
the com mand p rocess, execution control ler, ancl 
procedure servers. 
An agent in the ACMS monitor is a process that 
submits work requests to an application. In the 
ACMS system, the command p rocess is a special 
agent responsible for interactions with the termi­
nal user. (In terms of the DECdta architecture, the 
command p rocess i mp lements the functions of 
a request initiator, p resentation manager, and 
request manager for direct requests.)ц The com­
mand process is general ly created at system start­
up time, altho ugh ACMS commands al low it to 
be started at other t imes. The p rocess is m u lt i­
threaded through the use of VMS asynchronous 
system t raps (AS1'). Thus, one command process 
per node is generall y  sufficient for all terminals 
handled by that node. 
There are two subcomponents of the ACMS moni­
tor within the command p rocess: 
• 
System interface, which is a set of services for 
submitting work requests and for interacting 
with the ACMS application 
Vol. 3 No. 1 
Winter 1991 
Digital Tee/mica/ jour11al 
g 
g 
g 
l__ 
r 
MENU 
DATABASE 
+ 
COMMAND 
SYSTEM 
PROCESS 
INTERFACE 
DEC FORMS 
SERVER 
I 
I 
I 
I 
I 
I 
I 
I 
Digital's Transaction Processing Monitors 
IBACŻEND NODE - - - - ,  
I 
I 
I 
I 
I 
• 
I 
TASK 
DEFINITION 
, 
EXECUTION 
CONTROLLER 
I 
I 
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
 I 
KEY: 
ACMS 
PROCESSES 
APPLICATION 
PROCESSES 
PROCEDURE 
SERVERS 
USER DATABASES 
0
-
-
-
-
-
-
-
-
-
- _j 
Figure I 
Basic Run-time Architecture of the ACMS Monitor 
• 
DECforms, Digital's forms management product, 
which implements the A NSI/ISO Forms Inter­
face Management System (FIMS) that p rovides 
the presentat ion server for executing the 
exchange steps 
The command process reads the menu defini­
t ion for a particular terminal user and determines 
which menu to d isplay. When the terminal user 
selects a particular menu entry, the command pro­
cess calls the ACMS system interface services to 
submit the task. The system interface uses logical 
names from the VMS system to translate the appli­
cation name into the address of the execution con­
troller that represents that application. The system 
interface then sends a message to the execution 
control ler. The message conta ins the locations of 
the presentation server and an index into the task 
definition tables for the particular task. The status 
of the task is returned in the response. Duri ng the 
course of task execut ion, the command p rocess 
accepts callbacks from the task to d isplay a form 
for interaction with the term inal user. 
The execution controlle r  executes the task 
definition language and creates and manages p ro­
cedure servers. The control ler is created at appli­
cation start-up time and is multithreaded by 
using VMS ASTs. There is one execution controller 
per application. (In terms of the D ECdta archi­
tecture, the execution control ler and the proce-
Digital TeciJnical jounwl 
Vul . .> Nu. I 
Winter I'J91 
dure servers i mplement the functions of a t rans­
action server.)' 
When the execution controller receives a request 
from the command process, i t  invokes DECdtm 
(Digital D istributed Transaction Manager) services 
to join the transaction if the agent passes the 
t ransaction identifier. If the agent does not pass a 
t ransaction identifier, there is no t ransaction to 
join and a DECdtm or resource-manager-specific 
transaction is started as specified in the task defini­
tion. The execut ion controller then uses the task 
index to find the tables that represent the task. 
When the execution of a task reaches an exchange 
step, the execution control ler sends a cal lback to 
the command process for a form to be displayed 
and the input to be collected for the task. When 
the request to d isplay a form is sent to the com­
m and p rocess, the execution controller d ism isses 
the AST to enable other threads to execute. When 
the response to the request arrives from the 
exchange step, an AST is added to the queue for 
the execution controller. 
When a task comes to a processing step, the exe­
cution controlle r  allocates a free procedure server 
to the task. It then sends a request to the proce­
dure server to execute the particular p rocedure 
and dism isses the AST. If no procedure server is 
free, the execution controller puts the request 
on a wa iting l ist and dismisses the AST. When a 
2 1  
Transact ion Processing, Databases, and Fault-tolerant Systems 
procedure server becomes free, the execution con­
troller checks the wa it list and allocates the proce­
dure server to the next task, if any, on the wa it l ist. 
Procedure servers are created and deleted by 
the execution controller. Procedure servers are a 
col lection of user-written procedures that perform 
computation and provide database or fi le accesses 
for the appl ication. The procedures are written in 
standard languages and use no special services. The 
ACMS system creates a transfer vector from the 
server definition. This transfer vecror is l inked into 
the server image. With this vector, the ACMS system 
code can receive incoming messages and translate 
them into calls to the procedure. 
A procedure server is specified with initialization 
and termi nation procedures, which are routines 
supplied by the user. The ACMS monitor cal ls these 
procedures whenever a procedure server is created 
and deleted. The initial ization procedure opens 
files and performs database bind operations. The 
termination p rocedure does clean-up work, such 
as clos ing fi les prior to process exit. 
The ACMS architecture addresses the problem 
areas d iscussed in the On-l ine Execution Environ­
ment section in several ways. 
Resource Use 
Because procedure se. vers are al lo­
cated on l y  for the time required to execute a pro­
cessing step, the servers are ava ilable for other 
use whi l e  a terminal user types in data for the 
form. Thus, the system can execute efficiently with 
fewer procedure servers than active terminal 
users. Improvement ga ins in resource use can vary, 
depending on the application. Our debit and cred it 
benchmark experiments with the ACMS monitor 
and the Rdb/VMS relational database system ind i­
cated that the most improvement occurs with one 
p rocedure server for every one or two transactions 
per second (TPS). These benchmarks equate to 
I p rocedure serve r  for every lO to 20 active termi­
nal users. 
The use of p rocedure servers and the mu l ti­
threaded character of the execution controller and 
the command process a llow the architecture to 
reduce the number of processes and, therefore, the 
number of resources needed . The optimal solution 
for resource use wou ld consist of one large mu lti­
threaded process that performed all processing. 
However, we chose to trade off some resource use 
in the architecture in favor of other gains. 
• 
Ease of use - Multithreaded applications are 
generally more difficult to code than single-
22 
threaded applications. For this reason, p roce­
d ure server subroutines in the ACMS system 
can be written in a standard fashion by using 
standard calls to Rdb/VMS and the VMS system. 
• 
Error isolation - In one large multi threaded 
p rocess, the threads are not comp letely pro­
tected within the process. An aprl ication logic 
error i n  one thread can corrupt data in a thread 
that is executing for a different user. A severe 
error in one thread could potentially bring 
clown the entire application. The multi threaded 
processes in the ACMS archi tecture (i.e., the 
execution control ler and command p rocess) 
are provided by D igital. Because no applica­
tion code executes directly in these p rocesses, 
we can guarantee that no appl ication coding 
error can affect them. Procedure servers are 
single- threaded . Therefore, an application logic 
error in a procedur e  server is isolated to affect 
only the task that is executi ng i n  the p roce­
dure server. 
Start-up Costs 
The run-time environment is basi­
cally "static," which means that the start-up costs 
(i.e., system resources and elapsed time) are 
incurred i nfrequently (i.e., at system and appli­
cation start-up time). A timesharing user who is 
running many different applications causes image 
activations and rundowns by swi tching among 
images. Because the terminal user in the ACMS 
system is separated from the applications pro­
cesses, the p rocess of swi tching applications 
involves only changing message destinations and 
incurs m inimal overhead . 
Contention 
The database accesses in the ACMS 
environment are channeled through a relatively 
few, but heavily used, number of p rocesses. The 
typical VMS timesharing environment uses a large 
number of lightly used p rocesses. By reducing 
the number of processes that access the database, 
the contention for locks is reduced. 
Processing Location 
Because the ACMS monitor 
is a multiprocess architecture, the command pro­
cess and forms processing can be clone close to the 
terminal user on smal l, inexpensive machines. This 
method takes advantage of the inexpensive pro­
cessing power ava i lable on these smaller machines 
while the rest of the appl ication execu tes on a 
larger VA-'<cluster system. 
VI>!. .i No. I 
Winter !')')! 
Digital Technical journal 
DECintact On-line Execution 
Although the specific components of the DECintact 
monitor vary from those of the ACMS monitor, the 
basic architecture is very similar. Figure 2 shows the 
appl ication configured locally to the front end. The 
run-time architecture consists of three types of 
DECintact system processes - terminal manager/ 
dispatcher, DECforms servers, server m anager -
and, typically, one or more application processes. 
When forms processing is d istributed , the same 
application is configured as shown in Figure 3. 
The D ECintact monitor can run i n  m ultiple 
copies on any one VA)( node. Each copy can be an 
independent run-time environment; or it can share 
data and resources, such as user security profiles 
and menu definitions, with other copies on the 
same system. Thus, i ndependent development, 
testi ng, and production e nvironments can reside 
on the same node. 
In the DECintact system, the terminal manager/ 
d ispatcher process (one per copy) is responsible 
for the fol lowing: 
• 
Displaying DECintact forms 
• 
Coordinating DECforms forms display 
• 
Interact ing with local applications 
• 
Communicating, through DECnet, with remote 
DECintact copies 
• 
Maintaining security authorization, i ncludi ng 
the dynamic generation of user-specific menus 
KEY 
D 
D 
TERMINAL MANAGER/ 
DISPATCHER 
DECINTACT 
PROCESSES 
APPLICATION 
PROCESSES 
Digital's Transaction Processing Monitors 
Applications designated i n  the local menu data­
base as remote applications cause the front-end 
terminal manager/dispatcher process to communi­
cate with the cooperating back-end terminal 
manager/dispatcher process through a task-to-task 
DECnet l ink. (In terms of the DECdta architecture, 
the terminal m anage r/dispatcher implements the 
functions of presentation manager, request initia­
tor, and request manager for direct requests.)' 
When a user selects the remote task, that user's 
request is sent to the back end and is treated by the 
application as a local request. The terminal man­
ager/dispatcher process is started automatically as 
part of a copy start-up and is multithreaded. 
Therefore, one such process can hand le all the ter­
minal users for a particular DECintact copy. 
When the termi nal user selects a menu task, one 
of the following actions occurs, depending on 
whether the task is local or remote and whether it 
is single- or multithreaded. 
If the application is local and single-threaded, a 
VMS p rocess may be created that activates the 
application i mage associated with this task. The 
terminal manager/d ispatcher, upon start up, may 
create a user-specified number of application shell 
VMS p rocesses to activate subsequent applicat ion 
images. If such a shell exists when the user selects 
a task, this p rocess is used to run the app l ication 
i mage. Each user who selects a given menu entry 
receives an individual VMS p rocess and i mage. 
If the app lication is local and multithreaded, the 
terminal manager/dispatcher first determines 
MULTITHREADED 
APPLICATION 
DATABASE 
SERVERS 
USER DATABASES 
Figure 2 
Basic Run-time Architecture of the DEC intact Monitor 
Digital Technical journal 
Vol. j .Vo. I 
Winter 1991 
23 
Transaction Processing, Databases, and Fault-tolerant Systems 
- - - - - - - - - - - - - - - - - ±  
FRONT-END NODE 
<=>?@AB - - - - - - - - - - - ,  
I 
I 
I 
I 
I 
I 
TERMINAL MANAGER/ 1--.--t-+1 
DISPATCHER 
TERMINAL MANAGER/ 
DISPATCHER 
'--- - - - - - - - - - - - - - - - -
_I 
KEY 
D 
D 
DECINTACT 
PROCESSES 
APPLICATION 
PROCESSES 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
MULTITHREADED 
APPLICATION 
I 
I 
: 
USER DATABASES 
I 
_ _ _ _ _ _
_
_
_
_
_
_
_
_
_
_
_
_
 j 
Figure 3 
DECintact Basic Architecture with Distributed Forms Processing 
whether this task has al ready been activated by pre­
vious users. If the task has not been activated and 
a shell is not avai I able, the terminal manager/ 
dispatcher creates a VMS process for the appl ica­
tion and act ivates the image. If the task is al ready 
activated, the term inal manager/dispatcher con­
nects the user to the active task. The user becomes 
another thread of execution within the image. 
Multithreaded appl ications handle many simulta­
neous users within the context of one VMS p rocess 
and image. 
Remote applications, whether si ngle- or multi­
threaded, route the menu task selection to a remote 
terminal manager/dispatcher process. On receipt 
of the request, the remote terminal manager/ 
dispatcher processes the selection locally by using 
the same procedures as described above. 
Local DECintact forms interaction is hand led i n  
the following manner b y  the local terminal man­
ager/dispatcher. The application's cal l to display a 
for m  sends a request to the terminal manager. The 
terminal manager locates the form in its database 
of active forms, displays the form on the user's ter­
m inal, and returns control to the application when 
24 
the user has entered all data in the form. If the 
appl ication is remote, form information is sent 
between cooperating local and remote term inal 
manager processes; the interface is transparent to 
the application. 
In add ition to supporting DECintact forms, the 
DECintact monitor also supports applications that 
u s e  DECforms as their presentation service. The 
implementation of this support fol lows the same 
client/se rver model used by the ACMS system's 
support for DECforms and shares much of the 
underlying run-time interprocess communication 
code used by the ACMS monitor. Functional ly, the 
two implementations of DECforms support are also 
simila r  to the ACMS monitor. Both implemen­
tations offer t ransparent support for d istributed 
DECforms processi ng, automatic forms caching 
(i.e., p ropagation of updated DECforms in a distrib­
u ted environment), and DECforms session cachi ng 
for increased performance. 
The DECintact monitor supports application­
level, single- and multithreaded environments. The 
DECintact monitor's threading package allows appli­
cation programmers to use standard languages 
Vol. .) No. I 
Wi11ter 1991 
Digital Technical journal 
supported by the VMS system to write multi­
threaded r rocesses. App lications declare them­
selves as either single- or multithreac.leu . With t he 
exception of the declaration, there is l ittle differ­
ence between the way an on- line multithreaded 
application and its single-threaded counterpart 
must be coded . For on-l ine appl icat ions, thread 
creation, deletion, and management are automatic. 
New threads are created when a term inal user 
selects the multithreaded application and are 
deleted when the user leaves the appl ication. 
In a si ngle-threaded application, the fol lowing 
occurs: 
• 
Each user receives an individual VMS process and 
image context (e.g., 200 users, 200 processes). 
• 
Al l terminal and fi le l/0 is synchronous. 
• 
The application image normally ex its when the 
application work is completed. 
In a multithreaded on-line application, the fol­
lowing occurs: 
• 
One VMS process/image can hand le many simul­
taneous users. 
• 
All terminal and file 1/0 is asynchronous. 
• 
New threads are created automatically when 
new users are connected to the p rocess. 
• 
The appl ication image does not exit when all 
currently al located threads have comrleted exe­
cution but remains for use by new on-line users. 
For each thread in a multithreaded application 
image, the DECintact system ma inta ins thread con­
text and state information. Each l/0 request is 
issued asynchronously. Immed iately after control 
is returnec.l, but before the l/0 request completes, 
the DECintact system saves the currently execut ing 
thread's context and schedules another thread to 
execute. When the thread 's 1/0 completion AST is 
del ivered, the thread's context is restored, and the 
thread is inserted on an internal ly ma inta ined list 
of threads eligible for execution. 
A thread's context consists of the fol lowing: 
• 
An internally maintained thread block conta in­
ing state information 
• The stack 
• 
Standard DECintact work spaces that are allo­
cated to each thread and that ma intai n  terminal 
and file management context 
Digital Technical journal 
Vol. J No. I 
Winter I'J'JI 
Digital's Transaction Processing Monitors 
• 
Local storage (e.g., the $LOCAL PSECT in COBOL 
applications) that the appl ication has designated 
as thread-specific 
The PSECT nam ing convention allows the 
appl ication to decide which variable storage is 
thread-specific and which 
is process-global. 
Thread-specific storage is u nava i I able to other 
threads in the same process because i t  is saved 
and restored on each thread switch. Process-global 
storage is always ava i lable to all t hreads in the 
p rocess and can be used when interthread commu­
nication or synchronization is desired. 
The use of multithread ing in the DECintact sys­
tem is appropriate for higher volume multiuser 
appl ications that perform frequent 1/0. Such appli­
cation usage is typical in transaction p rocessing 
environments. Because threac.J switches occur on ly 
when l/0 is requested or when locking requests 
are issued, this environment may not be recom­
mended for appl ications that perform i nfrequent 
1/0 or that expect very smal l numbers of concur­
rent users, such as end-of-day accounting pro­
grams or other batch-oriented processi ng. These 
kinds of applications typical ly choose to declare 
themselves as single-threac.Jed . 
Al l  1/0 from within a multithreaded DECintact 
application process is asynchronous. Therefore, 
the DECintact system provides a cl ient/server i nter­
face between multithreaded applications and syn­
chronous database systems, such as VAX DBMS 
(Database Management System) and Rdb/VMS sys­
tems. The interface is provided because calling a 
synchronous database operation directly fro m  
within a multithreaded application would stall the 
cal ling thread and all other threads until the call 
completed. Figure 2 shows that a typical on-line 
DECintact application accessing Rdb/VMS, for 
example, is written i n  two pieces: 
• 
A multithreaded, on-line piece (the cl ient), that 
hand les forms requests from multiple users 
• 
A single-threaded, database server piece (a server 
instance), that performs the actual synchronous 
database 1/0 
This cl ient/server approach to database access is 
functionally very similar to that of ACMS procedure 
servers and offers similar benefits. Like the ACMS 
monitor, the DECintact monitor offers system man­
agement faci l ities to define pools of servers and to 
adjust them dynamically at run-time in accordance 
with load. Similar algorithms are used in both mon­
itors to allocate server instances to client threads 
25 
Transaction Processing, Databases, and Fault-tolerant Systems 
ami to start up new instances, as necessary. The 
DECintact server code, like the ACMS procedure 
server code, can define initia lization and termina­
tion procedures to perform once-only start-up and 
shut-down processing. With DECintact transaction 
semantics, which are layered on D ECdtm services, 
a cl ient can declare a global transaction that the 
server instance wil l  join. The server instance can 
also declare its own independent transaction or no 
t ransaction. (In terms of the DECdta architecture, 
this client/server approach implements the func­
tions of a t ransaction server.)' The principal differ­
ence between the DECintact and ACMS approach is 
that DECintact clients and servers use a message­
based 3GL communications interface to send and 
receive work requests. Control in the ACMS moni­
tor resides in the execution controller. 
As the ACMS monitor does, the DECintact archi­
tecture addresses the p roblem areas discussed in 
the On-line Execution section in several ways. 
AJso, as with the ACMS approach, the factors we 
chose to trade off al lowed us to achieve better effi­
ciency, performance, and ease of use. 
Resource Use 
The D ECintact system's multi­
threaded 
methodology 
economizes 
o n  VMS 
resources. Sim ilar to the method used in the ACMS 
monitor, the system reduces process creations 
and image activations. A major difference between 
the ACMS and DECintact architectures is the way 
the DECintact monitor implements multithread­
ing support. The transparent implementation of 
threading capabi l it ies means that cod ing multi­
threaded applications is no more difficult than 
coding traditional single-threaded applications. As 
with any application-level thread ing scheme, how­
ever, the responsibi lity for ensuring that a logic 
error in one thread is isolated to that thread lies 
with the application. The DECintact client/server 
faci lities for accessing databases, like those used in 
the ACMS monitor, can realize simi lar benefits in 
process reuse, throughput, and error isolation. 
Start-up Costs 
The DECi ntact architecture, like 
the ACMS architecture, distributes start-up costs 
(i.e . ,  system resources and elapsed t ime) between 
two points: the start of the DECintact system, and 
the start of applications. System start-up can 
involve prestarting VMS process shel ls (as d is­
cussed p reviously) for subsequent application 
image activation. On-l ine appl ication start-up is 
executed on demand when the first user selects a 
particular menu task. Multithreaded appl icat ions, 
26 
once started, do not exi t  but wait for new user 
threads as users select the appl ication. Thus, the 
IXCintact terminal user can switch between appli­
cation images and incur only an inexpens ive 
thread creation. 
Contention 
As in the ACMS moni tor, database 
accesses in the DECintact client/server environ­
ment are channeled through a relatively few, but 
heavily used, number of processes rather than 
through a large number of lightly used processes. 
This reduction decreases lock contention. 
Processing Location 
Forms processing can be 
off-loaded to a front end and brought closer to the 
terminal user. Thus smaller, less expensive CPUs 
can be used whi le the rest of the appl ication exe­
cutes on a larger back-end machine or cl uster. In 
the DECintact monitor, the front end can consist of 
forms processing on.ly or a mix of forms process­
ing and application remote queuing work. 
Off-line Execution 
Many transaction processing applications are used 
with nontermi nal devices, such as a bar code 
reade r  or a com munications link used for an elec­
tronic funds transfer application. Because there is 
no human interaction with these applications, 
they have two requirements that differ from the 
requirements of interactive appl ications: tasks must 
be simple data entries, and the system must handle 
fa i l ures transparently. 
ACMS Offline Execution 
The ACMS monitor's goal for off-line p rocessing is 
to allow simple transaction capture to cont inue 
when the application is not ava i lable. A typical 
example is the continued capture of data on a man­
ufacturing assembly l ine by a MicroVAX system 
when t he appl ication is u nava i !able. The ACMS 
monitor provides two mechanisms for support­
i ng nonterminal devices: queuing agents and user­
written agents. 
Figure 4 illustrates the ACMS queuing model. 
A queuing system is a resource manager that 
processes entries, with priorities, in first-in, first­
out (FIFO) order. (In terms of DECdta, this is the 
queue resource manager.)' The ACMS queuing faci l­
ity is built upon RMS-indexed files. The primary 
goal of ACMS queuing is to provide a store­
and-forward mechanism to allow task requests 
to be collected for later execution. By using 
the ACMS$ ENQlJE_TASK service, a user can write 
Vol. J Nu I 
\Vinter /991 
Digital Technicaljountal 
¯
-
-
-
-
-
-
-
-
-
-
-
-
- -
-
-
- , 
I NODE B 
I 
I 
I 
I 
I 
I 
I 
i u---
I 
USER DATABASES 
I 
KEY: 
D 
D 
ACMS 
PROCESSES 
APPLICATION 
PROCESSES 
EXECUTION 
CONTROLLER 
PROCEDURE 
SERVERS 
1...---r 
Figure 4 
ACMS Queuing Agents 
a process that captures a task request and safely 
stores the task on a local disk queue. 
The ACMS moni tor provides a special agent, 
called the queued task initiator (QTI), which takes 
a task entry from the queue and subm its it to the 
appropriate execution controller. The QTI starts a 
DECdtm t ransaction, removes the task entry from 
the queue within that transaction, invokes the 
ACMS task, and passes the transaction identifier. On 
the DECdta architecture, the QTI implements t he 
functions of a request manager for queued 
requests.)' The task then joins that transaction. 
The removal from the queue is atomic with the 
commit of the task, and no task entry is lost or 
executed twice. 
Figure 5 shows the ACMS user-written agent 
model for off-line processing. With the ACMS sys­
tem interface, users may write their own versions 
of the command process. Note that because t hese 
agents cannot be safely stored on d isks, this 
method is generally not as reliable as using queues. 
User-written agents can be used, however, with 
DECdtm and the fault-tole rant VAXft 3000 system 
to produce a reliable front-end system. To do so, a 
Digital Tee/mica/ journal 
Vol. 3 No. I 
Winter l!.J91 
Digital's Transaction Processing Monitors 
user writes an agent that captures the input for the 
task and then starts a DECdtm transaction. The 
agent uses t he system i nterface services to invoke 
the ACMS task and passes the transaction identifier 
and the input data. When the task call completes, 
the agent com mi ts the t ransact ion. If DECdt m  
returns a n  error o n  t h e  commit, the agent loops 
back to start another transaction and to resubm it 
the task. If a VA.Xcluster system is used for the appli­
cation, this configuration will survive any single 
point of fa ilure. 
DECintact Offline Execution 
The D ECintact monitor provides several facilities 
for appl ications to perform off-line p rocessing. 
These facilities al low applications to 
• 
Interface with and process data from nonterm i­
na! devices and asynchronous events 
• 
Control transaction capture, store and forward, 
interprocess communication, and business work 
flow through the DECintact queuing subsystem 
Off-line Multithreading 
Off-line, multithreaded 
DECintact applications are typically used to service 
r - - - - - - - - - - - - - - - - - - - - - 1 
I 
VAXFT 3000 
I 
I 
I 
I 
BARCODE 
I 
I 
R EADERS 
I 
I 
I 
I 
_
_
_
 j 
r - - - - - - - - - - - - - - - - - - °  
I BACK-END NODE 
I 
I 
I 
I 
I 
I 
I 
I 
EXECUTION 
CONTROLLER 
I 
u---
PROCEDURE 
I 
SERVERS 
I 
L---- 
I 
USER DATABASES 
I _
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
 _ 
KEY: 
D 
D 
ACMS 
PROCESSES 
APPLICATION 
PROCESSES 
Figure 5 
ACMS User-written Agent Model 
for Off-line Processing 
27 
Transaction Processing, Databases, and Fault-tolerant Systems 
asynchronous events, such as the arrival of an 
electronic funds transfer message or the addition 
to the queue of an item already on a DECintact 
queue. The application programmer explicitly 
controls how many threads are created, when they 
are created, and which execution path or paths 
each thread wi ll follow. Off-l ine, multithreaded 
appl icat ions are wel l-suited to message switching 
systems and other aspects of electronic fu nds 
transfer in which each thread may be ded icated to 
servicing a different kind of event. 
DECintact Queues 
The p rimary goal of the 
DECintact queuing subsystem is to support a work 
flow m odel of business t ransactions. (In the 
DEC:dta architecture, the DECintact queuing sub­
system implements the functions of a queue 
resource manager and request initiator for queued 
requests.)' In a typical DECintact application that 
rel ies on queuing, the state of the business trans­
action may be represented by the queue on which 
a particular queue item resides at the moment. An 
item moves from queue to queue as the item 's 
process ing state changes, much as a work item 
moves from desk to desk. The superset of queue 
items that reside on queues throughout the appli­
cation at any one t ime represents the state of trans­
actions currently execut ing. Depending on the 
number of programs that need to process data dur­
ing the course of a transaction, a queue item may 
be inserted on several different queues before the 
transaction completes. The appl ication also may 
wish to cha in together several small transactions 
within the context of a larger business transaction. 
The DECintact queuing system functions through­
out the appl ication: from the front end, where 
queues col lect and route i ncoming data; to the 
back end , where queues can be integrated with 
data fi les in recovery units; and in between, where 
different p rograms i n  the application can use 
queues to share data. 
The DEc:intact queuing subsystem consists of a 
comprehensive set of callable services for the cre­
ation and manipulation of queues, queue sets, and 
queue items. Queue item operat ions performed 
within the context of a DECintact transaction are 
fully atomic along with DECintact fi le operations. 
In addition to overall workflow control, the 
DECintact queuing system al lows the fol lowing: 
• 
Deferred processing - An  item can be queued 
by one process and then removed from the 
queue later by another p rocess for processing. 
Deferred processing is usefu l  when the volume 
28 
of data entry is concentrated at particular times 
of clay; applicat ions can ass ign themselves to 
one or more queues and can be not ified when 
an item is inserted on the queue. 
• 
Store-and-forward processing - \Vhen users at 
the front end of the system wri te i tems to local 
queues, data entry can be continuous in the 
event of back-end system fa ilure or whenever a 
program that is needed to process data is tem­
porarily unavailable. 
• 
lnterprocess communication - Local ly between 
applications sharing a node and by means of 
the DECintact remote queuing faci li ty, applica­
tions can use the queuing system to rei iably 
exchange application data between processes 
and applications. 
A fundamental difference between ACMS queues 
and DECintact queues is that the ACMS system 
inserts tasks onto the queues, and tile DECintact 
system inserts data items. In DECi ntact queuing, 
each data item conta ins both user-suppl ied data 
and a header that incl udes an item key and other 
control information. The header is used by the 
queu ing system to control the movement of the 
item from queue to queue. Each queue item can be 
assigned an item priority. Items can be removed 
from the queue in FIFO order, in FIFO order within 
item priority, or by direct access using the item 
key. Queues can be stopped and started for inser­
tion, removal, or both. Queues can also be red i­
rected transparently at the system management 
i<.:vcl to runn ing applicat ions. 
ln the DECintact monitor, alert thresholds can be 
specified on a queue-by-queue basis to alert the 
system manager when queue levels reach defined 
amounts. Individual queue i tems can be held 
aga inst removal or released. Queues can be grouped 
together into logical ent i t ies, called queue sets, 
which .look and behave to the appl ication the same 
as individual queues. Queue sets have added facili­
t ies for broadcast insertion on all members of a 
queue set and a choice of removing algori thms that 
can weight relative item- and queue-level priorities 
from the queue. 
DECintact queues can be automatica l l y  distrib­
uted. At the system management level, a local 
queue can be designated as remote outbound. That 
is to say, items aclclecl to this queue are shipped 
transparently across the network to a correspond­
ing remote inbound queue on the destination 
node. The transfer is hand led by the DECintact 
queuing system by using exactly-once semantics 
Vuf. 3 Nu. f 
Winter f'J'Jf 
Digital Tecbnical journal 
(i.e. , t he i tem is guaranteed to be sent once and 
only once). From the point of view of the appl i­
cation that is add ing or removing items from the 
queue, remote queues behave exactly as local 
queues behave. 
To better understand some of the uses for 
DECintact queuing, consider a simplified but repre­
sentative electronic funds transfer example built 
on the DECintact monitor. Figure 6 shows the ele­
ments of such an application. In this application, 
transactions m ight be initiated either locally by 
clerks entering data i nto the system from user-
NODE A 
Digital's Transaction Processing Monitors 
generated documents or by an off-line application 
that receives data from another branch or bank. 
The transactions are verified or repa ired by other 
clerks in a diffe rent department of the bank. The 
transact ions are then sent to destination banks 
over one or more network services. 
To implement this application, the developer uses 
queues to route, safely store, and synchronize data 
as i t  progresses through the system, and to priori­
tize data i tems. Data items are given priority levels, 
based on application-defined criteria, such as trans­
fer amount, destination bank, or time-to-closing. 
,I I II, 
TERMINAL MANAGER/ 
DISPATCHER 
g--...._____, 
DATA ENTRY 
APPLICATION 
TERMINAL MANAGER/ 
DISPATCHER 
DATABASE 
SERVERS 
USER DATABASES 
KEY: 
D 
DEC INTACT 
PROCESSES 
APPLICATION 
PROCESSES 
VERIFY AND REPAIR 
APPLICATION 
,..._--'.-- FEDWIRE 
NETWORK 
Figure 6 
Elements of a DEC intact Electronics Functs Transfer 
Digital Teclmical jow·nal 
Vol. 3 No. I 
Winter 1991 
29 
Transact ion Processing, Databases, and Fault-tolerant Systems 
As i l lustrated in Figure 6, the terminal manager 
controls terminals for the Data Entry and Verify and 
Repa ir applications. Clerks enter data from user­
generated documents on-line as complete messages. 
Verification and repair clerks receive these mes­
sages as work items from the verify and repair 
queue through the Verify and Repair application. 
The result of verification is either a validated mes­
sage, which is ultimately sent to a destination bank, 
or an unverifiable message, which is routed to the 
supervisor queue for special hand ling. After special 
hand ling, the message rejoins the p rocessing flow 
by returning to the verify and repa ir queue. After 
val idation, the messages are i nserted in the 
Fedwire Xmt queue and sent over the network to 
the Federal Reserve System. The Fedwire Process 
application controls the physical interface to 
the commu nication l i ne and implements the 
Fedwire protocol. The validated messages are also 
used to u pdate a local database by means of 
database server programs. 
The Fedwire Xmt queue could be defined as a 
queue set, which would permit the Fedwire 
Process application to remove items from the 
queue by a number of algorit hms that bias t he 
transfer amount by queue and item p riority. 
Simi larly, this queue set cou ld be passively repriori­
tized near the close of the business day. In other 
words, the DECintact system adm inistrator could 
use the DECintact queue uti lity near the end of the 
day to change queue-wide priorities and ensure 
that items with a higher p riority level in the queue 
set wou ld be sent over the Fedwire first, without 
changing any application code. 
Applicatio1l Ma1lageme1lt 
Typically, transaction processing appl ications are 
crucial to the business running the app l ications. If 
the appl ications cannot perform their functions 
rel iabl y or securely, business activity may have to 
cease altogether or be curtailed, as in the case of an 
i nventory control application or electronic funds 
processing application. Therefore, t he appl ica­
tions requ ire addit ional controls to ensure that the 
applications and the access by users to the appli­
cations are limited to exactly what is needed for 
the business. 
ACMS Application Management 
Of the many features and tools for moni toring and 
controlling the system offered in the AG>IS moni­
tor, three areas are most often used. 
30 
• 
Contro l l ing and restricting term inal user 
environments 
• 
Control ling and restricting the appl ication 
• 
Ability to dynamically make changes to the appli­
cation without stopping work 
In add ition to using the VMS user amhorization 
fi le (Vi'v!S SYSUAF), the ACMS monitor provides utili­
ties to define which users and terminals have 
access to the ACMS system. Contro l led terminals 
are term inals defined by one of these utilities to be 
owned by the ACJVIS monitor. These terminals are 
al located by the ACMS monitor when the ACM S  
system is started . When a user presses the Return 
key, the ACMS monitor displays its login prompt. 
Unless the user has login access, the VMS system 
cannot be accessed. The user's access is restricted 
to only those ACMS functions that t he user is per­
m itted to invoke. This restriction prevents a user 
from damaging the i ntegrity of data on the system. 
The ACMS monitor also allows access support for 
terminals that are automatical ly logged in to the 
ACMS system, such as a term inal on a shop floor. 
Such access is useful for u np rivileged users who 
are not accustomed to computers. They can enter 
data without understanding the process for log­
ging in to the system. 
For appl ication control, the ACMS monitor uses a 
protected d irectory, ACMS$DIRECTORY, to store the 
appl ication definition files. The application autho­
rization util ity (AAU) ensures that special authori­
zation is required for a user to make changes to an 
appl ication. 
In the ACMS monitor, the application is a single 
point of controL The ACMS/START APPI.ICATION and 
ACMS/ST'OP APPLICATION commands cause the exe­
cution contro ller for the appl ication to be created 
and deleted. An operator can control the t imes 
when an appl ication is accessible. For example, an 
application can be control led to run only on 
Fridays or only between certai n  hours. The control 
of access times can also be used to restrict access 
whi le changes or repairs are made to the applica­
tion. This type of access control is difficult to 
achieve with only the VMS system because the VMS 
system does not provide these capabil ities. 
The execution controller does access-control 
list checking that is specified for each task. This 
mechanism can restrict user access by function. 
For examp le, a user could have the privi lege to 
make a particular update to a database but not have 
access to read or make changes to any other parts 
Vol. j No. 1 
Winter 199/ 
Digital Tecb11ical jounwl 
of that database. The execution controller achieves 
a much finer level of control than do the mecha­
nisms of the VMS system or the database system. 
DECintact Application Management 
The DECintact monitor controls access to the whole 
system and to individual tasks by means of a secu­
rity subsystem. The subsystem adds transaction­
processing-specific features to basic VMS security. 
• 
User security profi les specify the DECintact user 
name and password (DECintact users are not 
required to have an entry in the VMS SYSUAF 
file); levels of security entitlement; inclusive and 
exclus ive hours of permissible sign-on; menu 
entries authorized for the user. Only one user 
under a given DECintact user name can be signed 
on to the DECintact system at any one time on 
any one node. 
• 
Dedicated terminal security profi les are used, in 
conjunction wit h  user security profiles, to pro­
vide geographic entitlement. 
• 
CAPTIVE and INITlAL_MENU user attributes 
restrict users to a specific menu level of func­
tions and prevent the user from accessing outer 
levels. 
• 
User-specific menus are menu entries for which 
an explicit authorization has been granted in the 
user profile and are the only menu i tems visible 
on the menu p resented to terminal users. The 
DECintact monitor does include an exception for 
users who have an auditor privilege. Auditors 
can see all menu functions but must be specifi­
cally authorized to execute any single function. 
• 
The subsystem provides the ability to dynami­
call y  enable or disable specific menu functions. 
• 
Password revalidation is an attribute that can be 
associated with a menu function. If set, the user 
must reenter the DECintact user name and pass­
word before being allowed to access the function. 
The DECintact monitor supports both controlled 
or dedicated terminals and terminals assigned LAT 
terminal server appl ication ports, as does the ACMS 
monitor. These terminals are owned by, and allo­
cated to, the DECintact system. When a user types 
any character at t hese term inals, a DECintact sign­
on screen is displayed, and the user is prevented 
from logging in to the VMS system. 
Geographic entitlement limits certain DECintact 
terminal-based funct ions to certain term inals or 
Digital TecbtJicaljourtJal 
Vol. 3 No. I 
WitJter 1991 
Digital's Transaction Processing Monitors 
even to certain users on certain terminals. The three 
elements in geographic ent itlement are as follows: 
• 
The user security profile enables a function to be 
accessed by a certain user. 
• 
The term inal security profile enables a function 
to be accessed at a certain terminal. 
• 
A GEOG attribu te is associated with a menu 
entry in the terminal manager/d ispatcher's 
menu database. This attribute, when associated 
with a function, demands that there be an appli­
cable term inal security profile before the func­
t ion can be accessed . 
Normally, if a function is enabled in a user 
profile, the user can access the function without 
further checks. If t he GEOG attribute is associated 
with the function, however, t hat function must 
be enabled in the user profi le and in the term inal 
profile before it can be accessed. 
Geographic enti tlement is frequently a require­
ment in financial environments which have specific 
and rigid security protocols. For example, a bank 
officer may be authorized to execute certain sensi­
tive functions available only at dedicated terminals 
when the officer is signed-in at the home office. 
The same officer may be authorized to execute 
onl y  a subset of less sens i tive functions when 
signed-in from a branch office. Such sensitive func­
tions can be protected by requ iring that the user 
profile and the dedicated terminal profile enable 
the function. 
Applications and 
resources are controlled 
within the context of a DECintact copy's run-time 
and management environment. Multiple copies 
can be establis hed on the same VMS system. 
Different groups of users can mainta in a certa in 
level of autonomy (e.g ., separate appl icat ions and 
data files), but all users can also share some or all 
functions and resources of a given DECintact ver­
sion. A typical example of this concept, that is, the 
ability to create multiple DECintact copies for isola­
tion and parti tioning, is the com mon practice of 
establishing development, acceptance testing, and 
product ion DECintact environments. Managing 
applications and resources within a development 
environment, for example, can differ from manag­
ing applications and resources within a prod uction 
environment with a d ifferent system manager. 
Access to menu functions is contro l led by the 
INTACT MANAGE DISABLE/ENABLE command. This 
command removes or restores specified funct ions 
3 1 
Transact ion Processing, Databases, and Fault-tolerant Systems 
dynamically from all menus i n  the DECintact copy 
and disables or enables their selection by subse­
quent users. (Current accessors of the specified 
function are al lowed to complete the function.) 
The execution of single- and multi threaded appli­
cations or DECi ntact system components can be 
shut down by the INTACT 1Y1Ai'IAGE SHUTDOWN 
command. This command issues a mailbox request 
to the appl ication or component, which then initi­
ates an orderly shutdown. Access to the system by 
inclusive and exclusive t ime of day is control led on 
a per-user basis through the DECintact security 
subsystem. In addition to these com mands and 
functions, the queuing subsystem is managed by 
means of a queue management util ity This utility 
creates and deletes queues and queue sets, modi­
fies queue and queue set attributes, and performs 
all other functions necessary for managing the 
DECintact queuing subsystem. 
In general, the DECintact monitor's security and 
application control focuses on the front end by 
concentrati ng access checking at the point of sys­
tem sign-in and menu generation. The ACMS system 
concentrates more on the back-end parts of the 
system by means of VMS access contro l  lists (ACL) 
on specified tasks. The ACMS approach is built on 
VMS security and system access (the SYSUAF fi lc) 
and reflects an environment i n  which the VMS sys­
tem and the transaction p rocessing security func­
tions are typical ly performed by the same system 
management agency The DECintact monitor's sys­
tem access is hand led more i ndependently of the 
VMS system and reflects an environment in which 
transaction-processing-specific security functions 
may be performed by a different department from 
those of the general VMS security system. 
Conclusion 
The ACMS and DECintact transaction processing 
monitors provide a unified set of transact ion-pro­
cessing-specific services to the application envi­
ronment. A large functional overlap exists between 
the services etch monitor provides. Where the 
functions provided by each moni tor are identical 
or similar (e.g., client/server database access and 
support for DECforms), the factors that d istinguish 
one from the other are p rimarily a result of the use 
of 4GL and .)GL application p rogramming styles 
and interfaces. Where notable functional differ­
ences remai n  (as in each p roduct's respective 
queuing or security systems), the differences are 
p rimari ly ones of emphasis rather than func­
tional incompatibi lity. The set of common features 
shared by both monitors has been growing with 
the l atest releases of the ACMS and DECintact 
monitors. This external convergence has been fos­
tered and made possible by an internal conver­
gence, which is based on sharing the underlying 
code that supports the common features of each 
moni tor. As more common features are introduced 
and enhanced in the DECtp system, the investment 
in applications built on either moni tor can be 
protected and the d istinctive programmi ng sty les 
of both can be preserved. 
Reference 
1 .  P A .  Bernstein, W T. Emberton, and V Trehan, 
"DEC:dta - Digital's D istributed Transaction Pro­
cessing Architecture," Digital Technical journal, 
vol. 3, no. 1 (Winter 1991, this issue): 10- 17 . 
Vol. 3 No. I 
Winter 1991 
Digital TeciJnical jour11al 
William A. Laing 
James E. Johnson 
Robert V. Landau 
Transaction Management 
Support in the 1/MS 
operating System Kernel 
Distributed transaction management support is an enhancement to the VMS oper· 
ating system. This support provides services in the VMS operating system for atomic 
transactions that may span multtple resource managers, such as those for flat files, 
network databases, and relational databases. These transactions may also be distrib­
uted across multiple nodes in a network, independent of the communications 
mechanisms used by either the application programs or the resource managers. 
The Digital distributed transaction manager (DECdtm) services implement an opti­
mized variant of the two-phase commit protocol to ensure transaction atomicity. 
Additionally, these services take advantage of the unique VAX. cluster capabilities to 
greatly reduce the potential for blocking that occurs with the traditional two-phase 
commit protocol. These features, now part of the VMS operating system, are readily 
available to multiple resource managers and to many applications outside the 
traditional transaction processing monitor environment. 
Busi nesses are becoming critically dependent on 
the ava ilability and integrity of data stored on com­
puter systems. As these businesses expand and 
merge, they acquire ever greater amounts of on-line 
data, often on disparate computer systems and often 
in disparate databases. The Digital distributed trans­
action manager (DECdtm) services described in 
this paper address the problem of integrating data 
from multiple computer systems and multiple 
databases while maintaining data integrity under 
transaction control. 
The DECdtm services are a set of transaction pro­
cessing features embedded in the VMS operating 
system. These services support d istributed atomic 
transactions and implement an optimized variant 
of the well-known, two-phase commit protocol. 
Design Goals 
Our overall design goal was to provide base services 
on which higher layers of software could be built. 
This software would support reliable and robust 
applications, while maintaining data integrity. 
Many researchers report that an atomic trans­
action is a very powerful abstraction for bui ld ing 
robust applications that consistently update data.' ' 
Supporting such an abstraction makes i t  possible 
both to respond to partial failures and to maintain 
Digital Tecbntcal]ournal 
Vol. 3 No. I 
Winter 1991 
data consistency. Moreover, a simplifying abstrac­
tion is crucial when one is faced with the complex­
ity of a d istributed system. 
With increasingly rel iable hardware and the 
influx of more general-purpose, fault-tolerant sys­
tems, the focus on reliabil i ty has shifted from 
hardware to software.1 Recent discussions indicate 
that the key requ irements for building systems 
with a 100-year mean time between fa i lures may be 
(1) software-fault containment, using processes, 
and (2) software-fau lt masking, using process check­
pointing and transactions.' 
It was clear that we could use transactions as a 
pervasive technique to increase application avail­
ability and data consistency. Further, we saw that 
this technique had merit in a general-purpose oper­
ating system that supports transaction processing, 
as well as t imesharing, office automation, and tech­
nical computing. 
The design of DECdtm services also reflects sev­
eral other Digital and VMS design strategies: 
• 
Pervasive availability and reliability. 
As organi­
zations become increasingly dependent on their 
information systems, the need for all applica­
tions to be universally available and highly reli­
able increases. Features that ensure application 
33 
Transaction Processing, Databases, and Fault-tolerant Systems 
avai lability and data integrity, such as journal ing 
and two-phase commit, must be ava i lable to all 
applications, and not l im ited to those tradi tion­
ally thought of as "transaction processing." 
• 
Operating environment consistency. Embedding 
features in the operating system that are required 
by a broad range of utilities ensures consistency 
in two areas: first, in the functionali ty across all 
layered software products, and, second, in the 
interface for developers. For i nstance, if several 
d istributed database products require the two­
phase com m i t  protoco l, i ncorporati ng the 
p rotocol i nto the underlyi ng system allows 
programmers to focus on prov iding "value­
added" features for their products i nstead of 
re-creating a common routine or protocol. 
• 
Flex ibility and interoperabil ity. Our vision 
i ncludes making DECdtm interfaces ava i lable to 
any developer or customer, al lowing a broad 
range of software products to take advantage of 
the VMS environment. Future D ECdtm services 
are also being designed to conform to de facto 
and international standards for transaction pro­
cessing, thereby ensuring that VMS applications 
can interoperate with applications on other 
vendors' systems. 
Transaction Manager - Some 
Definitions 
To grasp the concept of transaction manager, some 
basic terms must first be understood: 
• 
Resource manager. A software entity that con­
trols both the access and recovery of a resource. 
For example, a database manager serves as the 
resource manager for a database. 
• 
Transaction. The execut ion of a set of opera­
t ions with the properties of atomicity, serializ­
abi l ity, and durability on recoverable resources. 
• 
Atomicity. Either all the operations of a trans­
action complete, or the transaction has no effect 
at all. 
• 
Serializabil ity. All operations that executed for 
the transaction must appear to execute serially, 
with respect to every other transaction. 
• 
Durabil ity. The effects of operations that exe­
cuted on behalf of the transaction are resi l ient 
to fai lures. 
A transaction manager supports the transaction 
abstraction by providi ng the following services: 
34 
• 
Demarcation operat ions to start, com m it, and 
abort a transaction 
• 
Execution operations for resource managers to 
declare themselves part of a transaction and for 
transaction branch managers to declare the d is­
tribution of a transaction 
• 
Two-phase commit operations for resource man­
agers and other transaction managers to change 
the transaction state (to either "preparing" or 
"committing") or to acknowledge receipt of a 
request to change state 
Benifits of Embedding Transaction 
Semantics in the Kernel 
Several benefits are achieved by embeddi ng trans­
action semantics i n  the kernel of the VMS operati ng 
system. Briefly, these benefits include consistency, 
interoperabi l ity, and flexibility. Embedding trans­
action semantics in the kernel makes a set of 
services ava i lable to d ifferent environments and 
products in a consistent manner. As a consequence, 
interoperabili ty between products is encouraged, 
as well as i nvestment in the development of "value­
added" features. The inherent flexibility allows a 
programmer to choose a transaction processing 
monitor, such as VAX ACMS, and to access multiple 
databases anywhere in the network. The p rogram­
mer may also write an appl ication that reads a 
VAX DBMS CODASYL database, updates an Rdb/VMS 
relat ional database, and writes report records to 
a sequential VAX RMS file - all i n  a single trans­
action. Because all database and transaction pro­
cessing products use DECdtm services, a fa ilure at 
any point i n  the transaction causes all updates to 
be backed out and the files to be restored to their 
original state. 
Two-phase Commit Protocol 
D ECdt m  services use an optimized variant of t he 
technique referred to as two-phase commit. The 
technique is a member of the class of protocols 
known as Atom ic Com m i t  Protocols. This class 
guarantees two outcomes: first, a single yes or no 
decision is reached among a distributed set of par­
ticipants; and, second, this decision is consistently 
propagated to all participants, regard less of sub­
sequent machine or communications fai lures. This 
guarantee is used in transaction processi ng to help 
achieve the atomicity property of a transaction. 
The basic two-phase commit protocol is straight­
forward and well known. It has been the subject of 
considerable research and technical l iterature for 
Vol. 3 No. 1 
Winter 1991 
Digital Tec1Jnical]our11al 
Transaction Management Suppo1·t in the VMS Operating System Kernel 
several years.'·6·'"·" The following section describes 
in detail this general two-phase commit protocol 
for those who wish to have more information on 
the subject. 
The Basic Two-phase Commit 
Protocol 
The two-phase commit protocol occurs between 
two types of participants: one coordinator and one 
or more subordi nates. The coordinator must arrive 
at a yes or no decision (typically called the " com­
mit decision") and propagate that decision to all 
subordinates, regardless of any ensu ing fa ilures. 
Conversely, the subordinates must ma inta in cer­
tain guarantees (as described below) and must 
defer to the coordinator for the result of the com­
mit decis ion. As the name suggests, two-phase 
commit occurs in two distinct phases, which the 
coordinator drives. 
In the first phase, cal led the prepare phase, the 
coordinator issues " requests to prepare" to all sub­
ordinates. The subordinates then vote, either a "yes 
vote" or a "veto." Impl icit in a "yes vote" is the guar­
antee that the subordinate will neither commit nor 
abort the transaction (decide yes or no) without an 
explicit order from the coordinator. This guarantee 
must be maintained despite any subsequent fai l­
ures and usually requires the subordinate to place 
sufficient data on disk (prior to the "yes vote") to 
ensure that the operations can be either completed 
or backed out. 
The second phase, cal led the comm it phase, 
begins after the coordinator receives all expected 
votes. Based on the subordinate votes, the coor­
dinator decides to commit if there are no "veto" 
votes; otherwise, it decides to abort. The coordina­
tor propagates the decision to all subordi nates as 
either an ··order to com mit" or an "order to abort." 
SUBORDINATE 
COORD INA TOR 
INCREASING 
TIME 
j 
END TRANS FROM 
APPLICATION 
-----
REQUEST TO PREPARE 
----
FORCE WRITE 
"PREPARE" 
RECORD 
YES VOTE 
 EJ FORCE WRITE 
"COMMIT" 
COMMIT POINT --....-
RECORD 
NOTIFY 
APPLICATION 
----
ORDER TO COMMIT 
LAZY WRITE 
"COMMIT" 
RECORD 
DONE 
----- 
LAZY WRITE 
F===t 
"FORGET" 
l__.J 
RECORD 
LAZY WRITE 
"FORGET" 
RECORD 
FigU1·e 1 
Simple Two-phase Commit Time Line 
Digital Technicaljounwl 
Vol. 3 No. I 
\Vinter 1991 
35 
Transaction Processing, Databases, and Fault-tolerant Systems 
Because the coordinator's decision must survive 
fa ilures, a record of the decision is usually stored 
on disk before the orders are sent to the subordi­
nates. When the subordinates complete process­
ing, they send an acknowledgment back to the 
coordinator that they are "done." This allows the 
coord inator to reclaim d isk storage from com­
pleted transactions. Figure 1 shows a time l ine of 
the two-phase commit sequence. 
A subord inate node may also function as a supe­
rior (intermediate) node to follow-on subordinates. 
In such cases, there is a tree-structured relation­
ship between the coordinator and the full set of sub­
ordinates. Intermediate nodes must propagate the 
messages down the tree and collect responses back 
up the tree. Figure 2 shows a time l ine for a two­
phase commit sequence with an intermediate node. 
Most of us have had direct contact with the two­
phase commit protocol. It occurs in many activities. 
Consider the typical wedding ceremony as p re­
sented below, which is actual ly a very precise two­
phase commit. 
SUBORDINATE 
INTERMEDIATE 
COORDINATOR 
36 
INCREASING 
TIME 
j 
-----
FORCE WRITE 
"PREPARE" 
RECORD 
YES VOTE 
ORDER TO COMMIT 
LAZY WRITE 
"COMMIT" 
RECORD 
END TRANS FROM -
APPLICATION 
-----
REQUEST TO PREPARE 
-... EJ 
FORCE WRITE 
"PREPARE" 
..--
RECORD 
-----
YES VOTE 
------ -... ; FORCE WRITE 
l__.J "COMMIT" 
COMMIT POINT - ..--
RECORD 
NOTIFY 
APPLICATION 
-----
ORDER TO COMMIT 
LAZY WRITE 
"COMMIT" 
RECORD 
DONE 
------
LAZY WRITE 
"FORGET" 
RECORD 
-... EJ 
..--
LAZY WRITE 
"FORGET" 
RECORD 
Figure 2 
Three-node Two-phase Commit Time Line 
Vol. .3 No. I 
Winter 1991 
Digital Technical journal 
Transaction Management Support in the VMS Operating System Kernel 
Official: 
Bride: 
Will you, Mary, take john . 
! will. 
Official: 
Groom: 
Will you, John, take Mary . . .  ? 
I will. 
Official: 
I now pronounce you man and wife. 
The above dialog can be v iewed as a two-phase 
commit: 
Coordinator: 
Participant 1 :  
Coordinator: 
Participant 2: 
Coordinator: 
Request to Prepare? 
Yes Vote. 
Request to Prepare? 
Yes Vote. 
Commit Decision. 
Order to Commit. 
The basic two-phase commit protocol is straight­
forward, survives fa ilures, and produces a single, 
consistent yes or no decision. However, this proto­
col is rarely used in commercial products. Opti­
mizations are often applied to mi nimize message 
exchanges and physical d isk writes. These optimi­
zat ions are important particularly to the trans­
action process ing market because the market is 
very performance sens itive, and two-phase com­
mit occurs after the application is complete. Thus, 
two-phase commit is reasonably considered an 
added overhead cost. We have endeavored to reduce 
the cost in a number of ways, resulting in low 
overhead and a scalable protocol embodied i n  the 
DECdt m  services. Some of the optim izations are 
described later in another section. 
COMMUNICATION 
INTERFACE 
RESOURCE 
MANAGER 
REGISTRY 
TRANSACTION 
COORDINATOR 
RESOURCE 
MANAGER 
SERVICES 
t 
USER 
BRANCH 
MANAGEMENT 
SERVICES 
SERVICES 
Components of the DECdtm Services 
The DECdtm services were developed as three sep­
arate components: a transaction manager, a log 
manager, and a communication manager. Together, 
these components provide support for d istributed 
transaction management. The transaction manager 
is the central component. The log manager ser­
vices enable the transaction manager to store data 
on nonvolatile storage. The communication man­
ager provides a location-i ndependent interprocess 
communication service used by the transaction 
and log managers. Figure 3 shows the relationships 
among these components. 
The Digital Distributed Transaction 
Manager 
As the central component of the DECdtm services, 
the transaction manager is responsible for the 
application interface to the DECdtm services. This 
sect ion presents the system services the trans­
action manager comprises. 
The transaction coord inator is the core of the 
transaction manager. It implements the transaction 
state machine and knows which resource man­
agers and subordinate t ransaction managers are 
involved in a transaction. The coordinator also con­
trols what is writ ten to nonvolatile storage and 
manages the volatile l ist of active transactions. 
The user services are routines that implement 
the START_TRANSACTION, END_TRANSACTION, and 
ABORT_ TRANSACTION transaction system services. 
VOLATILE 
REGISTRY 
LOGGING 
INTERFACE 
t 
INFORMATION 
SERVICES 
-
TO REMOTE 
DECDTM 
TO HARDENED 
REGISTRY 
EXTERNAL 
INTERFACE 
Figure 3 
Components of the DECdtm Services 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
37 
Transaction Processing, Databases, and Fault-tolerant Systems 
They val idate user parameters, dispense a trans­
action identifier, pass state transition requests to 
the transaction coord i nator, and return informa­
tion about the transaction outcome. 
The branch management services support the 
creation and demarcation of branches in the d is­
tribu ted transaction tree. New branches are con­
structed when subordinate application programs 
are invoked in a d istributed environment. The ser­
vices are cal led on to attach an appl ication pro­
gram to the transaction, to demarcate the work 
done in that application as parr of the transaction, 
and finally to return i nformation about the trans­
action outcome. 
The resource manager services are routines that 
provide the interface between the DECdtm services 
and the cooperati ng resource managers. This inter­
face al lows resource managers to declare t hem­
selves to the transact ion manager and to register 
their i nvolvement in the "voting'' stage of the two­
phase comm i t  process of a specific transaction. 
Final ly, the i nformation services routines are 
the interface that allows resource managers to 
query and update transaction information stored 
by DECdtm services. This information is stored 
i n  either the volatile-active transaction l ist or the 
nonvolati le transaction log. Resource managers 
may resolve and possibly modify the state of 
"in-doubt" transactions through these services. 
The Log Manager 
The Jog manager provides the transaction manager 
with an interface for storing sufficient information 
in nonvolatile storage to ensure that the outcome 
of a transaction can be consistently resolved. This 
interface is ava ilable to operating system compo­
nents. The log manager also supports the creation, 
deletion, and general management of the trans­
action logs used by the transaction manager. An 
additional utility enables operators to examine 
transaction logs and, i n  extreme cases, makes it 
possible to change the state of any transaction. 
The Communication Manager 
The communication manager provides a command/ 
response message-passing facil ity to the trans­
action manager and the log manager. The interface 
is specifically designed to offer high-performance, 
low-latency services to operat i ng system com­
ponents. The command/response, connection­
oriented, message-passi ng system al lows clients 
to exchange messages. The clients may reside on 
the same node, within the same cluster, or within 
38 
a homogeneous VMS wide area network. The com­
munication manager also provides highly optimized 
local (that is, intranode) and i ntracluster trans­
ports. In addition, this service component multi­
plexes communication l inks across a single, cached 
DECnet virtual circuit to improve the performance 
of creating and destroying wide area links. 
Transaction Processing Model 
D igital's transaction processi ng model entai ls the 
cooperation of several distinct elements for correct 
execution of a d istributed transaction. These ele­
ments are ( 1 )  the application programmer, (2) the 
resource managers, (3) the i ntegrat ion of the 
DECdtm services into the VMS operating system, 
( 4) transaction trees, and (5) vote-gathering and 
the fi nal outcome. 
Application Programmer 
The application programmer must bracket a series 
of operations with START_TRANSACTION and 
END_TRANSACTION calls. This bracketing demar­
cates the unit of work that the system is to treat as 
a single atomic unit. The application programmer 
may call the DECdtm services to create the branches 
of the distributed transaction tree. 
Resource Managers 
Resource managers, such as VAX RMS, VA,'{ Rdb/VMS, 
and VAX DBMS, that access recoverable resources 
during a transaction i nform the DECdtm services of 
their i nvolvement in the transaction. The resource 
managers can then participate i n  the voti ng phase 
and react appropriately to the decision on the final 
outcome of the transaction. Resource managers 
must also provide recovery mechanisms to restore 
resources they manage to a transaction-consistent 
state in the event of a fa i l ure. 
Integration in the Operating System 
The DECcltm services are a basic component of the 
VMS operating system. These services are responsi­
ble for ma inta i n i ng the overa.l l state of the d istrib­
u ted transact ion and for ensuring that sufficient 
information is recorded on stable storage. Such 
information is essential in the event of a fa i lure so 
that resource managers can obtain a consistent 
view of the outcome of transactions. 
Each VMS node in a network normally conta ins 
one transaction manager object. This object mai n­
ta ins a l ist of participants in transactions that are 
act ive on the node. This l ist consists of resource 
managers local to the node and the transaction 
manager objects located on other nodes. 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
Transaction Management Support in the VMS Operating System Kernel 
Transaction Trees 
The node on which the transaction originated (that 
is, the node on which the START_TRANSACTION 
service was called) may be viewed as the "root" of 
a distributed transact ion tree. The t ransaction 
manager object on this node is usually responsible 
for coordinating the transaction commit phase of 
the transaction. The transaction t ree grows as 
applicat ions call on the branch management ser­
vices of the transaction manager object. 
The transaction identifier dispensed by the 
START_TRANSACTION service is an input parameter 
to the branch services. This parameter ident ifies 
two concerns for the local transact ion manager 
object: (1) to which transaction tree the new branch 
should be added, and (2) which transaction man­
ager object is the immed iate superior in the tree. 
Resource managers join specific branches in a 
transaction tree by cal l ing the resource manager 
services of the local transaction manager object. 
Vote-gathering and the Final Outcome 
When the "commit" phase of the transaction is 
entered (triggered by an application call to 
END_TRA.t"\ISACTION), each transaction manager 
object involved in the transaction must gather the 
"votes" of the locally registered resource managers 
and the subordinate transaction manager objects. 
The results are forwarded to the coordinating trans­
action manager object. 
The coordinating transaction manager object 
eventually informs the local ly registered resource 
managers and the subordinate transaction manager 
objects of the final outcome of the transaction. The 
subordinate transaction manager objects, in turn, 
propagate this information to local ly registered 
resource managers as well as to any subordinate 
transaction manager objects. 
Protocol Optimizations 
The DECd tm services use several previously pub­
lished optimizations and extend those optimiza­
tions with a number that are unique to VAXcluster 
systems. In this section we present these general 
optimizations, a discussion of VAXcluster consider­
at ions, and two VAXcluster-specific optimizations. 
General Optimizations 
The following sections describe some previously 
published optimizations. 
Presumed Abort 
DECdtm services use the "pre­
sumed abort" optimization."·" This optimization 
states that, if no information can be found for a 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
transaction by the coordinator, the transaction 
aborts. This removes the need to write an abort 
decision to disk and to subsequently acknowledge 
the order to abort. In addition, subordinates that 
do not mod ify any data during the transaction (that 
is, they are "read only"), avoid writing i nformation 
to disk or participating in the commit phase. 
Lazy Commit Log Write 
The DECdtm services 
can act as intermediate nodes in a distributed trans­
action. In this mode, they write a "prepare" record 
prior to responding with a "yes vote." They a lso 
write a "commit" record upon receipt of an order 
to comm it. This latter record is written so that the 
coordinator need not be asked about the commit 
decision should the intermed iate node fa il. This 
refi nement isolates the intermediate node's recov­
ery from communication fa ilures between i t  and 
the coordinator. 
Performance is enhanced when the DECdtm ser­
vices write the comm it record on an intermediate 
node in a "nonurgent" or " lazy" manner.'" The lazy 
write buffers the i nformation and waits for an 
urgent request to trigger the group commi t  t imer 
to write the data to disk. Typically, this operation 
avoids a disk write at the intermediate node. The 
increase in the length of t ime before the commit 
record is written is negligible. 
One-phase Commit 
A key consideration in the 
design of the DECdtm services was to incur mini­
mal impact on the performance of Digital's data­
base products. We exploited two attributes to 
achieve this goal. First, all current users are limited 
to non-distributed transactions (those that involve 
only a single subordinate). Second, the rwo-phase 
commit protocol requires that all subordinates 
respond with a "yes vote" to commi t  the trans­
action. This allows a highly optimized path for 
single subord inate transactions. Such transactions 
require no writes to d isk by the DECdtm services 
and execute in one phase . The subordinate is told 
that it is the only voting party in the transaction 
and, if it is willing to respond with a "yes vote," i t  
should proceed and perform its order t o  commit 
processing. 
VAX cluster Considerations 
The optimizations listed above (and others not 
described here) provide the DECdtm services 
with a competitive two-phase commit protocol. 
VAXcluster 
technology, 
though, 
offers 
other 
untapped potential. VAXcluster systems offer sev­
eral unique features, in particular, the guarantee 
39 
Transaction Processing, Databases, and Fault-tolerant Systems 
aga inst partitioning, the distributed lock manager, 
and the ability ro share disk access between CPUs." 
Within a VAXcluster system, use of these unique 
features al lows the DECdtm services to avoid a 
blocked condition which occurs during the short 
period of time when a su bord inate node responds 
wi th a "yes vote" and communication with its 
coord inator is lost. NormaLly, the subord inate is 
unable to proceed with that transaction's commit 
until com munications have been restored. 
Outs ide a VAXcluster system, the DECdtm ser­
vices would i ndeed be blocked. If, however, the 
subordi nate and its coordinator are in the same 
VAXcluster system, this wil l nor occur. If communi­
cation is lost, a subordinate node knows, as a result 
of the guarantee against partitioning, that i ts coor­
dinator has failed. 
Because a subordinate node can access the trans­
action Jog of the failed coordinator, it may imme­
diately "host" its fa iled coordinator's recovery. 
Communications to the hosted coord inator are 
quickly restored, and the subordinate node is able 
to complete the transaction commit. 
VAXcluster-specific Optimizations 
Once the blocking potential was removed from 
intra-VAXcluster transactions, several additional 
protocol optimizations became practical. The 
optim izat ions described in this section are dynam­
ically enabled if the subordinate and its coordina­
tor are both in the same VAXcluster system. 
Early Prepare Log Write 
As mentioned earlier, an 
intermediate node must write a "prepare" record 
prior to responding with a "yes vote." The pres­
ence of this record in an intermed iate node's 
log ind icates that the node must get the outcome 
of the t ransaction from the coordinator and, thus, 
it is subject to blocking. Therefore, the prepare 
record is typically written after all the expected 
votes are returned, which adds to commit-time 
latency. 
The DECdtm services are free from blocking con­
cerns within a VAXclusrer system; the vast majority 
of transactions do commit. This factor p rompted 
an optim ization that writes a prepare record while 
simultaneously collecting the subordinate votes. 
This reduces commit- time latency. 
No Commit Log Write 
The lazy commit log write 
optimization described above causes the inter­
mediate node's commit record to be written and , 
thus, minim izes the potential for blocking should 
the intermediate node fail. Note that this is not a 
concern for the intra-VAXcluster case. Therefore, no 
com mit record is written at the intermediate node. 
Performance Evaluation 
Table 1 describes the message and Jog write costs 
of the DECdtm services protocol and compares i t  
t o  the basic two-phase commit protocol, as wel l  
a s  to the standard presumed abort variant previ­
ously described." '' 
Table 1 
Logging and Message Cost by Two-phase Commit (2PC) Protocol Variant 
Coordinator 
Intermediate 
Coordinator 
Log Write 
Message 
Log Write 
Message 
Basic 2PC: 
2, 1 forced 
2N 
2, 2 forced 
2 
Presumed Abort: 
2, 1 forced 
2N 
2, 2 forced 
2 
(RO intermediate) 
2, 1 forced 
1 N  
0 
1 
Normal DECdtm: 
2, 1 forced 
2N 
2, 1 forced 
2 
(RO intermediate) 
2, 1 forced 
1 N  
0 
1 
lntracluster: 
2, 1 forced 
2N 
1 ,  1 forced* 
2 
(RO intermediate) 
2, 1 forced 
1 N  
0 
1 
DECdtm 1 PC: 
0 
Notes: 
Log writes are total writes, forced. The table entry 2,1 forced means that there are two total log writes, one of which is forced. A forced write 
must complete before the protocol makes a transition to the next state. 
RO means Read Only. 
Where a message is listed as xN, N represents the number of intermediates that fit that category. 
• In this i nstance, forced means that the log write is initiated optimistically; thus, it has lower latency. 
40 
Vol. 3 No. 1 
Winter 1991 
Digital Technical journal 
Transaction Management Support in the VMS Operating System Kernel 
Ease-of-use Evaluation 
A primary goal in providing transaction processing 
primitives within the VMS kernel was to supply 
many disparate applications with a stra ightforward 
interface to distributed transaction management. 
This contrasts with most commercially ava ilable 
systems, where distributed transaction manage­
ment functional ity is ava ilable only from a trans­
action processing moni tor. This latter form restricts 
the functional ity to applicat ions written to exe­
cute under t he control of the transaction process­
ing monitor, and it effectively precludes other 
applications from making use of the technology. 
from the short t ime it took to make the required 
changes. Based on this experience, we expect third­
party software vendors to rapid ly take advantage of 
the DECdtm services as they become available as 
part of the standard VMS operating system. 
From the outset of development, we endeavored 
to provide an interface that was suitable for as 
many applications as possible. We made early ver­
sions of the DECdtm services ava ilable within 
Digital to decrease the " time to market" for soft­
ware products that wished to exploi t  d istributed 
transaction processing technology. As of]uly 1990, 
at least seven D igital software products have been 
mod ified to use the DECdtm services. These 
products are VAX Rdb/VMS, VAX DBMS, VAX RMS 
)ournali ng, VAX ACMS, DECin tact, VAX RALLY, 
and VAX SQL. 
To i ncorporate the D ECdtm services into a 
recoverable resource manager, t he existing inter­
nal transaction management module with calls 
to the DECdtm services must be replaced. The 
resource manager must also be modified to cor­
rect ly respond to the prepare and commit callbacks 
by the DECdtm services. Further, the recovery 
logic of the resource manager must be modified to 
obtain from t he DECdtm services the state of "in 
doubt" transactions. 
Example of DECdtm Usage 
The model and pseudocode shown in Figures 4a 
and b i llustrate the use of DECdt m  services in a 
simple example of a d istributed transaction. The 
transaction spans two nodes, NODE_A and NODE_B, 
in a VMS network. During the course of the t rans­
action, recoverable resources managed by resource 
managers, RM_A and RM_B, are mod ified. Two 
"appl ication" programs, APPL_A and APPL_B, that 
run on NODE_A and NODE_B, respectively, make 
normal procedural cal ls to RM_A and RM_B. APPL_A 
In general, the modifications to these products 
have been relatively minor, as might be inferred 
NODE A 
I NODEB
- - - - - - - - - - - - - - - ­
DECDTM 
RESOURCE 
BRANCH 
USER 
MANAGER 
SERVICES 
SERVICES 
SERVICES 
+ 
+ 
- ? 
-. T 
I 
RM_A I====== APPL_A 
. . . . . .  
I 
I 
I 
- + - - - - - j _  
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
- ƒ· · · · · · · · J · 
I 
I 
I 
I 
I 
I 
DECDTM 
USER 
BRANCH 
RESOURCE 
SERVICES 
SERVICES 
MANAGER 
SERVICES 
+ 
+ 
 
 
+ 
+ 
. ...... 
APPL_B 
- - - - - 1 
- - - - - -
RM_B I 
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
 I 
$ - - - - - - - - - - - - - - - - - -
KEY: 
IPC CONN ECTION 
RPC 
--
SYSTEM SERVICE CALL 
RM 
APPL 
PROC EDURE CALL 
RESOURCE MANAGER 
APPLICATION 
Figure 4a 
Model Illustrating the Use of DECdtm Services 
Digital Technical journal 
Vtll. 3 No. I 
Winter 1991 
41 
Transaction Processing, Databases, and Fault-tolerant Systems 
P R O G R A M  A P P L  A 
E s t a b l i s h 
c o m m u n i c a t i o n s  w i t h  r e m o t e  a p p l i c a t i o n 
I P C _ L I N K  ( n o d e = " N O D E_B " ,  a p p l i c a t i o n = " A P P L_B " ,  
l i n k = l i n k_ i d ) ;  
E x c h a n g e  t r a n s a c t i o n 
m a n a g e r  n a m e s  
L I B $ G E T J P I  
( J P I $_C O M M I T_ D O M A I N , , , m y_ c d ) ;  
I P C 
T R A N S C E I V E  ( l i n k = L i n k_ i d ,  s e n d_d a t a = m y_ c d ,  
r e c e i v e_d a t a = y o u r _ c d ) ;  
S t a r t 
a 
t r a n s a c t i o n 
$ S T A R T_T R A N S W  
( i o s b = s t a t u s ,  
t i d = t i d ) ;  
M a k e  a 
p r o c e d u r a l 
c a l l  t o  R M  A 
t o  p e r f o r m  a n  o p e r a t i o n 
R M_A 
( t i d , 
r e q u e s t e d_o p e r a t i o n ) ;  
! 
N o w  
c r e a t e  a 
t r a n s a c t i o n 
b r a n c h  f o r  t h e  r e m o t e  a p p l i c a t i o n 
$ A D D  B R A N C H W  
( i o s b = s t a t u s ,  
t i d = t i d ,  b r a n c h = b i d ,  
c d_n a m e = y o u r_ c d ) ;  
A s k  A P P L  8 
t o  d o  s o m e t h i n g 
a s  p a r t  o f  t h i s  t r a n s a c t i o n 
! P C 
T R A N S C E I V E  ( l i n k = l i n k_ i d ,  s e n d_d a t a = ( t i d , 
b i d ,  d a t a ) ,  
r e c e i v e_d a t a = s t a t u s ) ;  
A n d  e n d  
t h e  t r a n s a c t i o n 
$ E N D  T R A N S W  
( i o s b = s t a t u s ,  
t i d = t i d ) ;  
P R O G R A M 
A P P L  B 
( l i n k  i d )  
4 2  
E x c h a n g e  t r a n s a c t i o n 
m a n a g e r  n a m e s  
I P C _R E C E I V E  ( l i n k = L i n k_ i d ,  d a t a = s u p_ c d ) ;  
L I B $ G E T J P I  
( J P I $_ C O M M I T_D O M A I N , , , m y_ c d ) ;  
I P C _ R E P L Y  
( L i n k = l i n k_ i d ,  d a t a = m y_ c d ) ;  
N o w  w e  e x e c u t e  t r a n s a c t i o n 
r e q u e s t s  
l o o p ;  
! P C 
R E C E I V E  ( l i n k = l i n k _ i d ,  d a t a = ( t i d , 
b i d ,  d a t a ) ) ;  
S t a r t  t h e  t r a n s a c t i o n 
b r a n c h  c r e a t e d 
b y  A P P L_A . 
$ S T A R T  B R A N C H W  ( i o s b = s t a t u s ,  
t i d = t i d ,  b r a n c h = b i d ,  
c d_n a m e = s u p_ c d ) ;  
! 
M a k e  a 
p r o c e d u r a l 
c a l l  t o  R M_B 
t o  p e r f o r m  a n  o p e r a t i o n 
R M_B 
( t i d , 
r e q u e s t e d_o p e r a t i o n ) ;  
T e l l  A P P L  A 
w e  a r e 
d o n e  
I P C  R E P L Y  
( l i n k = l i n k_ i d ,  d a t a = S S $_N O R M A L ) ;  
D e c l a r e  t h a t  w e  a r e  f i n i s h e d  f o r  t h i s 
t r a n s a c t i o n 
a n d  
w a i t  f o r  i t  t o  c o m p l e t e  
$ R E A D Y  T O  C O M M I T W 
( i o s b = s t a t u s ,  t i d = t i d ) ;  
e n d _ l o o p ;  
Vol .
. 3 No. I 
Winter 1991 
Digital Technical jourrw/ 
Transaction Management Support in the VMS Operating System Kernel 
R O U T I N E  R M_A 
( t i d , 
r e q u e s t e d_o p e r a t i o n )  
I f  t h i s 
i s  
t h e  f i r s t  o p e r a t i o n ,  
r e g i s t e r  w i t h  D E C d t m  s e r v i c e s  a s  a 
r e s o u r c e  m a n a g e r . 
A s  
p a r t  o f  
t h e 
r e g i s t r a t i o n 
w e  d e c l a r e 
a n  e v e n t  
r o u t i n e 
t h a t  w i l l  b e  
c a l l e d  d u r i n g 
t h e  v o t i n g 
p r o c e s s .  
i f  f i r s t  
t i m e 
w e ' v e 
b e e n  
c a l l e d  t h e n  
$ D E C L A R E  R M W  
( i o s b = s t a t u s ,  
n a m e = " R M_A " ,  
e v t r t n = R M_A_E V E N T ,  
r m_ i d = r m_ h a n d l e ) ;  
I n f o r m  D E C d t m  s e r v i c e s  o f  o u r  
i n t e r e s t  
i n  t h i s 
t r a n s a c t i o n 
i f  t i d  h a s  n o t  
p r e v i o u s l y  b e e n  
s e e n  
t h e n  
$ J O I N  R M W  ( i o s b = s t a t u s ,  
r m_ i d = r m_h a n d l e ,  
t i d = t i d , 
p a r t _ i d = p a r t i c i p a n t ) ;  
1 
P e r f o r m  t h e  r e q u e s t e d 
o p e r a t i o n 
D O_O P E R A T I O N  
( r e q u e s t e d_o p e r a t i o n ) ;  
R E T U R N 
R O U T I N E  R M  
A 
E V E N T  
( e v e n t  b l o c k )  
! 
S e l e c t  a c t i o n 
f r o m  t h e  D E C d t m  s e r v i c e s  e v e n t  
t y p e  
C A S E  
e v e n t  
b l o c k . D D T M $ L  O P T Y P E  
F R O M  
. . .  T O  
. . .  
D o  " r e q u e s t  t o  p r e p a r e "  p r o c e s s i n g 
[ D D T M $ K_ P R E P A R E J : 
D O  P R E P A R E  A C T I V I T Y  ( r e s u l t = s t a t u s ,  t i d = e v e n t _ t y p e . D D T M $ A_T I D ) ;  
D o  " o r d e r 
t o  c o mm i t "  p r o c e s s i n g 
[ D D T M $ K_ C O M M I T J : 
D O  C O M M I T  A C T I V I T Y  ( r e s u l t = s t a t u s ,  
t i d = e v e n t _t y p e . D D T M $ A_T I D ) ;  
D o  " o r d e r  t o  a b o r t "  p r o c e s s i n g 
[ D D T M $ K_A B O R T J : 
D O  A B O R T  A C T I V I T Y  
( r e s u l t = s t a t u s ,  
t i d = e v e n t _t y p e . D D T M $ A_T I D ) ;  
E S A C ;  
I n f o r m 
t h e 
D E C d t m  s e r v i c e s  o f  t h e  f i n a l  s t a t u s  o f  o u r  e v e n t  
p r o c e s s i n g . 
$ F I N I S H 
R M O P W  
( i o s b = i o s b ,  p a r t _ i d = e v e n t _t y p e . D D T M $ L_P A R T_ I D ,  
r e t s t s = s t a t u s ) ;  
R E T U R N  
Figure 4b 
Pseudocode Illustrating the Use of DECdtm Services 
and APPL_B use an interprocess communication 
mechanism to communicate information across 
the network. The DECdtm service calls are pre­
fi.."Xed with a dollar sign ($). 
ROUTINE RM_A_EVENT, is invoked by the DECdtm 
services during transaction state transitions. 
The code for the resource managers, RM_A and 
RM_B, is identical with respect to calls for the 
DECdtm services. The resource manager routine, 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
Conclusions 
The addition of a d istributed transaction manager 
to the kernel of the general-purpose VMS operating 
system makes d istribu ted transactions ava ilable 
43 
Transaction Processing, Databases, and Fault-tolerant Systems 
to a wide spectrum of appl ications. This design 
and implementation was accompl ished with com­
parative ease and with quality performance. In 
addition to uti lizing the most commonly described 
optimizations of the two-phase commit protoco l, 
we have used optim izations that exploit some of 
the unique benefits of the VAXcluster system. 
Acknowledgments 
We wish to gratefully acknowledge the contrib­
utions of all the transaction processi ng architects 
involved, and in particular Vijay Trehan, for del iver­
ing to us an understandable and implement­
able architecture. We also extend our thanks to 
Phi l  Bernstein for his encouragement and advice, 
and to our initial users, Bill Wright, Peter Spiro, 
and Lenny Szubowicz, for their persistence and 
good nature. 
Finally, and most importantly, we would l ike 
to thank all the DECdt m  development engineers 
and the others who helped ship the product: 
Stuart Bay ley, Cathy Foley, Mike Grossmith, Tom 
Harding, Tony Hasler, Mark Howell, Dave Marsh, 
Julian Palmer, Kevin Playford, and Chris Whitaker. 
References 
I .  R .  Haskin, Y. Malachi, W Sawdon, and G. Chan, 
" Recovery Management in Quicksi lver,'' ACLl-'1 
Transactions on Computer Systems, vol. 6, 
no. 1 (February 1988). 
2. 
A. Spector et al. , Camelot: A Distributed Trans­
action Facility for Mach and the Internet - An 
Interim Report (Pittsburgh: Carnegie Mellon 
University, Department of Computer Science, 
June 1987). 
). W Bruckert, C. Alonso, and J. Melvin, "Verifi­
cation of the First Fault-tolerant VA..'{ System," 
Digital Technical journal, vol. 3, no. 1 (Wi nter 
1991 , this issue): 79-85. 
4. J. Gray, "A Census of Tandem System Ava i la­
bi lity between 1985 and 1990," Tandem Techni­
cal Report 90.1 ,  part no. 33579 (January 1990). 
5. 
P Bernstei n ,  V Hadzilacos, and N. Goodman, 
Concurrency Control and Recovery in Data­
base Systems (Readi ng, MA: Add ison-Wesley, 
1987). 
6. J. Gray, " Notes on Database Operating Systems," 
In Operating Systems: An Advanced Course 
(Berlin: Springer-Verlag, 1978). 
44 
7. B. Lampson , "Atomic Transactions," In Dis­
tributed Systems-Architecture and Imple­
mentation: A n  Aduanced Course, edi ted by 
G. Goos and J. Hartmanis (Berlin: Springer­
Verl ag, 1981). 
8. C. Mohan, B. Lindsay, and R. Obermarck, 
"Transaction Management in the R* Distributed 
Database Management System ," ACM Trans­
actions on Computer Systems, vol. 11, no. 4 
(December 1986). 
9. 
C. Mohan and B. Lindsay, "Efficient Commit 
Protocol for the Tree of Processes Model of 
Distributed Transact ions," Proceedings of the 
2nd ACM SIGACT/SIGOPS Symposium on Prin­
ciples of Distributed Computing (Montreal, 
August 1983). 
10. D. Duchamp, "Analysis of Transaction Manage­
ment Performance," Proceedings of the Twelfth 
ACM Symposium on Operating Systems Prin­
ciples (Special issue), vol. 23, no. 5 (December 
1989): 177- 190. 
11. N. Kronenberg, H .  Levy, and W Strecker, 
"VAXclusters: A Closely-Coupled Distributed 
System," AOH Transactions on Computer 
Systems, vol. 4, no. 2 (May 1986). 
Vol. 3 No. 1 
Winter 1991 
Digital Technical journal 
Walter H. Kohler 
Yun-Ping Hsu 
Thomas K. Rogers 
Wael H. Bahaa-El-Din 
Performance Evaluation 
of Transaction Processing 
Systems 
Performance and price/performance are important attributes to consider when 
evaluating a transaction processing system. Two major approaches to performance 
evaluation are measurement and modeling TPC Benchmark A is an industry stan­
dard benchmark for measuring a transaction processing systems performance and 
price/perfmmance. Digital has implemented TPC Benchmark A in a distributed 
transaction processing environment. Benchmark measurements were performed 
on the VAX 9000 Model 210 and the VAX 4000 Mode/300 systems. Further, a compre­
hensive analytical model was developed and customized to model the peCformance 
behavior of TPC Benchmark A on Digital's transaction processing platforms. This 
model was validated using measurement results and has proven to be an accurate 
petformance prediction tool. 
Transaction process ing systems are complex i n  
nature a n d  are usual l y  characterized b y  a large 
number of interactive termi nals and users, a large 
volume of on-li ne data and storage devices, and a 
high volume of concurrent and shared database 
accesses. Transaction processing systems require 
layers of software components and hardware 
devices to work in concert. Performance and 
price/performance are two important attributes 
for customers to consider when selecting trans­
action processing systems. Performance is impor­
tant because transaction processing systems are 
frequently used to operate the customer's business 
or handle mission-critical tasks. Therefore, a certain 
level of throughput and response time guarantee 
are required from the systems during normal oper­
ation. Price/performance is the total system and 
maintenance cost in dollars, normal ized by the per­
formance metric. 
The performance of a transaction p rocessi ng 
system is often measured by i ts throughput in trans­
actions per second (TPS) that satisfies a response 
t ime constraint. For example, 90 percent of the 
transactions must have a response t ime that is less 
than 2 seconds. This throughput, qualified by the 
associated response time constraint, is called the 
maximum qualified t hroughput (MQTh). In a trans­
action processing environment, the most mean­
ingful response time definition is the end-to-end 
Digital Tecbllical]ournal 
Vol 
. .3 No. I 
Winter I<J91 
response time, i.e., the response t ime observed by 
a user at a terminal. The end-to-end response t ime 
represents the time required by all components 
that compose the transaction processing system. 
The two major approaches used for evaluating 
transaction processi ng system performance are 
measurement and model i ng. The measurement 
approach is the most realistic way of evaluating the 
performance of a system. Performance measure­
ment results from standard benchmarks have been 
the most accepted form of performance assess­
ment of transaction processing systems. However, 
due to the complexity of transaction processing 
systems, such measurements are usually very expen­
sive, very t ime-consu ming, and difficult to perform. 
Modeling uses simulation or analyt ical model­
i ng techniques. Compared to t he measurement 
approach, model ing makes it easier to produce 
results and requires less computing resources. 
Performance models are also flexible. Models can 
be used to answer "what-if" types of questions and 
to provide insights into the complex performance 
behavior of transaction processing systems, which 
is difficult (if not impossi ble) to observe in the 
measurement environment. Performance models 
are widely used in research and engineering com­
munities to provide valuable analysis of design 
alternatives, architecture evaluation, and capacity 
planni ng. Simpl ifying assumpt ions are usually 
45 
Transaction Processing, Databases, and Fault-tolerant Systems 
made in the modeling approach. Therefore, perfor­
mance models require validation, through deta iled 
s imulation or measurement, before p redictions 
from the models are accepted. 
The benchmark can be run in either a local 
area network (LAN) or a wide area network (WAN) 
configurat ion. The related t hroughput metrics 
are tpsA-Local and tpsA-Wide, respectively. The 
benchmark specification defines the general appli­
cation requirements, database design and scaling 
rules, testing and pricing guide! ines, full d isclo­
sure report requirements, and an audit checklist.' 
The following sections provide an overview of 
the benchmark. 
This paper presents Digital's benchmark measure­
ment and modeling approaches to transaction 
processi ng system performance evaluation. The 
paper i ncludes an overview of the current industry 
standard transaction processing benchmark, the 
TPC Benchmark A, and a descript ion of Digital's 
implementation of the benchmark, including the 
distinguishing features of the implementation and 
the benchmark methodology. The performance 
measurement results that were achieved by using 
the TPC &nchmark A are also presented . Finally, a 
multilevel analytical model of the performance 
behavior of transaction processing systems with 
response time constraints is presented and vali­
dated agai nst measurement results. 
Application Environment 
The TPC Benchmark A workload is patterned after a 
simplified banking application. In this model, the 
bank contains one or more branches. Each branch 
has 10 tellers and 100,000 customer accounts. A 
transaction occurs when a teller enters a deposit 
or a withdrawal for a customer aga inst an account 
at a branch locat ion. Each teller enters transactions 
at an average rate of one every 10 seconds. Figure I 
illustrates this simplified banking environment. 
TPC Benchmark A-An Overview 
The TPC Benchmark A simulates a simple banking 
environment and exercises key components of 
the system under test (SUT) by using a s imple, 
update-intensive transaction type. The benchmark 
is i ntended to simulate a class of t ransaction pro­
cessing application environments, not the entire 
range of transaction processi ng environments. 
Nevertheless, the single transaction type specified 
by the TPC &nchmark A standard provides a simple 
and repeatable unit of work. 
Transaction Logic 
The transaction logic of the TPC Benchmark A 
workload can be described in terms of the bank 
environment shown in Figure 1. A teller deposits 
in or withdraws money from an account, updates 
the current cash position of t he teller and branch, 
and makes an entry of the transaction in a history 
file. The pseudocode shown in Figure 2 represents 
the t ransaction. 
46 
ß- - - - - - - - ,  
̮- - - - - - - - ,  
ß- - - - - - - - ,  
I 
1 oo,ooo 
I 
1 
1 oo,ooo 
I 
1 
1 oo.ooo 
I 
ACCOUNTS 
1 
I 
ACCOUNTS 
1 
I 
ACCOUNTS 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
1--+--t----I 
-+ . . .  ŷ 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
I 
1 
1 0  
1 0  
I 
1 
1 0  
I 
TELLERS 
TELLERS 
I 
I 
TELLERS 
I 
I 
I 
I 
I 
I 
: 
CUSTOMERS 
I : 
CUSTOMERS 
: 
: 
CUSTOMERS 
L - - - - - - - Ÿ  
L - - - - - - - Ź  
L - - - - - - - ź  
Figure 1 
TPC Benchmark A Banking Environment 
Vol. 3 No. 1 
Winter 1991 
Digital Technical journal 
Performance Evaluation of Transaction Processing Systems 
R e a d  1 0 0 
b y t e s  
i n c l u d i n g 
B i d ,  T i d , 
A i d , 
D e l t a  f r o m  
t e r m i n a l  
B E G I N  T R A N S A C T I O N  
U p d a t e  A c c o u n t  
w h e r e  A c c o u n t _ I D 
= 
A i d :  
R e a d  A c c o u n t _B a l a n c e  f r o m  
A c c o u n t  
S e t  
A c c o u n t  
B a l a n c e  
= 
A c c o u n t  B a l a n c e  
+ 
D e l t a  
W r i t e 
A c c o u n t  B a l a n c e  t o  A c c o u n t  
W r i t e  
t o  H i s t o r y : 
A i d ,  T i d , 
B i d ,  
D e l t a ,  T i m e_ S t a m p  
U p d a t e  T e l l e r  w h e r e  
T e l l e r_ I D 
= 
T i d :  
S e t  
T e l l e r  B a l a n c e  
= 
T e l l e r  B a l a n c e  + 
D e l t a 
W r i t e  T e l l e r  B a l a n c e  t o  T e l l e r  
U p d a t e  B r a n c h  w h e r e  B r a n c h_I D 
= 
B i d :  
S e t  
B r a n c h  B a l a n c e  
= 
B r a n c h_B a l a n c e  
+ 
D e l t a  
W r i t e  B r a n c h _ B a l a n c e  t o  B r a n c h  
C O M M I T  T R A N S A C T I O N 
W r i t e  2 0 0 
b y t e s  
i n c l u d i n g  A i d ,  
T i d , 
D e l t a ,  A c c o u n t  B a l a n c e  
t o  t e r m i n a l 
Figure 2 
TPC Benchmark A Transaction Pseudocode 
Terminal Communication 
For each transaction, the originating terminal is 
required to transmit data to, and receive data from, 
t he system under test. The data sent to the system 
under test must consist of at least 100 alphanumeric 
data bytes, organized as at least four d istinct fields: 
Account_ID, Teller_ID, Branch_I D, and Delta. The 
Branch_ID identifies the branch where the teller is 
located . The Delta is the amount to be credited to, 
or debited from, the specified account. The data 
received from the system under test consists of at 
least 200 data bytes, organized as the above four 
input fields and the Account_Balance that results 
from the successful comm it operation of the 
transaction. 
Implementation Constraints 
The TPC Benchmark A imposes several condi tions 
on the test environment. 
• 
The transaction processing system must support 
atomicity, consistency, isolation, and durability 
(ACI D) properties during the test. 
• 
The tested system must preserve the effects of 
committed transactions and ensure database 
consistency after recovering from 
-
The fa ilure of a single durable medium that 
contains datatbase or recovery log data 
-
The crash and reboot of the system 
-
The loss of all or part of memory 
Digital TecbtRical ]ourttal 
Vol. 3 No. I 
\Vittter 1991 
• 
Eighty-five percent of the accounts processed 
by a teller must belong to the home branch (the 
one to which the teller belongs). Fifteen percent 
of the accounts processed by a teller must be 
owned by a remote branch (one to which the 
teller does not belong). Accounts must be uni­
formly d istributed and randomly selected. 
Database Design 
The database consists of four individual files/tables: 
Branch, Tel ler, Account, and History, as defined in 
Table 1 .  The overal l size of the database is deter­
mined by the throughput capacity of the system. 
Ten tellers, each entering transactions at an aver­
age rate of one transaction every 10 seconds, gener­
ate what is defined as a one-TPS load . Therefore, 
each teller contributes one-tenth (1/10) TPS. The 
history area must be large enough to store the his­
tory records generated during 90 eight-hour days 
of operation at the published system TPS capacity. 
For a system that has a processing capacity of 
x TPS, the database is sized as shown in Table 2. 
For example, to process 20 TPS, a system must 
use a database that includes 20 branch records, 200 
teller records, and 2,000,000 account records. 
Because each teUer uses a term inal, the price of the 
system must i nclude 200 term inals. A test that 
results in a higher TPS rate is invalid un less the size 
of the database and the number of termi nals are 
increased proportionately. 
47 
Transaction Processing, Databases, and Fault-tolerant Systems 
Table 1 
Database Entities 
Record 
Bytes 
Fields Required 
Description 
Branch 
1 00 
Branch_ID 
Branch_ Balance 
Identifies the branch across the range of branches 
Contains the branch's current cash balance 
Teller 
1 00 
Teller_ID 
Branch_ID 
Teller _Balance 
Identifies the teller across the range of tellers 
Identifies the branch where the teller is located 
Contains the teller's current cash balance 
Account 
1 00 
Account_ID 
Branch_ID 
Account_Balance 
Ident ifies the customer account uniquely for the entire database 
Identifies the branch where the account is held 
Contains the account's current cash balance 
History 
50 
Account_ID 
Teller_ID 
Branch_ID 
Amount 
Identifies the account updated by the transaction 
Identifies the teller i nvolved in the transaction 
Identifies the branch associated with the teller 
Contains the amount of credit or debit (delta) specified by 
the transaction 
Time_ Stamp 
Contai ns the date and time taken between the BEGIN 
TRANSACTION and COMMIT TRANSACTION statements 
Table 2 
Database Sizi ng 
Number of Records 
1 X X  
1 0  X X  
1 QQ,QQQ X X 
2,592,000 X X 
Benchmark Metrics 
Record Type 
Branch records 
Teller records 
Account records 
History records 
TPC Benchmark A uses two basic metrics: 
• 
Transactions per second (TPS) - throughput in 
TPS, subject to a response time constra int, i.e. , 
the MQTh, is measured whi le the system is in a 
susta i nable steady-state cond ition. 
• 
Price per TPS (K$/TPS) - the purchase price 
and five-year maintenance costs associated with 
one TPS. 
Transactions per Second 
To guarantee that the 
tested system provides fast response to on-line 
users, the TPC Benchmark A imposes a specific 
response time constraint on 
the 
benchmark. 
Ninety p e rcent of all transactions must have a 
response time of less t han two seconds. The TPC 
Benchmark A standard defines transaction response 
time as the time interval between the trans m ission 
from the terminal of the first byte of the input mes­
sage to the system under test to the arrival at the 
term inal of the last byte of the outpu t message 
from the system under test. 
The reported TPS is the total nu mber of com m i t­
ted transactions that both started and completed 
48 
during an i nterval of steady-state performance, 
d ivided b y  the elapsed time of the i nterval. The 
steady-state measurement i nterval must be at least 
15 m inures, and 90 percent of the transactions 
must have a response time of less t han 2 seconds. 
Price per TPS 
The K$/TPS price/performance 
metric measures the total system price in thou­
sands of dollars, normalized by the TPS rating of 
the system. The priced system i ncludes all the 
components that a customer requires to achieve 
the reported performance level and is defined by 
the TPC Benchmark A standard as the 
• 
Price of the system under test, including all hard­
ware, software, and ma i ntenance for five years. 
• 
Price of the terminals and n etwork compo­
nents, and their maintenance for five years. 
• 
Price of on-line storage for 90 days of history 
records at the publ ished TPS rate, which amounts 
to 2,592,000 records per TPS. A storage medium 
is considered to be on-line if any record can be 
accessed randomly within one second. 
• 
Price of addi tional products required for the 
operation, adm i n istration, or maintenance of 
the priced systems. 
• 
Price of pro d ucts required for application 
development. 
Al l hardware and software used in the tested 
configuration must be announced and general l y  
ava ilable to customers. 
ViJI. 3 No. I 
Winter /991 
Digital Technical journal 
Performance Evaluation of Transaction Processing Systems 
TPC Benchmark A Implementation 
Digital's implementation of the TPC Benchmark A 
goes beyond the minimum requirements of the 
TPC Benchmark A standard and uses Digital's d is­
tribu ted approach to transaction processing.' For 
example, D igital's TPC Benchmark A implementa­
t ion i ncludes forms management and transaction 
processing monitor software that are required in 
most real t ransact ion processing environments 
but are not required by the benchmark. The fol­
lowing sections provide an overview of D igital's 
approach and implementation. 
Transaction Processing Software 
Environment 
The three basic functions of a general-purpose 
transaction processing system are the user inter­
face (forms processing), applications management, 
and database management. Digital has developed a 
distributed transaction architecture (DECdta) to 
define how the major functions are partitioned 
and supported by components that fit together to 
form a complete transaction processing system. 
Table 3 shows the software components in a typical 
D igital transaction processing environment. 
Distributed Transaction Processing 
Approach 
D igital transaction processi ng systems can be d is­
tributed by placing one or more of the basic system 
functions (i.e. , user interface, application manager, 
BACK-END 
PROCESSORS 
1---
AP
_P_L_
IC
_
A_
T_
IO_N
_
-1 
TP MONITOR 
DATABASE 
OPERATING SYSTEM 
COMMUNICATIONS 
Table 3 
Transaction Processing Software 
Components 
Component 
Operat ing system 
Communications 
Database 
TP monitor 
Forms 
Appl ication 
Example 
VMS 
LAT, DECnet 
VAX RdbNMS 
VAX ACMS, DECintact 
DECforms 
COBOL 
database manager) on separate computers. In the 
simplest form of a d istributed transaction process­
i ng system, the user interface component runs on a 
front-end processor, and the application and data­
base components run on a back-end processor. The 
configuration allows terminal and forms manage­
ment to be performed at a remote location, whereas 
the application is p rocessed at a central location. 
The D igital transaction processing software com­
ponents are separable because their clearly defined 
interfaces can be layered transparently onto a net­
work. How these components may be part i tioned 
in the D igital d istributed transaction processing 
environment is i llustrated in Figure 3. 
TPC Benchmark A Test Environment 
The D igital TPC Benchmark A tests are imple­
mented in a d istributed transaction processing 
environment using the transaction processing 
FORMS 
TP MONITOR 
OPERATING SYSTEM 
COMMUNICATIONS 
DATABASE 
STORAGE 
FRONT-END 
PROCESSORS 
Figure 3 
Distributed Transaction Processing Environment 
Digital Technical journal 
Vol. 3 No. I 
Winter 1')91 
49 
Transaction Processing, Databases, and Fault-tolerant Systems 
software components shown in F igure 3. The user 
interface component runs on one or more front­
end processors, whereas the appl ication and 
database components run on one or more back­
end processors. Transactions are entered from 
teller termi nals, which communicate with the 
front-end p rocessors. The front-end processors 
then communicate with the back-end processors 
to invoke the appl ication servers and perform 
database operations. The communications can 
take place over either a local area or a wide area 
network. However, to s implify testing, the TPC 
Benchmark A standard allows sponsors to use 
remote ter minal emulators (RTEs) rather than real 
term i nals. Therefore, the TPC Benchmark A tests 
base performance and price/performance results 
on two distinctly configured systems, the target 
system and the test system. 
The target system is the configuration of hard­
ware and software components that customers can 
use to perform transaction processing. With the 
Digital distributed transaction processing approach, 
user terminals initiate transactions and com muni­
cate with the front-end processors. Front-end pro­
cessors communicate with a back-end processor 
using the DECnet protocol. 
The test system is the configuration of com­
ponents used i n  the lab to measure the perfor­
mance of the target system. The test system uses 
RTEs, rather than user termi nals, to generate the 
workload and measure response time. (Note: In 
previously published reports, based on D igital's 
DebitCredi t  benchmark, the RTE emulated front­
end processors. In the TPC Benchmark A standard, 
the RTE emulates only the user terminals.) The 
RTE component 
• 
Emulates the behavior of terminal users accord­
ing to the benchmark specification (e.g., think 
time, transact ion parameters) 
• 
Emulates term inal devices (e.g., conversion 
and mult iplexi ng into the local area t ransport 
[LAT) protocol used by the OECserver terminal 
servers) 
• 
Records transaction messages and resp onse 
t imes (e.g., the starting and end i ng times of 
individual transactions from each emulated 
termi nal device) 
Figure 4 depicts the test system configuration in 
the LAN environment with one back-end proces­
sor, multiple front-end processors, and multiple 
remote terminal emulators. 
so 
DATABASE 
Figure 4 
Test System Configuration 
TPC Benchmark A Results 
We now present the results of two TPC Benchmark 
A tests based on audited benchmark experiments 
performed on the VAX 9000 Model 210 and the 
VAX 4000 Model 300 systems.' ' These two systems 
are representative of Digital's large and small trans­
action p rocessing platforms. The benchmark was 
implemented using the VAX ACMS transaction p ro­
cessi ng monitor, the VAX Rdb/YMS relational data­
base management system, and the DECforms forms 
management system on the VMS operating system. 
Tables 4 and 5 show the back-end system configu­
rations for the VAX 9000 Model 210 and the VAX 4000 
Model 300 systems, respectively. Table 6 shows the 
system configuration of the front-end systems. 
Measurement Results 
The maximum qualified throughput and response 
time results for the TPC Benchmark A are summa­
rized in Table 7 for the Vч'\ 9000 Model 210 and the 
VAX 4000 Model 300 systems. Both configurations 
have sufficient m a in memory and disk drives such 
Table 4 
VAX 9000 Model 21 0 Back-end 
System Configuration 
Component 
Product 
Quantity 
Processor 
VAX 9000 Model 21 0 
1 
Memory 
256 MB 
Tape drive 
TA81 
1 
Disk contro ller 
KDM70 
2 
Disks 
RA92 
1 6  
Operat ing system 
VMS 5.4 
Communications 
DECnet-VMS Phase IV 
TP monitor 
VAX ACMS V3.1 
Dictionary 
VAX COD/Plus V4.1 
Appl ication 
VAX COBOL V4.2 
Database system 
VAX RdbNMS V4.0 
Forms management DECforms V1 .2 
Vol. 3 No. I 
Winter I<)') I 
Digital Tech11ical jour11al 
Performance Evaluation of Transaction Processing Systems 
Table 5 
VAX 4000 Model 300 Back-end 
System Configuration 
Component 
Product 
Quantity 
Processor 
VAX 4000 Model 300 
Memory 
64 MB 
Tape drive 
TK70 
1 
Disk controller 
DSSI 
3 
Disks 
RF31 
1 8  
Operat i ng system 
VMS 5.4 
Communications 
DECnet-VMS Phase IV 
TP monitor 
VAX ACMS V3.1 
Dictionary 
VAX CDD/Pius V4.1 
Application 
VAX COBOL V4.2 
Database system 
VAX RdbNMS V4.0 
Forms management 
DECforms V1 .2 
that the processors are effectively utilized with no 
other bottleneck. Both systems achieved well over 
90 percent CPU utilization at the maximum quali­
fied throughput under the response time constraint. 
In addi t ion to the throughput and response time, 
the TPC Benchmark A specification requires that 
several other data points and graphs be reported. 
We demonstrate these data and graphs by using 
the VAX 9000 Model 210 TPC Benchmark A results. 
• 
Response Time in Relationship to TPS. Figure 5 
shows the ninet ieth percenti le and average 
2.0 
(j) 
0 
z 
1 .8 
0 
1 .6 
(.) 
IJ.J 
̭ 
1 .4 
IJ.J 
::; 
1 .2 
f= 
IJ.J 
1 .0 
rn 
z 
0.8 
0 
c._ 
rn 
0.6 
IJ.J 
a: 
0.4 
20 
30 
40 
50 
60 
70 
80 
TRANSACTIONS PER SECOND 
KEY: 
t::,--{:,. AVERAGE 
..__... 
90TH PERCENTILE 
Figure 5 
VAX 9000 Response Time in 
Relationship to Transactions 
per Second 
response times at 100 percent and approximately 
80 percent and 50 percent of the maximum 
qualified throughput. The mean t ransaction 
response t ime sti l l  grows linearly with the 
transaction rate up to the 70 TPS level, but the 
ninetieth percentile response t ime curve has 
started to rise quickly due to the high CPU uti­
lization and random arrival of transactions. 
• 
Response Time Frequency Distribution. Figure 6 
is a graphical representation of the transaction 
Table 6 
Front-end Run-time System Configuration 
Component 
Product 
Quantity 
Processor 
VAXserver 31 00 Model 1 0 
1 0 for VAX 9000 back-end 
Memory 
Disks 
Operating system 
Communications 
TP monitor 
Forms management 
RZ23 (1 04 MB) 
VMS 5.3 
VMS 5.4 
DECnet-VMS Phase IV 
VAX ACMS V3.1 
DECforms V1 .2 
Table 7 
Maximum Qual ified Throughput 
3 for VAX 4000 back-end 
1 6 M B for VAX 9000 back-end 
1 2 M B for VAX 4000 back-end 
1 6  
1 for VAX 9000 back-end 
1 for VAX 4000 back-end 
1 
Response Time (seconds) 
System 
TPS (tpsA-Local) 
Average 
90 percent 
Maximum 
VAX 9000 Model 21 0 
VAX 4000 Model 300 
69.4 
21 .6 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
1 .20 
1 .39 
1 .74 
1 .99 
5.82 
4.81 
51 
Transaction Processing, Databases, and Fault-tolerant Systems 
(/) 
1 4000 
z 
0 
f= 
0 
<{ 
(/) 
z 
<{ 
[[ 
f-
1 2000 
1 0000 
8000 
" 
6000 
ffi 
4000 
CD 
3 
2000 
z 
I+- AVERAGE = 1 .20 SECONDS 
I I 
I I 
I I 
I 
I 
I I  
I 
I 
90TH PERCENTILE = 1 .74 SECONDS 
MAXIMUM = 5.82 SECONDS 
0 
2 
4 
6 
8 
1 0  
12 
14 
16 
18 
20 
RESPONSE TIME (SECONDS) 
Figure 6 
VAX 9000 Response Time Frequency 
Distribution 
response time distribu t ion. The average, n ine­
tieth percentile, and max imum transaction 
response times are also marked on the graph. 
• 
Transactions per Second over Time. The resul ts 
shown in Figure 7 demonstrate the sustainable 
maximum qualified throughput. The one-minute 
running average transaction throughputs dur­
ing the warm-up and data col lection periods of 
the experiment are plotted on the graph. This 
graph shows that the throughput was steady 
during the period of data collection. 
• 
Ave rage Response Time over Time. The results 
shown in Figure 8 demonstrate the sustain­
able average response time in the experiment. 
The one-minute running average t ransaction 
response times d uring the warm-up and data 
collection periods of the experiment are plotted 
on the graph. This graph shows that t he mean 
response time was steady during the period of 
data col lection. 
Comprehensive Analytical Model 
Model i ng techn iques can be used as a supplement 
or an alternative to the measurement approach. 
The performance behavior of complex transact ion 
processing systems can be characterized by a set of 
parameters, a set of performance metrics, and the 
relationships among them. These parameters can 
be used to describe the different resources ava i l­
able in the system, the database operations of trans­
actions, and the workload that the transaction 
processing system u ndergoes. To completely rep­
resent such a system, the size of t he parameter set 
would be too huge to manage. An analyt ical model 
simplifies, through abstraction, the complex behav­
ior of a system into a manageable set of parameters 
'52 
0 
z 
0 
0 
w 
(/) 
[[ 
w 
0.. 
(/) 
z 
0 
f= 
0 
<{ 
(/) 
z 
<{ 
[[ 
f-
80 
70 
60 
50 
40 
30 
20 
1 0  
0 
5 
1 0  
I- DATA COLLECTION -! 
I 
INTERVAL 
I 
I 
I 
I 
I 
I 
I 
1 5  
20 
25 
30 
TIME (MI NUTES) 
Figure 7 
VAX 9000 Transactions per Second 
ouer Time 
35 
and pol icies. Such a model, after proper validation, 
can be a powerful tool for many types of analysis, 
as well as a performance pred iction tooL Results 
can be obtai ned quickly for any combination of 
parameters. 
A comp rehensive analyt ical model of the perfor­
mance behavior of transaction processi ng systems 
with a response t ime constrai n t  was developed 
and validated aga inst measurement results. This 
model is hierarchical and flexible for extension. 
The fol lowi ng sections describe the basic con­
struction of the model and the customization made 
to model the execution of TPC Benchmark A on 
D igital's 
transaction 
processi ng 
systems. 
The 
model can also be used to study d ifferent trans­
action processing workloads in addit ion to the 
TPC Benchmark A .  
Response Time Components 
The main metric used in the model is the maxi­
mum qualified throughput u nder a response time 
constra int. The response time constra int is in the 
w 
::;;; 
6 
f= 
5 
w 
'Q UJ 4 
O o  
o.. z 
# 8  3 
[[ w  
lli
¼ 2 
<{ 
[[ 
w 
> 
<{ 
0 
Figure S 
I_ DATA COLLECTION -! 
I 
INTERVAL 
I 
i 
I 
I 
I 
1 0  
1 5  
20 
25 
30 
TIME (MINUTES) 
VA..-Y 9000 Auerage Response Time 
ouer Titne 
35 
Vol. 3 No. I 
Winter 1991 
Digital Tee/mica/ journal 
Performance Evaluation of Transaction Processing Systems 
form of "x percent of transaction response times 
are less thany seconds." 
To evaluate throughput under such response time 
constrai nt, the distribution of transaction response 
times is determined by first decomposing the trans­
action response time into nonoverlapping and 
independent components. The distribution of each 
component is then evaluated. Finally, the overall 
transaction response time d istribution is derived 
from the mathematical convolution of the compo­
nent response t ime distributions. 
The logical flow of a transaction i n  a front-end 
and back-end d istributed transaction processing 
system that is used to implement TPC Benchmark A 
is depicted i n  Figure 9. The response time of a 
transaction consists of three basic components: 
front-end p rocessing, back-end processing, and 
communication delays. 
• 
Front-end processing usually incl udes terminal 
1/0 processing, forms/presentation services, and 
communication with the back-end systems. In 
the benchmark experiments, no disk 1/0 activity 
was i nvolved during the front-end p rocessing. 
• 
Back-end processing includes the execution of 
application, database access, concurrency control, 
and transaction commit processing. The back-end 
processing usual ly involves a high degree of con­
currency and many disk 1/0 activities. 
• 
Communication delays primarily include the 
communications between t he user terminal and 
the front-end node, and the front-end and back­
end i nteractions. 
(Note: These response t ime components do not 
overlap with each other.) 
Within the back-end system, the transaction 
response t ime is further decomposed into two 
addi t ional components, CPU delays and non-CPU, 
nonoverlappi ng delays. CPU delays include both 
the CPU service and the CPU waiting t imes of trans­
actions. Non-CPU, nonoverlapping delays include: 
• 
Logging delays, which i nclude the t ime for trans­
action log writes and commit protocol delays 
• 
Database 1/0 delays, which include both waiting 
and service t imes for accessi ng storage devices 
• 
Other delays, which include delays that result 
from concurrency control (e.g., waiting for locks) 
and waiting for messages 
Two-level Approach 
The model is configured i n  a two-level hierarchy, a 
high level and a detailed level. The use of a hierarchy 
allows a complex and detai led model that considers 
many components and involves many parameters 
to be constructed easily. Because of the hierarchical 
approach, the model also provides flexibility for 
modifications and extensions, and validation of 
separate submodels. 
The high-level model assumes the decomposition 
of transaction response times, as described in the 
Response Time Components section, and models 
the behavior of the transaction processing system 
by an open queuing system, as shown in Figure 10. 
The queuing system consists of servers and delay 
centers, which are connected in a queuing net­
work with the fol lowing assumptions: 
• 
The front-end processing does not i nvolve any 
d isk 1/0 operation, and the load on the front­
end systems is equally balanced. 
.... ..... ..... 1 
I COMMUNICATION I FRONT-END I COMMUNICATION I 
BACK-END 
END-TO-END ----------------------------- 
RESPONSE 
TIME 
Figure 9 
Response Time Components 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
53 
Transaction Processing, Databases, and Fault-tolerant Systems 
COMMUN ICATION 
COMMUNICATION {8 
 : 
DELAYS r 
FRONT-END 
PROCESSORS 
BACK-END 8 
PROCESSORS 
1/0 DEVELOPMENT 
1/0 DEVELOPMENT 
Figure 10 
High-level Queuing Model for a Transaction Processing System 
• The back-end is a shared-memory multiprocessor 
system with symmetrical loads on all processors 
(or it can be simply a uniprocessor). 
• 
No intratransaction parallelism exists within 
i ndividual transaction execution. 
• 
No mutual dependency exists between trans­
action response time components. 
• Transaction arrivals tO the processors have a 
Poisson distribution. 
These assumptions correspond to Digital's TPC Bench­
mark A testing methodology and implementation. 
The front-end CPU is modeled as an M/M/1 queu­
ing center, and the back-end CPU is modeled as an 
M/M/m queui ng center. The transactions' CPU times 
on the front-end and back-end systems are assumed 
to be exponentially distributed (coefficient of vari­
ation equal tO 1) due to the single type of trans­
action i n  the benchmark. (Note: An approximation 
of M/G/m can be used to consider a coefficient of 
variation other than 1 for the back-end transaction 
CPU service time, especially in the multiprocessor 
case when the bus is highly utilized.) Database 1/0, 
logging 1/0, and other delays are modeled as delay 
centers, with appropriate delay distributions. For 
the model of the TPC Benchmark A workJoad, the 
database I/0, journal ing 1/0, and other communi­
cation and synchronization delays are combined 
into one delay center, called the LOD delay center, 
which is represented by a 2-Erlang distribution. 
The major input parameters for this h igh-level 
model are the 
• 
Number of front-end systems and the front-end 
CPU service t ime per transaction 
54 
• 
Number of CPUs in the back-end system and the 
back-end CPU service time per transaction 
• 
Sum of the back-end database 1/0 response time, 
journaling 1/0 response time, and other delay 
times (i.e. , the mean for the LOD delay center's 
2-Erlang distribution) 
• 
Response time constraint (in the form of x per­
centi le less thany seconds) 
The main result from the high-level model is the 
MQTh. This high-level model presents a global pic­
ture of the performance behavior and manifests the 
relationship between the most important parameters 
of the transaction processing system and MQTh. 
Some of the input parameters i n  the h igh-level 
model are dynamic. The CPU service time of a trans­
action may vary with the throughput or number of 
processors, and the database 1/0 or other delays 
may also depend on the throughput. A good exam­
ple of a dynamic model is a tightly coupled multi­
processor system, with one bus interconnecting 
the processors and with a shared common memory 
(e.g. , a VAX 6000 Model 440 system). Such a system 
would run a single copy of the symmetrical multi­
processing operating system (e.g., the VMS system). 
The average CPU service time of transactions is 
affected by both hardware and software factors, 
such as 
• 
Hardware contention that results from conflict­
ing accesses to the shared bus and main memory 
and that causes processor speed degradation 
and longer CPU service t ime. 
• 
Processor synchronization overhead that results 
from the serialization of accesses to shared data 
Vol. 3 No. 1 
Winter 1991 
Digital Technical jounml 
Performance Evaluation of Transaction Processing Systems 
structures. Many operating systems use spin­
locks as the mechanism for processor-level 
synchronization, and the processor spins (i.e., 
busy-waits) in the case of a conflict. In the 
model, the busy-wait overhead is considered 
to be part of the transaction code path, and 
such contention elongates the transaction CPU 
service time. 
Four detailed-level submodels are used to 
account for the dynamic behavior of these param­
eters: CPU-cache-bus-memory, busy-wait, I/0 group, 
and LOD. 
The CPU-cache-bus-memory submodel consists 
of many low-level parameters associated with the 
workload, processor, cache, bus, and memory com­
ponents of multiprocessor systems. It models these 
components by using a m ixed queuing network 
model that consists of both open and closed chains, 
as shown in Figure 11. The most important output 
from this submodel is the average number of CPU 
clock cycles per instruction. 
The busy-wait submodel models the spi n-lock 
contention that is associated with the two major 
VMS spin-locks, called SCHED and IOLOCK8. This sub­
model divides the state of a processor into several 
nonoverlapping states and uses probability analy­
sis to derive busy-wait time. The I/O grouping sub­
model models the group commit and group write 
mechanisms of the VAX Rdb/VMS relational database 
management system. This submodel affects the path 
length of transaction because of the amortization 
of disk I/O processing among grouped trans­
actions. The LOD submodel considers the disk I/0 
times and the lock contention of certain critical 
resources in the VAX Rdb/VMS system. 
Integrating the Two Levels of the Model 
The two levels of the model are integrated by using 
an iterative procedure outlined in Figure 12. It 
starts at the detai led-level submodels, with initial 
values for the MQTh, the transaction path length, 
the busy-wait overhead, and the CPU utilization. 
By applying the initialized parameters to the 
submodels, t he values of these parameters are 
refined and input to the high-level model. The out­
put parameters from the high-level model are then 
fed back to the detailed-level submodels, and this 
iterative process continues u ntil the MQTh con­
verges. In most cases, convergence is reached 
within a few iterations. 
Model Predictions 
The back-end portion of the model was validated 
against 
measurement results from numerous 
DebitCredit benchmarks (Digital's precursor of the 
TPC Benchmark A) on many VAX computers with 
the VMS operating system, running VAX ACMS and 
VAX Rdb/VMS software.1 With sufficient detailed 
parameters available (such as transaction instruc­
tion count, instruction cycle t ime, bus/memory 
access t ime, cache hit ratio), the model correctly 
estimated the MQTh and many intermediate results 
for several multiprocessor VAX systems. The model 
was then extended to i nclude the front-end sys­
tems. In this section, we discuss applying this com­
plete end-to-end model to the TPC Benchmark A 
on two VAX platforms, the VAX 9000 Model 210 and 
the VAX 4000 Model 300 systems, and then compare 
the results. The benchmark environment and imple­
mentation are described in the TPC Benchmark A 
Implementation section of this paper. 
MEMORY 1 
SINK 
®- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -Ŷ 
I 
I 
I 
I 
̬------------
I 
KEY: 
CLOSED CHAIN 
OPEN CHAIN 
SOURCE 
I 
I 
I 
I 
I 
- r  -
- - - - 1  
I 
I 
I 
I 
I 
I 
I 
MEMORY m 
1 
I 
I 
I 
• _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  ! 
Figure 11 
CPU-cache-bus-memory Submodel 
Digital Tecb,tcaljournal 
Vol. 3 No. I 
Winter 1991 
55 
Transaction Processing, Databases, and Fault-tolerant Systems 
I N I T I A L I Z E : 
T x n P L , M Q T h , B u s y W a i t P L , C p u U t i l i z a t i o n ;  
L O D - s u b m o d e l ( i n p u t : M Q T h ; o u t p u t : L O D )  
R E P E A T  
I / 0 - G r o u p i n g - s u b m o d e l ( i n p u t : M Q T h ; o u t p u t : D i o P e r T x n , T x n P L ) ;  
R E P E A T  
R E P E A T  
B u s y W a i t - s u b m o d e l ( i n p u t : T x n P L , B u s y W a i t P L , C p u U t i l i z a t i o n ,  
D i o P e r T x n ; o u t p u t : B u s y W a i t P L ) ;  
U N T I L ( B u s y W a i t P L  c o n v e r g e s ) ;  
C P U - C a c h e - B u s - M e m o r y - s u b m o d e l ( i n p u t : T x n P L , B u s y W a i t P L ;  
o u t p u t : C p u U t i l i z a t i o n , A v g C p u S v c T i m e ) ;  
U N T I L ( C p u U t i  L i z a t i o n 
c o n v e r g e s ) ;  
R E P E A T  
M Q T h - m o d e l ( i n p u t : A v g C p u S v c T i m e , L O D ; o u t p u t : M Q T h , C p u U t i l i z a t i o n ) ;  
L O D - s u b m o d e l ( i n p u t : M Q T h ; o u t p u t : L O D ) ;  
U N T I L ( M Q T h  
c o n v e r g e s ) ;  
U N T I L ( M Q T h  
c o n v e r g e s ) ;  
Figure 12 
Tbe Iterative Procedure to Integrating Submodels 
Because both the VAX 9000 Model 210 and the 
VAX 4000 Model 300 systems are uniprocessor 
systems, there is no other processor contending 
for the processor-memory interconnect and mem­
ory subsystems. Such contention effects can there­
fore be ignored w hen model i ng a uniprocessor 
system. The transaction processing performance 
prediction for the VAX 9000 Model 210 system is a 
successful example of the application of our analyt­
ical model. 
We needed an accurate estimate of TPC Bench­
mark A performance on the VAX 9000 Model 210 
system before a VAX 9000 system was actually avai l­
able for resting. The high-level (MQTh) model was 
used with estimated values for the input parame­
ters, LOD and transaction CPU service time. The 
est imated LOD was based on previous measure­
ment observations from the VAX 6000 systems. The 
other parameter, back-end transaction CPU service 
time, was derived from t he 
• 
Timing information of the VAX 9000 CPU 
• 
Memory access time and cache m iss penalty of 
the VA.'\ 9000 CPU 
• 
Prediction of cache hit ratio of the VAX 9000 sys­
tem under the TPC Benchmark A workload 
• 
Transaction path length of the TPC Benchmark A 
implementation 
• 
Instruction profi le of the TPC Benchmark A 
implementation 
56 
The high- level model predicted a range of MQTh, 
with a high end of 70 TPS and with a strong proba­
bility that the high-end performance was achievable. 
Additional pred ictions were made later, when an 
early prototype version of the VAX 9000 Model 210 
system was ava ilable for testing. A variant of the 
Debi tCredit benchmark, much smaller i n  scale and 
easier to run, was performed on the p rototype 
system, with the emphasis on measuring the CPU 
performance in a transaction processing environ­
ment. The result was used to extrapolate the CPU 
service time of the TPC Benchmark A transactions 
on the VAX 9000 Model 210 system and to refine 
the early estimate. The results of these modifica­
tions supported the previous high-end estimate of 
performance of 70 TPS and refined the low-end 
performance to be 62 TPS. The final, audited TPC 
Benchmark A measurement result of the VAX 9000 
Model 210 system showed 69.4 TPS, which closely 
matches the pred iction. Tab le 8 compares the 
results from benchmark m easurement and the 
analytical model outputs. 
Table 8 
Measurement Compared to Model 
Predictions 
System 
VAX 9000 Model 21 0 
VAX 4000 Model 300 
Measured 
MOTh 
69.4 
21 .5 
Modeled 
MOTh 
70.0 
20.8 
Vol. 3 No. I 
If/inter 1991 
Digital Technical Journal 
The VAX 4000 Model 300 TPC Benchmark A 
results were also used as a validation case. VAX 4000 
Model 300 systems use the same CMOS chip as 
the VAX 6000 Model 400 series and the same 
28-nanosecond (ns) CPU cycle time. However, i n  
the VAX 4000 series, the CPU-memory interconnect 
is not the XMI bus but a direct primary memory 
i nterconnect. This d irect memory interconnect 
results in fast main memory access. The processor, 
cache, and main memory subsystems are otherwise 
the same as in the VAX 6000 Model 400 systems. 
Therefore, the detailed-level model and associated 
parameters for the VAX 6000 Model 410 system 
can be used by ignoring the bus access time. The 
TPC Benchmark A measurement results are within 
7 percent of the model prediction, which means 
that our assumption on the memory access time 
is acceptable. 
Conclusion 
Performance is one of the most important attrib­
utes in evaluating a transaction processing system. 
However, because of the complex nature of trans­
action processing systems, a universal assessment 
of transaction processing system performance is 
impossible. The performance of a transaction pro­
cessing system is workload dependent, configura­
tion dependent, and implementation dependent. A 
standard benchmark, like TPC Benchmark A, is a 
step toward a fair comparison of transaction pro­
cessing performance by different vendors. But it is 
only one transaction processing benchmark that 
represents a l imited class of applications. When 
evaluating transaction processing systems perfor­
mance, a good understanding of the targeted appli­
cation environment and requirements is essential 
before using any ava ilable benchmark result. 
Additional benchmarks that represent a broader 
range of commercial applications are expected to 
be standardized by the Transaction Processing 
Performance Council (TPC) in the com ing years. 
Performance modeling is an attractive alterna­
tive to benchmark measurement because i t  is less 
expensive to perform and results can be compiled 
more quickly. Modeling provides more insight 
into the behavior of system components that are 
treated as black boxes in most measurement exper­
iments. Modeling helps system designers to better 
understand performance issues and to d iscover 
existing or potential performance problems. Model­
i ng also provides solutions for improving perfor­
mance by modeling different tuning or design 
alternatives. The analytical model presented in this 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
Performance Evaluation of Transaction Processing Systems 
paper was validated and used extensively in many 
engineering performance studies. The model also 
helped the benchmark process to size the hard­
ware during preparation (e.g., the number of 
RTE and front-end systems needed, the size of 
the database) and to provide an MQTh goal as a 
sanity check and a tuning a id. The model could 
be extended to represent additional distributed 
configurations, such as shared-d isk and "shared­
nothing" back-end transaction processing systems, 
and could be applied to additional transaction pro­
cessing workloads. 
Acknowledgments 
The Digital TPC Benchmark A implementation and 
measurements are the result of work by many 
individuals within Digital. The authors would like 
especially to thank Jim McKenzie, Martha Ryan, 
Hwan Shen, and Bob Tanski for their work in the 
TPC Benchmark A measurement experiments; and 
Per Gyllstrom and Rabah Mediouni for their con­
tributions to the analytical model and validation. 
References 
1. Transaction Processing Performance Council, 
TPC Benchmark A Standard Specification 
(Menlo 
Park, 
CA: 
Waterside 
Associates, 
November 1989). 
2. Transaction Processing Systems Handbook 
(Maynard: D igital 
Equipment Corporation, 
Order No. EC-H0650-57, 1990). 
3. TPC Benchmark: A Report for the VAX 9000 
Model 210 System (Maynard: Digital Equipment 
Corporation, Order No. EC-N0302-57, 1990). 
4. TPC Benchmark: A Report for the VAX 4000 
Model 300 System (Maynard: Digital Equipment 
Corporation, Order No. EC-N0301-57, 1990). 
5. L. Wright, W Kohler, and W Zahavi, "The Digital 
DebitCredit Benchmark: 
Methodology and 
Results," Proceedings of the International 
Conference on Management and Performance 
Evaluation of Computer Systems (December 
1989): 84-92. 
57 
William Z Zahavi I 
Frances A Habib 
Ketneth J. Omahen 1 
Tools and Techniques for Preliminary 
Sizing of Transaction Processing 
Applications 
Sizing transaction processing systems correctly is a difficult task. By nature, trans­
action processing applications are not predefined and can vmy from tbe simple to 
tbe complex. Sizing during the analysis and design stages of tbe application devel­
opment cycle is particularly difficult. It is impossible to measure tbe resource 
requirements of an application which is not yet written or fully implemented. To 
make sizing easier and more accurate in these stages, a sizing methodology was 
developed that uses measurements from systems on which industry-standard 
benchmarks have been run and employs standard systems analysis techniques for 
acquiring sizing information. These metrics are tben used to predict future trans­
action resource usage. 
The transaction processi ng marketplace is domi­
nated by commercial applications that support 
busi nesses. These applications contribute substan­
tially to the success or fai l ure of a business, based on 
the level of performance the applicat ion provides. 
In transaction processing, poor appl ication perfor­
mance can translate d irectly into lost revenues. 
The risk of implementing a transaction process­
i ng application that performs poorly can be m i n i­
mized by estimating the proper system size in the 
early stages of application development. Sizing esti­
mation includes configuring the correct processor 
and proper number of d isk drives and controllers, 
given the characteristics of the applicat ion. 
The sizing of transaction processing systems is 
a difficult activity. Un l ike tradi tional app l ications 
such as mail, transact ion processing applications 
are not predefi ned. Each customer's requirement 
is d ifferent and can vary from simple to complex. 
Therefore, Digital chose to develop a sizing method­
o logy that specificall y  meets the un ique require­
ments of transact ion processing customers. The 
goal of this effort was to develop sizing tools and 
techniques t hat would help marketing groups and 
design consu ltants in recommen d i ng configura­
tions that meet the needs of D igital's customers. 
Digital's methodology evolved over time, as experi­
ence was gain ed in dealing with the real-world 
problems of transaction process ing system sizing. 
58 
The development of Digital's transaction process­
ing sizing methodology was guided by several prin­
ciples. The first principle is that t he methodology 
should rely heavily upon measurements of Digital 
system s  running i ndustry-standard t ransaction 
process i ng benchmarks. These benchmarks pro­
vide valuable data that quantifies t he performance 
characteristics of d ifferent hardware and software 
configurations. 
The second pri nciple is that systems analysis 
methodologies should be used to provide a frame­
work for acquiring sizing information. In partic­
u lar, a m u lt ilevel view of a customer's business 
is adopted. This approach recogni zes that a man­
ager's view of the business functions performed by 
an organization is different from a computer ana­
lyst's view of the transaction process ing activity. 
The sizing methodology should accommodate both 
these views. 
The third principle is that the s izing methodol­
ogy must employ tools and teclmiques appropriate 
to the current stage of the customer's application 
design cycle. Early in t he effort to develop a sizing 
methodology, i t  was found that a d istinction must 
be made between prel im inary sizi ng and sizing 
during later stages of the application development 
cycle. Preliminary sizing occurs duri ng the analysis 
and design stages of the application development 
cycle. Therefore, no app l i cation software exists 
Vol. 3 No. I 
Wi11ter 1991 
Digital Technical journal 
Tools and Techniques for Preliminary Sizing of Transaction Processing Applications 
which can be measured. Application software does 
exist in later stages of the application development 
cycle, and its measurement provides valuable input 
for more precise s izing activities. 
For example, if a customer is in the analysis or 
design stages of the application development cycle, 
i t  is unlikely that estimates can be obtained for 
such quantities as paging rates or memory usage. 
However, if the application is fully implemented, 
then tools such as the VA.Xcluster Performance 
Advisor (VPA) and the DECcp capacity planning 
products can be used for sizing. These tools pro­
vide facilities for measuring and analyzing data 
from a running system and for using the data as 
input to queuing models. 
The term sizing, as used in this paper, refers to 
preliminary sizing. The paper presents the metrics 
and algebra used in the sizing process for DECtp 
applications. It also describes the individuaJ tools 
developed as part of Digital's transaction process­
ing sizing effort. 
Sizing 
The purpose of sizing tools is twofold. First, sizing 
tools are used to select the appropriate system 
components and to estimate the performance level 
of the system i n  terms of device util ization and 
user response times. Second, sizing tools bridge the 
gap between business specialists and computer 
specialists. This bridge translates the business units 
into functions that are performed on t he system 
and, ultimately, into units of work that can be quan­
tified and measured in terms of system resources. 
In the sections that follow, a number of important 
elements of the sizi ng methodology are described. 
The first of these elements is the platform on which 
the transaction processing system will be imple­
mented. It is assumed that the customer will supply 
general preferences for the software and hardware 
configuration as part of the platform information. 
The Levels of Business Metrics section details the 
multilevel approach used to describe the work per­
formed by the business. The Sizing Metrics and 
Sizing Formu las sections describe the algorithms 
that use platform and business metric i nformation 
to perform transaction processing system sizi ng. 
Platforms 
The term platform is used i n  transaction process­
ing sizing methodology to encompass general cus­
tomer preferences for the hardware and software 
upon which the transaction processing application 
will run. 
Digital Technical journal 
Vol. 3 Nu. I 
Wirzter 1991 
The hardware platform specifies the desired 
topology or processing style. For example, process­
ing style i ncludes a centralized configuration and a 
front-end and back-end configuration as valid alter­
natives. The hardware platform may also include 
specific hardware components within the process­
ing style. (In this paper, the term processor refers 
to the overall processing unit, which may be com­
posed of multiple CPUs.) 
The software platform identifies the set of layered 
products to be used by the transaction processing 
appl ication, with each software product identified 
by its name and version number. In the transaction 
processi ng environment, a software platform is 
composed of the transaction processing moni tor, 
forms manager, database management system, appli­
cation language, and operating system. 
D ifferent combi nations of software platforms 
may be configured, depending on the hardware plat­
form used. A centralized configuration contai ns 
all the software components on the same system. A 
distributed system is comprised of a front -end pro­
cessor and a back-end processor; different software 
platforms may exist on each processor. 
Levels of Business Metrics 
The term business metrics refers collectively to 
the various ways to measure the work associated 
with a customer's business. In this section, various 
levels of business metrics are identified and the 
relationship between metrics at d ifferent levels is 
described.' As mentioned earlier, the levels corre­
spond to the multilevel view of busi ness operation 
typically used for systems analysis. The organi­
zation or personnel most interested in a metric in 
relation to its busi ness operation is noted i n  the 
discussion of each metric. 
The decomposition of the business application 
requirements i nto components that can be counted 
and quantified in terms of resource usage requires 
that a set of metrics be defined. These met rics 
reflect the business activity and the system load. 
The business metrics are the foundation for the 
development of several transaction processing siz­
ing tools and for a consistent algebra that connects 
the busi ness units with the computer units. 
The busi ness metrics are natural forecasting units, 
business functions, t ransactions, and the number 
of I/Os per transaction. The relationship among 
these levels is shown in Figure 1 .  In general, a busi­
ness may have one or more natural forecasting 
units. Each natural forecasting unit may drive one or 
more business functions. A busi ness function may 
59 
Transaction Processing, Databases, and Fault-tolerant Systems 
FILES 
READS 
1/0 ACTIVITY REQUIREMENTS 
INSERTS 
UPDATE 
READS 
UPDATE 
WAITES 
Figure 1 
Levels of Business Activity Characterization 
have multiple transactions, and a si ngle transaction 
may be activated by different business functions. 
Every transaction issues a variety of 1/0 operations 
to one or more fi les, which may be physically 
located on zero, one, or more disks. This section 
discusses the business metrics but does not dis­
cuss the physical distribution of 1/0s across disks, 
which is an implementation-specific item. 
A natural forecasting unit is a macrolevel i ndica­
tor of business volume. (It is also called a key vol­
ume indicator.) A business generally uses a volume 
indicator to measure the level of success of the 
busi ness. The volume is often measured in time 
intervals that reflect the business cycle, such as 
weekly, monthly, or quarterly. For example, if busi­
ness volume indicators were "number of ticket sales 
per quarter," or "monthly production of widgets," 
then the correspond ing natural forecasting units 
would be "ticket sales" and "widgets." Natural fore­
casting units are used by high-level executives to 
track the health of the overall business. 
Business functions are a logical unit of work per­
formed on behalf of a natural forecasting unit. For 
example, within an a irline reservation system, a 
common business function might be "selling air­
l ine tickets." This business function may consist 
of multiple interactions with the computer (e .g. , 
flight i nquiry, customer credit check). The comple­
t ion of the sale termi nates the business function, 
and "airline t icket" acts as a natural forecasting unit 
for the enterprise selling the t ickets. The measure­
ment metric for business functions is the num­
ber of business function occurrences per hour. 
Business functions may be used by midd le-level 
60 
managers to track the activity of their departments. 
A transaction is an atomic unit of work for an 
applicat ion, and transaction response time is the 
primary performance measure seen by a user. Each 
of the interactions mentioned in the above busi­
ness function is a transaction. The measurement 
met ric for a t ransaction is the number of trans­
action occurrences per busi ness function. Trans­
actions may be used by low-level managers to track 
the activity of their groups. 
The bulk of commercial applications i nvolves 
the maintaining and moving of information. This 
information is data that is often stored on perma­
nent storage devices such as rotational disks, solid 
state disks, or tapes. An l/0 operation is the process 
by which a transaction accesses that data. The mea­
surement metric for the I/O profile is the number 
of l/0 operations per transaction. 1/0 operations 
by each transaction are important to programmers 
or system analysts. 
In addi tion to issuing 1/0s, each transaction 
requires a certain amount of CPU time to handle 
forms processi ng. (Forms processi ng t ime is not 
illustrated in Figure 1.) The measurement metric 
for forms processing time is the expected number 
of fields. The number of i nput and output fields 
per form are important metrics for users of a trans­
action processi ng application or programmer/ 
system analysts. 
By collecting information about a transaction 
processing application at various levels, high-level 
volume indicators are mapped to low-level units 
of 1/0 activity. This mappi ng is fundamental to the 
transaction processing sizing methodology. 
Vol. 3 No. I 
Winter 1991 
Digital TechtQicaljourtlal 
Tools and Techniques for Preliminary Sizing of Transaction Processing Applications 
Performance goals play a particularly important 
role in the sizing of transaction processing systems.2 
The major categories of performance goals com­
monly encountered in the transaction processing 
marketplace are bounds for 
• 
Device utilization(s) 
• 
Average response time for transactions 
• 
Response time quantiles for transactions 
For example, a customer might specify a required 
processor utilization of less than 70 percent. Such a 
constraint reflects the fact that system response 
time typically rises dramatically at higher proces­
sor utilizations. A common performance goal for 
response time is to use a transaction 's average 
response time and response t ime quantiles. For 
example, the proposed system should have an aver­
age response t ime of x seconds, with 95 percent 
of all responses complet ing in less than or equal 
to y seconds, where x is less than y. Transaction 
response times are crucial for bus inesses. Poor 
response times translate directly into decreased 
productivity and lost revenues. 
When a customer generates a formal Request For 
Proposal (RFP), the performance goals for the 
transaction processing system typical ly are speci­
fied in deta il. The specification of goals makes 
it easier to define the performance bounds. For 
customers who supply only general performance 
goals, it is assumed that the performance goal takes 
the form of bounds for device util izations. 
Overall response time consists of i ncremental 
contributions by each major component of the 
overall system: 
• 
Front-end processor 
• 
Back-end processor 
• 
Communications network 
• 
Disk subsystem 
A main objective in this approach to sizi ng was 
to identify and use specific metrics that could be 
easily counted for each m ajor component. For 
instance, the number of fields per form could be 
a metric used for sizing front-end processors 
because that number is specific and easily counted. 
As the path of a transaction is fol lowed through the 
overall system, the units of work appropriate for 
each component become clear. These units become 
the metrics for sizing that particular component. 
The focus of this paper is on processor s izing with 
bounds on processor utilization. Processors gener-
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
ally constitute the major expense in any proposed 
system solution. Mistakes in processor sizing are 
very expensive to fix, both in terms of customer 
satisfaction and cost. 
Sizing Metrics 
Transaction processing applications permit a large 
number of users to share access to a common data­
base crucial to the business and usually residing on 
disk memory. In an interactive transaction process­
i ng environment, transactions generally i nvolve 
some number of disk I/O operations, although the 
number is relatively small compared to those 
generated by batch transaction processing appli­
cations. CPU processing also is generally small and 
consists primaril y  of overhead for layered trans­
action processing software products. Although 
these numbers are small, they did i nfluence the 
sizing methodology in several ways. 
Ratings for relative processor capacity in a trans­
action processing environment were developed 
to reflect the ability of a processor to support disk 
1/0 activity (as observed in benchmark tests). In 
addition, empirical studies of transaction process­
i ng applications showed that, for purposes of pre­
lim inary s izing, the number of disk 1/0s generated 
by a transaction provides a good predict ion of the 
required amount of CPU processing.; Numerous 
industry-standard benchmark tests for product 
positioning were run on Digital's processors. These 
processors were configured as back-end proces­
sors in a distributed configuration with different 
software platforms. 
The base workload for this benchmark testing is 
currently the Transaction Processing Performance 
Council's TPC Benchmark A (TPC-A, formerly the 
DebitCredit benchmark)˷·'6 The most complete 
set of benchmark testing was run under Digital's 
VAX ACMS transaction processi ng monitor and 
VAX Rdb/VMS relational database. Therefore, results 
from this software platform on all Digital proces­
sors were used to compute the first sizing metric 
called the base load factor. 
The base load factor is a high- level metric that 
i ncorporates the contribution by all layered soft­
ware products on the back-end processor to the 
total CPU time per 1/0 operation. Load factors are 
computed by dividi ng the total CPU utilization by 
the number of achieved disk 1/0 operations per 
second. (The CPU utilization is normalized in the 
event that the processor is a Symmetrical Multi­
processing [SMP] system, to ensure that its value 
falls within the range of 0 to 100 percent.) The 
61 
Transaction Processing, Databases, and Fault-tolerant Systems 
calculation of load factor yields the total CPU time, 
in centiseconds (hundredths of seconds), required 
to support an appl ication's s ingle phys ical 1/0 
operation. 
The base load factors give the CPU time per 1/0 
required to run the base workload, TPC-A, on any 
Digi tal processor in a back-end configuration using 
the ACMS/Rdb. The CPU time per 1/0 can be esti­
mated for any workload. This generalized metric is 
called the application load factor. 
To relate the base load factors to workloads other 
than t he base, an additional metric was defined 
cal led the intensity factor. The metric calculation 
for the intens ity factor is the application load 
factor divided by the base load factor. The value in 
using intens ity factors is that, once estimated (or 
calculated for ru nning appl icat ions), i ntensi ty fac­
tors can be used to characterize any application in 
a way that can be applied across all processor types 
to estimate processor requirements. 
Intensity factors vary based on the software 
platform used. If a software plattorm other than a 
combined VAX ACMS and VAX Rdb/YMS platform is 
selected, the estimate of the i ntensity factor must 
be adjusted to reflect the resource usage character­
istics of the selected DECtp software platform. 
To estimate an appropriate intensity factor for a 
nonexistent appl ication, judgment and experience 
with similar applications are required. However, 
measured cases from a range of DECtp appl icat ions 
shows relatively little variation in intensity factors. 
Guidelines to help determine intensity factors are 
included in the documentation for Digital's inter­
nal ly developed transaction processing sizing tools. 
The work requ ired by any transaction pro­
cessing application is composed of two parts: the 
appl ication/database and the forms management. 
This division of work corresponds to what occurs 
in a distributed configuration, where the forms pro­
cessing is off-loaded to one or more front-end pro­
cessors. Load factors and intensity factors are 
metrics that were developed to size the application/ 
database. To estimate the amount of CPU time 
required for forms management, a forms-specific 
metric is required. For a first-cut approx imation, 
the expected nu mber of (input) fields is used as the 
sizing metric. This number is obta ined eas ily from 
the business-level descript ion of the application. 
Sizing Formulas 
This section describes the underlying algebra devel­
oped for processor selection. Different formulas 
to estimate the CPU t ime required for both t he 
62 
application/database and forms management were 
developed. These formulas are used separately for 
sizing back-end and front-end processors i n  a d is­
tributed configuration. The ind ividual contribu­
t ions of the formu las are combined for sizing a 
centralized configuration. 
The application/database is the work that takes 
place on the back-end processor of a distributed 
configuration. It is a function of physical d isk 
accesses. To determine the minimal CPU t ime 
required to handle this load, processor utilization 
is used as the performance goal, setting up an 
i nequal ity that is solved to obtain a correspond ing 
load factor. The resulting load factor is then com­
pared to the table of base load factors to obtai n  a 
recom mendation for a processor type. To rein­
force this dependence of load factors on processor 
types, load factor x refers to the associated pro­
cessor type x in the following calcu lations. 
One method for estimating the average CPU time 
per transaction is to multiply the number of 1/0s 
per transaction by the load factor x and the i nten­
sity factor. This yields CPU time per transaction, 
expressed in centiseconds per transaction . By mul­
t iplying this product by the transactions per sec­
ond rate, an expression for processor utilization is 
derived. Thus processor utilization (expressed as a 
percentage scaled between 0 and 100 percent) is 
the number of transactions per second, times the 
number of i/Os per transaction, t imes load factor x, 
times the intensity factor. 
The performance goal is a CPU util ization that is 
less than the util ization specified by the customer. 
Therefore, the calculation used to derive the load 
factor is the utilization percentage provided by the 
customer, divided by the number of transactions 
per second, times the number of l/Os per trans­
action, times the intensity factor. 
Once computed, the load factor is compared to 
those values in the base load factor table. The base 
load factor equal to or Jess than the computed value 
is selected, and its corresponding processor type, 
x, is returned as the mi nimal processor required to 
hand le this workload . 
The four input parameters that need to be esti­
mated for inclusion in this inequality are 
• 
Processor utilization performance goal (tradi­
tionally set at around 70 percent, but may be set 
higher for D igital's newer, faster processors) 
• 
Target transactions per second (which may be 
derived from Digital's multilevel mapping of 
busi ness metrics) 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
Tools and Techniques for Preliminary Sizing of Transaction Processing Applications 
• 
l/Os per transaction (estimated from application 
description and database expertise) 
• 
Intensity factor (estimated from experience with 
similar applications) 
Note: Response time performance goals do not 
appear in this formula. This sizing formula deals 
strictly with ensuring adequate processor capacity. 
However, these performance parameters (includ­
ing the CPU service time per transaction) are fed 
into an analytic queuing solver embedded in some 
of the t ransaction processing sizing tools, which 
produces estimates of response times. 
Forms processing is the work that occurs either 
on the front-end processor of a distributed config­
uration or in a centralized configuration. It is not a 
function of physical disk accesses; rather, forms 
processing is CPU intens ive. To estimate the CPU 
time (in seconds) required for forms processing, 
the following simple linear equation is used: 
y = c(a + bz) 
where y equals the CPU time for forms processing; 
a equals the CPU time per form per t ransaction 
i nstance, depending on the forms manager used; 
b equals the CPU time per field per transaction 
instance, depending on the forms manager used; 
z equals the expected number of fields; and c equals 
the scaling ratio, depending on the processor type. 
This equation was developed by feed ing the results 
of controlled forms testing into a linear regression 
model to estimate the CPU cost per form and per 
field (i.e., a and b). The multiplicative term, c, is 
used to el iminate the dependence of factors a and 
b on the hardware platform used to run these tests. 
Sizing Tools 
Several sizing tools were constructed by using the 
above formulas as starting points. These tools dif­
fer in the range of required i nputs and outputs, and 
in the expected technical sophistication of the user. 
The first tool developed is for quick, first­
approximation processor sizing. Currently embod­
ied as a DECalc spreadsheet, with one screen for 
processor selection and one for transactions-per­
second sensitivity analysis, it can handle back-end, 
front-end, or centralized sizing. The first screen 
shows the range of processors required, given the 
target processor utilization, target transactions 
per second, expected number of fields, and the 
possible intensity factors and number of 1/0s per 
transaction. (Because the estimation of these last 
Digital TecbnicalJourual 
VrJI. 3 No. I 
Winter 1991 
two i nputs generally i nvolves the most uncer­
tainty, the spreadsheet allows the user to input a 
range of values for each.) The second screen turns 
the analysis around, showing the resulting trans­
action-per-second ranges that can be supported by 
the processor type selected by the user, given the 
target processor utilization, expected number of 
fields, and possible i ntensity factors and number of 
1/0s per transaction. 
The basic sizing formula addresses issues that 
deal specifically with capacity but not with per­
formance. To predict behavior such as response 
t imes and queue lengths, modeling techniques that 
employ analytic solvers or simulators are needed. 
A second tool embeds an analytic queuing solver 
within i tself to produce performance estimates. 
This tool is an automated system (i.e., a DECtp 
appl ication) that requests informat ion from the 
user according to the multilevel workload charac­
terization methodology. This starts from general 
business-level i nformation and proceeds to request 
successively more deta i led i nformation about the 
application. The tool also conta ins a knowledge 
base of D igital's product characteristics (e.g., pro­
cessor and disk) and measured DECtp applications. 
The user can search through the measured cases to 
find a similar case, which could then be used to 
provide a starting point for est imating key applica­
t ion parameters. The built-in product characteris­
t ics shield the user from the numeric deta ils of the 
sizing algorithms. 
A third tool is a spin-off from the second tool. 
This tool is a standalone analytic queuing solver with 
a simple textual i nterface. The tool is intended for 
the sophisticated user and assumes that the user 
has completed the level of analysis required to be 
able to supply the necessary technical input param­
eters. No automatic table lookups are provided . 
However, for a completely characterized applica­
t ion, this tool gives the sophisticated user a quick 
means to obta in performance estimates and run 
sensitivity analyses. The complete DECtp software 
platform necessary to run the second tool is not 
required for this tool. 
Data Collection 
To use the sizing tools fully, certa in data must be 
available, which allows measured workloads to be 
used to establish the basic metrics. Guidance in 
sizing unmeasured transaction processing applica­
tions is highly dependent on developi ng a knowl­
edge base of real-world transaction processing 
application descriptions and measurements. The 
63 
Transaction Processing, Databases, and Fault-tolerant Systems 
kinds of data that need to be stored withi n the 
knowledge base require the data collection tools to 
gather information consistent with the transaction 
processing sizing algebra. 
For each transaction type and for the aggregate 
of all the transaction types, the fol lowing i nforma­
tion is necessary to perform transaction process­
i ng system sizing: 
• 
CPU time per disk 1/0 
• 
D isk 1/0 operations per transaction 
• 
Transaction rates 
• 
Logical-to-physical disk 1/0 ratio 
The CPU to 1/0 ratio can be derived from Digital's 
existing instrumentation products, such as the VAX 
Software Performance Monitor (SPM) and VAXcluster 
Performance Advisor (VPA) products.' Both prod­
ucts can record and store data t hat reflects CPU 
usage levels and physical disk 1/0 rates. 
The DECtrace product collects event-driven data. 
It can col lect resource i tems from layered soft­
ware products, including VAX ACMS monitor, the 
VAX Rdb/VMS and DBMS database systems, and if 
instrumented, from the application program itself. 
As an event collector, the DECtrace product can be 
used to track the rate at which events occur. 
The methods for determining the logical-to­
physical disk 1/0 ratio per transaction rema in open 
for continuing study. Physical disk 1/0 operations 
are issued based on logical commands from the 
application. The find, update, or fetch commands 
from an SQL program translate i nto from zero to 
many thousands of physical disk I/O operations, 
depending upon where and how data is stored . 
Characteristics that affect this ratio i nclude the 
length of the data tables, number of index keys, and 
access methods used to reach i ndividual data items 
(i.e., sequential, random). 
Few tools currently available can provide data 
on physical l/0 operations for workloads in the 
design stage. A knowledge base that stores the 
logical-to-physical disk 1/0 activity ratio is the best 
method avai lable at this time for predicti ng that 
value. The knowledge base in the second sizing 
tool is beginning to be populated with application 
descriptions that include this type of information. 
It is anticipated that, as this tool becomes widely 
used in the field, many more applicat ion descrip­
t ions wil l  be stored in the knowledge base. Pooling 
individual application experiences into one central 
repository will create a valuable source of knowl­
edge that may be utilized to provide better infor­
mation for future sizing exercises. 
64 
Acknowledgments 
The authors would like to acknowledge our col­
leagues i n  the Transaction Processing Systems 
Performance Group whose efforts led to the devel­
opment of these sizing tools, either through prod­
uct characterization, system support, objective 
critique, or actual tool development. In particular, 
we would like to acknowledge the contributions 
made by Jim Bouhana to the development of the 
sizi ng methodology and tools. 
References 
1. W Zahavi and ]. Bouhana, "Business-Level Des­
cription of Transaction Processi ng Applications," 
CMG '88 Proceedings (1988): 720 -726. 
2. K. Omahen, "Practical Strategies for Config­
uring Balanced Transaction Processing Systems," 
IEEE COMPCON Spring '89 Proceedings (1989): 
554-559. 
3. W 
Zahavi, 
"A 
First Approximation Sizi ng 
Technique -The 1/0 Operation as a Metric of 
CPU Power," CMG '90 Conference Proceedings 
(forthcoming December 10- 14, 1990). 
4. "TPC BENCHMARK A - Standard Specification," 
(Transaction Processi ng Performance Council, 
November 1989). 
5. "A Measure of Transaction Processing Power," 
Datamation, vol. 31, no. 7 (April 1, 1985): 112- 118. 
6. L. Wright, W Kohler, and W Zahavi, "The Digital 
DebitCredi t  Benchmark: Methodology and 
Results," 
CMG 
'89 Conference Proceedings 
(1989): 84-92. 
7 F Habib, Y. Hsu, and K. Omahen, "Software 
Measurement Tools for VAX/VMS Systems," CMG 
Transactions (Summer 1988): 47-78. 
Vol. 3 No. J 
Winter 1991 
Digital Technical journal 
Ananth Raghavan I 
T. K. Rengarajan 
Database Availability for 
Transaction Processing 
A transaction processing system relies on its database management system to supply 
high availability Digital offers a network-based product, the VAX DBMS system, 
and a relational data-based product, the VAX Rdb/VMS database system, for its 
transaction processing systems. These database systems have several strategies to 
survive failures, disk head crashes, revectored bad blocks, database corruptions, 
memory corruptions, and memory overwrites by faulty application programs. 
They use base hardware technologies and also employ novel software techniques, 
such as parallel transaction recovery, recovery on surviving nodes of a VA.Xcluster 
system, restore and rollforward operations on areas of the database, on-line 
backup, verification and repair utilities, and executive mode protection of trusted 
database management system code. 
Modern businesses store critical data in database 
management systems. Much of the daily activity 
of business i ncludes manipulation of data in the 
database. As businesses extend their operations 
worldwide, t heir databases are shared among 
office locations in d ifferent parts of the world. 
Consequently, these businesses require transac­
tion processing systems to be available for use at 
all times. This requirement translates directly to a 
goal of perfect avai labil ity for database manage­
ment systems. 
VAX DBMS and VAX Rdb/VMS database systems are 
based on network and relational data models, respec­
tively. Both systems use a kernel of code that is 
largely responsible for providing high availability. 
This layer of code is maintained by the KODA group. 
KODA is the physical subsystem for VAX DBMS and 
VAX Rdb/VMS database systems. It is responsible for 
all 1/0, buffer management, concurrency control, 
transaction consistency, locking, journaling, and 
access methods. 
In this paper, we define database avai lability, 
and describe downtime situations and how such 
situations can be resolved. We then discuss the 
mechanisms that have been implemented to pro­
vide minimal loss of avai lability. 
Database Availability 
The unit of work in transaction processing systems 
is a transaction. We therefore define database avail­
ability as the ability to execute transactions. One 
Dtgttal Tecbnicaljournal 
Vol. 3 No. I 
Winter 1991 
way the database management system provides 
high avai lability is by guaranteei ng the proper­
t ies of transactions: atomicity, serializability, and 
durabi lity.1 For example, if a transaction that has 
made updates to the database is aborted, other 
transactions must not be allowed to see these 
updates; the updates made by the aborted trans­
action must be removed from the database before 
other transactions may use that data. Yet, data that 
has not been accessed by the aborted transaction 
must continue to be avai lable to other transactions. 
Downtime is the term used to refer to periods 
when the database is unavailable. Downtime is 
caused by either an u nexpected fai lure (unex­
pected downtime) or scheduled maintenance on 
the database (scheduled downtime). Such classifi­
cations of downtime are useful. Unexpected down­
t ime is caused by factors that are beyond the 
control of the transaction processing system. For 
example, a d isk failure is quite possible at any 
t ime duri ng normal p rocessing of transactions. 
However, scheduled downtime is entirely within 
the control of the database administrator. H igh 
availability demands that we eliminate scheduled 
downtime and ensure fast system recovery from 
unexpected failures. 
The layers of the software and hardware services 
which compose a transaction processing system 
are dependent on one another for high availability. 
The dependency among these services is i llus­
trated i n  Figure 1 .  Each service depends on the 
65 
Transaction Processing, Databases, and Fault-tolerant Systems 
APPLICATION 
PROGRAM 
1 
DATABASE 
MANAGEMENT 
SYSTEM 
I 
OPERATING 
SYSTEM (VMS) 
I 
HARDWARE 
(CPU, DISK) 
1 
GENERAL 
ENVI RONMENT 
AVAILABI LITY 
Figure 1 
Layers of Availability in Transaction 
Processing Systems 
avai lability of the service in the lower layers. 
Errors and fa ilures can occur in any layer, but may 
not be detected immediately. For example, in the 
case of a database management system, the effects 
of a database corruption may not be apparent until 
long after the corruption (error) has occurred . 
Hence it is difficult to deal with such errors. On the 
other hand , fa ilures are noticed immediately. 
Failures usually make the system unavailable and 
are the cause of u nexpected downtime. 
Each layer can provide only as much avai labi lity 
as the immediate lower layer. Hence we can also 
express the perfect-avai lability goal of a database 
management system as the goal of matching the 
ava ilabi lity of the immediately lower layer, which 
in our case is the operating system. 
At the outset, it is clear that a database manage­
ment system layered on top of an operating system 
and hence only as avai lable as the underlying oper­
ating system. However, a database management 
system is in general not as ava ilable as the under­
lying layer because of the need to guarantee the 
properties of transactions. 
Unexpected Downtime 
In this section we discuss the causes of u nex­
pected downtime and the techniques that mini­
m ize downtime. 
66 
A database monitor must be started on a node 
before a user's process running on that node can 
access a database. The monitor oversees all data­
base activity on the node. It allows processes to 
attach to and detach from databases and detects 
fai lures. On detecting a fa ilure, the monitor starts 
a process to recover the transactions that did not 
complete because of the fa ilure. Note that this 
database monitor is different from the TP monitor.' 
Application Program Exceptions 
Although transaction processing systems are based 
on the client/server architecture, Digital's database 
systems are process based. The privi leged database 
management system code is packaged in a share­
able library and l inked with the application pro­
grams. Therefore, bugs i n  the applications have 
a good chance of affecting the consistency of the 
database. Such bugs in applications are one type of 
fai lure that can make the database unavailable. 
The VAX DBMS and VAX Rdb/VMS systems guard 
aga inst this class of failure by executing the data­
base management system code in the VAX execu­
tive mode. Since application programs execute in 
user mode, they do not have access to data struc­
tures used by the database management system. 
When a faulty application program attempts such 
an access, the VMS operating system detects it and 
generates an exception. This exception then forces 
an image rundown of the application program. 
In general, when an image rundown is initiated, 
Digital's database management products use the 
condition-hand ling facility of VMS to abort the trans­
act ion. Condition handling of image rundown is 
performed at two levels. Two cond ition handlers 
are established, one in user mode and the other in 
kernel mode. The user mode exit handler is usual ly 
i nvoked, which rolls back the current transaction 
and unbinds it from the database. In this case, the 
rest of the users on the system are not affected at 
all. The database rema ins ava ilable. The execution 
of the user mode exi t  handler is, however, not 
guaranteed by the VMS operating system. Under 
some abnormal circumstances, the user mode exit 
handlers may not be executed at all. In such cir­
cumstances, the kernel mode exit handler is 
invoked by the VMS system. This handler resides 
in the database monitor. The monitor starts a 
database recovery (DBR) process. It is the responsi­
bility of the DBR process to roll back the effects of 
the aborted transaction. To do this, the DBR pro­
cess first establishes a database freeze. This freeze 
prevents other processes from acquiring locks that 
Vol. 3 No I 
Winter 1991 
Digital Technical Journal 
were held by the aborted transaction and hence 
see and update uncommitted data. (The VMS lock 
manager releases all locks held by a process when 
that process dies.) The DBR process then proceeds 
to roll back the aborted transaction. 
Code Corruptions 
It is important to prevent coding mistakes within 
the DBMS from irretrievably corrupting the data­
base . To protect the database management system 
from cod ing mistakes, internal data structure con­
sistency is examined at different points in the 
code. If any inconsistency is found, a bug-check 
utility is cal led that dumps the internal database 
format to a fi le. The utility then ra ises an excep­
tion that is handled by the monitor, and the DBR 
process is started as described above. 
To deal with corruptions to the database that are 
undetected with this mechanism, an explicit utility 
is provided that verifies the structural consistency 
of the database. This verify utility may be executed 
on-line, while users are still accessing the data­
base. Such verification may also be executed by a 
database adm inistrator (DBA) in response to a bug­
check dump. Once such a corruption is detected, 
an on-line utility provides the ability to repair the 
database. 
In general, corruption in databases causes unex­
pected downtime. D igital provides the means of 
detecting such corruption on-line and repairing 
them on-line through recovery utilities. 
Process Failure 
In the VMS system, a process fa i lure is always pre­
ceded by image rundown of the current image run­
ning as part of the process. Therefore, a process 
fa ilure is detected by the database monitor, which 
then starts a DBR process to handle recovery. 
Node Failure 
Among the many mechanisms Digital provides for 
availability is node fa ilover within a cluster. When 
a node fails, another node on the cluster detects 
the fa ilure and rolls back the lost transactions from 
the failed node. Thus the fa ilure of one node does 
not cause transactions on other active nodes of the 
cluster to come to a halt (except for the t ime the 
DBR process enforces a freeze). It is the database 
monitor that detects node fa ilure and starts a 
recovery process for every lost transact ion on the 
fa iled node. The database becomes available as 
soon as recovery is complete for all the users on 
the fai led node. 
Digital Technical journal 
Vol. 3 No. I 
Winter 1991 
Database Availability for Transaction Processing 
Power Failure 
Power fa i lure is a hardware fai lure. As soon as 
power is restored, the VMS system boots. When a 
process attaches to the database, a number of mes­
sages are passed between the process that is attach­
ing and the monitor. If the database is corrupt 
(because of power fail ure), the monitor is so 
informed by the attaching process, and aga in the 
monitor starts recovery processes to return the 
database to a consistent state. The database becomes 
ava ilable as soon as recovery is complete for all 
such fai led users. 
As described above, recovery is always accom­
plished by the monitor process starting DBR pro­
cesses to do the recovery. The only differences in 
the case of process, node, or cluster fa i l ure is the 
mechanism by which the monitor is informed of 
the failure. 
Disk Head Crash 
Some fa ilures can result i n  the loss or corruption of 
the data on the stable storage device (disk). Digital 
has a mechanism for bringing the database back to 
a consistent state in such cases. 
A disk head cras h is a failure of hardware that is 
usual ly characterized by the inability to read from 
or write to the disk. Hence database storage areas 
residing on that disk are unavailable and possibly 
irretrievable. A disk head crash automatically aborts 
transactions that need to read from or write to that 
disk. In addition, recovery of these aborted trans­
actions is not poss ible since the recovery pro­
cesses need access to the same disk. In this case, 
the database is shut down and access is denied until 
the storage areas on the fa iled disk are brought on­
line. Areas are restored from backups and then 
rolled forward until consistent with the rest of the 
database. The after image journal (AlJ) files are used 
to roll t he areas forward. As soon as all the areas on 
the failed disk have been restored onto a good disk 
and rolled forward, the database becomes available. 
Bad Disk Blocks 
Bad blocks are hardware errors that often are not 
detected when they happen. The bad blocks are 
revectored, and the next t ime the disk block is 
read, an error is reported. Bad blocks simply mean 
that the contents of a disk block are lost forever. 
The database administrator detects the problem 
only when a database appl ication fa ils to fetch data 
on the revectored block. Such an error may cause a 
certain transaction or a set of transactions to fa il, 
no matter how many attempts are made to execute 
67 
Transaction Processing, Databases, and Fault-tolerant Systems 
the transactions. This failure constitutes reduced 
ava ilability; parts of the database are unava i !able to 
transactions. Exactly how much of the database 
remains available depends on which blocks were 
revectored. 
The mechanism provided to reduce the possible 
downtime is early detection. D igital's database 
systems provide a verification utility that can be 
executed while users are running transactions. 
The verification utility checks the structural con­
s istency of the database. Once a bad block is 
detected by such a utility, that area of the database 
may be restored and rolled forward. These two 
operations make the whole database temporarily 
unavai lable; however, the bad block is corrected, 
and future downtime is avoided. The downtime 
caused by the bad block may be traded off agai nst 
the downtime needed to restore and roll forward. 
Site Failure 
A s ite failure occurs when neither the computers 
nor the disks are ava ilable. A site fa ilure is usually 
caused by a natural disaster such as an earthquake. 
The best recourse for recovery is archival storage. 
Digital provides mechanisms to back up the data­
base and AIJ files to tape. These tapes must then be 
stored at a site away from the site at which the 
database resides. Should a disaster happen, t hese 
backup tapes can be used to restore the database. 
However, the recovery may not be complete. It 
cannot restore the effects of those committed trans­
actions that were not backed up to tape. 
After a disaster, the database can be restored 
and rolled forward to the state of the completion of 
the last AIJ that was backed up to tape. Any trans­
actions that committed after the last Al] was backed 
up cannot be recovered at the alternate s ite. Such 
transaction losses can be minimized by frequently 
backing up the AIJ files. 
Memory Errors 
Memory errors are quite i nfrequent, and when 
they happen, they usually are not detected. If the 
error happens to a data record, it may never be 
detected by any utility, but may be seen as i ncor­
rect data by the user. If the verification utility is run 
on-line, it may also detect the errors. Aga in, the 
database may only be partially ava ilable, as in the 
case of bad blocks. However, it is possible to repair 
the database while users are still accessing the 
database. Digital's database management products 
provide explicit repair facilities for this purpose. 
68 
The loss of ava ilability during repair is not worse 
than the loss due to the memory error itself. 
As explained previously, the database monitor 
plays an important part in ensuring database con­
sistency and avai lability. Most unexpected failure 
scenarios are detected by the monitor, which then 
starts recovery processes. In addition, some fa i l­
ures might require the use of backup files to 
restore the database. 
Scheduled Downtime 
Most database systems have scheduled maintenance 
operations that require a database shutdown. Data­
base backup for media recovery and verification to 
check structural consistency are examples of oper­
ations that may require scheduled downtime. In 
this section we describe ways to perform many of 
these operations while the database is executing 
transactions. 
Backup 
Digital's database systems allow two types of trans­
actions: update and "snapshot." The ability to back 
up data on-line depends on the snapshot transaction 
capability of the database. 
Database backup is a standard way of recovering 
from media fa ilures. Digital's database systems pro­
vide the ability to do transaction consistent back­
ups of data on-line while users continue to change 
the database. 
The general scheme for snapshot transactions is 
as fol lows. The update transactions of the database 
preserve the previous versions of the database 
records in the snapshot file. All versions of a data­
base record are cha ined. Only the current version 
of the record is in the database area. The older ver­
sions are kept in the snapshot area. The versions 
of the records are tagged with the transaction 
numbers (TSNs). When a snapshot transaction (for 
example, a database backup) needs to read a data­
base record, it traverses the chain for that database 
record and then uses the appropriate version of 
the record. 
There are two modes of database operation with 
respect to snapshot activity. In one mode, al l update 
transactions write snapshot copies of any records 
they update. In the deferred snapshot mode, the 
updates cause snapshot copies to be written only 
if a snapshot transaction is active and requires old 
versions of a record. In this mode, a snapshot trans­
action cannot start until aU currently active update 
transactions (which are not writing snapshot 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
records) have completed; that is, the snapshot 
transaction must wait for a quiet point in time. If 
there are either active or pend ing snapshot trans­
actions when an update transaction starts, the 
update transaction must write snapshot copies. 
Here we see a trade-off between update trans­
actions and snapshot transactions. The database 
is completely ava ilable to snapshot transactions 
if all update transactions always write snapshot 
copies. On the other hand, if the deferred snapshot 
mode is enabled, update transactions need not 
write snapshot copies if a snapshot transaction 
in not active. This approach obviously resu lts i n  
some loss o f  ava ilabi lity t o  snapshot transactions. 
Verification 
Database corruption can also result in downtime. 
Although database corruption is not probable, it 
is possible. Any database system that supports 
critical data must provide facilities to ensure the 
consistency of the database. D igital's database man­
agement systems provide verification utilities that 
scan the database to check the structural consis­
tency of the database. These utilities may also be 
executed on-line through the use of snapshot 
transactions. 
AI] Backup 
The backup and the AlJ log are the two mechanisms 
that provide media recovery for Digital's database 
management products. The AlJ fi le is continuously 
written to by all user processes updating the data­
base. We need to provide some abil ity to back up 
the AlJ file since it monotonically increases in size 
and eventual ly fi l ls up the disk. Digi tal's database 
Digital Technical]ourrwl 
Vol. 3 Nu. I 
Winter 1991 
Database Availability for Transaction Processing 
systems offer the ability to back up the AlJ file to 
tape (or another device) on-line. The only restric­
tion is that a quiet point must be established for a 
short period during which the backup operation 
takes place. A quiet point is defined as a point 
when the database is quiescent, i.e., there are no 
active transactions. 
On-line Schema Changes 
Digital's database management systems allow users 
to change metadata on-line, whi le users are sti l l  
accessing the database. Although this may be stan­
dard for relational database management systems, 
it is not standard for network databases. The VAX 
DBMS system provides a utility called the database 
restructuring utility (DRU) to allow for on-line 
schema modifications. 
Acknowledgments 
Many engineers have contributed to the develop­
ment of the algorithms described i n  this paper. We 
have chosen not to enumerate all such contribu­
tions. However, we would like to recognize the con­
tributions of Peter Spiro, Ashok Joshi, Jeff Arnold, 
and Rick Anderson who, together with the authors, 
are members of the KODA team. 
References 
1 .  P Bernstein, W Emberton, and V Trehan, 
"DECdta - Digital's Distributed Transaction Pro­
cessing Architecture," Digital Technical journal, 
vol. 3, no. 1 (Winter 1991 , this issue): 10 -17. 
2. T. Speer and M .  Storm, "Digital's Transaction 
Processing Monitors," Digital Technical journal, 
vol. 3, no. 1 (Winter 1991 , this issue): 18-32. 
69 
Peter M. Spiro I 
Ashok M.joshi 
T. K. Rengarajan 
Designing an optimized 
Transaction Commit 
Protocol 
Digital's database products, VAX Rdb/VMS and VAX DBMS, share the same database 
kernel called KODA. KODA uses a grouping mechanism to commit many concurrent 
transactions together. This feature enables high transaction rates in a transaction 
processing (TP) environment. Since group commit processing affects the maximum 
throughput of the transaction processing system, the KODA group designed and 
implemented several grouping algorithms and studied their performance charac­
teristics. Preliminary results indicate that it is possible to achieve up to a 66 percent 
improvement in transaction throughput by using more efficient grouping designs. 
Digital has two general-purpose database products, 
Rdb/VMS software, which supports the relational 
data model, and VAX DBMS software, which sup­
ports the CODASYL (Conference on Data Systems 
Languages) data model. Both products layer on top 
of a database kernel called KODA. In add ition to 
other database services, KODA provides the trans­
action capabi lities and commit processing for these 
two products. 
In this paper, we address some of the issues rele­
vant to efficient commit processing. We begin by 
explaining the importance of commit processing 
in achieving high transaction throughput. Next, we 
describe in deta il the current algorithm for group 
commit used in KODA. We then describe and con­
trast several new designs for perform ing a group 
commit. Following these discussions, we present 
our experimental results. And, final ly, we discuss 
the possible direction of future work and some 
conclusions. No attempt is made to present formal 
analysis or exhaustive empirical results for commit 
processing; rather, the focus is on an intuitive 
understanding of the concepts and trade-offs, 
along with some empirical results that support our 
conclusions. 
Commit Processing 
To fol low a discussion of commit processing, two 
basic terms must first be understood. We begin this 
section by defining a transaction and the "moment 
of commit." 
70 
A transaction is the execution of one or more 
statements that access data managed by a database 
system. General ly, database management systems 
guarantee that the effects of a transaction are atomic, 
that is, either al l updates performed within the con­
text of the transaction are recorded in the database, 
or no updates are reflected in the database. 
The point at which a transaction's effects become 
durable is known as the "moment of commit." This 
concept is important because it allows database 
recovery to proceed in a predictable manner after 
a transaction fa ilure. If a transaction terminates 
abnormal ly before it reaches the moment of com­
mit, then it aborts. As a result, the database system 
performs transaction recovery, which removes al l 
effects of the transaction. However, if the trans­
action has passed the moment of commit, recovery 
processing ensures that al l changes made by the 
transaction are permanent. 
Transaction Profile 
For the purpose of analysis, i t  is useful to divide a 
transaction processed by KODA into four phases: 
the transaction start phase, the data manipulation 
phase, the logging phase, and the commit process­
ing phase. Figure I illustrates the phases of a trans­
action in time sequence. The first three phases are 
collectively referred to as "the average transaction's 
CPU cost (excluding the cost of commit)" and the 
last phase (commit) as "the cost of writing a group 
commit buffer." ' 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
TIME
-
DATA 
MANIPULATION 
Figure 1 
Phases in the Execution 
of a Transaction 
The transaction start phase involves acquiring 
a transaction identifier and setting up control 
data structures. This phase u sually incurs a fixed 
overhead. 
The data manipulation phase involves executing 
the actions dictated by an application program. 
Obviously, the t ime spent in this phase and the 
amount of processing required depend on the 
nature of the application. 
At some point a request is made to complete the 
transaction. Accordingly in KODA, the transaction 
enters the logging phase which involves updating 
the database with the changes and writing the 
undo/redo information to disk. The amount of work 
done in the logging phase is usually small and con­
stant (less than one 1/0) for transaction processing. 
Finally, the transaction enters the commit pro­
cessing phase. In KODA, this phase i nvolves writing 
commit information to d isk, thereby ensuring that 
the transaction's effects are recorded in the data­
base and now visible to other users. 
For some transactions, the data manipulation 
phase is very expensive, possibly requiring a large 
number of 1/0s and a great deal of CPU time. For 
example, if 500 employees in a company were to 
get a 10 percent salary increase, a transaction would 
have to fetch and modify every employee/salary 
record i n  the company database. The commit pro­
cessing phase, in this example, represents 0.2 per­
cent of the transaction duration. Thus, for this class 
of transaction, commit processing is a small frac­
tion of the overall cost. Figure 2 illustrates the pro­
file of a transaction modifying 500 records. 
COMMIT 
.---- START 
LOGGING +l 
II 
DATA 
MANIPULATION 
Ill 
TIME
-
Figure 2 
Profile of a Transaction Modifying 
500 Records 
In contrast, for transaction processing applica­
tions such as hotel reservation systems, banking 
Digital Technical journal 
Vol. 3 No. I 
Winter 1!)91 
Designing an Optimized Transaction Commit Protocol 
applications, stock market transactions, or the 
telephone system, the data manipulation phase is 
usually short (requiring few 1/0s). Instead, the log­
ging and commit phases comprise the bulk of the 
work and must be optimized to allow high trans­
action throughput. The transaction profile for a 
transaction modifying one record is shown i n  
Figure 3 .  Note that the commit processing phase 
represents 36 percent of the transaction duration, 
in this example. 
rr= START 
DATA 
MANIPULATION 
II I 
LOGGING 
TIME
-
COMMIT 
Figure 3 
Profile of a Transaction Modifying 
One Record 
Group Commit 
Generally, database systems must force write infor­
mation to disk in order to commit transactions. In 
the event of a failure, this operation permits recov­
ery processing to determine which fa i led trans­
actions were active at the time of their termination 
and which ones had reached their moment of com­
mit. This information is often in the form of lists of 
transaction identifiers, called commit lists. 
Many database systems perform an optimized 
version of commit processing where commit infor­
mation for a group of transactions is written to disk 
in one 1/0 operation, thereby, amortizing the cost 
of the 1/0 across multiple transactions. So, rather 
than having each transaction write i ts own commit 
list to disk, one transaction writes to disk a com­
mit list contai ning the commit information for a 
number of other transactions. This technique is 
referred to in the literature as "group commit."' 
Group commit processing is essential for achiev­
ing high throughput. If every transaction that 
reached the commit stage had to actually perform 
an 1/0 to the same disk to flush its own commit 
information, the throughput of the database sys­
tem would be limited to the l/0 rate of the disk. A 
magnetic disk is capable of performing 30 l/0 
operations per second. Consequently, i n  the 
absence of group commit, the throughput of t he 
system is limited to 30 transactions per second 
(TPS). Group commit is essential to breaking this 
performance barrier. 
71 
Transaction Processing, Databases, and Fault-tolerant Systems 
There are several variations of the basic algo­
rithms for grouping multiple commit l ists into a 
single 1/0. The specific group commit algorithm 
chosen can significantly influence the throughput 
and response times of transaction processing. One 
study reports throughput gains of as much as 25 
percent by selecting an optimal group commit 
algorithm.1 
At high transaction throughput (hundreds of 
transactions per second), efficient commit process­
i ng provides a significant performance advantage. 
There is little information in the database litera­
ture about the efficiency of different methods of 
perform ing a group commit. Therefore, we ana­
lyzed several grouping designs and evaluated their 
performance benefits. 
Factors Affecting Group Commit 
Before proceeding to a description of the experi­
ments, it is useful to have a better understanding of 
the factors affecting the behavior of the group com­
mit mechanism. This section discusses the group 
size, the use of timers to stal l transactions, and the 
relationship between these two factors. 
Group Size 
An important factor affecting group 
commit is the number of transactions that partici­
pate in the group commit. There must be several 
transactions in the group i n  order to benefit from 
1/0 amortization. At the same time, transactions 
s hould not be required to wait too long for the 
group to build up to a large size, as this factor 
would adversely affect throughput. 
It is interesting to note that the incremental 
advantage of adding one more transaction to a 
group decreases as the group s ize increases. The 
incremental savings is equal to 1/(G x (G + 1 )), 
where G is the initial group size. For example, if 
the group consists of 2 transactions, each of them 
does one-half a write. If the group size increases 
to 3, the incremental savings in writes will be 
(1/2 - l/3), or 1/6 per transaction. If we do the same 
calculation for a group s ize incremented from 10 
to 1 1 ,  the savings will be (1/10 - l/11), or l/110 of a 
write per transaction. 
In general, if G represents the group size, and I 
represents the number of 1/0s per second for the 
disk, the maximum transaction commit rate is Jx G 
TPS. For example, if the group size is 45 and the rate 
is 30 I/Os per second to disk, the maximum trans­
action commit rate is 30 x 45, or 1350 TPS. Note that 
a grouping of only 10 will restrict the maximum 
TPS to 300 TPS, regardless of how powerful the 
72 
computer is. Therefore, the group size directly 
affects the max imum transaction throughput of 
the transaction processi ng system. 
Use of Timers to Stall Transactions 
One of the 
mechanisms to i ncrease the s ize of the commit 
group is the use of timers.u Timers are used to 
stall the transactions for a short period of time 
(on the order of tens of milliseconds) during com­
mit processing. During the stall, more transactions 
enter the comm i t  p rocessing phase and so the 
group size becomes larger. The stalls provided by 
the timers have the advantage of increasing the 
group size, and the disadvantage of increasing the 
response time. 
Trade-ojfs 
This section discusses the trade-offs 
between the size of the group and the use of timers 
to stall transactions. Consider a system where there 
are 50 active database programs, each repeatedly 
processing transactions against a database. Assume 
that on average each transaction takes between 
0.4 and 0.5 seconds. Thus, at peak performance, the 
database system can commit approximately 100 
transactions every second, each program actually 
completing two transactions in the one-second 
time interval. Also, assume that the transactions 
arrive at the commit point in a steady stream at dif­
ferent times. 
If transaction commit is stalled for 0.2 sec­
onds to allow the commit group to build up, the 
group then consists of about 20 transactions 
(0.2 seconds x 100 TPS). In this case, each trans­
action only incurs a small delay at commit time, 
averaging 0.10 seconds, and the database system 
shoul.d be able to approach its peak throughput of 
100 TPS. However, if the mechanism delays commit 
processing for one second, an entirely different 
behavior sequence occurs. Since the transactions 
complete in approximately 0.5 seconds, they accu­
mulate at the commit stall and are forced to wait 
until the one-second stall completes. The group 
size then consists of 50 transactions, thereby maxi­
mizing the l/0 amortization. However, throughput 
is also limited to 50 TPS, since a group commit is 
occurring only once per second. 
Thus, it is necessary to balance response time 
and the size of the commit group. The longer the 
stall, the larger the group size; the larger the group 
size, the better the l/0 amortization that is achieved. 
However, if the stall time is too long, i t  is possible 
to limit transaction throughput because of wasted 
CPU cycles. 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
Motivation for Our Work 
The concept of using commit timers is discussed 
in great detail by Reuter' However, there are signifi­
cant differences between his group commit scheme 
and our scheme. These differences prompted the 
work we present in this paper. 
In Reuter's scheme, the timer expiration triggers 
the group commit for everyone. In our scheme, no 
single process is in charge of commit processing 
based on a timer. Our commit processing is per­
formed by one of the processes desiring to write a 
commit record. Our designs i nvolve coordination 
between the processes in order to elect the group 
committer (a process). 
Reuter's analysis to determine the optimum value 
of the timer based on system load assumes that the 
total transaction duration, the time taken for com­
mit processing, and the time taken for performing 
the other phases are the same for all transactions. 
In contrast, we do not make that assumption. Our 
designs strive to adapt to the execution of many dif­
ferent transaction types under different system 
loads. Because of the complexity introduced by 
allowing variations in transaction classes, we do 
not attempt to calculate the optimal timer values as 
does Reuter. 
Cooperative Commit Processing 
In this section, we present the stages in perform­
ing the group commit with cooperating processes, 
and we describe, in deta il, the grouping design cur­
rently used i n  KODA, the Commit-Lock Design. 
Group Committer 
Assume that a number of transactions have com­
pleted all data manipulation and logging activity 
and are ready to execute the commit processing 
phase. To group the commit requests, the follow­
ing steps must be performed in KODA: 
1 .  Each transaction must make its commit infor­
mation avai lable to the group committer. 
2. One of the processes must be selected as the 
"group committer." 
3. The other members of the group need to be 
informed that their commit work wil.l be com­
pleted by the group committer. These processes 
must wa it until the commit information is writ­
ten to disk by the group committer. 
4. Once the group committer has written the com­
mit information to stable storage, it must inform 
the other members that commit processing is 
completed. 
Digital Technical journal 
Vul. 3 No. I 
Winter 1991 
Designing an Optimized Transaction Commit Protocol 
Commit-Lock Design 
The Commit-Lock Design uses a VMS lock to gener­
ate groups of committing transactions; the lock is 
also used to choose the group committee 
Once a process completes all its updates and 
wants to commit its transaction, the procedure is 
as follows. Each transaction must first declare its 
intent to join a group commit. In KODA, each pro­
cess uses the interlocked queue instructions of the 
VAX system running VMS software to enqueue a 
block of commit information, known as a commit 
packet, onto a global ly accessible commit queue. 
The commit queue and the commit packets are 
located in a shared, writeable global section. 
Each process then issues a lock request for the 
commit lock. At this point, a number of other 
processes are assumed to be going through the 
same sequence; that is, they are posti ng their 
commit packets and making lock requests for the 
commit lock. One of these processes is granted 
the commit lock. For the time being, assume the 
process that currently acquires the lock acts as 
the group committer. 
The group committer, first, counts the number 
of entries on t he commit queue, provid ing the 
number of transactions that will be part of the 
group commit. Because of the VAX interlocked 
queue instructions, scanning to obtain a count and 
concurrent queue operations by other processes 
can proceed simultaneously. The group committer 
uses the information in each commit packet to 
format the commit block which will be written 
to disk. In KODA, the commit block is used as a 
commit list, recording which transactions have 
committed and which ones are active. In order to 
commit for a transaction, the group committer 
must mark each current transaction as completed. 
In addition, as an optimization, the group commit­
ter assigns a new transaction identifier for each 
process's next transaction. Figure 4 illustrates a 
commit block ready to be flushed to disk. 
Once the commit block is modified , the group 
committer writes it to disk in one atomic 1/0. This 
is the moment of commit for all transactions in 
the group. Thus, all transactions that were active 
and took part in this group commit are now stably 
marked as committed. In addition, as explained 
above, these transactions now have new transac­
tion identifiers. Next, the group committer sets a 
commit flag in each commit packet for all recently 
committed transactions, removes all commit pack­
ets from the commit queue, and, finally, releases 
the commit lock. Figure 5 illustrates a committed 
73 
Transaction Processing, Databases, and Fault-tolerant Systems 
COMMIT 
PACKET 
COMMIT 
QUEUE 
CURR_TID 
37 
CURR TID 
32 
-
NEXT_TID 
0 -- NEXT
-
TID 
0 r--
COMMIT_FLG 0 
COMMIT_FLG 0 
COMMIT GROUP 
KEY: 
CURR_TID 
NEXT_TID 
37 
42 
32 
43 
41 
44 
COMMIT BLOCK 
CURR_ TID 
CURRENT TRANSACTION IDENTIFIER 
NEXT TID 
NEXT TRANSACTION IDENTIFIER 
COMMIT_FLG 
COMMIT FLAG 
CURR TID 
4 1  
CURR TID 
28 
CURR_TID 
39 
NEXT
-
TID 
0 r--
NEXT
-
TID 
0 --
NEXT TID 
0 
COMMIT_FLG 0 
COMMIT_FLG 0 
COMMIT_FLG 0 
Figure 4 
Commit Block Ready to be Flushed to Disk 
group with new transaction identifiers and with 
commit flags set. 
At this point, the remaining processes that were 
part of the group commit are, i n  turn, granted 
the commit Jock. Because their commit flags are 
already set, these processes realize they do not 
need to perform a commit and, thus, release the 
commit lock and proceed to the next transaction. 
After all these committed processes release the 
commit lock, a process that did not take part in the 
COMMIT 
QUEUE 
CURR TID 
-1 
NEXT
-
TID 
42 
COMMIT _FLG 
1 
KEY: 
CURR TID 
-1 
NEXT
-
TID 
43 
COMMIT _FLG 1 
COMMITTED GROUP 
CURR TID 
-1 
NEXT
-
TID 
44 
COMMIT_FLG 
1 
CURR TID 
CURRENT TRANSACTION IDENTIFIER 
NEXT
-
TID 
NEXT TRANSACTION IDENTIFIER 
COMMIT _FLG 
COMMIT FLAG 
group commit acquires the lock, notices it has not 
been committed, and, therefore, initiates the next 
group commit. 
There are several i nteresting points about using 
the VMS Jock as the grouping mechanism. Even 
though all the transactions are effectively commit­
ted after the commit block l/0 has completed, the 
transactions are stil l  forced to proceed serially; 
that is, each p rocess is granted the lock, notices 
that it is comm itted, and then releases the Jock. 
NEXT COMMIT PACKET 
CURR TID 
28 
CURR TID 
39 
CURR TID 
29 
NEXT
-
TID 
0 --
NEXT
-
TID 
0 --
NEXT
-
TID 
0 
COMMIT_FLG 0 
COMMIT_FLG 0 
COMMIT_FLG 0 
Figure 5 
Committed Group 
74 
Vol. 3 No. I 
Winter 1991 
Digital Technical journal 
So there is a serial procession of lock enqueues/ 
dequeues before the next group can start. 
This serial procession can be made more concur­
rent by, first, requesting the lock in a shared mode, 
hoping that aU processes commit ted are granted 
the lock in unison. However, in practice, some pro­
cesses that are granted the lock are not committed. 
These processes must then request the lock in an 
exclusive mode. If this lock request is mastered on 
a different node in a VAXcluster system, the lock 
enqueue/dequeues are very expensive. 
Also, there is no explicit stall time built into 
the algorithm. The latency associated with the 
lock enqueue/dequeue requests allows the commit 
queue to build up. This stall is entirely dependent 
on the contention for the lock, which in turn 
depends on the throughput. 
Group Commit Mechanisms ­
Our New Designs 
To improve on the transaction throughput provided 
by the Commit-Lock Design, we developed three 
different grouping designs, and we compared their 
performances at high throughput. Note that the 
basic paradigm of group commit for all these 
designs is described in the Group Committer sec­
tion. Our designs are as follows. 
Com.m.it-Stall Design 
In the Commit-Stall Design, the use of the commit 
lock as the grouping mechanism is eliminated. 
Instead , a process inserts its commit packet onto 
the commit queue and, then, checks to see if it is 
the first process on the queue. If so, the process 
acts as the group committer. If not, the process 
schedules its own wake-up call, then sleeps. Upon 
waking, the process checks to see if it has been 
committed . If so, the process proceeds to its next 
transaction. If not, the process agai n  checks to see 
if it is first on the commit queue. The algorithm 
then repeats, as described above. 
This method attempts to el iminate the serial 
wake-up behavior displayed by using the commit 
lock. Also, the duration for which each process 
stalls can be varied per transaction to allow explicit 
control of the group size. Note that if the stall time 
is too smal l, a process may wake up and stall many 
times before it is committed. 
Willing-to-Wait Design 
As we have seen before, a delay in the commit 
sequence is a convenient means of converting a 
response time advantage into a throughput gain. If 
we increase the stall time, the transaction duration 
Digital Technical journal 
Vol. 3 No. 1 
Winter 1991 
Designing an Optimized Transaction Commit Protocol 
increases, which is u ndesirable. At the same time, 
the grouping size for group commit increases, 
which is desirable. The challenge is to determine 
the optimal stall time. Reuter presented an analyti­
cal way of determining the optimal stall time for a 
system with transactions of the same type.' 
Ideally, we would like to devise a flexible scheme 
that makes the trade-off we have just described in 
real time and determines the optimum commit 
stall time dynamically. However, we cannot deter­
mine the optimum stall time automatically, because 
the database management system cannot judge 
which is more important to the user in a general 
customer situation - the transaction response time 
or the throughput. 
The Willing-to-Wait Design provides a user param­
eter called WTW time. This parameter represents 
the amount of time the user is willing to wait for 
the transaction to complete, given this wait will 
benefit the complete system by increasing through­
put. wrw time may be specified by the user for each 
transaction. Given such a user specification, it is 
easy to calculate the commit stall to i ncrease the 
group size. This stal l equals the WlW time minus 
the time taken by the transaction thus far, but only 
if the transaction has not already exceeded the 
WlW time. For example, if a transaction comes to 
commit processing in 0.5 second and the wrw time 
is 2.0 seconds, the stall time is then 1 .5 seconds. In 
addition, we can make a further improvement by 
reducing the stall time by the amount of time 
needed for group commit processing. This delta 
time is constant, on the order of 50 milliseconds 
(one 1/0 plus some computation). 
The WTW parameter gives the user control over 
how much of the response time advantage (if any) 
may be used by the system to improve transaction 
throughput. The choice of an abnormally high value 
of WlW by one process only affects its own trans­
action response time; it does not have any adverse 
effect on the total throughput of the system. A low 
value of WlW would cause small commit groups, 
which in turn would l imit the throughput. However, 
this can be avoided by adm inistrative controls on 
the database that specify a minimum WlW time. 
Hiber Design 
The Hiber Design is sim i lar to the Commit-Stall 
Design, but, instead of each process scheduling i ts 
own wake-up call, the group committer wakes up 
all processes i n  the committed group. In addition, 
the group committer must wake up the process 
that will be the next group committer. 
75 
Transaction Processing, Databases, and Fault-tolerant Systems 
Note, this design exhibits a serial wake-up behav­
ior like the Comm it-Lock Design, however, the 
mechanism is less costl y  than the VMS lock used by 
the Commit-Lock Design. In the Hiber Design, if 
a process is not the group committer, it simply 
sleeps; it does not schedu le its own wake-up call .  
Therefore, each process is guaranteed to sleep and 
wake up at most once per commit, in contrast to 
the Commit-Stall Design. Another interesting char­
acteristic of the Hiber Design is that the group 
committer can choose to either wake up the next 
group com mitter immediately, or it can actually 
schedule the wake-up call after a delay. Such a delay 
al lows the next group size to become larger. 
Experiments 
We implemented and tested the Commit-Lock, the 
Com mit-Sta ll, and the Wi lling-to-Wait designs in 
KODA . The objectives of o ur  experiments were 
• 
To find out which design wou ld yield the 
maximum throughput under response time 
constraints 
• 
Tb understand the performance characteristics 
of the designs 
In the fol lowing sections, we present the deta ils 
of our experiments, the results we obta ined, and 
some observations. 
Details of the Experiments 
The hardware used for all of the fol lowing tests was 
a VAX 6340 with four processors, each rated at 36 
VAX units of performance (VUP). The total possible 
CPU utilization was 400 percent and the total p ro­
cess ing power of the computer was 14.4 vurs. As 
the com m i t  processing becomes more sign ificant 
in a t ransaction (in relation to the other phasc:s), 
the impact of the grouping mechanism on the trans­
action throughput increases. Therefore, i n  order 
to accentuate the performance differences between 
the various designs, we performed our experiments 
using a t ransaction that involved no database activ­
ity except to fol low the commit sequence. So, for 
all rractical purposes, the TPS data presented 
in this paper can be interp reted as "commit 
sequences rer second.'' Also, note that our system 
imposed an upper limit of 50 on the grouping size. 
Results 
Using the Commit-Lock Design, transaction pro­
cess ing bott lenecked at 300 TPS. Performance 
greatly improved with the Comm it-Stal l Design; 
the maximum throughput was 464 ·rPS. The 
Wi l l ing-to-Wa it Design provided the highest 
76 
throughput, 500 TPS. Using this last design, it was 
possible to achieve up to a 66 percent improve­
ment over the less-efficient Commit-Lock Design. 
Although both timer schemes, i.e . ,  the Com m it ­
Stall and Wil ling-to-Wait designs, needed tuning to 
set the parameters and the Com m it-Lock Design 
did not, we observed that the maximum through­
put obtained using timers is much better than that 
obta ined with the lock. These results were similar 
to those of Reuter. 
For our Willing-to-Wa i t  Design, the minimum 
transaction duration is the WTW time. Therefore, 
the maximum TPS, the number of servers, and 
the WTW stall t ime, measured in m i lliseconds, 
are related by the formula: number of servers 
x 1000/WTW = maximum TPS. For example, our 
maximum TPS for the \.XITW design was obta i ned 
wi th 50 servers and 90 m i l l iseconds WTW time. 
Using the formula, 50 x 1000/90 = 555. The actual 
TPS achieved was 500, which is 90 percent of the 
maximum TPS. This ratio is also a measure of the 
effectiveness of the experiment. 
Dur ing our experiments, the maximum group 
s ize observed was 45 (with the Wi l l ing-to-Wa it 
Design). This is close to the system-imposed l imit 
of 50 and , so, we may be able to get better grouping 
with higher limits on the size of the group. 
Observations 
In the Commit-Stall and the Willing-to-Wait designs, 
given a constant stal l ,  if the number of servers is 
increased, the TPS increases and then decreases. 
The rate of decrease is slower than the rate of 
increase. The TPS decrease is due to CPU overload­
ing. The TPS increase is due to more servers trying 
to execute transactions and better CPU utilization. 
Figure 6 i l lustrates how TPS varies with the num­
ber of servers, given a constanr stal l WlW time. 
Aga in, i n  the stalling designs, for a constant num­
ber of servers, if the stall is increased, the TPS 
increases and then decreases. The TPS increase is 
due to bet ter grouping and the decrease is due to 
CPU underutilization. Figures 7 and 8 show the 
effects on TPS when you vary the commit-stall 
time or the WT\V time, while keepi ng the number 
of servers constant. 
Tb maximize TPS with the Comm it-Stal l Design, 
the fol lowing " mountai n-climbing" algorithm was 
useful. This algorithm is based on the previous two 
observations. Start with a reasonable value of the 
stall and the number of servers, such that the CPU 
is u nderutil ized. Then in-crease the number of 
servers. CPU u t i l ization and the TPS i ncrease. 
Vol . .) No. I 
Winter 1991 
Digital Tecbnical journal 
0 
480 
z 
0 
0 
460 
w 
(/) 
a: 
440 
w 
(l_ 
(/) 
420 
z 
Q 
1-
400 
0 
<{ 
(/) 
380 
z 
<{ 
a: 
1-
360 
N UMBER OF SERVERS 
NOTE THE WILLING-TO-WAIT STALL TIME IS A CONSTANT 
1 00 MILLISECONDS 
Figure 6 
Transactions per Second in 
Relationship to the Number of 
Servers, Given a Constant 
Willing-to-Wait Time 
Continue until the CPU is overloaded; then, increase 
the stall t ime. CPU utilization decreases, but the 
TPS increases due to the larger group size. 
This algorithm demonstrates t hat increasi ng 
the number of servers and the stall by small 
amounts at a t ime increases the TPS, but only up 
to a limit. After this poi nt, the TPS drops. When 
close to the limit, t he two factors may be varied 
alternately i n  order to find the true maximum. 
Table 1 shows the pe rformance measurements of 
the Commit-Stal l Design. Comments are i ncluded 
in the table to highlight t he performance behavior 
the data supports. 
The same mountain-climbing algorithm is modi­
fied slightly to obtai n  the maximum TPS with t he 
Willing-to-Wa it Design. The performance measure-
0 
440 
z 
0 
0 
w 
(/) 
400 
a: 
w 
360 
(l_ 
(/) 
z 
0 
320 
i= 
0 
<{ 
280 
(/) 
z 
<{ 
a: 
1-
240 
20 
30 
40 
50 
60 
70 
1 0  
80 
COMMIT-STALL TIME (MILLISECONDS) 
NOTE THE NUMBER OF SERVERS EQUALS 50 
Figure 7 
Transactions per Second in 
Relationship to the Commit-Stall 
Time, Given a Constant Number 
of Servers 
Digital Techn ical journal 
Vul. 3 No. I 
Winter J'YJI 
Designing an Optimized Transaction Commit Protocol 
0 
490 
z 
0 
480 
0 
w 
(/) 
470 
a: 
w 
(l_ 
460 
(/) 
z 
450 
Q 
1-0 
<{ 
440 
(/) 
z 
430 
<{ 
a: 
420 
1-
90 
1 00 
1 1 0  
1 20 
1 30 
1 40 
1 50 
WILLING-TO-WAIT TIME (MI LLISECONDS) 
NOTE THE NUMBER OF SERVERS EQUALS 65. 
Figure 8 
Transactions per Second in 
Relationshzp to the WTW Time, 
Given a Constant Number 
of Servers 
ments of this design are presented i n  Table 2. As 
we have seen before, the maximum TPS with this 
design is i nversely proportional to the wrw time, 
whi le CPU is not fully utilized . The first four rows 
of Table 2 i llustrate this behavior. The rest of the 
table follows the same pattern as Table 1. 
The Willing-to-Wait Design performs s lightly 
better than the Commit-Stall Oesign by adjusting 
to the variations in the speed at which different 
servers arrive at the commit point. Such variations 
are compensated for by t he variable stalls in the 
Willing-to-Wa it Design. The refore, if the variation 
is h igh and the commit sequence is a significant 
portion of the transaction, we expect the Willing­
to-Wa it Design to perform much better than the 
Commi t-Stall Design. 
Future Work 
There is scope for more interesting work to further 
optimize commit processing in t he KODA database 
kernel. First, we wou ld like to perform experi­
ments on the Hiber Design and compare it to the 
other designs. Next, we would like to explore ways 
of combining the Hiber Design wi th either of the 
two timer designs, Commit-Stall or Willing-to­
Wa it. This may be the best design of all the above, 
with a good mixture of automat ic stall, low over­
head , and explicit con trol over the total stall time. 
In addition, we would like to invest igate the use of 
t imers to ease system management. For example, a 
system admin istrator may i ncrease the stalls for 
all transactions on the system i n  order to ease CPU 
contention, thereby increasing the overall effective­
ness of the system. 
77 
Transaction Processing, Databases, and Fault-tolerant Systems 
Table 1 
Commit-Stall Design Performance Data 
Number of 
Commit Stall 
CPU Utilization 
Servers 
(Milliseconds) 
(Percent)* 
TPS 
Comments 
50 
20 
360 
425 
Starting poi nt 
55 
20 
375 
454 
Increased number of servers, therefore, higher TPS 
60 
20 
378 
457 
Increased number of servers, therefore, CPU saturated 
60 
30 
340 
461 
Increased stall, therefore, CPU less util ized 
65 
30 
350 
464 
Increased number of servers, maximum TPS 
70 
30 
360 
456 
"Over-the-hill" situation, same strategy of further 
i ncreasing the number of servers does not increase TPS 
70 
40 
330 
451 
No benefit from increasing number of servers and stall 
65 
40 
329 
448 
No benefit from just increasing stall 
• Four processors were used in the experiments. Thus, the total possible CPU utilization is 400 percent. 
Table 2  
Willing-to-Wait Performance Data 
Willing-to-Wait 
Number of 
Stall 
CPU Util ization 
Servers 
(Mill iseconds) 
(Percent)* 
TPS 
45 
1 00 
285 
426 
45 
90 
295 
466 
45 
80 
344 
498 
45 
70 
363 
471 
50 
80 
372 
485 
50 
90 
340 
500 
55 
90 
349 
465 
50 
1 00 
324 
468 
Comments 
Starting point, CPU not saturated 
Decreased stall to load CPU, CPU still not saturated 
Decreased stall again 
Further decreased stall, CPU almost saturated 
Increased number of servers, CPU more saturated 
Increased stall to lower CPU usage, maximum TPS 
"Over-the-hill"situation, same strategy of further 
increasing number of servers does not increase TPS 
No benefit from just increasing stall 
• Four processors were used in the experiments. Thus, the total possible CPU utilization is 400 percent. 
Conclusions 
We have presented the concept of group commit 
processing as well as a general analysis of various 
options available, some trade-offs involved, and 
some performance results indicating areas for pos­
sible improvement. It is clear that the choice of the 
algorithm can significantly influence performance 
at high transaction throughput. We are optimistic 
that with some further investigation an optimal 
commit sequence can be incorporated into Rdb/VMS 
and VAX DBMS with considerable gains i n  trans­
action processing performance. 
Acknowledgments 
We wish to acknowledge the help provided by 
Rabah Mediouni in performing the experiments 
discussed in this paper. We would l ike to thank 
Phil Bernstei n  and Dave Lomet for their carefu l  
78 
reviews of this paper. Also, we want to thank the 
other KODA group members for their contri­
butions during informal d iscussions. Finally, we 
would l ike to acknowledge the efforts of Steve Klein 
who designed the original KODA group commit 
mechan ism. 
References 
I .  P Helland , H. Sam mer, ). Lyon, R. Carr, P Garrett, 
and A. Reuter, "Group Commit Timers and High 
Volume Transaction Processing Systems," High 
Performance Transaction Systems, Proceedings 
of the 2nd International Workshop (September 
1987). 
2. D. Gawlick and D. Kinkade, "Varieties of Con­
currency Control in IMS/VS Fast Path," Database 
Engineering Qune 1985). 
Vol. 3 No. I 
Winter 1991 
Digital Techuicaljournal 
William F. Bruckert 
Carlos Alonso 
James M. Melvin 
Verification of the First 
Fault-tolerant l2.lX System 
The fault-tolerant character of the VAXft 3000 system required that plans be made 
early in the development stages for the verification and test of the system. To ensure 
proper test coverage of the fault-tolerant features, engineers built fault-insertion 
points directly into the system hardware. During the verification process, test engi­
neers used hardware and software fault insertion in directed and random test 
forms. A four-phase verification strategy was devised to ensure that the VAXft system 
hardware and software was fully tested for error recovery that is transparent to 
applications on the system. 
The VAXft 3000 system provides transparent fault 
tolerance for applications that run on the system. 
Because the 3000 i ncludes fault-tolerant features, 
verification of the system was unlike that ordinar­
ily conducted on VAX systems. To facilitate system 
test, the verification strategy outlined a four-phase 
approach which would require hardware to be 
built into the system specifically for test purposes. 
This paper presents a brief overview of the VAXft 
system architecture and then describes the meth­
ods used to verify the system's fault tolerance. 
VAXft 3000 Architectural Overview 
The VAX.ft fault-tolerant system is designed to 
recover from any single point of hardware failure. 
Fault tolerance is provided transparently for all 
applications running under the VMS operati ng 
system. This section reviews the implementation 
of the system to provide background for the main 
discussion of the verification process. 
The system comprises two duplicate systems, 
called zones. Each zone is a fully functional com­
puter with enough elements to run an operating 
system. These two zones, referred to as zone A and 
zone B, are shown in Figure 1, which illustrates the 
duplication of the system components. The two 
independent zones are connected by duplicate 
cross-link cables. The cabinet of each zone also 
includes a battery, a power regulator, cooling fans, 
and an AC power input. Each zone's hardware has 
sufficient error checking to detect all single faults 
within that zone. 
Figure 2 is a block diagram of a single zone with 
one 1/0 adapter. Note the portions of the zone 
Digital Technicaljourtral 
Vol. 3 No. I 
Winter 1991 
labeled dual-rail and single-ra il. The dual-rail por­
tions of the system have two independent sets 
of hardware performi ng the same operations. 
Correct operation is verified by comparison. The 
fault-detection mechanism for the single-rai l  I/O 
modules combines checking codes and communi­
cation protocols. 
The system performs J/0 operations by sending 
and receiving message packets. The packets are 
exchanged between the CPU and various servers, 
including d isks, Ethernet, and synchronous lines. 
These message packets are formed and interpreted 
in the dual-ra il portion of the system. They are pro­
tected in the single-rai l  portion of the machine by 
check codes which are generated and checked i n  
the dual-ra i l  port ion of the machine. Corrupted 
packets can be retransmitted through the same or 
alternate paths. 
In the normal mode of fault-tolerant operation, 
both zones execute the same instruction at the 
same time. The four processors (two in each zone) 
appear to the operating system as a single logical 
CPU. The hardware supplies the detection and 
recovery facil it ies for faults detected in the CPU 
and memory portions of the system. A defective 
CPU module and its memory are automatically 
removed from service by the hardware, and the 
remaining CPU continues processing. 
Error hand ling for the l/0 interconnections is 
managed differently. The paths to and from I/O 
adapters are duplicated for checking purposes. If a 
fault is detected, the hardware retries the operation. 
If the retry is successful, the error is logged, and 
operation continues without software assistance. 
79 
Transaction Processing, Databases, and Fault-tolerant Systems 
80 
ZON E A 
E 
>-
0:: 
w 
f-
G 
f-
<( 
m 
'"'== 
AC BOX 
DUAL-RAIL 
SINGLE-RAIL 
DISK OR 
TAPE 
>- >- >-
0:: 0:: 0:: 
0 0  0 
2 2 2  
>- w  w w  
o:: 2 2 2  
0 0:: 0:: 0:: 
::::J 2 0 0  0 
Ŵ ŵ  
[l_ W  0 0  0 
0 2  ::::
.:::: ;:, 
I 
FAN I 
Figure 1 
0 
1 
FIREWALL 
EDC 
ZON E B 
CROSSLINK CABLES 
A Dual-zone VAX.ft System 
MEMORY 
INTERFACE 
BUS 
CROSSLINK 
CABLES 
TO ZONE B 
MODULE 
INTE RCONNECT 
2 
3 
FIREWALL 
EDC 
D 
# 
CPU 
MODULE 
1/0 ADAPTER 
Figure 2 
Single-zone Structure of a VAX.ft 3000 System 
Vol 3 No. 1 
Winter 1991 
Digital Techt¡ical ]our nell 
If the ret ry is unsuccessful, the Fault-tole rant 
System Services (FTSS) software performs e rror 
recovery. FTSS is a layered software product that is 
utilized with every VAX.ft 3000 system. It provides 
the software necessary to complete system error 
recovery. For system recovery from a fai led 1/0 
device, an alternate path or device is used. All 
recoverable fau lts have an associated maximum 
threshold value. If this threshold is exceeded, FTSS 
performs appropriate device reconfiguration. 
Verification of a Fault-tolerant 
J::aXSystem 
This section entai ls a discussion of the types of sys­
tem tests and the fault-insertion techniques used 
to ensure the correct operation of the VAXft system. 
In addition, the four-phase verification strategy and 
the procedures involved in each phase are reviewed. 
There are two types of system tests: directed and 
random. Directed tests, which test specific hard­
ware or software features, are used most frequently 
in computer system verification and follow a strict 
test sequence. Complex systems, however, cannot 
be completely verified in a directed fashion.' As a 
case i n  point, an operating system running on a 
processor has innumerable states. Directed tests 
verify functional operation under a particular set 
of conditions. They may not, however, be used to 
verify that same functionality under all possible 
system conditions. 
In comparison, random testing allows multiple 
test processes to interact in a pseudo-random or 
random fashion. In random testing, test coverage 
is increased with additional run-time. Thus, once 
the proper test processes are in place, the need to 
develop additional tests in order to increase cover­
age is eliminated. This type of testing also reduces 
the effects of the biases of the engineers generating 
the tests. While directed testing can provide only a 
limited level of coverage, this coverage level can be 
well understood. Random testing offers a poten­
tially unbounded level of coverage; however, quan­
tifying this coverage is difficult if not impossible. 
To achieve the proper level of verification, the 
VAX.ft verification utilized a balance of directed 
and random testi ng. Directed testi ng was used to 
achieve a certain base level of functionality, and 
random testi ng was used to expand the level of 
coverage. 
To permit testing of system fault tolerance in a 
practical amount of time, some form of fault inser­
tion is required. The reliability of components used 
in computer systems has been improving, and more 
Digital Techtticaljoul"lwl 
Vol. 3 No. I 
Winter 1991 
Verification of the First Fault-tolerant VAX System 
importantly, the number of components used to 
implement any function has been dramatically 
decreasing. These factors have produced a corre­
spondi ng reduction in system fa ilure rates. Given 
the high reliability of today's machines, it is not 
practical from a verification standpoint to verify a 
system by letting it run until failures occur. 
Conceptually, faults can be inserted in two ways. 
First, memory locations and registers can be cor­
rupted to mimic the results of gate-level faults 
(software fault i nsertion). Second, gate-level faults 
may be inserted directly into the hardware (hard­
ware fault i nsertion). There are advantages to 
both techniques. One advantage of software· 
implemented fault insertion is that no embedded 
hardware support is required.' The advantage of 
hardware fault i nsertion, on the other hand, is that 
faults are more representative of actual hardware 
fa ilures and can reveal unanticipated side effects 
from a gate-level fa i lure. To utilize hardware fault 
insertion, either a mechanism must be designed 
into the system, or an external i nsertion device 
must be developed once the hardware is available. 
Given the physical feature size of the components 
used today, it is virtually impossible to achieve ade­
quate fault-insertion coverage through an external 
fault-insertion mechanism. 
The error detection and recovery mechanism 
determines which fault insertion technique is 
suitable for each component. Some examples illus­
trate this point. For the lockstep portion of the 
VAXft 3000 CPUs, software fault insertion is not suit­
able because the lockstep functional ity prevents 
corruption of memory or registers when faults 
occur. Therefore, hardware faults cannot be mim­
icked by modifying memory contents. However, 
the software fault-insertion technique was suitable 
to test the l/0 adapters since the system handles 
fau lts in the adapters by detecting the corruption 
of data. Hardware fault insertion was not suitable 
because the 1/0 adapters were implemented with 
standard components that did not support hard­
ware fault insertion. 
Because the verification strategy for the 3000 
was considered a fundamental part of the system 
development effort, fault insertion points were 
built directly into the system hardware. The amount 
of logic necessary to implement fault insertion is 
relatively small. The goals of the fau lt-insertion 
hardware were to 
• 
Eliminate any corruption of the environment 
under test that could result from fault insertion. 
For example, if a certa in type of system write 
8J 
Transaction Processing, Databases, and Fault-tolerant Systems 
operation is required to insert a fault, then every 
test case will be done on a system that is in a 
"post-fault-insertion" state. 
• 
Enable the user to d istribute faults randomly 
across the system. 
• Allow insertion of faults during system operation. 
• 
Enable testing of transient and solid faults. 
The fault-insertion points are accessed through 
a separate serial interface bus isolated from the 
operating hardware. This separate interface ensures 
t hat the environment under test is unbiased by 
fault i nsertion. 
E ven with hardware support for fault insertion, 
only a small number of fault-insertion points can 
be implemented relative to the total number possi­
ble. Where the number of fau lt-insertion points is 
small, the selection of the fault-insertion points 
is important to achieve a random d istribution. 
Fault-insertion points were designed into most of 
the custom chips in the VAXft system. When the 
designers were choosing the fault-insertion points, 
a single bit of a data path was considered sufficient 
for data path coverage. Since a significant portion 
of the chip area is consumed by data paths, a high 
level of coverage of each chip was achieved with 
relatively few fault-insertion points. The remaining 
fault-insertion points could then be applied to the 
control logic. Coverage of this logic was important 
because control logic faults result in error modes 
that are more unpredictable than data path failures. 
The effect that a given fault has on the system 
depends on the current system operation and when 
in that operation the fault was inserted. In the 
3000, for example, a failure of bit 3 in a data path 
will have significantly different behavior depend­
ing upon whether the data bit was incorrect during 
the address transmission portion of a cycle or dur­
ing the succeeding data portion. Therefore, the 
timing of the fault insertion was pseudo-random. 
The choice of pseudo-random insertion was based 
on the fact that the fault-insertion hardware oper­
ated asynchronously to the system under test. This 
meant that faults could be i nserted at any time, 
without correlation to the activity of the system 
under test. 
Faults may be transient or solid in nature. For 
design purposes, a solid fault was defined as a fail­
ure that wil l  be present on retry of an operation. 
A transient fault was defined as a fault that wil l  not 
be present on retry of the operation. Transient 
faults do not require the removal of the device that 
82 
experienced the fault; solid faults do require device 
removal. Since the system reacts differently to tran­
sient and hard faults, both types of faults had to 
be verified i n  the VAXft system .  Therefore, it was 
required that the fault-insertion hardware be capa­
ble of inserting solid or transient faults. Solid faults 
were i nserted by continually applying the fault­
insertion signal. Transient faults were i nserted by 
applying the fault-insertion signal only until the 
machine detected an error. 
As noted earlier, the verification strategy utilized 
both hardware and software fault insertion. The 
hardware fault-insertion mechanisms allowed faults 
to be inserted into any system environment, includ­
ing diagnostics, exercisers, and the VMS operating 
system. As such, it was used for initial verification 
as well as regression testing of the system. The veri­
fication strategy for the VAXft 3000 system involved 
a multiphase effort. Each of the fol lowing four veri­
fication phases built upon the previous phase: 
1. Hardware verification under simulation 
2. Hardware verification with system exerciser and 
fault insertion 
3. System software verification with fault insertion 
4. System application verification with fault 
insertion 
Figure 3 shows the functional layers of the 
VAXft 3000 system in relation to the verification 
phases. The numbered brackets to the right of 
the diagram correlate to the testing coverage of 
each layer. For example, the system software verifi­
cation, phase 3, verified the VMS system, Fault­
tolerant System Services (FTSS), and the hardware 
platform. 
The fol lowing sections briefly describe the four 
phases of the VAXft verification. 
Hardware Verification under Simulation 
Functional design verification using software simu­
lation is inherently slow i n  a design as large as the 
VAXft 3000 system. To use resources most efficiently, 
a verification effort must incorporate a number of 
different modeling levels, which means trading off 
detail to achieve other goals such as speed.' 
VAXft 3000 simulation occurred at two levels: the 
module level and the system leveL Module-level 
simulation verified the base functionality of each 
module. Once this verification was complete, a sys­
tem-level model was produced to validate the 
intermodule functional ity. The system-level model 
Vol. 3 No. I 
Winter 1991 
Digital Techt¢ical]ourtlal 
Verification of the First Fault-tolerant VAX System 
TEST PHASE COVERAGE 
....--------. - - - - -
- - - - - - -
USER APPLICATION 
HOST-BASED VOLUME SHADOWING 
z------------- - - - - - - - -
VMS 5.4 
PHASE 4 
FAULT-TOLERANT SYSTEM SERVICES 
PHASE 3 
VAXFT 3000 HARDWARE 
} PHASE 1 } PHASE 2 
Figure 3 
Functional Layers of the VAXft 3000 System in Relation to the Verification Phases 
consisted of a fu l l  dual- ra i I, dual-zone system with 
an 1/0 adapter in each zone. At the final stage, h1ll 
system testing was performed. 
More than 500 directed error test cases were 
developed for gate-level system simu lation. For each 
test, the test environment was set up on a fully 
operational system model, and then the fault was 
inserted. A simulation controller was developed to 
coordinate the system operations in the simu lation 
environment. The simu lation controller provided 
the following control ove r the testing: 
• 
Initialization of all memory elements and certain 
system registers to reduce test time 
• 
Setup of all memory data buffers to be used in 
testing 
• 
Automated test execution 
• 
Automated checking of test results 
• 
Log of test results 
For each test case, the test environment was 
selected from the following: memory testing, 1/0 
register access, direct memory access (DMA) traf­
fic, and interrupt cycles. In any given test case, any 
number of the previous tests could be run. These 
environments could be run with or without faults 
inserted . In addition, each environment consisted 
of multiple test cases. In an error handl ing test case, 
the proper system environment required for the 
test was set, and then the fault was i nserted into 
the system. The logic simulator used was designed 
to verify logic design. When an il legal logic condi­
tion was detected, it produced an error response. 
When a fault i nsertion resulted in an illegal logic 
condition, the simulator responded by i nvalidat­
i ng the test. Because of this, a great deal of time was 
spent to ensure that faults were i nserted in a way 
Digital Technical journal 
Vol. 3 No. 1 
Winte1' 1991 
that wou ld not generate i l legal condit ions. Each 
test case was considered successful only when the 
system error registers conta ined the correct data 
and the system had the ability to continue opera­
t ion after the fault. 
Hardware Verification with System 
Exerciser and Fault Insertion 
After the prototypes were available, the verification 
effort shifted from simulation to fault insertion on 
the hardware. The goal was to insert faults using an 
exerciser that induced stressful, reproducible hard­
ware activity and that allowed us to analyze and 
debug the fault easily. 
Exerciser test cases were developed to stress 
the various hardware functions. The tests were 
designed to create maximum interrupt and data 
transfer activity between the CPU and the l/0 
adapters. These functions could be tested individ­
ually or s imultaneously. The exerciser scheduler 
provided a degree of randomness such that the 
interaction of functions was representative of a 
real operating system. The fault-insertion hardware 
was used to achieve a random distribution of fault 
cases across the system. 
Because it was possible to insert initial fau lts 
while specific functions were performed, a great 
degree of reproducibi lity was achieved that a ided 
debug efforts. Once the full su ite of tests worked 
correctly, fault insertion was performed while the 
system continually switched between all fu nc­
tions. This test ing was more representative of actual 
faults in customer environments, but was less 
reproducible. 
As previously mentioned, the hardware fault­
insertion tool al lowed the i nsertion of both tran­
sient and solid fa ilures. The VAXft 3000 hardware 
recovers from transient fa ilures and utilizes 
83 
Transaction Processing, Databases, and Fault-tolerant Systems 
software recovery for hard fa ilures. Since the goal 
of phase 2 testing was to verify the hardware, the 
focus was on t ransient fault i nsertion. Two criteria 
for each error case determined the success of the 
test. First and foremost, the system must continue 
to run and to p roduce correct results. Second, the 
error data that the system captures must be correct 
based on the fault that was i nserted. Correct error 
data is important because it is used to ident ify the 
fa il ing component both for software recovery and 
for servicing. 
Although the simulation environment of phase 1 
was substantially slower than phase 2, it provided 
the designers with more information. Therefore 
when problems were discovered on the prototypes 
used in phase 2, the failing case was transferred to 
the simulator for further debugging. The hardware 
verification also validated the models and test pro­
cedures used in the simulation environment. 
System Software Verification with Fault 
Insertion 
In parallel with hardware verification, the VA.'{ft .)000 
system software error hand ling capabilities were 
tested .  This phase represented the next higher 
level of testing. The goal was to verify the VAX func­
tionality of the 3000 system as well as the software 
recovery mechanisms. 
D igital has p roduced various test packages to 
verify VAX functionality. Since the VA.'{ft 3000 system 
incorporates a VAX chip set used i n  the VAX 6000 
series, i t  was possible to use several standard 
test packages that had been used to verify that 
system.' 
Fau lt-tolerant verification, however, was not 
addressed by any of the existi ng test packages. 
Therefore, add itional tests were developed by com­
bin ing the ex isting functional test suite with the 
hardware fault-insertion tool and software fault­
insertion routines. Test cases used included cache 
fa i l ure, clock fai lure, memory fa ilure, i ntercon­
nect fa ilures, and disk fa ilures. These fa ilures were 
applied to the system during various system opera­
tions. In addition, servicing errors were also tested 
by removing cables and modules while the system 
was running. T he completion criteria for tests 
included the following: 
• 
Detection of the fault 
• 
Isolation of the fai led hardware 
• 
Continuation of the test p rocesses without 
interruption 
84 
System Application Verification with 
Fault Insertion 
The goals for the fi nal phase of the VAXft 3000 
verification were to run an application with fault 
i nsertion and to dl'monstrate that any system 
fau lt recovery action had no effect on the process 
integrity and data integrity of the application. The 
appl ication used in the testing was based on the 
standard DebitCred it banking benchmark and was 
implemented using the DECintact layered product. 
The bank has 10 branches, 100 tel le rs, and 3,600 
customer accounts ( 10 tellers and 360 accounts 
per branch) Traffic on the system was simulated 
using terminal emulat ion process (VAXRTE) scripts 
representing bank teller activity. T he transaction 
rate was initially one transaction per second (TPS) 
and was varied up to the maximum TPS rate to stress 
the system load. 
The general test p rocess can be described as 
follows: 
1 .  Started appl ication execution. The terminal emu­
lation processes emulating the bank tellers were 
started and conti nued until the system was 
operating at the desired TPS rating. 
2. Invoked fault insertion. A fault was selected at 
random from a table of hardware and software 
faults. The terminal emulation process submitted 
stimuli to the application before, during, and 
after fault insertion. 
3. Stopped term inal emulation p rocess. The appli­
cation was run until a qu iescent state was 
reached. 
4. Performed resu lt validation. The p rocess i nteg­
rity and data i ntegrity of the appl ication were 
validated. 
All the meani ngful events were logged and time­
stamped during the experiments. Process integrity 
was proved by verifying continu i ty of transaction 
processing through fa ilures. The time stamps on 
the transaction executious and the system error 
logs allowed these two independent processes to 
be correlated. 
The proof of data integrity consisted of using the 
following consistency rules for transactions: 
1 .  The sum of the account balances is equal to the 
sum of the teller balances, which is equal to the 
sum of the branch balances. 
2. For each branch, the sum of the teller balances is 
equal to the branch balance. 
Vol. 3 No J 
Winter 1991 
Digital Teclmical journal 
3. For each transaction processed, a new record 
must be added to the history file. 
Appl ication verification under fau lt i nsertion 
served as the final level of fault-tolerant validation. 
Whereas the previous phases ensured that the vari­
ous components required for fault tolerance oper­
ated properly, the system application verification 
demonstrated that these components could oper­
ate together to provide a fully fau lt-tolerant system. 
Conclusions 
The process of verifying fault tolerance requires 
a strong architectural test plan. This plan must be 
developed early in the design cycle because hard­
ware support for testing may be required. The veri­
fication plan must demonstrate cognizance of the 
capabilities and limi tations at each phase of the 
development cycle. For example, the speed of sim­
u lation prohibits verification of software error 
recovery in a simulation enviro nment. Also, when 
a system is implemented with V!.Sl technology, the 
abi l ity to physically insert faults into the system 
by means of an external mechan ical mechanism 
may not be adequate to properly verify the correct 
system error recovery. These and other issues 
must be addressed before the chips are fabricated 
or adequate error recovery verification may not be 
possible. I nadequate error recovery verification 
directly increases the risk of real, u nrecoverable 
faults resu lting in system outages. 
The verification plan for the VAXft 3000 system 
consisted of the fol lowing phases and object ives: 
l. Hardware simu lation with fault insertion verified 
error detection, hardware recovery, and e rror 
data capture. 
2. System exerciser with fault insertion enhanced 
the coverage of the hardware simulation effort. 
3. System software with fau lt i nsertion verified 
software error recovery and reporting. 
4. System software verification with fau lt inser­
t ion verified t he transparency of the system 
error recovery to t he application runn ing on 
the system. 
The rest of any fault tolerant system is to survive 
a real fault whi le running a customer appl ication. 
Removing a module from a machine may be an 
impressive test, bur machi nes fa il as a result of 
modu les fal l ing out of the backplane. The initial 
rest of the VAXft 3000 system showed that the sys­
tem wou ld survive most of the faults introduced. 
Digital Technicaljournal 
Vol. 3 No. I 
1Vi11ter I')'JI 
Verification of the First Fault-tolerant VAX System 
Tests also revealed problems that would have 
resu lted in system outages if left uncorrected. 
System enhancements were made in the areas 
of system recovery act ions and repair cal l out. 
Whereas some of the problems were simple 
codi ng errors, others were errors i n  carefully 
reviewed and documented algori thms. Simply pur, 
the col lective wisdom of t he designers was not 
always sufficient to reach the degree of accuracy 
desired for this fault-tolerant system .  
A s  the VAXft p roduct fam i l y  evolves, perfor­
mance and functional enhancements will be ava i l­
able. The test processes described in this paper 
wiJI rema in in use, so t hat every future release 
of software wi l l  be better than the previous one. 
The combination of hardware and software fault 
insertion, coupled with physical system disrupt ion 
allows testing to occur at such a great ly accelerated 
rate, that al l testing performed will be repeated for 
every new release. 
Riferences 
1. J Croll, L. Camilli, and A. Vaccaro, "Test and 
Qualification of the VAX 6000 Model 400 System." 
Digital Technical journal, vol. 2, no. 2 (Spring 
1990): 73-83 
2. J. Barron, E. Czeck, Z. Segall, and D. Siewiorek, 
" Fault Injection Experiments Using FIAT (Fault 
Injection-based Automated Testing," IEEE Trans­
actions on Computers, vol. 39, no. 4 (Apri l 1990). 
3. R. Calcagni and W Sherwood, "VAX 6000 Model 
400 CPU Chip Set Functional Design Verification," 
Digital Technical journal, voL 2, no. 2 (Spring 
1990): 64-72. 
85 
I Further Readings 
The Digital Technical]ournal 
publishes papers that explore 
the technological foundations 
of Digital's major products. Each 
journal focuses on at least one 
product area and presents a 
compilation of papers written 
Æ the engineers who developed 
the product. The content for 
the journal is selected Æ the 
journal Advisory Board. 
Topics covered in previous issues of the Digital 
Technical journal are as follows: 
VAX 9000 Series 
Vol. 2, No. 4, Fall 1990 
The technologies and processes used to build 
Digital's first mainframe computer, including 
papers on the architecture, microarchitecture, 
chip set, vector processor, and power system, 
as well as CAD and test methodologies 
DECwindows Program 
Vol. 2, No. 3, Summer 1990 
An overview and descriptions of the enhancements 
Digital's engineers have made to MIT's X Window 
System in such areas as the server, toolkit, interface 
language, and graphics, as well as contributions 
made to related industry standards 
VAX 6000 Model 400 System 
Vol. 2, No. 2, Spring 1990 
The highly expandable and configurable midrange 
family of VAX systems that includes a vector pro­
cessor, a high-performance scalar processor, and 
advances in chip design and physical technology 
Compound Document Architecture 
Vol. 2, No. 1, Winter 1990 
The CDA family of architectures and services that 
support the creation, interchange, and processing 
of compound documents in a heterogeneous 
network environment 
Distributed Systems 
Vol. 1, No. 9,]une 1989 
Products that allow system resource sharing 
throughout a network, the methods and tools to 
evaluate product and system performance 
Storage Technology 
Vol. 1, No. 8, February 1989 
Engineering technologies used i n  the design, 
86 
manufacture, and maintenance of Digital's storage 
and information management products 
CVAX-based Systems 
Vol. 1, No. 7, August 1988 
CVAX chip set design and multiprocessing archi­
tecture of the mid-range VAX 6200 family of 
systems and the Micro VAX 3500/3600 systems 
Software Productivity Tools 
Vol. 1, No. 6, February 1988 
Tools that assist programmers in the development 
of high-quality, reliable software 
VAXcluster Systems 
Vol. 1, No. 5, September 1987 
System communication architecture, design and 
implementation of a distributed lock manager, 
and performance measurements 
VAX 8800 Family 
Vol. 1, No. 4, February 1987 
The microarchitecture, internal boxes, VAXBI bus, 
and VMS support for the VAX 8800 high-end multi­
processor, simulation, and CAD methodology 
Networking Products 
Vol. 1, No. 3, September 1986 
The Digital Network Architecture (DNA), network 
performance, LANbridge 100, DECnet-ULTRIX and 
DECnet-DOS, monitor design 
MicroVAX II System 
Vol. 1, No. 2, Mm·ch 1986 
The implementation of the microprocessor and 
floating point chips, CAD suite, MicroVAX work­
station, disk controllers, and TK50 tape drive 
VAX 8600 Processor 
Vol. 1, No. 1, August 1985 
The system design with pipelined architecture, 
the 1-box, F-box, packaging considerations, signal 
integrity, and design for reliability 
Subscriptions to the Digital Technical journal are 
ava ilable on a yearly, prepaid basis. The subscrip­
tion rate is $40.00 per year (four issues). Requests 
should be sent to Cathy Phillips, Digital Equipment 
Corporation, ML01·3/B68, 146 Main Street, Maynard, 
MA 01754, U.S.A. Subscriptions must be paid in U.S. 
dollars, and checks should be made payable to 
Digital Equipment Corporation. 
Single copies and past issues of the Digital 
Technical journal can be ordered from D igital 
Press at a cost of $ 16.00 per copy. 
Vol. 3 No. I 
Winter 1991 
Digital TechnicalJow·nal 
Technical Papers and Books by Digital Authors 
P. Bernstein, V. Hadzilacos, and N. Goodman, 
Concurrency Control and Recovery in Database 
Systems (Readi ng, MA: Addison-Wesley, 1987). 
P. Bernstein, M. Hsu, and B. Mann, "Implementing 
Recoverable Requests Using Queues," Proceedings 
1990 ACM 5/GMOD Conference on Management of 
Data (May 1990). 
T.K. Rengarajan, P. Spiro, and W Wright, "High 
Availability Mechanisms of VAX DBMS Software," 
Digital Technical journal, vol. 1 ,  no. 8 (February 
1989): 88-98. 
K. Morse, "The VMS/MicroVMS Merge," DEC 
Professional Magazine, vol. 7, no. 5 (May 1988). 
K. Morse and R. Gamache, "VAX/SMP," DEC 
Professional Magazine, vol. 7, no. 4 (April 1988). 
K. Morse, "Shrinking VMS," Datamation Quly 15, 
1984). 
L. Frampton, ]. Schriesheirn, and M. Rountree, 
"Planning for D istributed Processing," Auerbach 
Report on Communications (1989). 
Digital Press 
Digital Press is the book publishing group of Digital 
Equipment Corporation. The Press is an interna­
tional publisher of computer books and journals 
on new technologies and products for users, system 
and network managers, programmers and other 
professionals. Press editors welcome proposals and 
ideas for books in these and related areas. 
VAX/VMS: Writing Real Programs in DCL 
Paul C. Anagnostopoulos, 1989, softbound, 
409 pages ($29.95) 
X WINDOW SYSTEM TOOLKIT: The Complete 
Programmer's Guide and Specification 
Paul ]. Asente and Ralph R. Swick, 1990, softbound, 
967 pages ($44.95) 
UNIX FOR VMS USERS 
Philip E. Bourne, 1990, softbound, 
368 pages ($28.95) 
VAX ARCHITECTURE REFERENCE MANUAL, 
Second Edition 
Richard A. Brunner, Editor, 1991, softbound, 
560 pages ($44.95) 
Digital Tecbnical]ournal 
Vol. 3 No. I 
Winter 1991 
SOFTWARE DESIGN TECHNIQUES FOR LARGE 
ADA SYSTEMS 
William E. Byrne, 1991, hardbound, 
314 pages ($44.95) 
INFORMATION TECHNOLOGY STANDARDIZA­
TION: Theory, Practice, and Organizations 
Carl F. Cargi l l, 1989, softbound, 
252 pages ($24.95) 
THE DIGITAL GUIDE TO SOFTWARE 
DEVELOPMENT 
Corporate User Publication Group of D igital 
Equipment Corporation, 1990, softbound, 
239 pages ($27.95) 
DIGITAL GUIDE TO DEVELOPING 
INTERNATIONAL SOFTWARE 
Corporate User Publication Group of D igital 
Equipment Corporation, 1991, softbound, 
400 pages ($28.95) 
VMS INTERNALS AND DATA STRUCTURES: 
Version 5 Update Xpress, Volumes 1,2,3,4,5 
Ruth E. Goldenberg and Lawrence ]. Kenah, 1989, 
1990, 1991, all softbound ($35.00 each) 
COMPUTER PROGRAMMING AND 
ARCHITECTURE: The VAX, Second Edition 
Henry M. Levy and Richard H. Eckhouse jr. ,  1989, 
hardbound, 444 pages ($38.00) 
USING MS-DOS KERMIT: Connecting Your PC 
to the Electronic World 
Christine M. Gianone, 1990, softbound, 
244 pages, with Kermit D iskette ($29.95) 
THE USER'S DIRECTORY OF COMPUTER 
NETWORKS 
Tracy L. LaQuey, 1990, softbound, 
630 pages ($34.95) 
SOLVING BUSINESS PROBLEMS WITH MRP II 
Alan D. Luber, 1991, hardbound, 
333 pages ($34.95) 
VMS FILE SYSTEM INTERNALS 
Kirby McCoy, 1990, softcover, 
460 pages ($49.95) 
TECHNICAL ASPECTS OF DATA 
COMMUNICATION, Third Edition 
john E. McNamara, 1988, hardbound, 
383 pages ($42 00) 
LISP STYLE and DESIGN 
Molly M. Miller and Eric Benson, 1990, softbound, 
214 pages ($26.95) 
87 
Further Readings 
THE VMS USER'S GUIDE 
james F Peters III and Patrick J Holmay, 1990, 
softbound, :)04 pages (5 28.9'5) 
THE MATRIX: Computer Networks and 
Conferencing Systems Worldwide 
john S. Quarterman, 1990, softbound, 
719 pages ($49 95) 
X AND MOTIF QUICK REFERENCE GUIDE 
Randi J Rost, 1990, softbound, 
369 pages ($24.95) 
FIFTH GENERATION MANAGEMENT: 
Integrating Enterprises Through Human 
Networking 
Charles M. Savage, 1990, hardbound, 
267 pages ($28 9'5) 
A BEGINNER'S GUIDE TO VAX/VMS UTILITIES 
AND APPLICATIONS 
Ronald M. Sawey and ·rroy T Stokes, 1989, 
softbound, 278 pages ($26.95) 
88 
X WINDOW SYSTEM, Second Edit ion 
Robert Scheifler and james Gettys, 1990, 
softbound, 851 pages ($49.95) 
COMMON LISP: The Language, Second Edition 
Guy L. Steele jr. ,  1990, 1 ,029 pages ($ 38.9'5 in 
softbound, $46.95 in hardbound) 
WORKING WITH WPS-PLUS 
Charlotte Temple and Dolores Cordeiro, 1990, 
softbound, 235 pages ($24.95) 
To receive information on these or other publ ica­
tions from Digital Press, write: 
D igital Press 
Department DTJ 
12 Crosby Drive 
Bedford, MA 01730 
617/276-1536 
Or order directly by calling DECdirect at 
800-DIGITAL (800-344 -4825). 
Vol. 3 No. I 
lVinll!r 1991 
Digital Tecbnical journal 
ISSN 0898-901X 
Printed in U.S.A. EY-F588E-DP/90 11 02 16.0 MCG/BUO Copyright © Digital Equipment Corporat ion. All Rights Reserved. 


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | dtj-v03-01-tp-and-fault-tolerant-1991-cf078c |
| title | Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991) |
| author | Digital Equipment Corporation |
| date | 1991-01-01 |
| type | employer-record |
| subject_domain | transaction-processing |
| methodology | document-review, industry-analysis |
| source_file | dtj-v03-01-1991.pdf |
| license | CC-BY-4.0 |

### Abstract

This issue of the Digital Technical Journal presents eight peer-reviewed technical papers documenting DEC's complete distributed transaction processing stack, including the DECdta architecture, ACMS and DECintact TP monitors, DECdtm kernel-level transaction management, TPC Benchmark A performance results, database availability strategies, optimized commit protocols, and VAXft 3000 fault-tolerant system verification. The papers collectively define DEC's strategy to lead the distributed TP market through an integrated, standards-aligned, client/server architecture. Formal TPC Benchmark A results are disclosed: 69.4 tpsA-Local on VAX 9000 Model 210 and 21.6 tpsA-Local on VAX 4000 Model 300.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Primary-source technical journal documenting the complete DECtp architecture at the moment of its 1988 announcement and 1991 maturation; first formal disclosure of DEC's TPC Benchmark A audited results and the DECdta distributed TP architecture. |
| **Relevance** | high | Transaction ACID properties, two-phase commit, client/server TP decomposition, fault-tolerant hardware design, and group commit optimization remain foundational concepts in modern distributed databases and cloud transaction systems. |
| **Prescience** | high | DECtp's open-standards alignment (X/Open DTP, OSI-TP, POSIX) and client/server model accurately anticipated the dominant paradigm; predicted convergence of ACMS and DECintact proved correct; VAXft fault-tolerant architecture foreshadowed modern high-availability designs. |

### Prescience Detail


**Prediction 1:** DECtp open-standards alignment will enable market leadership
- **Claimed:** This combination of architecture, software, hardware technology, and support for emerging industry standards places Digital in excellent position to become industry leader for distributed portable transaction processing systems
- **Year:** 1991
- **Confidence at time:** medium


### Entities Referenced (36)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Digital Equipment Corporation | company | acquired | Compaq (1998) then HP (2002) |
| International Business Machines Corporation | company | active | [none] |
| Transaction Processing Performance Council (TPC) | institution | active | [none] |
| Carlos G. Borgialli | person | unknown | [none] |
| Philip A. Bernstein | person | active | [none] |
| William T. Emberton | person | unknown | [none] |
| Vijay Trehan | person | unknown | [none] |
| Thomas G. Speer | person | unknown | [none] |
| Mark W. Storm | person | unknown | [none] |
| William A. Laing | person | unknown | [none] |
| James E. Johnson | person | unknown | [none] |
| Robert V. Landau | person | unknown | [none] |
| Walter H. Kohler | person | unknown | [none] |
| Yun-Ping Hsu | person | unknown | [none] |
| Thomas K. Rogers | person | unknown | [none] |
| Wael H. Bahaa-El-Din | person | unknown | [none] |
| William Z. Zahavi | person | unknown | [none] |
| Frances A. Habib | person | unknown | [none] |
| Kenneth J. Omahen | person | unknown | [none] |
| Ananth Raghavan | person | unknown | [none] |
| T. K. Rengarajan | person | unknown | [none] |
| Peter M. Spiro | person | unknown | [none] |
| Ashok M. Joshi | person | unknown | [none] |
| William F. Bruckert | person | unknown | [none] |
| Carlos Alonso | person | unknown | [none] |
| James M. Melvin | person | unknown | [none] |
| Jane C. Blake | person | unknown | [none] |
| Samuel H. Fuller | person | unknown | [none] |
| X/Open Company Ltd. | institution | unknown | unknown |
| International Organization for Standardization | institution | active | [none] |
| Institute of Electrical and Electronics Engineers | institution | active | [none] |
| Conference on Data Systems Languages (CODASYL) | institution | unknown | unknown |
| Sperry Corporation | company | acquired | Unisys (1986) |
| National Semiconductor Corporation | company | acquired | Texas Instruments (2011) |
| NCR Corporation | company | active | [none] |
| Peter S. Kastner | person | active | [none] |

### Technologies Referenced (28)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| DECtp | framework | DEC | growth | legacy-discontinued |
| DECdta (Digital Distributed Transaction Architecture) | framework | DEC | growth | legacy-discontinued |
| DECdtm (Digital Distributed Transaction Manager) | platform | DEC | growth | legacy-discontinued |
| VAX ACMS (Application Control and Management System) | application | DEC | mature | legacy-discontinued |
| DECintact (Integrated Application Control) | application | DEC | growth | legacy-discontinued |
| VAX Rdb/VMS | application | DEC | mature | active |
| VAX DBMS | application | DEC | mature | legacy-discontinued |
| KODA (database kernel) | platform | DEC | mature | legacy-discontinued |
| VMS (Virtual Memory System) | platform | DEC | mature | active |
| DECforms | application | DEC | growth | legacy-discontinued |
| VAXft 3000 | platform | DEC | new-product | legacy-discontinued |
| Fault-tolerant System Services (FTSS) | application | DEC | new-product | legacy-discontinued |
| VAX 9000 Model 210 | platform | DEC | new-product | legacy-discontinued |
| VAX 4000 Model 300 | platform | DEC | new-product | legacy-discontinued |
| VAX 6340 | platform | DEC | mature | legacy-discontinued |
| VAX 6000 Series | platform | DEC | mature | legacy-discontinued |
| VAXcluster | platform | DEC | mature | legacy-discontinued |
| DECnet | protocol | DEC | mature | legacy-discontinued |
| TPC Benchmark A | protocol | TPC | current | superseded |
| X/Open Distributed Transaction Processing (DTP) | protocol | X/Open | emerging | superseded |
| OSI-TP (Open Systems Interconnection Transaction Processing) | protocol | ISO | emerging | legacy-discontinued |
| IBM SNA LU6.2 | protocol | IBM | mature | legacy-discontinued |
| ANSI/ISO SQL | protocol | ANSI/ISO | mature | active |
| Two-Phase Commit Protocol (2PC) | protocol | industry | mature | active |
| Digital Network Architecture (DNA) | protocol | DEC | mature | legacy-discontinued |
| DebitCredit Benchmark | protocol | industry | mature | superseded |
| VAX RMS (Record Management Services) | application | DEC | mature | active |
| LAT (Local Area Transport) | protocol | DEC | mature | legacy-discontinued |

### Observation Summary

- Total observations: 40
- By type: architecture-decision: 15, product-fact: 5, benchmark-result: 5, performance-model: 4, standards-alignment: 2, security-feature: 2, strategic-positioning: 1, performance-claim: 1, standards-insight: 1, viability-prediction: 1, actual-outcome: 1, market-context: 1, competitive-context: 1
