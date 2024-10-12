# Processes and Jobs

---

## Listing Processes

### Description
In this challenge the goal is to find the renamed challenge executable which is already running as a process. The challenge involves using the `ps` command to list running processes identifying the renamed executable and re-executing it to retrieve the flag.

### Info / Stuff We Should Know
- **Listing processes with `ps`**: The `ps` command allows you to see a snapshot of the currently running processes. By using the appropriate options you can display more details about these processes.
  - Example command:
    ```bash
    ps -ef
    ```
    This will list all running processes including the PID PPID (parent process ID) and the command that launched each process.

- **Identifying the challenge process**: The executable for the challenge has been renamed and you will need to find it in the list of processes based on its name (which starts with `/challenge/`).

### Step-by-Step Solution

**Command to list all running processes**:
```bash
ps -ef
```
This command will output the list of all processes running on the system. Look for a process whose `CMD` column contains `/challenge/`:

Example output:
```bash
root          68       1  0 19:11 ?        00:00:00 /challenge/15162-run-26359
```

The process `/challenge/15162-run-26359` is the renamed executable we need.

**Command to re-run the challenge executable**:
```bash
/challenge/15162-run-26359
```
Running this command will execute the challenge process again, and the flag will be displayed as output.

### Flag
> pwn.college{U5Iy_Ti7MnsZoNP_3RI2nFgdgmW.dhzM4QDL4czN0czW}

![image](https://github.com/user-attachments/assets/7627ecd0-7218-4320-acf3-99cb845c4d31)

---

## Killing Processes 

### Description
In this challenge the goal was to terminate a process named `/challenge/dont_run` that was preventing the `/challenge/run` command from executing. To do this we needed to use the `kill` command which terminates a process by sending it a signal. 

### Info / Stuff We Should Know
- **Viewing running processes**: The `ps -e` command lists all running processes on the system. This is useful for finding the process ID (PID) of a specific process.
  - Example:
    ```bash
    ps -e
    ```
- **Using `kill` to terminate a process**: Once you have identified the PID of the process you want to terminate you can use the `kill` command to stop it.
  - Example:
    ```bash
    kill <PID>
    ```
 
### Step-by-Step Solution

**Command to list all running processes**:
```bash
ps -e
```
This command listed the processes and identified the PID of the process to kill (in this case the `sleep` process with PID `74`).

**Command to kill the `sleep` process**:
```bash
kill 74
```

**Command to execute the challenge after killing the process**:
```bash
/challenge/run
```
This command succeeded after terminating the blocking process and the challenge was completed.

### Flag
> 4EAxrbsApabr201sThzVyKUKhiK.dJDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/259cabfa-8d56-4a28-991a-79252808efca)

---

## Interrupting Processes

### Description
In this challenge the objective was to use the `Ctrl-C` keyboard shortcut to interrupt a running process. This command sends an interrupt signal to the currently active process in the terminal prompting it to terminate cleanly.

### Info / Stuff We Should Know
- **What is Ctrl-C?**: The `Ctrl-C` combination is a keyboard shortcut used in terminal environments to send an interrupt signal (SIGINT) to a running process. This is useful for stopping processes that are waiting for user input or taking too long to execute.
  
- **How it works**: When `Ctrl-C` is pressed it typically allows the application to perform any necessary cleanup before terminating. This is different from the `kill` command which forcibly stops a process.

### Step-by-Step Solution

**Command to run the challenge**:
```bash
/challenge/run
```
Output:
```
I could give you the flag... but I won't until this process exits. Remember you can force me to exit with Ctrl-C. Try it now!
```

**Command to interrupt the process**:
- While the process is running press:
```plaintext
Ctrl-C
```
This action sends the interrupt signal causing the process to terminate and allowing us to receive the flag.

### Flag
> IwzD1UZxK_fEDr1JnIA1-GAO8Zr.dNDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/b89310f9-fe5a-47a2-a007-997074c65c9c)

---

## Suspending Processes

### Description
In this challenge the objective was to use the `Ctrl-Z` keyboard shortcut to suspend a running process. This command temporarily halts the active process allowing you to launch another instance of the same process in the terminal.

### Info / Stuff We Should Know
- **What is Ctrl-Z?**: The `Ctrl-Z` combination is a keyboard shortcut used in terminal environments to send a suspend signal (SIGTSTP) to a running process. This is useful for pausing processes that may be waiting for input or that you need to temporarily halt.

- **How it works**: When `Ctrl-Z` is pressed the currently running process is suspended and moved to the background. You can then start another instance of the same process or execute other commands. The suspended process can be resumed later using commands like `fg` (to bring it back to the foreground) or `bg` (to continue running it in the background).

### Step-by-Step Solution

**Command to run the challenge**:
```bash
/challenge/run
```
This returns us with the current processes in the terminal and this prompt ->
[I'll only give you the flag if there's already another copy of me running in this terminal... Let's check!

I don't see a second me!

To pass this level, you need to suspend me and launch me again! You can 
background me with Ctrl-Z or, if you're not ready to do that for whatever 
reason, just hit Enter and I'll exit!]

**Command to suspend the process**:
- While the process is running, press:
```plaintext
Ctrl-Z
```
This action suspends the process, allowing it to be moved to the background.

**Command to launch another instance**:
- Now that the first process is suspended start another instance by running:
```bash
/challenge/run
```
This returns the flag :D

### Flag
> Mb3G4Jg7QP9KG2qr7B0Da_FYr1L.dVDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/80d1b27e-b4ec-4529-9e6a-eb14170c9b70)

--- 

## Resuming Processes

### Description
In this challenge the objective was to use the `Ctrl-Z` keyboard shortcut to suspend a running process and then resume it using the `fg` command. This allows the user to temporarily pause the active process and bring it back to the foreground for interaction.

### Info / Stuff We Should Know
- **What is fg?**: The `fg` command is a built-in shell command used to resume a suspended process and bring it back to the foreground. This allows the user to interact with the process as if it had never been suspended.

- **How it works**: When you suspend a process with `Ctrl-Z` it is paused and moved to the background. The `fg` command can then be used to resume the process enabling it to continue running. If there are multiple suspended processes you can specify which one to resume using its job number (e.g. `fg %1` for the first job).

### Step-by-Step Solution

**Command to run the challenge**:
```bash
/challenge/run
```

This returns a prompt indicating that you should suspend the process:
Let's practice resuming processes! Suspend me with Ctrl-Z then resume me with the 'fg' command! Or just press Enter to quit me!

**Command to suspend the process**:
```plaintext
Ctrl-Z
```
This action suspends the process allowing it to be moved to the background. 

**Command to resume the suspended process**:
- To bring the suspended process back to the foreground run:
```bash
fg
```
This will then output the flag as the process has been resumed. We then press enter to exit it 


### Flag
> 83i72RCQxFQ8DSX6R-XXMjwqiN9.dZDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/37b48989-5c98-482a-976b-af0db44204b9)

---






