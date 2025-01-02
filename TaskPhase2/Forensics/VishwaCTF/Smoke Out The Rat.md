# Smoke Out The Rat

## Solving

```
There was a major heist at the local bank. Initial findings suggest that an intruder from within the bank, specifically someone from the bank’s database maintenance team, aided in the robbery. This traitor granted access to an outsider, who orchestrated the generation of fake transactions and the depletion of our valuable customers’ accounts. We have the phone number, ‘789-012-3456’, from which the login was detected, which manipulated the bank’s employee data. Additionally, it’s noteworthy that this intruder attempted to add gibberish to the binlog and ultimately dropped the entire database at the end of the heist. Your task is to identify the first name of the traitor, the last name of the outsider, and the time at which the outsider was added to the database. Flag format: VishwaCTF{TraitorFirstName_OutsiderLastName_HH:MM:SS}
```

They have provided us a file of the name ``DBLOG-bin.000007`` Now to see what kind of file it is we first run the file command.

```shell
hadakoi@Laptop:~/ctfsolve$ file DBlog-bin.000007
DBlog-bin.000007: MySQL replication log, server id 1 MySQL V5+, server version 8.0.36
```

From this we can understand that it is a MySQL binary log file, hence recording and logging all changes to the database as well as statements that alter the database.


Now firstly opening the file in notepad and trying to search for the phone number ``789-012-3456`` we find the name of ``Mathew Miller`` hence we have the first part of our flag. Now upon looking through this on notepad we notice that alof of the output is obfuscated.

Hence to view it in a readable format we can use the ``mysqlbinlog`` utility.



```shell
hadakoi@Laptop:~/ctfsolve$ mysqlbinlog DBlog-bin.000007
/*!50530 SET @@SESSION.PSEUDO_SLAVE_MODE=1*/;
/*!40019 SET @@session.max_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
# at 4
#240217  9:15:13 server id 1  end_log_pos 126 CRC32 0x32e61563  Start: binlog v 4, server v 8.0.36 created 240217  9:15:13 at startup
# Warning: this binlog is either in use or was not closed properly.
ROLLBACK/*!*/;
BINLOG '
IXnQZQ8BAAAAegAAAH4AAAABAAQAOC4wLjM2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAhedBlEwANAAgAAAAABAAEAAAAYgAEGggAAAAICAgCAAAACgoKKioAEjQA
CigAAWMV5jI=
'/*!*/;
# at 126
#240217  9:15:13 server id 1  end_log_pos 157 CRC32 0xea8569cb  Ignorable
# Ignorable event type 35 (MySQL Previous_gtids)
# at 157
#240218 16:24:55 server id 1  end_log_pos 236 CRC32 0x92d92a42  Ignorable
# Ignorable event type 34 (MySQL Anonymous_Gtid)
# at 236
mysqlbinlog: Character set '#255' is not a compiled character set and is not specified in the '/usr/share/mysql/charsets/Index.xml' file
Segmentation fault (core dumped)
hadakoi@Laptop:~/ctfsolve$
```

However trying this seems to provide an error output so lets pipe it to a txt file then see what it has gotten.

``mysqlbinlog DBlog-bin.000007 > log.txt`` 

Now we can examine this text file easily -> 

From the description we know the outsider had ended up dropping the entire database meaning it removed all the contents etc the only way to do this normally is by using the ``DROP`` command so lets look for that where we find one where he drops the entire database for the bank and the log ends there. We can also see that he had tried testing this before by doing ``drop database test``

From this we can see this above it multiple hexa strings that come after a text ``BINLOG '`` with what seems to be logs and the time it was done at.  This line marks the beginning of the binary log event essentially recording changes being made.

when decoding each of these from ``base64`` we see that the first 2 logs above it are useless and show us nothing however the third one ->

```shell
SET TIMESTAMP=1709028089/*!*/;
BEGIN
/*!*/;
# at 80199
#240227 10:01:29 server id 1  end_log_pos 80286 CRC32 0xfd8d1522 	Table_map: `bank`.`employees` mapped to number 117
# has_generated_invisible_primary_key=0
# at 80286
#240227 10:01:29 server id 1  end_log_pos 80520 CRC32 0x181c03e7 	Update_rows: table id 117 flags: STMT_END_F

BINLOG '
+bLdZRMBAAAAVwAAAJ45AQAAAHUAAAAAAAEABGJhbmsACWVtcGxveWVlcwALAw8PCg8PDw8PDwMQ
yADIAJABPAD8A5ABkAFQAP4HAQEAAgP8/wAiFY39
+bLdZR8BAAAA6gAAAIg6AQAAAHUAAAAAAAEAAgAL/////wAAAQAAAARKb2huBVNtaXRor4IPFgBq
b2huLnNtaXRoQGV4YW1wbGUuY29tCjEyMzQ1Njc4OTALADEyMyBNYWluIFN0BgBNdW1iYWkLAE1h
aGFyYXNodHJhBjQwMDAwMQEAAAAAAAEAAAAESm9obgZEYXJ3aW4hjA8TAGpvaG5kb2VAZXhhbXBs
ZS5jb20LKzEyMzQ1Njc4OTALADEyMyBNYWluIFN0BwBBbnl0b3duCABBbnlzdGF0ZQUxMjM0NQEA
AADnAxwY
'/*!*/;
```

``ù²�￹e￹W￹�￹9￹u￹bank￹employees￹�￹�￹�￹<￹ü￹�￹�￹P￹þ￹üÿ￹"￹�￹ýù²�￹e￹ê￹�￹:￹u￹ÿÿÿÿ￹John￹Smith¯�￹john.smith@example.com￹1234567890￹123 Main St￹Mumbai￹Maharashtra￹400001￹John￹Darwin!�￹johndoe@example.com￹+1234567890￹123 Main St￹Anytown￹Anystate￹12345￹ç￹``

Hence from this we can assume that the surname can either be smith, doe or Darwin.

From this text we can also see the ``TIMESTAMP=1709028089`` Now asking gpt to convert this we get this output of ``2024-02-27 10:01:29 in UTC``


**NOTE:** Now upon looking at the official Writeup it was seen the flag was infact using the surname of darwin yet has a different time. 
However this in IST time is ``Matthew_Darwin_2024 15:31:29`` which is 


## Flag

> VishwaCTF{Mattew_Darwin_15:31:29}