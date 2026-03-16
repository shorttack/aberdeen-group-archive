# Emerging Technologies: Assessing Strategic Benefits

**Source:** 1996 Sequent.pptx
**Study ID:** 1996-sequent-38f0b1
**Author:** Peter S. Kastner, Group Vice President, Aberdeen Group, Inc.
**Date:** May 1996
**Conference:** Vision 2000

---

## Original Text

```
Emerging Technologies:Assessing Strategic Benefits
Vision 2000 - May 1996

Peter S. Kastner
Group Vice President
Aberdeen Group, Inc.
One Boston Place
Boston, MA 02108
Tel: 617/723/7890  Fax: 617/723/7897   www.aberdeen.com
Copyright Aberdeen Group - 1996






Agenda
Technology equals productivity
Business change is driving computer architecture change
Issues in traditional computer architectures
... and solutions
Aberdeen Group’s conclusions
The IT Decision Maker View:Technology = Productivity
Lower the cost and increase the speed of internal processes
Increase revenue per employee
Create the infrastructure for capturing unforeseen revenue-generating opportunities
Provide global-competitive advantage

The superior use of technology will lead to superior corporate returns and more effective government 
Lower Enterprise Overhead Costs
Typical Company Income Statement
100%  Total Revenue
 55%   Cost of Goods Sold (COGS)
 35%   Selling, General, & Administrative (SG&A)
   3%    IS (part of SG&A)
 10%   Profit Before Tax (PBT)

Options: Direct IS to lower:
SG&A by 20%:   	70% PBT improvement
COGS by 5%:     	27% PBT improvement
IS by 50%:       	15% PBT improvement


Lower EnterpriseOverhead Costs
Fewer customer-supplier relationships
More revenues from existing customers
New customer capture tactics
And after enterprises achieve the 
initial 20% SG&A overhead reduction, 
the cycle starts again!

End User’s New Job Process
Decide
Analyze
Transact
Report



End User’s New Job Process:Information Flow


DSS
Brain
OLTP & Workflow
Messaging



End-User View of Client-Server
Workgroup Server or Router
Departmental/
Other Workgroup
Servers
Fat Clientsor Web Browsers
Enterprise Databases

The
WEB
User curtain

Aberdeen’s Four-Level Information Infrastructure
Level 4: IS Enterprise Operations
Level 3: OLTP
Level 2: Workgroup
Level 1: Client
Data consolidation, batch processing,
data warehouse, systems management
Business process logic, departmental
databases, enterprise networking
Network operating system, decision support,
workflow mgt.., OLTP-lite applications
Graphical user interface, integrated office
suites, data access tools, knowledge-based
communications


3-Tier Application Example:Insurance Claims

Unix or NT cluster
Highly Parallel, Scaleable
8,000 users at 50 offices and headquarters
Local transaction processing against a replicated database
OLTP ProductionSystem &Administration
Data Warehouse
PC desktops and Intel/Risc Office server
Economical, Scaleable


3-Tier Application Example:Information Flow

Data Warehouse Transformation & Replication
Classic 2-Tier Client-Server
Transaction Pull
Replication to every office
Transaction Push
Database of RecordEnterprise Superserver
Application Implications
Aberdeen projects 3x-5x increases in demand for information resources over next 5 years
There is no time for application downtime -- the computer system is the business
Capacity plans for new make-the-money applications exceed traditional mainframe capacities -- by a long shot 
Huge advantages to an IS Buy vs. Make
And the complexity of distributed computing must be hidden by IT to keep costs and manageability under control
Building an Enterprise Superserver


Planning for Technology in 2001
10x-15x more client and server CPU horsepower
Cheap, infinite network bandwidth with ATM
Cheap, infinite managed storage
Radically new voice, text, document recognition
Nearly intelligent system software
But, like 1996, the information highway will still be under construction!
Symmetric Multiprocessors
Multiple CPUs share common data highway (bus), memory and operating system
Examples: Sequent Symmetry, HP 9000, IBM ES/9000, many more
Well understood technology.  New chip-set accelerators. Inexpensive engineering.
Issue is Scaleability: 
Good to 4 processors; fair to 8; few do more than 10 well
Sequent does very well!


Software
Hardware
OperatingSystemTask1
Task2Task3Task4Task n ...



Memory access isa big problemgetting worse
Memory & I/O
Processors
Clusters
Multiple, independent computing nodes cooperate via messages
Each node can be a uniprocessor or SMP
Most common use is for high availability; second is resource sharing
Examples: Digital VAXcluster, IBM SP2 & ES/9000 Sysplex
Traditional Issues: 
Message-passing resource expense
Data shipping
Message Bus
Node 1
Node 2
Node 4
OSTasks...
Cluster Reality:Software Bottlenecks
Today's system software and customer applications are not cluster-enabled.  Require re-engineering to work in a cluster and may not scale well unless carefully architected
Example: Oracle Parallel Server, IBM ES/9000 Sysplex
Implication:  Must wait for special versions
Message-passing burns up CPU and memory cycles
Messaging between nodes is a very complex technology. Requires time to mature.
Sequent’s Next-Generation Technology
Builds on Intel’s highly competitive, highly economical microprocessors and SMP building-blocks
Is aimed at the world’s toughest commercial computing problems
On-line Transaction Processing
Complex decision support
Messaging
Has engineering elegance in delivering
Scaleability with minimal overhead
No application software changes
Will be a benchmark for high-end commercial computing leadership into the 21st century
Summary Observations
Enterprises are being harshly driven to cut SG&A costs while raising productivity
New, multi-tier application architectures demand a new breed of “enterprise superservers” for OLTP, DSS, & messaging
Traditional SMP and cluster implementations are ill-suited to efficient scaleability
Sequent’s NUMA-Q technology will extend the Intel-standard to well beyond even traditional mainframes -- while preserving software investments
Customers will surely benefit


AberdeenGroupCharting the Course
```

---

## Frictionless Data Package Metadata Appendix

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1996-sequent-38f0b1 |
| title | Emerging Technologies: Assessing Strategic Benefits |
| author | Peter S. Kastner |
| date | 1996-05-01 |
| type | presentation |
| subject_domain | enterprise-computing |
| methodology | industry-analysis, benchmarking |
| source_file | 1996 Sequent.pptx |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group presentation for the Vision 2000 conference (May 1996) analyzing
enterprise superserver architectures. The study compares symmetric multiprocessing
(SMP), clustering, and Sequent's emerging NUMA-Q technology, arguing that NUMA will
extend Intel-standard computing beyond traditional mainframe capabilities while
preserving software investments. Covers the business case for enterprise IT investment,
multi-tier application architectures, and technology planning through 2001.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| Importance | high | Early Aberdeen analysis of NUMA architecture vs SMP and clusters; Sequent was a pioneer whose approach proved architecturally prescient for modern multi-socket servers. |
| Relevance | medium | NUMA concepts remain foundational in modern server architecture; specific vendor and product details are dated but the architectural principles endure. |
| Prescience | high | Predicted that NUMA-Q would extend Intel-standard computing beyond mainframes while preserving software investments; this vision was validated as x86 NUMA servers replaced proprietary mainframes. |

### Prescience Detail

The presentation's core prediction -- that NUMA architecture built on Intel-standard
processors would extend enterprise computing beyond traditional mainframes while
preserving software investments -- was remarkably prescient. Key validations:

1. **Sequent acquired by IBM (1999):** IBM paid ~$810M for Sequent, integrating NUMA
   expertise into its x86 server line, confirming the technology's strategic value.
2. **NUMA became standard (2003+):** AMD Opteron and Intel Xeon adopted NUMA as the
   standard architecture for multi-socket servers, exactly as predicted.
3. **x86 displaced mainframes (2000s):** Intel-standard servers with NUMA architecture
   progressively replaced proprietary Unix and mainframe systems for enterprise workloads.
4. **Software transparency achieved:** Modern NUMA-aware operating systems (Linux, Windows)
   handle NUMA transparently, validating the "no application changes" promise.

The ATM networking prediction (cheap infinite bandwidth) was not validated; Gigabit
Ethernet prevailed instead. The "information highway still under construction" observation
proved enduringly accurate.

### Entities

| entity_id | entity_name | entity_type | status | successor |
|-----------|-------------|-------------|--------|-----------|
| sequent-computer | Sequent Computer Systems | vendor | acquired | IBM |
| aberdeen-group | Aberdeen Group | analyst-firm | acquired | Spiceworks Ziff Davis |
| ibm | IBM | vendor | active | |
| intel | Intel | vendor | active | |
| digital-equipment | Digital Equipment Corporation | vendor | acquired | Compaq (then HP) |
| hp | Hewlett-Packard | vendor | active | |
| oracle | Oracle | vendor | active | |

### Technologies

| tech_id | tech_name | category | lifecycle_at_study | lifecycle_current |
|---------|-----------|----------|-------------------|------------------|
| numa-q | Sequent NUMA-Q | server-architecture | emerging | legacy-influential |
| smp | Symmetric Multiprocessing | server-architecture | mature | mature |
| clustering | Clustering | server-architecture | growth | mature |
| intel-x86 | Intel x86 Processors | processor | growth | mature |
| vaxcluster | Digital VAXcluster | clustering | mature | obsolete |
| ibm-sp2 | IBM SP2 | parallel-computing | growth | obsolete |
| ibm-es9000-sysplex | IBM ES/9000 Sysplex | mainframe-clustering | mature | evolved |
| oltp | Online Transaction Processing | workload-type | mature | mature |
| dss | Decision Support Systems | workload-type | growth | evolved |
| atm-networking | ATM Networking | networking | emerging | obsolete |

### Observation Summary

- **Total observations:** 35
- **Observation types:** strategy-classification (4), technology-assessment (7), viability-prediction (5), framework-factor (3), market-data (3), benchmark-result (2), expert-opinion (4), actual-outcome (5)
- **Confidence distribution:** high (22), medium (3), low (1), verified (5)
- **Methodology codes:** industry-analysis (27), benchmarking (2), document-review (5)
