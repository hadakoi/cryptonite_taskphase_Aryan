# Percieving Permissions

---

## Changing File Ownership

### Description
In this challenge we learn about file ownership in Linux and how to change the owner of a file using the `chown` command. The goal is to change the ownership of the `/flag` file which is originally owned by the `root` user to the `hacker` user. Once we have ownership we can read the flag.

### Info / Stuff We Should Know
- **File Ownership**: In Linux each file is owned by a user and a group. The file's owner has specific permissions to read write or execute the file.
  - The first `root` in the output from `ls -l` shows the file’s owner.
  - The second `root` shows the file's group owner.
- **chown**: The `chown` command allows changing the ownership of a file. 
  - Syntax: `chown [new-owner] [file]`
  - Only the `root` user can normally change file ownership.
  
### Step-by-step Solution
1. Check the ownership of the `/flag` file using `ls -l` (optional but informative):

   ```bash
   ls -l /flag
   ```
   You will see that the owner is `root`.

2. Change the ownership of the `/flag` file to the `hacker` user:
   ```bash
   chown hacker /flag
   ```

3. Once the ownership is changed read the flag:
   ```bash
   cat /flag
   ```

The flag will be displayed and the challenge is completed.

### Flag

> sYpWW-oaEX-Sy76dfChicQCjNex.dFTM2QDL4czN0czW

![image](https://github.com/user-attachments/assets/680aa04e-31d1-41c5-9572-b13ce0fa4bb7)

---

## Groups and Files Writeup

### Description
In this challenge, we learn about file groups in Linux and how they control access to files. Files have both an owning user and group, and group ownership determines who can access a file based on their group membership. The goal is to change the group ownership of the `/flag` file to the `hacker` group using the `chgrp` command, and then read the flag.

### Info / Stuff We Should Know
- **File Groups**: In Linux, files are owned by both a user and a group. A group can have multiple users, and file permissions can be set to allow group members to read, write, or execute a file.
  - The command `ls -l [file]` shows the user and group ownership of a file.
  
- **chgrp**: The `chgrp` command allows changing the group ownership of a file.
  - Syntax: `chgrp [new-group] [file]`

## Step-by-step Solution
1. Check the group ownership of the `/flag` file using `ls -l`:
   ```bash
   ls -l /flag
   ```
   You will see that the group is `root`.

2. Change the group ownership of the `/flag` file to the `hacker` group:
   ```bash
   chgrp hacker /flag
   ```

3. Verify that the group ownership has been changed:
   ```bash
   ls -l /flag
   ```

4. Now that the group ownership has been changed, read the flag:
   ```bash
   cat /flag
   ```

The flag will be displayed, completing the challenge.

### Flag

> 05acgqbOnmHayj_KNoMlZ6IWbJT.dFzNyUDL4czN0czW

![image](https://github.com/user-attachments/assets/0862d11c-e3e4-4c32-a05e-745c5a03901f)

---


