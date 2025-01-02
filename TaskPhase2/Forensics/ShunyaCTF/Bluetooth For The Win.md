# Bluetooth For The Win

## Solving

```
(bluetooth.pcap) Mr Jaap Haartsen once told me that he used to have his secret mode of transmission through a technology he invented. There is a saying that he still have one message that no one could ever decrypt, I still have that file (bluetooth.pcap) and I challenge you to retrieve that message. PS: Mind that this guy used to FIDGET a lotttt!!!!
```

---
**Note-**
A PCAP (Packet Capture) file is a file format used to store network traffic data. It contains packets that have been captured from a network interface.
---

From the description of the challenge we can tell we have to see something related to the bluetooth devices of the pcap challenge. 

So we first open the bluetooth devices section on wireshark when looking at the pcap file.

Upon doing this we can see some intresting stuff seems like the bro had nothingphone earpods in (they are garbo just get airpods smh).

![image](https://github.com/user-attachments/assets/28bfb441-8acd-41dc-8fca-5c00affc638b)

Now if we want to see the packets that where captured just from this device we can set a filter for it. 

Now looking at the packets sent from this device with filter ``bluetooth.src`` we understood that he has changed the volume to many times bringing it down and up while pausing to many times to count. Looking further at the challenge description we can understand the **FIDGET** These guys are referencing the use of him turning up and down the volume, pausing the pods on and off. 

![image](https://github.com/user-attachments/assets/3915fc00-fc9d-4dec-9515-0bbbdab8755c)

Now from this we can assume that ->

```
Increase in volume -> - (increasing volume = longer signals)
Decrease in volume -> . (decreasing volume = shorter signals)
Pausing and Unpausing the audio -> whitespace
```

Hence interpreting this we get ``-... .-.. . ..--.- ..-. - .--``


Decoding this we get ``BLE_FTW`` which will be encased in the flag format hence returning us the flag.



## Flag

> 0CTF{BLE_FTW}
