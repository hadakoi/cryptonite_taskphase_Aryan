# Bypassing Transport Layer

## Solving

```
The exploit not only manipulated MogamBro's secret but also tried to establish an external TCP connection to gain further access to the machine. But I don't really think he was able to do so. Can you figure out where the exploit was trying to reach to?
```

Now for this challenge I assume we need to look at the ``trace.pcap`` that we have been given in the main folder. 

This ``.pcap file`` is a file that contains captured network data.

When the system was logging network traffic, it was capturing the SSL/TLS traffic (encrypted by default).
At the same time it was logging the keys (likely the TLS session keys used to encrypt and decrypt the traffic). (Transport layer Security)

So upon looking at it at first glance in wireshark it is very useless as it does not provide any good info. This is because it was probably encrypted so to encrypt it we must go to **Edit > Preferences > Protocols > TLS -> (pre)-master-secret-log-file.** . Now using the keys file we found on the ``desktop`` we can reveal the unecrypted packets.

After doing this we see a bunch of HTTP2 packets. So lets export the data as HTTP2 packets and check them out.


Now from here we can use the strings and grep command to look for the flag

```shell
hadakoi@Laptop:~/ctfsolve/CTF$ strings * | grep BITSCTF
</div></li><li class="li1"><div class="de1">Anyways here&#039;s your flag - BITSCTF{5te4l1ng_pr1v47e_key5_ez:)}</div></li></ol>        </div>
hadakoi@Laptop:~/ctfsolve/CTF$
```

hence we find the flag

## Flag

> BITSCTF{5te4l1ng_pr1v47e_key5_ez:)}