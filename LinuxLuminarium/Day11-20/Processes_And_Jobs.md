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

## Backgrounding Processes

### Description
In this challenge the objective was to suspend a running process using `Ctrl-Z` resume it in the background with the `bg` command and then launch another instance of the same process in the terminal. The challenge required you to ensure that one instance was running while the other was in the background.

### Info / Stuff We Should Know
- **What is bg?**: The `bg` command resumes a suspended process in the background. This allows the process to run while freeing up the terminal for additional commands.

- **Process States**:
  - **R**: Running
  - **S**: Sleeping (waiting for input)
  - **T**: Stopped (suspended with `Ctrl-Z`)
  - **+**: Indicates that the process is in the foreground

### Step-by-Step Solution

**Command to run the challenge**:
```bash
/challenge/run
```
The output will indicate that another instance of the process is required:
I'll only give you the flag if there's already another copy of me running *and not suspended* in this terminal... Let's check!
I don't see a second me!

To pass this level, you need to suspend me, resume the suspended process in the 
background, and then launch a new version of me! You can background me with 
Ctrl-Z (and resume me in the background with 'bg') or, if you're not ready to 
do that for whatever reason, just hit Enter and I'll exit!

**Command to suspend the process**:
```plaintext
Ctrl-Z
```

The output confirms that the process is suspended:
[1]+  Stopped                 /challenge/run

**Command to resume the process in the background**:
```bash
bg
```
This outputs:
The process is now running in the background, allowing you to proceed with the next command.

**Command to launch another instance**:
```bash
/challenge/run
```

This returns us the flag

### Flag
> IdOozWmM2Gomc_7H5IhTm6Pz3xI.ddDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/c08e7b17-29b8-4816-86e0-8ff9db29fb2a)

---

## Foreground Running Processes

### Description
In this challenge, you are required to manage process states by suspending a running process, moving it to the background, and then bringing it back to the foreground without re-suspending it. This task demonstrates the ability to manipulate processes within the terminal effectively.

### Info / Stuff We Should Know
- **fg Command**: The `fg` command is used to bring a backgrounded process back into the foreground, allowing you to interact with it directly.

### Step-by-Step Solution

**1. Start the Challenge**:
Launch the challenge with the following command:
```bash
/challenge/run
```
You will see the following prompt
To pass this level, you need to suspend me, resume the suspended process in the background, and *then* foreground it without re-suspending it! You can background me with Ctrl-Z (and resume me in the background with 'bg') or, if you're not ready to do that for whatever reason, just hit Enter and I'll exit!

**2. Suspend the Process**:

```plaintext
Ctrl-Z
```

**3. Resume the Process in the Background**:
```bash
bg
```

You will receive feedback:
Yay, I'm now running in the background! Because of that, this text will probably overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times to scroll this text out. After that, resume me into the foreground with 'fg'; I'll wait.

**4. Bring the Background Process to the Foreground**:
```bash
fg
```
Upon successfully bringing the process to the foreground, the prompt will indicate:
YES! Great job! I'm now running in the foreground. Hit Enter for your flag!
this returns us our Flag


### Flag

> Mrq33iFHAJkG3TlftvBziRk2rNw.dhDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/c3459d28-1a0f-4e43-86cc-f08e7afcb338)

---

## Starting Background Processes

### Description
In this challenge you will learn how to start a process in the background directly by appending an `&` to the command. This enables you to run tasks without occupying the terminal allowing you to execute additional commands while the background process runs.

### Info / Stuff We Should Know
- **Background Process**: A process that runs without occupying the terminal. You can continue to use the terminal for other commands.
- **Starting a Process in Background**: To launch a process in the background, append an `&` at the end of the command.
- **Process Confirmation**: When a command runs in the background it returns a job number and process ID (PID) confirming that it has started successfully.

### Step-by-Step Solution

**1. Start the Process in Foreground**:
Initially, when you try to start the process without appending `&`, it will run in the foreground:
```bash
/challenge/run
```
You will receive a message indicating that the command is running in the foreground:
You've started me in the foreground! You must start me in the background (by appending '&' to the command) to get the flag!


**2. Start the Process in the Background**:
```bash
/challenge/run &
```

The output will confirm that the process has started in the background, showing something like:

Yay, you started me in the background! Because of that, this text will probably overlap weirdly with the shell prompt, but you're used to that by now...

Anyways! Here is your flag!
returning our flag :D

### Flag

> wtLqbAq3De7TQ_NgM1XxWeV0SH6.dlDN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/f2537416-0fd8-4084-8508-b391ff623e0e)

---

## Process Exit Codes Write-up

### Description

In this challenge you need to retrieve the exit code from the command `/challenge/get-code` and then use that exit code as an argument for the command `/challenge/submit-code`.
we can find out the exit code for the last command by doing '$?' however we need to pass it literally as an argument.

### Info / Stuff We Should Know

- **Exit Codes**: Every command executed in the shell returns an exit code upon completion. Typically:
  - `0`: Indicates success.
  - Non-zero: Indicates failure (commonly `1`, but can vary).
- **Accessing Exit Code**: The exit code of the last executed command can be accessed using the special variable `$?`.

### Step-by-step Solution

1. **Run the Command to Get the Exit Code**:
   ```bash
   hacker@processes~process-exit-codes:~$ /challenge/get-code
   Exiting with an error code!
   ```
   
2. **Submit the Exit Code**:
   ```bash
   hacker@processes~process-exit-codes:~$ /challenge/submit-code $?
   ```

### Flag

> 8paMl6mZi7O5by3F73T9ygVSTjB.dljN4UDL4czN0czW

![image](https://github.com/user-attachments/assets/422a3790-1bbc-4c98-a33a-3c36284963e9)

---















