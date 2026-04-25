# DEC Proposed Debit-Credit Benchmark Guidelines (Kohler/Hsu, Dec 1987)

> Archived from: DECtp-debit-credit-guidelines-1987-12-3.pdf
> Original publication date: 1987-12-21
> Author: Walt Kohler & Yun-Ping Hsu, DEC HPS/OLTP Systems Performance Analysis Group

---

## Original Document Text

From:   HPSRAD::HSU "Yunping Hsu, MRO1-1/A65 DTN:297-6517            21-Dec-1987 1633" 21-
To:.    @DCTESTERS
Subj:   Proposed Debit-Credit Guidelines




         | d | i | g | i 111 a 111   I NTEROFFICE           MEMORANDUM


         TO:     DISTRIBUTION                       DATE:   Dec. 21, 1987
                                                    FROM:   Yunping Hsu
                                                    DEPT:   HPS/OLTP Systems
                                                            Performance
                                                            Analysis Group
                                                    DTN:    297-6517
                                                    LOC:    MR01-1/A65
                                                   ENET:    HYEND::YHSU



         SUBJECT:         Proposed Debit-Credit Benchmark Guidelines

         Attached for your review is a document prepared by HPS/OLTP
         System Performance Group concerning the interpretation and
         implementation guidelines for the Debit-Credit Benchmark.
         Suggestions, questions and discussion are heartily welcome,
         and please forward your comments to the above address. If you
         know of anyone who is not on the distribution list and whom
         you feel should read this document please forward their name
         to us so that we may add the name to the distribution list.
          DECEAT::BHANDARKAR                   !   Dileep Bhandarkare
          SUGAR::MOSES                         !   Bhagyam Moses
          COOKIE::RDOWNS                       !   Rudy Downs
          SQM::MARCONIS                        !   Joe Marconis
          HERON::MARSHALL                      1   Christopher Marshall
          CURIE::SASENA                        I   Jim Sasena
          CURIE: .-HOWELL                      I   Fred Howell
          CURIE::DEMPSEY                       !   Mike Dempsey
          HPS::KASTNER                         !   Peter Kastner
          HYEND::BZAHAVI                       I   Bill Zahavi
          HYEND::WRIGHT                        I   Linda Wright
                   COMPANY          CONFIDENTIAL

                          Proposed Guidelines
                                  for
         Implementing and Reporting the Debit-Credit Benchmark
                                 Walt Kohler
                                 Yun-Ping Hsu
                   OLTP Systems Performance Analysis Group
                           High Performance Systems
                               21 December 1987




1   INTRODUCTION

     Since a description of the Debit-Credit benchmark appeared in a
DATAMATION article in 1985 [Anon85], it has been used as the de-facto
industry standard on-line transaction processing benchmark in spite of
its limitations   [SERLIN86].    As pointed out in a 1986 memo by Vijay
Trehan [TREHAN86], "each group that has implemented the Debit-Credit
benchmark has interpreted the requirements somewhat differently..."
and "seemingly minor differences in interpretation can lead to
significant    differences    in   reported   results   ..."   Tandem's
interpretation of the specification and their benchmark results are
contained in a recent report [TANDEM87].

     This memo summarizes the DATAMATION Debit-Credit         benchmark
specification,     discusses    possible    interpretations     of   the
specification,   and proposes guidelines     for   implementing    valid
interpretations that should achieve the best possible performance.    It
also specifies the minimum data that must be collected and reported to
verify compliance with the benchmark specification and implementation
guidelines.   It is hoped that this will remove, or at least help to
identify,   implementation and testing variations and inconsistencies.
This memo does not attempt to provide guidelines for determining the
capital cost of the system under test.

     In the remainder of this document, the Debit-Credit benchmark is
divided   into   eleven   components    and for each component,     the
specification,   interpretations,    implementation   guidelines,   and
compliance requirements are discussed.   Finally, Appendix A contains a
summary of the compliance information and Appendix B contains a
summary of the performance results that should be reported for each
benchmark test.


2   APPLICATION IMPLEMENTATION LANGUAGE
                                                                           Page 2
APPLICATION IMPLEMENTATION LANGUAGE


       o   Specification:    COBOL is specified.

       o   Interpretations:   Any high level language        that    has      the
           appropriate database system support.
       o   Guidelines:    Any high level language.

       o   Compliance:

            Application Programming Language :




3   TERMINAL COMMUNICATIONS


       O   Specification: Block mode,   e.g    IBM 3270, with a base
           screen of 20 fields.    Ten (10) fields from a base screen of
           twenty (20) are read, mapped by presentation services     and
           then re-mapped and written as part of the reply.     The line
           protocol is X.25.    Figure 1 shows the general view of
           specification.

             BLOCK MODE
             TERMINALS                                               SUT
                                         X.25


                               >   10 fields 100 bytes
                               -             200 bytes
                                                                   DB    MGMT
                                                                  (FORMS MGMT)
                                                                  (TERM MGMT)
                                                                  (COMM)

                            Figure 1:   BENCHMARK SPECIFICATION


       o   Interpretations: The benchmark does not clearly specify the
           roles of X.25 and presentation services.  The general view of
           the benchmark is to emulate an environment with bank tellers
           using interactive terminals, but the functions that should be
           performed by the system under test (SUT)       are not well
           defined.   Although X.25 was specified as the communications
           protocol, other protocols may be used.

       o   Guidelines:  Use block mode terminals where possible.    When
           character mode terminals and DECnet communications are used,
           there are many possible configurations.  For example,  assume
           that terminal management and forms management are done by the
           database hosts and the remote terminals are connected to the
           database hosts through communication networks, as depicted in
           Figure 2 below.
                                                                              Page 3
TERMINAL COMMUNICATIONS



          Branch                                                    Machine
          Offices                                                    Room
         <------- >                                                <------ >

           +---+                                          Response
           I     |                                           Time
           +--- +                                             |      SUT
             o            Communication Networks              V    +----+
             °        ===============------- =============== --- - |     |
              O                                                    4------------- 1-
           +---+         ------ >   10 fields 100 bytes 10 BIOS
           |    |        <------              200 bytes 1 BIO
           +---+
                                                                    DB    MGMT
                                                                    FORMS MGMT
                                                                    TERM MGMT
                                                                    COMM
                     Figure 2:   Character Mode Terminals without FEP's.


              As a second example, assume that terminal management and
         forms management are done by the front-end processors (FEP's)
         that are in the same central machine room with the back-end
         host and the remote terminals are connected to the FEP in the
         central machine room through communication networks,       as
         depicted in Figure 3 below.
                                                                                  Page 4
TERMINAL COMMUNICATIONS




          Branch                                                     Machine
          Offices                                                     Room
         <------- >

         Char. Mode                             Response
         Terminals                                Time


           4-----------t-                                   FEP                DB HOST
             o                 Comm. Networks              +---- +             +—-- +
             o
             o                                           +----+ DECnet         +—-- +
           +--- +                                      FORMS MGMT
                                                       TERM MGMT               DB MGMT
                                                                  ------ >
                   10 fields (100 bytes)                      10 fields ( 100 bytes
                          10 BIOS                                  1 BIO
                             <------                                 <------
                         200 bytes                               200 bytes
                          1 BIO                                    1 BIO


                            Figure 3: Character Mode Terminals with FEP in the
                                      machine room.

              Another possible configuration is assuming that the
         FEP's are remote from the central machine room.     Terminals
         are connected to the FEP through either local area network or
         direct   terminal   lines connections,   and the FEP's are
         connected to the back-end database host through DECent
         networks as depicted in Figure 4 below.     For example, each
         branch office may have a MicroVAX serving the ten character
         mode terminals as a FEP/terminal controller, and there is no
         FEP at the central machine room.
                                                                            Page 5
TERMINAL COMMUNICATIONS




              Branch                                                   Machine
              Offices                                                   Room
          <------------------ >                                      <------- >
                                                          Response
          Char. Mode                                        Time
          Terminals                                           I


            +---+          FEP                               |        DB HOST
              o          +---- +         Comm. Networks      V        +---- +
              o          +---- +     1                                 +---- +
            +---+       FORMS MGMT
            |    |      TERM MGMT            '                         DB MGMT
            +---+
                  ---- >                                      >
               10 fields (100 bytes)                10 fields (100 bytes)
                  10 BIOS                            1 BIO
                  <----                           <------
               200 bytes                         200 bytes
                  1 BIO                             1 BIO

                     Figure 4: Character Mode Terminals with FEP's in the
                               Branch offices.


               When the first configuration is used,   the RTE should
          emulate asynchronous character mode terminals. When FEP's
          are used as the second configuration above,  both the FEP's
          and the back-end database hosts should be considered as
          systems under test (SUT), and the RTE should emulate remote
          terminals as in the case of the first configuration.   If the
          third configuration is assumed then the RTE can emulate the
          FEP's.   However,  if the FEP's are emulated, the transaction
          interarrival time distribution should be adjusted to emulate
          the distribution that would have been generated by terminals
          connected to the FEP.  The 100/200 bytes input/output between
          the terminals and the SUT should be maintained in all
          configurations. When FEP's are used,     the data transfers
          between the FEP's and the database hosts should also be
          100/200 bytes.

      o   Compliance:
          Type of terminal emulated ?
          # of fields entered at each terminal for a transaction ?

          Total # of bytes entered ?
                                                                    Page 6
TERMINAL COMMUNICATIONS


           # of fields returned from the SUT per transaction ?

           Total # of bytes returned ?

           Communication Protocol :

           Include a diagram of the terminal/SUT configuration, describe
           the functions performed by each component (terminal management,
           forms management, database management, etc.), and specify all
           communications protocols used.




4   DATABASE DESCRIPTION, SIZE, AND LOCATION


       o   Specification: The database consists of four record types
           (branch,  teller, account, and history).  Each history record
           is 50 bytes long and the other records are 100 bytes each.
           The key for the account is 10 bytes long but the others may
           be shorter.  For a throughput test of X TPS,    the database
           should contain 10X branch, 100X teller, and 100,000X account
           records. A 90-day history file of 2,000,000X history records
           must also be maintained.  There is no need to duplex the data
           files.
       o   Interpretations:  The accounts belong to branches and the
           tellers belong to branches.   The database may be implemented
           using a hierarchical, network, or relational database system
           or a file system.    Tandem tested two relational systems and
           oversized the database for many tests.        (The oversized
           database   will   reduce lock contention and may improve
           performance.) According to the example in the Datamation
           article,  an X TPS system must store 100,000,000 X bytes of
           history data on-line (2,000,000X records at 50 bytes/record ).
           The cost of the disks used to store the history data must be
           considered when calculating the cost of        the   hardware
           investment, but a smaller history file can be used during the
           benchmark runs.
       o   Guidelines:  Use any database or file system but size the
           database properly.    The number of records and their sizes in
           each database    file    must    conform   to    the   benchmark
           specification, but the physical disk space used for the
           database can be larger than that needed for the      records if
           this   increases   performance.     Furthermore,   the physical
           allocation of the records and files is not part of the
           benchmark   specification,    so    allocations    that improve
           performance are allowed.   For example, the branch and teller
           files can be partitioned into smaller data sets according to
           branch number and the data sets can be managed by different
           hosts in a VAXcluster.
                                                                         Page 7
database description, size, and location

      o    Compliance:

                 Transaction throughput :                TPS

                 Branch :    Record Size                 bytes

                             # of records
                             Access method

                 Teller :    Record Size                 bytes

                             # of records

                             Access method

                 Account :   Record Size                     bytes

                             # of records

                             Access method

                 History :   Record Size                     bytes

                             Space on-line                   bytes

                             Access method




5   TRANSACTION LOGIC

       o   Specification: The transaction      logic   was     defined   by   the
           following pseudo-code:
           Begin-Transaetion
               Read    Message from Terminal    (100 bytes)
               Rewrite Account                  (100 bytes, random)
               Write   History                  (50 bytes, sequential)
               Rewrite Teller                   (100 bytes, random)
               Rewrite Branch                   (100 bytes, random)
               Write   Message to Terminal      (200 bytes)
           Commit-Transaction

       o   interpretations:   The actual terminal I/Os need not be
           handled   within   the   transaction.    A   more reasonable
           specification with the terminal I/O moved outside        the
           transaction is given below in an SQL-like pseudo code:
                                                                      Page 8
TRANSACTION LOGIC



           Read      Message from Terminal; (100 bytes)
           Perform Presentation Services Giving Account_Number,
                                  Teller_Number, Branch_Number , Delta;
           Begin-Transaetion;
             Update Account
                Set balance = balance + :Delta
                Where account_number = :Account_Number;
             Insert Into History Values
                ( Timestamp,Account_Number,Teller_Number ,Branch_Number ,
                  Delta);
             Update Teller
                Set balance = balance + :Delta
                Where teller_number =     :Teller_Number
             Update Branch
                Set balance = balance + :Delta
                Where branch_number =     :Branch_Number
           Commit-Transaction;
           Perform Presentation Services;
           Write     Message to Terminal;    (200 bytes)

                Tandem used a similar      approach,   but   their   SQL
           transaction specification [TANDEM87]    reordered some of the
           steps:  the History file update is performed after the Branch
           update and the presentation services are performed before the
           Commit.

      o    Guidelines:  Choose a functionally equivalent structure that
           maximizes TPS performance.  The best ordering of updates will
           depend on how the database is implemented and how the locks
           are controlled.  The balance fields in the branch, teller and
           account records should be updated by each transaction.
      o    Compliance:  The application program for the Debit-Credit
           transaction should be included in the complete report.




6   SELECTION OF TRANSACTION DATA VALUES

       o   Specification: The DATAMATION article states that "branch
           keys are generated randomly; then a teller within the branch
           is picked at random..." and then "a random account at the
           branch is picked 85% of the time, and a random account at a
           different branch is picked 15% of the time."
       o   Interpretations:    In reality,   each transaction  from   a
           particular terminal    (user) would always specify the same
           branch and teller number and would usually specify         a
           different   account   number    for   each  new transaction.
           Therefore, the branch and teller keys from a particular
                                                                   Page 9
SELECTION OF TRANSACTION DATA VALUES


           terminal should be fixed and it should not be possible for
           two concurrent transactions to specify the same teller
           number.  (DEC'S current Debit-Credit RTE script does not meet
           this guideline.) However, the most important issue here is
           that the account number should be generated randomly and
           probability of accessing cross-branch account records must be
           15%.

      o    Guidelines: When using an RTE for the transaction workload,
           each RTE user should be associated with a particular branch
           and teller, but the teller and branch values, as well as the
           account and debit values,     should be included in the input
           message.  For multiple host implementations     (e.g.,  in a
           VAXcluster environment), assign all transactions that access
           a particular branch to the same host.        Partitioning of
           database   records (either logically into different groups or
           physically into different files in order to minimize the
           distributed locking overhead) is allowed.

       o   Compliance:

           Is the 15% / 85% account accessing policy in effect ?

           Is each terminal associated with a fixed teller and branch?

           Explain how are branch, teller, and account keys are chosen.




7   NUMBER OF TELLERS AND TRANSACTION ARRIVAL RATE AND DISTRIBUTION


       o   Specification: On average, tellers perform one transaction
           every   100   seconds.   However,  the distribution of the
           interarrival times is NOT specified.

       o   Interpretations:  For an X TPS test, the DATAMATION article
           also seems to require 100X on-line tellers, with each teller
           submitting transactions at an average rate of one per 100
           seconds.   Emulating "concentrators" that multiplex multiple
           terminals at a branch into a single connection by using
           proportionately shorter interarrival times is not allowed.
           It would not test the capability or measure the cost of the
           SUT to handle a large number of simultaneous terminal
           sessions.  It would also set a smaller upper bound on the
           maximum   number of concurrent transactions in the SUT.
           Therefore, the RTE should emulate each of the 100X terminals.
           In addition, while the rate per terminal is specified as
           1/100 transactions    per   second,   the   distribution   of
           interarrival times between transaction initiations is not
           specified. Tests that have been performed within DEC using
                                                                  Page 10
number of tellers and transaction arrival rate and distribution

          the RTE have used a constant 100 second interval.  The TANDEM
          tests assumed an exponentially      distributed   transaction
          interarrival time at the back-end host with 10 tellers
          multiplexed into a single connection.  It is more reasonable
          to assume that customers arrive independently at each teller
          and a teller submits transactions to the SUT one at a time as
          long as some customer is waiting. When a customer is not
          available, the teller is free and waits for the next arrival.

      o   Guidelines:  For an X TPS test,  emulate each of the 100X
          teller terminals.    Model the arrival of customers at each
          teller as a Poisson process, i.e., the customer interarrival
          time has an exponential distribution with a mean of 100
          seconds, and assume each teller submits transactions to the
          SUT one at a time as long as customers are waiting.  Figure 5
          shows a model for the overall system, illustrates the system
          events on a simple time line, and uses this time line to show
          the relationship between different interarrivals. Ci is the
          time that the ith customer arrives at the teller, Ti is the
          time that the teller submits a transaction for the customer,
          and Si is the time that the system completes the transaction.
          The customer interarrival time, the transaction interarrival
          time,  and the transaction response time is defined in Figure
          5 in terms of these event times.   Note that customers may
          queue at the teller before submitting a transaction.
NUMBER OF TELLERS AND TRANSACTION ARRIVAL RATE AND DISTRIBUTION




                                                    Next Customer
                                          +------- <—                   ■<—1r
                                       Si |

                                      V                     +-------
                                                             -+        1
                  Arrive ----+ .--- .                  1        1      | Depart
          CUSTOMERS------ > | | | | |   |-------- --- > SUT       -- H i------- >
                  Ci       ----+ ’--- '    Ti                              Si
                                                       +------ +
                        TELLER TERMINAL             SYSTEM UNDER TEST


                     Ci - Ci-1    =>    Customer Interarrival Time
                     Ti - Ti-1    =>    Transaction Interarrival Time
                     Si   - Ti    =>    Transaction Response Time

          Time line of events:
           Cl         Tl     SI           C2         T2     S2           C3            T3

                Teller Trans.  Teller          Teller Trans.   Teller         Teller
                Typing Response Free           Typing Response Free           Typing

           Cl                        C2                          C3
           |<---------------------- >|<----------------------- >|
              Customer Interarrival       Customer Interarrival
                       Tl                       T2                          T3
                       |<--------------------- >|<----------------------- >|
                        Transaction Interarrival Transaction Interarrival

                      Tl       SI                    T2       S2
                      |<---- >|                      |<---- >|
                         Trans.                       Trans.
                     Response Time                  Response Time


                 Figure 5:   Interarrival Time Relationships for Single
                             Terminal.


      o   Compliance:
            # of terminals emulated ?
            Arrival rate from each teller terminal ?
            Interarrival time distribution of customers at teller

            terminals ?
                                                                   Page 12
RESPONSE time requirement and measurement


8   response time requirement and measurement


       o   Specification:  The requirement is for 95% of the transaction
           response times to be one second or less and "to eliminate the
           issue of communication line speed and delay, response time is
           defined as the time interval between the arrival of the last
           bit from the communications line and the sending of the first
           bit to the communications line."

       o   Interpretations:     The response time should be measured within
           the SUT at the communication line interface between the SUT
           (the systems within the computer room)      and the terminals.
           The proper response time constraint that can best describe
           the throughput capability is         dependent   on   the   host
           architecture.       For   example,   in   Tandem's NonStop SQL
           Debit^Crbdit benchmark [TANDEM87], the throughput is 110 TPS
           foiz 9 0% A. second and 208 TPS for 90% 2 seconds.

       o   Guidelines: Measure at the SUT if possible.         When not
           possible,   measure at the RTE and correct the value by
           subtracting the communication delay.  In Figure 2, 3 and 4,
           the boundaries where transaction response time should be
           measured for the three possible configurations are also
           shown.    For example, when remote FEP's are used as in the
           third configuration (FEP's not in the central machine  room),
           the  response time should be measured at the DB host's
           interface to the remote FEP's.  (See Figure 4.)  In addition
           to the maximum TPS rate that meets the response time criteria
           (95% of the transactions have a response time of one second
           or less), gather additional response time data for TPS rates
           above and below the rated TPS to see how sensitive response
           time is to TPS rate.     For comparison purposes, the maximal
           TPS under both 95% 1 second and 90% 2 seconds response time
           constraints should be measured.

       o   Compliance:
           Transaction throughput :            TPS
           Response time constraint :          % less than         seconds

           Measurement :   Measured at SUT ?
                           Adjusted for communication delay ?

                           How much ?            seconds
                                                                  Page 13
CONCURRENCY CONTROL


9    CONCURRENCY CONTROL


       o   Specification: All data files must    be   protected   by   fine
           granularity locking and logging.

       o   Interpretations:  Fine granularity locking provides higher
           concurrency   and probably higher throughput.      The exact
           locking granularity is not specified in the benchmark and is
           left as an implementation decision.

       o   Guidelines:  Lock at the level that gives highest TPS,    but
           the lockable granule should not be larger than the disk block
           (512 bytes).

       o   Compliance:
             Is locking in effect for Branch records ?

                                         Granularity ?

                                      Teller records ?
                                         Granularity ?

                                      Account records ?

                                          Granularity ?




10   RECOVERY MECHANISMS

       o   Specification: All data files must be protected by fine
           granularity   locking   and   logging.     The log file for
           transaction recovery must be duplexed to tolerate single
           failures; data files need not be duplexed.
       o   Interpretations: No transaction that a teller thinks has
           been committed should be lost due to a single failure.
           However, instead of defining clearly what single failures are
           possible,  the DATAMATION article proposes that the log file
           for transaction recovery must be duplexed to tolerate single
           failures.    A single failure could be any one of the
           following:
            *   Transaction abort - This could be caused by a software
                fault, deadlock, access violation, or an user who chooses
                not to complete the transaction.       In this case,    a
                transaction abort is forced. Whatever the transaction
                had done to the databases must be backed out to the
                                                                Page 14
recovery mechanisms


              previous state without affecting other transactions.
          *   System failure - This     could   be   caused  by   any
              hardware/software failure that forces the operation of
              the system to stop. All on-going transactions' activity
              will be discontinued and the contents of the volatile
              memory will be lost.

          *   Media failure - This usually means a disk crash.    The
              contents of the disk that crashed is lost. Any on-going
              transaction that accesses the contents of the disk will
              be aborted.


              A write ahead logging protocol (WAL) in conjunction with
         log files   (Before-Image-Journal or After-Image-Journal) can
         be used to recover from any one of the above failures.    The
         use for either BIJ or AIJ or both is dependent on the
         strategy used by the database management software         and
         application programs, in particular :

          *   How does the DBMS update the physical database    on    disk
              during the execution of transactions ?
          *   How does the TP system handle a transaction commit ?


              The following cases explain when BIJ, AIJ   or   both    are
         needed :
               CASE 1 :   WHEN IS BIJ SUFFICIENT ?

              If database media failure is taken care by another
         mechanism,  e.g., mirroring the database disks, the BIJ can
         cover the other two failure modes under certain conditions.
         If a transaction can commit only after the updates to the
         database and log are forced     (flushed),  then transaction
         failures can be    recovered by applying the BIJ to back out
         that transaction and system failures can be recovered by
         applying the BIJ to back out those transactions that had
         started but not yet committed at the time of system failure.
         Since the BIJ may be needed to roll back a transaction that
         fails due to deadlock or user abort, if the BIJ media fails
         and then the transaction fails after making some database
         updates, the database can't be rolled back.    Although this
         may   be   considered   as   a double failure, media plus
         transaction, the system should have a means to recover.
         Mirroring the BIJ would be one solution.
               CASE 2 :   WHEN IS AIJ SUFFICIENT ?

              An AIJ is sufficient if the DBMS can guarantee that
         whatever the transaction intends to update on the database
         will not be applied to the physical database on the disk
                                                                Page 15
RECOVERY mechanisms


          until the AIJ has been logged and a commit record has been
          recorded on stable storage. A scenario can be described as
          follows :
                      BEGIN-TRANSACTION

                          DB OPERATION ON PRIVATE BUFFER AREA

                          COMMIT  - AIJ and COMMIT record logging
                                  - DB UPDATE
                                  - COMPLETE (Transaction checkpoint)
                      END-TRANSACTION

               The durability of a transaction is guaranteed after the
          AIJ and COMMIT records are forced to disk. All three modes
          of failure can be recovered by the AIJ and a backup archive
          copy of the database.      Since the physical database is not
          updated until all AIJ and COMMIT records are logged,      the
          physical database never contains the results of uncommitted
          transactions.  Furthermore, any uncommitted transaction can
          be aborted by discarding the contents of its private buffers.
          System failure is recovered by scanning the log to find those
          transactions that had logged COMMIT records but not COMPLETE
          records.  Those transactions will be redone using the AIJ
          records.   Database media failures can be recovered by using
          an archive database and the AIJ.  If the disk that stores the
          AIJ file fails,    the consistency of the database is still
          preserved by flushing the buffers       of   the   incomplete
          transactions, aborting those transactions that cannot commit,
          and then restarting after assigning a new AIJ device.

               CASE 3 :   WHEN DO WE NEED BOTH AIJ AND BIJ ?
                When the conditions mentioned above for using only AIJ
          or BIJ are not true, we need an AIJ and BIJ.       Transaction
          aborts and system failures are then recoverable by applying
          either the AIJ or BIJ records, depending on how the physical
          database is updated.   Database media failures can also be
          recovered    from the AIJ and an archive database copy.
          However, in order to survive from media failures of the
          journal disks,    the BIJ and AIJ must be either stored on
          separate disks or, if both BIJ and AIJ are stored on the same
          disk,   it must be duplexed. When AIJ and BIJ are stored on
          separate disks, then if the AIJ is lost the BIJ can be used
          to roll back the database to a consistent state.    If the BIJ
          is lost the AIJ can be used to roll forward the database
          using an archive copy of the database. When both AIJ and BIJ
          are stored on the same disk, it must be mirrored to guarantee
          that a single failure cannot destroy both BIJ and AIJ.

      o   Guidelines: As discussed above, duplexing the journal is NOT
          always necessary. Any of the methods discussed above can be
          used, but recovery from a single failure must be guaranteed.
                                                                 Page 16
RECOVERY MECHANISMS


      o    Compliance:

                 Is BI J used ?         Duplexed ?

                 Is Al J used ?         Duplexed ?
                 If both are used,
                 are they stored on the same disk?




11   DATA COLLECTION INTERVAL


       o   Specification:   None.

       o   Interpretations: Collect data for a reasonable period of
           time after the system enters steady state. The warm-up
           period and data collection period should be long enough to
           generate reproducible results.

       o   Guidelines: A 20 minute data collection period and a 10
           minute warm-up period after all users logged in is probably
           reasonable, but some experiments must be done to verify that
           the performance   results are reproducible.     Multiple runs
           should be performed for some tests, the variance should be
           computed, and confidence intervals should be computed for the
           TPS performance.

       o   Compliance:  Show that tests are reproducible by giving
           examples of independent experiments, and described the time
           in each period (users log-in, warm-up and data collection).




12   DETERMINING COST

       o   Specification:   Cost is the five-year capital cost      of
           vendor-supplied hardware and software in the machine room.
           It   does   not   include   expenditures  for    terminals,
           communications,  application development or operations.  It
           does include hardware and software purchase,  installation,
           and maintenance charges.
       o   interpretations: All the software and hardware equipment in
           the machine room should be included when determining the
           cost.  Front-end processors that are not in the machine room
           do not need to be included.
                                                                 Page 17
determining cost


     o    Guidelines:   The benchmark should be configured to reflect a
          realistic environment that is most cost-effective.         For
          example, using one MicroVAX as FEP at each branch office for
          the 10 teller terminals may be more cost-effective than using
          another VAX as an FEP in the machine room for all the teller
          terminals.   In the former case the machine room cost does not
          include the MicroVAXes while in the later case it includes
          the FEP VAX.

      o   Compliance:   Not available.




     REFERENCES
  [ANON85] Anon, et al., "A Measure of Transaction Processing Power,"
           DATAMATION, April 1, 1985, pp. 112-118.

[SERLIN86] Omni Serlin, "Debit-Credit: a Standard?," FT Systems
           Newsletter, ITOM International Co., Issue No. 47,
           July 15, 1986.
[TREHAN86] Vijay Trehan, "Debit-Credit Benchmark Implementation
           Guidelines," Internal Digital Memo, March 28, 1986.

[TANDEM87] Tandem Computers Incorporated, "Workbook of the TOPGUN
           Benchmark Demonstrating NonStop SQL Performance on 32
           TANDEM VLX Processors and audited by Codd and Date
           Consulting Group," March 6, 1987.
                                   APPENDIX A

                 DEBIT-CREDIT BENCHMARK COMPLIANCE SUMMARY



    Application Programming Language :

Terminal Communications :

      Type of terminal emulated ?

      # of fields entered at each terminal

      for a transaction ?

      Total # of bytes entered ?

      # of fields returned from the SUT

      per transaction ?

      Total # of bytes returned ?

      Communication Protocol :
      Include a diagram of the terminal/SUT configuration, describe
      the functions performed by each component (terminal management
      forms management, database management, etc.), and specify all
      communications protocols used.


Database Description, Size, and Location :

      Transaction throughput :                  TPS

      Branch :      Record Size                 bytes

                    # of records

                    Access method

      Teller :      Record Size                 bytes
                    # of records
debit-credit benchmark compliance summary                        Page A-2


                    Access method

     Account :      Record Size               bytes

                    # of records

                    Access method

     History :      Record Size               bytes

                    Space on-line                 bytes

                    Access method


Transaction Logic :     Include application program listing.

Selection of Transaction Data Values :
      Is the 15% / 85% account accessing policy in

      effect ?

      Is each terminal associated with a fixed teller

      and branch?

      Explain how are branch, teller, and account keys

      are chosen.
Number of Tellers and Transaction Arrival Rate and Distribution

      # of terminals emulated ?

      Arrival rate from each teller terminal ?

      Interarrival time distribution of customers at

      teller terminals ?
Response Time Requirement and Measurement :

      Transaction throughput :              TPS
      Response time constraint :            % less than        seconds

      Measurement :     Measured at SUT ?
                        Adjusted for communication delay ?

                        How much ?            seconds
debit-credit benchmark compliance summary                       Page A-3


Concurrency Control :

     Is locking in effect for Branch records ?

                                 Granularity ?     ■

                              Teller records ?

                                 Granularity ?

                              Account records ?
                                  Granularity ?

Recovery :
      Is BI J used ?         Duplexed ?
      Is Al J used ?         Duplexed ?

      If both are used,
      are they stored on the same disk?


Data Collection Interval :
      Show that tests are reproducible by giving examples of
      independent experiments, and described the time in each
      period (users log-in, warm-up and data collection).
                                        APPENDIX B

        DEBIT-CREDIT BENCHMARK CONFIGURATION SUMMARY



System Under Test

   Hardware:

        Back-End System :
               1) Processor type :

                    Main memory              :




               n)   .       .   .
        Front-End Processor (FEP)                :

               1) Processor type :

                    Main memory              :

                    # of Terminal            :




               n)   .       .   .
        Disk controller :

               1) Type :




               n)       .   .       .
        Disk storage :
               1) Type                   :
debit-credit benchmark configuration summary   Page B-2




                    Controller   :

                    DB/Log file :    ------




               n)   .   .
debit-credit benchmark configuration summary                  Page B-3




      Software :

          System Under Test/Back-End System (SUT)   •

               1) Operating system      :           Ver

                    TP monitor          :           Ver

                    Proq. language      :           Ver

                    File/DB system      :           Ver

                    Forms mgmt system :             Ver

                    Comm, mqmt system :             Ver
               •
               •
               •

               n)   .   .   .
          Front-End Processor (FEP)     :

               1) Operating system      :           Ver

                    Forms mqmt system :             Ver

                    Comm, mqmt system :             Ver




  Driver system (RTE)       :

               1) Processor type            :
                    Operating system        :           Ver

                    Load driver system :                Ver

                    Comm, mgmt system       :           Ver
debit-credit benchmark configuration summary                               Page B-4




            Debit-Credit Benchmark Performance Results Summary



 Test Procedure :

      Transaction arrival pattern :                      Constant interarrival time, or
                                                         Exponential interarrival time

      Data collection period :


  Back-End System 1


      THROUGHPUT (TPS)


      # OF USERS Number of users :

      Response time :       1) Mean                          second

                            2)           % under                 second

      Input/Output rate :          DIO   ________       _ /second

                                   BIO   ________            /second

      CPU utilization :          Total                       %

                                 Int                         %

                                 ker                         %

                                 exe                         %

                                 user                  __ %

      Memory utilization :                         %

      Page fault :    Rate                    / second

                          Hard fault ___ ______          %

      Locking :   New ENQ                          / second

                    Conv. ENQ                      / second

                    DEQ                            / second

                    Total locks
debit-credit benchmark configuration summary   Page B-5



                 Total resources




  Back-End System n



  Front-End System 1



  Front-End System n


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | dec-debit-credit-guidelines-kohler-hsu-1-e228b4 |
| title | DEC Proposed Debit-Credit Benchmark Guidelines (Kohler/Hsu, Dec 1987) |
| author | Walt Kohler & Yun-Ping Hsu, DEC HPS/OLTP Systems Performance Analysis Group |
| date | 1987-12-21 |
| type | internal-engineering-memo |
| subject_domain | OLTP-benchmark-methodology |
| methodology | engineering-guidelines-document |
| source_file | DECtp-debit-credit-guidelines-1987-12-3.pdf |
| license | CC-BY-4.0 |

### Abstract

Internal Digital Equipment Corporation HPS/OLTP Systems Performance Analysis Group memorandum dated 21-Dec-1987 by Walt Kohler and Yun-Ping Hsu, addressed to a distribution list including Dileep Bhandarkar, Bhagyam Moses, Rudy Downs, Joe Marconis, Christopher Marshall, Jim Sasena, Fred Howell, Mike Dempsey, Peter Kastner (HPS::KASTNER), Bill Zahavi, and Linda Wright. Document marked COMPANY CONFIDENTIAL. Provides DEC-internal proposed guidelines for implementing and reporting the Debit-Credit benchmark. Summarizes the 1985 DATAMATION Anon Et Al specification, divides Debit-Credit into eleven components, and for each component lists Specification, Interpretations, Implementation Guidelines, and Compliance requirements. Components include: Application Implementation Language, Terminal Communications (X.25 block-mode vs. character-mode terminals with FEPs), database operations, response-time measurement (95th percentile/1 second), database size, transaction-mix and verification reporting. Includes ASCII diagrams of three implementation configurations: character-mode terminals without FEPs, character-mode with FEPs in machine room, and remote FEPs (e.g. MicroVAX per branch). Cites Trehan (1986), Serlin (1986), and Tandem (1987) prior memos. Establishes baseline DEC reporting standard before the public Transaction Processing Performance Council (TPC) was founded in August 1988.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Insider engineering document showing DEC's approach to benchmark methodology 8 months before TPC was founded. Names 11 OLTP performance engineers including Peter Kastner, anchoring his presence in DEC's TP performance community during the formative period. Foundational artifact for understanding the pre-TPC era of vendor-defined benchmark interpretation. |
| **Relevance** | high | Direct evidence of Kastner's DEC-employer-era role in OLTP/TP performance work. Distribution list places him alongside the engineers (Bhandarkar, Hsu, Kohler, Zahavi) who shaped DEC's transaction-processing benchmark practice. Companion to the Kastner-authored 1988 Primer (Study 4). |
| **Prescience** | high | The eleven-component decomposition (response time, database size, transaction mix verification, etc.) anticipates TPC-A's structure released August 1989. The concerns about ambiguous specs, partition tricks, and vendor interpretations directly motivated the formal TPC standardization effort. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (11)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998), then HP (2002) |
| Tandem Computers | company | acquired | Compaq (1997), then HP (2002) |
| IBM Corporation | company | active |  |
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| Walt Kohler | person | active |  |
| Yun-Ping Hsu | person | active |  |
| Dileep Bhandarkar | person | active |  |
| Bill Zahavi | person | active |  |
| Rudy Downs | person | active |  |
| Transaction Processing Performance Council (TPC) | organization | active |  |

### Technologies Referenced (9)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Debit-Credit Benchmark | performance-benchmark | Anon-et-al / Tandem / Datamation | industry-defacto-standard | superseded-by-TPC-A-and-TPC-C |
| VAXcluster | system-architecture | Digital Equipment Corporation | production-shipping | legacy-OpenVMS-Cluster-on-Itanium-then-x86 |
| ACMS (Application Control Management System) | TP-monitor | Digital Equipment Corporation | active-product | legacy-OpenVMS |
| DECintact | TP-monitor | Digital Equipment Corporation | active-product | discontinued |
| VAX Rdb/VMS | relational-DBMS | Digital Equipment Corporation | active-product | Oracle-Rdb-after-1994-sale |
| VAX DBMS | CODASYL-DBMS | Digital Equipment Corporation | active-product | legacy |
| X.25 packet-switching protocol | communications-protocol | ITU-T (ex CCITT) | industry-standard | obsolete-replaced-by-frame-relay-then-IP |
| IBM 3270 block-mode terminal family | terminal-architecture | IBM Corporation | industry-standard | emulated-only |
| MicroVAX | minicomputer | Digital Equipment Corporation | production-shipping | discontinued |

### Observation Summary

- Total observations: 11
- By type: benchmark_decomposition: 1, response_time_spec: 1, distribution_list: 1, memo_classification: 1, authorship: 1, authorship_2: 1, benchmark_lineage: 1, tpc_anticipation: 1, config_3_topology: 1, vaxcluster_lock_constraint: 1, rdb_role: 1
