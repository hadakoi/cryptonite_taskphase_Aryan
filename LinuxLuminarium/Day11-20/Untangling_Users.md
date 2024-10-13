# Untangling Users

---

## Becoming root with su Challenge

### Description
In this challenge, participants will use the `su` (switch user) command to become the root user and retrieve the flag. While modern Linux systems primarily use `sudo` for elevating privileges, `su` is an older utility that requires the root password to switch users. The `su` command is a Set User ID (SUID) binary, allowing it to run with the permissions of the file owner, which is root.

### Info / Stuff We Should Know
- **su Command**: The `su` (switch user) command allows a user to switch to another user account, including root, provided they know the password for that account.
- **Root Password**: For this challenge, the root password is `hack-the-planet`.
- **root**: refers to the most privileged user on the system, also known as the superuser. The root user has complete control over the system and can perform any administrative tasks, such as:

- Installing, updating, or removing software
- Managing system files and directories
- Changing system-wide configurations
- Adding or removing users and groups
- Accessing and modifying files that other users cannot

### Step-by-Step Solution

 **Run the su Command**:
   - Command to switch to root user using `su`:
     ```bash
     su
     ```

 **Enter the Password**:
   - When prompted for the password, enter the provided root password:
     ```
     Password: hack-the-planet
     ```

 **Verify User Identity**:
   - Command to check the current user identity:
     ```bash
     whoami
     ```
   - Output:
     ```
     root
     ```

 **Retrieve the Flag**:
   - Command to display the flag:
     ```bash
     cat /flag
     ```
     
This displays the flag.

### Flag

> 0mfhZuDTg_Xg-BpXDzqIT_u9nf2.dVTN0UDL4czN0czW

![image](https://github.com/user-attachments/assets/78ab6def-ec4f-47ee-9e4c-4725af90470c)

---

## Switching to Other Users with SU

### Description
In this challenge, you need to use the `su` (switch user) command to switch to the `zardus` user and then run a program `/challenge/run`. The `su` command, when provided with a username as an argument, switches to that user’s environment after verifying their password. This allows you to act as that user for the current session.

### Info / Stuff We Should Know
- **su Command with a Username**: To switch to a specific user using `su`, provide the username as an argument to the `su` command:
  ```bash
  su username
  ```
  The system will prompt for the user's password. If the password is correct, you will log in as that user.

---

### Step-by-Step Solution

**Attempt to Switch to the `zardus` User**:
   - First, use the `su` command to switch to the `zardus` user. This command will ask for the `zardus` user's password.
     ```bash
     su zardus
     ```

**Input the Correct Password**:
     ```
     Password: dont-hack-me
     ```

**Confirm You Are Logged in as `zardus`**:
   - To verify that you've successfully switched to the `zardus` user, you can run the `whoami` command, which should return `zardus`.

**Run the Challenge Program**:
   - After confirming you're logged in as `zardus`, run the challenge program `/challenge/run`. This program will display the flag if everything is done correctly.
     ```bash
     /challenge/run
     ```

### Flag

> 07MYRxjxfjFhwCJ3yw8P4dZWUSF.dZTN0UDL4czN0czW

![image](https://github.com/user-attachments/assets/a7b6bc82-5b67-445c-a77f-73c3d504d641)

---

## Cracking Passwords with John the Ripper

### Description of the Challenge
In this challenge, you are provided with a leaked shadow file that contains a hashed password for the `zardus` user. Your task is to crack the password using John the Ripper, a password-cracking tool, and then use the `su` command to switch to the `zardus` user. After switching, you'll need to run a program to retrieve the flag.

### Info / Stuff We Should Know
- **John the Ripper**: A widely used password-cracking tool that cracks hashes using techniques like brute force or dictionary attacks. In this challenge, we'll use it to crack the hashed password from a shadow file leak.

### Step-by-Step Solution

 **Crack the Password Using John the Ripper**:
   - Run `John the Ripper` on the leaked shadow file to start cracking the password hash:
     ```bash
     john /challenge/shadow-leak
     ```
   - Wait for it to complete. The password for the `zardus` user will be revealed (`aardvark` in this case).

 **Switch to the Zardus User**:
   - Use the `su` command to switch to the `zardus` user:
     ```bash
     su zardus
     ```
   - Enter the cracked password (`aardvark`) when prompted.

 **Run the Challenge Program**:
   - After switching to the `zardus` user, run the challenge program to get the flag:
     ```bash
     /challenge/run
     ```
This returns the flag

### Flag

> wBylHyeH4bLorBzK5OMUv63J7-1.ddTN0UDL4czN0czW

![image](https://github.com/user-attachments/assets/44656b34-ceb3-4d59-ab24-8ed9fbd5e21c)

---

## Using Sudo to Read the Flag

### Description of the Challenge
In this challenge, you are provided with `sudo` access on a Linux system. Your task is to use `sudo` to read a protected flag file that requires root privileges. Unlike the old `su` method of elevating privileges, `sudo` allows you to run commands as the root user based on policies defined in the `/etc/sudoers` file. This method is more secure and manageable for system administration.

### Info / Stuff We Should Know
- **Sudo (superuser do)**: A command that allows a permitted user to execute a command as the superuser or another user, as specified by the security policy configured in `/etc/sudoers`. Unlike `su`, which switches the user context to the root user, `sudo` runs a specific command with elevated privileges.
  
- **/etc/sudoers**: The configuration file that defines user privileges for running commands with `sudo`. This file specifies who can run what commands on which machines.

### Step-by-Step Solution

1. **Check Access to the Flag**:
   - First, try to read the flag file without `sudo` to confirm that you don't have permission:
     ```bash
     cat /flag
     ```
   - You should see a permission denied message.

2. **Use Sudo to Read the Flag**:
   - Now, use `sudo` to run the `cat` command as root:
     ```bash
     sudo cat /flag
     ```
   - This command will authenticate you based on the sudo policy and allow you to read the flag.

### Flag
> QEZz_ZE1_VVaYmRBATTAqL4vz2X.dhTN0UDL4czN0czW

![image](https://github.com/user-attachments/assets/95b73672-b509-455f-a294-5837850b725d)

---
