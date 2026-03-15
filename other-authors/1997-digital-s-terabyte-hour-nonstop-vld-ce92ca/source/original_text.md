# Original Document

The Wayback Machine - https://web.archive.org/web/19970604112203/http://www.aberdeen.com:80/secure/viewpnts/1997/v10n7/body.htm
AberdeenGroup
Volume 10 / Number 7
May 20, 1997
Digital’s Terabyte/Hour NonStop VLDB:
Consider The Possibilities
Backup/restore technology is the Rodney Dangerﬁeld of the computer industry:
it gets no respect. What’s more, database designers view system backup as a
major barrier to scaling database size to meet users’ demands for ever-greater
amounts of information.
All this is about to change. Digital Equipment has just announced a quantum
leap in backup/-restore performance, under the title of NonStop VLDB. This
should not only ensure that backup/restore will not be a data-scalability barrier
in the foreseeable future; it will give system designers and administrators a new
weapon in their arsenals, for such uses as rapid database reorganization for
greater data-architecture ﬂexibility. Backup/restore is going to go strategic.
Executive Summary
Backup and restore functions – the necessary housekeeping chores that insure
against database disaster – pervade the computer industry. However, until now
suppliers have regarded them as infrastructure commodity items, and IS has
seen them as a major component of administrative cost overhead – to back up
and restore a database, the administrator must often take it ofﬂine, costing users
valuable production time. The major backup/restore technology advance of the
last 10 years – parallelized online backup and restore – has extended the
scalability of database size by deferring the point at which backup/restore
crowds out processing; but backup/restore remains a bottleneck.
What could the IS buyer do with an order-of-magnitude – or two –
backup/restore speedup? We are about to ﬁnd out: Digital Equipment Corp.
now has a solution called NonStop VLDB that consistently delivers 400-500
gigabytes per hour backup and restore in tests – and should be able to scale to
one terabyte per hour in many situations.
Aberdeen research shows that this quantum leap in backup/restore speed can
have powerful bottom-line effects on the typical IS department and enterprise,
at three levels:
eliminating the major bottleneck and cost effects of today’s
backup/restore;
expanding the ways in which IS can apply backup/restore to other
common IS tasks, such as reconﬁguration, data movement, or upgrade –
thus improving these increasingly strategic IS functions; and
enlarging IS’ and the enterprise’s strategic toolset, by giving architecture
designers the option of inserting backup/restore software and hardware at
key points in the architecture to reduce or eliminate bottlenecks.
Backup/restore speed can be particularly effective in business-critical
applications, such as application servers, data-warehousing backup and
download, "disaster tolerance", or back ofﬁce processing – the heartbeat of the
enterprise.
Since Digital’s solution works well with major RDBMSs and operating
systems, migrating to NonStop VLDB from older solutions should be relatively
painless if not plug-and-play in most situations. Digital offers not only the
software and hardware necessary but also a well-regarded service arm, aimed at
placing backup/restore at the right spot in the enterprise’s architecture for
maximum effect.
Digital presently stands alone in delivering such a backup/restore solution.
Moreover, Aberdeen ﬁnds that scaling backup/restore by an order of magnitude
over the state of the art requires not only fast hardware and long backup/-
restore software experience, but also careful rethinking of the software, the
operating system, and the underlying communications paths – meaning that
Digital should have at least a ½ to 1 year lead over most if not all other
suppliers.
What should IS do with this opportunity? We urge them not only to refurbish
their present backup/restore software, but also to consider the possibilities. IS
should identify and seize the opportunities to ratchet up their architectures’
scalability and ﬂexibility, dramatically, by surgical use of this powerful new
tool.

User Problem: The Backup/Restore Drag
Backup is, plain and simple, the process of copying the contents of a database
at a given point in time to permanent storage (typically tape); and restore is
copying such a stored database "state" back onto the database. RDBMSs are the
most frequent users of backup/restore technology, because if a database crash
causes data to become inconsistent and partial ﬁxes fail, restoring a database to
a previous state (that was captured by a previous backup) ensures that at least
some of the ongoing changes in the database do not have to be painfully re-
created and redone. For the same reasons, backup/restore is used to back up ﬁle
systems on most computers, including mainframe hosts, servers, and even
desktops.
Backup/restore technology is a necessary part of any robust data-management
solution; but as the size of the database scales in the real world, backup/restore
becomes a major drag on the system. Backup/restore can cause:
signiﬁcant administrative costs. Administrators must often perform and
monitor night-long and weekend-long backups – a major component of
overall administrative labor costs.
substantial decreases in system availability. To carry out night-long and
weekend-long backups, administrators typically must bring down the
system while the backup is occurring. Online backup/restore allows users
to keep the system running during backup in some cases, but takes up a
major chunk of the system’s processing power, slowing end-user queries
and updates.
long business-impacting downtimes after crashes. Restoring the previous
state of today’s 30-gigabytes-and-up databases with 10-gigabytes-per-hour
restore can cause major delays in the ability to keep business-critical
systems running, or require expensive fault tolerant technology to avoid.
Ongoing decreases in system performance. As data is added and deleted,
data storage on disk becomes fragmented to the point where a data access
can take 2-10 times longer than when related data was stored together – a
process of sclerosis not unlike fatty-deposit buildup leading to a heart
attack. The cure is database reorganization: backing up the database to
tape, then restoring it in an optimized form to disk. But where
backup/restore takes too long, most users don’t want to incur the cost and
time or reorganization – so system performance keeps getting slower and
slower.
Upper limits to database size. If the time it takes to back up a database of
a given size is more than a night or weekend, most enterprises will not use
the system. Thus, today’s 10-gigabytes-per-hour systems often run into
trouble when the data to be backed up is greater than 40-200 gigabytes,
depending on the frequency of updates. Aberdeen ﬁnds that backup/restore
lack of speed continues to be a major barrier to user needs for increased
database size, for OLTP, decision support/data warehousing, and
application-server data.
Meeting The Challenge: Super-Fast
Backup/Restore
Digital Equipment Corp. is now making available the ﬁrst example (NonStop
VLDB) of a new technology: super-fast backup/restore. By carefully tailoring
all parts of a data management system – data-management software, operating
system, communications paths, CPU, tape systems, and the backup/restore
software itself – this technology eliminates most if not all bottlenecks to the
maximum ﬂow of data down to or up from tape. The result is a speedup of one
or even two orders of magnitude in back-up/restore rates over today’s typical
backup/re-store solution: a revolutionary change.
Consider the effects on backup/restore drag:
administrative costs become insigniﬁcant. A conservative 20-fold
backup/restore speedup shrinks a night-long backup to ½ hour, a 2-day
weekend backup to less than 3 hours.
system availability is close to optimal. For the 95% or more of databases
under 100 gigabytes in size, restoring from a previous backup can take
less than 20 minutes – less time in some cases than failover. Digital’s tests
show that at a 400-gigabyte-per-hour rate, backup/restore takes much less
than 30% of the processing power available – ensuring that online backup
of most databases causes minimal system overhead.
downtime after crashes is minimal – it can be less than 20 minutes in most
cases, as noted above.
reorganization becomes cost-effective, so database sclerosis never occurs.
Since administrative costs and effects on system availability are minimal,
users can now afford to reorganize databases frequently, lengthening the
lifespan and increasing the user-friendliness of legacy mission-critical
systems.
upper limits to the size of all of today’s databases are removed. Even the
largest of today’s databases are less than 10 terabytes; and those are data
warehouses that have few updates and therefore require less frequent
backup. At a terabyte per hour, the new backup/restore technology can
back up or restore even these in a night.

New Places To Use Backup/Restore
Not only does the new super-fast backup/restore technology eliminate the
major bottleneck and cost effects of today’s backup/restore; it also expands the
ways in which IS can apply backup/re-store to other common IS tasks, such as
reconﬁguration, data movement, or upgrade. Moreover, such a backup/restore
speedup can enlarge IS’ and the enterprise’s strategic toolset, by giving
architecture designers the option of inserting backup/re-store software and
hardware at key points in the architecture to reduce or eliminate bottlenecks.
Aberdeen ﬁnds that super-fast backup/restore can yield added value especially
in the following ways:
Fast reconﬁguration for database redesign. Although databases can
evolve with changing user needs to a certain extent by changing the data
dictionary, large-scale database-design changes are often blocked by the
complexity, cost, and ofﬂine time required to redesign the database. Super-
fast backup/restore takes cost and time out of the equation. This allows
users to "push the envelope" and make more major database-design
changes.
Rolling online backup or download for very large databases. Super-fast
backup/restore allows the very large database administrator to back up
OLTP databases online, e.g., by backing up 100-gigabyte sub-databases in
turn ("rolling backup"). Moreover, the restore operation is essentially the
same as the "load" operation that data warehouses and data marts perform
to import new data streams from OLTP databases. Thus, if the data-
warehouse server can take advantage of backup/re-store technology, users
can "refresh" the database with many more new data points, much more
frequently – yielding broader and more timely information.
Data migration. An increasingly strategic challenge for IS – at any level –
is to move data. At the enterprise level, business competitive-advantage
strategies lead to "acquire it, communicate it, employ it" database
architectures. These, in turn, require ever-faster merging of ever-larger
incoming data streams and ever-greater integration of ever-proliferating
data "archipelagoes". At the production level, IS is ﬁnding that per-project
data migration – e.g., moving data from the mainframe to new servers,
linking a data warehouse to legacy OLTP, or feeding workgroup/desk-
top/remote data into corporate systems – is occurring more and more
frequently and leading to recurring maintenance-type data
reconﬁgurations. Using super-fast backup/restore to move data avoids
migration downtime. By combining backup/restore technology with data-
migration software, users can create a "migration server" that speeds the
migration process and isolates any translation needed, allowing
prototyping and testing during the process.
"Disaster tolerance". Super-fast backup/-restore changes the economics of
disaster recovery. Where many sites now pass all transactions to a remote
site that mimics each server or host – at a very high cost in added
hardware – users now have the option of periodically backing up systems
to a remote tape bank. While this does not capture all transactions up to
the second, online backup/restore speed plus today’s communication
speeds can keep gap between the remote data and the local system to 1-10
minutes in most cases – a much more inexpensive "good enough" solution.
This approach can be used for insurance against various types of disasters
– not only earthquake or ﬁre but also checking for viruses.
And super-fast backup/restore has even more global implications for IS
strategists, giving them new ﬂexibility in designing the enterprise’s
architecture:
With scalability limits removed, databases – OLTP, decision-support,
application-server, or Web – can become larger;
With more frequent backup possible, users can more allow more OLTP in
their data warehouses and data marts; and
users can cost-effectively and ﬂexibly rede-sign their "backup
architecture", e.g., by streaming multiple backups to a central server.
Business Beneﬁts Of The New Backup/Restore
Technology
By removing backup/restore drag and giving IS new options, super-fast
backup/restore technology can have a powerful impact on a business’s bottom
line:
It reduces administrative costs, a substantial part of the typical IS budget;
It dramatically increases scalability of business-critical data-management
systems and data-intensive applications;
It gives IS strategists and designers more architectural ﬂexibility;
It cost-effectively increases system robustness, providing alternatives to
costly solutions such as fault tolerance, failover, and disaster recovery.

Often, it improves system performance substantially, by decreasing
online-backup overhead and avoiding database sclerosis.
Digital’s Backup/Restore Technology
Digital Equipment Corp.’s new NonStop VLDB backup/restore solution
includes a Digital AlphaServer conﬁgured and tuned for backup/re-store as
server hardware and high-end Unix or cost-effective Windows NT for operating
systems. SCH Technologies, Open Vision, Spectralogic, Cheyenne, and Legato
backup software have been tested with the Digital solution. NonStop VLDB
works with major RDBMSs – e.g., Oracle, Informix, Sybase, and Microsoft
SQL Server – as well as applications – e.g., SAP. NonStop VLDB also works
with major suppliers’ tape drives, including the ability to reuse mainframe tape
silos.
Digital couples NonStop VLDB with Digital’s service offering – well-regarded
for its distributed-system and networking support – for installation,
conﬁguration, and maintenance.
Digital achieves such a large backup/restore speedup partly by using its own
fast hardware and I/O communications paths, partly by tuning major system
bottlenecks such as the operating system and disk storage patterns, partly by
upgrading system features such as I/O load balancing, and partly by careful
integration with backup/restore and data-management software. A typical high-
performance conﬁguration (used in benchmarking) might include a Digital
AlphaServer 8400 (Turbo laser) server with 8 Alpha CPUs, 8 gigabytes of
system memory, a TLIOP I/O channel with 4 PCI buses, 30 SCSI controllers,
and 16 tape drives, plus backup/re-store software and RDBMS or packaged
application.
Real-life test results from benchmarking NonStop VLDB are dramatic. All four
of the backup/restore suppliers – as well as SAP R/3 –report backup results in
the 400-750 gigabyte per hour range. Percentage of CPU utilized (3 to 16% in
some tests) is low enough that some suppliers estimate that by adding 1-2
TLIOP channels and additional tape drives they can achieve 1.5 terabytes per
hour at maximum CPU load.
Where Backup/Restore Technology Can Be Most
Effective
As we have argued above, the new backup/re-store technology can give a boost
to every major application in the enterprise. For maximum effect, the IS buyer
should consider applying the new technology ﬁrst to the following key areas:
enterprise backup and restore, and related business-critical back-ofﬁce
processing;
data warehousing; and
particularly rapidly scaling new solutions such as competitive-advantage
application servers and Web servers.
Enterprise backup and restore. Rather than picking off targets of opportunity
one by one, the IS buyer should consider zeroing in on the heart of the
enterprise’s use of backup and restore: the data center and corporate computing.
Simply by adding a backup/restore server to these business-critical sites, the IS
manager can get the biggest bang for the buck in terms of improved scalability
and robustness and decreased administrative costs, and thereby impact on the
bottom line. A related tactic is to focus in on mission-critical back-ofﬁce
processing such as accounting and budgeting – often but not always at the same
sites – and implement super-fast backup and restore there.
Data warehousing. Here, backup/restore offers two major opportunities: more
frequent download for more timely information, and the ability to add more
OLTP-style updates to the data mart or data warehouse, leavening the bulk of
day-old or week-old information with key time-critical data and lessening the
need for complicated OLTP-database downloads.
Rapidly-scaling new solutions. Applying super-fast backup/restore to fast-
growing major packaged applications can give them signiﬁcantly enhanced
scalability "elbow room" and availability, since these depend on medium-scale
to large-scale databases. Likewise, Web servers have in some cases been
scaling dramatically in database size and numbers of end users over the last
year. Web-server backup/restore can help meet these scalability demands, and
perhaps provide a less-costly alternative to failover or fault tolerance for
keeping the Web site available worldwide at all hours.
Security. Viruses and attacks on corporate computer systems not only require
signiﬁcant corporate expenditures but also system overhead for virus-checking
and ﬁrewall software.
A backup/restore solution that allows users to undo the pervasive of effects of a
security breach by restoring the state of the system immediately before the

attack gives IS new options for more cost-effective "security disaster
tolerance".
The Competition
Aberdeen predicts that few if any other suppliers will come within hailing
distance of Digital NonStop VLDB’s speed in the next ½ to 1½ years.
There are two major roadblocks to entry of other backup/restore competitors:
the need for high-performance large-scale hardware, and the necessary process
of tuning the hardware and the rest of the solution (operating system, caching,
etc.) for backup/restore – a process that at minimum should take 6 months.
The ﬁrst entrants into the market after Digital should be other major large-scale
high-performance hardware suppliers – Silicon Graphics, HP, and Sun, for
three. Aberdeen predicts that Intel-based suppliers such as Sequent will provide
solutions a little further in the future, since the process of tuning the system
involves Intel as well as the supplier.
Conclusions
Aberdeen concludes that Digital’s test results show the technology is real; it has
arrived; it can deliver signiﬁcant beneﬁts wherever applied; and it should make
IS buyers think carefully about the possibilities and the strategic potential. One
to two orders of magnitude performance increase is big news in any arena.
Combine this with the fact that the new technology has the potential to end
backup/restore’s role as a major drag on databases, and that the technology
applies to computer systems across the board, and the implications are
profound.
Speciﬁcally, Digital’s quantum leap in backup/restore performance offers IS a
golden opportunity: not only to cost-effectively inject further scalability and
robustness into systems throughout the enterprise, but also to use the
backup/restore technology in new ways – to deliver more time-critical
information to data warehouses, to handle disaster recovery and database
redesign, or to migrate data on an ongoing basis with minimal impact on
production systems. For maximum effect, users can apply super-fast
backup/restore to data centers, corporate computing, and back-ofﬁce business-
critical processing such as accounting systems; to data warehouses and data
marts; and to key large-scale applications and Web servers.
To put it bluntly, the major limitation on the new backup/restore technology is
IS’ willingness to use it. Aberdeen strongly urges IS buyers to prototype and
ponder the architectural implications of Digital NonStop VLDB now, to rethink
past attitudes about backup/restore, and above all to consider the possibilities.
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
For further information on AberdeenGroup's
products and services please contact us at
info@aberdeen.com
This Document is for Electronic Distribution
Only
-- REPRODUCTION PROHIBITED --
Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this
publication are the property of their respective holders. Unless otherwise noted, the entire

contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be
reproduced, stored in a retrieval system, or transmitted in any form or by any means
without prior written consent of the publisher.


---

## Frictionless Data Package Metadata Appendix

*Appended by archival pipeline — not part of original document*

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1997-digital-s-terabyte-hour-nonstop-vld-ce92ca |
| title | Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities |
| author | Aberdeen Group |
| date | May 20, 1997 |
| type | Viewpoint (Aberdeen Group Volume 10, Number 7) |
| subject_domain | Database Storage / Very Large Database Management |
| license | CC-BY-4.0 |
| source_url | https://web.archive.org/web/19970604112203/http://www.aberdeen.com:80/secure/viewpnts/1997/v10n7/body.htm |

### Abstract

Aberdeen Group assessed Digital Equipment Corporation's NonStop VLDB backup/restore solution in May 1997, which delivered 400-750+ GB/hour rates — an order-of-magnitude improvement over 1997's typical 10 GB/hour. Aberdeen predicted this technology would "go strategic," removing backup/restore as a database scaling barrier and enabling novel architectural uses.

### Document Assessment

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 4 | Highly prescient recognition of backup/restore as strategic capability; directly anticipates continuous data protection, SAN replication, and cloud backup strategies. |
| Relevance | 4 | Foundational to understanding evolution from tape-based backup to SAN/cloud data protection; the 'backup goes strategic' thesis is now orthodoxy. |
| Prescience | 4 | Core technical insights proved accurate. The specific DEC product did not survive, but every architectural use case Aberdeen described became real practice. SGI/HP/Sun as first competitors proved wrong; disk-based backup vendors led. |

### Prescience Detail

Aberdeen's core prediction — that backup/restore would "go strategic" and that an order-of-magnitude speedup would enable fundamentally new data management architectures — proved remarkably accurate over the 10-20 year horizon. The five novel applications Aberdeen described in 1997 all became standard practice: (1) Fast database reorganization — now standard via online table reorganization and database maintenance windows; (2) Rolling online backup for VLDB — now standard in cloud data warehouse architectures (Snowflake, BigQuery, Redshift); (3) Data migration servers — now realized as ETL/ELT platforms (Informatica, Talend, dbt); (4) Disaster tolerance via periodic remote backup — now realized as cloud DR (AWS Disaster Recovery, Azure Site Recovery); (5) Security disaster tolerance (restore after breach) — now a core ransomware response strategy. However, the technology vector was wrong: the order-of-magnitude improvement came through disk-based backup (SAN snapshots, EMC Data Domain deduplication) and cloud storage, not through optimized tape/Alpha server configurations. Digital NonStop VLDB was discontinued when Compaq acquired DEC in 1998. Aberdeen's competitive prediction (SGI/HP/Sun as first entrants) also proved incorrect — those vendors did not become fast backup technology leaders; specialist backup software/hardware vendors (Veritas/Symantec, EMC, CommVault) and storage array vendors drove the market.

### Entities Referenced

| entity_id | entity_name | type | status | successor |
|-----------|-------------|------|--------|-----------|
| ENT-S5-001 | Digital Equipment Corporation | Vendor | Acquired | Compaq (1998); HP (2002) |
| ENT-S5-002 | SCH Technologies | Software Partner | Unknown | — |
| ENT-S5-003 | Open Vision Technologies | Software Partner | Acquired | Symantec (1999) |
| ENT-S5-004 | Spectralogic Corporation | Hardware Partner | Active | Continues |
| ENT-S5-005 | Cheyenne Software | Software Partner | Acquired | CA Technologies (1996) |
| ENT-S5-006 | Legato Systems | Software Partner | Acquired | EMC (2003); Dell Technologies |
| ENT-S5-007 | Oracle Corporation | RDBMS Partner | Active | Continues |
| ENT-S5-008 | Informix Software | RDBMS Partner | Acquired | IBM (2001) |
| ENT-S5-009 | Sybase Inc. | RDBMS Partner | Acquired | SAP (2010) |
| ENT-S5-010 | SAP AG | Application Partner | Active | Continues |
| ENT-S5-011 | Silicon Graphics (SGI) | Competitor | Defunct | HPE (2016) |
| ENT-S5-012 | Hewlett-Packard | Competitor | Active (HPE) | HPE (2015) |
| ENT-S5-013 | Sun Microsystems | Competitor | Acquired | Oracle (2010) |

### Technologies Referenced

| tech_id | tech_name | era | lifecycle_at_study | lifecycle_current |
|---------|-----------|-----|--------------------|-------------------|
| TECH-S5-001 | NonStop VLDB | 1997 | Emerging | Defunct |
| TECH-S5-002 | AlphaServer 8400 | 1994–1998 | Mature | Obsolete |
| TECH-S5-003 | TLIOP I/O Channel | 1996–1998 | Mature | Obsolete |
| TECH-S5-004 | Parallelized Online Backup | 1990s | Mature | Succeeded |
| TECH-S5-005 | SAP R/3 | 1992–2004 | Growth | Succeeded (S/4HANA) |
| TECH-S5-006 | Legato NetWorker | 1990s | Growth | Active (Dell EMC) |
| TECH-S5-007 | ARCserve | 1990s | Growth | Active (Arcserve) |
| TECH-S5-008 | Digital Unix (Tru64) | 1993–2004 | Mature | Legacy |
| TECH-S5-009 | Data Deduplication | 2000s | Not yet | Active |
| TECH-S5-010 | Cloud Backup | 2008+ | Not yet | Active |

### Observation Summary

30 observations: 3 benchmark-result, 3 market-data, 4 technology-assessment, 5 framework-factor, 2 strategy-classification, 1 expert-opinion, 5 viability-prediction, 7 actual-outcome.

**Key Predictions and Outcomes:**

1. *Backup/restore going strategic* → Confirmed. Cloud backup, CDP, DR-as-a-service are core enterprise architecture.
2. *Database size limits removed* → Confirmed. Multi-petabyte databases are now commonplace in cloud warehouses.
3. *Fast database reorganization* → Confirmed via online DDL, cloud-native storage separation.
4. *Cost-effective disaster tolerance* → Confirmed via cloud DR (AWS, Azure, GCP).
5. *SGI as first competitor entrant* → Incorrect. Disk-based backup specialists led; SGI went bankrupt.
6. *Digital maintaining technology lead* → Moot. DEC acquired by Compaq 1998.
