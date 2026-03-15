The Wayback Machine - https://web.archive.org/web/19970604113235/http://www.aberdeen.com:80/secure/proﬁles/1997/ibmecf/ibmecf.htm
IBM Network Computing
Enterprise Communications Family
Executive Summary
As users begin to achieve network computing’s potential beneﬁts – and
especially increased ﬂexibility and rapid implementation of new solutions –
they are ﬁnding that communications-software infrastructure is a key to
success.
Whether the new architecture is n-tier client-server, distributed-object, or
Internet thin-client, a critical component of satisfactory solution performance is
communi-cations performance, and speciﬁcally communications-software
performance. Moreover, new architectures bring with themselves new
complexity, including new communications protocols that IS must integrate and
balance with older commun-ications schemes. Flexible communications
software supports easy hooking-up of new nodes and technologies without
having to bring down or disrupt the enter-prise network, improves availability
by providing multiple paths between the user and system services, and adapts
readily to widely varying types of network trafﬁc. Thus, effective network-
computing enterprise communications software provides an easy migration
path from present networking, scalable performance, ﬂexibility, robustness, and
rapid implementation of network changes.
IBM’s Enterprise Communications Family targets the full array of network
computing communications-software beneﬁts by expanding IBM’s present
offer-ings especially in two areas: extending software to cover more corporate
network-ing protocols and architectures and a wider range of corporate needs,
from the desktop to the enterprise level and the "inter-enterprise workgroup";
and improv-ing this software’s performance, ﬂexibility, robustness,
administrative support, and migration capabilities. Thus, for the present IBM
installed base, the Enterprise Communications Family’s offerings and plans
provide a relatively low-risk path to network computing’s beneﬁts. For other IS
buyers looking at IBM’s approach to network computing, the Enterprise
Communications Family, effectively implemented, delivers strong
price/performance, a more robust migration from present systems, and one-
stop-shop ease of implementation building on IBM’s unmatched service
capabilities.
Overview: Enterprise Communications Family
Product Suite
The IBM Enterprise Communications Family offers both server-side
(Communications Server and NetWare for SAA) and client-side (Personal
Communications, CS/2 Access feature, and Internet Connection for Windows)
communications software. This software provides support for multiple
communications protocols, including IBM’s enterprise-scale SNA and the de-
facto-standard LAN and internetwork protocol, TCP/IP, as well as a wide
variety of media, features, and conﬁguration options. Table 1 lists some of the
functionality available with the Enterprise Communications Family.
Table 1: Communications Server Family Technical Highlights
CS/2 CS/NT CS/AIX OS/400 NetWare CS/MVS
OS/390
SNA Support:
3270 SNA
Gateway
X
X
X
X
APPN EN and
NN function
X
X
X
X
X
High
Performance
Routing
intermediate node
routing
X
X
X
X
X

HPR connection
endpoint
X
X
X
3270 support over
APPN
(DLUS/R)
X
X
X
X
Multiprotocol
support:
TN3270E server
X
X
X
X
Sockets over
SNA access node
X
X
X
X
X
SNA over TCP/IP
access node
X
X
X
X
X
Sockets over
SNA gateway
X
X
X
X
SNA over TCP/IP
gateway
X
X
X
X
IPX over SNA
gateway
X
X
IPX over TCP/IP
gateway
X
NetBIOS over
SNA gateway
X
NetBIOS over
TCP/IP gateway
X
Netware
Directory
Services
integration
X
Two especially important technologies available across the Enterprise
Communications product family are advanced multiprotocol support and High
Performance Routing (HPR), used especially in the Communications Server
and Personal Communications products. IBM’s advanced multiprotocol support
takes a different approach to multiple-protocol communications that can deliver
signiﬁcant user beneﬁts in performance and ease of network migration
In the past, a typical multiprotocol solution would "encapsulate" messages –
e.g., wrap SNA transmissions with TCP/IP headers and send them across the
network as standard TCP/IP packets. IBM’s tack is to replace the top layers of
one protocol by the other’s, leaving networking layers intact – e.g., their
AnyNet technology, a version of Multiprotocol Transport Network (MPTN)
that places SNA APIs and top-layer application support on top of TCP/IP’s
transport layer. In this case, an SNA transmission header will include
application-layer SNA information, for use at each end point of the
transmission, plus TCP/IP information, for use by intermediate nodes for
routing.
The results of this approach are subtle but profound. Instead of having to store
and operate two or more full sets of communications protocol software on end
and/or intermediate nodes, users can keep one protocol’s software plus the top
layers of others – a far smaller set of software. Instead of passing each message
through two full sets of communications protocols, the "top-layer replacement"
approach passes the message through the top layers of one and the bottom
layers of the other – typically a signiﬁcant performance boost. Adding or
migrating to a new protocol is simply a matter of adding top layers to existing
protocol stacks – network administrators do not need to learn to monitor new
routing tables or "read" entirely new message headers.
Thus, advanced multiprotocol support can confer signiﬁcant strategic beneﬁts:
• Ability to choose and implement applications independent of the user’s
underlying protocols -- IS can support new applications dependent on new
protocols by adding top layers for those protocols, with minimal
implementation and learning curves, and minimal impact on performance;
• Potential increased network performance, either via avoiding executing
two protocol stacks or because users can now choose and implement
higher-performance protocols without major impact on present
applications;
• Increased availability of services for more users -- since enterprises can
deploy business applications across the organization rather than only
where a particular LAN or WAN protocol reigns;
• Leveraging existing applications -- older applications can be supported
without change, or migrated to a new protocol with no application
changes;
• Ability to expand network service while reducing costs – e.g., costs of
learning, administration, and new-application implementation;

• Ability to consolidate previously-isolated networks without impacting
applications;
• Enterprise-wide standardization on a single backbone protocol.
IBM’s High Performance Routing (HPR) has several attractive features. It
offers automatic rerouting as nodes and routes are removed/fail and are
added/rejoin the network. This rerouting is dynamic -- the network "map", and
hence the route, can change while a message is on its way to its destination,
without requiring an administrator to bring the network down. The routing can
intermix low- and high-bandwidth data in order to maximize throughput on a
line, rather than forcing each communications stream to take its turn.
Sophisticated congestion control can delay or avoid performance degradation
when the communications is near peak load.
Meeting User Criteria
As noted above, Aberdeen ﬁnds that key user network-computing-
communications criteria are:
• performance and performance scalability of the network and of
distributed applications invoking communications protocol APIs;
• open ﬂexibility, including support for key communications standards;
• robustness, including ability to handle failures rapidly and automatically
as well as powerful administrative tools to allow effective network
monitoring and "tuning"; and
• ease of migration to new protocols and technologies.
Performance And Scalability
The Enterprise Communications Family’s advanced multiprotocol support and
HPR technologies give users substantial real-world performance/scalability
beneﬁts in moving towards network computing. As noted above, enterprises
can use advanced multiprotocol support to achieve higher protocol-execution
performance or to choose a higher-bandwidth protocol. On the router side,
HPR’s dynamic routing allows choice of the fastest route even while that "best
choice" is changing; HPR’s intermixing of high- and low-bandwidth trafﬁc
improves performance on mixed-trafﬁc networks (e.g., E-mail and multimedia
applications); and HPR’s congestion control scales trafﬁc further without
performance degradation. Users’ ability to place gateways between protocols
on the highest-performance server or router also improves overall network
performance.
IBM’s support for new high-bandwidth communications technologies such as
frame relay and ATM can be particularly effective in enhancing performance in
large-scale intra-enterprise networks or Intranets. By adding an Internet-TCP/IP
top-layer replacement to an SNA or frame-relay Intranet, users can have the
"best of both worlds": Internet application portability/ease-of-use/low cost plus
communications-technology performance in multimedia and other high-
bandwidth applications.
Particular products also offer platform-speciﬁc performance features. For
exam-ple, Communications Server for OS/390 TCP/IP includes a native sockets
imple-mentation that improves TCP/IP’s performance, and Communications
Server for AIX offers load balancing and multiprocessor support for server
scalability.
Flexibility
At a very basic level, advanced multiprotocol support improves administrators’
and developers’ ﬂexibility by allowing substitution of lower-level
communications protocols. The administrator can add the best business
application independent of the installed protocol; the developer can write to one
protocol’s API and ensure that the code will be interoperable with applications
written to different protocols on remote sites and portable (along with the top-
layer replacement) to platforms using other protocols.
This ﬂexibility is enhanced by Enterprise Communications Family’s support for
de-facto standards at the transport (SNA, SPX/IPX, TCP/IP) and lower (SDLC,
asynchronous protocols) layers as well as frame relay and ATM standards.
Standard-protocol support provides assurance to users that typical and
upcoming communications software is an integral part of their IBM-based
network-computing solutions. Internet Connection for Windows allows the
resulting network to tap in to the Internet’s portability and interoperability.
Robustness
As noted above, HPR provides added availability and failover capabilities via
its dynamic rerouting feature. Particular products also offer platform-speciﬁc
reliability functions. For example, Communications Server for AIX offers "hot
standby" to allow automated failover to another gateway if the server hardware

fails. The Personal Communications products also include automatic rerouting
if a server fails.
Ease Of Migration
Moving an enterprise’s networking towards a network-computing architecture
is today a particularly tricky operation. Many organizations must decide the
least-cost, least-risk migration path towards the most scalable long-term
network-computing network. Typical target network-computing architectures
may wish to integrate Intranets that use TCP/IP at both the WAN and desktop
level (but not necessarily at the LAN level), hosts that use SNA at the WAN
level, and departmental LANs that use SPX/IPX.
IBM’s Enterprise Communications Family is notable for its ability to allow
enterprises and departments to keep their present protocols in place,
superimposing top-layer replacements for additional protocols rather than
requiring administrators and developers to cope with their internals. Thus, to
integrate the three protocols in the case cited above, an enterprise can (1)
integrate SPX/IPX with SNA by providing LAN-to-LAN and LAN-to-host
communications via SNA, and/or (2) integrate TCP/IP with both SNA and
SPX/IPX by providing LAN-to-LAN and LAN-to-host communications via
SNA. In scenario (1), NetWare for SAA can provide the client-to-host function,
and CS/2 can provide IPX-to-IPX LAN-to-LAN communications over the SNA
networking layers. In scenario (2), the organization can add a TCP/IP sockets
API and top layers at the client, plus CS/2 or CS/AIX sockets over SNA
gateways to connect IP from the LAN to the host or LAN-to-LAN.
IBM’s unmatched breadth of service allows it to provide advice, consulting,
and support in the migration process.
Where Enterprise Communications Family Is
Most Effective
For enterprises moving to a network computing architecture, Enterprise
Communications Family is especially effective where a signiﬁcant portion of
the present architecture involves IBM hardware and software, and where price-
performance, service and handholding, or a robust implementation are primary
concerns. Where the organization is migrating from IBM systems, the Personal
Communications Family’s ease of migration from present IBM protocols and
gateways, performance/scalability, and ﬁt with other IBM network-computing
technologies mean a relatively low-risk migration strategy. Moreover, the new
Enterprise Communications Family technologies bring to an IBM customer all
the value-added beneﬁts of network-computing communications software cited
above: improved performance for critical client-server and server-server
communications, decreased system-design and system-support complexity,
increased ﬂexibility, and higher availability.
For organizations moving to network computing and having software and
hardware from multiple suppliers, Enterprise Communications Family can also
be particularly effective in many cases. Advanced multiprotocol support and
HPR allow high-performance multiprotocol networking at both the workgroup
and the enterprise level. IBM’s broad services mean one-stop-shop support for
the complex tasks of network migration. If Enterprise Communications Family
is combined with other network-computing services (e.g., the Communications
Servers form the base layer for IBM Application and Data Servers), the
resulting integrated network-computing approach ensures that users can take
advantage of the "tuning experience" of IBM in making applications, data
management, and communications software work in synchronization.
Aberdeen Conclusions
IBM’s Enterprise Communications Family of communications-software
products has made a strong start towards delivering the communications
infrastructure needed for network computing. The Enterprise Communications
Family has taken a collection of point products, added multiprotocol and
routing technolo-gies, and integrated them with each other and with a larger set
of product suites that together form the basis of a comprehensive network
computing architecture.
Aberdeen ﬁnds that IBM’s advanced multiprotocol support and High
Performance Routing technologies are particularly effective in delivering
value-added scalability, ﬂexibility, robustness, and ease of migration, both to
IBM’s installed base and to a broader class of multisupplier customers. Users
can therefore employ IBM’s communications-software suite to improve client-
server and server-server comm-unications performance, simplify network
design and administration, give the enterprise-network designer greater
ﬂexibility, and increase network robustness.
Just as network computing’s technologies such as the Internet are evolving
rapidly, so too is the Enterprise Communications Family a work in progress.
For example, Aberdeen expects the suite to continue to expand products such as
Communications Server across all major platforms, extend its Internet-speciﬁc
functionality in such areas such as multimedia-download streamlining, and add
ATM and frame-relay support as the standards evolve.

The Enterprise Communications Family is therefore immediately useful on its
own, and attractive in the long term because of its key role in IBM’s network
computing architecture. Aberdeen recommends that IS buyers considering
IBM’s network computing strategy place the Enterprise Communications
Family high on their list of products to buy.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #:
617.854.5212)
David Borde, Marketing Manager (direct #:
617.854.5226)
Email: rinehart@aberdeen.com or
borde@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright © 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this publication are
the property of their respective holders. Unless otherwise noted, the entire contents of this
publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a
retrieval system, or transmitted in any form or by any means without prior written consent of
the publisher.


---

## Frictionless Data Package Metadata

**Study ID:** 1997-ibm-s-enterprise-communications-fam-14559a
**Title:** IBM Network Computing: Enterprise Communications Family
**Author:** Aberdeen Group
**Date:** 1997-06-01
**Type:** profile
**Subject Domain:** Enterprise Networking / Communications Software
**License:** CC-BY-4.0
**Importance:** 3/5
**Relevance:** 3/5
**Prescience:** 4/5

### Importance Rationale
Represents a transitional moment in IBM's networking stack — the strategic pivot from SNA-centric to TCP/IP-aware multiprotocol architectures. Important as a primary source on the SNA deprecation trajectory and AnyNet/MPTN technology decisions.

### Relevance Rationale
Directly relevant to the history of enterprise networking transitions from SNA to TCP/IP. Documents IBM's technical strategy at a critical juncture and provides benchmark context for evaluating communications middleware choices of the era.

### Prescience Rationale
Aberdeen accurately predicted that TCP/IP would displace SNA; that multiprotocol bridging would be a transitional strategy; that HPR dynamic routing features anticipate modern SDN concepts; and that ATM would not displace TCP/IP long-term. The call to place ECF 'high on lists to buy' was overstated — SNA was sunset by IBM within a decade.

---

## Prescience Detail

### Predictions Made (1997)
- **IBM ECF recommended as enterprise communications purchase**: Aberdeen recommends placing ECF high on lists to buy
- **AnyNet/MPTN as long-term multiprotocol standard**: Predicted to remain strategically important for enterprise networking
- **ATM viability for enterprise WAN**: ATM predicted to expand as standards evolve
- **SNA long-term relevance in enterprise networking**: Predicted to remain important via multiprotocol bridging strategies

### Actual Outcomes (Verified)
- **IBM Communications Server end-of-support** (2024): Distributed CS end-of-support announced April 2024; z/OS version continued
- **AnyNet/MPTN market adoption** (2005): Obsolete by mid-2000s; TCP/IP won outright without bridging layer
- **ATM enterprise adoption** (2003): ATM failed to gain broad enterprise LAN/WAN adoption; displaced by Gigabit Ethernet and MPLS
- **SNA protocol deprecation** (2024): IBM deprecated SNA in IBM i 7.4 (2024); SNA largely replaced by TCP/IP
