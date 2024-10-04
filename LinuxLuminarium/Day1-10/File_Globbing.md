# File Globbing

## Matching with *
```
This challenge requires us to change to directories using globbing.
globbing is where it expands identifiers like *, ? and [] into filenames and paths.
challenge specifically uses *.
We are supposed to enter the challenge directory using globbing where we need to pass the argument to at most 4 characters.
This will be considered as /ch* which is 4 characters.
And after entering we must run the /challenge/run.

to enter it by globbing we can do cd /ch* where the shell will look at any directory in root beginning with cha.
the * will match any characters after.

After this we do /challenge/run
This returns the flag

Flag -> 8yjHPjQZzzISI56ncw6TIbLfULa.dFjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/77d7dcc6-613f-4e84-845b-1b4c025197c6)

## Matching with ?
```
This challenge requires us to change to directories using globbing
challenge specifically uses ?
The ? unlike the * in globbing matches exactly 1 character from the directory.
Hence in this challenge we are supposed to reference c and l as ? in the directory name when navigating to it.

We can do this by changing cd /challenge to cd /?ha??enge

Once we have entered the directory we can enter /challenge/run
This returns the flag

Flag -> I2BaVpC3QzO41eGcyGUvCFM1Ljm.dJjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/8f74dae7-0ae3-4b23-ae16-c0999f6b961f)

## Matching with []
```
This challenge requires us to change directories using globbing
challenge specifically uses []
The [] in globbing matches exactly one character from a specific set of characters listed inside the brackets.
Hence in this challenge we already hinted that our files have the identifier file_b,  file_a, file_s, and file_h.
As such we have to access these files by passing all as an argument of the command /challenge/run

we first switch to the directory /challenge/files using cd

we then use the command /challenge/run file_[bash], bash signifies the file_b, file_a, file_s, file_h. I.E  their identifier.
doing this returns the flag.

Flag -> IdQQ-w7BWQ2cgaMnxL7OK38i4b4.dNjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/df50c325-49be-440f-8597-b8b5c2cb8852)

## Matching paths with []
```
This challenge requires us to run /challenge/run for the flag with a sinlge argument.
we must use bracket globs in the argument to search in specific files namely file_b, file_a, file_s, and file_h
using their absolute paths.
These files are located in /challenge/files.

Hence our command is /challenge/run /challenge/files/file_[bash]

Flag -> ISHPrPswN5qCSFP7f08GLIFlp-x.dRjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/d54c3470-c202-4580-bc48-d98520591d39)

## Mixing Globs
```
This challenge requires us to make a glob that will come under 3 file names "challenging", "educational", and "pwning".
It also must be 6 characters or less.

We first swap to the directory /challenge/files and do ls
After doing this we can see all the files in the directory including the ones we need to glob.

Over here we can pass an argument to the run command like before.
/challenge/run (Argument)
our Arguemnt here will be [CEP]* as [CEP] accounts for the starting of each file.
We can do it like this as each file name has a unique alphabet at the start and * just continues listing each file path for the letter.
Hence running this /challenge/run [cep]* returns our flag.

Flag -> gVuDI-werY1rB1ugguyHnzcxfgI.dVjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/ec44feb4-1b1a-4170-ab35-586f41079ed3)

## Exclusionary Globbing
```
In this challenge we are supposed to use the [] to filter out glob paths.
in this one we specifically need to filter out files that begin with p, w, n.
We can negate it with the syntax of [!pwn]

first we swap to cd /challenge/files.
Then we do /challenge/run [!pwn]*
This excludes pwn and finishes the path to the rest of the files using *.
This returns the flag.

Flag -> 8dapwwVqtNyvinBYf1BREKNjzNy.dZjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/37985bf0-75fd-47f5-93d6-212e2c7ab303)




