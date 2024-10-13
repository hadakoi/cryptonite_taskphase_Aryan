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

## Groups and Files

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

## Fun with Group Names

### Description
In this challenge we explore a situation where the user's group name has been randomized. Instead of the usual `hacker` group the group name is now different and must be identified using the `id` command. The goal is to find the current group name change the group ownership of the `/flag` file to this group using `chgrp` and then read the flag.

### Info / Stuff We Should Know
- **Randomized Group Names**: The user's group name has been randomized. We need to determine the group name before proceeding with the challenge.
  - The `id` command shows the group the user belongs to.
  - The `chgrp` command is used to change the group ownership of a file.
  
- **chgrp**: Changes the group ownership of a file.
  - Syntax: `chgrp [new-group] [file]`
  
### Step-by-step Solution
1. First, find out which group the `hacker` user currently belongs to using the `id` command:
   ```bash
   id
   ```
   This will show the group name (e.g., `grp1318`).

2. Change the group ownership of the `/flag` file to the correct group:
   ```bash
   chgrp grp1318 /flag
   ```

3. Verify the group ownership has been updated by listing the details of the `/flag` file:
   ```bash
   ls -l /flag
   ```

4. Now use `cat` to read the flag:
   ```bash
   cat /flag
   ```

The flag will be displayed completing the challenge.

### Flag

> gLpLQXmcpuwtvVoxhAlZtUMIqFn.dJzNyUDL4czN0czW

![image](https://github.com/user-attachments/assets/c94773ef-8582-487b-a64f-dfde011f0ba8)

---

## Changing Permissions 

### Description
In this challenge we are tasked with modifying the file permissions of the `/flag` file to gain access to it. Normally changing permissions requires write access to the file but for this challenge the `chmod` command has been made all-powerful allowing us to modify the permissions of any file without requiring ownership or write access.

The flag file is owned by `root` and it initially has very restrictive permissions (`-r--------`) meaning only the owner (root) can read the file, and no one else (group or others) has any access. Our goal is to change these permissions to allow the `hacker` user to read the file and retrieve the flag.

### Info / Stuff We Should Know
- **File Permissions**:
  - `r`: Read permission.
  - `w`: Write permission.
  - `x`: Execute permission.
  - `-`: No permission.
  
- **chmod**: Changes file permissions using the `WHO+/-WHAT` format, where `WHO` can be:
  - `u` for the file owner (user).
  - `g` for the group.
  - `o` for others (all users not in the group or the owner).
  - `a` for all (user, group, and others).

- **Permission Modifications**:
  - `o+r`: Adds read permission for others.
  - `o-w`: Removes write permission for others (if present).
  
### Step-by-step Solution
1. Check the initial permissions of the `/flag` file:
   ```bash
   ls -l /flag
   ```
   
   -r-------- 1 root root 58 Oct 13 09:05 /flag

2. Since the file is owned by `root` and only `root` has read access, we will use the `chmod` command to grant read access to others (i.e., the `hacker` user):
   ```bash
   chmod o+r /flag
   ```

3. Verify that the file’s permissions have been updated to allow others to read the file:
   ```bash
   ls -l /flag
   ```

   -r-----r-- 1 root root 58 Oct 13 09:05 /flag

4. Now, use the `cat` command to read the contents of the `/flag` file:
   ```bash
   cat /flag
   ```

The flag will be displayed, completing the challenge.

### Flag

> 8GOvPnM30DJI8HtGuKyw4eD8npa.dNzNyUDL4czN0czW

![image](https://github.com/user-attachments/assets/5ab6e1bd-e044-46c0-92cc-8af6ac01ee26)

---

## Executable Permissions Challenge

### Description
In this challenge, we explored the concept of execute permissions in Linux. The objective was to make the `/challenge/run` program executable so that we could successfully run it and retrieve the flag.

### Info / Stuff We Should Know
- **File Permissions**: In Linux, file permissions control the ability to read, write, or execute a file. They are categorized into three groups: owner, group, and others.
- **Permission Representation**: The permissions are represented in the `ls -l` format:
  - `r` - read permission
  - `w` - write permission
  - `x` - execute permission
  - `-` - no permission
- **Commands**: The `chmod` command is used to change file permissions.

### Step-by-Step Solution

1. **Check Initial Permissions**:
   Verify the current permissions of the `/challenge/run` file.
   ```bash
   ls -l /challenge/run
   ```

2. **Modify Permissions**:
   Add execute permission for the user (owner) using the `chmod` command.
   ```bash
   chmod u+x /challenge/run
   ```

3. **Verify Permission Changes**:
   Confirm that the permissions have been updated.
   ```bash
   ls -l /challenge/run
   ```

4. **Execute the Program**:
   Run the `/challenge/run` program to obtain the flag.
   ```bash
   /challenge/run
   ```

Upon successful execution the output displayed the flag

### Flag

> 0kTOCxc0AKIU4KyofAsTvAvycy0.dJTM2QDL4czN0czW

![image](https://github.com/user-attachments/assets/184545e7-c049-424f-9a82-185c0a455c98)

---

## Executable Permissions Challenge

### Description
In this challenge participants are tasked with changing the permissions of the `/challenge/pwn` file in specific ways through a series of rounds. Success in eight consecutive rounds allows the participant to modify the permissions of the `/flag` file to make it readable.

### Info / Stuff We Should Know
- **File Permissions**: In Linux, file permissions determine the level of access users have to files and directories. Permissions can be read (`r`), write (`w`), and execute (`x`).
- **Permission Groups**:
  - **User**: The owner of the file.
  - **Group**: Users who are part of the file's group.
  - **Others**: All other users.
- **Commands**: The `chmod` command modifies file permissions. It can add (`+`) or remove (`-`) permissions for user (`u`), group (`g`), and others (`o`).

### Step-by-Step Solution

1. **Round 0**:
   - Current permissions: `rw-r--r--`
   - Needed permissions: `rwxrwxr--`
   - Command:
     ```bash
     chmod u+x,g+wx /challenge/pwn
     ```
   - Result: Correct permissions set!

2. **Round 1**:
   - Current permissions: `rwxrwxr--`
   - Needed permissions: `r-xr-xr--`
   - Command:
     ```bash
     chmod u-w,g-w /challenge/pwn
     ```
   - Result: Correct permissions set!

3. **Round 2**:
   - Current permissions: `r-xr-xr--`
   - Needed permissions: `r-xr-xrw-`
   - Command:
     ```bash
     chmod o+w /challenge/pwn
     ```
   - Result: Correct permissions set!

4. **Round 3**:
   - Current permissions: `r-xr-xrw-`
   - Needed permissions: `---r-xrw-`
   - Command:
     ```bash
     chmod u-r,u-x /challenge/pwn
     ```
   - Result: Correct permissions set!

5. **Round 4**:
   - Current permissions: `---r-xrw-`
   - Needed permissions: `------rw-`
   - Command:
     ```bash
     chmod g-r,g-x /challenge/pwn
     ```
   - Result: Correct permissions set!

6. **Round 5**:
   - Current permissions: `------rw-`
   - Needed permissions: `------rwx`
   - Command:
     ```bash
     chmod o+x /challenge/pwn
     ```
   - Result: Correct permissions set!

7. **Round 6**:
   - Current permissions: `------rwx`
   - Needed permissions: `------r-x`
   - Command:
     ```bash
     chmod o-w /challenge/pwn
     ```
   - Result: Correct permissions set!

8. **Round 7**:
   - Current permissions: `------r-x`
   - Needed permissions: `r--r--r-x`
   - Command:
     ```bash
     chmod u+r,g+r /challenge/pwn
     ```
   - Result: Correct permissions set!

9. **Final Step**:
   - After completing all 8 rounds, the ownership of the `/flag` file was changed, allowing permission modification.
   - Current permissions of `/flag`: `---------`
   - Command to make it readable:
     ```bash
     chmod u+r /flag
     ```

10. **Retrieve the Flag**:
    - Command to display the flag:
      ```bash
      cat /flag
      ```
Hence this returns the flag :D

### Flag

> EDrn77RF-UekQfVnxezTj59gDiR.dBTM2QDL4czN0czW

Also p.s there will be no ss of terminal this was way to long. D:

--- 

## Permission Setting Practice

### Description
In this challenge, participants are tasked with changing the permissions of the `/challenge/pwn` file in specific ways through a series of rounds. Success in eight consecutive rounds allows the participant to modify the permissions of the `/flag` file to make it readable.

### Info / Stuff We Should Know
- **File Permissions**: In Linux, file permissions determine the level of access users have to files and directories. Permissions can be read (`r`), write (`w`), and execute (`x`).
- **Permission Groups**:
  - **User**: The owner of the file.
  - **Group**: Users who are part of the file's group.
  - **Others**: All other users.
- **Commands**: The `chmod` command modifies file permissions. It can set (`=`), add (`+`), or remove (`-`) permissions for user (`u`), group (`g`), and others (`o`).

### Step-by-Step Solution

1. **Round 1**:
   - Current permissions: `rw-r--r--`
   - Needed permissions: `rwxr-xr--`
   - Command:
     ```bash
     chmod u=rw,g=rx /challenge/pwn
     ```
   - Result: Correct permissions set!

2. **Round 2**:
   - Current permissions: `rwxr-xr--`
   - Needed permissions: `r-xr-xrw-`
   - Command:
     ```bash
     chmod o+w /challenge/pwn
     ```
   - Result: Correct permissions set!

3. **Round 3**:
   - Current permissions: `r-xr-xrw-`
   - Needed permissions: `---r-xrw-`
   - Command:
     ```bash
     chmod u=,g=x /challenge/pwn
     ```
   - Result: Correct permissions set!

4. **Round 4**:
   - Current permissions: `---r-xrw-`
   - Needed permissions: `------rw-`
   - Command:
     ```bash
     chmod g-r,g-x /challenge/pwn
     ```
   - Result: Correct permissions set!

5. **Round 5**:
   - Current permissions: `------rw-`
   - Needed permissions: `------rwx`
   - Command:
     ```bash
     chmod o+x /challenge/pwn
     ```
   - Result: Correct permissions set!

6. **Round 6**:
   - Current permissions: `------rwx`
   - Needed permissions: `------r-x`
   - Command:
     ```bash
     chmod o-w /challenge/pwn
     ```
   - Result: Correct permissions set!

7. **Round 7**:
   - Current permissions: `------r-x`
   - Needed permissions: `r--r--r-x`
   - Command:
     ```bash
     chmod u+r,g+r /challenge/pwn
     ```
   - Result: Correct permissions set!

8. **Round 8**:
   - Current permissions: `r--r--r-x`
   - Needed permissions: `r--r-x--x`
   - Command:
     ```bash
     chmod g+x /challenge/pwn
     ```
   - Result: Correct permissions set!

9. **Final Step**:
   - After completing all 8 rounds, the ownership of the `/flag` file was changed, allowing permission modification.
   - Command to make it readable:
     ```bash
     chmod u+r /flag
     ```

10. **Retrieve the Flag**:
      ```bash
      cat /flag
      ```
Hence this returns the flag :D

### Flag

> sLtPIwf-34XkAJFBGHrdk5R8pyn.dNTM5QDL4czN0czW

Also p.s there will be no ss of terminal this was way too long. D:

---

## Set User ID (SUID) Bit Challenge

### Description
In this challenge, participants are tasked with adding the Set User ID (SUID) permission to the `/challenge/getroot` program. This allows the program to execute with the permissions of its owner (root), enabling users to spawn a root shell to access the flag. The SUID mechanism is commonly used in system administration tools like `su` and `sudo`.

### Info / Stuff We Should Know
- **SUID Permissions**: The SUID bit allows a user to run an executable with the permissions of the executable's owner, which is often root. The permission indicator appears as `s` in the owner's executable permission slot.
- **Command to Set SUID**:
  - You can set the SUID bit on a file using the `chmod` command:
    ```bash
    chmod u+s [program]
    ```
- **Example**:
  - Current permissions of a SUID-enabled file:
    ```bash
    hacker@dojo:~$ ls -l /usr/bin/sudo
    -rwsr-xr-x 1 root root 232416 Dec 1 11:45 /usr/bin/sudo
    ```
- **Security Note**: Be cautious when giving the SUID bit to executables owned by root, as this can create potential security vulnerabilities.

### Step-by-Step Solution

1. **Check Current Permissions**:
   - Command to check the permissions of the `/challenge/getroot` file:
     ```bash
     ls -l /challenge/getroot
     ```
     
     -rwxr-xr-x 1 root root 155 Jul 12 10:30 /challenge/getroot

2. **Set the SUID Bit**:
   - Command to set the SUID bit on the `/challenge/getroot` program:
     ```bash
     chmod u+s /challenge/getroot
     ```

3. **Verify the Change**:
   - Command to check the updated permissions:
     ```bash
     ls -l /challenge/getroot
     ```
     -rwsr-xr-x 1 root root 155 Jul 12 10:30 /challenge/getroot
 
4. **Execute the Program**:
   - Command to run the program:
     ```bash
     /challenge/getroot
     ```
     
     SUCCESS! You have set the suid bit on this program, and it is running as root! 
     Here is your shell...
 
5. **List Files in Root Shell**:
   - Command to list files in the root shell:
     ```bash
     ls
     ```
   - Possible Output:
     ```
     COLLEGE  Desktop  PWN  instructions  intercepted_data  myflag  not-the-flag  the-flag  x
     ```

6. **Retrieve the Flag**:
   - Command to display the flag:
     ```bash
     cat not-the-flag
     ```
     [FLAG] Here is your flag:
     [FLAG] pwn.college{oRdJKWViyunWAbwErnr4cO9tRnf.dNTM2QDL4czN0czW}
  

### Flag

> 0GwdkQdwRw79WCFOIQEs1kN8l8I.ddjN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/44c2cff4-5ee1-4a90-9b1d-36137f1d15ae)

---











