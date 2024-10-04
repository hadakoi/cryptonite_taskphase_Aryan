# Comprehending Commands

## **Cat: not the pet, but the command**

### Description
In this challenge we are asked to read a file directly using `cat`. 
The flag is stored in the file `flag`, which we found from doing `ls`. 
Hence we use the command `cat flag`. This returns the flag.

### Info / Stuff We Should Know
- The flag is located in a file named `flag`.
- We can list files in the directory using the `ls` command.

### Step-by-Step Solution

**Read the file flag**
```bash
cat flag
```

### Flag
> **Flag:** `854TpKiLLVYslvWrHZK7i0FXthF.dFzN1QDL4czNOCZW`

**(p.s i will still pet tha cat)**

![image](https://github.com/user-attachments/assets/2bc75152-7436-4053-a366-1f2634f6aae5)

---

## **catting absolute paths**

### Description
As it is asking us to use an absolute path when referencing the flag file we must use `cat /flag`.
Before we used the relative path (relative path means looking in the current directory). 
Using it as an absolute path means we are searching for the file `flag` from the `/` directory which is the root.

### Info / Stuff We Should Know
- Absolute paths start from the root directory (`/`), while relative paths depend on the current working directory.
- In this challenge, we need to reference the flag file using its absolute path.

### Step-by-Step Solution

**Read the flag file using an absolute path**
```bash
cat /flag
```

### Flag
> **Flag:** `09S57AQLuUvJDJ0uxzJxleeW9Nz.dlTM5QDL4czNOCZW`

**(p.s. If we had absolute paths in real life for petting cats, does that mean we can pet cats from anywhere? ... hmmm)**
![image](https://github.com/user-attachments/assets/cddb3aba-bfeb-4a76-9e9d-57f3997fe14a)

---

## **more catting practice**

### Description
In this challenge we are asked to read the flag file from the crazy directory and we cannot use cd.
This means we must use an absolute path.
However there is no directory or path we can possibly consider 

Hence we first do ls which lists out the directories desktop and x We first try cd x.

To which we are given a prompt indicating where the user has actually hidden the flag file.

This prompt states You MUST chase past cat the absolute path of where I put it on the filesystem which is /opt/pwndbg/tests/flag.

### Info / Stuff We Should Know
- We cannot change directories with cd so we must directly reference the flag file using its absolute path
- The prompt gives us a hint about the exact location of the flag file

### Step-by-Step Solution

**Read the flag file using its absolute path**
```bash
cat /opt/pwndbg/tests/flag
```
### Flag
> **Flag:** `U5A09mAMuBzIWCEMгnLOEAWHW2Y.dBjM5QDL4czN0czw`

**(p.s This level should have been called more petting practice)**
![image](https://github.com/user-attachments/assets/9a1e1e0e-1a37-4de9-bf5f-4e5de3f4b99f)

---

## **grepping for a needle in a haystack**

### Description
In this challenge we are given a path to a text file where there are 1000s of lines of data code. To search for our flag here we must use the grep command which has the syntax grep "stringtosearch" path. In this context we are given the path and know the starting part string of each flag. Hence our command is grep "pwn.college" /challenge/data.txt.

This returns our flag.

### Info / Stuff We Should Know
- The grep command searches for specific strings within files.
- The syntax for grep is grep "stringtosearch" path.

### Step-by-Step Solution

**Search for the flag in the text file**
```bash
grep "pwn.college" /challenge/data.txt
```
### Flag
> **Flag:** `EOR7-Bq_03RSTLyaJN4KiceHZ1c.ddTM4QDL4czN0cz`

![image](https://github.com/user-attachments/assets/41d54ebe-53ff-4efc-8ffb-6ca2bd2a1dac)

---
## **Listing Files**

### Description
In this challenge we are going to use `ls` to list the files for a 
certain directory by using the command `ls /directoryName`. 
This command lists out the files and programs in `directoryName`. 
In this case, we have to use `ls /challenge`. 
This gives us two file options: a `description.md` and an executable program with a 
random name. Now, to execute the program, we do `/challenge/filename`. 
This returns the flag.

### Info / Stuff We Should Know
- Use `ls /directoryName` to list files in a specific directory.
- You can execute a file by specifying its path.

### Step-by-Step Solution

**List the files and execute the program**
```bash
ls /challenge
```
```bash
/challenge/filename
```
### Flag
> **Flag:** `E20fWuuXfjcxYIECWMLd55oK0zg.dhjM4QDL4czN0czw`

![image](https://github.com/user-attachments/assets/3ec3d545-2a86-4235-b311-d55603884264)

---

## Touching Files

### Description
In this challenge, we are going to create two files in the `/tmp` directory. We can do this using a command when inside the `/tmp` directory, which is `touch filename`. In this case, we do `touch pwn` and `touch college`. Once these two files are created, we reference the `/challenge/run` program. This returns the flag.

### Info / Stuff We Should Know
- Use `touch filename` to create an empty file.
- You can create multiple files by running the `touch` command multiple times.

### Step-by-Step Solution

**switch to temp directory**
```bash
cd /tmp
```
**Create the files in tmp directory**
```bash
touch pwn
```
```bash
touch college
```
**run the program**
```bash
/challenge/run
```

### Flag
> **Flag:** `sxgoz1S6ca__b_TC1dDsDizXtMS.dBzM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/7512bc44-cc3c-423a-a822-65cb027ee174)

---

## Removing Files

### Description
In this challenge, we are asked to remove the file `delete_me` using the `rm` command. This file is in the home directory. So we run the command `rm delete_me`. Then we run the command `/challenge/check` which runs a program to see if it is not present. This returns the flag.

### Info / Stuff We Should Know
- Use `rm filename` to remove a file.
- Ensure that you are in the correct directory or specify the full path to the file.

### Step-by-Step Solution

**change directory to ~**
```bash
cd ~
```
**Delete the delete_me file**
```bash
rm delete_me
```
**run the programme**
```bash
/challenge/check
```
### Flag
> **Flag:** `MTlreXe5peZraeMLLo1ZaDXK-JE.dZTOwUDL4czN0czW`

![image](https://github.com/user-attachments/assets/94480784-b98c-4086-be1a-73b32417ac43)

---

## **Hidden Files**

### Description
In this challenge, we have to find a hidden file in the root directory. We switch to it simply by typing `cd /`. We look for the file by passing the command `ls -a`, where `-a` is the argument for all. Once we have the name of the file, we can open or read it using `cat /.filename`. This returns the flag.

### Info / Stuff We Should Know
- Use `cd /` to navigate to the root directory.
- Use `ls -a` to list all files, including hidden ones.
- Use `cat` to read the contents of a file.

### Step-by-Step Solution

**Find and read the hidden file**
```bash
cd /
```
**List all the files in root directory even the hidden ones**
```bash
ls -a
```
**Read the hidden file name**
```bash
cat /.filename
```
### Flag
> **Flag:** `Uv0tAnVzY17bMckrtkbUO9MApSt.dBTN4QDL4czN0czW`


![image](https://github.com/user-attachments/assets/761896c7-5cd6-4949-b328-04cee1994ea6)

---
## An epic filesystem quest

### Description
In this challenge we are asked to find a flag by following a path of breadcrumbs. 
We start by entering the root directory with `cd /`. 
After that we run `ls -a` where we see a file called GIST. 
We then use the command `cat GIST`. 
This tells us the file is located in the directory `/usr/share/icons/Adwaita/scalable-up-to-32/status`.

However we do not know the file name in this directory that contains the key
and entering the directory deletes the key.
So we do a test run with `ls /usr/share/icons/Adwaita/scalable-up-to-32/status` which shows us the next hint is trapped in MESSAGE-TRAPPED. 

Now that we know the path and where MESSAGE-TRAPPED is located
we can do `cat /usr/share/icons/Adwaita/scalable-up-to-32/status/MESSAGE-TRAPPED`.
This returns a hint saying we must change to a certain directory as the flag will 
become readable only when inside it. 
So we do `cd /usr/local/lib/python3.8/dist-packages/bleach/_vendor/html5lib/_trie`.

Upon entering this directory and running `ls`,
we see a file named INFO. We then do `cat INFO`,
which has a similar situation to swapping to a directory before accessing the next clue.
Hence we do `cd /usr/share/vim/vim81/lang/fi/LC_MESSAGES`.
Here we use `ls` and see the file is called BRIEF.
We `cat BRIEF` to receive another directory to go to and a hint that the file is hidden.

Next, we do `cd /usr/share/javascript/mathjax/jax/output/SVG/fonts/Neo-Euler/Fraktur` 
and then run `ls -a`, where we find the filename is .BLUEPRINT. 
Hence we do `cat .BLUEPRINT` 
which gives us another hint and like the second hint this one is trapped. 
So we run the command `ls /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace`. This gives us the filename SPOILER-TRAPPED. The command `cat /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace/SPOILER-TRAPPED` tells us that the next clue is in the `/usr/share/systemd` directory. 

Once we change the directory, we run `ls` to find the next filename of breadcrumbs, 
which is LEAD. We do `cat LEAD`, which presents us with the next directory and mentions 
that we need to use special viewing with `ls -a`. 
So we do `cd /opt/linux/linux-5.4/tools/usb/ffs-aio-example/multibuff/device_app` 
and then run `ls -a`. We see the filename is .EVIDENCE. Hence we do `cat .EVIDENCE`
which informs us that the next clue is in `/usr/share/cmake-3.16/Help/prop_inst`.

So we change to that directory with `cd /usr/share/cmake-3.16/Help/prop_inst`, 
and after that we run `ls -a`, where we see the filename is DISPATCH. 
We then `cat DISPATCH` to reveal the flag finally. (This reminded me of that one bandit level)

### Info / Stuff We Should Know
- Follow the hints provided in the files to find the flag.
- Use `cd` to change directories and `cat` to read file contents.

### Step-by-Step Solution

**Navigate and find the flag. (P.S -> i am not writing what each one does.)**
```bash
cd /

ls -a

cat GIST

ls /usr/share/icons/Adwaita/scalable-up-to-32/status

cat /usr/share/icons/Adwaita/scalable-up-to-32/status/MESSAGE-TRAPPED

cd /usr/local/lib/python3.8/dist-packages/bleach/_vendor/html5lib/_trie

ls

cat INFO

cd /usr/share/vim/vim81/lang/fi/LC_MESSAGES

ls

cat BRIEF

cd /usr/share/javascript/mathjax/jax/output/SVG/fonts/Neo-Euler/Fraktur

ls -a

cat .BLUEPRINT

ls /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace

cat /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Monospace/SPOILER-TRAPPED

cd /usr/share/systemd

ls

cat LEAD

cd /opt/linux/linux-5.4/tools/usb/ffs-aio-example/multibuff/device_app

ls -a

cat .EVIDENCE

cd /usr/share/cmake-3.16/Help/prop_inst

ls -a

cat DISPATCH
```
### Flag
> **Flag:** `c0oqKkRDMHxJNpPytbQ2sbvzELZ.dljM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/7e806dc3-8f8d-4fc8-8b1b-347f3549406d)
![image](https://github.com/user-attachments/assets/3c33d51f-5723-42af-a31b-1c24b4995c4b)

---
## **Making Directories**

### Description
In this challenge, we need to create a `/tmp/pwn` directory and make a file called `college` in it. Then we run `/challenge/run`.

To do this, we first switch to the `tmp` directory by using `cd /tmp`. Once this is done, we use the command `mkdir pwn`, which creates a directory inside `/tmp`. Next, we switch to the `pwn` directory with `cd pwn`. After that, we use the command `touch college`, which creates a file called `college` inside the `/tmp/pwn` directory. Finally, we can directly run `/challenge/run`.

This process returns the flag.

### Info / Stuff We Should Know
- Use `mkdir` to create a new directory.
- Use `touch` to create an empty file.

### Step-by-Step Solution

**Change to tmp directory**
```bash
cd /tmp
```
**makes directory pwn**
```bash
mkdir pwn
```
**moves into pwn directory**
```bash
cd pwn
```
**makes file college**
```bash
touch college
```
**runs the command to recieve the flag**
```bash
/challenge/run
```
### Flag
> **Flag:** `c6g1unb6WJAnA5K1dRu8mbOhOV3.dFzM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/35c36bd1-ef7a-456f-a711-1214405ed6f7)

---

## **finding files**

### Description
In this challenge we are expected to search the entire file system for a file called flag. 
Using the command they gave us for find called find / -name flag it will show us all paths with the name flag in its filename. 
This command searches in the root directory for all the file names with flag. It gives a list of files. Luckily catting the first path returns the flag.

### Info / Stuff We Should Know
- The find command searches for files in the file system.
- The syntax for searching files can vary based on the parameters used.
- SEARCHING File syntaxes ->
  1. find (searches current directory)
  2. find directoryname (searches in directoryname)
  3. find -name directoryname (searches for the directoryname)

### Step-by-Step Solution

**Search for the flag file in the entire file system**
```bash
find / -name flag
```
**Cat the first path returned to read the flag**
```bash
cat /path/to/flag
```

### Flag
> **Flag:** `kqzgDvgkOkoDhqupJmxJ8UKC2AV.dJzM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/cabb3d2a-9797-4c44-b5be-aee746d01615)


---
## **linking files**

### Description
In this challenge we are expected to use a symbolic link to make /challenge/catflag read the contents of /flag instead of /home/hacker/not-the-flag. Doing /challenge/catflag outputs About to read out the /home/hacker/not-the-flag file.

Hence now we create a symlink. This makes /home/hacker/not-the-flag act as a link to /flag. This will allow the return of the flag since it will follow the symlink and read /flag instead of /home/hacker/not-the-flag.

We do this using the command ln -s /flag /home/hacker/not-the-flag. Hence running the command /challenge/catflag returns the flag.

### Info / Stuff We Should Know
- A symbolic link allows us to reference a file or directory from another location.
- The symlink points to the actual file we want to read.

### Step-by-Step Solution

**Create a symbolic link to the flag file**
```bash
ln -s /flag /home/hacker/not-the-flag
```
**Read the flag file through the symbolic link**
```bash
/challenge/catflag
```

### Flag
> **Flag:** `4IjF5BNYn8Gq9tBlkFgPY3pxvE8.dlTM1UDL4czN0czW`

![image](https://github.com/user-attachments/assets/b736dad7-84b9-4d97-b882-77ce6742ebe6)

---

