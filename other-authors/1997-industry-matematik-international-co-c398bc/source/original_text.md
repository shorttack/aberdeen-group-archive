The Wayback Machine - https://web.archive.org/web/19970604113149/http://www.aberdeen.com:80/secure/proﬁles/1997/imi/body.htm
IMI Americas
560 White Plans Road
Tarrytown, NY 10591
(914) 631 2700
http://www.im.se
Industri-Matematik International
Corporation
Kungsgatan 12-14, Box 7733
Stockholm, Sweden 103 95
+46.8.676.50.00
Industri-Matematik International Corp.:
Strategic Solution for Fast-Moving, High-Volume Goods Industries
Preface
In the past, manufacturers and distributors reigned supreme in mandating the rules of trade with retailers and customers.
They controlled the products produced, the quantities, distribution locations and oftentimes the prices to be charged — little
emphasis was placed on product requirements, timely delivery or customer satisfaction. So it is not surprising that
manufacturer and distributor information-systems business models concentrated on increasing manufacturing efﬁciency and
output.
In recent years, there has been a signiﬁcant transfer of market inﬂuence to the retailers and customers. Today's buyers
increasingly are choosing suppliers based on their ability to match product ﬂow to actual customer demand. As a result,
manufacturers and distributors are feverishly working to reengineer their businesses and correspondingly redirect their
information systems to focus on satisfying customer demand through efﬁcient, cost effective, and accurate order fulﬁllment.
Aberdeen observes that IMI's System ESS pushes the envelope of traditional supply-chain management capabilities with
System ESS's pull-driven, customer-demand-requirements model that manages the ﬂow of information from the customer
back through the manufacturing enterprise. In addition, System ESS provides a feature-rich promotions management
capability that lays down the foundation for improved enterprise logistics productivity and value-added customer service, as
evidenced by IMI's notable success in the Consumer Packaged Goods (CPG) and wholesale distributor markets.
This Proﬁle discusses IMI's System ESS from the perspective of business process functionality, market ﬁt and the
technological underpinnings of the product architecture for Internet deployment today and evolution to distributed object
technology in the near future.
Executive Overview
Aberdeen holds that information is the single most strategic weapon for gaining competitive advantage as the
manufacturer/distributor world changes to a demand-driven business process. The open exchange of competitive-advantage
information allows manufacturers and distributors to synchronize their operations to achieve greater levels of efﬁciency and
improve customer responsiveness and satisfaction.
Demand-chain management solutions give manufacturers and distributors the requisite information processing tools to
quickly turn data into customer service information. Aberdeen ﬁnds that tools such as System ESS can play a critical role in
helping an enterprise increase efﬁciency and build a highly responsive and effective customer-centric order fulﬁllment
business system.
Aberdeen has determined that forward-looking distributors planning to manage their internal processes to support a
customer-centric business model must:
• view customer service as a way of doing business;
• tailor order entry, invoicing, and shipping to the customer's business;
• handle and process product orders efﬁciently and accurately; and
• be able to effectively manage sales and marketing promotional activities.
Aberdeen research also indicates that manufacturers and distributors planning to become more competitively positioned by
replacing their legacy systems with new Client-Server Solutions (CSS) such as ERP systems should look for order
fulﬁllment solutions, such as IMI's System ESS, that balance and leverage these ERP solutions.
Market Position
IMI has acquired strong technical expertise from 25+ years in global order-fulﬁllment/logistics management and from
implementing over 150 systems worldwide. IMI's System ESS business solution is intended to meet today's sophisticated
customer-centric order fulﬁllment requirements. It is grounded in a sound technical architecture well suited to promote
encapsulating customer-hardened business logic and information for accurate planning and forecasting. The company
intends to further its customer value proposition by extending System ESS to provide full Internet-enablement and
distributed object-oriented methods and capabilities.

IMI targets its System ESS solution at fast-moving, high-volume enterprises with annual sales of $250 million and over in
the consumer and industrial products, business equipment, and wholesale distribution industries. These targeted-vertical-
market companies typically are seeking solutions to the complex logistics challenge of effective order fulﬁllment.
To be competitive in a fast growing market, Aberdeen research indicates that a solution supplier must support a growing list
of demanding requirements. IMI is noted as being in an advantageous market position when System ESS functionality is
evaluated. Aberdeen ﬁnds that competitive order fulﬁllment CSS offerings must be able to provide manufacturers and
distributors with the ability to manage:
• a broadening of product portfolios;
• multi-national distributors;
• reduced delivery response times;
• frequent and customer-speciﬁc product promotions;
• lowering of inventory levels;
• rapidly changing customer behavior; and
• more complex manufacturing strategies, involving global sourcing from internal and outsourced manufacturers and
suppliers.
Products/Key Technologies
Product Overview
System ESS is a UNIX- and NT-based CSS that gives manufacturers and distributors of fast-moving, high-volume consumer
and industrial products a means of managing their business more effectively. System ESS provides capabilities to manage
the demand-chain, including order cycle, price and promotions management, demand replenishment, electronic commerce
and logistics activities. System ESS can efﬁciently support large user counts and substantial amounts of data while
maintaining superior system performance by exploiting Oracle's relational database technology and making judicious use of
caching algorithms for frequently accessed program modules and data. System ESS manages the information ﬂow of
customer order requirements back through the manufacturing enterprise to improve logistics productivity and value-added
service levels. Refer to Table 1 for list of IMI modules.
Product Architecture
IMI's System ESS is based on a distributed, three-tier, client-server architecture — separating presentation, application and
database functionality — grounded in open, industry-standard technologies. System ESS supports standard Windows-based
Graphical User Interfaces (GUIs), leading UNIX-based and WindowsNT-based server platforms, and a common data model
implementable across industry-standard Relational Database Management Systems (RDBMS).
Laying open the outer shell of System ESS exposes the heart of the layered modular substructure, designed from its
inception to isolate business logic from database access and application user interface implementations. Refer to Figure 1.
Modularity of Design
System ESS Application Layer — System ESS applications consist primarily of on-line and batch/report modules. The
modular design of the applications is made possible by using the IM Data Dictionary (IM*DD). All business logic initiated
by the application layer is executed by the System ESS Core Services layer. The event-driven application logic capability is
also used to present information to the user and to occasionally access the database directly when the System ESS Core
Services need to be extended or customized for a speciﬁc business.
Vortex the Database Access Layer — Vortex, an independently supplied database access technology from Trifox, is used to
provide application-transparent access to heterogeneous RDBMSs. Isolating the database function as IMI has done permits
any combination of local or distributed database deployment. Aberdeen ﬁnds this deployment ﬂexibility to be a vital
contribution to system-wide performance.
System ESS Core Services Layer — The essence of System ESS's order fulﬁllment-differentiating business logic is encoded
in the System ESS Core Services layer. This layer establishes isolation from computing platform and system interfaces and
provides for a high degree of System ESS portability.
Among other attributes, the System ESS Core Services layer isolates the user presentation from the business logic. This
separation also delivers interoperability beneﬁts because regardless of the originating source — batch, character or GUI
terminal, event-based occurrences of EDI or legacy systems — constancy of implementation and execution is assured.
Furthermore, the layer establishes a central point for instituting database access performance concepts. Concepts such as
optimistic locking compensate for variations in RDBMS data-locking methods while providing a single and efﬁcient
application-based method of operation.
Development Environment
System ESS's development environment is based on a common data model covering the information needs of all users
within an enterprise. System ESS uses popular, open, relational database technology and adds effective tools to store and
retrieve information. The IM*DD repository maintains a single and constant description of all domains, data elements and
their relationships. This meta data repository is accessed by all applications for such things as ﬁeld attributes and data
validation and to provide event triggers for initiating actions when a ﬁeld is entered or a function key is pressed.
TRIMtools from Trifox Inc. is an integrated set of development tools for database and data management applications. IMI
chose TRIMtools in order to build System ESS to be independent of hardware or software platforms. The resultant System
ESS applications are interfaced with another Trifox product, VORTEX, to provide System ESS application transparent
interoperation with the underlying RDBMS.
Customer Service Workbench (CSW)
CSW is a set of client-server, Microsoft Windows-based software tools that integrate the System ESS data repository with
client-based decision support capabilities such as spreadsheets, electronic mail, and alert facilities.

ESS Alert — is a workﬂow-enabling technology that proactively monitors demand-chain activities and provides rules-based
notiﬁcation using user-deﬁned triggers to electronically notify users when certain situations occur or do not occur.
Systems Integration
ESS Event Manager — is a general-purpose communications interface that handles gateway trafﬁc to/from internal legacy
systems and EDI trafﬁc to/from external trading partners. System ESS can be seamlessly connected to legacy systems using
the ESS Event Manager that also allows integration of legacy applications with the System ESS database. Thus the ESS
Event Manager helps customers to continue leveraging value from their existing systems by integrating with both legacy and
new client-server manufacturing, planning and ﬁnancial information systems.
ESS Event Express — is a communications tool kit designed to simplify real-time communication by providing integration
and visibility between System ESS and other mission critical systems.
Figure 1: System ESS Layered, Modular Architecture
Source: AberdeenGroup and IMI, January 1997
Oracle Financials Integration — System ESS is able to tightly integrate with the Oracle Financials CSS to become part of a
total client-server order management and cash settlement solution.
Decision Support Integration — Business Object's query, reporting and analysis solution offers improved decision-support
capabilities and meaningful access to manufacturing, logistics and customer service data, enabling enterprises to respond
more effectively to customer inquiries.
Strategies/Product Direction
Aberdeen considers IMI well poised to be a leading provider of demand-chain order fulﬁllment solutions to multinational
manufacturers, distributors and wholesalers. To accomplish this System ESS must manage the ﬂow of customer-unique
information back through the enterprise to create a customer-centric, pull-driven ﬂow of goods. The key empowering
elements of IMI's current strategy are to:
• enhance the core functionality of System ESS — increase throughput capacity and overall performance, add customer
requested functions;
• target speciﬁc vertical industry markets;
• integrate System ESS with complementary products — align with other vendors for planning, manufacturing, ﬁnance
and decision support;
• establish partnerships to assist in developing customer relationships and implementing System ESS — work with
systems integrators; and
• expand worldwide sales and support organization — expand presence in North America, Europe, and Asia Paciﬁc.
Aberdeen believes that additional IMI target markets should include: wholesale distribution and pharmaceutical/healthcare.
To these markets, IMI will need to stress its ability to enhance an organization’s external focus on suppliers and customers,
and its potential for cutting costs and increasing customer/supplier rapid-reaction via purchase order, price/promotion
management, and warehouse management.
Table 1: Product Line Breakdown
Product Distribution
Decision Support
Order Management
Customer Service Workbench
Logistics Management
Economic Value Analyzer
Price and Promotion Management
Business Objects
Inventory Management
Electronic Commerce
Demand Replenishment
EDI Workbench
Global Organization Management
Internet Commerce Workbench
Internet Strategy — Internet Commerce Workbench (ICW)
IMI's Internet strategy centers on enabling greater interaction between clients and their customers, improving customer
service while adding value to trading partnerships. Aberdeen supports IMI's intention to enable manufacturers and
distributors to go beyond today's read-only, Internet-browser applications to be able to conduct their business more
interactively and in real-time.
Currently delivering on their vision — ICW, a TRIM-based Toolkit, supports the development of Web pages and facilitates
the read-only integration between the Internet World Wide Web (WWW) and System ESS. IMI-supplied templates give a
jump start to customer development of Web pages written in Hyper Text Markup Language (HTML). Using current Internet
browser technology, customers and sales organizations can access business-critical information directly from the corporate
repository. Furthermore, IMI's openness of design allows both Netscape's Composer and Microsoft's Front Page to be used
to develop System ESS Web Pages.

ESS Order Tracker — is the ﬁrst add-on Web browser application component of the ICW. ESS Order Tracker gives users
shipping and order information through the Internet and Intranets. This capability can free up valuable customer service
resources and reduce costs by off loading many routine inquiries to the client user.
Additional ICW browser component offerings like historical purchases and available-to-promise (ATP) are shipping with
System ESS Version 4.3. Future extensions will include: the ability to update order entry data and obtain order
acknowledgment; a security layer; and the use of the Java language to create interactive Web pages.
Future Product Strategy — Evolution not Revolution
IMI has begun the process of moving its System ESS software into the advanced-state-of-the-technology arena of object-
oriented and fully web-empowered applications. IMI plans to move their System ESS offering in three major
implementation/migration phases:
• Phase I — surrounding the System ESS Core Services with ever increasing Object-Oriented (OO) and Internet
enabling technologies;
• Phase II — OO ESS applications replace procedural ESS application; and
• Phase III — Object-Relational DBMS replacing RDBMS technology.
Phase I will establish a series of steps consisting of surrounding or encapsulating the System ESS Core Services with object-
oriented and Internet-enabling layered modules and interfacing technologies as follows:
• continued support for GUI access through the Application Layer;
• additional Internet browser applications accessing the ICW Layer;
• object encapsulating the System ESS Core Services Layer;
• exposing the System ESS Core Services layer as methods on ESS objects;
• adding an Object Request Broker (ORB) layer to dispatch object requests to the System ESS Object Services Layer;
• creating Java applets for ORB access to the System ESS Object Services Layer;
• creating new System ESS enhancements as OO System ESS using OOP tools;
• adding OLE Layer desktop support for access to ORB and System ESS Objects;
• adding new/upgraded functionality as OO System ESS object applications; and
• providing direct interface access through APIs directly to the TRIM database layer.
IMI plans to deliver Phase I enhancements with Version 5 of System ESS beginning in Q1 1997. Aberdeen ﬁnds the key to
this phased approach is IMI's ability to provide continued fully-functional System ESS business value with the already well
proven System ESS Core Services Layer. Customers adopting or migrating to the new System ESS technology will not have
to sacriﬁce any System ESS functionality.
Sales and Distribution
IMI was founded in 1967 with headquarters in Stockholm, Sweden. IMI sells and supports its products through direct sales
and support organizations in Sweden, the United States and the United Kingdom. To enhance implementation and support
service capabilities, IMI has marketing and sales partnership arrangements with a number of consulting and systems
integration ﬁrms.
Table 2: Supported Technology Platforms
Platform
Product Suite Name
Hardware Client:
Intel PCs: Windows 3.1x, Windows 95, NT Workstation
Server: Digital Equipment: DEC Alpha, Digital Unix
Hewlett Packard: HP9000, HP/UX
IBM: RS/6000, AIX
Microsoft: WindowsNT *
Sequent: Symmetry, Dynix
Sun: Solaris * ( * available Q197)
Database Server: Oracle 7
Network:
TCP/IP
Competition
IMI competes in the Enterprise Resource Planning (ERP) and Supply Chain Management (SCM) markets. However, this
ERP-SCM marketspace has literally exploded with opportunity and many companies populate this overall space.
Competitors loosely fall into categories of fully-integrated suite or best-of-breed point-solution. Among the ﬁrst group are
Baan, J. D. Edwards, Oracle, PeopleSoft, Pivotpoint (formerly Spectrum Associates), PowerCerv, QAD, SAP, and SSA. The
best-of-breed crowd includes Industri-Matematik International Corp. (IMI), American Software, FourGen, i2 Technologies,
Numetrix, Manugistics, and SynQuest (formerly Fact).
Demand-side software innovation in enterprise computing is particularly important to Fortune-class manufacturing
companies because they are able to create a more elaborate feedback loop. The desire to link production and demand has
long simmered in the consumer goods segment — especially in areas of fast-moving goods — where companies that can
meet that challenge will experience lower costs, reduced inventories, better customer service, lower prices and fewer
mistakes.

IMI’s targeting of the CPG and closely-related high-volume, fast-moving markets, has established a major beachhead in
these markets for the company. IMI differentiates itself by its emphasis on independent line-item ﬂexibility, an impressive
customer list, Internet capabilities and vision, scalability for large volume transaction environments, promotion
management, and close integration between a customer-focused approach and enabling software.
Financials
Publicly traded (NASDAQ: IMIC), IMI's FY96 (4/30/96) revenues were $40 Million. $18M was from North American
operations which represents a nine-fold increase in two years. In September 1996, IMI had a successful IPO, generating
$33M in working capitol.
Aberdeen Conclusions
Consumer Packaged Goods (CPG) is one area where best-of-breed point-solution vendors, such as IMI, are competing
aggressively. Enterprise software applications are making their way into manufacturing market segments as companies seek
ways to meet consumer demand with manufacturing strategies. Best-of-breed point-solution suppliers are providing the
components enterprises need to create an infrastructure of best-business processes across the supply-chain. IMI's System
ESS has consistently scored well in this area with signiﬁcant Fortune 500 customer wins. IMI is considered by these
enterprises as providing viable and compelling alternatives for demand-chain management with superior line item
independence and promotion management facilities.
IMI's System ESS is empowering companies to become world-class, demand-chain management enterprises. By bringing
together the System ESS demand generation and fulﬁllment solution with supply-chain-wide business processes, IMI is
poised to be a leading market supplier of customer service and customer-centric demand- chain management solutions and is
particularly well designed for fast-moving, high-volume markets like CPG, consumer durables, and wholesale distribution.
IMI's System ESS is providing enterprises with a more precisely matched product ﬂow to actual customer demand. The
rewards for an enterprise successfully implementing a customer demand-driven approach — meeting customer delivery
expectations — are many but a few signiﬁcant ones are:
• reduced inventories,
• reduced cycle times, lower costs,
• fewer mistakes, better customer service and
• lower prices for customers.
Assessing solutions capable of supporting this approach, Aberdeen considers IMI's System ESS a great choice for best-in-
class demand-chain management — due in part to its superior functionality and market agility developed by working
cooperatively with major consumer and industrial product businesses worldwide.
Over the next few years, IMI will need to rapidly continue its planned technology upgrade path to keep an industry-leading
position in the company's focused industry markets. For example, IMI will need to complete its Internet vision and to fully
exploit object-oriented technologies such as objects and object brokers within its applications; recruit more partners to add
functionality to its model; and expand into adjacent markets. Aberdeen believes IMI’s experience and customer-focused
architecture will allow it to adapt swiftly to changes in its targeted markets.
In summary, Aberdeen recommends to CSS buyers looking to realize the potential that leading demand-chain solutions can
deliver — especially when quick implementation, high performance and interoperability with existing business-critical
systems is essential — should put IMI's System ESS at the top of their lists.
AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #: 617.854.5212)
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
This Document is for Electronic Distribution Only
-- REPRODUCTION PROHIBITED --
Copyright © 1997 Aberdeen Group, Inc., Boston, Massachussetts
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless
otherwise noted, the entire contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval
system, or transmitted in any form or by any means without prior written consent of the publisher.


---

## Frictionless Data Package Metadata

**Study ID:** 1997-industry-matematik-international-co-c398bc
**Title:** Industri-Matematik International Corp.: Strategic Solution for Fast-Moving, High-Volume Goods Industries
**Author:** Aberdeen Group
**Date:** 1997-01-01
**Type:** profile
**Subject Domain:** ERP / Supply Chain Management / Order Fulfillment Software
**License:** CC-BY-4.0
**Importance:** 4/5
**Relevance:** 4/5
**Prescience:** 4/5

### Importance Rationale
Primary source documenting a niche but significant ERP/SCM vendor at the moment of its IPO and peak visibility. IMI's demand-chain pull model was prescient — it prefigures modern demand-driven supply chain management. The study documents the 1990s ERP landscape and best-of-breed vs suite competition at a pivotal moment.

### Relevance Rationale
Directly relevant to the history of supply chain software, ERP/SCM market evolution, and the best-of-breed vs integrated suite debate. IMI's survival and recent resurgence as a niche SCM provider make this study valuable for understanding durable specialized vendors.

### Prescience Rationale
Aberdeen correctly identified demand-chain pull management as the future direction of supply chain (accurate: S&OP, demand sensing are now standard); Internet enabling of order management (accurate: B2B e-commerce); and need for object-oriented migration (accurate though IMI's specific path evolved). Aberdeen's recommendation to expand to pharma/healthcare proved partially correct. IMI survived the ERP consolidation wave as a specialist — as Aberdeen predicted for best-of-breed vendors.

---

## Prescience Detail

### Predictions Made (1997)
- **IMI Phase I OO/Internet migration (Version 5, Q1 1997)**: IMI to deliver ORB/Java/OO encapsulation of ESS Core Services in V5 starting Q1 1997
- **IMI as leading demand-chain solutions provider**: Aberdeen considers IMI well-poised to be leading provider of demand-chain order fulfillment solutions

### Actual Outcomes (Verified)
- **SAP market position outcome** (2024): SAP became dominant ERP suite vendor; market cap ~$250B in 2024
- **PeopleSoft acquisition by Oracle** (2005): Oracle completed hostile acquisition of PeopleSoft for $10.3B in January 2005
- **Baan Company acquisition/decline** (2000): Baan acquired by Invensys 2000; later became part of Infor via SSA GT
- **IMI identity and brand evolution** (2019): IMI renamed Aptean AB ~2012; rebranded back to Industri-Matematik International AB March 2019
- **IMI acquisition by Priveq Investment** (2021): Priveq became majority owner of IMI January 2021; enabled acquisition-driven growth
- **Business Objects acquisition by SAP** (2007): SAP acquired Business Objects for $6.78B in 2007
- **IMI 60-year anniversary and current status** (2026): IMI celebrates 60 years in 2026; six acquisitions since 2021; offices in four countries; doubled revenue and headcount
- **i2 Technologies / JDA / Blue Yonder evolution** (2020): i2 merged with JDA Software 2010; JDA rebranded Blue Yonder 2020; Panasonic acquired 2021
