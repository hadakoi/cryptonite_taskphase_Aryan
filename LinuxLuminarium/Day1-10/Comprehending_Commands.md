# Comprehending Commands

## cat: not the pet, but the command!

```

In this challenge we are asked to read a file directly using cat. The flag is stored in the file flag which we found from doing *ls*
Hence we use the command *cat flag*
This returns the flag.

Flag -> 854TpKiLLVYslvWrHZK7i0FXthF.dFzN1QDL4czNOCZW

(p.s i will still pet tha cat)
```

![image](https://github.com/user-attachments/assets/2bc75152-7436-4053-a366-1f2634f6aae5)

## catting absolute paths
```
As it is asking us to use an absolute path when referencing the flag file we must do cat /flag. Before we use the relative path ( relative path means looking in current directory )
using it as an absolute path means we are searching for the file flag from the / directory which is root.

This returns the flag.

Flag -> 09S57AQLuUvJDJ0uxzJxleeW9Nz.dlTM5QDL4czNOCZW

(p.s if we had absolute paths irl for petting cats does that mean we can pet cats from anywhere..... hmmm)
```
![image](https://github.com/user-attachments/assets/cddb3aba-bfeb-4a76-9e9d-57f3997fe14a)

## more catting practice
```
In this challenge we are asked to read the flag file from the crazy directory and we cannot use cd. This means we must use an absolute path.
However there is no directory or path we can possibly consider. hence we first do ls. this lists out directories desktop and x. We first try cd x.

To which we are given where the user has actually hidden the flag file. This prompt is given by
you MUST chase pass 'cat' the absolute path of where I put it on the filesystem (which is /opt/pwndbg/tests/flag).

hence we do the command *cat /opt/pwndbg/tests/flag* which gives an absolute path to flag.

Flag -> U5A09mAMuBzIWCEMгnLOEAWHW2Y.dBjM5QDL4czN0czw

(p.s this level shoulda been called more petting practice)
```
![image](https://github.com/user-attachments/assets/9a1e1e0e-1a37-4de9-bf5f-4e5de3f4b99f)


## grepping for a needle in a haystack
```
In this challenge we are given a path to a text file where there are 1000s of lines of data code. to search for our flag here we must
Use the grep command which has the syntax *grep "stringtosearch" path* in this context we are given the path and know the starting
part string of each flag hence our command is *grep "pwn.college" /challenge/data.txt*

This returns our flag.
Flag -> EOR7-Bq_03RSTLyaJN4KiceHZ1c.ddTM4QDL4czN0czw
```
![image](https://github.com/user-attachments/assets/41d54ebe-53ff-4efc-8ffb-6ca2bd2a1dac)

## listing files
```
In this challenge we are going to use ls to list our the files for a certain directory. by using the command *ls /directoryName*
This command would list out the files / programmes in directoryName. In this case we have to ls /challenge
This gives us 2 file options which is a description.md and a executable programme with a random name.
Now to execute the programme we do /challenge/filename
This returns the flag.

Flag -> E20fWuuXfjcxYIECWMLd55oK0zg.dhjM4QDL4czN0czw
```
![image](https://github.com/user-attachments/assets/3ec3d545-2a86-4235-b311-d55603884264)

## touching files
```
In this challenge we are going to create 2 files in the /tmp directory.
we can do this using a command when inside the /tmp directory which is touch filename.
in this case we do touch pwn and touch college
once these 2 files are created
we reference the /challenge/run programme

This returns the flag.
Flag -> sxgoz1S6ca__b_TC1dDsDizXtMS.dBzM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/7512bc44-cc3c-423a-a822-65cb027ee174)

## removing files
```
In this challenge we are asked to remove the file "delete_me" using the rm command.
This file is anyways in the home directory.
So we run the command *rm delete_me*.
Then we run the command /challenge/check which runs a programme to see if its not present.
This returns the flag.

Flag -> MTlreXe5peZraeMLLo1ZaDXK-JE.dZTOwUDL4czN0czW
```
![image](https://github.com/user-attachments/assets/94480784-b98c-4086-be1a-73b32417ac43)

## hidden files
```
In this challenge we have to find a hidden file in the root directory. we switch to it simply by typing *cd /*
We look for the file this by passing the command *ls -a* where -a is the argument for all.
Once we have the name of the file. we can open / read it using cat /.filename
This returns the flag.

Flag -> Uv0tAnVzY17bMckrtkbUO9MApSt.dBTN4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/761896c7-5cd6-4949-b328-04cee1994ea6)

## An epic filesystem quest 
```
In this challenge we are asked to find a flag by following a path of breadcrumbs.
Entering the root directory with cd /.
After that we ls -a where we see a file called GIST.
We put the command cat GIST.
This tells us the file is in the directory /usr/share/icons/Adwaita/scalable-up-to-32/status

However we do not know what the file is called in this directory that contains the key and entering the directory
deletes the key
So we do a test run where we ls /usr/share/icons/Adwaita/scalable-up-to-32/status
which shows us the next hint is trapped in MESSAGE-TRAPPED

Now as we know the path and where MESSAGE-TRAPPED is we can simply do cat /usr/share/icons/Adwaita/scalable-up-to-32/status/MESSAGE-TRAPPED

After this it returns a hint saying we must change to a certain directory as the flag will become readable only when inside it.
so we do cd /usr/local/lib/python3.8/dist-packages/bleach/_vendor/html5lib/_trie

Upon entering this file and doing ls we see a file name of INFO.
We then cat this which has a similar situation to swapping to directory before accessing the next clue.
Hence we do cd /usr/share/vim/vim81/lang/fi/LC_MESSAGES
Over here we use ls and see the file is called BRIEF. we cat BRIEF.
To which we get another directory to go to and a hint that the file is hidden.

Hence we do cd /usr/share/javascript/mathjax/jax/output/SVG/fonts/Neo-Euler/Fraktur
and then do ls -a
To which we find the filename is .BLUEPRINT. Hence we cat .BLUEPRINT
for which we get another hint and like the 2nd hint this one is trapped.
so we do the command ls /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace
This gives us the filename SPOILER-TRAPPED.
cat /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace/SPOILER-TRAPPED. gives us a hint that its in the /usr/share/systemd directory hence we cd /usr/share/systemd

once directory has changed we do ls to find the next filename of breadcrumbs
This is LEAD so we do cat LEAD. This presents us with the next directory and the fact we need to use special viewing with ls -a
so we do cd /opt/linux/linux-5.4/tools/usb/ffs-aio-example/multibuff/device_app
then ls -a
we see the file name is .EVIDENCE
hence we do cat .EVIDENCE which tells us the next clue is in /usr/share/cmake-3.16/Help/prop_inst

So we do cd /usr/share/cmake-3.16/Help/prop_inst
after that we do ls -a to which we see the filename is DISPATCH
we then cat DISPATCH to see the flag finally :D

Flag -> c0oqKkRDMHxJNpPytbQ2sbvzELZ.dljM4QDL4czN0czW

```
![image](https://github.com/user-attachments/assets/7e806dc3-8f8d-4fc8-8b1b-347f3549406d)
![image](https://github.com/user-attachments/assets/3c33d51f-5723-42af-a31b-1c24b4995c4b)


## Making Directories
```
In this challenge we need to create a /tmp/pwn directory and make a college file in it. Then we run /challenge/run.

To do this we first switch to the tmp directory by using cd /tmp. once this is done we use the command
mkdir pwn which creates a directory inside /tmp. Then we switch to the pwn directory with cd pwn.
After that we use the command touch college which creates a file called college inside the /tmp/pwn directory.
Then we can directly run the /challenge/run

This returns the flag.

Flag -> c6g1unb6WJAnA5K1dRu8mbOhOV3.dFzM4QDL4czN0czW 
```
![image](https://github.com/user-attachments/assets/35c36bd1-ef7a-456f-a711-1214405ed6f7)


## finding files
```
In this challenge we are expected to search the entire file system for a file called flag.
Using the command they gave us for find called find / -name flag it will show us all paths with the name flag in its filename.
This command searches in the root directory for all the file names with flag.
It gives a list of files luckily catting the first path returns the flag.

Flag -> kqzgDvgkOkoDhqupJmxJ8UKC2AV.dJzM4QDL4czN0czW

NOTE:
SEARCHING File syntaxes ->
1. find (searches current directory)
2. find directoryname (searches in directoryname)
3. find -name directoryname (searches for the directoryname)
```
![image](https://github.com/user-attachments/assets/cabb3d2a-9797-4c44-b5be-aee746d01615)


## linking files
```
In this challenge we are expected to use a symbolic link to make /challenge/catflag read the contents of /flag
instead of /home/hacker/not-the-flag.
doing /challenge/catflag
This  outputs About to read out the /home/hacker/not-the-flag file!

hence now we create a symlink.
This makes /home/hacker/not-the-flag act as a link to /flag.
this will allow the return of the flag since it will follow the symlink and read /flag instead of /home/hacker/not-the-flag.

we do this using the command ls -s /flag /home/hacker/not-the-flag
hence running the command /challenge/catflag returns the flag.


Flag -> 4IjF5BNYn8Gq9tBlkFgPY3pxvE8.dlTM1UDL4czN0czW
```
![image](https://github.com/user-attachments/assets/b736dad7-84b9-4d97-b882-77ce6742ebe6)





