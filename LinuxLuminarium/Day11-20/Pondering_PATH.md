# Pondering PATH

---

## The PATH Variable Challenge

### Description of the Challenge
In this challenge, we need to prevent the `/challenge/run` program from finding the `rm` command so that it fails to delete the flag. The solution involves manipulating the `PATH` environment variable, which tells the shell where to search for commands. By clearing the `PATH`, we can ensure that the `rm` command cannot be found.

### Info / Stuff We Should Know
- **PATH Variable**:
  - The `PATH` variable contains a list of directories where the shell looks for executable commands like `ls`, `rm`, etc. If the command is not in any of these directories, the shell cannot find and execute it.
  
  - **Clearing the PATH**:
    - By setting `PATH=""`, we remove all directories from the list, so no commands can be found.
    - Any child processes (like `/challenge/run`) will inherit the current shell's `PATH`, so it will also fail to find `rm` if we clear `PATH` before running the program.

### Step-by-Step Solution

1. **Check the Current PATH**:
   - View the directories listed in the current `PATH` variable:
     ```bash
     echo $PATH
     ```
   - Output: 
     ```bash
     /run/challenge/bin:/run/workspace/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
     ```

2. **Clear the PATH**:
   - Set the `PATH` variable to an empty string so that no directories are searched:
     ```bash
     PATH=""
     ```

3. **Run the Program**:
   - Execute the `/challenge/run` program. Since `rm` cannot be found, the flag will not be deleted:
     ```bash
     /challenge/run
     ```

The Flag will now be displayed.

### Flag

> EuLw3I4c7DK2zKcCaoPDzCpH7Bb.dZzNwUDL4czN0czW

![image](https://github.com/user-attachments/assets/8e0ef016-77e5-4092-87fe-4314832fcf6c)

---

## Setting the PATH Variable Challenge

### Description of the Challenge
In this challenge, the goal is to set the `PATH` variable to include a specific directory so that the `/challenge/run` program can find and execute the `win` command, which is located in the `/challenge/more_commands/` directory. By modifying the `PATH`, we allow the program to run the `win` command using its bare name.

### Info / Stuff We Should Know
- **PATH Variable**:
  - The `PATH` variable contains directories that the shell uses to search for executable commands.
  - By adding or changing directories in the `PATH`, we can make custom scripts or programs available to be executed without typing their full paths.

- **Updating PATH**:
  - You can either replace the existing `PATH` with a new directory or append/prepend a new directory to the existing `PATH`.
  - In this challenge, we only need to include `/challenge/more_commands/`, so we can replace `PATH` entirely.

### Step-by-Step Solution

1. **Set the PATH**:
   - Update the `PATH` variable to include only `/challenge/more_commands/`:
     ```bash
     PATH=/challenge/more_commands
     ```

2. **Run the Program**:
   - Execute the `/challenge/run` program, which will attempt to invoke the `win` command. Since `win` is now in the `PATH`, the program will find and run it:
     ```bash
     /challenge/run
     ```

This returns the flag.

### Flag

> EISQQphTOmn3E6jXSNjRMYtDyTg.dVzNyUDL4czN0czW

![image](https://github.com/user-attachments/assets/f94c815f-ef45-4365-9859-aea7e946bda0)

---



First Method. ![image](https://github.com/user-attachments/assets/29cd07f3-0e00-49b5-b4d5-fdeed1c45e38)
Second Method. ![image](https://github.com/user-attachments/assets/59bd2284-3ce5-4502-8144-13287c30325c)
Third Method. ![image](https://github.com/user-attachments/assets/3f128c28-f92a-481c-bdec-b03516a4095e)


