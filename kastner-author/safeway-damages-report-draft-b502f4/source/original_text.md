Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 1 
Page 1 
 
Safeway Damages Report 
 
 
Aberdeen Group Backgrounder 
 
 
 
Evidence and Sources of Information 
 
 
 
 
 
Purpose and Methodology 
 
Aberdeen Group has been asked to provide its expert opinion regarding the impact of the 
February 6, 2002 fire suppression system discharge at the Consonus data center with 
respect to Safeway, Inc.’s 40-node Teradata system.  Specifically, Aberdeen has been 
asked for its opinion with respect to the damage amount sustained by the 40-node 
Teradata system; the resulting impact on Safeway’s business operations; and the options 
available for Safeway to restore comparable levels of processing power, reliability, 
availability, and data analytics delivery to end-users throughout the organization. 
 
In developing its opinion, Aberdeen combined its experience in following information 
technology (IT) markets, products and implementations with primary field research.  
Aberdeen’s field research for this assignment included interviews with Safeway 
individuals who designed, implemented, maintained and used the Teradata-based 
applications, as well as those individuals responsible for data center operations.  
Aberdeen also interviewed several other Teradata users from organizations other than 
Safeway, as well as representatives from NCR Corporation (the parent of the Teradata 
Division), and individuals involved in the market for used/refurbished computer 
hardware equipment and components.  Finally, Aberdeen conducted Web-based research 
with respect to Teradata products, services and customers; the Teradata resale market; 
and Safeway and its competitors. 
 
Executive Summary 
 
Based on my experience and the research conducted for this assignment, key findings are: 
 
• 
Safeway had extensive experience in developing complex data analytics 
applications and running data warehouse systems.  The company’s initial 
efforts in this area dated back to 1996 with an Informix database running on Sun 
Solaris hardware platforms.  The data model was originally built by ICL/Fujitsu.  
This effort coincided with, and was intended to leverage, Safeway’s Loyalty Card 
program.  However, the Informix/Sun solution was limited to storing only 2-3 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 2 
Page 2 
terabytes of data and supporting only six concurrent users.  Moreover, 
processing/query speed was inadequate and did not capture all store transactions.  
By 1999, Safeway had outgrown this system and needed a new solution.  Safeway 
choose a hardware/software solution from NCR/Teradata. 
 
• 
By February 2002, Safeway’s Teradata system could be classified as a 
mission-critical Operational Data Store (ODS).  An ODS is a data warehouse 
system in which data is continually added throughout the day so that real-time 
business decisions can be made based on queries against the data.  Safeway had 
evolved from the batch-oriented queries and nightly updates typically associated 
with more traditional data warehouses to a more real-time-oriented system.  The 
deployment of Safeway’s Trickle application meant that the same query returned 
different results as the day progressed.  The ODS approach allowed Safeway to 
have a near real-time view of its business and enabled operational decisions to be 
made on the data.  The mission-criticality of this data is shown by the fact that 
senior executives, including the CEO, demanded access to Trickle-oriented data 
repeatedly throughout the business day, and that Trickle data is sent to the pagers 
of key executives.  Moreover, core business processes fundamental to the 
operations and profitability of the company depended on the availability, 
reliability and performance of the 40-node Teradata system. 
 
• 
Safeway was prudent in selecting Teradata hardware and software as the 
new platform for its data analytics initiatives.  Safeway chose the Teradata 
platform due to its unique architecture that was specifically designed for complex, 
ad hoc queries in a data warehouse or operational data store environment.  
Additionally, Safeway was attracted to Teradata’s modularity, which enabled 
additional storage and processing power to be added over time by increasing the 
number of nodes deployed.  This allowed Safeway to have a data 
warehouse/operational data store that could grow to meet changing business 
requirements. 
 
• 
The Teradata solution was unique, specifically assembled to meet Safeway’s 
requirements.  Teradata systems are multi-million dollar hardware/systems 
software deployments that are sized and configured to meet each customer’s 
requirements.  Unlike PCs and mass-production servers, pre-built Teradata 
systems are not kept in NCR inventory, but rather are built to order once a 
customer makes a purchasing decision.  This, combined with the relatively large 
size of Safeway’s system, made it extremely unlikely that a comparable system 
could be found on the used equipment market from any organization other than 
NCR/Teradata. 
 
• 
Teradata has a unique hardware/software architecture.  Software and 
hardware engineers at NCR/Teradata have developed a system specifically 
designed to handle large, complex queries against massive data sets.  Hardware 
and software advances and design decisions — specific to NCR — mean that the 
company is the sole source of Teradata-compatible hardware and systems 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 3 
Page 3 
software (OS and database).  The company enjoys monopolistic pricing as a 
result. 
 
• 
Teradata is used extensively in the retail vertical.  Teradata claims that its 
solutions drive over 55% of the revenue generated by the top 30 global retailers 
and over 70% of the revenue generated by the top 15 U.S. general merchandisers.  
Several of these customers are direct Safeway competitors, including Albertson’s 
and Wal-Mart.  The capabilities offered by a Teradata-based solution are a key 
element in competing effectively in the retail/grocery market. 
 
• 
New Teradata systems require extensive lead times for delivery.  Because 
there is no inventory, customers cannot expect immediate delivery of new 
systems.  This is particularly true for larger systems, such as Safeway’s.  As a 
result, delivery of a new system several months after a customer places an order is 
not uncommon. 
 
• 
Safeway’s Teradata system grew in an evolutionary fashion.  Safeway’s 
actions clearly show that it continued to deploy additional processing power and 
storage, as well as new applications, to its Teradata implementation.  As a result, 
the system grew from an original 28 nodes in January of 2000 to 40 nodes by 
February of 2002.  Thus, the 40-node 5250-class system in place at the time of the 
February 6, 2002 incident can be viewed as a foundation upon which Safeway 
planned to deploy additional nodes and applications.  This continued evolution of 
incremental system upgrades is confirmed by both the new applications that 
Safeway has deployed since February 2002 as well as by the fact that Safeway 
purchased an additional twelve 5300-class nodes (above and beyond the 
comparable 48-node 5300-class system) in the second half of 2002.   
 
• 
The Teradata system was used for real-time executive decision making at 
Safeway.  Senior executives demanded regular updates from the Teradata system 
on business performance throughout the day.  This allowed them to have year-
over-year sales comparisons and gauge business performance — critical 
performance indicators necessary to effectively buy and profitably merchandise 
groceries and other products. 
 
• 
The Teradata system was used to run core business processes at Safeway.  
Activities in this category included vendor allowances, e-commerce 
(Groceryworks/Safeway.com), sweepstakes, and the customer service call center.  
When the Teradata system was not available, many of these business processes 
simply could not be performed. 
 
 
• 
The Teradata solution offers unique advantages that Safeway wanted to use 
to its advantage.  Teradata has designed its solution to be an analytical 
engine/data warehouse database.  Specifically, Teradata has optimized its 
solutions for fast queries/complex queries using such techniques as parallel 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 4 
Page 4 
processing.  This is in contrast to other database solutions, such as Oracle or 
IBM’s DB2, which are more oriented towards the fast updates required for 
operational transaction-oriented systems.  Thus, Teradata optimized to reduce 
processing times for the complex queries of the kind generated by Safeway’s 
applications.  Replacing Teradata with another technology would result in making 
performance compromises.  It should be noted that Safeway has other significant 
IT investments, including an IBM mainframe, yet still chose Teradata for its 
complex data analytics requirements.  Finally, the Teradata system is designed for 
very high levels of availability.  That is, the Teradata system can sustain a failure 
to any single hardware or software element and still continue operating.  That 
meant Safeway could design business processes which expected the Teradata 
system to be responsive all the time — the cliché is 24 x 7.  However, there are no 
commercially available machines in the world which could sustain the damage 
incurred during the February 6, 2002 incident and keep operating.  To avoid such 
a business disruption which would cripple Safeway’s business processes, Safeway 
contracted with Consonus for a state-of-the-industry fault-resilient datacenter. 
 
• 
The Teradata system was used to optimize business processes at Safeway.  
Data from the system was used to finely tune business activities, including fuel 
pricing, promotional mailings and marketing campaigns.  Ensuring maximum 
effectiveness from these activities is crucial in an industry with 1-2% profits. 
• 
Time lost is lost forever.   
Like an airline, any grocery chain must operate at peak efficiency during its store-
open hours.  The failure of critical computer systems during the hours when stores 
are open cannot be recovered later.  Whatever potential operational or customer 
satisfaction decisions that could have been made on the spot cannot be easily 
made later.  Therefore, Safeway needed and expected its Teradata system to be 
available during business hours. 
 
• 
The incident of February 6, 2002 had the following implications for Safeway. 
a. An immediate downtime of over 97+ hours or six days (2/6/02 through 
2/11/02), during which those business processes which relied on Teradata-
based information could not be performed. 
b. Repeated, unanticipated downtime for a period of several months, which 
interrupted business processes repeatedly and unexpectedly. 
c. Frequent degradation of performance for the Teradata system.  Combined 
with unexpected outright outages, this quickly resulted in a loss of 
confidence among senior executives as to the validity of information being 
delivered by the Teradata system, and operational managers were 
distracted by the frequent need to employ stopgap processes to alleviate 
the lack of the Teradata-based applications. 
d. The diversion of internal IT resources away from developing new 
applications that provided Safeway with a competitive edge, to performing 
triage on the numerous outages and performance problems now troubling 
the Teradata system. 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 5 
Page 5 
e. A loss of confidence in the reliability of the Teradata hardware on the part 
of Safeway management and line employees. 
f. A termination of the hardware services contract with respect to the 40-
node Teradata system by NCR, leaving Safeway with no good alternatives 
for maintaining a complex asset. 
As a result of the preceding two factors, the 40-node system could no longer serve 
as a reliable foundation upon which to add additional hardware/processing 
resources or to deploy new applications.  Thus, Safeway’s business objective to 
have an expandable, evolutionary operational data store system was destroyed.  A 
key part of the business value the Teradata system and Safeway’s investment in 
specialized IT staff was eliminated.  Moreover, with its growth path for its 
Teradata system removed, Safeway could no longer stay ahead, or even keep 
pace, with its highly competitive rivals. 
 
• 
Safeway’s Teradata implementation consisted of three primary components: 
Hardware, Software, and Professional Services.  Like nearly any enterprise-
class, mission-critical IT solution, all three of these elements must be in place for 
Safeway to derive business value from its Teradata investment.  The hardware 
component consists of the physical equipment located in the Consonus data center 
– disk drives, processors, tape storage, power supplies, etc.  The software has two 
major sub-components – systems software such as the operating system and 
database, and the custom-build applications used by Safeway to run its business.  
Professional services are based on the highly-skilled personnel, both internal to 
Safeway as well as external (most notably NCR’s services group) that are 
responsible for the ongoing operation, maintenance, spare parts and repair of the 
system.  The hardware component was damaged on February 6, 2002 as a result 
of the incident at the Consonus data center.  Safeway lost a second component, its 
maintenance contract with NCR and associated professional services and spare 
parts, on April 10, 2002, also as a result of the February 6th incident.  Interviews 
with Teradata customers reveal that the professional services/maintenance 
capabilities offered by NCR are a critical component of their overall Teradata 
solution. 
 
• 
After the February 6th incident, Safeway faced four options if it was to again 
have a system with the same reliability, availability, scalability and power as 
the 40-node Teradata system.  The first option was to immediately order a new 
replacement system and put no recovery efforts into the existing damaged system.  
However, due to the long lead times involved with the delivery of new Teradata 
systems, this would have involved using a heavily damaged system for a 
timeframe that would likely last several months.  It is questionable as to whether 
the 40-node system could have functioned at all without some recovery efforts 
and spare part replacement.  In my opinion, this option carries an unacceptable 
risk to Safeway’s business and data.  Should the system be entirely unavailable 
for a period of months, the business interruption costs would have been much 
greater that those actually documented in my report. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 6 
Page 6 
The second option was to replace every single part of the 40-node system on a 
piece-by-piece basis.  This course is impractical from a cost perspective.  Just as 
crafting an automobile entirely out of new spare parts is much more expensive 
than purchasing a new model off the lot, so too would be assembling a 40-node 
system out of new individual power supplies, processors and disk drives.  
Moreover, a search I made through Web sites for several of the largest brokers of 
used computer equipment and components reveal practically no Teradata 
equipment for sale.  Also, the downtime required to implement this option would 
be extensive, further impacting ongoing Safeway operations. 
 
The third option was for Safeway to migrate its highly-custom applications over 
to a new database/hardware platform (such as Oracle or DB2 running on a Unix 
machine) or move to a system that consisted of the Teradata database running on 
top of the Microsoft Windows operating system.  Moving to a new database 
would have required extensive rewriting for many of Safeway’s custom 
applications, adding additional cost and time delays measured in months or 
perhaps years.  Moving to the Teradata database on top of Windows would have 
added a high level of risk.  Interviews with Teradata executives indicate that had 
Safeway selected this path in mid-2002, it would have resulted in the largest 
Teradata/Windows implementation in the world – much larger than what Teradata 
typically recommends.  In my experience, that would be too high a risk to take. 
 
The final option was to replace the damaged 40-node system with a new Teradata 
hardware platform of comparable size and performance.  In my opinion, this was 
the logical, most cost-effective choice for allowing Safeway to continue operating 
and evolving its mission-critical applications.  This option gives Safeway a 
proven, reliable and scalable hardware platform that can support its existing 
application portfolio.  It reduces risk associated with migrating to new technology 
platforms that are unproven at the size required by Safeway.  And it does not 
require the existing application portfolio to be modified to support a new 
database.  The ability to use the existing application portfolio is critical – Safeway 
had been developing applications for the Teradata platform since the summer of 
2000.  Lastly, it preserves the key-partner relationship between Safeway and NCR 
that was strained by the service, support, and costs associated with the incident. 
 
• 
It is highly unlikely that Safeway could have purchased a used 40-node 5250-
class machine.  This is for three reasons.  The first is that the number of installed 
Teradata systems in the market is low – approximately 700, with about 100 new 
systems manufactured and sold by NCR every year.  It is a very thinly-traded 
market with a handful of machines available at any one time.  The second factor is 
the fact that Safeway’s 40-node system is considered a relatively large 
deployment further reduces the likelihood that a comparable system could be 
obtained in an acceptable timeframe.   
 
Third, it is important to understand that the market for used Teradata equipment 
from third parties is for the hardware only.  The operating system and database 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 7 
Page 7 
licenses, without which the hardware is useless, must still be obtained from a 
single source – NCR.  Software purchased independently of hardware is 
monopolistically expensive. 
 
• 
The damaged 40-node system has little to no value on the used market.  
Interviews I had with dealers of used computer equipment revealed that used 
Teradata hardware typically sells for 5-10% of original purchase price in 
undamaged condition.  One factor in this discount is that the 5200 series is 
currently one generation (and soon to be two generations) behind Teradata’s latest 
models.  Additionally, since Teradata still controls the operating system and 
database licenses, a buyer of new hardware must still go to NCR to get the 
software needed to run the system.  When asked about the potential value of a 
system that had been subjected to the conditions of the February 6th incident, 
individuals interviewed were suspect as to whether any buyer could be found.  
Thus, the residual value of this damaged electronic equipment is negligible, 
approaching scrap. 
 
• 
Safeway could not resell the damaged system, in whole or in parts.  Based on 
my investigations, damaged Teradata hardware has nothing more than scrap 
value.  Should Safeway (or any entity) wish to get more than this scrap value, the 
hardware would have to be represented as undamaged.  However, based on the 
history of the 40-node system, such a representation could be construed as a 
fraudulent misrepresentation of the Teradata system, subjecting Safeway to a 
legal risk which vastly outweighs the value of the system. 
 
• 
Safeway acted prudently in opting to purchase a new Teradata system.  The 
Teradata system was integral to several core business processes that enabled 
Safeway to compete in the highly-competitive grocery/retail market.  Safeway 
was put at a competitive disadvantage due to a damaged Teradata system.  For 
example, the Teradata system had a direct impact on Safeway’s cash flow, 
through the Business Tracker/Allowances application.  A reduction in cash flow 
would have put a significant financial squeeze on the company.  Safeway’s 
decision minimized replacement time, reduced risk and allowed the company to 
continue to have a growth path for its data analytics efforts. 
 
Teradata’s Market Position  
 
A division of NCR, Teradata is a highly-regarded technology supplier in the data 
analytics market – both for its hardware solutions and its database technology.  More 
specifically, the company has a very strong position in the retail/grocery space.  Teradata 
claims that its solutions drive over 55% of the revenue generated by the top 30 global 
retailers and over 70% of the revenue generated by the top 15 U.S. general 
merchandisers.  Teradata customers include Albertson’s, Wal-Mart, Tesco, Sainsbury’s, 
JC Penny, Kmart, Lowe’s, and Office Depot. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 8 
Page 8 
For the year ended December 31, 2002, the Teradata division generated $1.226 billion in 
revenues.  Teradata sells approximately 100 new systems each year and has an installed 
base of approximately 700 systems. 
 
Teradata has positioned itself in the high-end business intelligence/business analytics 
market.  The company provides a sophisticated, modular, expandable hardware platform; 
database software optimized for the complex queries generated by business analytics 
applications; and related professional services.  As a company, it is unique in its market 
position. 
 
The Teradata database was designed from inception to be an analytic/data warehouse 
solution, compared to other competitors, such as IBM and Oracle, which have architected 
their databases for an operational/transaction-oriented application portfolio.  To this end, 
Teradata uses several techniques, such as parallel processing, the use of “quiet” time to 
do processing sooner rather than later, and efficient allocation of resources.  These 
techniques can dramatically increase performance.  Teradata has cited an example where 
a SAS benchmark took 1,200 minutes on another database, 200 minutes when run or 
Teradata, and 15 seconds when converted to a Teradata-specific implementation of the 
Structured Query Language.  Additionally, Teradata has designed its system to reduce the 
number of database administrators required.  Numerous customers cite this reduced labor 
cost as a significant benefit. 
 
 
Safeway’s Business Case for Implementing a Teradata-based System 
 
During research interviews I conducted, Safeway executives familiar with the Teradata 
system stated that the 40-node system was selected in 2000 as a replacement for the 
existing data analytics solution, which used a data model built by ICL/Fujitsu on an 
Informix database running on Sun servers.  The Informix/Sun system was deployed to 
enable Safeway to run loyalty marketing programs that targeted its Club Card customers.  
The data from Club Card customers is highly valuable to Safeway, since over 90% of all 
transactions involve a Club Card.  Although helpful, the Informix/Sun system was 
limited.  Safeway executives cited the following reasons for moving from Informix/Sin to 
Teradata: 
 
• 
At the time, Safeway had 2-3 terabytes of data, which was at the upper end of 
what the system was designed to handle.  Safeway planned to grow its data 
warehouse and wanted a system designed to handle larger amounts of data. 
• 
Only six concurrent users could be supported.  No one outside of the IT group 
could directly access the system.  Safeway wanted to deploy new and existing 
data analytics applications to a wider audience, such as service representatives in 
the call center, but was constrained by the Informix/Sun system. 
• 
Safeway wanted better performance and throughput.  The Informix/Sun system 
took days for some complex queries and experienced frequent downtime. 
• 
Sales transaction and customer data was extracted from the mainframe in batch 
mode on a nightly basis.  Safeway wanted to move to more frequent updates.  

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 9 
Page 9 
This could be accomplished by deploying a Teradata system and changing the 
way data was fed to the system by using the “Trickle” application to supply 
incoming store point-of-sale data during the workday. 
• 
Safeway wanted a better data model and data cleansing capabilities than it had 
with the Informix/Sun system. 
• 
Safeway wanted data from all transactions from all stores captured.  The 
Informix/Sun system only captured approximately 95% of all transactions.  With 
all transactions captured, the system could provide accounting-quality operational 
information. 
 
Safeway wanted a solution that would provide much wider access to sales data in real-
time or near-real-time fashion.  As stated by Safeway individuals interviewed, the belief 
of senior management was that effectively executed loyalty marketing programs would 
give the company the opportunity to increase sales 1-2%, which equals approximately 
$350 million to $700 million based on Safeway’s 2002 results. 
 
Description of Safeway’s Teradata Implementation and Associated Applications 
 
Safeway’s activities with data analytics to support its loyalty marketing efforts began in 
1996 with the purchase of an Informix database running on Sun Microsystems hardware.  
The data model was written by ICL/Fujitsu.  Data was extracted from the mainframe-
based transactional system on a nightly, batch basis.  The majority of applications 
deployed on this system provided historical snapshots of past activities. 
 
By late 1999/early 2000, Safeway had determined to look for a replacement system.  This 
decision was based on the limitations of the Informix/Sun system cited earlier, as well as 
capture, model, analyze and display data in a more real-time fashion so that it could be 
acted upon in time to effect Safeway’s operations. 
 
Safeway eventually selected a 28-node Teradata system as a replacement.  A chronology 
of the evolution of this system from early-2000 to February 2002, including both 
hardware upgrades and individual application deployments, follows. 
 
Hardware 
• 
January 28, 2000 – Purchase of original 28-node 5200-class Teradata system, 
with operating system and database licenses for $10,227,814.54 
 
• 
April 27, 2000 – Purchase of NCR maintenance contract for 28-node Teradata 
system. 
 
• 
July 11, 2001 – Purchase of 6-node add-on for $2,548,834.76 
 
• 
September 1, 2001 – Purchase of maintenance contract for additional 6 nodes. 
 
• 
October 4, 2001 – Purchase of 4-node add-on and upgrade of entire system to 
5250-class for $3,945,432.21 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 10 
Page 10 
 
• 
January 1, 2002 – Purchase of maintenance contract for 4 nodes for $516,000.00. 
 
Application Software 
 
Below is a list of the applications deployed on Safeway’s Teradata system at the time of 
the February 6th incident.  I have placed each application in one of three categories.  Class 
1 applications are static reporting solutions with infrequent data refreshment and access 
(anywhere from weekly to quarterly).  Class 2 Applications utilize data that is refreshed 
on a daily basis and are accessed by end-users at least once per day, and typically more 
frequent.  Class 3 Applications are of an operational data store nature.  Data is refreshed 
constantly throughout the day and end-users access the application continuously 
throughout the day. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 11 
Page 11 
 
 
Incident of February 6, 2002 and its Impact 
 
The incident of February 6th 2002 caused significant interruptions to Safeway’s business 
processes and its data center/IT operations.  Following is a chronology of the key events 
associated with the data center incident: 
 
Timeline of Events – Need to compile – wait for Safeway depositions 
 
• 
February 6, 2002 – Fire suppression disaster at Consonus Salt Lake City facility.  
40-node Teradata system is shut down.  System is unavailable to Safeway line 
users for 97 hours. 
Application
Date of Deployment
Category
Escrip
Sep-99
1
Business Tracker 
(Allowances)
Nov-99
2
United Airlines
Dec-99
1
Dreyer's Extract
Jan-00
2
Customer Care Extract 
(quarterly)
Mar-00
1
Alaska Airlines
Mar-00
1
Fuel
Apr-01
3
Call Center
Jun-01
3
American Airlines
Jul-00
1
Continental Airlines
Jul-00
1
CDRT (Customer Data 
Retention Technique)
Jul-00
2
Fraud/Shrink
Jul-00
1
Real-time Promotion 
Mananagement
Jul-00
2
CRM Segment & 
Target
Jul-00
3
Trickle (Data Feeds)
Oct-00
3
Dashboards for 
Executives
Nov-00
3
Sweeps
Dec-00
2
Distribution Voids
Jan-01
1
Out-of-stock Alerts
Apr-01
3
Lawyer Milk
Sep-01
1
SMS
Oct-01
3
Grocery 
Works/Safeway.com
Oct-01
3
Checker Scan 
Frequency/Checker 
Productivity Extract
Oct-01
1
Markdowns to NASC 
Extract
Jan-02
1

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 12 
Page 12 
• 
February 6 to February 11, 2002 – Extensive disaster recovery efforts by 
Consonus, Safeway, NCR and other third-party personnel.   
• 
February 11, 2002 – Teradata 40-node system is brought back on line. 
• 
February 11, 2002 to December 31, 2002 – Teradata 40-node system operates in a 
reduced capacity, experiencing over 47 total hours of unscheduled downtime and 
over 111 total hours of degraded performance. 
• 
April 10, 2002 – Letter from NCR’s Alan Chow to Stu Rhea at Safeway 
providing NCR’s assessment of the February 6th incident, citing concern for long-
term reliability and availability of system, and stating that associated repairs are 
“out of scope” with current maintenance contract.  Letter also urges replacement 
of current system with a new one. 
 
Impact to Safeway 
 
As a result of the data center incident, Safeway’s operations were impacted in the 
following ways. 
 
• 
Applications were unavailable – The Teradata system experienced a total of 144+ 
hours of downtime.  During these outages, executives and line staff at Safeway 
who depended on Teradata applications were unable to perform their jobs using 
the business processes built around the Teradata system, resulting in business 
loss.  Interviews with Safeway executives and testimony given in depositions 
indicate that an outage of one hour or greater impacted an entire day’s effort.  In 
my experience, the crippling impact of a one-hour outage on the day’s business is 
consistent with what I have observed at other organizations. 
 
• 
Application performance was degraded – The Teradata system experienced a total 
of 111 hours of degraded performance from February 6, 2002 to December 31, 
2002.  During these periods, response time was delayed or data loaded through 
Trickle may have been up to several hours old.  Because the Teradata system was 
a real-time, mission-critical system, delayed or old data was unacceptable.  
Executives and staff began to question the validity of the data, not knowing how 
recent it was, reducing the business value of the system.  Safeway experienced an 
economic loss because of this. 
 
• 
IT staff resources were redeployed to recover the 40-node system – Immediately 
following the February 6th incident Safeway IT employees were reassigned to 
assist in recovering the system and associated data.  Thus, they could not perform 
the normal job functions for which Safeway was paying their salaries and 
benefits.  From February 6th 2002 to December 6th 2002, Safeway records show 
that three individuals spent a total of 359.5 hours on direct recovery efforts not 
associated with their normal job activities. 
 
• 
Applications were rewritten – As a result of repeated outages and performance 
degradation, Safeway rewrote its Trickle application so that it could be accessed 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 13 
Page 13 
without involving the Teradata system.  Safeway estimates that this application 
rewrite took the equivalent of two man-months of developer time. 
 
• 
Rollout of new applications was delayed – Because the IT staff was preoccupied 
with recovery efforts, IT staff resources were unavailable to develop planned new 
applications needed to maintain Safeway’s competitive edge.  Most notably, 
Safeway’s PPD application, which allowed products to be tracked according to 
margin and profits was delayed by two months.  Safeway estimates that this 
application provides an annual return on investment of $100 million. 
 
• 
IT staff resources were expended on bringing the new 60-node system online – 
Bringing a new Teradata system online requires installation, testing and loading 
of data.  Although Safeway has no direct records of the efforts involved in this 
task, in my opinion the company experienced an economic cost as a result of this 
otherwise unnecessary installation effort. 
 
 
Risks/Threats to Safeway as a Result of the Incident 
 
The February 6th incident created significant risks to Safeway’s business operations.  
These risks were in direct conflict with Safeway’s key business objectives of creating a 
reliable, secure, evolutionary system that could provide critical business intelligence in 
real-time and of an operational nature.  Following are the major risks posed to Safeway’s 
business. 
 
• 
Loss of confidence in the data – Safeway’s executives and line staff needed to be 
sure that the information delivered by the Teradata system reflected actual 
business conditions at a given time.  Business decisions and operations depended 
on the validity of this data.  Repeated outages and performance degradation led 
Safeway personnel to question the validity of the data produced by Teradata, thus 
limiting or eliminating the value of the system to assist in business decisions and 
operations.  For example, if sales at noon look like they should be at 11am, is it 
because the Teradata system failed and processing is behind by an hour or 
because the business is just having a really bad day? 
 
• 
Risk of data loss and/or corruption – Although the Teradata system does 
provide for redundant data storage and fall-back facilities, many of these 
capabilities depend on an expected mean-time-between failures (MTBF) of 
approximately 1.2 million hours per disk drive.  Under normal conditions, a 1.2 
million hour MTBF allows for the detection and replacement of a failed drive 
well before its data mirror fails.  The incident of February 6th significantly 
reduced disk drive life expectancy for a variety of reasons.  As a result, the 
possibility of multiple disk drives failing nearly simultaneously increased 
significantly — if not exponentially.  Should these failed drives contain the all the 
copies of a particular set of data (all customers whose name begins with the letter 
“S” for example), that data would be lost to the system and would require 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 14 
Page 14 
recovery from backup tape.  Estimates put this recovery time as high as 45 days, 
due to the fact that tape runs relatively slowly, the missing data could be 
anywhere on the tape or tapes, and that numerous tapes might have to be loaded to 
find the missing data from literally trillions of bytes of data — an unacceptable 
period given Safeway’s reliance on customer and purchasing data for its 
operations.  Thus, the February 6th incident significantly increased Safeway’s 
likelihood of losing critical data for potentially weeks at a time. 
 
• 
Business decision interruption/business operation interruption – repeated outages 
and performance degradation meant that at times the system was simply not 
available to aid Safeway personnel in their daily tasks.  As a result, pricing 
decisions could not be made, e-commerce engines and Website information was 
inaccurate, promotions could not be run, customer concerns could not be 
adequately addressed, and transactions with vendors could not be effectively 
executed.  The interruption of these business processes, as well as others that were 
threatened due to the February 6th incident, was an unacceptable business risk for 
Safeway. 
 
• 
Loss of NCR/Teradata Maintenance contract – Safeway’s maintenance contract 
with NCR was effectively terminated as a result of the February 6th incident (see 
NCR letter to Safeway dated April 10, 2002).  As a result, a key component of the 
overall Teradata.  There are few reliable sources of Teradata maintenance outside 
NCR. 
 
• 
Inability to evolve the system/add capacity – As stated earlier, the ability 
add/upgrade nodes is a key value proposition of the Teradata system and one for 
which Safeway had demonstrated a desire to take advantage of.  However, with 
the effective termination of the maintenance contract and the instability of the 
existing 40 nodes, it is highly unlikely that Safeway would add additional 
capacity to the system.  In my opinion, it would be an unwise business decision to 
enhance the damaged 40-node system.  As a result, one of the key business values 
which Safeway had previously recognized from its Teradata system – the ability 
to grow and adapt to new business requirements – was eliminated. 
 
These threats to its business operations were unacceptable to Safeway on a continuing 
basis.  The company faced three options: replace every single part with a brand-new 
spare in order to constitute a new system; replace the Teradata hardware/software 
solution with an alternative technology; or purchase a comparable new system from 
NCR/Teradata.  As discussed earlier, in my opinion, Safeway decided on the most 
prudent and cost-effective solution – to purchase a new Teradata system. 
 
 
Specific Damages 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 15 
Page 15 
I have identified the following damages incurred by Safeway as a direct result of the 
February 6th incident.  These damages fall into three major categories: direct recovery 
costs, direct replacement costs, and business interruption costs. 
 
Direct Recovery Costs 
 
The damages contained in this area reflect the direct costs (internal and external) incurred 
by Safeway in order to bring the 40-node system back online after the February 6th 
incident and to keep it operating in reduced capacity until the new 5300-class system was 
operational.  These costs include: 
 
• 
Recovery-related invoices paid to NCR – $1,234,889.26 
• 
MCI phone bills directly related to recovery efforts – $36,850.00 
• 
Hours spent by Safeway staff directly related to recovery efforts – $23,137.50 
• 
Effort spent by Safeway staff to rewrite the Trickle application for Web access -- 
$16,666.00 (based on 2 man-months developer time at a fully-loaded annual cost 
of $100,000). 
 
Total = $1,311,542.76 
 
Direct Replacement Costs 
 
In calculating the damages associated with these costs, I used the direct replacement costs 
associated with purchasing the new 48-node 5300-class system.  Replacement costs for a 
new system were because Safeway’s 40-node 5200-class system was a unique solution 
for which there is no two-year-old “used equipment” replacement on the open market.  
My research shows that the odds that Safeway would have been able to find a comparable 
used replacement in an acceptable timeframe were virtually nil and that it would not have 
been a prudent business decision to base a strategy on such a replacement path. 
 
In my opinion, Safeway took reasonable efforts to ensure that the replacement system 
configuration matched the 40-node system as closely as possible with respect to 
performance and throughput. 
 
The direct replacement costs for the 48-node 5300-class system from NCR invoices 
submitted as evidence is $11,742,608.18.  It is important to note that this total is less than 
the total of the two invoices dated DATE and September 27, 2002.  This is because I 
subtracted certain line items of the invoices that corresponded to software upgrades, 
which did not have to be replaced as a result of the incident. 
 
Because it should be considered as scrap, I have assigned no value to the damaged 40-
node system. 
 
Business Interruption Costs 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 16 
Page 16 
In calculating business interruption costs, I only assigned damage amounts in those cases 
where reliable data and metrics could be obtained.  Although I firmly believe that 
Safeway experienced additional damages that could not be measured, such as customer 
defections or lost business opportunities, I did not attempt to place a value on these items.  
It is important to note, however, that these intangible losses were not insignificant and 
clearly had an impact in Safeway’s decision to replace the damaged 40-node Teradata 
system with a new platform.  In my experience, consideration of these intangible issues is 
a reasonable business practice and Safeway was prudent in including these issues in its 
decision making process. 
 
The five applications for which I assigned direct business interruption damages are: 
 
• 
Call Center    
 
 
 
$199,688.00 
• 
Business Tracker/Allowances   
 
$6,875.00 
• 
CRM Segment and Target    
 
$1,680,000.00 
• 
Groceryworks/Safeway.com    
 
$279,949.00 
• 
Fuel    
 
 
 
 
$773,391.00 
 
Total    
 
 
 
 
 
$2,939,903.00 
 
Detailed descriptions of these applications, as well as the calculations used to arrive at 
damage estimates, are provided in Appendix A. 
 
Other applications deployed as of February 6th 2002 are listed below.  Damage estimates 
were not calculated because reliable data could not be gathered and/or the outages of the 
Teradata system were not of sufficient duration to cause measurable business interruption 
costs.  However, it is my opinion that additional, although intangible damages did in fact 
occur as a result of the unavailability/performance degradation experienced by these 
applications.  Moreover, were outages or performance degradation of longer duration to 
occur, additional applications (such as Fraud/Shrink) would have experienced measurable 
business interruption damages. 
 
Additional applications deployed on February 6, 2002. 
 
o Escript 
o United Airlines 
o Dreyer’s Extract 
o Customer Care Extract 
o Alaska Airlines 
o American Airlines 
o Continental Airlines 
o Customer Data Retention Technique 
o Fraud/Shrink 
o Real-time Promotion Management 
o Trickle (Data Feeds) 
o Dashboards for Executives 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 17 
Page 17 
o Sweepstakes 
o Distribution Voids 
o Out-of-stock Alerts 
o Lawyer Milk 
o SMS 
o Checker Scan Frequency/Checker Productivity Extract 
o Markdowns to NASC Extract 
 
 
 
Conclusions 
 
The incident at the Consonus data center on February 6, 2002 resulted in unacceptable 
damage to Safeway’s 40-node Teradata system.  In my opinion, Safeway made a prudent 
and correct choice in replacing this hardware in order to run its mission critical 
applications.  Remaining with the damaged 40-node would have resulted in unacceptable 
risk to Safeway, from a business interruption, data loss and spare parts/repair cost 
perspectives.  As a result of the incident, Safeway lost both its Teradata hardware and the 
maintenance contract associated with that system – two key components in its overall 
data warehousing solution.  Safeway needed this mission critical system in order to 
survive in the highly-competitive grocery market, and this was not possible with the 
compromised 40-node system.  Replacement was the most sound business decision. 
 
In my opinion, Safeway suffered significant damages as a result of the incident at the 
Consonus data center on February 6, 2002.  These damages are as follows: 
 
Direct Recovery Costs 
 
$1,311,542.76 
Dirrect Replacement Costs 
 
$11,742,608.18 
Business Interuption Costs 
 
$2,939,903.00 
 
 
Total Damages 
 
 
$15,994,053.94 
 
Supporting Data 
 
In addition to the depositions and evidence supplied by Dewsnup, King and Olsen, I have 
relied on the following information and analysis in formulating my decisions. 
 
Application Sheets  
 
Application Matrix from Safeway – Have – need to convert file format 
 
 
Interviews with Teradata Customers -- Have 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 18 
Page 18 
 
Interview with ANT -- Have 
 
 
 
Interview with other parts reseller – Need to write up 
 
 
Interview with CSI Financial – have 
 
 
Results of Parts Broker Site Searches – have in hardcopy 
 
 
 
 
Company Financials – have in hardcopy – need to extract in electronic format 
 
• 
Safeway 
• 
Albertsons 
• 
Kroegers 
• 
Walmart 
 
 
 
Teradata Product Information 
 
 
 
Teradata Customer Case Studies from NCR Website – have excel spreadsheet, need to 
embed. 
 
Excel spreadsheet itemizing costs of systems. 
 
 
Damage calculation worksheets with specific documents listed as evidence. 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 19 
Page 19 
 
Appendix A: Application Analysis Worksheets 
 
 
This section provides Aberdeen’s analysis of the various applications deployed on 
Safeway’s Teradata system on February 6, 2002.  For each application, I have provided a 
brief description; metrics with respect to date of deployment, number of users, frequency 
of data refreshment and user access, and data accessed; the origin of the application; its 
business value to Safeway; the business impact of application unavailability and data 
loss; and specific damage calculations.   
 
Additionally, I have assigned each application to one of three classifications.  Class 1 
Applications are static reporting solutions with infrequent data refreshment and access 
(anywhere from weekly to quarterly).  Class 2 Applications utilize data that is refreshed 
on a daily basis and are accessed by end-users at least once per day, and typically more 
frequent.  Class 3 Applications are of an operational data store nature.  Data is refreshed 
constantly throughout the day and end-users access the application continuously 
throughout the day. 
 
 
 
SHOW SCREEN SHOTS FOR AS MANY APPLICATIONS AS POSSIBLE. 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 20 
Page 20 
 
Name of Application: 
 
Call Center 
 
 
Application Classification :  
 
3 
 
 
Business Description of Application: 
 
Safeway customers can call a toll-free telephone number with questions.  Many of these 
questions regard purchases made at a local store – often purchases made the same day.  
Within 20 minutes of a purchase, call center representatives can access the purchase 
record of a customer who bought using a club card.  This is done through Trickle data 
uploaded into the Teradata system and then made available to the call center application.  
On average, the call center makes 100-200 queries against the Teradata system per day 
(average of 150 queries). 
 
 
Date of Deployment: 
 
On or about June 2001. 
 
Number of Users: 
 
Approximately 20. 
 
Frequency of Data Refresh 
 
Every 20 minutes 
 
Frequency of User Access 
 
Continuously on a 24 x7 basis.   
 
Data Sets Accessed: 
 
Trickle data from the store point-of-sale (POS) systems. 
 
Business Value of Application: 
 
The call center application allows service representatives to quickly and effectively 
answer customer inquiries.  Being responsive to customers is critical if Safeway is to 
foster customer loyalty through superior service.  As a result, Safeway has made 
significant investments in having a responsive call center. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 21 
Page 21 
Many of the calls into the center are in regards to purchases made that day at a local 
Safeway store or through Safeway.com/GroceryWorks.  As a result, call centers often 
need to be able to access what a customer has just purchased in order to answer their 
question effectively.  This purchase information is made available through the Teradata 
system.  If this information is not available, the service representative is not able to 
effectively perform his or her customer service function.  In essence, Safeway has 
incurred the high expense of answering a customer’s inquiry through a call center without 
receiving the business value of a fully satisfied customer. 
 
 
Planned Enhancements 
 
There are no planned enhancements for this application. 
 
 
Impact of February 6, 2002 Incident 
 
As a result of the incident, the call center application suffered from a total of 14.75 days 
of Teradata downtime (6 days from 2/6/02 to 2/11/02 and 8.75 days (70 hours) from 
2/11/02 to 12/31/02).  Additionally, the Teradata system also experienced a total of 38.5 
days (308 hours) of degraded performance from 2/6/02 to 12/31/02.  Because the call 
center application relies on customer transaction data that is updated every 20 minutes, 
the application was not receiving useful data during periods of degraded performance.  
As a result, the call center experienced a total of 53.25 days of operation (representing 
7,988 calls) without up-to-date data from the Teradata solution.  Calls that required 
access to this data could not be resolved completely in the manner Safeway and its 
customers had come to expect. 
 
Business Impact for Short Term Outage (1 hour or less)\ 
 
Customer calls requiring access to recent POS data cannot be resolved. 
 
Business Impact for Medium Term Outage (between 1 hour and 1 day) 
 
Customer calls requiring access to recent POS data cannot be resolved. 
 
Business Impact for Long-term Outage (Greater than 1 day) 
 
Customer calls requiring access to recent POS data cannot be resolved.  Potential of 
significant customer dissatisfaction. 
 
 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 22 
Page 22 
Business Value Damage Calculations 
 
If a call that comes into the call center requires access to the Teradata system in order for 
a query to be answered and the Teradata system is not available, Safeway has incurred 
the cost of answering/servicing that call without the business value of having a satisfied 
customer.  On average, 100-200 call per day required access to the Teradata system 
(average of 150 calls per day).  Most industry estimates put the cost of a live telephone 
call into a call center at around $25.00. 
 
Moreover, it is my opinion that some for these incompletely-answered calls resulted in 
customer defections to the competition.  However, I have no way of placing a dollar 
figure on these damages. 
 
Loss for 6-day period – 2/6/02 to 2/11/02 
 
6 days x 150 calls per day x $25 per call = $22,500 
 
 
Loss for subsequent days with downtime/degraded service 
 
Downtime excluding 2/6-11/03 = 70 hours or 8.75 business days 
 
Degraded time = 308 hours or 38.5 business days 
 
Total of 47.25 days with no or limited access to Teradata system from call center 
 
47.25 days x 150 calls per day x $25 per call = $177,188 
 
 
 
Total Damages = $199,688 
 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 23 
Page 23 
 
 
Application:    
 
Business Tracker/Allowances 
 
 
Application Classification:  
 
2 
 
 
Business Description of Application: 
 
Safeway uses Business Tracker for a variety of business monitoring and analytic 
activities.  For the purposes of this discussion, I am focusing on the use of Business 
Tracker by Safeway to determine reimbursement amounts from vendor promotions.  
Safeway participates in numerous discount programs initiated by its suppliers.  In many 
of these, a customer receives a discount for an item or coupon when they are at the check-
out counter.  Safeway must track these discounted transactions and then seek 
reimbursement from the supplier.  Should Safeway not be able to track these allowances, 
it is unable to be reimbursed for the allowances.  These funds due to Safeway are then 
delayed until accurate tracking data can be provided through the Teradata system. 
 
Date of Deployment: 
 
On or about November 1999 
 
Number of Users: 
 
Approximately 230 
 
Frequency of Data Refreshment 
 
Every 20 minutes 
 
Frequency of User Access 
 
Periodically throughout the day. 
 
Data Sets Accessed: 
 
POS data through Trickle – specifically product sale data, store information, shipments 
and promotions. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 24 
Page 24 
Business Value of Application: 
 
The application is used to claim reimbursements from vendors for promotion campaigns.  
For 2002, $2,070,218,313 ($5,571,830 per day) was reimbursed to Safeway as part of this 
program. 
 
In contrast, Safeway had only $65,000,000 in cash for the period ending March 23, 2002.  
The company’s cost of goods sold and operating/administrative expenses totaled 
$7,320,800,000 ($87,152,000 per day) for that 12-week period.  Safeway has less than 
one day’s cash on hand.  Should Safeway be unable to report and collect allowance 
reimbursements, Safeway’s cash flow would be negatively impacted by $5.57 million per 
day.  This would reduce Safeway’s cash position to zero in less than 12 days. 
 
In comparison, for the quarter ended May 2, 2002, Albertson’s reported a cash balance of 
$383 million on quarterly revenues of $8.921 billion.  The Kroger Company had $185 
million in cash on revenues of $15.667 billion for the quarter ended May 25, 2002.  
These financial figures were gathered from SEC filings. 
 
Planned Enhancements 
 
Convert application to access Teradata solely.  Today it accesses Teradata and Greenland. 
 
Impact of February 6, 2002 Incident 
 
As a result of the incident, Safeway was unable to calculate the reimbursement amounts 
due from its suppliers.  Although this data was eventually recovered and the discounts 
reimbursed, there was a delay.  As a result, money that could have been earning a return 
for Safeway was in some other organization’s account.  My direct damage calculations 
are based on this logic.  Aberdeen I used an interest rate of 1.8% (the average rate for 3-
month non-financial commercial paper for the week ending February 8, 2002 according 
to the Federal Reserve’s Web site) and assumed an average allowance reimbursement of 
$5.57 million per day.  All allowance reimbursements were assumed to be delayed until 
February 12, 2002.  Additionally, for the period of 2/12/02 through 12/31/03, for any day 
that experienced an outage of one hour or more, the $5.57 million in reimbursements was 
delayed for a single day.  My reasoning is that the effects of an hour-plus outage linger 
after on after the system is restored, in my experience, such that IT staff typically has 
control of the system, not business users.  Therefore, if an outage of more than an hour 
occurs, the presumption is that business users do not have application access for the 
remainder of the business day. 
 
 
Business Value Damage Calculations 
 
Loss for 6-day period – 2/6/02 to 2/11/02 
 
Interest on $5.57 million per day (cumulative) at 5% interest rate.   

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 25 
Page 25 
 
• 
February 6th: $5.57 million for 6 days = $1,650.00 
• 
February 7th: $5.57 million for 5 days = $1,375.00 
• 
February 8th: $5.57 million for 4 days = $1,100.00 
• 
February 9th: $5.57 million for 3 days = $825.00 
• 
February 10th: $5.57 million for 2 days = $550.00 
• 
February 11th: $5.57 million for 1 day = $275.00 
 
Total = $5,775.00 
 
Loss for subsequent days with downtime of one hour or more. 
 
2/16/02, 3/31/02, 4/21/02, 5/16/02 = 4 total days 
 
• 
Interest on $5.57 million for 4 single days = $1,100.00 
 
 
Total Damages = $6,875.00 
 
 
 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 26 
Page 26 
 
 
Application:    
 
CRM Segment and Target 
 
 
Application Classification:  
 
3 
 
 
Business Description of Application: 
 
The Segment and Target (S&T) application is used by Safeway’s marketing organization 
to target specific groups of loyalty card holders with individual enticements and 
promotions.  In 2002, Safeway held 631 individual promotions, or an average of 1.72 per 
day.  Safeway executives develop a specific promotion and then determine what segment 
within its card holder database (based on geography, demographics and previous 
purchasing history) should receive the promotion.  Safeway has over 35 million 
households in its database and based on the success of this program, the direct mail 
budget for promotions has been increased from $3.77 million in 2002 to $6.85 million in 
2003. 
 
The S&T application is used to extract the names of individuals for these promotions and 
then to track the success of a promotion on an ongoing basis. 
 
Date of Deployment: 
 
On or about July 2000 
 
Number of Users: 
 
5 
 
Frequency of Data Refreshment 
 
Every 20 minutes 
 
Frequency of User Access 
 
Hourly 
 
Data Sets Accessed: 
 
POS data through Trickle – specifically product sale data by customer. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 27 
Page 27 
Business Value of Application: 
 
The value of the application is measured through increased spending by individuals 
targeted by a specific promotion.  Safeway typically also tracks a control group in 
measuring the impact of a promotion.  Safeway provided me with data for fifteen 
promotions that occurred between April 2002 and March 2003 as a random sample.  The 
average return on each promotion was $97,312 when measuring the spending of the 
participants in the promotion against the control group.  Extrapolating this figure over 
631 promotions yields an annual figure of $61.4 million in incremental sales, or $168,000 
per day. 
 
Planned Enhancements 
 
No enhancements are planned. 
 
Impact of February 6, 2002 Incident 
 
During February 6-11, 2002, Safeway was unable to extract targeted lists of individuals 
for promotions.  As a result, Safeway could not perform its targeted promotion business 
processes for six days.  This is a loss that cannot be recovered.  Additionally, for any day 
that experienced an unscheduled outage of one hour or more for the Teradata system, my 
assumption is that extractions for that day were also not performed. 
 
Interviews with senior Safeway executives revealed that the Teradata outages resulted in 
a great deal of uncertainty with respect to targeted promotions.  Divisional staff 
continuously questioned the numbers resulting from promotions and was hesitant to 
initiate new programs.  This atmosphere of uncertainty lasted throughout 2002.  Although 
I am not comfortable putting a firm damage calculation estimate on the cost of this 
uncertainty, I do believe that it was an important factor that was considered when 
evaluating whether a new Teradata system was required, and how soon. 
 
Business Value Damage Calculations 
 
Loss for 6-day period – 2/6/02 to 2/11/02 
 
Six days at $168,000 per day = $1,008,000.   
 
Loss for subsequent days with downtime of one hour or more. 
 
2/16/02, 3/31/02, 4/21/02, 5/16/02 = 4 total days 
 
Four days at $168,000 per day = $672,000.   
 
Total Damages = $1,680,000.00 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 28 
Page 28 
 
 
Application:    
 
GroceryWorks/Safeway.com 
 
 
Application Classification:  
 
3 
 
 
Business Description of Application: 
 
GroceryWorks is Safeway’s online shopping website.  It allows Safeway customers to 
look at pricing for items at their local store as well as to make actual purchases for home 
delivery.  The Teradata system has two important roles in this application.  First, the 
Teradata system is responsible for populating the pricing and promotion information that 
is displayed for all products on an individual store level.  Second, on an individual user 
basis the Teradata system automatically populates the “My Favorites” menu, which 
displays the most frequently-purchased items on an individual-shopper basis.  My 
Favorites is driven off of Club Card data. 
 
Date of Deployment: 
 
On or about October 2001 
 
Number of Users: 
 
Approximately 100 per day in February 2002.  Almost 800 per day by December 2002. 
 
Frequency of Data Refreshment 
 
Every 20 minutes 
 
Frequency of User Access 
 
24 x 7 
 
Data Sets Accessed: 
 
POS data through Trickle – specifically product pricing information by store; Club Card 
information. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 29 
Page 29 
Business Value of Application: 
 
The value of the application is two-fold.  First, it is a direct source of revenues through 
incremental sales.  In February 2002, Safeway was rapidly ramping up its online sales 
initiative.  Total online revenues for Weeks 5-8 2002 totaled $255,963.  For the last 4 
weeks of 2002, total GroceryWorks sales totaled $2,995,830. 
 
A second value of GroceryWorks, but one that cannot be measured is that it is a way for 
customer to comparison shop before they visit a Safeway location.  Because pricing 
varies throughout the day, and by store location, in order to be competitive, it is critical 
for Safeway to have accurate pricing and promotion data displayed in GroceryWorks.  
With inaccurate pricing, individuals may, after checking pricing over the Web, decide to 
go to a competitor’s location. 
 
Planned Enhancements 
 
No enhancements are planned at this time. 
 
Impact of February 6, 2002 Incident 
 
The loss of the Teradata system had two ramifications for GroceryWorks.  The first is the 
inability to have pricing updates automatically populated on the safeway.com Web site.  
As a result, customer were receiving inaccurate, outdated pricing.  Even though Safeway 
frequently reduces prices on certain items to remain competitive, these updates would not 
be reflected on the Web site.  In the highly price-sensitive grocery market, this inability 
to manage prices put Safeway at a competitive disadvantage — especially with those 
sophisticated customers who had become used to seeing accurate promotional pricing on 
the GroceryWorks web site.   
 
Moreover, GroceryWorks was relatively new for Safeway at the time of the incident, 
having been deployed only four months before.  Sales via the company’s Web site were 
just ramping up.  As a result, although the actual lost sales were relatively small in 
February 2002, as total sales increased through 2002, the impact of inaccurate pricing 
would grow proportionally.  Finally, potential customers may also spot-check prices for 
Safeway and its competitors before deciding which location to actually visit on a 
particular day.  Incorrect pricing may thus drive away customers in addition to those that 
shop online.  Although there is no way of measuring this loss, it is an important factor in 
determining the business value of the Teradata system – and the business risk of not 
having the system available. 
 
The second impact of an outage of the Teradata system is that the “My Favorites” 
component of GroceryWorks would not be updated based on the most recent purchase 
information tied to an individual’s Club Card.  Although this facility is not critical to 
executing online orders, it is a capability that fosters loyalty among shoppers and 
considerably improves the overall online experience. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 30 
Page 30 
 
 
Business Value Damage Calculations 
 
In determining business damages for this application, I examined actual sales data 
through GroceryWorks for the period of January – March 2002.  Actual sales were then 
mapped against a straight-line plot of how sales would have grown had they increased an 
equal amount each week (see Figure XX).  This exercise was performed for 10-week, 12-
week and 52-week growth lines.  I used 10- and 12-week growth lines because this is the 
approximate time that showed the greatest downtime and performance degradation for 
the Teradata system.  I used a 52-week growth line to get rid of any seasonal variation.  
As can be seen, starting in the sixth week of 2002 (the time of the data center incident) 
actual sales dip significantly below what the straight-line plot forecast.  Aberdeen then 
calculated the difference between the actual and the three projected GroceryWorks sales 
plots and totaled the average of these three calculations (see Table XX).   
 
These values were calculated for two time frames – Weeks 6-10 and Weeks 6-12.  The 
reason for these 5- and 7-week timeframes is that there is often a residual effect of 
improper pricing that extends beyond the actual period of missed pricing.  This effect can 
be seen visually in Figure XX. 
 
The result is an average shortfall in GroceryWorks sales of $279,929.   
 
 
Total Damages = $279,949.00 
 
Figure XX 
 
 
 
 
 
 
GroceryWorks Sales Comparison Q1 2002
$0.00
$50,000.00
$100,000.00
$150,000.00
$200,000.00
$250,000.00
$300,000.00
$350,000.00
1
2
3
4
5
6
7
8
9 10 11 12
Week
Sales
Actual
GroceryWorks
Sales
12-Week Straight-
line Sales
10-Week Straight-
line Sales
52-Week Straight-
line

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 31 
Page 31 
Table XX 
 
 
Week
Actual Sales
12-Week Straight-
line Sales
Difference
1
$18,123.78
$18,123.78
$0.00
2
$42,240.25
$42,785.78
$545.53
3
$58,939.64
$67,447.77
$8,508.13
4
$60,143.54
$92,109.77
$31,966.23
5
$71,833.01
$116,771.76
$44,938.75
6
$66,967.77
$141,433.76
$74,465.99
7
$56,176.43
$166,095.75
$109,919.32
8
$60,987.25
$190,757.75
$129,770.50
9
$106,170.72
$215,419.74
$109,249.02
10
$142,959.53
$240,081.74
$97,122.21
11
$247,161.82
$264,743.73
$17,581.91
12
$289,405.73
$289,405.73
$0.00
Difference Weeks 6-12
$538,108.96
Week
Actual Sales
10-Week Straight-
line Sales
Difference
1
$18,123.78
$18,123.78
$0.00
2
$42,240.25
$31,994.42
-$10,245.83
3
$58,939.64
$45,865.06
-$13,074.58
4
$60,143.54
$59,735.70
-$407.84
5
$71,833.01
$73,606.34
$1,773.33
6
$66,967.77
$87,476.97
$20,509.20
7
$56,176.43
$101,347.61
$45,171.18
8
$60,987.25
$115,218.25
$54,231.00
9
$106,170.72
$129,088.89
$22,918.17
10
$142,959.53
$142,959.53
$0.00
Difference Weeks 6-10
$142,829.56
Week
Actual Sales
52-Week Straight-
line Sales
Difference
1
$18,123.78
$18,123.78
$0.00
2
$42,240.25
$32,453.86
-$9,786.39
3
$58,939.64
$46,783.94
-$12,155.70
4
$60,143.54
$61,114.02
$970.48
5
$71,833.01
$75,444.10
$3,611.09
6
$66,967.77
$89,774.18
$22,806.41
7
$56,176.43
$104,104.26
$47,927.83
8
$60,987.25
$118,434.34
$57,447.09
9
$106,170.72
$132,764.41
$26,593.69
10
$142,959.53
$147,094.49
$4,134.96
Difference Weeks 6-10
$158,909.98
Average of 3 Methods
$279,949.50

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 32 
Page 32 
 
Application:    
 
Fuel Sales & Pricing 
 
 
Application Classification:  
 
3 
 
 
Business Description of Application: 
 
Fuel is used by Safeway to examine fuel sales at its 268 fuel outlets (approximately 150 
outlets in February 2002).  The application provides metrics in both dollars and gallons.  
Because the fuel pumps are not integrated with Safeway’s operational POS system, the 
Teradata system provides the only means by which fuel sales data can be tracked and 
analyzed.  Safeway individuals examine fuel sales data on a regular basis throughout the 
day and typically make two pricing changes per outlet per day.  Interviews with Safeway 
employees reveal that because the Safeway fuel does not have a strong brand attached to 
it (in comparison to Shell or Exxon-Mobil), Safeway must compete based on price and 
convenience.  As a result, Safeway individuals indicated, a price differential of only a 
few cents may mean a difference of up to 50% in the total volume (gallons) of fuel sold at 
a particular location.  Through aggressive pricing, Safeway has managed to its gallons 
sold per outlet per day to nearly four times the industry average.  Moreover, increasing 
sales through its fuel outlets is a key element in increasing same-store-sales and 
profitability for Safeway. 
 
Date of Deployment: 
 
On or about April 2001 
 
Number of Users: 
 
Approximately 18 
 
Frequency of Data Refreshment 
 
Daily 
 
Frequency of User Access 
 
Daily 
 
Data Sets Accessed: 
 
CCISTech Fuel Management System (TBF) 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 33 
Page 33 
Business Value of Application: 
 
The value of the application is that it allows Safeway users to monitor fuel sales in both 
dollars and gallons.  If gallon volume is below nominal values, Safeway would lower 
prices to boost sales.  If volume is above nominal values, prices can be increased for extra 
profit margin.  The ability to monitor sales on a location-by-location basis is critical in 
maintaining volume.  Without this capability, prices cannot be effectively changed to 
meet local market demand from a centralized location. 
 
Additionally, by law Safeway must track gallons sold by location on a daily basis.  The 
reason for this is to spot potential leakages. 
 
Planned Enhancements 
 
Load fuel sales through Trickle.  Provide dashboard views onto fuel sales on a 24 hour 
basis. 
 
Impact of February 6, 2002 Incident 
 
Interviews with Safeway individuals reveal that the outages caused by the data center 
incident eliminated their ability to make pricing decisions – particularly for the period of 
February 6-11.  Thus, Safeway could not price competitively. 
 
Additionally, because Safeway could not track gallon volume on a daily basis, it was 
technically in default of its legal obligation to do so. 
 
Business Value Damage Calculations 
 
In determining business damages for this application, I examined actual fuel sales data 
through for the period of January – March 2002.  Actual sales were then mapped against 
a straight-line plot of how sales would have grown had they increased an equal amount 
each week (see Figure XX).  This exercise was performed for 10-week, 12-week and 24-
week growth lines.  I used 10- and 12-week growth lines because this is the timeframe 
that showed the greatest downtime and performance degradation for the Teradata system.  
As can be seen, starting in the sixth week of 2002 (the time of the data center incident) 
actual sales dipped significantly below what the straight-line plot forecast.  I then 
calculated the difference between the actual and the three projected fuel sales plots and 
totaled the average of these three calculations (see Table XX).   
 
These values were calculated for two time frames – Weeks 6-10 and Weeks 6-12.  The 
reason for these 5- and 7-week timeframes is that there is often a residual effect of 
improper pricing that extends beyond the actual period of missed pricing.  This effect can 
be seen visually in Figure XX. 
 
The result is an average shortfall in fuel sales of $773,391.   
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 34 
Page 34 
 
Total Damages = $773,391.00 
 
Figure XX 
 
 
Fuel Sales Comparison Q1 2002
$0
$500,000
$1,000,000
$1,500,000
$2,000,000
$2,500,000
$3,000,000
$3,500,000
1
2
3
4
5
6
7
8
9
10 11 12
Week
Sales
2002 Actual Fuel
Sales
12-week Straight-
line Sales
10-week Straight-
line Sales
24-week Straight-
line Sales

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 35 
Page 35 
 
Table XX 
 
Week
Actual Sales
12-week Straight-line 
Sales
Difference
1
$1,929,383
$1,929,383
$0
2
$2,069,896
$2,030,160
-$39,736
3
$2,254,811
$2,130,936
-$123,874
4
$2,172,458
$2,231,713
$59,255
5
$2,209,879
$2,332,489
$122,610
6
$2,058,943
$2,433,266
$374,323
7
$2,091,102
$2,534,042
$442,940
8
$2,215,808
$2,634,819
$419,011
9
$2,539,727
$2,735,595
$195,868
10
$2,532,165
$2,836,371
$304,207
11
$2,802,961
$2,937,148
$134,187
12
$3,037,924
$3,037,924
$0
Difference Weeks 6-12
$1,870,536
Week
Actual Sales
10-week Straight-line 
Sales
Difference
1
$1,929,383
$1,929,383
$0
2
$2,069,896
$1,996,359
-$73,536
3
$2,254,811
$2,063,335
-$191,476
4
$2,172,458
$2,130,311
-$42,147
5
$2,209,879
$2,197,286
-$12,593
6
$2,058,943
$2,264,262
$205,319
7
$2,091,102
$2,331,238
$240,136
8
$2,215,808
$2,398,213
$182,406
9
$2,539,727
$2,465,189
-$74,538
10
$2,532,165
$2,532,165
$0
Difference Weeks 6-10
$553,323
Week
Actual Sales
24-week Straight-line 
Sales
Difference
1
$1,929,383
$1,929,383
$0
2
$2,069,896
$1,977,588
-$92,308
3
$2,254,811
$2,025,792
-$229,019
4
$2,172,458
$2,073,996
-$98,462
5
$2,209,879
$2,122,200
-$87,680
6
$2,058,943
$2,170,404
$111,461
7
$2,091,102
$2,218,608
$127,506
8
$2,215,808
$2,266,812
$51,004
9
$2,539,727
$2,315,016
-$224,711
10
$2,532,165
$2,363,220
-$168,945
Difference Weeks 6-10
-$103,685
Average of 3 Methods
$773,391

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 36 
Page 36 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 37 
Page 37 
 
 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 38 
Page 38 
 
Appendix B: Supporting Data 
 
Following is the data gathered during my research efforts and used to formulate my 
opinions in this case. 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 39 
Page 39 
 
 
Interview with CSA Financial 
 
 
Date:  
10/27/2003 
 
Individual: 
Pat Rosseel, Sales Executive 
 
Company: 
CSA Financial 
 
CSA Financial is a leasing firm for enterprise-class hardware and software solutions.  
One of the companies they lease for is Teradata. 
 
They will take back used equipment and resell it, but typically this is only done if it is 
equipment that is coming off one of their leases, or a new customer wants to trade in old 
equipment as part a new leasing package.  They typically do not just take used equipment 
and try to resell it for a customer.  It usually must be part of some larger package.  The 
used equipment would be applied as a credit against the new leasing program. 
 
CSA does not control the Teradata operating system, database or software utilities.  The 
customer must still buy these direct from NCR at NCR-established pricing.  Rosseel 
stated that because NCR has recently announced the 6300-class system, the 5250 systems 
will soon be two generations old.  He believes that this means that the hardware for an 
undamaged 5250 system will be worth 5-10% of the original hardware purchase price.  
Given that the system has been in the incident with the fire suppression system and 
experienced arcing, he was skeptical as to whether the system would now be worth 
anything at all.  He would certainly insist on examining the system before offering any 
kind of credit. 
 
He currently has a 4-node 5250 system in his inventory.  He stated that a 40-node system 
is quite large and he would likely have to sell it in smaller components. 
 
He also stated that in his experience, existing users of Teradata systems are very loyal 
and are typically inclined to stay with Teradata as they upgrade capabilities. 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 40 
Page 40 
 
 
Interview with ANT (Aix Nittany Technology) 
 
 
Date:  
9/16/2003 
 
Individual: 
Joe Kennedy, President 
 
Company: 
ANT 
 
ANT is a broker of used Teradata equipment and was identified by NCR individuals as 
the only company of which they are aware that brokers used Teradata equipment in the 
U.S.   
 
Mr. Kennedy stated that there essentially is no market for used, complete Teradata 
systems.  In his experience, used Teradata hardware is only valuable for its individual 
parts.  The reason for this is that NCR/Teradata controls the operating system and 
database licenses.  As a result, he only deals with the hardware.  He does not provide 
maintenance services nor does he resell software licenses.  Therefore, even if he could 
find a buyer for an entire multi-node hardware system, the customer would still need to 
buy software and maintenance services from NCR.  Moreover, in his experience, most 
users typically will buy maintenance contracts directly from NCR only.  His perspective 
is that NCR would then raise the software/maintenance price so high that the total cost of 
the used system would be equivalent to a new system direct from NCR.  He has found 
that NCR tries to discourage a used market for Teradata systems. 
 
He thought that it might be possible to find a customer who might be looking for a few 
nodes to add on to an existing system.  Even then you would have to buy software and 
maintenance from NCR for these nodes.  He believed it to be very unlikely that you could 
find such a buyer. 
 
In summary, to him used Teradata hardware is a collection of disk drives, processors, 
power supplies, cables, etc.  He noted that in undamaged condition the disk drives for a 
5250-class machine typically sold for $10 to $20 each. 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 41 
Page 41 
 
Surveys of Teradata Customers 
 
Following are five survey questionnaires filled out by Teradata customers with NCR’s 
assistance on my behalf. 
 
Customer #1 
 
1. Name: Confidential 
2. Title 
 
3. Company: Major Mall-based Mass Merchant in the U.S. 
 
4. Company Size and Industry: 2003 Rev $ 32.3B, General Merchandise Department 
Store with  1,100 locations 
 
5. Please describe your involvement/experience with your Teradata system. Using 
Teradata since 1996 for marketing and customer scoring supporting catalog 
operations initially. 
 
6. How big is your current system?  40 Production Nodes, and 4 Test and 
Development Nodes. 103.10 Terabytes How long has it been in place? Since 1996  
 
7. Have you upgraded your Teradata system since initial installation? Yes, multiple 
times as required by new business user needs. Started with NCR 5100 then 
upgraded CPU and Disks resulting in 5150s. Again Upgraded to 5200s and finally 
in 2000 to 5250s. We now have two Teradata systems supporting Merchandising 
and Marketing functions.   
 
8. Please describe the application portfolio currently on your Teradata system. 
Teradata supports the daily operation of the company. Our systems run Teradata 
CRM, Click stream analysis, Logistics, Teradata Demand Chain Mgmt. 
(purchased in 2003), Price Optimization, Financial Reporting, Sales Reporting, 
HR Reporting, and basic end user Ad-Hoc reporting. 
 
9. Please describe any future applications that you plan to deploy on your Teradata 
system. We have not identified any at this time but will begin to evaluate this in 
2004. 
 
10. How long do you plan to keep your system?    We lease most of our technology 
for three or five years depending on platform and what it supports. Our current 
Teradata lease expires in 2005. What do you believe is the system’s life 
expectancy?  Given we lease NCR equipment, we determine at the end of the 
lease if we should extend the lease or purchase new equipment. We have done 
both in the past.  We do, however, try to stay current with technology if it will 
advance our capability to run our business more efficiently.  

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 42 
Page 42 
11. Would you consider purchasing a used Teradata system?  Yes and we have in the 
past due to our economic condition and the state of the retail economy. We 
purchased the equipment from NCR which at the time met our economic needs. 
 
12. If so, what would be your criteria for evaluating such a system?  Compatibility 
with our installed platform, 100% certification from NCR Customer Services, 
economical price, age, supportability, past history and cost of bring up to current 
specifications.  What would you want to know about its previous history? Why it 
was returned, how it was used, where it was used, age, was it supported and was it 
maintained by NCR or a third party contractor, compatibility with our current 
system, maintenance history, upgrade history, and down time history.  
 
13. Do you have a services contract from NCR for your Teradata system?  Yes, 
Business Critical ESS If so, how important is the contract to your ongoing 
activities? Could not run those aspects of our business that depend on Teradata 
without NCR Customer Service supporting our maintenance needs? 
 
14. What is the typical availability of your Teradata system?   99.89 % up time 
annually at this time. What is the amount of downtime experienced? .11 annually  
 
15. How critical is the Teradata system to the ongoing operations/success of your 
business? Teradata is critical to operating our business. It is considered mission 
critical for both decision support and operational aspects of our business. If it 
were down for an extended period (more than a day), it would severely affect 
running our business. 
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 43 
Page 43 
 
 
Customer #2 
 
1. Name: Confidential 
 
2. Title 
 
3. Company: Large Grocery Store Chain in the Western US 
 
4. Company Size and Industry: $ 35.6 Billion, 2003 sales, 2,300 locations 
 
5. Please describe your involvement/experience with your Teradata system.  We 
purchased our first Teradata system in 2001. The initial purchase was 20 nodes 
supporting 30 Terabytes of disk storage. 
 
6. How big is your current system? 40 Nodes, 60 Terabytes.  How long has it been 
in place? 2001 
 
7. Have you upgraded your Teradata system since initial installation? Our first 
purchase was in 2001 with 20 nodes and 30 Terabytes of disk. We have upgraded 
in 2002 to additional 20 nodes and 30 Terabytes of disk. 
 
8. Please describe the application portfolio currently on your Teradata system. 
Teradata supports traditional business analytics such as sales analysis, category 
management, marketing, and basic low-level customer analysis. 
 
9. Please describe any future applications that you plan to deploy on your Teradata 
system. We plan to add product forecasting, supply chain, financial management 
and promotions analysis in the future. 
 
10. How long do you plan to keep your system?   We typically depreciate technology 
purchases over a five-year period. What do you believe is the system’s life 
expectancy? Five years: this means we will replace half our system in 2006 and 
the remaining half in 2007. 
 
11. Would you consider purchasing a used Teradata system? Not at this time 
 
12. If so, what would be your criteria for evaluating such a system?  What would you 
want to know about its previous history? 
 
13. Do you have a services contract from NCR for your Teradata system?  Yes we 
have a Business Critical service agreement.  If so, how important is the contract to 
your ongoing activities? This is very important to how we operate our business. 
Without NCR service, it would drastically impact our ability to operate our 
business as we do today. 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 44 
Page 44 
 
14. What is the typical availability of your Teradata system?   99.93 at this time. 
What is the amount of downtime experienced? .07 unplanned outages. 
 
15. How critical is the Teradata system to the ongoing operations/success of your 
business? The system is critical to our ongoing success to service shopper needs 
by having the right products in the stores when needed. Teradata is not a mission 
critical system since we could run our business if it were to be down for an 
extended time. However, it would drastically affect our profitability and 
capability to maintain customer satisfaction.  
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 45 
Page 45 
 
 
Customer #3 
 
1. Name: Confidential 
2. Title 
 
3. Company: Hypermarket in the US 
 
4. Company Size and Industry: 2003 Rev $ 14.4 B, 4,250 stores 
 
5. Please describe your involvement/experience with your Teradata system. 
Purchased Teradata for sale & inventory analysis with basic decision support 
activities in 2000 and view it as fundamental to helping to enable achieving our 
corporate vision. 
 
6. How big is your current system?  24 Nodes, 25 Terabytes How long has it been in 
place? Since 2000 
 
7. Have you upgraded your Teradata system since initial installation? Yes.   In 2000, 
we started with eight nodes. In 2001, we upgraded to 5250 hardware. In early 
2002 we added 4 5300 nodes and another 4 5350 nodes late 2002.  In June of 
2003, we replaced all of our disk storage with EMC that now has us at 25 TB. 
 
8. Please describe the application portfolio currently on your Teradata system. 
Teradata is supporting basic retail decision support in the areas of merchandising, 
management and allocation in addition to sales reporting. We have several home 
grown applications running as well.  
 
9. Please describe any future applications that you plan to deploy on your Teradata 
system.  Loss Prevention and financial mgmt.   
 
10. How long do you plan to keep your system?   We purchase all equipment and 
depreciate it over a 36-month period at which time we evaluate replacing it 
depending on technology advancements and business needs. What do you believe 
is the system’s life expectancy?  36 months but depends on several factors if 
replace with new technology.  
 
11. Would you consider purchasing a used Teradata system? No. 
 
12. If so, what would be your criteria for evaluating such a system?  What would you 
want to know about its previous history? 
 
13. Do you have a services contract from NCR for your Teradata system?  Yes, 
Business Critical ESS If so, how important is the contract to your ongoing 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 46 
Page 46 
activities?  Their support is key to keeping our system running and serving our 
business user needs. 
 
14. What is the typical availability of your Teradata system?   99.975 % up time. 
What is the amount of downtime experienced? We have experienced this year an 
extended outage that took several days to repair.  
 
15. How critical is the Teradata system to the ongoing operations/success of your 
business?  Teradata is key to our success but we can run our business without it 
should we experience a long outage. We could function but the decisions we 
would have to make would not be the most accurate and eventually it would affect 
our results.  
 
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 47 
Page 47 
 
 
Customer #4 
 
 
1. Name: Confidential 
2. Title 
 
3. Company: Hypermarket in the US 
 
4. Company Size and Industry: 2003 Rev $ 10.6 B, 160 locations 
 
5. Please describe your involvement/experience with your Teradata system. We have 
been using Teradata since 1991 with the purchase of a DBC 1012. Our system 
and dependency on system has expanded since 1991 through multiple generations 
of Teradata hardware and data base releases. We currently have 4,000+ users on 
the system. 
 
6. How big is your current system?  20 Nodes, 20 Terabytes How long has it been in 
place? Since 1991  
 
7. Have you upgraded your Teradata system since initial installation? Yes. The 
company has gone through multiple upgrades due to increasing business demands 
along with technology and Teradata DB advancements. DBC 1012-3600-5100-
5200-5350. Started with DBC 1012 then 3600 in the early nineties.  We had a 12 
node 5250 before 2001supporting 12 TB of disk drives. We added 8 more nodes 
in 2002 and an additional 8 TB of disk storage. 
 
8. Please describe the application portfolio currently on your Teradata system. 
Teradata is supporting merchandising, forecasting, financial mgmt reporting. 
Store operations, and Marketing functions. It also supports HR reporting with data 
feeds from our PeopleSoft application. 
 
9. Please describe any future applications that you plan to deploy on your Teradata 
system.  We are evaluating future application road maps at this time for 
deployment in 2004 but nothing is definite yet.  
 
10. How long do you plan to keep your system?   We typically lease all major 
equipment purchases for two to three years. We currently have a 31-month lease 
that expires in 2004. We are planning to either floor sweep and upgrade to the 
newest generation hardware platform or extend the lease and add 50% more 
capacity in nodes and disk drives.  What do you believe is the system’s life 
expectancy?  The company typically leases technology based solutions for three 
years and replaces them with new technology.  
 
11. Would you consider purchasing a used Teradata system? No. 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 48 
Page 48 
 
12. If so, what would be your criteria for evaluating such a system?  What would you 
want to know about its previous history? 
 
13. Do you have a services contract from NCR for your Teradata system?  Yes, 
Business Critical ESS If so, how important is the contract to your ongoing 
activities? Could not run those aspects of our business that depend on Teradata 
without NCR Customer Service supporting our maintenance needs. 
 
14. What is the typical availability of your Teradata system?   99.96 % up time. What 
is the amount of downtime experienced? 0.04 annually . 
 
15. How critical is the Teradata system to the ongoing operations/success of your 
business? We classify our Teradata systems as mission critical but could survive 
if it were down for short time periods of a day or two but anything longer than 
that would impact our ability to deliver products to stores as forecasted.  
 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 49 
Page 49 
 
 
Customer #5 
 
 
1. Name: Confidential 
2. Title 
 
3. Company: Major Mall-based Department Store Retailer in US 
 
4. Company Size and Industry: 2003 Rev $ 41.3 B, GMS Department Store, 1,400 
locations 
 
5. Please describe your involvement/experience with your Teradata system. Using 
Teradata since 1994 with the purchase of a DBC 1012. Original purchase to 
interrogate weekly sales transactions for sales and inventory analysis. System and 
dependency on system has expanded since 1994 to a corporate use servicing over 
5,000 persons. 
 
6. How big is your current system?  44 Nodes, 69 Terabytes How long has it been in 
place? Since 1994  
 
7. Have you upgraded your Teradata system since initial installation? Yes. The 
company has gone through multiple upgrades due to increasing business demands 
along with technology and Teradata DB advancements. DBC 1012-3600-5100-
5255-5350. 
 
8. Please describe the application portfolio currently on your Teradata system. 
Teradata supports the daily operation of the company’s primary merchandising 
and marketing departments. Daily sales data is analyzed for local store assortment 
planning, promotional analysis and sales/inventory analysis. 
 
9. Please describe any future applications that you plan to deploy on your Teradata 
system. The company plans to deploy Teradata CRM application to expand on its 
existing marketing capabilities. Fraud and HR applications are also under 
consideration for 2004. 
 
10. How long do you plan to keep your system?   Three years due to lease expiration 
and then a new Teradata complex will be purchased. What do you believe is the 
system’s life expectancy?  The company typically leases technology based 
solutions for three years and replaces them with new technology. If the client 
were to purchase, the equipment the shelf life would be 1.5 to 2 years before trade 
out would occur. The client tries to stay as current as possible with technology 
advancements. 
 

Initial Draft 
Aberdeen Group/Dewsnup, King & Olsen – Highly Confidential 50 
Page 50 
11. Would you consider purchasing a used Teradata system? Not at this time. The 
client has never purchased used NCR Teradata equipment from Teradata nor the 
open market. 
 
12. If so, what would be your criteria for evaluating such a system?  What would you 
want to know about its previous history? 
 
13. Do you have a services contract from NCR for your Teradata system?  Yes, 
Business Critical ESS If so, how important is the contract to your ongoing 
activities? Could not run those aspects of our business that depend on Teradata 
without NCR Customer Service supporting our maintenance needs. 
 
14. What is the typical availability of your Teradata system?   99.994 % up time 
annually at this time. What is the amount of downtime experienced? .006 annually 
which includes both planned and unplanned downtime. 
 
15. How critical is the Teradata system to the ongoing operations/success of your 
business? The client does not classify Teradata as a tier one mission critical 
system on a scale of 1 – 5. They classify Teradata as a four. If down it would 
impact their ability to do business but not drastically impact servicing their 
shoppers but if a prolonged outage would occur it would eventually impact 
customer service levels do to impact on store assortment and replenishment. .  
 
 
 
 
 
 
 
 
 
 
