# Enterprise Information Integration: The New Way to Leverage E-information (Second Edition)

> Archived from: source/_raw_text.txt
> Original publication date: 2003-07
> Author: Aberdeen Group

---

## Original Document Text

AberdeenGroup




                Enterprise Information Integration
                  The New Way to Leverage E-information




                              Second Edition
                                 July 2003
Aberdeen Group, Inc.
Aberdeen Group is a leading IT market analysis and positioning services firm that
helps information technology vendors establish leadership in emerging markets.
Aberdeen Group performs specific projects for a select group of domestic and in-
ternational clients. Each project requires a combination of strategic advice and
pragmatic, experience-based action plans. Assignments range from corporate and
product positioning and organizational planning to in-depth market segment re-
search. Aberdeen consults on mergers and acquisitions, corporate positioning and
investor relations, and transaction-processing benchmarks; in addition, it offers
special expertise in software and midrange computer markets.
In carrying out assignments, Aberdeen uses a proprietary, comprehensive, ana-
lytical framework providing fresh insight into the complex future of computing
and communications, both from technological and market-dynamics perspectives.
Aberdeen also offers retainer-fee programs to a group of continuing clients.
Aberdeen principals and staff are recognized industry figures with hundreds of
years of combined high-tech industry, research, and financial community experi-
ence among them. They are quoted extensively in industry trade and business
publications. Each staff member is a frequent conference and seminar speaker.
In addition to client-related research and consulting, Aberdeen publishes several
periodicals, Aberdeen Viewpoints, and Profiles, which summarize its analysis and
research findings.
To provide us with your feedback on this research, please go to
www.aberdeen.com/feedback.
The information contained in this publication has been obtained from sources Aberdeen believes to be reli-
able, but is not guaranteed by Aberdeen. Aberdeen publications reflect the analyst’s judgment at the time
and are subject to change without notice.
The trademarks and registered trademarks of the corporations mentioned in this publication are the property
of their respective holders.
Warning: This publication is protected by United States copyright law and international treaties. Unless oth-
erwise noted, the entire contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior written
consent. Unauthorized reproduction or distribution of this publication, or any portion of it, may result in severe
civil and criminal penalties, and will be prosecuted to the maximum extent necessary to protect the rights of
the publisher.
© 2003 Aberdeen Group, Inc., Boston, Massachusetts
              Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Table of Contents

  Preface ................................................................................................................ 1

  Chapter One: Executive Summary ...................................................................... 3

  Chapter Two: Summary of Findings..................................................................... 6

  Chapter Three: Market Definition and Dynamics ............................................... 10
     What Is EII, and How Does It Work?............................................................10
         EII Is New Technology ...........................................................................12
         EII in the User Site.................................................................................12
         Situations in Which Today’s Companies Often Feel a Need for EII........13
         Business Benefits of EII.........................................................................14
         Applying EII to Typical IT Tasks .............................................................15
         Criteria for Buying an EII Solution..........................................................18
         Critical Technology Factors....................................................................20
         Object, Multimedia, and Non-database Support ....................................20
         Specific Front-End Support....................................................................21
         Developer Support.................................................................................23
         Administrator Support ............................................................................23

  Chapter Four: EII As Part of Strategic Information Management ....................... 25
     A Brief Introduction to Strategic Information Management ...........................25
         What Is Information Aggregation, and Why Does It Matter? ..................26
         When to Apply What Information Aggregation Technology ....................30
         The State of the Art in Information Aggregation .....................................30
         Action Items...........................................................................................38

  Chapter Five: Market Forecast and Segmentation ............................................ 40
     Key Technologies for EII Initiatives...............................................................40
     Aberdeen EII Technology Segmentation Model............................................40
         EAI.........................................................................................................41
         Database Technologies..........................................................................42
         XML Messaging Technologies ...............................................................43
         Combinations of Technologies ...............................................................43
         Summarizing the Model .........................................................................44
     Growth Forecasts.........................................................................................47


                                                                                                           AberdeenGroup • i
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




          Table of Contents

               Chapter Six: Aberdeen Observations..................................................................49
                  Impact of Major IT Trends ............................................................................49
                      Application Servers................................................................................49
                      The Role of Java ...................................................................................49
                      Extensible Markup Language (XML) .....................................................50
                      Emphasis on Cost-Effective Administration ...........................................50
                      Enterprise Portals ..................................................................................50
                      Web Services ........................................................................................51
                  Supplier Success Factors ............................................................................52
                      Success Factors for Organizations........................................................52
                  Aberdeen Observations and Conclusions ....................................................54
                  Positioning and Capabilities .........................................................................54
                      Market Segmentation ............................................................................54
                      Technology Interdependency.................................................................54
                      Distribution and Implementation ............................................................55
                  Major Forces ................................................................................................56
                      Mergers and Acquisitions (M&A) ...........................................................56
                      Standardization and Integration.............................................................56
                  Success Factors...........................................................................................56
                  The Future ...................................................................................................56

               Chapter Seven: Supplier Profile .........................................................................58
                  MetaMatrix, Inc. ...........................................................................................59

               Author Profile......................................................................................................63

               Appendix A: Lexicon of Acronyms and Abbreviations .........................................64

               Appendix B: Related Aberdeen Research ..........................................................66

               Appendix C: Supplier Contact Information.........................................................67




ii • AberdeenGroup
            Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Figures

  Figure 1: EII in a Typical Architecture..................................................................11

  Figure 2: Example of Information Aggregation Architecture............................... 30

  Figure 3: EII Technology Segmentation Model .................................................. 44


Tables

  Table 1: Ways to Use EII in Strategic Initiatives................................................. 15

  Table 2: EII versus Traditional Approaches ........................................................ 18

  Table 3: EII Constituents and Their Data Needs ................................................ 21

  Table 4: Strategic Uses of Information Aggregation ........................................... 28

  Table 5: Taxonomy of Information Aggregation Tools......................................... 31

  Table 6: EII and Related Suppliers..................................................................... 45

  Table 7: EII and Related Suppliers.................................................................... 46

  Table 8: EII Supplier Revenues (Aberdeen Estimates, Projected over 2003) .... 47

  Table 9: Revenues for Markets Related to EII.................................................... 48




                                                                                             AberdeenGroup • iii
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Preface
Enterprise information integration (EII) is now a market separate
from enterprise application integration (EAI) and extract-transform-
load (ETL) solutions.
The main reason that companies now recognize a distinct need to
integrate information across the enterprise is that the overall pool of
proprietary enterprise information  as distinct from information
associated with specific packaged applications, Web databases, or
data mining sources  is now a key e-business differentiator. The
ability to leverage information from a wide variety of storage types,
environments, applications, databases, and files via enterprise portals
allows enterprises to deliver major value-add simultaneously to em-
ployees, partners, and customers.
A second reason to look closely at EII is that  as Aberdeen re-
search shows  firms are now at a critical stage in linking back-end
applications and data to their front-end Web sites. Three years of
fragmented efforts to link key applications one by one, followed by a
proliferation of enterprise portals that crisscross various back-end
data sources, have left companies with unnecessarily complex and
costly e-business architectures. The key to cutting administrative and
new application development costs is to implement a common soft-
ware infrastructure architecture  and EII infrastructure lies at the
core of such an architecture.
Third, the requirements of e-business are a superset of the require-
ments of traditional information processing. A narrow definition of
data integration as being concerned only with integrating informa-
tion within a company must change to encompass EII’s integration of
information between companies as well.
This report provides the reader with a clear understanding of the
forces influencing the market, as well as Aberdeen’s insights into the
real opportunities and benefits of EII and its future directions. The
second edition follows up the information published in May 2002 to
include major new suppliers and new trends. The report includes the
following:
•   Technology segmentation — An update to the Aberdeen
    segmentation model that indicates various technology
    approaches to EII and the suppliers supporting those technolo-
    gies

•   Market size and growth projections — Aberdeen’s most recent
    data on EII market size and growth



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 1
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    Issues and challenges — An outline of additional industry
                                        trends that are affecting EII initiatives

                                   •    Observations and conclusions

                                   •    Supplier profiles — A comprehensive list of the suppliers in this
                                        market

                                   The intended audience for this report is IT (information technology),
                                   corporate, and line-of-business management responsible for planning
                                   and managing initiatives for information integration, as well as
                                   communicating and interacting effectively with potential distributors
                                   and suppliers. This publication was designed to help these users
                                   understand the potential impact of information integration regarding
                                   the following:
                                   •    An enterprise’s total application portfolio

                                   •    Enterprise information strategies

                                   •    E-business planning and execution

                                   •    Present technologies, including Web services, which will under-
                                        pin corporate architectures over the next two to three years

                                   This publication profiles the key suppliers and products in the mar-
                                   ket. Aberdeen believes that this report will aid organizations in iden-
                                   tifying the technologies and attributes of EII products that can best
                                   fit their business requirements. It will also help organizations effec-
                                   tively plan EII acquisition strategies.




All print and electronic rights are the property of Aberdeen Group © 2003
2 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter One:
Executive Summary
Aberdeen research shows that the motivator of many e-enterprises is
not only cost savings but also competitive advantage. A slight Web
site advantage can cause customers across a global market to estab-
lish relationships; a slight but persistent disadvantage can, even to-
day, cause 10% to 20% of the installed base to walk away.
To create and maintain competitive advantage, enterprises have now
moved beyond pretty graphics, informational displays, and rudimen-
tary order taking. They have also connected their back-end order-
processing (B-to-C) and supply chain (B-to-B) applications to the
Web site  and, in some cases, with other companies’ Web sites or
with e-marketplaces. However, most of these efforts maintain sepa-
rate, uncoordinated links to one or more Web sites.
To integrate information at the user-interface level, enterprises are
now implementing enterprise portals. A portal allows the enterprise
to display data applications and fully leverage all major business-
critical company databases. However, by itself, an enterprise portal
does little beyond show data in different formats side by side.
To fully leverage the connections between information from differ-
ent applications and databases, an enterprise needs an EII infrastruc-
ture to aggregate data and coordinate transactions across back-end
data sources. At its most powerful, EII lets all back-end information
be seen as if it came from one comprehensive, global database.
The resultant Web site-based informational applications, or e-
information, do more than show the latest company news. As with
portals, they can serve as free advertising, attracting the information
researcher who is hungry to find a one-stop shop. They can comple-
ment customer relationship management systems by providing the
information desired at each point in the customer’s buying decision
process. Within an organization, they can tie the company together
and ensure faster, better decision-making. In some cases, such as
stock market reports and analysis, they can serve as money genera-
tors in their own right.
Along with these competitive advantages come built-in cost savings
 not only the cost savings from doing everything over the Internet,
outsourced or consolidated, but also the IT cost savings from simpli-
fying the administration of the database/application connections and,
thereby, saving key administrative costs. Moreover, users report that
developers writing to a common high-level database interface save



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 3
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   significant time in both development and upgrading data-intensive
                                   applications that cross data sources.
                                   Of equal importance is a side benefit: e-information can unify the
                                   enterprise’s archipelagoes of data. Whereas data warehouses failed to
                                   persuade data fiefdoms to merge, the Web site manager now has the
                                   political power to enforce common data standards on company divi-
                                   sions that seek the selling power of its Web site  but only if that
                                   manager plans ahead via an e-information strategy.
                                   A further note: Wringing Web site-displayed informational applica-
                                   tions, or e-information, from existing databases is not easy. Hence,
                                   competitive advantage is more durable and differentiation is easier.
                                   An early example of EII’s potential comes from the field of em-
                                   ployee self-service applications. EII plus an enterprise portal delivers
                                   an immediate impact to the bottom line by eliminating the need for
                                   “information intermediaries” that stand between the individual em-
                                   ployee and the information that he or she needs.
                                   The benefits of employee productivity EII do not end with the bot-
                                   tom line. For example, employee-productivity solutions based on EII
                                   provide additional information to employees, such as company poli-
                                   cies and standards or information about the company’s products, and
                                   they can deliver critical cross-database information in a just-in-time
                                   fashion. This information, in turn, can give users the ability to make
                                   higher quality, more rapid decisions because they can base their de-
                                   cision making on higher quality data that is more up-to-date. Visu-
                                   alization and personalization of the information can improve the em-
                                   ployee’s comprehension of the data. Improved accuracy of the in-
                                   formation can reduce the risk that company employees — or the
                                   company itself — will violate government regulations.
                                   However, one of the main potential advantages of EII is not yet on
                                   users’ radar screens — the ability to provide a common administra-
                                   tive locus for all major enterprise databases. Aberdeen research
                                   shows that database administration costs now dominate the TCO
                                   (total cost of ownership) of applications below the 500-user level,
                                   and they continue to increase in importance for all sizes of applica-
                                   tions. Users correctly identify the ability to manage multiple data-
                                   bases with one common interface as a major source of cost savings,
                                   but they often look to application servers as a method to achieve
                                   cross-database administration. However, full-featured EII, with its
                                   greater knowledge of database content, is much better suited to pro-
                                   vide database administration not only across a few applications at the
                                   Web site but also across many or all databases within the enterprise
                                   and even outside of it.
                                   In Chapter Three, Aberdeen describes how EII suppliers are meeting
                                   the challenge of delivering a “virtual federated database.” Aberdeen


All print and electronic rights are the property of Aberdeen Group © 2003
4 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



finds that providing a scalable, robust, low-administrative-cost solu-
tion is a tough nut to crack, but today’s EII solutions already provide
strong value-add by allowing the identification of new cross-
database, cross-application, and even extra-enterprise sources of in-
formation and data interrelationships. Today’s suppliers are, on the
average, larger and better able to provide supporting services than a
year ago, so users no longer need fear the perils of being pioneers.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 5
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Two:
                                   Summary of Findings
                                   •    Currently, EII is a small market  less than $200 million in size
                                         that lacks visibility to IT buyers. Over the last year, however,
                                        EII visibility has grown dramatically; this growth is especially
                                        due to IBM’s announcement of its Information Integrator prod-
                                        ucts.

                                   •    Buyers are beginning to see EII as a strategic infrastructure de-
                                        cision that can improve the agility of IT and enhance IT’s ability
                                        to quickly adapt technology to the rapidly changing needs of the
                                        business — especially the needs of e-business.

                                   •    The business benefit of EII increases exponentially with succes-
                                        sive integration of each related application and database. The
                                        connections between each additional information source and all
                                        the others have typically not been examined in most enterprises,
                                        and these connections  especially when combined with busi-
                                        ness process software  allow employee empowerment, greater
                                        insights into competitive advantage, more rapid response to cus-
                                        tomer inquiries and orders, and more effective integration with
                                        the databases of supply chain partners.

                                   •    EII solutions can enable and support today’s three high-priority
                                        e-business initiatives — customer relationship management, e-
                                        business integration across the supply chain, and Web-based
                                        employee productivity applications. Moreover, they offer a way
                                        to speed up business-process-integration efforts by allowing
                                        simultaneous access to multiple databases attached to multiple
                                        applications.

                                   •    Partial deployment of intranet, extranet, and Internet applica-
                                        tions without EII increases the difficulties of implementing EII,
                                        but also increases the costs of failing to implement EII by in-
                                        creasing the costs of administering unnecessarily complex archi-
                                        tectures.

                                   •    The EII market is still new, and most EII suppliers are small
                                        ones, such as MetaMatrix, Venetica, XAware, Enosys, and
                                        Nimble Technologies. Over the past year, large firms have be-
                                        gun adding the technology  BEA is contracting with Enosys
                                        to provide EII as part of BEA’s Liquid Data for WebLogic ini-
                                        tiative, and IBM’s Xperanto EII project has resulted in the new
                                        IBM DB2 Information Integrator products.


All print and electronic rights are the property of Aberdeen Group © 2003
6 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   EII-type functionality is a cornerstone of today’s more success-
    ful enterprise portals and of the Web services that enterprises are
    beginning to build. Initial EII implementations are project spe-
    cific and seek to simplify developer interfaces in which portals,
    Web services, and similar software makes cross-database que-
    ries.

•   Many EII suppliers have experience in data integration and data
    warehouse ETL. These suppliers’ experience in optimizing data-
    transmission performance across databases means that today’s
    EII solutions are by no means bleeding edge; in fact, they often
    offer the robustness and scalability of mature technologies. The
    advent of larger suppliers — such as BEA, Business Objects,
    and IBM — ensures that IT buyers will run fewer risks of sup-
    plier failure or inadequate service.

•   The potential of the EII market will mean that major hardware
    and database suppliers will continue to enter the market within
    the next two years, either by acquisition or by partnerships with
    existing EII suppliers. The entry of these suppliers will continue
    to increase EII’s visibility, allowing them to parlay advanced
    technology-based solutions and industry relationships into large-
    scale enterprise opportunities. If successful, these suppliers will
    fuel a $250 million-plus market over the next two years. In-
    creasingly, EII solutions will be incorporated in portal, EAI,
    business intelligence, and business-process-integration solu-
    tions, making EII a key technology in a $7.5 billion market.

•   Over the next two years, EII will begin to form part of a larger
    “information aggregation” market aimed at delivering tools for
    strategic, proactive information management. EII will be a key
    enabler for identifying, managing, and leveraging competitive-
    advantage proprietary information and information relation-
    ships.

•   EII can play an effective role in exposing enterprise data to out-
    side suppliers in supply chain and e-business integration solu-
    tions.

•   The strength of industry partnerships  professional services
    and systems integrator firms, enterprise portal and application
    suppliers, and system infrastructure suppliers  and of the con-
    sulting that EII suppliers provide on how to best utilize EII is as
    critical to EII implementers’ success as the technology that the
    suppliers offer. IT evaluators should be looking especially to
    those EII suppliers that continually enhance their capabilities
    across all three of these dimensions.



                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 7
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    One key EII supplier technology differentiator is the degree to
                                        which a supplier uses XML (Extensible Markup Language)
                                        technology for inter-database integration. The XML approach
                                        makes it easier to deliver the resulting aggregated data to a wide
                                        variety of inter- and extra-enterprise audiences. Another is sup-
                                        port for SOAP and Web services.

                                   •    Finding the appropriate skills to execute an EII project is not
                                        always easy, as EII implementation requires in-depth knowledge
                                        of the structure of existing enterprise databases. This will pro-
                                        vide a business opportunity for professional service suppliers
                                        and for application service providers (ASPs) that offer EII inte-
                                        gration services.

                                   •    Evaluators should favor EII solutions that allow users to define
                                        the databases to be integrated and provide developer-friendly
                                        user interfaces for doing so; support a wide variety of databases;
                                        and provide customized support for “de facto standard” applica-
                                        tion interfaces (e.g., enterprise portals) and delivery mechanisms
                                        (e.g., XML).

                                   •    At present, no EII solution offers administration across data
                                        sources. However, this capability is a key value-add to many us-
                                        ers. EII’s ability to drive down database administration costs
                                        will reduce per-application TCO significantly.

                                   •    In many organizations, the same team that monitors the server
                                        farm should make the EII buying decision. This requirement
                                        stems from the fact that understanding the enterprise’s e-
                                        business architecture is key to effective implementation of EII
                                        and new applications that leverage EII.

                                   To fully reap the benefits of EII, evaluators should also apply the
                                   following assessment criteria:
                                   •    Extensibility and reusability — The integration process should
                                        be extensible and reusable for the project at hand, as well as for
                                        future projects. The tools should be designed in such a manner
                                        that users can extend the tool from a per-project basis to an on-
                                        going enterprisewide usage.

                                   •    Flexibility — The solution should be able to fit into an existing
                                        architecture and handle new technologies without massive
                                        rewrites and without involvement from the supplier.

                                   •    Efficiency — The solution should be capable of operating across
                                        a wide range of performance levels (e.g., very fast, fast, moder-




All print and electronic rights are the property of Aberdeen Group © 2003
8 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



    ate, and overnight) and integration models (e.g., asynchronous
    messaging and synchronous transaction).

•   Interoperability and breadth — The solution should understand
    the relationships between various database technologies and
    provide interfaces to interdependent middleware technologies
    such as application servers.

•   Cost-effectiveness — In the long term, the solution should be
    able to contribute to an organization’s bottom line by reducing
    the cost and risk of developing and maintaining custom, one-off,
    EII solutions. The upside value of a common repository of in-
    formation for all major enterprise databases is immeasurable.

•   Ease of maintenance — In EII projects that involve the integra-
    tion of many data sources, maintaining independently coded
    modules for each integration process is extremely resource in-
    tensive and, hence, costly. Using a single, flexible, and consis-
    tent development framework for each process will greatly re-
    duce the amount of personnel resources needed to maintain and
    develop the system.

•   Deployment ease and efficiency — Deploying the runtime envi-
    ronment should be easy, and the EII solution should allow de-
    ployment to a wide variety of target systems, ensuring optimal
    use of the enterprise network. Upgrade deployment should also
    be simple.

•   Ease of administration — EII modules will be distributed
    widely across an enterprise  just as enterprise-packaged appli-
    cation modules are today  and conceivably across enterprises
    where a supply chain relationship exists. These integration mod-
    ules will need to be managed and administered with no less
    diligence than is applied to current systems, networks, data-
    bases, and applications.

•   Industry acceptability — A large number of partners should
    incorporate the EII technology and deliver solutions based on it.

•   Technological innovation — The solution should provide and
    fully exploit the latest integration technology.




                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 9
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Three:
                                   Market Definition and Dynamics

                                   What Is EII, and How Does It Work?
                                   EII is software that provides a “database veneer” that makes dispa-
                                   rate data sources appear as one database. It allows users to apply data
                                   management transactions to the pooled data, at a corporate or enter-
                                   prise level, in order to support applications that manage, present, or
                                   analyze the data in new ways.
                                   Currently, EII has three key technical characteristics:
                                   •    It is a software infrastructure. It is not an application; it supports
                                        the creation of applications, such as enterprise portals, that dis-
                                        play and analyze combined data. As software infrastructure, EII
                                        forms a key part of any overall e-business architecture.

                                   •    It links the second and third tiers of a typical enterprise architec-
                                        ture in a “many-to-one-to-many” approach. In other words, EII
                                        gives a wide variety of second-tier Web applications running on
                                        the second tier of an e-business architecture access to multiple
                                        back-end and legacy databases and file systems running on the
                                        third tier.

                                   •    It provides an enterprise-scale, integrated approach. Unlike to-
                                        day’s point-to-point application-to-database links, EII provides
                                        a common infrastructure on which all links are built, incremen-
                                        tally if the customer wishes. This common infrastructure can de-
                                        liver more rapid development, more cost-effective centralized
                                        administration of data from multiple data sources, and more
                                        flexible presentation and analysis of more data sources.

                                   All EII products usually offer certain basic components:
                                   •    A directory — This “database about databases” contains infor-
                                        mation about the data stored in the databases and often contains
                                        the same information that is stored in each database’s data dic-
                                        tionary, as well as information about the data that is shared
                                        across databases. A directory may also include information
                                        about “normalized” versions of the data  i.e., data converted
                                        into a common format that is particularly suitable for passing on
                                        to users, Web sites, or enterprise portals.

                                   •    Conversion capabilities — An EII solution must often convert
                                        incoming data from nonrelational to relational format or from
                                        relational to object format. When updates to back-end databases


All print and electronic rights are the property of Aberdeen Group © 2003
10 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



    are involved in a transaction, an EII solution must also perform
    the “inverse” task of converting a common format back into the
    target database’s format. Note that current EII solutions that
    support updates do so under strict conditions and/or the user’s
    control.

•   A database veneer — To the user, the EII solution should look
    like a database and, if possible, to the developer and administra-
    tor as well. Therefore, the EII solution should at least support
    standard SQL and querying transactions.

•   Front- and back-end communications — The EII solution
    should have a way of communicating with front-end programs
    and with users via programmatic and communications invoca-
    tions. It also should be able to send transactions to and receive
    results from back-end databases.

Figure 1 shows how EII fits into a typical architecture.

Figure 1: EII in a Typical Architecture




                                            Source: Aberdeen Group, July 2003




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 11
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   EII Is New Technology
                                   The IT buyer should carefully distinguish an EII solution from an
                                   ETL engine for data warehousing, an EAI solution, or a content
                                   management system. An ETL engine (sometimes called a “data inte-
                                   gration” solution) allows multiple streams of data to be converted to
                                   a common data warehouse data format and be loaded into the ware-
                                   house “in bulk” or in short “bursts.” However, it does not deliver
                                   that data to external targets, such as an enterprise portal; it does not
                                   make the source data appear as one database; and it does not typi-
                                   cally emphasize transactional access to the data.
                                   An EAI solution passes data among multiple packaged applications.
                                   It does not deliver that data to other external targets, such as a Web
                                   site or enterprise portal, and it often operates at the level-of-business
                                   processes rather than at the data level.
                                   A content management system allows users to place a wide variety
                                   of rich-media data into a common database and to operate on that
                                   data as if it were a single database. The content management system
                                   requires that data be uploaded to a common database, whereas the
                                   EII solution leaves that data in place. The typical content manage-
                                   ment system focuses on a variety of data, such as text, rich media,
                                   and business rules, whereas most EII solutions currently focus on
                                   relational operations that act upon relational and nonrelational data.

                                   EII in the User Site
                                   EII solutions serve three masters: the developer, the administrator,
                                   and the user.
                                   In order to serve the developer, the EII solution provides a bridge
                                   between the components and business logic residing in the second
                                   tier of the e-business architecture and back-end data sources — that
                                   is, it allows the developer to treat multiple, disparate databases, data
                                   management systems, and files as one gigantic enterprisewide data-
                                   base.
                                   To aid the administrator, the EII solution often (but not always) pro-
                                   vides a “metadirectory” of data and object types (e.g., an XML data
                                   dictionary) across multiple data sources, plus specific tools that al-
                                   low the administrator to monitor, maintain, and implement security
                                   for the virtual federated database.
                                   To aid the user, the EII supports the kind of operations on the virtual
                                   federated database commonly found in SQL (Structured Query Lan-
                                   guage), usually querying (decision support) and sometimes
                                   add/remove/update (online transaction processing [OLTP]). These
                                   features allow support for e-commerce and B-to-B OLTP, enable
                                   Web analytics queries across databases, and abet enterprise portal



All print and electronic rights are the property of Aberdeen Group © 2003
12 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



display and a combination of information from various data sources
for employees, customers, and partners.

Situations in Which Today’s Companies Often Feel a
Need for EII
Aberdeen clients find that the data connectivity projects for which
EII is a new tool are no small tasks. Typically, the project scope is
greater than anticipated, and the data connectivity problems involve
heterogeneous environments. IT administrators usually must perform
these integration projects in a complex environment and must rely on
a rapidly changing technology infrastructure. Other frequently en-
countered issues include the following:
•   A hodgepodge of legacy systems

•   Multiple legacy databases from multiple suppliers

•   Disparate operating platform environments  MVS, Unix,
    Windows NT and XP, wide area network (WAN), local area
    network (LAN), and Internet

•   Heterogeneous and geographically dispersed database manage-
    ment and file systems

•   Many communications protocols, including SNA, TCP/IP,
    HTTP, and XML/SOAP

Finally, there is no guarantee that the data-level integration will have
integrated the applications’ business processes as a seamless whole
when the project is done. Today’s data connectivity solutions deal
with transactions on a per-application, per-database basis, and they
do not make it easy to handle business processes that involve differ-
ent databases or different applications.
By contrast, EII:
•   Supports transactions across databases and applications, making
    the implementation of business processes much easier

•   Makes the reuse of integration techniques across heterogeneous
    environments much easier

•   Gives users the ability to implement integration solutions with-
    out needing detailed knowledge of the application infrastruc-
    ture’s specific underlying technologies.

Thus, for all of these issues and situations, EII provides added sim-
plicity leading to lower costs.



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 13
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Business Benefits of EII
                                   Aberdeen research shows that EII solutions can deliver not only cost
                                   savings but also a new kind of competitive advantage. As it becomes
                                   more difficult for e-enterprises to achieve differentiation via pack-
                                   aged or custom applications, the new frontier of competitive advan-
                                   tage becomes an IT organization’s ability to leverage proprietary
                                   information that its competitors cannot access. Much of this informa-
                                   tion is scattered across multiple databases, spreadsheets, and rich-
                                   media Web sites, making it difficult, if not impossible, to detect the
                                   connection between a customer’s existing product preferences and
                                   new products arriving via the supply chain and R&D. EII’s ability to
                                   amass metadata and carry out transactions across data sources allows
                                   the EII user to detect and display these key “relationships across data
                                   frontiers.”
                                   EII’s cost savings are nothing to sneeze at either. Many of today’s
                                   tasks in BI (business intelligence), CRM (customer relationship
                                   management), portals, and consolidation involve integrating business
                                   processes and information. In these cases, EII simplifies the devel-
                                   oper’s job by giving one interface and one set of metadata for all
                                   data sources, speeding the development of applications such as en-
                                   terprise portals. EII simplifies the administrator’s job by exposing
                                   key data that must be kept in synchronization across data sources.
                                   The benefits that EII delivers to the enterprise are often immediate.
                                   The ability to cross database boundaries, if used by applications,
                                   rapidly allows wider user access to key existing data for data mining,
                                   enterprise portals, or Web searches from inside or outside of the en-
                                   terprise. Establishing relationships between data sets across frontiers
                                   and data source types quickly enhances the data warehouse,
                                   empowering deeper data analysis and providing a more comprehen-
                                   sive view of the enterprise’s information assets. The development of
                                   today’s business-critical, data-intensive applications is speeded when
                                   programmers need only code for access to one data source rather
                                   than to several disparate ones. Key administrative costs show signifi-
                                   cant improvement the moment that administrators can manage data
                                   more easily across data-source frontiers.
                                   In real-world implementations, users are increasingly seeing specific
                                   instances of the following benefits:
                                   •    EII gives a broader picture of data to the user; e.g., by combin-
                                        ing data in Oracle and IBM DB2 databases.

                                   •    EII encourages IT administrators to identify data copies and re-
                                        lated data across databases, files, spreadsheets, and graphics and
                                        video. For the user, this means new insights into a company’s
                                        proprietary information  for example, an alert that a new



All print and electronic rights are the property of Aberdeen Group © 2003
14 • AberdeenGroup
                        Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



      product in which the customer has an interest is about to arrive
      and can be pre-ordered. For the administrator, this means a bet-
      ter understanding of the enterprise’s overall data relationships,
      so that, for example, the administrator can ensure that changes
      in one set of data changes other related data appropriately.

•     EII simplifies the developer’s job. Instead of writing custom
      code for each Java access to back-end data, the developer can
      write once for all accesses, whether they involve access to a sin-
      gle database or multiple ones. By combining EII with Web ser-
      vices, the developer can simplify the front end of the application
      (by making it a Web service) and the back end (by simplifying
      data access). By “abstracting” the interface to back-end data-
      bases, EII makes it easier to upgrade an application — there is
      “one application programming interface (API) to choke” when
      data access must be changed.

•     Although no EII products currently support this process, it
      should be possible to allow administrators to create scripts that
      perform database administration across databases and file sys-
      tems  for example, scheduling offline backup of Oracle and
      Microsoft databases in sequence, to load balance a backup.

Potentially, EII can be used as part of an overall IT strategy to iden-
tify, manage, and leverage the enterprise’s proprietary information
for competitive advantage (strategic information management). For a
full description of this idea, see Chapter Four.

Applying EII to Typical IT Tasks
When deftly used, a powerful EII tool can make a significant contri-
bution to many of an IT organization’s most critical tasks (Table 1).

Table 1: Ways to Use EII in Strategic Initiatives

Aim                              Way to Use EII
Integrate business processes     Write code in the applications to access an EII solu-
                                 tion rather than the databases so that the EII can
                                 determine if the transactions are part of a business
                                 process and update all data sources at the same
                                 time
Implement Web services inter-    Write a Web services front end to an EII solution
faces to existing information    rather than to each data source
Speed time to react to current   Provide an EII interface to the data for query
customer or supply chain data    purposes, bypassing the database server



                                     All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                            AberdeenGroup • 15
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Aim                               Way to Use EII
                                   Speed time to develop new         Use an EII solution to front end for both the data ware-
                                   applications that leverage        house and other proprietary information, ensuring one
                                   proprietary information, such     set of code for all information access
                                   as portals
                                                                     Use an EII solution’s XML support to avoid coding
                                                                     object-to-relational translations or access to unstruc-
                                                                     tured data
                                   Audit all information in the      Create an EII metadata repository by importing (or
                                   enterprise for government         generating) metadata from the data warehouse, ETL
                                   requirements                      tools, and file systems and rich-media sites, and
                                                                     then write a SQL or Xquery query to the EII interface
                                   Cut IT costs                      Cut administrative costs by creating an administra-
                                                                     tive “veneer” over an EII tool that issues administra-
                                                                     tive commands to multiple data sources
                                                                     Cut development costs with an EII tool that allows
                                                                     developers to “write once” to supply data access to
                                                                     many applications
                                   Merge companies                   Combine the metadata of the two companies via an
                                                                     EII metadata repository
                                   Increase the amount of            Create EII across multiple databases that expands
                                   information available to users    the range of information available to an enterprise
                                                                     portal via the same interface
                                                                                    Source: Aberdeen Group, July 2003

                                   The following real-world examples show that EII is making a contri-
                                   bution:
                                         •   Merrill Lynch uses MetaMatrix to speed development and to
                                             allow analysts to access stock, product, and pricing data in
                                             IBM, Oracle, and Sybase databases.
                                         •   Aventis uses IBM to mine its Oracle databases and external
                                             nonrelational sources (genomics, proteomics) for drug re-
                                             search, and they are seeing significant speedups in R&D.
                                         •   Crystal Decisions uses IBM as an ISV to improve perform-
                                             ance in accessing large amounts of heterogeneous, distrib-
                                             uted data in thousands of data sources via Crystal Reports; it
                                             claims that response time has improved by up to 98%.

                                   Developments in the Database Market Drive the
                                   Need for EII
                                   The IT buyer should consider another reason for assessing EII tools:
                                   the state of the database, EBI (enterprise business integration), and
                                   portal markets.


All print and electronic rights are the property of Aberdeen Group © 2003
16 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Periodically, database suppliers attempt to “own” the market by per-
suading organizations to migrate existing data to their database.
Organizations are perfectly willing to do so  after all, the cost of
administering multiple databases is a major and increasing compo-
nent of a summed IT total cost of ownership. However, moving all
key enterprise data onto Oracle, for example, has almost always
proven impossible to achieve. Legacy databases will continue to live.
As a result, organizations need a second-best alternative: to adminis-
ter, as far as possible, multiple databases as if they were from one
supplier. This alternative not only dramatically simplifies the job of
the database administrator but also eases the process of incorporating
a wide variety of data (spreadsheets, data in the form of text, multi-
media data) into the enterprise’s visible information portfolio. Thus,
a cross-database-supplier solution sharply reduces administrative
time required (and, hence, costs), and enlarges the scope of the data
administered.
At the same time, the need to aggregate data across databases and
deliver it to a wide variety of audiences is increasingly urgent. The
two key drivers of the market’s demand for cross-database solutions
are EBI and enterprise portals. As XML-based solutions proliferate,
they create a demand for more varied back-end data to feed to out-
side suppliers. Enterprise portals, by their nature, seek to display a
wide variety of data on a single screen, and ODBC- and JDBC-based
solutions simply require too much work of the programmer to be
implemented easily.
To meet these needs and overcome the difficulties associated with
existing solutions, EII acts as a many-to-many interface between the
user and multiple databases. Table 2 shows how this approach allows
the EII supplier to overcome the difficulties that have faced past ap-
proaches.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 17
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                  Table 2: EII versus Traditional Approaches

                                   Single “Central”         Programmatic                  EII
                                   Database”                Interface (JDBC)
                                   Cannot keep up with      Can keep up only with         Can keep up with upgrades
                                   upgrades to other        upgrades common to all        common to all databases,
                                   databases                databases                     allows programming to covert
                                                                                          new data types to a standard
                                                                                          format, and allows users to
                                                                                          bypass the EII solution for key
                                                                                          new single-database features

                                   No programming           Low-level programming         High-level components and
                                   interface for cross-     interface for cross-          programming interface (in
                                   database-supplier        database-supplier             some cases, looking like a
                                   transactions             transactions                  single database) for cross-
                                                                                          database-supplier transac-
                                                                                          tions
                                   No provision for         No provision for handling     Directory that “tags” data that
                                   handling data defined    data defined in multiple      exists in multiple databases
                                   in multiple databases    databases

                                   No load balancing for    No provision for load         In many cases, built-in load
                                   transactions across      balancing for transactions    balancing for transactions
                                   multiple databases       across multiple databases     across multiple databases


                                                                                   Source: Aberdeen Group, July 2003




                                   Criteria for Buying an EII Solution
                                   EII solutions differ markedly in their ability to support developers,
                                   users, and administrators. Aberdeen recommends that IT buyers use
                                   different criteria according to which of these is the “main constitu-
                                   ency” for an e-business architecture. The following are key criteria
                                   for developers:
                                   •    Scalability of the development tools and of the applications built
                                        over the EII solution. Development tools should allow team and
                                        remote development (e.g., via a “developer network”); data-
                                        access mechanisms should provide optimization of queries and
                                        transactions.




All print and electronic rights are the property of Aberdeen Group © 2003
18 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   Quality assurance to ensure robust e-business applications (e.g.,
    by providing the ability to persist data from the start of a cross-
    database transaction to the end, transparent to the developer).

•   Programmer productivity, by componentizing key EII opera-
    tions at the business level, allowing the developer to swiftly
    write EII-using applications, such as enterprise portals.

•   Flexibility to support a wide variety of platforms and architec-
    tures, by supporting open standards such as J2EE (Java 2 Enter-
    prise Edition), EJBs (Enterprise JavaBeans), and XML and by
    offering the ability to add new platforms and architectures easily
    and rapidly.

The following are key criteria for administrators:

•   Comprehensive cross-database administration features that al-
    low a database administrator to monitor and maintain multiple
    databases via EII as if they were one database, as well as coor-
    dinate with the database administration tools of back-end and
    legacy databases

•   Ability to monitor and tune transactions within the EII system in
    order to detect bottlenecks, preferably via a remote console

•   Connections to application-management and systems manage-
    ment products, such as CA Unicenter TNG

The following are key criteria for users:

•   Comprehensive support for a wide variety of back-end data-
    bases and other data sources

•   Easy “plugability” into front end e-commerce, B-to-B, and, es-
    pecially, enterprise portal implementations, as well as popular
    Web and application servers

•   Powerful cross-database transactional features, such as sophis-
    ticated querying

IT buyers should also consider the following overall criteria:

•   The supplier’s ability to serve as a “one-stop storefront” for
    system design and integration. The IT buyer should be espe-
    cially attentive and avoid “finger pointing” (the case in which
    multiple suppliers blame each other for a failure) because EII
    solutions typically involve complex connections to a wide vari-
    ety of supplier software.



                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 19
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    An EII solution’s ability to be a good foundation for a Web ser-
                                        vices architecture. Over the next two years, Web services im-
                                        plementations will become much more frequent, and EII must
                                        provide the standards support to integrate well with other up-
                                        coming Web services architecture components, such as a UDDI-
                                        based directory, as well as have the ability to access a wide vari-
                                        ety of intra- and extra-enterprise data sources that these Web
                                        services promise.

                                   Critical Technology Factors
                                   Aberdeen research has determined that the following five factors are
                                   key to understanding and differentiating EII solutions:
                                   •    Object and multimedia data support (including XML support)

                                   •    Non-database information access

                                   •    Specific support for front-end users and applications such as
                                        browser-based analytics, EBI, or enterprise portals

                                   •    Developer support

                                   •    Administrator support

                                   Object, Multimedia, and Non-database Support
                                   Data integration solutions will have a variety of constituents  in-
                                   ternal programs, Web site users, workgroups within the enterprise,
                                   partners/suppliers, internal workgroups or intranets via a LAN (local
                                   area network) or remotely, data miners, and IT administrators. These
                                   constituents vary widely in how they are accustomed to having data
                                   presented (Table 3). A good EII solution is, therefore, many-to-
                                   many: It draws data from a wide variety of data types, including ob-
                                   ject and multimedia ones, and delivers the data in a standardized
                                   format supported by each constituent.
                                   XML is the coming lingua franca (or common language) that allows
                                   this type of flexible response to a wide variety of constituents.
                                   Wrapping a transaction result in XML allows it to be delivered not
                                   only within the organization, where IT administrators can enforce
                                   XML support, but also to outside users via the Web, as well as part-
                                   ners and suppliers that are increasingly looking to XML for elec-
                                   tronic data interchange and EBI.
                                   The EII solution should also support access to text files, spread-
                                   sheets, graphics, video, and objects, as well as relational data. In-
                                   creasingly, business-critical data includes at least one of these non-
                                   traditional data types.



All print and electronic rights are the property of Aberdeen Group © 2003
20 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Table 3: EII Constituents and Their Data Needs

Constituent           Data Typically Accessed         Data Format Typically
                                                      Required
Internal              Relational                      Relational
programs
Web site users        Text, graphics, relational      HTML
Partners/suppliers    Relational, text                XML
Internal workgroups   Spreadsheet, text               HTML, graphical
or intranets
Data miners           Relational                      Graphical
Administrators        All types                       No requirements
                                             Source: Aberdeen Group, July 2003



Most EII suppliers are moderately advanced in supplying these fea-
tures. Most support access to a wide variety of data, although the
emphasis is usually on relational data. Most also have some variant
of XML support either available or planned. Few provide specific
support for a broad range of constituents.

Specific Front-End Support
Specific types of new solutions that many enterprises are implement-
ing call for specific support from an EII solution. The following are
major new application types that EII should support:
 •   Enterprise portals

 •   EBI

 •   Browser-based analytics

 Enterprise Portals
Today’s enterprise portal, via a rapid, straightforward implementa-
tion, allows the coordinated presentation and use of a much broader
range of information to B-to-C and B-to-B customers, as well as to
internal intranets and data miners. However, these connections work
best if integrated with the whole infrastructure of a Web’s architec-
ture. That includes the following:




                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 21
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   •    Middleware — e.g., Web servers, application servers, applica-
                                        tion messaging, and EAI

                                   •    Databases, as both second-tier caches and as “common” infor-
                                        mation stores

                                   •    Development tools and frameworks for rapid development and
                                        customization

                                   •    Hooks to integrate B-to-C and B-to-B supplier order processing

                                   •    XML formatting for Net market display

                                   •    Decision-support querying

                                   The EII solution stands between the enterprise portal and “common
                                   information store” databases, acting as a collection point for the data
                                   in order to forward it to the enterprise portal for display. The EII
                                   solution can also help with second-tier data caching, portal develop-
                                   ment, XML support, and querying across databases. In order to do so
                                   effectively, the EII solution can offer a caching database, its own
                                   development tools that are integrated with those of the enterprise’s
                                   portal-infrastructure solution, XML support, and its own querying
                                   facilities.

                                    EBI
                                   The EII solution can also serve to bypass the enterprise portal in pre-
                                   senting single-database and cross-database corporate information to
                                   partners and suppliers. By avoiding the user interface characteristic
                                   of an enterprise portal, the EII solution can simplify both many-
                                   database-to-one supplier and many-database-to-many-supplier inter-
                                   actions. However, this also means that the EII solution must supply
                                   the XML-standard support, tools for building connections on the
                                   supplier side, and security features characteristic of today’s EBI
                                   solutions.

                                    Browser-Based Analytics
                                   The promise of browser-based analytics is to extend the information
                                   analysis benefits of today’s data warehouses to a wider range of
                                   Web-based users and to simplify analysis so that it is not the prov-
                                   ince of a few highly skilled data miners. An EII solution can increase
                                   the scope and improve the ability to analyze real-time information of
                                   an analytics solution by allowing querying across a wide variety of
                                   data, not simply the data in a corporate data warehouse. To support
                                   browser-based analytics, EII solutions should supply some of the
                                   characteristics of a browser-based analytics solution in a cross-
                                   database situation  governors to avoid the “query from hell” that
                                   crowds out all other users from accessing a database, cost optimizers


All print and electronic rights are the property of Aberdeen Group © 2003
22 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



to maximize cross-database query performance, and tools to convert
back-end spreadsheet and relational data to graphical (pie chart, sta-
tistical) representations.
Most suppliers now provide specific features for browser-based ana-
lytics and portals, with fewer targeting EBI.

Developer Support
For both the developer and the administrator, the ideal EII solution
provides a “single database image,” in the same way that a good
clustering solution pretends that multiple systems are a “single-
system image.” This, in turn, means that the EII solution provides
most of the developer features of a high-end database  stored pro-
cedures, standard SQL support, a wide variety of APIs (including
support for ODBC, JDBC, and EJBs), and the ability to use the EII
solution’s directory to drive program design (e.g., by mapping direc-
tory “metadata” into common design tools such as Oracle’s and Ra-
tional’s design solutions). Note that the EII solution cannot offer one
of the advantages of the single database  the ability to run a pro-
gram inside the database’s process for high performance.
Most EII solutions are fairly far advanced in providing the developer
support that users need. Many solutions support stored procedures,
and they all support standard SQL. Some provide development tools
bundled with the application. Relatively few offer a full array of
high-end database APIs, and few provide mapping between the
metadata directory and design tools.

Administrator Support
Again, the EII solution should provide an image of a single database
to the administrator. However, this goal is much more difficult to
achieve for administrator support than for developer support. It ef-
fectively means that the EII solution must offer cross-database
backup/recovery, cross-database security, and interfaces to each da-
tabase’s own administrative tools for functions such as upgrade, re-
organization, and replication. The EII solution should also offer
SNMP (Simple Network Management Protocol) support to allow the
EII administrative tool to interact with common systems manage-
ment tools, such as CA Unicenter TNG.
Aberdeen characterizes the current administrator support tools of-
fered by EII suppliers as workable but basic. A few suppliers have
tools for transaction monitoring, user management, and security.
What is especially missing from all suppliers today is support for the
integration of these administrative tools with enterprise system and
network management facilities such as Unicenter TNG, Tivoli, or
OpenView. Current EII solutions are likely to be widely deployed in



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 23
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   large-scale and highly distributed computing environments, so it is
                                   obvious that enterprise administrators will need to be able to manage
                                   EII nodes and modules just as they do distributed EBA (enterprise
                                   business application) system components.
                                   Notably, few, if any, EII suppliers provide support for cross-database
                                   administration scripting.




All print and electronic rights are the property of Aberdeen Group © 2003
24 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter Four:
EII As Part of Strategic Information
Management
The proliferation of files, rich media, and traditional relational data,
as enterprise computing broadens in the number of users supported
and IT value-add, has become an inexorable long-term trend. Ways
to access this information are hindered by the differences in how this
information is stored, to the point where each Oracle database, group
of Excel spreadsheets, or Web site can require a separate program to
elicit data-based insights. Thus, the “frontiers” between information
sources delay competitive-advantage data analysis, add cost to the
process of creating queries and transactions across data boundaries,
and mire today’s efforts to leverage proprietary information into
long-term revenue enhancement in a hopeless game of “catch-up”
with enterprises’ growing cache of information.
Over the years, specialized tools and technologies have arrived that
tackle the problem of information frontiers. These technologies have
now reached a point of maturity in which the IT executive can use
them strategically, in what Aberdeen calls strategic information
management. The cross-frontier technologies that support strategic
information management are what Aberdeen calls information ag-
gregation technologies.
As an information aggregation tool, EII has an important role to play
in strategic information management, in concert with other such
tools. This chapter catalogs the other technologies that constitute
information aggregation, shows how EII and other information ag-
gregation tools can be used (singly or in combination) to abet strate-
gic information management, and examines the state of the art that
IT strategists can use today in attempting strategic information man-
agement.

A Brief Introduction to Strategic Information
Management
Today’s IT strategist, seeking to increase competitive advantage, can
focus primarily on the application resources or the data resources of
the enterprise. Until recently, it made most sense to focus on applica-
tions. Strategic solution management has sought to identify, manage,
leverage, and add to the application software that delivers value-add
to the enterprise, customer, or supply chain.
Over the last two years, IT organizations’ focus has shifted strongly
toward cost cutting. Cost squeezes at both ISVs (independent service


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 25
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   vendors) and major IT shops have nearly halted the development of
                                   new, competitive-advantage applications or major Web efforts.
                                   Meanwhile, CIOs and ISV CEOs have resorted to cost-saving meas-
                                   ures, such as offshore development outsourcing. However, strategies
                                   based solely on cost savings typically reach a point of no return 
                                   the ultimate result of long-term cost cutting is a “hollowed-out” cor-
                                   poration.
                                   Today, the obvious place to search for a cost-effective, long-term
                                   advantage is, therefore, in proprietary information that competitors
                                   cannot readily duplicate. For example, Amazon.com may seek to
                                   combine information about customers’ preferences with information
                                   about upcoming book releases, notifying them when a new book of
                                   interest is about to be published. However, this information is usu-
                                   ally locked in widely differing and often aged data sources. In an-
                                   other example, much Wall Street investment research depends on
                                   data from sources that range from Excel spreadsheets to reports, up-
                                   to-the-minute news articles, Web pages, and historical stock data-
                                   bases. Simply writing new code or buying a packaged business
                                   intelligence application does not do the trick. The IT strategist also
                                   needs to focus on making the information more widely available;
                                   therefore, strategic information management is needed.
                                   Strategic information management has a short- and a long-term com-
                                   ponent. The short-term job of strategic information management is to
                                   deliver available information consistently, no matter the variations in
                                   user demand  “on-demand” information. Tools that support the
                                   short-term job include storage management and SAN (storage area
                                   network)/NAS (network-attached storage) management (especially
                                   virtualization), database and cross-database administration, system
                                   and systems file administration, and Web site administration.
                                   The long-term job of strategic information management is to iden-
                                   tify, manage, support the leveraging of, and add to the information
                                   resources of the enterprise. Tools that support the long-term job(s)
                                   include metadata repositories and cross-database administration.
                                   Tools that support the “information aggregation” discussed here are
                                   just beginning to surface, and tools that allow automated searches of
                                   sources of new proprietary or extra-enterprise information that can
                                   be used for competitive advantage are not yet visible in the market.

                                   What Is Information Aggregation, and Why Does
                                   It Matter?
                                   Information aggregation is Aberdeen’s term for a collection of tools
                                   and technologies that have arrived over the last seven years and that
                                   allow users to combine data across data-source frontiers. Information
                                   aggregation includes the following:



All print and electronic rights are the property of Aberdeen Group © 2003
26 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   Tools to move or copy data from multiple “source” data sources
    to a “target” aggregated-data repository, which can be used to
    carry out such operations as queries across differing data types

•   Tools to access data from multiple data sources and then com-
    bine it temporarily for specific purposes, such as cross-database
    queries

Aberdeen arbitrarily calls this “information aggregation” rather than
“information integration” for two reasons. First, compared with the
term “integration,” “aggregation” better captures the idea that data
can be combined both permanently and temporarily. Second, “infor-
mation integration” may be confused with “enterprise information
integration” — a new sub-technology of information aggregation —
as well as various recent efforts by suppliers to coin the terms data
integration, enterprise application integration, and information inte-
gration.
Information aggregation currently includes the following types of
tools:
•   Data migration and bulk download tools

•   Replication and ETL tools

•   Data warehouses and data marts

•   Enterprise operational data stores

•   Mid-tier operational data stores

•   EII tools

•   Federated databases

Any information integration technology delivers immediate benefits
to the enterprise. The ability to cross database boundaries used by
applications gives wider user access to key existing data for data
mining, enterprise portals, or Web searches from inside or outside
the enterprise. Establishing relationships between data sets across
frontiers and types of data sources empowers deeper data analysis,
leverages proprietary information more effectively for competitive
advantage, and provides a more comprehensive view of the enter-
prise’s information assets. Development is speeded when program-
mers need only to code for access to one data source rather than sev-
eral disparate ones. Administrators often cut costs by managing more
easily across data-source frontiers.
When IT administrators wish to manage information strategically,
information aggregation can play a key role in leveraging existing


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 27
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   information. Information aggregation’s ability to establish relation-
                                   ships between data sets in widely different data sources helps the IT
                                   strategist identify key data and key “data connections” by placing
                                   that “information about information” in one place. Moreover, typical
                                   side effects of information aggregation tool use are the gathering of
                                   cross-data-source metadata and the ability to administer aggregated
                                   data and metadata. Thus, the information management strategist can

                                   Table 4: Strategic Uses of Information Aggregation

                                   Key Task                     Value-Add of Information Aggregation
                                   Identify                     ETL tools and data warehouses can create a cross-database
                                                                metadata repository.
                                                                EII tools can add file and rich-media data-source metadata.
                                   Manage                       Data warehouses and operational data stores, fed by data-
                                                                movement tools (data migration, data cache, ETL), allow full
                                                                administrative operations across at least one copy of aggre-
                                                                gated relational data sources and, sometimes, file and rich-
                                                                media data sources.
                                                                EII and federated databases potentially allow full administra-
                                                                tive operations across all copies of relational, file, and rich-
                                                                media data sources.
                                   Leverage                     Data warehouse, federated database, and EII APIs allow
                                                                broader, more quickly developed application access to rela-
                                                                tional data sources.
                                                                EII extends application access to file and rich-media data
                                                                sources.
                                                                Enterprise portals extend application access to a broader
                                                                range of users.
                                                                Operational data stores, federated databases, and EII can
                                                                allow update as well as query access.
                                   Find new use                 No effect (still a manual process)

                                                                           Source: Aberdeen Group, July 2003
                                   also identify and manage information across frontiers more effec-
                                   tively. Table 4 suggests specific ways in which specific information
                                   aggregation tools can be useful in each key strategic information
                                   management task.
                                   The culmination of these benefits occurs when an IT shop decides to
                                   implement full-fledged strategic information management. By apply-
                                   ing each information aggregation tool appropriately and strategi-
                                   cally, the IT strategist can potentially attain an “almost enter-


All print and electronic rights are the property of Aberdeen Group © 2003
28 • AberdeenGroup
                    Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



prisewide” metadata repository, an almost enterprisewide data-
source administration tool, and an almost enterprisewide informa-
tion-leveraging tool to constantly search the enterprise’s ever-
growing information store for new ways to combine the information
for competitive advantage.




                                All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                       AberdeenGroup • 29
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   When to Apply What Information Aggregation
                                   Technology
                                   Figure 2 shows how information aggregation technologies can be
                                   combined in an overall architecture.

                                   Figure 2: Example of Information Aggregation Architecture




                                                             Source: Raining Data Inc. and Aberdeen Group, March 2003


                                   The State of the Art in Information Aggregation

                                   Data Migration and Mass Download Tools
                                   Data migration and mass download tools were the first information
                                   aggregation tools, and they linger in today’s ETL products that can
                                   also be used for bulk data migration and download. For example,
                                   Evolutionary Technologies Inc. (ETI) continues to provide data mi-
                                   gration capabilities in its “data integration” product.
                                   Moreover, the enterprise-database-supplier consolidation in the late
                                   1990s spawned several tools for migrating from one database to an-
                                   other  e.g., from Sybase and Informix to IBM relational databases


All print and electronic rights are the property of Aberdeen Group © 2003
30 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



or from these databases to Oracle. In addition, several major enter-
prise database suppliers offer tools to migrate files and/or rich-media
“objects” into their relational databases  e.g., Oracle and IBM 
or to move or copy large amounts of other data  e.g., IBM to move
IMS data into a DB2 database.
Most of these tools focus on migration from one relational database
to another. The general-purpose data migration and ETL tools are the
most flexible, allowing migration across suppliers and, in some
cases, across a wide array of data types. Therefore, they are often
preferred for long-term strategic information management because
they can be reapplied in many different cases in which permanent
data movement is desired or in which database consolidation will
likely be ongoing.
Table 5 shows one way to categorize information aggregation tech-
nologies.

Table 5: Taxonomy of Information Aggregation Tools

 Tool             Characteristics            Typical Uses Today
 Data migration   Typically move large       End use of a database by
 and mass         amounts of data at once,   moving it to another database
 download         either permanently or      (e.g., move to another data-
                  intermittently, almost     base supplier)
                  always “offline” (when
                                             Allow database operations
                  the target data store is
                                             (especially queries) to be
                  not operating)
                                             applied to a data source (e.g.,
                  Typically one source,      PC files) by moving/copying it
                  one target                 inside the database
                                             Backup and disaster recovery




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 31
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                     Tool               Characteristics              Typical Uses Today
                                     Replication and    Copy (one way) one           Refresh a data warehouse or
                                     ETL tools          piece of data at a time,     data mart from mission-critical
                                                        either continuously as       OLTP (online transaction
                                                        data changes or in           processing) relational data-
                                                        spurts, usually offline      bases, typically daily
                                                        Transform data to differ-    Reflect local-office data to a
                                                        ent format to improve its    central site for backup and
                                                        quality or to convert to a   querying (“mass-deployment”)
                                                        common format
                                                                                     Synchronize handheld/laptop
                                                        Typically multiple           and central databases
                                                        sources, one target
                                                                                     Copy data between embed-
                                                                                     ded databases for packaged
                                                                                     applications from different
                                                                                     suppliers to integrate busi-
                                                                                     ness processes (EAI)
                                     Data               Copy (one way) large         Support querying, data min-
                                     warehouses         amounts of data at a         ing, and business intelligence
                                     and data marts     time, usually daily, al-
                                                                                     Provide metadata repository
                                                        most always offline
                                                                                     of key business information
                                                        Typically multiple
                                                        sources, one target
                                                        Usually includes ETL tool
                                                        Allow querying of aggre-
                                                        gated data, but not up-
                                                        date
                                                        Often extremely large
                                                        (terabytes)
                                     Enterprise         Copy (one way), typically    Combine key customer and
                                     operational        changes in data (imme-       supply chain data to detect
                                     data stores        diately)  often from the    and query relationships
                                                        store/cache to multiple
                                                                                     Combine data from key busi-
                                                        targets, always online
                                                                                     ness applications to integrate
                                                        Typically multiple           business processes
                                                        sources, one target
                                                                                     Improve speed-to-react to
                                                        Often use replication or     business conditions (re-
                                                        ETL tool                     freshed more frequently than
                                                                                     data warehouse)
                                                        Allow querying and up-
                                                        date                         Improve visibility of current
                                                                                     (less than a week old) data
                                                        Often large, but not so
                                                        large as data warehouse




All print and electronic rights are the property of Aberdeen Group © 2003
32 • AberdeenGroup
                  Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Tool          Characteristics             Typical Uses Today
Mid-tier      Copy (one way) changes      Combine key customer and
operational   in data (immediately)      supply chain data to detect
data stores   often from the              and query relationships
              store/cache to multiple
                                          Combine data from key busi-
              targets, always online
                                          ness applications to integrate
              Typically multiple          business processes
              sources, one target
                                          Improve speed-to-react to
              Often use replication or    business conditions (re-
              ETL tool                    freshed more frequently than
                                          data warehouse)
              Allow querying and up-
              date                        Improve visibility of current
                                          (less than a week old) data
              Smaller than enterprise
              operational data store      Improve performance and
                                          scalability of key applications
                                          and “composite” applications
EII           Leaves the data sources     Queries and updates across a
              as is                       wide variety of data sources
                                          (including file and rich media)
              Often uses real-time ETL
                                          without creating copies to
              tool
                                          synchronize
              Allows querying and
                                          Creates a more global meta-
              (less frequently) update
                                          data repository than any other
              Must transform data for     IA tool
              each query
                                          Allows cross-data-source
                                          development
                                          Potentially, allows cross-data-
                                          source administration



Federated     Leaves the databases as     Combines differing relational
database      is                          databases from the same
                                          supplier or two suppliers
              Allows querying and up-
              date
              Must transform data for
              each query


                                         Source: Aberdeen Group, July 2003




                               All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                      AberdeenGroup • 33
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                    Replication and ETL Tools
                                   If an IT organization chooses to copy data from a data source to data
                                   “target,” then changes in that data must likewise be copied from
                                   source to target. If an IT organization needs up-to-date sources and
                                   targets at all times, the data copies must be kept in synchronization
                                    every transaction must see the same value for the data at all times,
                                   no matter what copy is changed first. In OLTP situations, that means
                                   using two-phase commit technology (a technical method of achiev-
                                   ing two-way synchronization between two information bases). The
                                   drawback of this technology (as with all two-way synchronization
                                   technologies) is that it is low performance  it can take a long time
                                   to carry out a single multiple-copy update, much less a high-volume
                                   stream of them. Thus, in synchronized OLTP systems, only a few
                                   data copies are realistically possible.
                                   In data warehousing environments, the situation is simpler. The data
                                   warehouse is not intended as an OLTP environment; it is in no hurry
                                   to record changes to data items. Therefore, all a data warehouse
                                   needs is one-way synchronization, or data replication. The OLTP
                                   “feeder” databases record a change in the data and, at some later
                                   point, it is replicated to the copies in the data warehouse database.
                                   Of course, even in a data warehousing context, replication is not
                                   without cost. Updates that occur while the data warehouse is running
                                   means write locks that can slow querying. Selective updates of some
                                   data items, although related data items are not updated until the end
                                   of the day, may result in inconsistent data. However, these problems
                                   are typically easy to handle  slower querying by delaying updates
                                   until times of low querying (such as the end of the day)  enabling
                                   mass replication to update data all at once and inconsistent data to be
                                   avoided by careful data warehouse design. Deft use of replication,
                                   therefore, can result in far more timely data on which data miners
                                   can operate.
                                   Replication tools abound in the market, and the major database sup-
                                   pliers offer many of them. These tools may allow replication from
                                   multiple suppliers’ relational databases to a particular supplier’s da-
                                   tabase, but not vice versa. However, because it is easy to find an-
                                   other replication tool to perform “reverse replication,” one-way rep-
                                   lication is not a major drawback.
                                   ETL tools combine both data migration and replication tool technol-
                                   ogy. As with data migration technology, they allow the translation of
                                   data formats from widely different source formats into widely differ-
                                   ent target formats via a process of extracting, transforming (with
                                   cleansing), and loading. As with replication tools, they can copy data
                                   in real time and in small amounts. An ETL tool can be combined
                                   with replication technology to ensure that when data is changed, that
                                   change is sent on to the target database.


All print and electronic rights are the property of Aberdeen Group © 2003
34 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Initially, ETL tools were targeted primarily at the data warehousing
market, but the advent of EAI has meant that ETL tools are also
packaged as part of EAI solutions, often as “adapters” that translate
between the data formats of major packaged applications such as
those provided by SAP and PeopleSoft. Recently, ETL tools have
appeared in the offerings of EII suppliers.
The wide array of ETL tools in the market is often from suppliers
that specialize in data warehousing add-ons, or EAI, or both  sup-
pliers such as Compuware, Data Junction, ETI, Sybase, TIBCO, and
webMethods. IT strategists should note that ETL tools are excep-
tionally flexible and, therefore, applicable as the base technology for
a wide variety of information aggregation needs.

 Data Warehouses and Data Marts
Data warehouses aggregate data primarily, and often exclusively, for
decision support. A data warehouse’s data is derived from outside
OLTP and “mixed” databases. The databases’ data is fed to the deci-
sion-support information base via either mass downloads involving
careful cleansing of the data (typically via an ETL tool) or by one-
way synchronization, in which changes in specific data items are
replicated in the data warehouse information base. Specialized que-
rying or analytics tools allow specialized “data miners” to access the
data and derive insights about patterns of sales or similar competi-
tive-advantage information. Data marts are smaller data warehouses
 often for specific functions within an enterprise — that feed a
large central data warehouse.
Experience has shown that the data warehouse has major limitations
that prevent it from serving as the ultimate information aggregation
of all data in the enterprise. First, it can grow only to a certain size
before performance becomes too poor; hundreds of terabytes may
sound like a large number, but the typical major organization stores
far more data than that. Second, in order to service the “query from
hell,” the data warehouse must focus on queries to the exclusion of
all other operations, including the updates that accompany key op-
erations, such as customer order entry. Third, holders of line-of-
business data or other data are often reluctant to register it in the data
warehouse’s metadata repository because it brings no immediate
business benefit. Fourth, refreshing a large data warehouse daily is a
massive operation that prevents warehouse usage for hours, so keep-
ing the warehouse more than one day or one week behind is, practi-
cally speaking, impossible.
Nevertheless, the data warehouse is often the best base on which to
begin implementing strategic information management. It is not only
the largest aggregation of data in the enterprise; it is also the largest
aggregation of metadata.


                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 35
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   All major enterprise database suppliers  IBM, Microsoft, Oracle,
                                   and Sybase  offer extensive data warehousing support, as does
                                   NCR-Teradata.

                                    Enterprise Operational Data Store
                                   The idea of the operational data store is to combine the key data
                                   from multiple data sources or “systems of record” in one database
                                   that  unlike a data warehouse  allows the updating of the data.
                                   An enterprise operational data store focuses on collecting business-
                                   wide, mission-critical data. This approach gives the enterprise opera-
                                   tional data store the ability to aggregate the data of a data warehouse
                                   and provide near real-time “data freshness,” giving users the ability
                                   to react to changes in business conditions  such as shifts in buying
                                   patterns  instantaneously. However, the price of adding updates is
                                   a sharp decrease in the amount of data that can be stored in the op-
                                   erational data store and the amount of sophisticated data mining that
                                   can be applied to it. In other words, in an enterprisewide operational
                                   data store, users can react more quickly to insights, but gain fewer of
                                   them.
                                   All enterprise databases can be used as enterprise operational data
                                   stores when combined appropriately with real-time ETL or replica-
                                   tion tools. The trick to successfully implementing an operational data
                                   store is not so much picking the right database as picking the right
                                   data to go into the database. However, the process of picking the
                                   right data is precisely what makes either an enterprise or a mid-tier
                                   operational data store such a valuable tool for strategic information
                                   management. All data is not equal; the strategic information manager
                                   needs to distinguish proprietary data that can be leveraged, and that
                                   type of data is frequently found in an operational data store.
                                   The idea of an enterprise operational data store, pioneered by suppli-
                                   ers such as Unisys, is now generally accepted across the industry,
                                   and most major enterprise database suppliers now offer support for
                                   implementation of enterprise operational data stores (often referred
                                   to simply as “operational data stores”). Note that many enterprise
                                   operational data stores combine only data from relational databases.

                                    Mid-tier Operational Data Stores
                                   A mid-tier operational data store is a recent idea with distinct merits
                                   for strategic information management. A high-performance database
                                   serves as a persistent, long-term cache, not only for one but also for
                                   several databases from one or several suppliers. This “cache” data-
                                   base, unlike most caches, provides all of the functionality of an op-
                                   erational data store. This functionality allows users not only to speed
                                   the performance of each data source but also to combine key data
                                   from each data source, reflecting changes to this key data back to all
                                   data sources. In other words, a mid-tier operational data store can


All print and electronic rights are the property of Aberdeen Group © 2003
36 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



provide all of the benefits of an enterprise operational data store (al-
though often on a smaller scale), as well as improved performance
and scalability for mission-critical databases and applications.
As with EII and EAI tools, the enterprise and mid-tier operational
data stores can store metadata about relationships across databases
and, therefore, provide users, administrators, and developers with the
benefits of an EII solution on a much smaller scale. In addition, EII
and operational data stores can be combined quite effectively. Recent
examples of mid-tier operational data stores include Raining Data’s
TigerLogic XML Data Management Server (XDMS) and Ipedo In-
formation Hub.

EII Tools
The potential for EII as an enabler of strategic information manage-
ment cannot be overestimated. EII can serve as the focal point for
gathering an unprecedented amount of metadata about the enter-
prise’s proprietary information. Potential EII tools can administer
across as wide a swath of the enterprise’s data sources as desired. EII
allows leveraging data relationships across data sources without the
effort of moving or copying the data.

 The Usefulness of Combining Mid-tier ODS and EII
Users should note that EII tools typically do not include any persis-
tence technology, so information that is extracted, transformed, and
integrated for each request can cause performance overhead com-
pared with an ODS — although the ODS does not permit access to
as large a data store as an EII tool. Thus, a combination of EII and an
operational data store is often a better combination of data-store size
and performance than either would be separately.
This is true not only for decision-support querying but also for tasks
such as order entry that require data updates. A mid-tier ODS’s abil-
ity to index data from other data sources allows users to not only
query these sources  an ability that all EII tools share  but also
insert, remove, and update them (actions that relatively few EII tools
permit).
Moreover, a combined EII/mid-tier ODS lets the information strate-
gist “have it your way”  (1) to merge data into an ODS, where
swift access to real-time data for rapid decision making is para-
mount; (2) apply a cross-data-source query rather than moving data,
when an ODS “tops out” or operational data must be combined with
data warehouse historical data; or (3) rapidly react to new floods of
data by moving some into the ODS and access the rest via EII.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 37
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Federated Database
                                   The federated database may well be an idea whose time has passed;
                                   however, it is still worth noting as an alternative approach to infor-
                                   mation aggregation that may yet pan out. The idea of a federated
                                   database is to provide the same data management software to differ-
                                   ent data sources. Thus, in Informix’s federated approach, the same
                                   version of Informix OnLine accesses object and relational data pre-
                                   viously served by different Informix databases, allowing the same
                                   queries, administration, etc., to be used on both data sets. Other vari-
                                   ants would allow the same operations across multiple suppliers’ data
                                   sources or across widely different data sources.
                                   The major difficulty so far with this one-size-fits-all approach is that
                                   it has proved very hard to make one operation fit all data sources —
                                   e.g., to make query optimization appropriate to relational data effec-
                                   tive in optimizing queries of video-heavy large Web objects. That is
                                   compounded by the fact that the amount and types of data in the
                                   typical enterprise are continually proliferating, so the federated data-
                                   base implementer is chasing a moving target.
                                   Periodically, an enterprise database supplier will propose to get
                                   around this problem by simply providing different “sub-database”
                                   software within the same database for each data type, then persuad-
                                   ing the organization to migrate all other data in the enterprise to its
                                   database. Three years ago, it looked as if Oracle might actually
                                   achieve this goal  but that was a market mirage. Data migration of
                                   all legacy databases and upgrading of all legacy applications, de-
                                   pending on each legacy database, is simply too hard for most if not
                                   all enterprises.
                                   The result is that, for now, the vision of one enterprise-standard da-
                                   tabase or of a federated database that can encompass all data sources
                                   is pretty much dead. Organizations can still apply a federated data-
                                   base to combine two existing data sources from the same supplier, if
                                   that supplier supports it, but that is only a minor step toward infor-
                                   mation aggregation.

                                   Action Items
                                   Clearly, today’s information aggregation tools have enormous poten-
                                   tial to support strategic information management by helping to iden-
                                   tify, manage, and leverage existing proprietary competitive-
                                   advantage data. Just as clearly, no one has combined these tools in an
                                   overall tool set to do this.
                                   The action item for IT buyers, therefore, is to assess existing infor-
                                   mation aggregation tools within their enterprises, supplement the
                                   tools where necessary, and create a long-range plan to use them to
                                   identify, manage, and leverage the enterprise’s data sources. A key


All print and electronic rights are the property of Aberdeen Group © 2003
38 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



to success in this effort is the implementation of EII not merely on a
per-project basis, but also as an ongoing effort to amass metadata
about all enterprise data sources, including nonrelational ones. The
political payoff for “data fiefdoms” that provide this metadata is
greater exposure to customers via the Web and greater cost cutting as
database administrators operate across data sources.
The action item for suppliers is to actually implement a full-fledged
information aggregation tool set. That would mean not only combin-
ing data migration/mass download, replication/ETL, data ware-
house/data mart, enterprise and mid-tier operational data store, and
EII tools, but also defining  and aiding customers in defining 
when to use each of these tools for strategic information manage-
ment.
In most cases, the pioneers of new computing technologies take the
arrows. Because the component technologies are already in most
cases field proven and well supported, all that the pioneers of strate-
gic information management risk is a relatively small added invest-
ment. By contrast, the benefits to the first mover are not only imme-
diate competitive advantage but also short- and long-term cost sav-
ings plus long-term entrenched competitive advantage.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 39
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Five:
                                   Market Forecast and Segmentation

                                   Key Technologies for EII Initiatives
                                   As stated in Chapter Two, EII is a business issue and, if implemented
                                   correctly, should improve the overall bottom line. Moreover, taking
                                   the appropriate first steps on an EII project can have a significant, posi-
                                   tive effect on the final success of an entire information integration ini-
                                   tiative.
                                   By implementing EII solutions, enterprises can isolate their applica-
                                   tions from the extensive differences in back-end databases and un-
                                   derstand the potential of an open, heterogeneous, multisupplier com-
                                   puting infrastructure.
                                   Enterprises are increasingly adopting EII-type approaches as part of
                                   their efforts to identify and rationalize their information assets. Ear-
                                   lier efforts to create a “universal repository” containing metadata
                                   about all of a corporation’s data, typically as part of a data warehous-
                                   ing effort, failed because lines of business had no incentive to hand
                                   over control of their information assets to a corporate IT department.
                                   In contrast, today’s lines of business clearly have a strong bottom-
                                   line incentive to make their information available to new customers
                                   via the Web, partners and suppliers via EBI, and internal employees
                                   via employee self-service portals.
                                   The problem to date has been that information integration ap-
                                   proaches have been fragmented, sometimes incompatible, and typi-
                                   cally not so cost-effective as an overall EII solution.

                                   Aberdeen EII Technology Segmentation Model
                                   The Aberdeen EII segmentation model represents the various tech-
                                   nology components that often complement an EII tool in an overall
                                   solution. The aim of the model is to identify suppliers that are most
                                   likely to complement an EII solution. Aberdeen defines the various
                                   EII “complementary technologies” in order to provide a clear under-
                                   standing of the functionality provided by each technology category.
                                   Aberdeen research indicates that integrating an EII solution with
                                   related technologies will be the most attractive integration solution
                                   for enterprises that seek to integrate their information in a global,
                                   cost-effective way.
                                   Aberdeen notes the following complementary technologies:




All print and electronic rights are the property of Aberdeen Group © 2003
40 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•     EAI technologies

•     Database technologies

•     Application server technologies

•     XML messaging technologies

EAI
EAI suppliers’ products offer the ability to pass data between enter-
prise applications. Their key technologies complementary to EII are
data transport, data integration, and business process support.

 Data Transport
In an EAI solution, data transport technology (“adapters” or ETL)
provides support for communications between objects and applica-
tions, providing greater performance than standard file transfers. In
addition, it provides flexibility in routing data or objects to many
recipients on multiple platforms, regardless of system or network
failures. Thus, EAI data transport can be useful in transporting data
between an EII solution and an enterprise application or in adding
application-specific data to the EII solution’s information base.

 Data Integration
In an EAI solution, data integration technology provides the ability
to manage a disparate set of application data sources and targets us-
ing a tool set. This tool set allows the user to seamlessly flow data
from step to step in a process without having to go outside of the
tool. A data integration product has the ability to manage an in-
creased volume or number of similar objects  for example, the
volume of data transformations or the number of users accessing a
data mart. The scalability of the data integration tool is linear  if
the volume of data transformations doubles, then the time to process
the data integrations should also double. A data integration product
can manage a nonlinear increase in difficulty — measured in the
workload of individuals or systems or in the functional limitations of
software — because of new intricacies when working with the inter-
relationships between or among objects.
The application of EAI data integration tools in EII is straightfor-
ward. Therefore, EAI data integration can serve as an alternative way
to combine data sources.

 Business Process Support
A business process flow is inherently composed of multiple, distinct,
work-based processes or steps. Usually, it is carried out over or
through multiple organizations and managerial levels within an en-


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 41
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   terprise. Conceivably — and usually — not all of the personnel and
                                   organizations involved in the process will be users of the same line
                                   of business. The best process flow will need to reach out beyond its
                                   normally associated application boundaries to provide for enter-
                                   prisewide process-flow automation.
                                   In an EAI solution, support and integration are done at the level of
                                   business processes, not transactions. The solutions enable the easier
                                   reuse of the integration techniques across heterogeneous environ-
                                   ments; organizations can also implement integration solutions with-
                                   out needing detailed knowledge of the application infrastructure’s
                                   specific underlying technologies — a likely situation when the other
                                   application resides in a different company. This capability can be
                                   particularly useful when meshing an EII solution with the business
                                   processes in another company via EBI.

                                   Database Technologies
                                   Two sets of database supplier technologies are particularly useful as
                                   a complement to EII:
                                   •    Open veneers

                                   •    Integrated file and multimedia storage capabilities

                                    Open Veneers
                                   Sybase offers a product that provides a common front end to its own
                                   and other relational databases. This “veneer” lets developers write to
                                   a common SQL and allows users to issue the same transaction to any
                                   relational database. In combination with the integrated file and mul-
                                   timedia storage capabilities of suppliers such as Oracle, it allows
                                   relational access to a wide variety of data types. It does not allow the
                                   combination of data or a transaction to cross multiple suppliers’ da-
                                   tabases.
                                   An open veneer such as Sybase’s can significantly ease the EII solu-
                                   tion’s task of accessing multiple databases.

                                   Integrated File and Multimedia Storage Capabilities
                                   IBM/Informix (IDS), Oracle (Oracle8i and Oracle9i), and Microsoft
                                   (SQL Server 7.0 and 2000) have made a particular point of allowing
                                   users to fold both multimedia/object data and desktop files into their
                                   relational databases. IBM DB2 and Sybase Enterprise Server also
                                   provide some nonrelational-data-type and file access capabilities.
                                   These capabilities allow the user to fold nonrelational data into an
                                   existing database in order to give the EII solution easier access to a
                                   wide variety of information and to provide greater ability to combine




All print and electronic rights are the property of Aberdeen Group © 2003
42 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



that information by using the database’s cross-data-type-transaction
capabilities.

XML Messaging Technologies
XML is a descendant of SGML (Standard Generalized Markup Lan-
guage) and a sibling of HTML (HyperText Markup Language) 
both ISO (International Standards Organization) and Internet stan-
dards. XML was developed to add data management features similar
to those of SGML, but went beyond HTML by keeping the data and
its context or metadata together in the same “message.” As a result,
when the information displayed on a Web page is stored in XML, a
price change can be inserted on a Web page immediately by chang-
ing the data portion of the XML, without reprogramming the entire
page.
XML also provides great improvement in the portability of data,
inside and outside of the enterprise. By agreeing to accept the defini-
tion of data embodied in an XML message, another department, an
enterprise portal, or an outside supplier can access, display, or re-
spond to that data. To ease the use of this type of EBI in particular
industries, an abundance of XML dialects (properly termed “vocabu-
laries”) have emerged.
XML databases store data as XML objects in an object-oriented da-
tabase. Although XML databases do not replace enterprise-scale
databases, they are useful not only for permanent or “cache” storage
of XML data but also as a repository for XML information used in
XML-based interactions; as a second-tier or “cache” server for gen-
eral-purpose Web data processing; and as a “common language”
database for storing a wide variety of data types, such as files, mul-
timedia data, and relational data. In such small-to-medium scale da-
tabase situations, a typical advantage includes the storing of data in a
widely useful format, supporting key XML-using applications with
less customization and providing greater processing speed for trans-
actions involving XML.
XML messaging is, therefore, a highly flexible way for the EII solu-
tion to communicate with both front-end programs/users and back-
end databases. Moreover, an XML database can be a high-
performance way for the EII solution to store cache data and direc-
tory metadata.

Combinations of Technologies
Combinations of these technologies are often useful in particular EII-
related situations. Consider, for example, the products of Progress
Corp. The ObjectStore XML database can be used as a mid-tier
ODS. The PeerDirect InnerEdge and OuterEdge Server replication
solution can deliver high performance in ETL and data migra-


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 43
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   tion/download. The SonicMQ XML messaging products support
                                   enterprise and cross-enterprise XML messaging infrastructure,
                                   allowing the exchange of information in such applications as EBI.
                                   The Progress OpenEdge “embedded infrastructure” allows
                                   organizations to apply the foregoing products plus an application
                                   server and enterprise database in creating scalable industry-specific
                                   applications rapidly.

                                   Summarizing the Model
                                   Figure 3 shows Aberdeen’s EII technology segmentation model,
                                   which can be used to categorize various EII and related offerings
                                   based on technology and functionality. The model also illustrates the
                                   interdependence of the various technologies.

                                   Figure 3: EII Technology Segmentation Model




                                                                                   Source: Aberdeen Group, July 2003




All print and electronic rights are the property of Aberdeen Group © 2003
44 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Table 6 describes how the suppliers profiled in this report fit within
the Aberdeen segmentation model.

Table 6: EII and Related Suppliers

Aberdeen EII Segmentation Model
Technology Segmentation                Examples of Suppliers
EAI technology                         Actional, BEA, Celcorp, Crossweave, iWay,
                                       SeeBeyond, TIBCO, Viewlocity, Vignette, Vitria,
                                       webMethods, CNT, MITEM, Tempest, Candle,
                                       CommerceQuest, Compaq, Compuware, Darc
                                       Software, DataMirror, Dharma, ETI, IBM, Level
                                       8 Systems, Neon Systems, OST Business
                                       Rules, Percussion, Scribe Software, Sybase,
                                       Taviz Technology, Transoft, EnterWorks, Mer-
                                       cator, PTC, Software AG, WRQ
Database technology                    IBM, IBM/Informix, Microsoft, Oracle, Sybase

XML messaging                          Progress/Excelon, Ipedo, Metapa, Software AG
                                       (database); ArborText, Altova, and SoftQuad
                                       (publishing); DataChannel, Sequoia Software,
                                       Sybase, Bowstreet, SilverStream, Oracle, and
                                       iPlanet (enterprise portal); webMethods, InfoTe-
                                       ria, IBM, Sun, i4i, Whitehill, and Inera (EBI);
                                       Vitria, Contivo (EDI); HP, IBM, Sun, Microsoft
                                       (Web services)
EII solution                           Attunity, Business Objects, Ipedo, XAware,
                                       MetaMatrix, Venetica, BEA, Nimble Technolo-
                                       gies, IBM (Information Integrator)
                                            Source: Aberdeen Group, April 2003



Table 7 categorizes the EII suppliers based on the core technology
solutions that they provide.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 45
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                  Table 7: EII and Related Suppliers

                                   Aberdeen EII Segmentation Model
                                   Technology Segmentation                    Examples of Suppliers
                                   EAI Technology                             Actional, BEA, Celcorp, Crossweave, iWay,
                                                                              SeeBeyond, TIBCO, Viewlocity, Vignette, Vitria,
                                                                              webMethods, CNT, MITEM, Tempest, Candle,
                                                                              CommerceQuest, Compaq, Compuware, Darc
                                                                              Software, DataMirror, Dharma, ETI, IBM, Level
                                                                              8 Systems, Neon Systems, OST Business
                                                                              Rules, Percussion, Scribe Software, Sybase,
                                                                              Taviz Technology, Transoft, EnterWorks, Mer-
                                                                              cator, PTC, Software AG, WRQ
                                   Database Technology                        IBM, IBM/Informix, Microsoft, Oracle, Sybase

                                   XML Messaging                              Progress/Excelon, Ipedo, Metapa, Software AG
                                                                              (database); ArborText, Altova, and SoftQuad
                                                                              (publishing); DataChannel, Sequoia Software,
                                                                              Sybase, Bowstreet, SilverStream, Oracle, and
                                                                              iPlanet (enterprise portal); webMethods, InfoTe-
                                                                              ria, IBM, Sun, i4i, Whitehill, and Inera (EBI);
                                                                              Vitria, Contivo (EDI); HP, IBM, Sun, Microsoft
                                                                              (Web services)
                                   EII Solution                               Attunity, Business Objects, Ipedo, XAware,
                                                                              MetaMatrix, Venetica, BEA, Nimble Technolo-
                                                                              gies, IBM (Information Integrator)
                                                                                  Source: Aberdeen Group, April 2003




All print and electronic rights are the property of Aberdeen Group © 2003
46 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Growth Forecasts
Most of the suppliers profiled in this report do not break out reve-
nues associated with “data integration”  a frequently used supplier
term for what we now call EII. Moreover, for suppliers, the dividing
line between EII, EAI, content management, and ETL tools for data
warehousing is frequently not a clear and precise one. Aberdeen has
assigned to EII only revenues in which the primary purpose of the
EII solution is to integrate data across databases for delivery to tar-
gets other than data warehouses. This category includes a small pro-
portion of the EAI and ETL markets, as well as projects that involve
an enterprise portal or EBI. Revenues from suppliers that do not pro-
vide a full-fledged EII solution are not included.
Based on available data regarding supplier revenue, Table 5 repre-
sents current market revenue and projected market growth. Aberdeen
believes that the overall market will grow by 80% in 2003, with
growth being especially fueled by the need to rationalize existing e-
business efforts. Web services will contribute significantly to EII
revenues over the next year, and they will be increasingly important
from 2004 onward.
These estimates are strongly dependent on the overall growth of the
high-tech sector of the economy. Specifically, if enterprises continue
to delay spending on new initiatives, such as business process auto-
mation, into the first quarter of 2004, these numbers will be overes-
timates. If enterprises advance new initiatives in the third quarter of
2003, then these numbers will be underestimates.
Table 8 shows that, as yet, no single supplier dominates the market.
Typically, suppliers do not release revenue figures. Therefore, these
Aberdeen estimates are based on the number of employees and the
number of years that a particular product has been offered.

Table 8: EII Supplier Revenues (Aberdeen Estimates,
Projected over 2003)

Supplier                          Revenues
Business Objects                  $15 million
Attunity                          $4 million to $7 million
BEA                               $25 million
XAware                            $4 million to $7 million
IBM                               $60 million
MetaMatrix                        $10 million



                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 47
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Nimble Technologies                    $4 million to $7 million
                                   Venetica                               $7 million to $10 million
                                                                                    Source: Aberdeen Group, July 2003

                                   Aberdeen believes that the professional services needed to success-
                                   fully implement an EII initiative will become more easily measurable
                                   as revenue over the next 6 to 12 months. However, Aberdeen’s field
                                   experience indicates that, for every dollar spent on software applica-
                                   tion licenses, $1.25 to $1.50 is spent on professional services to im-
                                   plement integration of the application and the resultant data.
                                   Table 9 shows our estimate of the size of closely related markets. As
                                   these markets expand and mature, their products increase the demand
                                   for EII as an integral part of the solution. Thus, EII’s impact extends
                                   far beyond its own market.

                                  Table 9: Revenues for Markets Related to EII

                                   Markets                         2002               2003              2004

                                   EAI                             $2.2 billion       $2.6 billion      $3.0 billion
                                   Content management              $1.2 billion       $1.6 billion      $2.0 billion
                                   Portal                          $1.5 billion       $2.2 billion      $2.8 billion
                                   Total                           $4.9 billion       $6.4 billion      $7.8 billion
                                                                                   Source: Aberdeen Group, April 2003




All print and electronic rights are the property of Aberdeen Group © 2003
48 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Chapter Six:
Aberdeen Observations

Impact of Major IT Trends
Aberdeen research shows that EII is on the critical path in corporate
efforts to achieve comprehensive, information-leveraging, e-business
architectures. Piecemeal efforts to link back-end databases to Web
sites, EBI, and enterprise portals have left a rat’s nest of point-to-
point connections between Web server, application server, or appli-
cations and back-end Web text/graphics, workgroup files, or enter-
prise databases. EII’s many-to-one-to-many approach is, therefore,
well suited to rationalizing connections between internal and external
users and key corporate information. However, its ability to do so is
strongly affected by today’s key IT trends, as described below.

Application Servers
Over the last two years, application servers have been steadily incor-
porating many of the middleware functions of an e-business architec-
ture, including load balancing, acting as a development framework
(hence, the increasing linkage of application servers and develop-
ment tool sets), and application management. One of the main selling
points of an application server has been that it is more manageable,
scalable, and efficient because application servers can integrate data
from a variety of heterogeneous sources, including back-office ap-
plications and databases. Therefore, over the next two years, many of
today’s EII solutions may possibly be incorporated in an application
server  as BEA WebLogic for Liquid Data already does (Enosys).
However, this might require the reprogramming of much of the exist-
ing code that is used to access back-end databases. Therefore, IT
buyers examining an application server that incorporates an EII solu-
tion should carefully assess its ability to support existing database
connections without recoding.

The Role of Java
Enterprise JavaBeans (EJB), the Java specification for server-side
components, has received significant interest because of its ability to
simplify and accelerate the development of business applications. By
providing services such as transaction and resource management,
persistence, mobility, versioning, scalability, and security, it enables
the easier development of robust, mission-critical applications that
access back-end databases — and using fewer developers. The wide
availability of EJB 2.0 components means that programming data
access in Java is becoming much easier, and EII is a complement that


                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 49
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   makes the job easier still. In other words, because Java is well suited
                                   for EII and vice versa, the continued adoption of Java improves the
                                   market for and usefulness of EII.

                                   Extensible Markup Language (XML)
                                   XML is now a de facto, as well as du jour, standard. All major sup-
                                   pliers provide XML functionality, and many smaller suppliers focus
                                   on XML-based messaging, allowing enterprises to not only
                                   communicate externally but also drive business processes internally
                                   (and externally). As noted above, XML is particularly well suited for
                                   EII solutions because it can provide a common language for trans-
                                   mitting transactions from back-end data sources to internal and ex-
                                   ternal users and programs. A proliferation of XML standards is caus-
                                   ing difficulties for users in implementing XML connections with
                                   particular customers, partners, and suppliers, but that does not dimin-
                                   ish the basic value proposition of EII. XML is, increasingly, a check-
                                   list item in EII solutions. A related upcoming standard is XQuery,
                                   which supports standardized querying on XML-formatted data.

                                   Emphasis on Cost-Effective Administration
                                   The economic downturn has caused enterprises to focus on rational-
                                   izing existing architectures for greater cost-effectiveness, rather than
                                   for building new e-business applications. A key area of concern is
                                   administration, as the costs of administrative personnel mount while
                                   hardware and networking costs decline. In response, suppliers have
                                   provided more automated and more administrator-friendly solutions.
                                   EII promises to reduce the administrative burden by offering a single
                                   administrative interface to multiple back-end databases, but, at pre-
                                   sent, the lack of administrative support in most EII solutions makes it
                                   appear that EII is an added cost burden rather than a cost savings. In
                                   fact, EII reduces administrative costs by simplifying user-to-database
                                   connections and making cross-database transactions more visible to
                                   the administrator. Over the next 18 months, increasing support for
                                   administration in EII products will allow administrators to begin to
                                   monitor multiple databases from different suppliers as one database.
                                   Moreover, connections to systems management tools will allow EII
                                   to take its proper place in overall systems administration.

                                   Enterprise Portals
                                   An enterprise portal allows the enterprise to coordinate the data dis-
                                   played across applications and to fully leverage all major business-
                                   critical company databases. Moreover, a portal allows the enterprise
                                   to expose these data to new markets, such as Net markets and ex-
                                   changes in general. Along with these competitive advantages come
                                   built-in cost savings — not only the cost savings derived from doing
                                   everything over the Internet (outsourced or consolidated) but also the


All print and electronic rights are the property of Aberdeen Group © 2003
50 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



IT cost savings derived from simplifying the administration of the
database/application connections, thereby saving key administrative
costs. There is a side benefit of equal importance: e-information can
unify the enterprise’s “data islands.” However, both of these “data-
base benefits” will fail to emerge unless the enterprise portal uses EII
technology to provide cross-database operations and displays. There-
fore, EII is critical to the long-term success of enterprise portals.
Likewise, a successful enterprise portal is a prime “target of oppor-
tunity” for users seeking to apply EII to initial projects promising
major return on investment.

Web Services
Enterprises that take advantage of the Web in their businesses inevi-
tably begin to implement Web services. The fundamental idea of
Web services is to apply the tried-and-true idea of a service  a cen-
tral piece of software that carries out specific functions that its users
demand — to the Internet. The Web service is self-describing be-
cause it contains enough information about itself to allow any Web
user or Web application to find out what it does and then to use it,
making it a highly flexible service. The Web service’s ability to use
other Web applications to carry out complex tasks makes it feature
rich and offers enterprises a new way to mine the Web for competi-
tive-advantage applications and content.
Moreover, Web services allow IT to write one server version  no
client version is needed  that can be automatically deployed across
all the servers in the organization. It thereby becomes instantly avail-
able to the entire organization as well as global customers and a
partner base of millions. These technical advantages also lead to
broader business benefits, such as lowering the cost of doing busi-
ness, allowing companies to achieve much greater efficiencies from
using broadly available applications, and giving the organization
greater ability to adapt quickly to changing conditions. These advan-
tages are so great that Aberdeen expects implementing Web services
and upgrading existing applications to be Web services will be the
major new efforts of most enterprises over the next two years. EII
plays a role in this effort because it provides a common access point
from Web services to the “enterprise substrate”  key proprietary
information. However, in order to allow organizations to fully lever-
age EII’s potential in abetting Web services, EII solutions must pro-
vide SOAP support, frameworks supporting Web service develop-
ment tools, and, if possible, a Web service provider interface. For
further details, see the Aberdeen White Paper, EII and Web Services
(July 2002).




                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 51
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Supplier Success Factors
                                   To meet long-term user flexibility needs, suppliers should continue
                                   to integrate various middleware technologies into a smoothly work-
                                   ing whole. The aim is to enable IT to create a distributed environ-
                                   ment in which applications and data move instantly, cost-effectively,
                                   and flexibly to where a user needs them.
                                   A supplier’s EII solution should be extensible and reusable for the
                                   project at hand, as well as for future projects. The tools should be
                                   designed in such a manner that users are able to extend the tool from
                                   a per-project basis to ongoing enterprisewide usage.
                                   In the long term, the EII supplier’s tools and solutions should be able
                                   to contribute to an organization’s bottom line by reducing the costs
                                   of application design, development, deployment, and, above all,
                                   maintenance. Suppliers should also satisfy overall user criteria, such
                                   as scalability and robustness.
                                   Outside resources should be leveraged through strategic partnerships.
                                   A potential bottleneck for present EII suppliers could be customer
                                   demand for services. In-house services adapted to EII, key partner-
                                   ships with systems integrators, as well as the professional services of
                                   major infrastructure suppliers, can alleviate this bottleneck. It is also
                                   important to build partnerships with suppliers of complementary
                                   software products (e.g., enterprise portal infrastructure suppliers).
                                   Achieving customer satisfaction and delivering an expanding set of
                                   products will differentiate the new market leaders. Today, few EII
                                   providers have embraced integration with enterprise management
                                   products.
                                   Suppliers should capitalize on increased interest in cost-effectiveness
                                   via solution consolidation. This trend provides EII suppliers with the
                                   opportunity to sell the ability to consolidate databases without the
                                   pain of physically merging them.
                                   An unplumbed area is the use of EII for an “information audit.” Ser-
                                   vice providers can use automatic “repository population” tools in EII
                                   solutions to walk into a customer site and gain a map of major data.
                                   This map, like asset management maps, can be highly useful in rec-
                                   ommending ways of better leveraging information.

                                   Success Factors for Organizations
                                   Successful organizations establish business goals to be achieved by
                                   the implementation of an EII technology (e.g., increased sales and
                                   reduced cost of customer service). They identify the appropriate EII
                                   technology required to meet these goals and create metrics to gauge
                                   the successful use of the EII technology.



All print and electronic rights are the property of Aberdeen Group © 2003
52 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



EII initiatives may involve integrating many sources and targets
while maintaining independently coded modules for each integration
process. This process is extremely resource intensive. Using a single,
flexible, and consistent framework for each process will greatly re-
duce the amount of personnel resources needed to maintain and de-
velop the system.
An EII solution should be built on an architecture that has the ability
to scale, support, and introduce new technologies within a globally
distributed environment. In addition, the solution should provide the
flexibility to add multiple servers as a system grows, as well as the
ability to use preconfigured components that “hook” into legacy da-
tabases.
Aberdeen advises IT buyers to demand that the EII suppliers define a
path toward an integrated overall architecture. Choose the supplier
with the best combination of a strong current solution, a good vision,
and a solid, open position within the industry. Plan to prototype
within the next six months and to spread EII across the enterprise
architecture within the following year.
When selecting EII suppliers, organizations should look for two
critical attributes:
    1. Does the supplier have in-depth knowledge of the major da-
       tabases to be integrated? Can the supplier demonstrate that
       the integration will be reliable, scalable, and possible? Is the
       supplier able to provide references that show systems in pro-
       duction?
    2. Does the supplier have credibility (e.g., systems in produc-
       tion) in claiming to be able to support all of the relevant in-
       formation integration initiatives in which your company ex-
       pects to engage? Does the supplier have the consulting ex-
       pertise or partnerships that can bring best practices from
       other integration implementations to bear on your business
       problems and opportunities?
The IT buyer should proactively involve users. The executives; busi-
ness analysts; financial, marketing, and support representatives; and
sales professionals who will eventually be using the information
need to be involved in the integration requirements. These individu-
als can provide helpful insight into actual usage patterns and what
will and will not be useful. Incorporating their opinions into the inte-
gration and deployment process also creates a sense of ownership
and excitement on the part of users for the new integrated application
systems.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 53
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Aberdeen Observations and Conclusions
                                   Aberdeen research shows that there now exists a distinct market for
                                   EII that is beginning the “high-end user per-project” stage. This
                                   market is driven by enterprises’ needs to rationalize existing access
                                   to multiple databases, both to cut administrative costs and to lever-
                                   age competitive-advantage, cross-database, proprietary information.
                                   EII solutions do this by providing many-to-one-to-many mechanisms
                                   to take a wide variety of back-end data sources, merge them into a
                                   common format, and pass them to a variety of front-end users and
                                   programs.
                                   EII solutions also provide specific value-add to enterprise portal and
                                   EBI solution upgrade. Enterprise portals’ focus on providing end-
                                   users with access to multiple information sources means that EII’s
                                   ability to provide cross-database data and/or support cross-database
                                   transactions simplifies the developer’s job and the portal’s architec-
                                   ture. EBI solutions can use EII to expose more data to the outside,
                                   with more control over a single (EII) exposure point.
                                   EII can also play an important role in Web services implementations.
                                   A “Web-servicized” EII solution can provide easier access by other
                                   Web services to local, remote, and cross-company data.

                                   Positioning and Capabilities

                                   Market Segmentation
                                   As a new market with relatively few entrants, EII also has relatively
                                   few segments. The most meaningful division is between suppliers
                                   that focus primarily on EII (e.g., MetaMatrix) and suppliers for
                                   which “data integration” is one among many middleware products or
                                   that focus strictly on business intelligence (e.g., Business Objects).
                                   Some suppliers focus on EII for content databases; others focus on
                                   EII across data marts and decision-support databases.
                                   As noted earlier, Aberdeen believes that the technology in the EII
                                   market is moving toward a full single database image or “veneer”
                                   that makes multiple databases look like a single database. As a result,
                                   suppliers that focus primarily on EII and can draw on knowledge of
                                   database technology are at a significant advantage in the next two
                                   years.

                                   Technology Interdependency
                                   Aberdeen research has indicated that one key criterion to being a
                                   long-time player in the EII market space is the ability to develop key
                                   alliances. These alliances provide complementary products, com-
                                   plementary services, efficient access to new markets, and joint ef-
                                   forts in development.


All print and electronic rights are the property of Aberdeen Group © 2003
54 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



Aberdeen research indicates that EII suppliers will benefit most not
from integration with each other’s technologies, but via partnerships
with full-function “infrastructure solutions” for particular enterprise
needs. Again, the most attractive partnerships will allow better sup-
port for enterprise portals, EBI, and Web services. Other useful part-
nerships will combine EII and a mid-tier ODS, or EII and EAI.
This is clearly a window of opportunity for Web infrastructure sup-
pliers such as Sun, IBM, BEA, and Sybase. By establishing partner-
ships with EII suppliers or acquiring EII solutions, these suppliers
can position themselves as a stronger long-term solution in enterprise
portals, EBI, and Web services. So far, IBM and BEA have been
quickest to respond. By contrast, suppliers such as Oracle and Mi-
crosoft have not shown a full appreciation of the potential of EII.
EII suppliers have begun to establish alliances with professional ser-
vice organizations (PSOs). The A-list comprises the Big Five PSOs
(Andersen Consulting, Deloitte & Touche, Ernst & Young, KPMG,
and PricewaterhouseCoopers) and industry service heavyweights
(e.g., HP and Sun). Aberdeen expects the extension and deepening of
those relationships over the next two years.

Distribution and Implementation
Many EII suppliers are young companies, in the range of one to four
years. The market’s awareness of most of these suppliers’ EII identi-
ties began in 2001. Thus, the EII suppliers discussed here, except for
Business Objects, BEA, and IBM, are still mostly in their formative
stages.
Among these newcomers, there is no common distribution model for
the EII market. All of these suppliers seek to define themselves as
software solution suppliers that rely on their own systems integration
efforts, third-party implementers, and training to address customer
implementation requirements. Sales models are primarily direct, yet
some companies have initiated alternative distribution or original
equipment manufacturer (OEM) strategies as significant future dis-
tribution and revenue-enhancing strategies. Direct sales capabilities
were limited at the start of 2003, but continue to significantly ex-
pand.
The established suppliers  IBM, BEA, and Business Objects 
have already established channels, which they are beginning to lev-
erage. Especially promising is the “services-led” model, in which EII
comes bundled with extensive services for system integration and
advice on strategic uses of EII and other software infrastructure tools
and services.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 55
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Major Forces

                                   Mergers and Acquisitions (M&A)
                                   Because it is such a new and small market, most “newcomer” EII
                                   suppliers have not had the capital to pursue acquisitions. Aberdeen
                                   expects that over the next two years, most M&A activity will con-
                                   tinue to center on larger “infrastructure solution” providers acquiring
                                   “newcomer” EII suppliers.
                                   In the case of full-function EII solutions, a barrier to these acquisi-
                                   tions is that being acquired by one provider locks the EII solution
                                   supplier out of the installed base of other providers  for example,
                                   being acquired by IBM might lock an EII supplier out of Oracle’s
                                   installed base. However, because these installed bases are far larger
                                   targets of opportunity than EII suppliers currently have, Aberdeen
                                   expects some acquisitions to proceed despite the barrier.

                                   Standardization and Integration
                                   EII solutions are and must be firmly founded on standards such as
                                   SQL, ODBC/JDBC, and EJB. A key future standard is XML, and
                                   Aberdeen expects all EII suppliers to wrap their transactions in XML
                                   over the next two years, if they have not done so already.
                                   As noted above, key targets for integration over the next two years
                                   will be application servers and Web services infrastructures. Appli-
                                   cation servers are already sources of legacy, cross-database code. In
                                   order to simplify the Web architecture, they will need to merge that
                                   code with code written directly on an EII framework. Some EII solu-
                                   tions that have not done so already will also need to define connec-
                                   tions to Web services infrastructure solutions as another data “tar-
                                   get,” as well as to define their solutions as Web services.

                                   Success Factors
                                   Suppliers must work toward achieving customer satisfaction.
                                   Delivering an expanding set of products will differentiate the new
                                   market leaders. Furthermore, when choosing an EII supplier, users
                                   should look for the critical attributes listed in User Success Factors.
                                   There were significant deployments in 2003, so IT buyers should
                                   expect to have enough reference accounts to interview.
                                   Organizations should apply the evaluation criteria cited in Chapter
                                   Two to ensure that they are implementing an integration platform
                                   that is flexible, extensible, and scalable.

                                   The Future
                                   Six enabling technologies will have a strong impact on EII solutions
                                   during 2003: application servers, Java, XML, database administra-


All print and electronic rights are the property of Aberdeen Group © 2003
56 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



tion technologies, enterprise portals, and Web services. These tech-
nologies are critical to delivering long-term value-add from an EII
implementation and to simplifying an e-business architecture using
EII.
Organizations need to coordinate their initiatives for EII and EBI as
well as EII and architecture rationalization or cost cutting. Doing so
correctly will avoid another decade of slow, costly, and mostly un-
necessary piece-by-piece data integration, and it will allow
organizations to invest the capital saved into key new initiatives,
such as Web services.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 57
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Chapter Seven:
                                   Supplier Profile
                                   As noted above, many EII suppliers profiled in this report are small,
                                   recently created companies. The reader should, therefore, pay addi-
                                   tional attention to their partnerships to determine their ability to sup-
                                   port complex enterprise information architectures.




All print and electronic rights are the property of Aberdeen Group © 2003
58 • AberdeenGroup
                       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




MetaMatrix, Inc.
680 Fifth Avenue
10th Floor
New York, NY 10019
(314) 739-3190, Ext. 120
www.metamatrix.com

Market Position
MetaMatrix sees itself as a provider of an “open, rapid-deployment
system” for helping enterprises “integrate data sources and manage
metadata” globally. MetaMatrix aims its EII solution especially at:
•   Financial services

•   Government

•   Migration services

•   Large and midsize systems integration companies

•   CRM/call center applications

•   Enterprise portals

•   ASPs

•   Business intelligence, knowledge management, and data ware-
    housing

•   B-to-B and B-to-C exchanges

•   Other custom applications

MetaMatrix’s full set of features, ability to tie in to formalized de-
velopment methodologies, and administrative support make it a
prime candidate for large enterprises with long-term EII, architecture
rationalization, and administrative cost-cutting plans, or for enter-
prises seeking to rapidly develop or upgrade complex, business-
critical, information-driven applications. MetaMatrix’s EII solution
is also appropriate for a range of more focused efforts, including
meshing with EAI solutions to coordinate business processes and
business rules or providing dynamic querying across relational and
rich-media “content” data such as Internet feeds or time series data,
as well as supporting EBI, enterprise portals, and BI/Web analytics.
Although MetaMatrix’s sophistication may make it “overkill” for



                                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                          AberdeenGroup • 59
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   small organizations, its breadth of functionality makes it useful for
                                   most if not all EII efforts of large enterprises.
                                   The MetaMatrix product set is a full-featured EII solution with
                                   MetaBase, a modeling tool based on MOF (OMG’s Meta-Object
                                   Facility), with a searching and browsing tool (MetaViewer), a re-
                                   pository manager (MetaData Repository Manager), and MetaMatrix
                                   Server, with transaction support, development features, administra-
                                   tive tools, a “single database image,” ETL “connectors,” and access
                                   control, as well as publish/subscribe capabilities. MetaMatrix differ-
                                   entiates its EII solution especially by its:
                                   •    Abstraction Layer — MetaMatrix allows creation of virtual da-
                                        tabases, which are a logical layer between the disparate data
                                        sources and the application developer or application. The layer
                                        integrates the information so that from the outside it looks like a
                                        single database to the developer or the application. Inside this
                                        layer, MetaMatrix metadata mappings point to the sources of
                                        each element.

                                   •    Two way XA-compliant transactions.

                                   •    Scalability owing to the solution to being entirely built in Java.

                                   •    Interoperability with a wide variety of front-end programs via
                                        XMI, JDBC, ODBC, SOAP, and XML support.

                                   •    Metadata management system based on standards such as MOF,
                                        XML Metadata Interchange (XMI), Common Warehouse Meta-
                                        Model (CWM), UML (Uniform Modeling Language), and other
                                        relevant OMG standards.

                                   •    A modeling tool that allows abstraction of existing metadata
                                        (improving programmer productivity by reducing custom cod-
                                        ing), as well as creation of user-defined “metamodels.”

                                   •    Sophisticated metadata-search, querying, and “connector” fea-
                                        tures.

                                   •    Ability to support business rules in the repository.

                                   Core Products
                                   MetaMatrix provides a “model-driven” EII solution that combines an
                                   enterprise metadata management system, MetaBase, with scalable
                                   query management technology. MetaMatrix offers two main prod-
                                   ucts, MetaBase — which can stand alone as an enterprise metadata
                                   management system — and MetaMatrix Information Integration
                                   Server. MetaBase includes:


All print and electronic rights are the property of Aberdeen Group © 2003
60 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



•   MetaData Modeler, which uploads metadata from data sources,
    places them in a “model” format, and allows users to manage
    these models as well as creating models of their own

•   The ability to create an abstraction layer through virtual meta-
    data models

•   MetaBase Repository, which houses physical and virtual models
    in an XMI format and uses them to generate runtime models for
    the MetaMatrix Information Integration Server

•   Searchbase, a search tool that allows MetaData Modeler users to
    examine the contents of the MetaBase Repository in a flexible
    way

•   MetaViewer, a browser-based search tool accessing metadata
    models and data types across intranets or the Internet

MetaMatrix Server includes:
•   MetaMatrix Server, which provides user-definable virtual data-
    bases based on cross-database metadata, with views and support
    for SQL operations. MetaMatrix Server also allows developers
    to access data at a high “virtual metadata” level.

•   MetaMatrix Administration Console, a GUI-based administra-
    tive console that monitors MetaMatrix Server operations, allows
    administration of user accounts and access rights, and provides a
    log of transactions.

•   Query Builder, a utility that allows developers to create and test
    queries.

•   MetaMatrix Connector Development Kit, an SDK that allows
    developers to create connectors and test them on a simulated
    MetaMatrix Server, as well as against live data.

MetaMatrix Server can be deployed on J2EE-compliant application
servers such as IBM WebSphere, BEA WebLogic, SAP Application
Server, and JBoss-compliant open source application servers.
MetaMatrix Server provides support for Web services via
SOAP/XML, as well as access via ODBC and JDBC using SQL.
MetaMatrix’s EII solution allows cross-database access to relational
and legacy databases, unstructured data, packaged-application data-
bases, and XML-based messaging (e.g., data from across an organ-
izational boundary). As noted above, it offers an extensible connec-
tor framework for development of custom connectors as well as sup-
port for JDBC-style connectors from a number of partners.


                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 61
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



                                   Services and Partnerships
                                   MetaMatrix provides consulting and training in how to create and
                                   use its models. MetaMatrix partners with Consulting and Integration
                                   Partners to provide support throughout the customer’s EII life cycle.
                                   MetaMatrix recently announced an OEM agreement with SAP to
                                   provide MetaMatrix Server embedded in SAP NetWeaver, SAP’s
                                   new Enterprise Services Architecture.

                                   Aberdeen Conclusions
                                   MetaMatrix’s EII solution is the Cadillac of today’s EII solutions —
                                   it is comprehensive in its feature set, able to support developers and
                                   administrators at a relatively high level, and includes sophisticated
                                   features for complex-application development. Thus, MetaMatrix
                                   may not be appropriate for medium-sized enterprises without the
                                   need for sophisticated modeling of multiple databases, but is highly
                                   suitable for the largest enterprises with complex information archi-
                                   tectures or a need to develop complex cross-database applications.
                                   Overall, MetaMatrix is clearly taking a leadership role among early
                                   entrants into the EII market in implementing the technology needed
                                   for EII to scale to the largest of enterprise needs and to provide a
                                   long-term enterprise information architecture. For these situations, IT
                                   buyers should look at MetaMatrix immediately.




All print and electronic rights are the property of Aberdeen Group © 2003
62 • AberdeenGroup
                      Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Author Profile

Wayne Kernochan, Managing Vice-President,
Platform Infrastructure
Wayne Kernochan focuses on databases, development environments,
and proprietary hardware. His areas of coverage also include related
software infrastructure, such as enterprise portal infrastructure, con-
tent management infrastructure, enterprise information integration
solutions, and testing and software life cycle tools. He also contrib-
utes in related areas such as XML databases and tools, Web services,
frameworks, and database administration utilities.
Kernochan has 25 years of experience in computers, including 12 as
a programmer and technical manager in databases, development
tools, e-mail, and office automation, most recently at Prime Com-
puter. Before joining Aberdeen, Kernochan covered non-mainframe
computer technologies for The Yankee Group.
Kernochan holds a B.A. in Government from Harvard University, an
M.S. in Computer Science from Cornell University, and an M.B.A.
in Information Systems from Sloan School of Management at M.I.T.




                                  All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                         AberdeenGroup • 63
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Appendix A:
                                   Lexicon of Acronyms and Abbreviations

                                   API                       Application Program Interface
                                   ASP                       Application Service Provider
                                   BI                        Business Intelligence
                                   CRM                       Customer Relationship Management
                                   EAI                       Enterprise Application Integration
                                   EBA                       Enterprise Business Application
                                   EBI                       e-business Integration
                                   EII                       Enterprise Information Integration
                                   EJB                       Enterprise JavaBeans
                                   ERP                       Enterprise Resource Planning
                                   ETL                       Extract, Transform, Load
                                   GUI                       Graphical User Interface
                                   HTML                      Hypertext Markup Language
                                   ITO                       International Standards Organization
                                   ITV                       Independent Software Vendor
                                   IT                        Information Technology
                                   J2EE                      Java 2 Enterprise Edition
                                   LAN                       Local Area Network
                                   LOB                       Line-of-Business
                                   OEM                       Original Equipment Manufacturer
                                   OLTP                      Online Transaction Processing
                                   PSO                       Professional Service Organization
                                   ROI                       Return on Investment
                                   SCM                       Supply Chain Management
                                   SDK                       Software Development Kit
                                   SGML                      Standard Generalized Markup Language
                                   SMB                       Small to Medium-Sized Businesses



All print and electronic rights are the property of Aberdeen Group © 2003
64 • AberdeenGroup
       Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)



SNMP    Simple Network Management Protocol
SQL     Structured Query Language
TCO     Total Cost of Ownership
VAR     Value-Added Reseller
WAN     Wide Area Network
XML     Extensible Markup Language




                   All print and electronic rights are the property of Aberdeen Group © 2003
                                                                          AberdeenGroup • 65
Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




                                   Appendix B:
                                   Related Aberdeen Research
                                   The following publication provides complementary market research
                                   relating to EII:
                                   Embedded Infrastructure Cost of Ownership Study (December
                                   2001)

                                   Information on this and any other Aberdeen publication can be found
                                   at www.aberdeen.com or by e-mail at info@aberdeen.com.




All print and electronic rights are the property of Aberdeen Group © 2003
66 • AberdeenGroup
                     Enterprise Information Integration — The New Way to Leverage E-information (Second Edition)




Appendix C:
Supplier Contact Information
MetaMatrix, Inc.
680 Fifth Avenue, 10th Floor
New York, NY 10019
(314) 739-3190, Ext. 120
www.metamatrix.com




                                 All print and electronic rights are the property of Aberdeen Group © 2003
                                                                                        AberdeenGroup • 67


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-eii-2003-ea3f1a |
| title | Enterprise Information Integration: The New Way to Leverage E-information (Second Edition) |
| author | Aberdeen Group |
| date | 2003-07 |
| type | employer-record |
| subject_domain | EII; enterprise information integration; data integration; information aggregation; ETL; EAI |
| methodology | market-analysis; technology-segmentation; vendor-assessment; qualitative-research |
| source_file | source/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

74-page Aberdeen Group second edition market report on Enterprise Information Integration (EII), the predecessor to SOA/ESB thinking. Author: Wayne Kernochan, Managing VP Platform Infrastructure. EII market sized at under $200 million, projected 80% growth in 2003. IBM leads with $60M EII revenue estimate; BEA $25M; Business Objects $15M. Report introduces Aberdeen EII Technology Segmentation Model covering EAI, database, XML messaging, and EII solution categories. Taxonomy of information aggregation tools: data migration, replication/ETL, data warehouses, operational data stores, EII, federated databases. MetaMatrix featured as case study supplier. SAP OEM deal with MetaMatrix for NetWeaver noted. Related markets: EAI $2.2B→$3.0B, content management $1.2B→$2.0B, portal $1.5B→$2.8B (2002-2004).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Foundational document establishing EII as distinct market category separate from EAI and ETL; introduces Aberdeen EII segmentation model that influenced subsequent SOA-era data integration framing; 2003 predecessor to SOA/ESB era |
| **Relevance** | high | Rich market sizing, vendor revenue estimates, technology taxonomy, and segmentation model; positions EII as precursor to web services and SOA data integration approaches; covers full landscape of 20+ vendors |
| **Prescience** | high | Correctly predicted that IBM and BEA would dominate through acquisitions; web services/XML would become mandatory EII wrapper; application server integration of EII would occur; EII concepts evolved into data virtualization and service mesh data patterns |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (27)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Aberdeen Group | firm | acquired | Harte-Hanks (Sep 2006) -> Halyard Capital (Apr 2015) -> Spiceworks Ziff Davis (Dec 2020) |
| Wayne Kernochan | person | unknown |  |
| MetaMatrix Inc. | company | acquired | Red Hat / JBoss (April 2007) |
| IBM | company | active |  |
| BEA Systems | company | acquired | Oracle Corporation (January 2008) |
| Business Objects | company | acquired | SAP AG (January 2008) |
| Attunity | company | acquired | Qlik Technologies (May 2019) |
| XAware | company | acquired | BEA Systems (2005/2006) |
| Venetica | company | acquired | IBM (August 2004) |
| Nimble Technologies | company | acquired | Actuate Software (July 2003) |
| Enosys Markets | company | acquired | TIBCO Software (circa 2002-2003) |
| Raining Data Corporation | company | acquired | Renamed TigerLogic Corp. (2008), then sold/wound down |
| Ipedo Inc. | company | defunct |  |
| TIBCO Software | company | acquired | Vista Equity Partners (private, December 2014); later merged with TIBCO/Citrix |
| webMethods | company | acquired | Software AG (April 2007) |
| Software AG | company | active |  |
| Progress Software | company | active |  |
| Evolutionary Technologies International (ETI) | company | acquired | Versata (May 2008) |
| SeeBeyond Technology | company | acquired | Sun Microsystems (June 2004) |
| Vitria Technology | company | active |  |
| Oracle | company | active |  |
| Microsoft | company | active |  |
| Sybase | company | acquired | SAP AG (July 2010) |
| SAP | company | active |  |
| PeopleSoft | company | acquired | Oracle Corporation (December 2004) |
| Sun Microsystems | company | acquired | Oracle Corporation (January 2010) |
| Hewlett-Packard | company | active |  |

### Technologies Referenced (15)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Enterprise Information Integration (EII) | data-integration |  | emerging | evolved |
| Extract, Transform, Load (ETL) Tools | data-integration |  | mature | mature |
| Enterprise Application Integration (EAI) | middleware |  | mature | legacy |
| XML Messaging Technologies | standards-infrastructure |  | growth | mature |
| Data Warehouse and Data Marts | data-management |  | mature | mature |
| Enterprise Operational Data Store (ODS) | data-management |  | mature | mature |
| Mid-tier Operational Data Store | data-management |  | emerging | evolved |
| Federated Database | data-management |  | declining | legacy |
| Enterprise Portal | application |  | growth | evolved |
| Web Services (in EII context) | architecture |  | emerging | mature |
| IBM DB2 Information Integrator | data-integration | IBM | emerging | legacy |
| MetaMatrix Information Integration Server | data-integration | MetaMatrix Inc. | emerging | legacy |
| BEA Liquid Data for WebLogic | data-integration | BEA Systems | emerging | legacy |
| Content Management Software | enterprise-applications |  | growth | mature |
| Enterprise JavaBeans (EJB) / Java Platform | development-platform | Sun Microsystems | growth | evolved |

### Observation Summary

- Total observations: 45
- By type: technical-claim: 19, market-share: 6, competitive-analysis: 6, prediction: 5, market-size: 4, adoption: 3, strategic-recommendation: 2
