The Wayback Machine - https://web.archive.org/web/19971210211635/http://www.aberdeen.com:80/secure/profiles/1997/oracle8/body.htm 

**==> picture [240 x 82] intentionally omitted <==**

## _Oracle Corporation_ 

500 Oracle Parkway Redwood Shores, CA 94065 (415) 506-7000 

## Oracle8: The Database For Network Computing 

## Preface 

The rapid adoption of network computing places new demands upon today’s IS databases. Network computing, which leverages the simplicity of thin clients on the desktop, makes information accessible from more types of client devices than ever before. To support the new era of broad information access, databases must provide dramatic increases in power and functionality. 

Network computing will meet the new IS needs and leapfrog the abilities of past mainframe or client-server computing models because of its inherent useability, flexibility and cost-effectiveness. The use of thin software clients reduces or eliminates the requirement for expensive and harder-to-manage PC clients. Users can rely instead on flexible Web-based applications that are supported by a powerful database. 

A database’s ability to support network computing is easily tested. It must support tens of thousands of end users and tens of terabytes of data, regardless of data type; it must conduct any type of processing or data operations extremely fast; and it must be extremely easy to manage in order to reduce cost of ownership. This Profile describes Oracle8, the next generation of Oracle database that is equipped with the functionality to support the new era of database requirements. 

## Executive Summary 

Scheduled for delivery this summer, Oracle8 provides the scalability and power to support any of today’s applications at any scale, while introducing a complete and stable evolution to object-relational technology. 

The foundation relational technology of Oracle8 significantly reduces Oracle customers’ cost of ownership, regardless of scale. Oracle8 can support tens of thousands of users, and has powerful management capabilities for more easily and cost-effectively managing any amount of data, from a few gigabytes to tens of terabytes. And Oracle8’s performance in the areas of queries, transactions, and data operations has been dramatically enhanced. 

Furthermore, Oracle8’s pragmatic, evolutionary approach to object-relational technology can ease the development challenges of sophisticated network computing applications. By supporting existing and new relational data as well as new object data, and providing a mechanism whereby object applications can seamlessly use relational data, Oracle8 provides a relatively easy, safe, and powerful path for customers to move to the new era of object-relational technology. 

Oracle8 is a key component of Oracle’s Network Computing Architecture (NCA), an open, standards-based blueprint aimed at helping users evolve their solutions to support multi-tier, web-based application environments. As part of its NCA effort, Oracle is also recasting its design and development tools (Designer/2000 and Developer/2000) to support applications that only need to be designed and built once, regardless of whether they will be deployed on client-server, distributed object, or Internet enterprise platforms. 

Oracle has subjected Oracle8 to a 10-month beta test that includes nearly 100 partners and over 1000 customers. Initial tests suggest that upgrading from Oracle7 to Oracle8 is relatively fast and simple. Oracle customers can use an upgrade utility that does not require changes to existing data or applications. Oracle has also tested Oracle8’s ability to support application migration by moving Oracle Applications from Oracle 7.3 to Oracle8. Oracle now runs many key internal MIS functions on the Oracle8 beta version, such as E-mail and customer support. 

Aberdeen concludes that Oracle8 is powerful and profound. It sets a new standard for handling an exceptionally broad range of customer needs, whether for small implementations on the Windows NT operating system or for the 

functionality and reliability typical of enterprise database systems. It addresses the new challenges of transaction processing and data warehousing. It brings powerful object technology to the mainstream. And it has done this while heeding the ease-of-use requests made by line-of-business customers. 

## The Key Criteria For Database Buyers 

Aberdeen finds that IS buyers seeking to meet today’s data-management challenges need to focus on three key database characteristics: 

_scalability_ to handle rapid increases in end-user population, database size, and performance needs; 

_flexibility_ to address the need for rapid change; and 

_manageability_ to cut deployment/administration/maintenance costs. 

Oracle8 targets these areas with broad functionality advances, as discussed below. 

## Oracle8 Scalability: More Users, More Data, More Performance 

To achieve scalability, the database must scale in the number of end users, processing speed, and database size. Thus, typical bottlenecks to high-end scalability are limits on the number of end users, processing time per transaction, databases that are poorly organized on disk, and database-size constraints. Oracle8 provides extensive functionality targeted at each of these challenges. 

Oracle 8 includes new, more efficient database connection techniques, such as pooled and multiplexed connections. Oracle8 reduces per-user memory requirements by approximately 50%. Combined, these capabilities provide Oracle8 with the ability to support more than 10,000 end users per node – a dramatic increase. 

In addition to supporting many end users, Oracle8 can support hundreds of terabytes of data – and manage them more effectively. Bulk insert/update/delete operations, key to data warehouse performance, are now fully parallelized. Oracle8 enhances data replication performance by parallelizing it, delivering replication speeds that tests indicate can be an order of magnitude faster. Partitioning, discussed below, improves Oracle8’s capabilities in managing very large databases. 

By reducing the amount of I/O traffic required per transaction, Oracle8 increases its transaction throughput. Likewise, improvements in parallel query operations, including leading-edge-technology integration of parallel query with bitmapped indexing and star joins, provide major increases in decision support query throughput. In fact, Oracle tests suggest that Oracle8 improves performance on a 2.7-million row star query by an order of magnitude over Oracle 7.3, and two orders of magnitude over Oracle 7.0. 

_Partitions for Management and Performance_ . Key to supporting and easily managing large amounts of data is a major new Oracle8 feature: table partitioning. Oracle8 partitioning allows a table to be divided into smaller, more manageable chunks. 

Oracle8 allows users to partition the data for maximum manageability; and once it is partitioned, Oracle8 can process that data with greater speed. When data must be accessed, Oracle8 is "partition-aware," meaning that the access request will travel only to the partition(s) containing that data. And Oracle8 supports parallelism between _and_ within partitions – a major feature that applies all of the scalability benefits of parallelism to a wide range of data storage options. 

Partitioning can speed up queries by confining table scans to appropriate partitions. Partitions also provide a new way to distribute data across I/O devices, helping users to reduce the likelihood of disk "hot spots" where performance bottlenecks occur because data is far more frequently accessed than average. And, very importantly, partitioning reduces down time by confining the effects of a failure to a partition: queries that do not access the damaged partition are unaffected, and the database administrator can recover the partition and rebuild the index in a relatively non-disruptive manner. 

_Messaging for Distributed Computing_ . Aberdeen defines messaging as a set of tools and components that allows developers to use store-and-forward methods to communicate between programs. A messaging product takes a request for service or piece of data sent by one program, forwards it – often via intermediate programs and nodes – and stores it in a queue until a program is asynchronously ready to receive it. 

Because messaging is a key technology for implementing large-scale distributed computing, it is a foundation component for overall system scalability. In enterprise-scale networks, communications are inevitably interrupted or delayed; messaging is the only effective method of handling these problems. Messaging products minimize node-to-node routing times and costs and assure message delivery. Messaging can deliver immediate benefits 

versus today's typical program-to-program communication mechanism: it can add architectural flexibility, robustness, performance, and location independence. 

Oracle8 is taking a leadership role in message-based computing by placing queuing in the database engine. Oracle8 Advanced Queuing significantly reduces the developer and managerial burden of having to deal with the middleware and the database separately. Moreover, putting queuing functionality into the database increases performance for high-volume, message-based applications. 

## Oracle8 Flexibility: Object-Relational Technology 

To allow users to adapt to change more rapidly, today’s database server should deliver support for powerful data models (relational and object-relational). Oracle8’s new object-relational technology provides extensive functionality for data-model support. 

## _The Value of Object-Relational Technology_ 

Object-relational technology allows users to efficiently access complex data types – including functions related to particular data types – and support openextensible user-defined data types. Object-relational technology has frequently been confused with multimedia databases. In fact, multimedia data types have been supported by Oracle7, a relational database, since 1996. The real valueadded of object-relational technology lies not so much in its greater ability to support multimedia data types, but rather in its ability to increase developer productivity through a more powerful data model. 

Oracle8’s object-relational technology allows users to define "business objects" such as an insurance policy, an airline reservation, or even a customer. This object can use both alphanumeric or multimedia data; in fact, the type of data defined within the object is irrelevant. The value, then, of business objects is that they reduce the complexity presented by the increasingly interrelated set of data required for today’s sophisticated applications. By capturing these business semantics in the database, Oracle8 allows developers to focus more on the business application and less on mapping the application to the various places where the data is stored. 

_Pragmatic Object Support_ . Oracle8 users can create, access, combine, and query objects – the operations that pragmatic users need to take advantage of object technology. Oracle8 provides new optimizations for objects, by allowing retrieval of a complex object all at once, by simplified navigational access, by an object cache, and by providing support for complex data types such as multimedia and Large Objects (LOBs). Objects can inherit data and code from other objects, allowing users to develop object-based programs more rapidly. Oracle8 extends PL/SQL so that programmers can use familiar SQL statements to access objects, and supports C/C++ object access, with Java access to be supported in Oracle 8.1. 

Oracle8 users now can create new, more complex data types out of old ones by wrapping the old data type as an object class and "inheriting" its features into a new object class. Oracle8 users can mix and match object classes in many different ways, e.g., by creating a table each of whose rows is an object, creating nested objects, or placing references to other objects in an object. Moreover, IS developers can write "cross domain" queries that navigate across many related object classes or data types. By using Oracle and ISV multimedia "rich objects" as building blocks, Oracle users can now provide customized data types for Internet multimedia, for complex ROLAP queries, and to support a particular application’s complex-data needs. 

_Integration_ . The existing relational technology and the new object-relational technology are fully integrated with Oracle8 (see Figure 1). Oracle8 is an evolution of Oracle 7.3, not a revolution – meaning that upgrade to 8.0 should be relatively straightforward. Oracle 7-based applications work without change in Oracle8. 

Figure 1: Oracle8 Integrates Relational And Object Data 

**==> picture [7 x 8] intentionally omitted <==**

Undisplayed Graphic 

Source: Oracle Corporation, June 1997 

Present customers can use Oracle’s development tools to add new capabilities, or access new types of data using PL/SQL commands. New applications can access relational data using "views" that make that data appear as objects to the 

application. As a result, Oracle8 users can create new applications that use both relational and complex-data objects and continue to run old applications without change. 

## _Flexible Multimedia Support_ 

The need for data-management solutions accessing multimedia data types – in data warehouses, Web pages, or competitive-advantage applications – is exploding. While multimedia data types have been supported with Oracle7, Oracle8 increases the number of multimedia data types that are native in the server, and provides an "extensibility" mechanism for customers or third parties to create their own special-purpose data types or unique kinds of functionality. 

Oracle7 provided native support for alphanumeric data as well as text, spatial, and video. These have been demonstrated in large-scale, real-world customer sites such as Bristol Myers and Pacific Bell. Oracle8 takes this capability further, by combining specific support for these data types with its overall object-relational capabilities. As a result, Oracle8 adds to Oracle7’s ability to support multimedia data by including support for images and time-series data, while also providing an "extensibility" mechanism for developers to create Data Cartridges that support their complex-data needs. 

## _Extensibility_ 

Oracle8 adds extensibility features that give a new dimension to Oracle’s openness story. These include Oracle8’s support for user-defined data types and ISV-/IS-created data cartridges that can access these core-engine functions. Enterprises can write data cartridges that extend Oracle8’s functions, data types, and indexes, then write solutions that invoke these data cartridges, rather than stored procedures that must invoke a narrow range of database functions. 

The key extension to the core engine is a set of programming interfaces that give users access to major RDBMS-engine functionality, including the query optimizer and indexing. Thus, users can further optimize query handling and indexing for higher performance. 

## Oracle8 Manageability 

Oracle8’s new manageability features significantly improve management-tool ease of use, Oracle8 performance, and Oracle8 robustness. 

One new feature for Oracle8 is Server Managed Backup and Recovery. This feature automatically and intelligently performs these data management operations, and maintains an archive of all operations that occur. Oracle8’s Recovery Manager ensures that data management mistakes are more easily and efficiently corrected. 

Partitioning, as noted earlier, is a major source of benefit for Oracle8’s manageability. By allowing tables to be divided flexibly into smaller chunks, partitioning allows large data management and administration tasks to be "divided and conquered" as well, easing IS’ operational challenges. The ability to confine a failure to the affected partition reduces system downtime. 

Oracle8’s Incremental Backup capability allows users to back up only the data that has changed since the last backup. This is a major benefit, especially for very large databases: administrators can significantly reduce "backup window" time by backing up gigabyte partitions rather than terabyte tables. 

System failures are far easier to manage, as well. Oracle8 automatically switches end users over from a failed node to a surviving node. 

## Oracle8 Programmer Productivity Support 

The Oracle Network Computing Architecture is a development framework that includes Oracle products supporting today’s three major environments – clientserver, Internet, and distributed objects – plus new features (Cartridges and an Inter Cartridge Exchange (ICX) mechanism) that integrate these and allow developers to create enterprise-scale applications that span all three. Client, application server, and database server cartridges improve programmer productivity by embedding much programming detail in infrastructure "middleware" code. The Network Computing Architecture incorporates major standards (e.g., Java, CORBA) with open interfaces. 

Oracle8 is a key part of the Network Computing Architecture – and vice versa. Oracle8 is the NCA’s database server component that database-server cartridges can invoke. Oracle8’s extensibility features give the developer exceptionally open, hands-on control over database customization. 

## Where Oracle8 Is Most Effective 

The new object-relational technology in Oracle8, plus other new Oracle offerings such as the Network Computing Architecture, allow IS to apply the Oracle database in new solutions. Oracle8 should allow enterprises to: 

Create new Internet-based competitive-advantage solutions, and 

Scale their OLTP and decision support, extending these with "richer" data. Oracle8 can be particularly effective where IS buyers are trying to scale Intranet architectures to handle data-intensive applications or improve programmer productivity in creating mission-critical solutions. Where users are trying to scale Intranets, Oracle8 combines proven enterprise scalability with support for Web-site multimedia data. By adding the Oracle database’s scalable application-server technology to the Network Computing Architecture, Oracle creates an infrastructure that minimizes the Internet’s communications and Web-server bottlenecks. Oracle8’s ability to support Business Objects allows developers to write at a higher level, allowing them to more rapidly create sophisticated solutions that are not only scalable but also flexible to handle changes that occur at "Internet speed". 

The potential benefits of Oracle8’s new technology in OLTP and data warehousing may be even more significant. For example, Oracle8 scalability features can allow customers to increase the number of end users and database size of present systems dramatically. Object-relational ROLAP extensions that define functions for ranking, profitability, and time series will make development more rapid and high-er quality. Bill-of-materials explosion or economic-order-quantity calculation will become relatively straightforward, and allow much more effective just-in-time resource planning. Video cameras monitoring an assembly line can feed video data into a object-relational database that can detect anomalies such as defects and trigger corrective action, improving product quality at lower cost. 

## Aberdeen Conclusions 

Oracle8 is not yet another example of a supplier chanting an "object-oriented" mantra: it is a straightforward yet elegant evolution of today’s premier enterprise-scale database to new technology with clear real-world benefits. Oracle8 reinfor-ces the Oracle database’s scalability and robustness. Oracle8’s full-featured object-relational technology allows complex-data support for sophisticated applications and promotes greater developer productivity in creating mission-critical solutions. 

In a rapidly changing data-management market, Oracle8 is not the end of the Oracle database’s evolution. For example, Aberdeen anticipates that Oracle will add further features and functions to its object-relational capabilities, will further integrate relational and object data, and will improve object-access performance for particular types of complex data over the next 1-2 years. 

Oracle8 reinforces Oracle’s image as a market leader in product breadth and a real-world-technology leader. IS buyers looking for Oracle to keep them in sync with data management technology should find Oracle8 to be a broad solution to their problems and a solid foundation for customers’ future solutions. 

**==> picture [41 x 48] intentionally omitted <==**

**==> picture [41 x 48] intentionally omitted <==**

**==> picture [40 x 48] intentionally omitted <==**

**==> picture [41 x 48] intentionally omitted <==**

**==> picture [40 x 49] intentionally omitted <==**

**==> picture [42 x 49] intentionally omitted <==**

**==> picture [41 x 49] intentionally omitted <==**

**==> picture [40 x 49] intentionally omitted <==**

Aberdeen _Group_ , Inc. 

_One Boston Place Boston, Massachusetts 02108 USA Tel: 617.723.7890 Fax: 617.723.7897_ 

## Contact Information: 

For further information on Aberdeen _Group_ 's products and services please contact us at info@aberdeen.com 

## This Document is for Electronic Distribution Only -- REPRODUCTION PROHIBITED -- 

Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts 

The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire 

contents of this publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior written consent of the publisher. 

