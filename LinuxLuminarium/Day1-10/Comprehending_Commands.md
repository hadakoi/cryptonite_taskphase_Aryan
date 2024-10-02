# Comprehending Commands

## cat: not the pet, but the command!

```

In this challenge we are asked to read a file directly using cat. The flag is stored in the file flag which we found from doing *ls*
Hence we use the command *cat flag*
This returns the flag.

(p.s i will still pet tha cat)
```

![image](https://github.com/user-attachments/assets/2bc75152-7436-4053-a366-1f2634f6aae5)

## catting absolute paths
```
As it is asking us to use an absolute path when referencing the flag file we must do cat /flag. Before we use the relative path ( relative path means looking in current directory )
using it as an absolute path means we are searching for the file flag from the / directory which is root.

This returns the flag.

(p.s if we had absolute paths irl for petting cats does that mean we can pet cats from anywhere..... hmmm)
```
![image](https://github.com/user-attachments/assets/cddb3aba-bfeb-4a76-9e9d-57f3997fe14a)

## more catting practice
```
In this challenge we are asked to read the flag file from the crazy directory and we cannot use cd. This means we must use an absolute path.
However there is no directory or path we can possibly consider. hence we first do ls. this lists out directories desktop and x. We first try cd x.

To which we are given where the user has actually hidden the flag file. This prompt is given by
you MUST chase pass 'cat' the absolute path of where I put it on the filesystem (which is /opt/pwndbg/tests/flag).

hence we do the command *cat /opt/pwndbg/tests/flag* which gives an absolute path to flag

(p.s this level shoulda been called more petting practice)
```
![image](https://github.com/user-attachments/assets/9a1e1e0e-1a37-4de9-bf5f-4e5de3f4b99f)


## grepping for a needle in a haystack
```
In this challenge we are given a path to a text file where there are 1000s of lines of data code. to search for our flag here we must
Use the grep command which has the syntax *grep "stringtosearch" path* in this context we are given the path and know the starting
part string of each flag hence our command is *grep "pwn.college" /challenge/data.txt*

This returns our flag.
```
![image](https://github.com/user-attachments/assets/41d54ebe-53ff-4efc-8ffb-6ca2bd2a1dac)

## listing files
```
```

