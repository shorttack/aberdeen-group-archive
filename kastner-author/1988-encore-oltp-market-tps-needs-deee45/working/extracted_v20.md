Manufacturing and Distribution Applications 

Shop Floor Control - controls, manages, and accounts for work-in-process in discrete manufacturing.  Frequently involves communications with factory machine networks. Application is usually distributed across real-time control machines, data collection minicomputers, and factory mainframes or minicomputers.  Major competitors are IBM, Digital, and Hewlett-Packard.  Volumes range to 40 TPS peaks. 

Manufacturing Resource Planning (MRP) - maintains a database of discrete manufacturing assemblies and parts lists.  Bill of material explosions and economic order point calculations are quite CPU intensive.  This is primarily a batch application traditionally run on mainframe computers or superminis. 

Distribution - warehouse control applications are increasingly sophisticated, involving machine-controlled automated warehousing, picking, and movement by guided vehicles.  Volumes to 10 TPS. 

Order entry - most large-scale order entry systems are custom-tailored to a specific company's requirements.  Extensive database manipulation, rule-checking, and CPUintensive editing is common.  Volumes vary tremendously.  Home Shopping Services and mail order firms generate volumes up to 100 TPS. 

Computer-Assisted Design (CAD) - CAD applications assist engineers in the design, drafting, and engineering record-keeping process.  CAD requires heavy computing for solids modelling (3D drawings), wire frame generation, stress analysis and other scientific calculations related to manufacturability.  Efforts to integrate CAD with computer-assisted manufacturing (CAM), the OLTP-side of CAD/CAM, have been sparse.  The key to CAD sales is applications software from a wide range of ISVs. 

## Banking Applications (Retail) 

On-line banking - integrates demand deposit accounting (checking), deposit instruments, installment and mortgage loans, and customer relationship data. Application software is a prerequisite in this market.  In the U.S., commercial banks have not implemented on-line banking and are unlikely to in the next five years. There is no pressing market demand to do so.  U.S. savings and loans have traditionally been on-line at the teller level and have implemented automated teller machines for off-premise services.  There are 25 large S&L's requiring more than 50 TPS for their systems.  However, the problems of S&L's are widely known. 

Internationally, banks in Europe and Japan are more centralized an on-line than their U.S. commercial counterparts.  Very large mainframes are the norm, requiring up to 125 TPS.  In Europe, the 1992 economic changes will probably loosen the national computer vendor strangle-hold on large bank computer systems, creating an opportunity. 

Relationship accounting - customer information systems aggregate data from individual bank applications into a relationship repository.  The intent is to allow personnel to view all of a customer's activities at the bank.  While widely desired, these systems have only been installed at the largest banks -- or else the functionality is rudimentary.  The decision support characteristics of a relational database are ideal for this application, but RDBMS performance has been so poor (until recently) that these systems could not be price/performance justified.  While application performance requirements in TPS are modest, the processing necessary to manage complex decision support queries in real-time is high. 

Automated teller machines - local banks require up to 15 TPS.  Nationwide ATM networks like CIRRUS require 25 TPS or less.  This market is maturing.  Volume requirements are higher, to 60 TPS, in Europe due to the widespread use of debit cards for electronic funds transfer (EFT). 

Credit and debit card - are listed under Retail. 

Banking Applications (Wholesale) 

International funds transfer - large money-center banks generate 10K-15K transactions per day (less than 1 TPS) in this high-profile application.  Security and availability are key requirements. 

Cash management - allows corporate cash managers the ability to move monies around the globe.  Timing is critical, volumes are a modest 20 TPS in large systems, and information retrieval and presentation is a critical factor in these applications. 

Foreign exchange - purchase and sale of foreign currencies.  Up to 40K transactions per day (1 TPS). 

Interbank clearing systems - time-critical bank-to-bank item transfer of checks, drafts, and notes among members.  Volumes to 200 TPS peak.  Examples include CHIPS (the NY clearing house) and FedWire, which handles Federal Reserve Bank transactions.  While this applications appears very attractive, there are only a handful of clearing house systems in place -- it is not an attractive market. 

## Brokerage/Securities Applications 

Retail trading - multiple computers manage the flow of information from the broker's desktop through wire rooms to the exchange floor and back.  Volumes are substantially governed by the retail broker's ability to enter transactions;  75 TPS is a peak load at a large brokerage firm. 

Mutual funds - shareholder systems and securities accounting system volumes are up to 100 TPS.  The stock ticker plant application (usually on a fault-tolerant computer) maintains real-time database and position information for the institution's wholesale 

business.  At the start-of-day, opening quotes drive volume to 150 TPS.  These transactions require minimal database activity. 

Program trading - about 400 firms engage in program trading.  A typical program involves watching a basket of the Standard and Poor's 500 stocks and making continual mathematic calculations against the underlying options.  This application requires the ability to maintain the security "basket" database, run the linear equations necessary to make the buy/sell determination, and execute the trade through an automated interface to the trading floor.  This can involve the quick purchase or sale of 500 stocks;  each stock is an individual transaction.  Because program traders are competing with other large institutions, speed and accuracy become competitive advantages. 

Commodity trading - foreign currency, bond, and commodity trading involves international markets with intense competition.  Individual institutional traders use rapidly changing spreads between markets to make minuscule profits (or losses) on large volumes of transactions.  Computers are increasingly used to manage multiple market databases, determine profitable spreads, and signal traders to initiate the transaction.  Volumes range to 75 TPS. 

Information providers - Reuters, Telerate and other securities information providers deliver securities market information over proprietary networks to customers.  The systems require numerous (over 50) information input sources and the capacity to communicate 1-2M bytes per second over up to 2,000 communications lines. 

## Government Applications 

Federal Aviation Administration (FAA) - current programs to upgrade flight plan records, national radar weather databases, air traffic controller consoles.  Typical applications have a profile of high computation and/or large database. 

Census Bureau - preliminary plans are to distribute data to regional site where an RDBMS will allow decision support on the 1990 census data.  Large databases with the potential for high computation requirements. 

Social Security - antiquated system requires replacement with a modern, OLTP-based system.  Aggregate transaction volumes estimated at 100 TPS over 10,000 terminals. 

Command and Control - The military is increasingly interested in commercial off-theshelf (COTS) OLTP hardware for logistics, intelligence analysis (text retrieval and database), and decision systems.  Unix is highly desirable. 

Retail Applications 

Point of Sale (POS) - a scanner data capture application requires 10 TPS per store or less.  Usually, individual store data is aggregated by an in-store computer and 

forwarded in batch to regional or corporate data centers.  Market innovators are now doing regional warehouse inventory control and restock ordering based on near-realtime feeds from individual stores.  These volumes are less than 50 TPS. 

Credit Authorization - positive authorization requires retrieval and updating of the customer's record and insertion of a hold record.  Volumes range to 200 TPS for VISA and MasterCard systems.  Negative authorization systems look up hot cards and reject on a match.  American Express uses a negative authorization system with each regional node processing 150 TPS at Christmas peak on $100K midrange systems. 

Inventory control - see Manufacturing. 

Product Management - decision support application based on scanner or sales data from individual stores.  Used by buyers and product planners to track promotions, advertising, shelf-life, etc.  Very large (10GB and up) databases require considerable processing power to deliver rapid query responses. 

Transportation Applications 

Airlines Reservations Systems - American's Sabre system processes 200 TPS per IBM 3090-200.  Volumes peak at 2,000 TPS and are growing at 15% per annum. without the effect of the merger with Delta airlines. 

Other reservations systems - travel brokers, holiday package brokers, steamship lines, hotels, automobile and other reservations systems are high volume systems requiring connectivity to large numbers of terminals.  Volumes range from 75 to 150 TPS on the largest systems. 

Rate setting - the airline industry averages 10,000 fare/route/schedule changes a day. This information is used by the transportation industry as a whole and within the airlines for competitive analysis (match a competitor's fare change), route profitability analysis and other decision support applications.  Trucking and shipping rate setting, in today's deregulated environment, is a database-intensive application. 

Routing - the computation-intensive algorithms of least-cost distribution routing suggest that this application deserves modest attention. 

Insurance Applications 

Claims Processing systems - these custom-tailored applications at large insurance companies generate volumes to 60 TPS.  None have been implemented with an RDBMS to our knowledge. 

Agent Support - agent/broker online support for customer records, policy information, price quotes, etc.  Volumes to 40 TPS against many databases. 

Risk Management - online ad hoc management of claims data to adjust risks to rates. Large databases with decision support query volumes. 

Policy Systems - inquiry, billing, payments and renewals with online access by local or remote agents.  Volumes to 35 TPS. 

Actuarial - this computation-intensive application has traditionally been done on large mainframes in batch or background.  An opportunity exists for on-line actuarial decision support. 

Imaging - we believe the insurance industry will increasingly embrace digital imaging and the use of object-oriented databases.  The on-line storage and retrieval capacities of these systems at the major insurance companies are conjectural but have the potential to be very large. 

## Service Applications 

Information retrieval - information-for-a-fee services have matured rapidly in the 1980s, and competition is driving the search for new or improved information delivery vehicles.  In order to speed full-text retrieval services, Dow Jones installed a massively-parallel Thinking Machine.  Large service providers like Dow Jones, Mead Data, OAG, MCI Mail and Compuserve require up to 150 TPS from 10,000 on-line users. 

Ticketing - like transportation market reservations systems, ticketing requires online access to event databases and site seating databases by thousands of terminals. Volumes range to 55 TPS. 

Home services - home shopping requires timely order processing with volumes to 100 TPS.  Home banking has not been commercially successful yet, but systems installed to date have required up to 25 TPS.  Sears/IBM Prodigy expects 100 TPS within three years with its videotext application.  The French electronic mail system generates over 300 TPS during peak hours. 

## Communications applications 

Call switching - operator-assisted 800 number call switching systems generate 400 TPS today with the expectation of growth to 600 TPS in five years.  Low processing and data access requirements per transaction.  Very high availability requirements. 

Alarm systems - high connectivity (to over 2,000 asynchronous 300 baud lines) with low computation. 

Value-added switching - Telenet, Tymnet, GEISCO, or Canada's iNet connect information providers and their customers.  Services include protocol/speed conversions, concentration, and accounting.  Accounting transactions to 70 TPS. 

Service order processing - RBOCS average 10,000 customer service orders a day (5 TPS) against massive databases which are also used to produce white page telephone books. 

Maintenance orders - network preventive maintenance and remedial maintenance systems generate 10 TPS, use large databases, and require extensive communications capabilities. 

Miscellaneous Applications 

Hospital management - integrated hospital systems generate 25-30 TPS. 

Utility customer service - like any customer service application, telephone inquiry operators must be able to access and update customer records.  Volumes to 25 TPS. Conclusions for Encore Computer 

The market for high-end OLTP applications exceeded $1.4 billion in 1989 for systems with application requirements exceeding 25 TPS, and was $630M at 100 TPS throughput rates.  Every vertical market has a need for the kind of computing the Series 90 will provide.  We rate, in priority order, the Communications, Government, Financial (banking, brokerage, insurance) and Retail vertical markets as most attractive for a commercial Series 90. 

The commercial Series 90 has significant projected price/performance advantages over IBM's 3090 mainframes -- the machine of choice for high-end OLTP.  Aberdeen believes that most data centers can achieve 40 TPS using CICS and DB2 on a 3090-180J with an $8 million five-year life-cycle cost for hardware, software, and maintenance.  Therefore, the commercial Series 90 could well address wider database/data communications commercial applications markets than just high-end OLTP by showing outstanding price/performance measured in multiples of IBM mainframes. 

In general, we believe the most attractive application profile for the commercial Series 90 is one where hundreds or thousands of applications-workers, such as customer service representatives, must have real-time access to enterprise administrative and accounting records.  Traditionally, this has been the province of mainframes.  Unless the commercial Series 90 has outstanding availability features, it will be more difficult to market high-end computer-to-computer OLTP than people-to-computer OLTP. 

Based on the above analysis, Aberdeen rates the following ten 1990 market/ application areas for applications requiring 100 TPS or greater, in priority order, as most attractive for a 1991 Series 90 product. 

The total market potential for these ten market/applications in 1990 is estimated at $630M in 1990.  These ratings are based on a combination of factors, including: 

demonstrable requirements for high-end commercial processing;  market barriers to entry;  entrenched competition;  financial attractiveness;  time to market for new applications;  market innovation or risk aversion tendencies. 

1. Communications:  service order processing, maintenance processing.  Same profile as Utility customer service.  Total market for high-end OLTP in this application area is estimated at $40M.  Encore, while not well-established in the Communications industry, has extensive experience in high-end Unix systems. 

2. Retail:  credit authorization.  Total market for high-end OLTP in this application area is estimated at $35M. 

3. Government:  non-specific applications.  The combination of UNIX, excellent price/performance, and high-end processing are well-suited for both administrative and national security applications.  Total market for high-end OLTP in this application area is estimated at $200M. 

4. Transportation:  reservations systems.  While the core airlines reservations systems are locked-in to IBM, other transportation reservations systems are attractive.  In addition, airlines are increasingly installing front-end adjunct machines to offload the core reservations systems.  Total market for high-end OLTP in this application area is estimated at $45M. 

5. Brokerage:  mutual fund shareholder customer service.  Total market for high-end OLTP in this application area is estimated at $35M. 

6. Manufacturing/Distribution:  order entry and inventory control. Total market for high-end OLTP in this application area is estimated at $50M. 

7. Banking:  cash management and international funds transfer. The money center (top 200) banks are looking at a new generation of wholesale banking systems.  Total market for high-end OLTP in this application area is estimated at $55M. 

8. Banking:  retail banking systems.  The market in Europe for new retail banking systems is hot, while continuing competitive pressures in the U.S. is fueling demand for new, market-driven systems.  Total market for high-end OLTP in this application area is estimated at $65M. 

9. Brokerage:  trading systems.  While U.S. and European demand is currently soft, the inexorable trend towards world-wide, 24-hour-a-day trading will continue.  Total market for high-end OLTP in this application area is estimated at $60M. 

10. Manufacturing:  shop floor control.  Total market for high-end OLTP in this application is estimated at $45M. 

