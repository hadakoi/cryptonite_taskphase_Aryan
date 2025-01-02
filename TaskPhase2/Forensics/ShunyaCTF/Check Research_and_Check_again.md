# Check Research and Check again

## Method

```
(corrupted_flag.png) Sometimes in life, everything goes wrong, nothing works and you crash every time you try to look within yourself.
In such moments, calculate where you came from, and see what you can correct, generally the last thing you did wrong is what needs to be corrected first. 
Flag Format: 0ctf{words_with_underscore}
```
In this challenge it seems as  though they have provided us a corrupt ``png`` image that would display the flag when fixed.

A corrupt image occurs when its binary structure is altered due to file transfer errors, storage issues, or incomplete saves, making it unviewable by our normal viewing options. 

Now upon doing a pngcheck we notice some things

```shell
hadakoi@Laptop:~/ctfsolve$ pngcheck -v corrupted_flag.png
zlib warning:  different version (expected 1.2.13, using 1.3)

File: corrupted_flag.png (456 bytes)
  chunk IHDR at offset 0x0000c, length 13:  invalid interlace method (82)
ERRORS DETECTED in corrupted_flag.png
hadakoi@Laptop:~/ctfsolve$
```
The **IDHR** chunk (first and most important chunk) is invalid due to a wrong interlacing error. which should be either ``0`` or ``1``


---
**Note -** 

PNG files are structured as a series of chunks each having a specific purpose in the file. The IDHR chunk is the first chunk in the png that contains critical metadata about the image and must appear at the beginning of the file. It defines the images properties such as width, height, bit depth and so on...

Interlacing is a method of progressively displaying an image on the screen often for showing a rough preview of the image before its fully loaded. 


**In this case interlacing can only be 0 or 1 never 82 as that is a invalid value**
---

Hence we can use a hex editor allowing for modification of the file's raw data allowing us to identify and repair damaged sections. As such the tool of my choice was [``010 editor``](https://www.sweetscape.com/010editor/).

Upon opening it and trying to a view an output we can see serveral errors D: with our known error of the **IDHR** chunk hence we can just go about fixing it, first changing the value in the IDHR chunk to no interlacing. 


After that we move onto the CRC mismatches the file shows.. It is known as **cyclic redundancy check** it uses a calculated checksum to see if the file's data matches the stored checksum (every png image has a checksum for each of its chunks). If it is different then the file is corrupted. 


Hence we already can see what to change these to so we make the changes to the hex values. 

After doing this and saving the file and opening it as a png we can see the flag :D


## Flag

> 0ctf{crc_1s_a_us5ful_m5chan1sm}