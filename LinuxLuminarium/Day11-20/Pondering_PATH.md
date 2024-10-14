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

## Adding Commands

### Description
In this challenge, you need to create a shell script named `win` that will be executed by the `/challenge/run` program. The objective is to ensure that your `win` command can access the `cat` command to read the flag file. Since `/challenge/run` runs as root, it will call your `win` command, which should simply output the contents of the flag file.

To achieve this, you will manipulate the `PATH` environment variable so that your shell can locate both the `win` command and the `cat` command. However, if you overwrite the `PATH` variable with only the directory containing `win`, the command will not be able to find `cat`. You will need to choose your method carefully.

### Info / Stuff We Should Know
- **PATH Variable**: The `PATH` variable in a shell specifies the directories the shell searches for executable files. It consists of a list of directory paths separated by colons (`:`).
- **Finding Executables**: To find where executables such as `cat` are located, you can check the current `PATH` variable and navigate through the directories listed.
- **Using Shell Built-ins**: The `read` command is a built-in function in Bash that can read data from files. It does not depend on the `PATH`, so it can be used to directly access the flag file without needing to find `cat`.

Here’s the revised hint explanation with three sections for each method based on the provided hints:

### Step-by-Step Solution

#### Hint Explanation

##### Method 1: Locating the `cat` Command
To successfully invoke the `cat` command from your `win` script, you first need to determine its absolute path. This can be done by using the `which` command, which reveals where the `cat` program is located on the filesystem. The `cat` command must reside in a directory listed in your `PATH` variable. You can check your `PATH` using `echo $PATH` and then search through its entries (separated by `:`) to find the directory containing `cat`. After identifying the absolute path, you can reference it directly in your `win` script.

##### Method 2: Adding the Current Directory to `PATH`
Instead of searching for the `cat` command, you can modify the `PATH` variable to include your current directory, where your `win` script will be located. By appending `./` to the existing `PATH`, the shell will be able to find and execute your `win` script directly. This approach allows you to create a simple `win` script that directly calls `cat` without needing to specify its absolute path, as long as the script and the `cat` command exist in the same `PATH` hierarchy.

##### Method 3: Using `read` to Access the Flag
If you want to avoid relying on the `cat` command altogether, you can use the built-in `read` functionality in Bash to access the flag file. The `read` command allows you to read data from a file into a variable, and since it's a shell built-in, it is not affected by the `PATH` variable. By redirecting input from `/flag` into a variable (e.g., `flag`) and then echoing that variable, you can access the contents of the flag file without any dependencies on external commands.

---

### Method 1: Locating the `cat` Command

1. **Find the Location of `cat`**:
   ```bash
   which cat
   /run/workspace/bin/cat
   ```
   This command reveals the absolute path to the `cat` executable, which will be useful for invoking it from your `win` script.

2. **Create the `win` Script**:
   ```bash
   echo '/usr/bin/cat /flag' > win
   ```
   This command writes the script `win`, which will execute `cat` to read the `/flag` file.

3. **Update the `PATH`**:
   ```bash
   export PATH=$PATH:./
   ```
   This command appends the current directory (`./`) to the existing `PATH`, allowing the shell to find your `win` script.

4. **Execute the Challenge**:
   ```bash
   /challenge/run
   ```
   
   This returns the Output.

---

### Method 2: Adding the Current Directory to `PATH`

1. **Update the `PATH`**:
   ```bash
   export PATH=$PATH:./
   ```
   This command adds the current directory to the `PATH`, allowing your shell to find the `win` script.

2. **Create the `win` Script**:
   ```bash
   echo 'cat /flag' > win
   ```
   This command creates a script named `win` that directly uses the `cat` command to read the `/flag` file.

3. **Execute the Challenge**:
   ```bash
   /challenge/run
   ```

   This returns the Output.

---

### Method 3: Using `read` to Access the Flag
1. **Create the `win` Script with `read`**:
   ```bash
   echo 'read flag < /flag; echo $flag' > win
   ```
   This command writes a script that reads the flag directly into a variable named `flag` and then echoes its value.

2. **Update the `PATH`**:
   ```bash
   export PATH=$PATH:./
   ```
   Again, this command adds the current directory to the `PATH`, allowing your shell to find the `win` script.

3. **Execute the Challenge**:
   ```bash
   /challenge/run\
   ```
   
   This returns the Output.

---

### Flag

> 8yZw6vRkaP4QmuIA7I4fAtanHGt.dZzNyUDL4czN0czW

First Method. 

![image](https://github.com/user-attachments/assets/8c1044f2-8856-4bd6-aeb3-726e9cf47c5b)

<br>

Second Method. 

![image](https://github.com/user-attachments/assets/0d8a8112-5369-4052-974f-6af7d1f13911)

<br>

Third Method.

![image](https://github.com/user-attachments/assets/46ad3e4c-4fbd-48df-8add-89865e2119a5)

---



