# Reverse Engineering

---

## level1.0

### Solving

```
Reverse engineer this challenge to find the correct license key.
```
I first open up the virtual desktop provided to us by pwncollege. Having done so i first navigate to the challenge directory. Where i see my first challenge file that we are required to reverse. 

Now I first check what filetype it is by running file 

```shell
hacker@reverse-engineering~level1-0:/challenge$ ls
babyrev-level-1-0
hacker@reverse-engineering~level1-0:/challenge$ file babyrev-level-1-0 
babyrev-level-1-0: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fd76c90df030748c8a9d39b14fac0dd6e4f87411, for GNU/Linux 3.2.0, not stripped
hacker@reverse-engineering~level1-0:/challenge$ 
```
It is an ELF file which is our executable. 

Now trying to run this we are greeted with a type of game . It essentially wants us to enter in an input and each challenge seems to peform different operations on the input and compare it to the liscence key.

```shell
hacker@reverse-engineering~level1-0:/challenge$ ./babyrev-level-1-0 
###
### Welcome to ./babyrev-level-1-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	74 65 73 74 0a 

Expected result:

	69 61 74 78 62 

Checking the received license key!

Wrong! No flag for you!

```

I tried Entering ``test`` as an input at first to not get a correct output (ofcourse) but they seem to have provided what our input looks like after the operations where peformed on it and what the expected result looks like after its own operations.

In this specific case it would seem as though the initial input is the same as the mangling input. So there are no changes being made, Hence we just need to figure out what the expected result is by reconverting it back.

Looking closer we recognise that it is converting our input to hex

Hence we will use an hex decoder reconverting ``69 61 74 78 62`` back to characters which becomes `iatbx`


```c
hacker@reverse-engineering~level1-0:/challenge$ ./babyrev-level-1-0 
###
### Welcome to ./babyrev-level-1-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

iatxb
Initial input:

	69 61 74 78 62 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	69 61 74 78 62 

Expected result:

	69 61 74 78 62 

Checking the received license key!

You win! Here is your flag:
pwn.college{wEvmw8ivXbG0hmFWpWb6XIjK8XB.0VM1IDL4czN0czW}
```

### flag

> pwn.college{wEvmw8ivXbG0hmFWpWb6XIjK8XB.0VM1IDL4czN0czW}

---

## level1.1

### Solving

```
Reverse engineer this challenge to find the correct license key.
```
Again Lets try and run this file and see what exactly it spits out. Entering ``test`` 
However unlike last time it is not providing us the hex encoded version of the key we need to enter. 

Luckily ghidra is provided so lets check that out.

Upon opening it in ghidra we find the main strcmp and what its comparing it to if i double clicked this it will show me the assembly for this. And in the assembly section i found ``chhjb`` which should be our key. 

![image](https://github.com/user-attachments/assets/ef6ac62b-93a7-43c1-a9a4-9fe745b446c2)

Entering this returns our flag.

```shell
hacker@reverse-engineering~level1-1:/challenge$ ./babyrev-level-1-1 
###
### Welcome to ./babyrev-level-1-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

chhjb
Checking the received license key!

You win! Here is your flag:
pwn.college{sqxC7Y1TiMbkz4Z87MekgvZTrWc.0lM1IDL4czN0czW}

```

### flag

> pwn.college{sqxC7Y1TiMbkz4Z87MekgvZTrWc.0lM1IDL4czN0czW}

---

## level2.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
Unlike the last challenge it would seem as though our input will be modified when entered unlike last time before being compared to the correct key.

So now lets again start the challenge and enter test as a value.

```shell
###
### Welcome to ./babyrev-level-2-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 

This challenge is now mangling your input using the `swap` mangler for indexes `2` and `4`.

This mangled your input, resulting in:

	74 65 0a 74 73 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	74 65 0a 74 73 

Expected result:

	64 77 6b 61 6e 

Checking the received license key!

Wrong! No flag for you!

```

Upon doing this it seems to show us an extra step where it is swapping  our 2nd and 4th indexes which is our final value. 

Our expected result should be ``64 77 6b 61 6e`` which is ``dwkan`` However this result is where the 2nd and the 4th indexes of the original string where swapped. Hence our original string entered should be ``dwnak`` 

Entering this returns our flag

```shell
hacker@reverse-engineering~level2-0:/challenge$ dwnak
bash: dwnak: command not found
hacker@reverse-engineering~level2-0:/challenge$ ./babyrev-level-2-0 
###
### Welcome to ./babyrev-level-2-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

dwnak
Initial input:

	64 77 6e 61 6b 

This challenge is now mangling your input using the `swap` mangler for indexes `2` and `4`.

This mangled your input, resulting in:

	64 77 6b 61 6e 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	64 77 6b 61 6e 

Expected result:

	64 77 6b 61 6e 

Checking the received license key!

You win! Here is your flag:
pwn.college{0YgJ2m-PAt9cQg_K-fsAzKgbVL_.01M1IDL4czN0czW}
```


### flag

> pwn.college{0YgJ2m-PAt9cQg_K-fsAzKgbVL_.01M1IDL4czN0czW}


---

## level2.1

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

Now like the last ``1.1`` challenge we realise that it does now show the exchange index values but rather tells us directly that we are long. it does not even show the key.


So lets throw this into IDA

Looking at this we realise that buff our input string has can take upto 4 bytes ( 4 hex chars ) and v5 which comes right after will take the overflow

![image](https://github.com/user-attachments/assets/59442757-7f06-4904-9a1d-bc2bc4193008)

Now looking at the swap

![image](https://github.com/user-attachments/assets/59442757-7f06-4904-9a1d-bc2bc4193008)

```pseudocode
  buf = 0;
  v5 = 0;
  puts("Ready to receive your license key!\n");
  read(0, &buf, 5uLL);
  v3 = BYTE1(buf);
  BYTE1(buf) = v5;
  LOBYTE(v5) = v3;
```

We can understand that v3 is first taking the first index of the buf string that we are entering which is the second byte.
We then seem to store the value in v5 in the buf then finally store v3 into the value of v5. 
Why this is working I believe its because buf can only hold 4 characters and as v5 was next declared thats where it is overflowed into the last character. As such when using LOBYTE of v5 it accesses the first index of v5 which is the 4th index of the entire string and the last character

Hence we can conclude we are exchanging the 1st index and the last index.

back to ghidra

![image](https://github.com/user-attachments/assets/3204ef6f-819b-4c9a-a415-b6e605cd5809)

``jvsyo`` We can  see this in the cmp.

hence

``josyv`` is the correct input.

```shell
hacker@reverse-engineering~level2-1:/challenge$ ./babyrev-level-2-1 
###
### Welcome to ./babyrev-level-2-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

josyv
Checking the received license key!

You win! Here is your flag:
pwn.college{cHuhuv5pwfFbmrsd5ByjfsOcmzB.0FN1IDL4czN0czW}


```

### flag

> pwn.college{cHuhuv5pwfFbmrsd5ByjfsOcmzB.0FN1IDL4czN0czW}

---

## level3.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
We start the challenge entering test to get our output as we already know the .0 challenges print the hex of what we entered and what they where changed to. 

```shell
hacker@reverse-engineering~level3-0:/challenge$ ./babyrev-level-3-0 
###
### Welcome to ./babyrev-level-3-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	0a 74 73 65 74 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	0a 74 73 65 74 

Expected result:

	7a 6d 73 65 63 

Checking the received license key!
```

Over here we can understand that whatever we entered is being reversed then checked against ``7a 6d 73 65 63``
This in hex is ``zmsec`` so essentially we have to enter ``cesmz`` so it gets reversed to show ``zmsec`` hence fulfilling the condition. 

```shell
hacker@reverse-engineering~level3-0:/challenge$ ./babyrev-level-3-0 
###
### Welcome to ./babyrev-level-3-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

cesmz
Initial input:

	63 65 73 6d 7a 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	7a 6d 73 65 63 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	7a 6d 73 65 63 

Expected result:

	7a 6d 73 65 63 

Checking the received license key!

You win! Here is your flag:
pwn.college{YTOxrgc8FcjjeFedwRKNsTkwZVK.0VN1IDL4czN0czW}
```


### Flag

> pwn.college{YTOxrgc8FcjjeFedwRKNsTkwZVK.0VN1IDL4czN0czW}

---

## level3.1

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
As this is a .1 we dont get to see how our output is mangled. So lets shove this into ghidra.

We end up seeing this in the c programming 

```c
for (local_1c = 0; local_1c < 2; local_1c = local_1c + 1) {
    uVar1 = *(undefined *)((long)&local_16 + (long)local_1c);
    *(undefined *)((long)&local_16 + (long)local_1c) =
         *(undefined *)((long)&local_16 + (long)(4 - local_1c));
    *(undefined *)((long)&local_16 + (long)(4 - local_1c)) = uVar1;
  }
```
This loop runs two times swapping bytes symmetrically within a block of 5 bytes starting at &local_16.

**Iteration 1:** ``(local_1c = 0)``

``uVar1 = *(undefined *)((long)&local_16 + (long)local_1c);``

reads the bytes at index 0 and stores it in uVar1

``*(undefined *)((long)&local_16 + (long)local_1c) = *(undefined *)((long)&local_16 + (long)(4 - local_1c));``

replaces the byte at index 0 with index 4

``*(undefined *)((long)&local_16 + (long)(4 - local_1c)) = uVar1;``

Replaces the byte at index 4 with the value of uVar1


**Iteration 2:** ``local_1c = 1``

``uVar1 = *(undefined *)((long)&local_16 + (long)local_1c);``

reads the bytes at index 1 and stores it in uVar1

``*(undefined *)((long)&local_16 + (long)local_1c) = *(undefined *)((long)&local_16 + (long)(4 - local_1c));``

replaces the byte at index 1 with index 3

``*(undefined *)((long)&local_16 + (long)(4 - local_1c)) = uVar1;``

Replaces the byte at index 3 with the value of uVar1


Hence essentially just swapping symmetrically and reversing it.

![image](https://github.com/user-attachments/assets/982d287d-64fa-4bd1-8499-f76da6227f9f)

We also know what it is compared against which is: ``zmsec`` which we can see from ghidra.

So reversing the bits how it was shown above we get ``cesmz``

```shell
hacker@reverse-engineering~level3-1:~$ /challenge/./babyrev-level-3-1 
###
### Welcome to /challenge/./babyrev-level-3-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

cesmz
Checking the received license key!

You win! Here is your flag:
pwn.college{AwvbRBkukE0yXyPxM0Dtts-QEXK.0lN1IDL4czN0czW}
```

### Flag

> pwn.college{AwvbRBkukE0yXyPxM0Dtts-QEXK.0lN1IDL4czN0czW}

---

## level4.0

### Solving
```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

Again enter the challenge and enter test.

```shell
hacker@reverse-engineering~level4-0:~$ /challenge/./babyrev-level-4-0 
###
### Welcome to /challenge/./babyrev-level-4-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	0a 65 73 74 74 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	0a 65 73 74 74 

Expected result:

	68 6f 73 74 7a 

Checking the received license key!

Wrong! No flag for you!
```

Over here we can understand that our input seems to be getting sorted in the values of their ascii because converting ``0a 65 73 74 74 `` back gives us ``estt`` 

Trying this with ``68 6f 73 74 7a`` converted to ``hostz``

considering this is what its looking for and that hostz is already sorted why can't I just enter ``hostz`` again?

Doing so gives us the flag.

```shell
hacker@reverse-engineering~level4-0:~$ /challenge/./babyrev-level-4-0 
###
### Welcome to /challenge/./babyrev-level-4-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

hostz
Initial input:

	68 6f 73 74 7a 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	68 6f 73 74 7a 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	68 6f 73 74 7a 

Expected result:

	68 6f 73 74 7a 

Checking the received license key!

You win! Here is your flag:
pwn.college{8OWjML9eGCp8FUCw0zxGgihEWrp.01N1IDL4czN0czW}
```

### Flag

> pwn.college{8OWjML9eGCp8FUCw0zxGgihEWrp.01N1IDL4czN0czW}

---

## level4.1

### Solving
```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

As we know from before the .1 challenges do not provide what it expects to give us the flag so we can just shove it into ghidra.

Doing so i find main then the strcmp and find the str it is comparing with.

Now this str is already in ascending ascii order which is ``akvxz`` hence i can just enter it getting the flag

![image](https://github.com/user-attachments/assets/e86b246f-8407-4a60-977a-c78a3b49b34d)

```shell
hacker@reverse-engineering~level4-1:~$ /challenge/./babyrev-level-4-1 
###
### Welcome to /challenge/./babyrev-level-4-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

akvxz
Checking the received license key!

You win! Here is your flag:
pwn.college{0gNVybz8KLWQP8CSI2Q5qUCLtNp.0FO1IDL4czN0czW}
```

### Flag

> pwn.college{0gNVybz8KLWQP8CSI2Q5qUCLtNp.0FO1IDL4czN0czW}

---

## level5.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

Launching the challenge and ofc inputting ``test`` again we do'nt get the flag yet.

```shell
###
### Welcome to ./babyrev-level-5-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 

This challenge is now mangling your input using the `xor` mangler with key `0xe2`

This mangled your input, resulting in:

	96 87 91 96 e8 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	96 87 91 96 e8 

Expected result:

	92 83 9b 93 94 

Checking the received license key!

Wrong! No flag for you!
```

From this we can see the ``test`` ascii values are being increased. I deduced that it is using an ``XOR`` function or ``^``

``Xor Encoding: A ^ key = B then B ^ A = key``

Each Letter has been encoded key it would seem so lets first find what key each letter used.

- 74 ^ 96 = e2
- 65 ^ 87 = e2
- 73 ^ 91 = e2
- 74 ^ 96 = e2
- 0a ^ e8 = e2

From doing this we now know our key is e2.

Now we can decode the supposed flag using the same method by doing ``B ^ key``

This becomes ``70 61 79 71 76`` which converting from hex to ascii ``payqv``

Entering this returns our flag.

```shell
hacker@reverse-engineering~level5-0:/challenge$ ./babyrev-level-5-0 
###
### Welcome to ./babyrev-level-5-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

payqv
Initial input:

	70 61 79 71 76 

This challenge is now mangling your input using the `xor` mangler with key `0xe2`

This mangled your input, resulting in:

	92 83 9b 93 94 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	92 83 9b 93 94 

Expected result:

	92 83 9b 93 94 

Checking the received license key!

You win! Here is your flag:
pwn.college{ovLmd_oZns57eltzbHqohe3EI2N.0VO1IDL4czN0czW}
```

### Flag

> pwn.college{ovLmd_oZns57eltzbHqohe3EI2N.0VO1IDL4czN0czW}

---

## level5.1

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

### Solving

Now like the previous .1 they do not provide an encoded version of the flag nor what happens after we operate on it So lets first shove this thing into ghidra so we can see what key it possibly is using and what the word we may have to enter is.

Now upon examining with ghidra we can see each character is being XORed with 0x49 which is 73 in decimal.

![image](https://github.com/user-attachments/assets/833f954c-6aba-4a41-9c94-cf2f0d57a4e4)


Now we need to find what string it is being compared to.

![image](https://github.com/user-attachments/assets/1d2297de-249d-4be3-871a-cec9b8f6d821)

which is suprisingly ``#8:=\"`` We can then decode this XORing each character with 0x49 which decodes is ``jqstk``

Now entering this works giving us the flag. 

```shell
hacker@reverse-engineering~level5-1:/challenge$ ./babyrev-level-5-1 
###
### Welcome to ./babyrev-level-5-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

jqstk
Checking the received license key!

You win! Here is your flag:
pwn.college{4kOb7hXCIuwc-V6SSmCYisYkl0L.0FM2IDL4czN0czW}

```

### Flag

> pwn.college{4kOb7hXCIuwc-V6SSmCYisYkl0L.0FM2IDL4czN0czW}

---

## level6.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
Now like the before .0 challenges we can just enter our first thing to test what happens.

```shell
hacker@reverse-engineering~level6-0:/challenge$ ./babyrev-level-6-0 
###
### Welcome to ./babyrev-level-6-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	00 00 00 00 00 00 00 00 00 00 00 00 00 0a 74 73 65 74 

This challenge is now mangling your input using the `swap` mangler for indexes `3` and `5`.

This mangled your input, resulting in:

	00 00 00 00 00 00 00 00 00 00 00 00 00 0a 74 73 65 74 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 

Expected result:

	79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77 

Checking the received license key!

Wrong! No flag for you!
```

This seems a bit different and it even seems to be telling us what it is doing thankfully. This time however instead of 5 characters we have 18 characters.

1. The first mangle it seems to reverse our input string.
2. Now it swaps the indexes 3 and 5
3. It then reverses it again.

After that our mangling is done. 
Now to reverse this mangle on the expected result we can just follow the reverse order.

1. ``79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77`` -> ``77 63 6c 6e 6f 6e 71 68 6d 68 73 70 63 78 7a 64 79``
2. swap indexes 3 and 5 ``77 63 6c 6e 6f 6e 71 68 6d 68 73 70 63 78 7a 64 79`` -> ``77 63 6c 6e 6f 6e 71 68 6d 68 73 70 63 78 7a 64 79`` which swaps 6e in both cases.
3. Now we rereverse the string which then becomes our original ``79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77``

Converting this now to ascii we get ``ydzcxcpshmhqnonlcw``

Entering this we then get our flag.

```shell
hacker@reverse-engineering~level6-0:/challenge$ ./babyrev-level-6-0 
###
### Welcome to ./babyrev-level-6-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

ydzcxcpshmhqnonlcw  
Initial input:

	79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	77 63 6c 6e 6f 6e 71 68 6d 68 73 70 63 78 63 7a 64 79 

This challenge is now mangling your input using the `swap` mangler for indexes `3` and `5`.

This mangled your input, resulting in:

	77 63 6c 6e 6f 6e 71 68 6d 68 73 70 63 78 63 7a 64 79 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77 

Expected result:

	79 64 7a 63 78 63 70 73 68 6d 68 71 6e 6f 6e 6c 63 77 

Checking the received license key!

You win! Here is your flag:
pwn.college{EfalP3BNhla0Fi0RvdVrRoVFC_n.0VM2IDL4czN0czW}
```

### Flag

> pwn.college{EfalP3BNhla0Fi0RvdVrRoVFC_n.0VM2IDL4czN0czW}

---

## level6.1

### Solving

We know the drill now so lets just shove this into ghidra.

```c
for (local_30 = 0; local_30 < 0x10; local_30 = local_30 + 1) {
    for (local_2c = 0; local_2c < 0x10 - local_30; local_2c = local_2c + 1) {
      if (*(byte *)((long)&local_28 + (long)(local_2c + 1)) <
          *(byte *)((long)&local_28 + (long)local_2c)) {
        uVar1 = *(undefined *)((long)&local_28 + (long)local_2c);
        *(undefined *)((long)&local_28 + (long)local_2c) =
             *(undefined *)((long)&local_28 + (long)(local_2c + 1));
        *(undefined *)((long)&local_28 + (long)(local_2c + 1)) = uVar1;
      }
    }
  }
```

This is essentially a bubblesort algorithim that is implmented.

We also see some assembly on the left side that relates to this statement ``uVar1 = local_28._5_1_;``

Looking at the rest of the c programme we just reverse the string set twice.
so now we know that it basically does nothing to the string in the end other than sorting it. 

![image](https://github.com/user-attachments/assets/f1d647c0-2f32-41ee-9989-541752d42f20)

Looking at the string it compares it to abceemjllllfnotww which is sorted already so we can just input this. And this returns us the flag.

```shell
hacker@reverse-engineering~level6-1:/challenge$ ./babyrev-level-6-1 
###
### Welcome to ./babyrev-level-6-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

abceemjllllfnotww
Checking the received license key!

You win! Here is your flag:
pwn.college{wDoHqAXqE3OVBWae8z5cKfWebCS.0lM2IDL4czN0czW}

```

### Flag

> pwn.college{wDoHqAXqE3OVBWae8z5cKfWebCS.0lM2IDL4czN0czW}

---

## level7.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
Now like before load the challenge up and enter test to see how it mangles our input and what the expected input should be.

```Shell
hacker@reverse-engineering~level7-0:/challenge$ ./babyrev-level-7-0 
###
### Welcome to ./babyrev-level-7-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

abcdefghijklmnopqrstuvwxy 
Initial input:

	61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 

This challenge is now mangling your input using the `xor` mangler with key `0x19d20b`

This mangled your input, resulting in:

	78 b0 68 7d b7 6d 7e ba 62 73 b9 67 74 bc 64 69 a3 79 6a a6 7e 6f a5 73 60 

This challenge is now mangling your input using the `xor` mangler with key `0x409e4f3828`

This mangled your input, resulting in:

	38 2e 27 45 9f 2d e0 f5 5a 5b f9 f9 3b 84 4c 29 3d 36 52 8e 3e f1 ea 4b 48 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	27 29 2d 2e 36 38 3b 3d 3e 45 48 4b 4c 52 5a 5b 84 8e 9f e0 ea f1 f5 f9 f9 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	f9 f9 f5 f1 ea e0 9f 8e 84 5b 5a 52 4c 4b 48 45 3e 3d 3b 38 36 2e 2d 29 27 

This challenge is now mangling your input using the `swap` mangler for indexes `3` and `14`.

This mangled your input, resulting in:

	f9 f9 f5 48 ea e0 9f 8e 84 5b 5a 52 4c 4b f1 45 3e 3d 3b 38 36 2e 2d 29 27 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	f9 f9 f5 48 ea e0 9f 8e 84 5b 5a 52 4c 4b f1 45 3e 3d 3b 38 36 2e 2d 29 27 

Expected result:

	fe fb fa 44 f0 e8 96 8e 82 57 57 55 4a 44 f6 42 3e 3c 3a 38 30 2f 29 28 25 

Checking the received license key!

Wrong! No flag for you!
```

Over here now there is 25 characters that we are supposed to enter.

Looking at the mangling process 

1. what we enter is XORed with key `0x19d20b`
2. It then XORed this with key `0x409e4f3828`
3. We then sort the function in ascending order
4. We then reverse the string
5. We then swap indexes 3 and 14. 


Now essentially we just have to go in reverse for the expected flag to get the correct answer.

The way encryption works when using an XOR key like ```0x19d20b``

XOR with 0x19d20b means taking each byte of the target and XORing it with a repeating 3-byte key pattern (0xab, 0xc1, 0x23). 
When i = 0: i % 3 = 0, so uses 0x19. 
When i = 1: i % 3 = 1, so uses 0xd2. 
When i = 2: i % 3 = 2, so uses 0x0b. 
When i = 3: i % 3 = 0, so uses 0x19 again for this key. 
This repeats until all hexa chars are done decoding.


1. First swapping the indexes we get ``fe fb fa f6 f0 e8 96 8e 82 57 57 55 4a 44 44 42 3e 3c 3a 38 30 2f 29 28 25``
2. Next reversing the string we get  ``25 28 29 2f 30 38 3a 3c 3e 42 44 44 4a 55 57 57 82 8e 96 e8 f0 f6 fa fb fe``
3. Now from we just need reverse the string, then reverse the sort.
4. Now we just peform XOR operations with the sequential XOR key ``0x409e4f3828``
5. Then peform XOR operations with sequential XOR key ``0x19d20b``


To do this I made a script 

```python
# Initial encoded string (in hex)
encoded_str = [
    0x25, 0x28, 0x29, 0x2f, 0x30, 0x38, 0x3a, 0x3c, 0x3e, 0x42, 0x44, 0x44,
    0x4a, 0x55, 0x57, 0x57, 0x82, 0x8e, 0x96, 0xe8, 0xf0, 0xf6, 0xfa, 0xfb, 0xfe
]

# Reverse the encoded string
buf = encoded_str[::-1]

# Sort in descending order
buf.sort(reverse=True)

# Key1 for XOR operation (5 bytes)
key1 = [0x40, 0x9e, 0x4f, 0x38, 0x28]

# XOR with key1
for i in range(len(buf)):
    buf[i] ^= key1[i % 5]

# Key2 for XOR operation (3 bytes)
key2 = [0x19, 0xd2, 0xb]  

# XOR with key2
for i in range(len(buf)):
    buf[i] ^= key2[i % 3]

# Convert the result to a string
result = ''.join(chr(x) for x in buf)

# Print the result as a string
print("Decoded String:", result)

# Print hex values
print("Hex values:", [hex(x) for x in buf])
```
This gave me the output off 

```shell
Decoded String: §·¾×
£◄‼±fÅÀ∟®gx{¨´¶
ex values: ['0xa7', '0xb7', '0xbe', '0xd7', '0xa', '0xa3', '0x11', '0x13', '0xb1', '0x66', '0xc5', '0xc0', '0x1c', '0xae', '0x67', '0x1b', '0x72', '0x78', '0x1b', '0xc2', '0x7b', '0xa8', '0xb4', '0x1b', '0x14']
```
Trying to send the special characters as is does not work. 

However after asking advice on the pwncollege discord server and pushing gpt I was guied in the right direction on how to give these things as input.

![image](https://github.com/user-attachments/assets/7fc8c139-bc6d-427a-ba6a-b8b8caac47ec)

From here I just asked gpt to make the command on what he told which is ``echo -ne "\xa7\xb7\xbe\xd7\xa\xa3\x11\x13\xb1\x66\xc5\xc0\x1c\xae\x67\x1b\x72\x78\x1b\xc2\x7b\xa8\xb4\x1b\x14" | ./babyrev-level-7-0``

And solved.

```shell
hacker@reverse-engineering~level7-0:/challenge$ echo -ne "\xa7\xb7\xbe\xd7\xa\xa3\x11\x13\xb1\x66\xc5\xc0\x1c\xae\x67\x1b\x72\x78\x1b\xc2\x7b\xa8\xb4\x1b\x14" | ./babyrev-level-7-0


###
### Welcome to ./babyrev-level-7-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Initial input:

	a7 b7 be d7 0a a3 11 13 b1 66 c5 c0 1c ae 67 1b 72 78 1b c2 7b a8 b4 1b 14 

This challenge is now mangling your input using the `xor` mangler with key `0x19d20b`

This mangled your input, resulting in:

	be 65 b5 ce d8 a8 08 c1 ba 7f 17 cb 05 7c 6c 02 a0 73 02 10 70 b1 66 10 0d 

This challenge is now mangling your input using the `xor` mangler with key `0x409e4f3828`

This mangled your input, resulting in:

	fe fb fa f6 f0 e8 96 8e 82 57 57 55 4a 44 44 42 3e 3c 3a 38 30 2f 29 28 25 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	25 28 29 2f 30 38 3a 3c 3e 42 44 44 4a 55 57 57 82 8e 96 e8 f0 f6 fa fb fe 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	fe fb fa f6 f0 e8 96 8e 82 57 57 55 4a 44 44 42 3e 3c 3a 38 30 2f 29 28 25 

This challenge is now mangling your input using the `swap` mangler for indexes `3` and `14`.

This mangled your input, resulting in:

	fe fb fa 44 f0 e8 96 8e 82 57 57 55 4a 44 f6 42 3e 3c 3a 38 30 2f 29 28 25 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	fe fb fa 44 f0 e8 96 8e 82 57 57 55 4a 44 f6 42 3e 3c 3a 38 30 2f 29 28 25 

Expected result:

	fe fb fa 44 f0 e8 96 8e 82 57 57 55 4a 44 f6 42 3e 3c 3a 38 30 2f 29 28 25 

Checking the received license key!

You win! Here is your flag:
pwn.college{goyBrobt2Y9aIFOhYoVSac7nOWp.01M2IDL4czN0czW}


hacker@reverse-engineering~level7-0:/challenge$ 
```

### Flag

> pwn.college{goyBrobt2Y9aIFOhYoVSac7nOWp.01M2IDL4czN0czW}

---

## level7.1

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
Like before lets first put this into an editor this time i tried using IDA

I then get to see the entire encoding process



```c
  int v3; // eax
  char v4; // [rsp+26h] [rbp-4Ah]
  char v5; // [rsp+28h] [rbp-48h]
  char v6; // [rsp+2Ah] [rbp-46h]
  int i; // [rsp+2Ch] [rbp-44h]
  int j; // [rsp+30h] [rbp-40h]
  int k; // [rsp+34h] [rbp-3Ch]
  int m; // [rsp+38h] [rbp-38h]
  int n; // [rsp+3Ch] [rbp-34h]
  __int64 buf; // [rsp+40h] [rbp-30h] BYREF
  __int64 v13; // [rsp+48h] [rbp-28h]
  __int64 v14; // [rsp+50h] [rbp-20h]
  int v15; // [rsp+58h] [rbp-18h]
  char v16; // [rsp+5Ch] [rbp-14h]
  unsigned __int64 v17; // [rsp+68h] [rbp-8h]
  v17 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  puts("###");
  printf("### Welcome to %s!\n", *a2);
  puts("###");
  putchar(10);
  puts(
    "This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you");
  puts("are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely");
  puts(
    "different operations on that input! You must figure out (by reverse engineering this program) what that license key is.");
  puts("Providing the correct license key will net you the flag!\n");
  buf = 0LL;
  v13 = 0LL;
  v14 = 0LL;
  v15 = 0;
  v16 = 0;
  puts("Ready to receive your license key!\n");
  read(0, &buf, 0x1CuLL);
  v4 = BYTE5(v13);
  BYTE5(v13) = BYTE4(v14);
  BYTE4(v14) = v4;
  for ( i = 0; i <= 26; ++i )
  {
    for ( j = 0; j < 27 - i; ++j )
    {
      if ( *((_BYTE *)&buf + j) > *((_BYTE *)&buf + j + 1) )
      {
        v6 = *((_BYTE *)&buf + j);
        *((_BYTE *)&buf + j) = *((_BYTE *)&buf + j + 1);
        *((_BYTE *)&buf + j + 1) = v6;
      }
    }
  }
  for ( k = 0; k <= 27; ++k )
  {
    v3 = k % 4;
    if ( k % 4 == 3 )
    {
      *((_BYTE *)&buf + k) ^= 0x2Du;
    }
    else if ( v3 <= 3 )
    {
      if ( v3 == 2 )
      {
        *((_BYTE *)&buf + k) ^= 0x97u;
      }
      else if ( v3 <= 2 )
      {
        if ( v3 )
        {
          if ( v3 == 1 )
            *((_BYTE *)&buf + k) ^= 0x93u;
        }
        else
        {
          *((_BYTE *)&buf + k) ^= 0x4Bu;
        }
      }
    }
  }
  for ( m = 0; m <= 27; ++m )
  {
    if ( m % 2 )
    {
      if ( m % 2 == 1 )
        *((_BYTE *)&buf + m) ^= 0x4Cu;
    }
    else
    {
      *((_BYTE *)&buf + m) ^= 9u;
    }
  }
  for ( n = 0; n <= 13; ++n )
  {
    v5 = *((_BYTE *)&buf + n);
    *((_BYTE *)&buf + n) = *((_BYTE *)&buf + 27 - n);
    *((_BYTE *)&buf + 27 - n) = v5;
  }
```

We are also able to view the expected flag which seems to be 
``1b e4 a6 3b 19 e6 a7 37 14 ea ab 36 13 ee b0 2f 0c f2 b4 2a 06 f9 b8 24 07 fb bd 23``

From here lets see how the string that was entered was encrypted.

1. **Now essentially buffer can only store 8 bytes, v13 and v14 as well. Now essentially the first 8 bytes (characters) of the string we input goes into buf then the next 8 into v13 and the last 8 into v14. Now the script to swap is essentially accessing ``BYTE5(v13);`` and `` BYTE4(v14)`` now normally we would be accessing the bytes in these specific arrays However due to the way these arrays are structured and the fact that they are one singular array in actuality when doing BYTE5 we access the 5th index and in BYTE4 we access the 4th index of this entire string**
2. We then sort the array ascending
3. We then have a xor function of sequence
Summary of the XOR Sequence:
k % 4 == 0: XOR with 0x4B.
k % 4 == 1: XOR with 0x93.
k % 4 == 2: XOR with 0x97.
k % 4 == 3: XOR with 0x2D.
4. we then have another XOR sequence
j % 2 == 0: XOR with 0x9u
j % 2 == 1: XOR with 0x4Cu
5. We then Reverse the string.


```python
encoded_str = [0x1b, 0xe4, 0xa6, 0x3b, 0x19, 0xe6, 0xa7, 0x37, 0x14, 0xea, 0xab, 0x36, 0x13, 0xee, 0xb0, 0x2f, 0x0c, 0xf2, 0xb4, 0x2a, 0x06, 0xf9, 0xb8, 0x24, 0x07, 0xfb, 0xbd, 0x23]

# Reverse the array
buf = encoded_str[::-1]

# Define the XOR keys
key1 = [0x09, 0x4c]
key2 = [0x4B, 0x93, 0x97, 0x2D]

# Apply XOR with key1
for i in range(len(buf)):
    buf[i] ^= key1[i % 2]

# Apply XOR with key2
for i in range(len(buf)):
    buf[i] ^= key2[i % 4]

buf[4], buf[5] = buf[5], buf[4]

# Sort the buffer in descending order
buf.sort(reverse=True)

# Convert the result to a string
result = ''.join(chr(x) for x in buf)

# Print the result as a string
print("Decoded String:", result)

# Print hex values
print("Hex values:", [hex(x) for x in buf])

```

Output of script.
```
Decoded String: zzyyxxxuutttrpommlkhgggffeba
Hex values: ['0x7a', '0x7a', '0x79', '0x79', '0x78', '0x78', '0x78', '0x75', '0x75', '0x74', '0x74', '0x74', '0x72', '0x70', '0x6f', '0x6d', '0x6d', '0x6c', '0x6b', '0x68', '0x67', '0x67', '0x67', '0x66', '0x66', '0x65', '0x62', '0x61']
```

Terminal for final output 

```shell
encoded_str = [0x1b, 0xe4, 0xa6, 0x3b, 0x19, 0xe6, 0xa7, 0x37, 0x14, 0xea, 0xab, 0x36, 0x13, 0xee, 0xb0, 0x2f, 0x0c, 0xf2, 0xb4, 0x2a, 0x06, 0xf9, 0xb8, 0x24, 0x07, 0xfb, 0xbd, 0x23]

# Reverse the array
buf = encoded_str[::-1]

# Define the XOR keys
key1 = [0x09, 0x4c]
key2 = [0x4B, 0x93, 0x97, 0x2D]

# Apply XOR with key1
for i in range(len(buf)):
    buf[i] ^= key1[i % 2]

# Apply XOR with key2
for i in range(len(buf)):
    buf[i] ^= key2[i % 4]

# Swap the 4th and 5th indexes (3 and 4 in 0-indexing)
buf[3], buf[4] = buf[4], buf[3]

# Sort the buffer in descending order
buf.sort(reverse=True)

# Convert the result to a string
result = ''.join(chr(x) for x in buf)

# Print the result as a string
print("Decoded String:", result)

# Print hex values
print("Hex values:", [hex(x) for x in buf])
```

```shell
hacker@reverse-engineering~level7-1:/challenge$ ./babyrev-level-7-1 
###
### Welcome to ./babyrev-level-7-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

zzyyxxxuutttrpommlkhgggffeba
Checking the received license key!

You win! Here is your flag:
pwn.college{MF329KyvLrXXbejIv6jQjZBwCSx.0FN2IDL4czN0czW}
```

### Flag

> pwn.college{MF329KyvLrXXbejIv6jQjZBwCSx.0FN2IDL4czN0czW}

---

## level8.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```

First starting the challenge up and inputing ``test`` we get the mangling methods

```shell
hacker@reverse-engineering~level8-0:/challenge$ ./babyrev-level-8-0 
###
### Welcome to ./babyrev-level-8-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

test
Initial input:

	74 65 73 74 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 74 73 65 74 

This challenge is now mangling your input using the `swap` mangler for indexes `26` and `28`.

This mangled your input, resulting in:

	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0a 74 73 65 74 

This challenge is now mangling your input using the `xor` mangler with key `0x05d8083530b2c2`

This mangled your input, resulting in:

	05 d8 08 35 30 b2 c2 05 d8 08 35 30 b2 c2 05 d8 08 35 30 b2 c2 05 d8 08 35 30 b2 c2 05 d8 02 41 43 d7 b6 

This challenge is now mangling your input using the `xor` mangler with key `0xcca1512ad5e1`

This mangled your input, resulting in:

	c9 79 59 1f e5 53 0e a4 89 22 e0 d1 7e 63 54 f2 dd d4 fc 13 93 2f 0d e9 f9 91 e3 e8 d0 39 ce e0 12 fd 63 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	63 fd 12 e0 ce 39 d0 e8 e3 91 f9 e9 0d 2f 93 13 fc d4 dd f2 54 63 7e d1 e0 22 89 a4 0e 53 e5 1f 59 79 c9 

This challenge is now mangling your input using the `swap` mangler for indexes `10` and `32`.

This mangled your input, resulting in:

	63 fd 12 e0 ce 39 d0 e8 e3 91 59 e9 0d 2f 93 13 fc d4 dd f2 54 63 7e d1 e0 22 89 a4 0e 53 e5 1f f9 79 c9 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	0d 0e 12 13 1f 22 2f 39 53 54 59 63 63 79 7e 89 91 93 a4 c9 ce d0 d1 d4 dd e0 e0 e3 e5 e8 e9 f2 f9 fc fd 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	0d 0e 12 13 1f 22 2f 39 53 54 59 63 63 79 7e 89 91 93 a4 c9 ce d0 d1 d4 dd e0 e0 e3 e5 e8 e9 f2 f9 fc fd 

Expected result:

	0d 0f 11 19 30 32 3e 40 53 56 69 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 b0 b6 b7 b9 be d5 e1 fa fb fe ff 

Checking the received license key!

Wrong! No flag for you!
hacker@reverse-engineering~level8-0:/challenge$ 
```

The mangling process seems to be this. We also realise that it takes in 36 characters.

1. Reverse the string
2. swap indexes 26 and 28
3. Sequential XOR mangler with ``0x05d8083530b2c2``
if char % 7 == 0: XOR with 0x05 <br>
if char % 7 == 1: XOR with 0xD8u <br>
if char % 7 == 2: XOR with 0x08 <br>
if char % 7 == 3: XOR with 0x35u <br>
if char % 7 == 4: XOR with 0x30u <br>
if char % 7 == 5: XOR with 0xB2u <br>
if char % 7 == 6: XOR with 0xC2u <br>
if char % 7 == 0: XOR with 0x05 again <br>
4. Sequential XOR mangler with ``0xcca1512ad5e1``
if char % 6 == 0: XOR with 0xCCU <br>
if char % 6 == 1: XOR with 0xA1u <br>
if char % 6 == 2: XOR with 0x51u <br>
if char % 6 == 3: XOR with 0x2Au <br>
if char % 6 == 4: XOR with 0xD5u <br>
if char % 6 == 5: XOR with 0xE1u <br>
if char % 6 == 0: XOR with 0xCCU again <br>
5. Reverse the string
6. Swap the index 10 and 32
7. Sorted in Ascending order

The reverse process can then be taken as this

1. Sort in descending order
2. Swap the index 10 and 32
3. Reverse the string
4. Sequential XOR mangler with ``0xcca1512ad5e1``
5. Sequential XOR mangler with ``0x05d8083530b2c2``
6. Swap indexes 26 and 28
7. Reverse the string

I made cool python script to do this ->

```python
encoded_str = [
    0x0d, 0x0f, 0x11, 0x19, 0x30, 0x32, 0x3e, 0x40, 0x53, 0x56, 0x69, 0x6e,
    0x7c, 0x7d, 0x7d, 0x80, 0x80, 0x84, 0x84, 0x8b, 0x8e, 0x94, 0x99, 0xa3,
    0xb0, 0xb6, 0xb7, 0xb9, 0xbe, 0xd5, 0xe1, 0xfa, 0xfb, 0xfe, 0xff
]

key1 = [0xCC, 0xA1, 0x51, 0x2A, 0xD5, 0xE1]
key2 = [0x05, 0xD8, 0x08, 0x35, 0x30, 0xB2, 0xC2]

# Reverse the array
buf = encoded_str[::-1]

# Sorting the buffer in descending order
buf.sort(reverse=True)

# Swap elements at index 10 and 32
buf[10], buf[32] = buf[32], buf[10]

# Apply XOR with key1
for i in range(len(buf)):
    buf[i] ^= key1[i % 6]

# Apply XOR with key2
for i in range(len(buf)):
    buf[i] ^= key2[i % 7]

# Swap elements at index 26 and 28
buf[26], buf[28] = buf[28], buf[26]

# Reverse the array again
buf = buf[::-1]

# Convert the result to a string
result = ''.join(chr(x) for x in buf)

# Print the result as a string
print("Decoded String:", result)

# Print hex values
print("Hex values:", [hex(x) for x in buf])
```

Output:
```
Decoded String: ␦Ñô
°¨îÇqRî|PYyÚ÷çrñ>°å¢6
Hex values: ['0x1a', '0x97', '0xd1', '0x8d', '0xf4', '0xb', '0xb0', '0xa8', '0xee', '0xc7', '0x90', '0x87', '0x71', '0x52', '0xee', '0x93', '0x7c', '0x50', '0x59', '0x79', '0xda', '0xf7', '0xe7', '0x72', '0xf1', '0x94', '0x3e', '0x1d', '0xb0', '0x86', '0x4', '0xe5', '0xa2', '0x87', '0x36']
```
As we know from before we cannot send special strings without cool command so i made it and it worked giving us tha flag.

```
echo -ne "\x1a\x97\xd1\x8d\xf4\x0b\xb0\xa8\xee\xc7\x90\x87\x71\x52\xee\x93\x7c\x50\x59\x79\xda\xf7\xe7\x72\xf1\x94\x3e\x1d\xb0\x86\x04\xe5\xa2\x87\x36" | ./babyrev-level-8-0

```

```shell
hacker@reverse-engineering~level8-0:/challenge$ echo -ne "\x1a\x97\xd1\x8d\xf4\x0b\xb0\xa8\xee\xc7\x90\x87\x71\x52\xee\x93\x7c\x50\x59\x79\xda\xf7\xe7\x72\xf1\x94\x3e\x1d\xb0\x86\x04\xe5\xa2\x87\x36" | ./babyrev-level-8-0
###
### Welcome to ./babyrev-level-8-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Initial input:

	1a 97 d1 8d f4 0b b0 a8 ee c7 90 87 71 52 ee 93 7c 50 59 79 da f7 e7 72 f1 94 3e 1d b0 86 04 e5 a2 87 36 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	36 87 a2 e5 04 86 b0 1d 3e 94 f1 72 e7 f7 da 79 59 50 7c 93 ee 52 71 87 90 c7 ee a8 b0 0b f4 8d d1 97 1a 

This challenge is now mangling your input using the `swap` mangler for indexes `26` and `28`.

This mangled your input, resulting in:

	36 87 a2 e5 04 86 b0 1d 3e 94 f1 72 e7 f7 da 79 59 50 7c 93 ee 52 71 87 90 c7 b0 a8 ee 0b f4 8d d1 97 1a 

This challenge is now mangling your input using the `xor` mangler with key `0x05d8083530b2c2`

This mangled your input, resulting in:

	33 5f aa d0 34 34 72 18 e6 9c c4 42 55 35 df a1 51 65 4c 21 2c 57 a9 8f a5 f7 02 6a eb d3 fc b8 e1 25 d8 

This challenge is now mangling your input using the `xor` mangler with key `0xcca1512ad5e1`

This mangled your input, resulting in:

	ff fe fb fa e1 d5 be b9 b7 b6 11 a3 99 94 8e 8b 84 84 80 80 7d 7d 7c 6e 69 56 53 40 3e 32 30 19 b0 0f 0d 

This challenge is now mangling your input using the `reverse` mangler.

This mangled your input, resulting in:

	0d 0f b0 19 30 32 3e 40 53 56 69 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 11 b6 b7 b9 be d5 e1 fa fb fe ff 

This challenge is now mangling your input using the `swap` mangler for indexes `10` and `32`.

This mangled your input, resulting in:

	0d 0f b0 19 30 32 3e 40 53 56 fb 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 11 b6 b7 b9 be d5 e1 fa 69 fe ff 

This challenge is now mangling your input using the `sort` mangler.

This mangled your input, resulting in:

	0d 0f 11 19 30 32 3e 40 53 56 69 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 b0 b6 b7 b9 be d5 e1 fa fb fe ff 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	0d 0f 11 19 30 32 3e 40 53 56 69 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 b0 b6 b7 b9 be d5 e1 fa fb fe ff 

Expected result:

	0d 0f 11 19 30 32 3e 40 53 56 69 6e 7c 7d 7d 80 80 84 84 8b 8e 94 99 a3 b0 b6 b7 b9 be d5 e1 fa fb fe ff 

Checking the received license key!

You win! Here is your flag:
pwn.college{cToNwif1SvewpQBhX_mcchXJ8QW.0VN2IDL4czN0czW}

```

### Flag

> pwn.college{cToNwif1SvewpQBhX_mcchXJ8QW.0VN2IDL4czN0czW}

---

## level8.1

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key.
```
Like before let us first shove the challenge into ghidra/ida

```c
  int v3; // eax
  int v4; // eax
  char v5; // [rsp+2Eh] [rbp-52h]
  char v6; // [rsp+30h] [rbp-50h]
  char v7; // [rsp+32h] [rbp-4Eh]
  int i; // [rsp+34h] [rbp-4Ch]
  int j; // [rsp+38h] [rbp-48h]
  int k; // [rsp+3Ch] [rbp-44h]
  int m; // [rsp+40h] [rbp-40h]
  int n; // [rsp+44h] [rbp-3Ch]
  int ii; // [rsp+48h] [rbp-38h]
  int jj; // [rsp+4Ch] [rbp-34h]
  __int64 buf[3]; // [rsp+50h] [rbp-30h] BYREF
  __int64 v16; // [rsp+68h] [rbp-18h]
  int v17; // [rsp+70h] [rbp-10h]
  __int16 v18; // [rsp+74h] [rbp-Ch]
  unsigned __int64 v19; // [rsp+78h] [rbp-8h]

  v19 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  puts("###");
  printf("### Welcome to %s!\n", *a2);
  puts("###");
  putchar(10);
  puts(
    "This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you");
  puts("are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely");
  puts(
    "different operations on that input! You must figure out (by reverse engineering this program) what that license key is.");
  puts("Providing the correct license key will net you the flag!\n");
  memset(buf, 0, sizeof(buf));
  v16 = 0LL;
  v17 = 0;
  v18 = 0;
  puts("Ready to receive your license key!\n");
  read(0, buf, 0x25uLL);
  for ( i = 0; i <= 17; ++i )
  {
    v7 = *((_BYTE *)buf + i);
    *((_BYTE *)buf + i) = *((_BYTE *)buf + 36 - i);
    *((_BYTE *)buf + 36 - i) = v7;
  }
  for ( j = 0; j <= 36; ++j )
  {
    switch ( j % 7 )
    {
      case 0:
        *((_BYTE *)buf + j) ^= 0x8Fu;
        break;
      case 1:
        *((_BYTE *)buf + j) ^= 7u;
        break;
      case 2:
        *((_BYTE *)buf + j) ^= 0x6Eu;
        break;
      case 3:
        *((_BYTE *)buf + j) ^= 0xA2u;
        break;
      case 4:
        *((_BYTE *)buf + j) ^= 0xF8u;
        break;
      case 5:
        *((_BYTE *)buf + j) ^= 0xB6u;
        break;
      case 6:
        *((_BYTE *)buf + j) ^= 0xBCu;
        break;
      default:
        continue;
    }
  }
  v5 = BYTE5(buf[0]);
  BYTE5(buf[0]) = BYTE6(v16);
  BYTE6(v16) = v5;
  for ( k = 0; k <= 36; ++k )
  {
    switch ( k % 5 )
    {
      case 0:
        *((_BYTE *)buf + k) ^= 0x3Du;
        break;
      case 1:
        *((_BYTE *)buf + k) ^= 0x77u;
        break;
      case 2:
        *((_BYTE *)buf + k) ^= 0xC1u;
        break;
      case 3:
        *((_BYTE *)buf + k) ^= 0x64u;
        break;
      case 4:
        *((_BYTE *)buf + k) ^= 0x66u;
        break;
      default:
        continue;
    }
  }
  for ( m = 0; m <= 35; ++m )
  {
    for ( n = 0; n < 36 - m; ++n )
    {
      if ( *((_BYTE *)buf + n) > *((_BYTE *)buf + n + 1) )
      {
        v6 = *((_BYTE *)buf + n);
        *((_BYTE *)buf + n) = *((_BYTE *)buf + n + 1);
        *((_BYTE *)buf + n + 1) = v6;
      }
    }
  }
  for ( ii = 0; ii <= 36; ++ii )
  {
    v3 = ii % 4;
    if ( ii % 4 == 3 )
    {
      *((_BYTE *)buf + ii) ^= 0x78u;
    }
    else if ( v3 <= 3 )
    {
      if ( v3 == 2 )
      {
        *((_BYTE *)buf + ii) ^= 0x47u;
      }
      else if ( v3 <= 2 )
      {
        if ( v3 )
        {
          if ( v3 == 1 )
            *((_BYTE *)buf + ii) ^= 0x4Eu;
        }
        else
        {
          *((_BYTE *)buf + ii) ^= 0x49u;
        }
      }
    }
  }
  for ( jj = 0; jj <= 36; ++jj )
  {
    v4 = jj % 4;
    if ( jj % 4 == 3 )
    {
      *((_BYTE *)buf + jj) ^= 0x39u;
    }
    else if ( v4 <= 3 )
    {
      if ( v4 == 2 )
      {
        *((_BYTE *)buf + jj) ^= 0xCDu;
      }
      else if ( v4 <= 2 )
      {
        if ( v4 )
        {
          if ( v4 == 1 )
            *((_BYTE *)buf + jj) ^= 0xCDu;
        }
        else
        {
          *((_BYTE *)buf + jj) ^= 0x93u;
        }
      }
    }
  }
  puts("Checking the received license key!\n");
  if ( !memcmp(buf, &unk_4020, 0x25uLL) )
  {
    sub_12A9();
    exit(0);
  }
  puts("Wrong! No flag for you!");
  exit(1);
```

From this we can see that the number of characters for input is 37.
Upon doing this we have the encryption the steps are 

1. Reverse the string
2. Sequential XOR with 
char % 7 = 0: XOR char with 0x8Fu <br>
char % 7 = 1: XOR char with 0x07 <br>
char % 7 = 2: XOR char with 0x6Eu <br>
char % 7 = 3: XOR char with 0xA2u <br>
char % 7 = 4: XOR char with 0xF8u <br>
char % 7 = 5: XOR char with 0xB6u <br>
char % 7 = 6: XOR char with 0xBCu <br>
char % 7 = 0: XOR char with 0x8Fu <br>
3. We then seem to do a swap. 
```c
v5 = BYTE5(buf[0]);
BYTE5(buf[0]) = BYTE6(v16);
BYTE6(v16) = v5;
```
Now form before that 
__int64 buf[3]; // [rsp+50h] [rbp-30h] BYREF
__int64 v16; // [rsp+68h] [rbp-18h]

This means buf contains 3 elements of 8 byte strings. essentially holding 24 bytes
and v16 will hold another 8 bytes accounting for 32 of the 37 characters.

the v5 first stores the byte at index6 of the string we entered.
Now this byte at index6 is then replaced by ``BYTE6(v16)`` which as it has string values that overflowed from buff we will be taking this byte from the start of the buf array. Which is index7.

As such we swap index 6 and 7.
4. We now have another sequential XOR char with 
char % 5 == 0: XOR char with 0x3D <br>
char % 5 == 1: XOR char with 0x77 <br>
char % 5 == 2: XOR char with 0xC1 <br>
char % 5 == 3: XOR char with 0x64 <br>
char % 5 == 4: XOR char with 0x66 <br>
5. Sorts string in Ascending order
6. Sequential XOR with
char % 4 == 0: XOR char with 0x49 <br>
char % 4 == 1: XOR char with 0x4E <br>
char % 4 == 2: XOR char with 0x47 <br>
char % 4 == 3: XOR char with 0x78 <br>
7. Sequential XOR with
char % 4 == 0: XOR char with 0x93 <br>
char % 4 == 1: XOR char with 0xCD <br>
char % 4 == 2: XOR char with 0xCD <br>
char % 4 == 3: XOR char with 0x39 <br>


Now to reverse this We can go backwards through the encoding process.
1. Sequential XOR with 
char % 4 == 0: XOR char with 0x93 <br>
char % 4 == 1: XOR char with 0xCD <br>
char % 4 == 2: XOR char with 0xCD <br>
char % 4 == 3: XOR char with 0x39 <br>
2. Sequential XOR with
char % 4 == 0: XOR char with 0x49 <br>
char % 4 == 1: XOR char with 0x4E <br>
char % 4 == 2: XOR char with 0x47 <br>
char % 4 == 3: XOR char with 0x78 <br>
3. Sorts string in Descending order
4. We now have another sequential XOR char with 
char % 5 == 0: XOR char with 0x3D <br>
char % 5 == 1: XOR char with 0x77 <br>
char % 5 == 2: XOR char with 0xC1 <br>
char % 5 == 3: XOR char with 0x64 <br>
char % 5 == 4: XOR char with 0x66 <br>
5. Swap index values 6 and 7.
6. Sequential XOR with 
char % 7 = 0: XOR char with 0x8Fu <br>
char % 7 = 1: XOR char with 0x07 <br>
char % 7 = 2: XOR char with 0x6Eu <br>
char % 7 = 3: XOR char with 0xA2u <br>
char % 7 = 4: XOR char with 0xF8u <br>
char % 7 = 5: XOR char with 0xB6u <br>
char % 7 = 6: XOR char with 0xBCu <br>
char % 7 = 0: XOR char with 0x8Fu <br>
7. Reverse the string

Now looking for the expected final code we look through ida to find

``da, 80, 8e, 45, cb, 97, 93, 65, f3, d0, dc, 21, b8, ed, 1b, d9, 44, 21, 22, e9, 70, 2f, 38, f3, 68, 36, 3d, f8, 19, 5b, 56, a5, 36, 70, 7c, ba, 21``

Now 

```python
# Hex input to decode
buf = [
    0xDA, 0x80, 0x8E, 0x45, 0xCB, 0x97, 0x93, 0x65, 0xF3, 0xD0, 0xDC, 0x21, 
    0xB8, 0xED, 0x1B, 0xD9, 0x44, 0x21, 0x22, 0xE9, 0x70, 0x2F, 0x38, 0xF3, 
    0x68, 0x36, 0x3D, 0xF8, 0x19, 0x5B, 0x56, 0xA5, 0x36, 0x70, 0x7C, 0xBA, 0x21
]

# Keys
key1 = [0x93, 0xCD, 0xCD, 0x39]
key2 = [0x49, 0x4E, 0x47, 0x78]
key3 = [0x3D, 0x77, 0xC1, 0x64, 0x66]
key4 = [0x8F, 0x07, 0x6E, 0xA2, 0xF8, 0xB6, 0xBC]

# First XOR operation with key1
for i in range(len(buf)):
  buf[i] ^= key1[i % 4]

# Second XOR operation with key2
for i in range(len(buf)):
  buf[i] ^= key2[i % 4]

# Sort buffer in descending order
buf.sort(reverse=True)

# Third XOR operation with key3
for i in range(len(buf)):
  buf[i] ^= key3[i % 5]

# Swap buf[0] and buf[4]
buf[6], buf[7] = buf[6], buf[7]

# Fourth XOR operation with key4
for i in range(len(buf)):
  buf[i] ^= key4[i % 7]

# Reverse the buffer
buf = buf[::-1]

# Convert to string
result = ''.join(chr(x) for x in buf)

# Print results
print("Decoded String:", result)
print("Hex values:", [hex(x) for x in buf])
```

Running this gives output:

```
Decoded String: p±ÞÖ(ÁJEÂ.¥¦dW`r4Ë³[jÅ:(± or5YI
Hex values: ['0x70', '0xb1', '0xde', '0xd6', '0x28', '0xc1', '0x4a', '0x45', '0xc2', '0x2e', '0x97', '0xa5', '0xa6', '0x64', '0x57', '0x60', '0x1f', '0x72', '0x34', '0xcb', '0xb3', '0x96', '0x5b', '0x6a', '0xc5', '0x3a', '0x28', '0xb1', '0xa0', '0x96', '0x17', '0x6f', '0x72', '0x35', '0x59', '0x8b', '0x49']
```

As such we make a command to run send these characters to the script

``echo -ne "\x70\xb1\xde\xd6\x28\xc1\x4a\x45\xc2\x2e\x97\xa5\xa6\x64\x57\x60\x1f\x72\x34\xcb\xb3\x96\x5b\x6a\xc5\x3a\x28\xb1\xa0\x96\x17\x6f\x72\x35\x59\x8b\x49" | ./babyrev-level-8-1``


```shell
hacker@reverse-engineering~level8-1:/challenge$ 
echo -ne "\x70\xb1\xde\xd6\x28\xc1\x4a\x45\xc2\x2e\x97\xa5\xa6\x64\x57\x60\x1f\x72\x34\xcb\xb3\x96\x5b\x6a\xc5\x3a\x28\xb1\xa0\x96\x17\x6f\x72\x35\x59\x8b\x49" | ./babyrev-level-8-1
###
### Welcome to ./babyrev-level-8-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Checking the received license key!

You win! Here is your flag:
pwn.college{gA9XDQAK-yB5QWuIUlM48SPNqMg.0lN2IDL4czN0czW}
```

### Flag

> pwn.college{gA9XDQAK-yB5QWuIUlM48SPNqMg.0lN2IDL4czN0czW}

---

## level9.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.
```

Now basically what it is telling us to do is that we will be allowed to choose an address. Then patch 5 different bytes of our choice.

Now what we know by this is we get to pick any address in the challenge then change the code at that address.

Now first i try running the code with just test inputs to see that it is using a md5 meaning it is not reversable.

So the first thing i do is shove the thing into ghidra. 

My first thought was how to get to the win condition and i found the assembly and addresses for it easily on ghidra.

![image](https://github.com/user-attachments/assets/243fd57f-483f-4b59-9a07-3df735160d70)

``001028e3 75 14           JNZ        LAB_001028f9``

What this means is if our **comparison value ends up as not 0** we jump 14 hex ahead to ``001028f9`` Now as we have a md5 hash whatever we input
is extremely unlikely to give us our value as 0 and hence will always be greater or lesser wtv, hence making us always jump. Now to possibly bypass this Why don't i make this jump only happen when we get 0 (very unlikely) reversing the initial condition. 

What i essentially mean by this is essentially as the previous condition is where we win if our input is = liscence key i.e very unlikely.
so to make this very easy why dont i just make it give me the win condition if our input is never zero?

Lets look at the conditional opcodes for jumps that i found here [Jumps](http://www.unixwiz.net/techtips/x86-jumps.html)

![image](https://github.com/user-attachments/assets/402d3458-eee6-4b68-9402-eccd7eb36d4c)

We see that this statement comes under short jump codes and not near jump codes.

**NOTE:**
1. **Short jump op codes** are used for jumps within a small range.
2. **Near jump op codes** allow jumps to a larger range.
3. They also have different opcode formats
   
Now the opcode of JNZ is 75. However the opcode 74 is ``JE`` also known as if the value is zero it jumps to the condition. Now why does this work exactly?

Well first off our output is almost always never 0. Now the jump only happens when our input is 0. Meaning we get to enter the if statement hence winning :D

So lets access the ``28e3`` hex and change it to ``74``

```shell
hacker@reverse-engineering~level9-0:/challenge$ ./babyrev-level-9-0 
###
### Welcome to ./babyrev-level-9-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/5.
Offset (hex) to change: 28e3
New value (hex): 74
The byte has been changed: *0x56f6008ea8e3 = 74.
Changing byte 2/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x56f6008e8000 = 0.
Changing byte 3/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x56f6008e8000 = 0.
Changing byte 4/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x56f6008e8000 = 0.
Changing byte 5/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x56f6008e8000 = 0.
Ready to receive your license key!


Initial input:

	0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

	78 dd a0 70 82 18 c9 26 db f8 17 a5 5f c4 a2 3e 00 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	78 dd a0 70 82 18 c9 26 db f8 17 a5 5f c4 a2 3e 00 00 00 00 00 00 00 00 00 00 

Expected result:

	b9 74 d9 52 e7 39 c7 8d f3 df 2f 51 46 4f 86 5d 00 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{c4t3eYPIM7hWSIjh-yLsbMzJ9IW.01N2IDL4czN0czW}
```

### Flag

> pwn.college{c4t3eYPIM7hWSIjh-yLsbMzJ9IW.01N2IDL4czN0czW}

---

## level9.1

### Solving
```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 5 bytes in the binary.
```

This seems to be a similar type of challenge so I shove it into ghidra.

Im able to see a similar win function with the same if condition as before so should't I just exploit it just the same?

![image](https://github.com/user-attachments/assets/2a7cf5f4-23d2-4b9d-8389-69b040c42bbd)

The address where the jump is happening on is ``00101789 75 14           JNZ        LAB_0010179f``.

```shell
hacker@reverse-engineering~level9-1:/challenge$ ./babyrev-level-9-1 
###
### Welcome to ./babyrev-level-9-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/5.
Offset (hex) to change: 1789
New value (hex): 74
The byte has been changed: *0x59ea06c60789 = 74.
Changing byte 2/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x59ea06c5f000 = 0.
Changing byte 3/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x59ea06c5f000 = 0.
Changing byte 4/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x59ea06c5f000 = 0.
Changing byte 5/5.
Offset (hex) to change: 0
New value (hex): 0
The byte has been changed: *0x59ea06c5f000 = 0.
Ready to receive your license key!


Checking the received license key!

You win! Here is your flag:
pwn.college{MYIKmGZIbfmtesNGUHBTkdH6P3U.0FO2IDL4czN0czW}
```

### Flag

> pwn.college{MYIKmGZIbfmtesNGUHBTkdH6P3U.0FO2IDL4czN0czW}

---

## level10.0

### Solving


```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 1 byte in the binary.
```


Now unlike the last challenge where we had 5 byte changes it seems as though we are just given 1. But haven't I only been using 1 byte change anyways? Onwards we go with the same thing.

So lets first throw da programme into ghidra now like before i look for the jump condition here.

``      00102563 75 14           JNZ        LAB_00102579``

```shell
hacker@reverse-engineering~level10-0:/challenge$ ./babyrev-level-10-0 
###
### Welcome to ./babyrev-level-10-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/1.
Offset (hex) to change: 2563
New value (hex): 74
The byte has been changed: *0x5c549c71d563 = 74.
Ready to receive your license key!


Initial input:

	0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

	a7 98 4f dd f1 88 27 a8 ea b7 aa 8d 85 4a 86 9b 00 00 00 00 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	a7 98 4f dd f1 88 27 a8 ea b7 aa 8d 85 4a 86 9b 00 00 00 00 00 00 00 00 00 00 00 00 00 

Expected result:

	68 85 ab b6 1c 1b f5 50 61 2b ab 75 99 b2 3e 9e 00 00 00 00 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{c9QUWXv8DVSORMX0SmLQKN5tEl0.0VO2IDL4czN0czW}
```

### Flag

> pwn.college{c9QUWXv8DVSORMX0SmLQKN5tEl0.0VO2IDL4czN0czW}

---

## level10.1

### Solving
```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 1 byte in the binary.
```

Like last time throw into ghidra find the if statement at the end and we have the addresses ``        00101971 75 14           JNZ        LAB_00101987``


```shell
hacker@reverse-engineering~level10-1:/challenge$ ./babyrev-level-10-1
###
### Welcome to ./babyrev-level-10-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

Changing byte 1/1.
Offset (hex) to change: 1971
New value (hex): 74
The byte has been changed: *0x597095cd7971 = 74.
Ready to receive your license key!


Checking the received license key!

You win! Here is your flag:
pwn.college{YupTiYx-Gzvggx6C_aUrf9bBLCV.0FM3IDL4czN0czW}
```

### Flag

> pwn.college{YupTiYx-Gzvggx6C_aUrf9bBLCV.0FM3IDL4czN0czW}

---

## level11.0

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 2 bytes in the binary, but performs an integrity check afterwards.
```
Unlike the previous challenges there seems to be an integrity check.

Over here we seem to have an extra c code 

```c
  do {
    iVar1 = local_f8 << 0xc;
    local_f8 = local_f8 + 1;
    iVar1 = mprotect((void *)(local_d0 + iVar1),0x1000,7);
  } while (iVar1 == 0);
  puts("In order to ensure code integrity, the code will be hashed and verified.\n");
  MD5_Init(&local_c8);
  for (local_f4 = 0; local_f4 < local_f8 + -1; local_f4 = local_f4 + 1) {
    MD5_Update(&local_c8,(void *)((local_f4 << 0xc) + local_d0),0x1000);
  }
  MD5_Final(local_68,&local_c8);
  puts("The pre-crack code integrity hash is:\n");
  putchar(9);
  for (local_f0 = 0; local_f0 < 0x19; local_f0 = local_f0 + 1) {
    printf("%02x ",(ulong)local_68[local_f0]);
  }
  puts("\n");
  for (local_ec = 0; local_ec < 2; local_ec = local_ec + 1) {
    printf("Changing byte %d/2.\n",(ulong)(local_ec + 1));
    printf("Offset (hex) to change: ");
    __isoc99_scanf(&DAT_001023db,&local_fa);
    printf("New value (hex): ");
    __isoc99_scanf(&DAT_001023f1,&local_fb);
    *(byte *)(local_d0 + (ulong)local_fa) = local_fb;
    printf("The byte has been changed: *%p = %hhx.\n",(ulong)local_fa + local_d0,(ulong)local_fb);
  }
  MD5_Init(&local_c8);
  for (local_e8 = 0; local_e8 < local_f8 + -1; local_e8 = local_e8 + 1) {
    MD5_Update(&local_c8,(void *)((local_e8 << 0xc) + local_d0),0x1000);
  }
  MD5_Final(local_58,&local_c8);
  puts("The post-crack code integrity hash is:\n");
  putchar(9);
  for (local_e4 = 0; local_e4 < 0x19; local_e4 = local_e4 + 1) {
    printf("%02x ",(ulong)local_58[local_e4]);
  }
  puts("\n");
  iVar1 = memcmp(local_68,local_58,0x10)
```

Since the mprotect call returns 0 on success the condition iVar1 == 0 would only be true if mprotect fails. This could happen due to a variety of reasons, such as invalid memory addresses, improper permissions, or other system-level errors.

In the loop:

mprotect is being called on successive addresses, starting from local_d0 + (local_f8 << 0xc) and incrementing local_f8 each time.
If mprotect is successful, it will return 0, and the loop will continue as long as iVar1 != 0.
The key point here is that the loop will exit only if mprotect fails (when iVar1 == 0), so the fact that iVar1 is never equal to 0 implies that mprotect is always succeeding in these calls.
This implies that all the memory regions being passed to mprotect are valid and the system allows the memory protection to be modified as requested. If iVar1 were ever 0, it would indicate that mprotect failed for some reason (e.g., if the memory address is invalid or permissions cannot be set), but based on the structure of the loop, mprotect keeps succeeding

This never allows ivar1 = 0 

hence when we see the check condition after 

```c
  if (iVar1 != 0) {
    puts("The code\'s integrity has been breached, aborting!\n");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
```
It will always come true hence entering the error and exiting. Hence to never enter this condition How bout we change this exit to only happen when we have ``ivar1 == 0?`` 

Looking at the assembly we see ``        001019e6 75 6e           JNZ        LAB_00101a56`` Meaning that it Jumps when not equal to 0 6e hex ahead. which should not be possible as the condition in c literally states that when not equal to zero exit the programme meaning we where bound to setup to fail.

Hence why dont we make this condition ``JE`` Meaning it will jump ahead if == 0; Which the jump will never occur and it will also never enter this error meaning for this assembly we do the same thing we did before.

Now lets look at the last few lines which seem like the exact same type of assembly as our previous challenges.

Hence all we have to do is change both ``JNZ`` To ``JE`` entering ``74``.

Assembly lines of first is ``        001019e6 75 6e           JNZ        LAB_00101a56``
Assembly lines of second is ``        00101c78 75 14           JNZ        LAB_00101c8e``

Doing this we get the flag.

```shell
hacker@reverse-engineering~level11-0:/challenge$ ./babyrev-level-11-0 
###
### Welcome to ./babyrev-level-11-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

In order to ensure code integrity, the code will be hashed and verified.

The pre-crack code integrity hash is:

	78 96 b0 98 dc 1a 36 fc 82 e3 63 46 c0 68 37 64 c2 00 00 00 00 00 00 00 c7 

Changing byte 1/2.
Offset (hex) to change: 19e6
New value (hex): 74
The byte has been changed: *0x56e06605d9e6 = 74.
Changing byte 2/2.
Offset (hex) to change: 1c78
New value (hex): 74
The byte has been changed: *0x56e06605dc78 = 74.
The post-crack code integrity hash is:

	32 fb 00 d3 3a cc fe 94 22 66 cb 95 40 92 ab 76 c6 1b 9c 7d fd 7f 00 00 fd 

The code's integrity is secure!

Ready to receive your license key!


Initial input:

	0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

This challenge is now mangling your input using the `md5` mangler. This mangler cannot be reversed.

This mangled your input, resulting in:

	29 e5 52 84 34 07 75 cf b6 eb 07 18 f6 4f 73 b9 00 00 00 00 00 00 00 00 00 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

	29 e5 52 84 34 07 75 cf b6 eb 07 18 f6 4f 73 b9 00 00 00 00 00 00 00 00 00 

Expected result:

	9d 09 92 2c 9a 17 d9 5d e5 02 19 1e c5 cd bc 89 00 00 00 00 00 00 00 00 00 

Checking the received license key!

You win! Here is your flag:
pwn.college{QQEDX_jb21wj1Xk1yKUZjJlOfPX.0VM3IDL4czN0czW}

```

### Flag 

> pwn.college{QQEDX_jb21wj1Xk1yKUZjJlOfPX.0VM3IDL4czN0czW}

--- 

## level11.1

### Solving

```
Reverse engineer this challenge to find the correct license key, but your input will be modified somehow before being compared to the correct key. This challenge allows you to patch 2 bytes in the binary, but performs an integrity check afterwards.
```

We first shove it into ghidra and examine the code.
```c
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  puts("###");
  printf("### Welcome to %s!\n",*param_2);
  puts("###");
  putchar(10);
  puts(
      "This license verifier software will allow you to read the flag. However, before you can do so , you must verify that you"
      );
  puts(
      "are licensed to read flag files! This program consumes a license key over stdin. Each program  may perform entirely"
      );
  puts(
      "different operations on that input! You must figure out (by reverse engineering this program)  what that license key is."
      );
  puts("Providing the correct license key will net you the flag!\n");
  puts(
      "Unfortunately for you, the license key cannot be reversed. You\'ll have to crack this program .\n"
      );
  local_e0 = 0;
  local_d0 = 0x100000;
  do {
    iVar1 = local_e0 << 0xc;
    local_e0 = local_e0 + 1;
    iVar1 = mprotect((void *)(local_d0 + iVar1),0x1000,7);
  } while (iVar1 == 0);
  puts("In order to ensure code integrity, the code will be hashed and verified.\n");
  MD5_Init(&local_c8);
  for (local_dc = 0; local_dc < local_e0 + -1; local_dc = local_dc + 1) {
    MD5_Update(&local_c8,(void *)((local_dc << 0xc) + local_d0),0x1000);
  }
  MD5_Final(local_68,&local_c8);
  for (local_d8 = 0; local_d8 < 2; local_d8 = local_d8 + 1) {
    printf("Changing byte %d/2.\n",(ulong)(local_d8 + 1));
    printf("Offset (hex) to change: ");
    __isoc99_scanf(&DAT_001033a8,&local_e2);
    printf("New value (hex): ");
    __isoc99_scanf(&DAT_001033be,&local_e3);
    *(byte *)(local_d0 + (ulong)local_e2) = local_e3;
    printf("The byte has been changed: *%p = %hhx.\n",(ulong)local_e2 + local_d0,(ulong)local_e3);
  }
  MD5_Init(&local_c8);
  for (local_d4 = 0; local_d4 < local_e0 + -1; local_d4 = local_d4 + 1) {
    MD5_Update(&local_c8,(void *)((local_d4 << 0xc) + local_d0),0x1000);
  }
  MD5_Final(local_58,&local_c8);
  iVar1 = memcmp(local_68,local_58,0x10);
```

Like before this will never return 0. 

![image](https://github.com/user-attachments/assets/be168059-7c87-422c-b718-4f382e029c42)

```
0010220d 85 c0           TEST       EAX,EAX
0010220f 0f 85 e1        JNZ        LAB_001022f6
         00 00 00
```
Over here we know that it will never be 0 hence it will always jump. Trying to change this to 74 causes a seg fault.

hence we cannot use the same soln as the condition and assembly jumps are different

This is because the JNZ is not using its regular ``75`` encoding but rather its ``0f 85`` which is also known as near jump. Meaning if we want to convert this jump We must use the JE code for Near jump as well which is ``0f 84`` 

Now ``0010220f`` essentially is the ``0f`` part whereas ``00102210`` accesses the 85 part Meaning this is what we need to access and change.

Now that we know how to get through the first if statement the second if statement is a bit easier same as before challs

![image](https://github.com/user-attachments/assets/5b093dc0-099a-48d6-a69d-90b75be58404)

```
001022f0 85 c0           TEST       EAX,EAX
001022f2 75 2c           JNZ        LAB_00102320
```
This is a so called short jump hence we can just access ``22f2`` and change the hex value to ``74``

```shell
hacker@reverse-engineering~level11-1:/challenge$ ./babyrev-level-11-1 
###
### Welcome to ./babyrev-level-11-1!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Unfortunately for you, the license key cannot be reversed. You'll have to crack this program.

In order to ensure code integrity, the code will be hashed and verified.

Changing byte 1/2.
Offset (hex) to change: 2210
New value (hex): 84
The byte has been changed: *0x5dc08f4f6210 = 84.
Changing byte 2/2.
Offset (hex) to change: 22f2
New value (hex): 74
The byte has been changed: *0x5dc08f4f62f2 = 74.
The code's integrity is secure!

Ready to receive your license key!


Checking the received license key!

You win! Here is your flag:
pwn.college{YBTeIvs46sB09K-EK1GySKS-p-w.0lM3IDL4czN0czW}


hacker@reverse-engineering~level11-1:/challenge$
```

### Flag

> hacker@reverse-engineering~level11-1:/challenge$

---
