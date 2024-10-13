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

1. **Run the su Command**:
   - Command to switch to root user using `su`:
     ```bash
     su
     ```

2. **Enter the Password**:
   - When prompted for the password, enter the provided root password:
     ```
     Password: hack-the-planet
     ```

3. **Verify User Identity**:
   - Command to check the current user identity:
     ```bash
     whoami
     ```
   - Output:
     ```
     root
     ```

4. **Retrieve the Flag**:
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

### Step-by-Step Solution

1. **Switch to the Zardus User**:
   - Use the `su` command to switch to the `zardus` user:
     ```bash
     su zardus
     ```

2. **Enter the Password**:
   - When prompted, enter the password for the `zardus` user:
     ```
     Password: dont-hack-me
     ```

3. **Run the Challenge Program**:
   - After switching to the `zardus` user, run the challenge program `/challenge/run`:
     ```bash
     /challenge/run
     ```

The output will display the flag if you have successfully switched to the `zardus` user.

### Step-by-Step Commands

- Command to switch to `zardus` user:
  ```bash
  su zardus
  ```
- Command to run the challenge program:
  ```bash
  /challenge/run
  ```

### Flag

> pwn.college{07MYRxjxfjFhwCJ3yw8P4dZWUSF.dZTN0UDL4czN0czW}

![image](https://github.com/user-attachments/assets/a7b6bc82-5b67-445c-a77f-73c3d504d641)

---

