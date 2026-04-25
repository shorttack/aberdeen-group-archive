# Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)

> Archived from: TP-1-benchmark-guide-Stratus-1983-2.pdf
> Original publication date: 1983
> Author: Stratus Computer engineering (uncredited)

---

## Original Document Text


===== TP-1-benchmark-guide-Stratus-1983-2.txt =====
PERFORMANCE            MEASUREMENT



  THE   "T P - 1" PERFORMANCE MODEL



            Overview

             STRATUS Performance

             STRATUS VS. TANDEM

             Observations

             Future plans
                   OVERVIEW
          THE WTP-1" PERFORMANCE MODEL



Requester/Server model.

     Requester - COBOL/TPF

     Server    - PL/1


Transactions initiated by delay interval. No screen I/o

     or communications.


Servers are duplicated to achieve optimum performance

     on each system.


Various file sizes and types.


Input parameters specify:

     The number of reads and the number of updates for each
     transaction.

     Requester and server loop counts which are used to simulate
     the processing workload of real transactions.

     The number of server queues


File I/O designed to simulate random user access.
                     TP - 1 OVERVIEW (continued)


File parameters


      Small relative file           (20000 records, 150 bytes each)


      Large relative file           (100000 records, 150 bytes each)


      Large index file              (100000 records, 150 bytes each
                                     12 byte key, no duplicates)



      Each server was driven by a different random sequence read
      from a file at the beginning of the test.

      Different random files were used for consecutive tests
      to minimize caching.
          TP - 1 OVERVIEW (continued)


Common parameters used for this comparison:



    Number of terminals/tasks = 8

    Delay interval = 2 seconds

     Read count » 3

    Update count = 2

    Requester loop count » 100

    Server loop count = 200

    Number of requesters = 1

    Number of servers = 2
                      STRATUS PERFORMANCE



Small relative file     (20000 records - 150 bytes each)



   Non-duplexed system with SMB memory


   Non-duplexed 143MB disk


   Results:


        Transaction rate =2.9 trans/sec

        CPU utilization =69%

        Requester CPU utilization = 10%

        Disk I/O rate = 18.0/sec


   Observations:


        Multi-tasking requester used relatively small

              amount of cpu
               STRATUS PERFORMANCE (continued)


Large relative file   (100000 records, 150 bytes each)


    Non-duplexed system with 8MB memory


    Non-duplexed 143MB disk


    Results:


         Transaction rate =2.3 trans/sec

         CPU utilization = 94.7 %

         Disk I/O rate = 21/sec


    Observations:


         Less cache benefits compared to small relative file
                STRATUS PERFORMANCE



Large indexed file


    Non-duplexed system with either 4 or 8MB memory


     Non-duplexed 143MB disk


     Results:


          8MB / 1 server queue / 1 disk:

                Transaction rate =1.5 trans/sec.

                CPU utilization = 81 %

                Disk I/O rate = 17/sec.

                Requester CPU = .06 sec/trans.

                Server CPU = .33 sec/trans.


          8MB / 2 server queues / 1 disk:

                Transaction rate =1.6 trans/sec.

                CPU utilization = 78 %

                Disk I/O rate = 17/sec.

                Requester CPU = .04 sec/trans.

                Server CPU = .33 sec/trans.


          4MB / 2 server queues / 1 disk:

                Transaction rate =1.5 trans/sec.

                CPU utilization = 79 %

                Disk I/O rate = 18/sec

                Requester CPU = .04 sec/trans.

                Server CPU = .34 sec/trans.
                    STRATUS PERFORMANCE   (continued)


Large indexed file (continued)


               4MB / 2 server queues / 2 disks:

                    Transaction rate ■ 1.8 trars/sec

                    CPU utilization ■ 94 %

                    Disk I/O rate ■ 23/sec

                    Server CPU « .35 sec/trans.


               4MB / 2 server queues / 4 servers / 2 disks:

                    Transaction rate ■ 1.7 trans/sec

                    CPU utilization » 98 %

                    Disk I/O rate « 22/sec

                    Server CPU » .35 sec/trans.
             STRATUS PERFORMANCE



o   Overhead in the multi-tasking requestor was minimal.

o   Task metering had no measurable effect.

o   Cache utilization significantly impacts performance.  This
    is obviously application dependent, but significant improvements
    in performance are possible.
o   Stratus performance was most affected by disk issues - the type
    and number of disk accesses and the size of disk files.

o   Performance improved by adding a second disk drive.

o   Processor resource was saturated with two disks doing heavy
    indexed i/o.

o   Small improvement gain by using a second server queue.

o   Multiple server copies can greatly improve performance.            »

o   Process priorities are very important.  Server priority should
    be higher than requestor.  A production application should
    normally run at higher priority than development.  Actual
    priorities may not be obvious because of the scheduler algorithms.

o   Preliminary multi-module recommendations:

         - Use Stratalink for queueing rather than file access.
         - Put queues on the requestor module.
    TANDEM PERFORMANCE TESTS




o   Used identical TP-1 model.

         Same transaction workload.
         Same data file.
         Same record numbers and keys for random access.

o   PATHWAY requestor with TAL server.

o   Checkpointing done at system level (disk i/o) and in
    Pathway (interpreter and monitor processes).

o   Tests used single Tandem cpu.

o   Configuration for relative file tests:

         TNSI cpu with 768KB memory
         mirrored 64MB winchester disks

o   Configuration for indexed file tests:

         TNSII cpu with 2MB memory
         single 540MB winchester disk
    TEST RESULTS USING RELATIVE FILE ( 20,000 RECORDS)




TANDEM:


Transactions/sec                       1.4

Requester cpu time/transaction          .37

Server cpu time/transaction             .18
     (including disk processing)

Disk I/O rate (physical)              15.3




STRATUS:


Transactions/sec                       2.9

Requester cpu time/transaction          .03

Server cpu time/transaction             .15
     (including disk processing)

Disk I/O rate (physical)              18.0
   TEST RESULTS USING INDEXED FILE   ( 100,000 RECORDS)




TANDEM:                               Instructions in requestor loop

                                         50        100         200


Transactions/sec                        1.5       1.4          1.1
Requester cpu time/transaction           .31        .39         .61


Server cpu time/transaction              .20        .20         .20
     (including disk processing)

Disk I/O rate (physical)               22.2      22.0         17.5




STRATUS:

                                     One Disk             Two Disks


Transactions/sec                        1.5                   1.8

Requester cpu time/transaction           .04                   .04

Server cpu time/transaction              .34                   .35
     (including disk processing)

Disk I/O rate (physical)               18.2                  22.6
             STRATUS/TANDEM PERFORMANCE COMPARISON




o       Tandem disk drives are faster than current Stratus winchesters.

o       Comparison looked only at single Tandem cpu and single
        Stratus module.

o       Tandem performance was most sensitive to instruction workload
        of the requestor (Pathway TCP).  This is due to the fact that
        it interprets Screen Cobol and that it is checkpointing.

o       Stratus performance was most sensitive to the disk workload
        of the server.

o       The Tandem indexed file structure is more efficient than that
        of Stratus (at the expense of disk space) when accessing by
        primary key. When accessing by alternate key Tandem essentially
        doubles the time required to retrieve a record, while there is
        no difference between primary and alternate key access on Stratus.
        We did not have enough time to include alternate key access in
        our benchmark as yet.                                            I

o       Tandem offers very little flexibility in design options with
        their Pathway product which eliminates many opportunities for
        performance improvements.  Examples of this include very limited
        data storage, no data sharing between tasks, and the inability
        to do any disk access in the requestor.
    o    Tandem currently does not buffer disk writes in cache; writes
         go immediately to disk.
    o    Tandem does no optimization for sequential disk i/o and performance
         in this area is very poor compared to Stratus.
                future plans




o   Multi-module

o   Stratanet

o   Component (atomic) testing

o   Communications products

o   System measurement and tuning

o   Transaction processing

o   Disk verify

o   Duplex yersus simplex disks

o   File types and sizes

o   File locking types

o   New Stratus products

o   Competitive products when feasible


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | stratus-tp-1-internal-benchmark-guide-19-9b51bf |
| title | Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal) |
| author | Stratus Computer engineering (uncredited) |
| date | 1983 |
| type | internal-engineering-document |
| subject_domain | fault-tolerant-OLTP-benchmarks |
| methodology | Stratus internal performance-measurement document defining the TP-1 model (Requester/Server with COBOL/TPF requester and PL/1 server, transactions initiated by delay interval, no screen I/O, duplicated servers, varied file sizes/types). Reports 1.5-2.9 tps results across small/large relative and indexed file configurations on non-duplexed Stratus systems, then closes with Stratus-vs-Tandem observations. |
| source_file | TP-1-benchmark-guide-Stratus-1983-2.pdf |
| license | CC-BY-4.0 |

### Abstract

Earliest Stratus internal performance document recovered in the corpus. Defines the TP-1 model and walks through small relative file (2.9 tps; 69% CPU; 18.0 disk I/O/sec), large relative file (2.3 tps; 94.7% CPU), and large indexed file configurations (1.5-1.8 tps depending on memory and server-queue topology). Key observations: cache utilization significantly impacts performance; performance is most affected by disk type/number/file size; multiple server copies greatly improve performance; server priority should exceed requester priority. The Stratus-vs-Tandem comparison section sits behind the TP-1 model definition. Predates the FTSN-32/FTSN-33 1985 Stratus 1.0-1.1 tps/CPU figures cited in Batch 25 — TP-1 is essentially Stratus's pre-ET1 internal predecessor benchmark.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | moderate | Earliest Stratus internal benchmark document in the corpus; TP-1 model defines the Requester/Server pattern that underpins all later Stratus benchmark efforts. |
| **Relevance** | moderate | TP-1 is the model PSK 1987-08 TopGun memo critiques relative to Tandem ET1 — bridges 1983 Stratus internal benchmark practice to the 1987 audited-benchmark era. |
| **Prescience** | low | TP-1 was a Stratus-internal model that did not survive the TPC standardization wave; its tps numbers are inputs to the later FTSN/EE-Times 'tps/CPU' industry frame but the model itself was superseded by ET1/TPC-A. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (2)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| Tandem Computers | company | acquired | Compaq (1997), then HP (2002) |

### Technologies Referenced (4)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| TP-1 performance model (Stratus internal) | performance-benchmark | Stratus internal | internal-tool | superseded |
| Stratus VOS (Virtual Operating System) | operating-system | Stratus Computer | shipping | shipping |
| Debit-Credit benchmark (DC/ET1/TP1) | performance-benchmark | industry-standard | industry-standard | superseded-by-tpc-c |
| Fault-tolerant systems architecture (general) | computer-architecture | various | emerging | specialized-niche |

### Observation Summary

- Total observations: 5
- By type: benchmark-result: 3, methodology-observation: 1, performance-tuning-finding: 1
