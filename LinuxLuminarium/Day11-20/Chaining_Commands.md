# Chaining Commands

---

## Chaining Commands with Semicolons

### Description of the Challenge
In this challenge, you are tasked with chaining two commands using a semicolon (`;`). The goal is to run `/challenge/pwn` and then `/challenge/college` in a single line, and successfully retrieve the flag. By chaining commands, you execute multiple commands in one go, without waiting for individual prompts.

### Info / Stuff We Should Know
- **Chaining with Semicolons**: A semicolon (`;`) allows you to execute multiple commands in a single line. Each command is executed sequentially, and once one finishes, the next command is executed, similar to pressing Enter after each command but without prompting between them.
  - Example:
    ```bash
    command1; command2
    ```
  - This runs `command1`, and once it completes, it immediately runs `command2`.

### Step-by-Step Solution

 **Chain the Commands**:
   - To solve this challenge, you need to run `/challenge/pwn` followed by `/challenge/college` in one line using a semicolon:
     ```bash
     /challenge/pwn; /challenge/college
     ```

### Flag

> c3_7hNJQ6GLEHcra2Ob3ljViHpj.dVTN4QDL4czN0czW

![image](https://github.com/user-attachments/assets/e3dfce85-5182-420a-9a07-f3cc67902f42)

---

## Your First Shell Script

### Description of the Challenge
In this challenge, you're tasked with chaining two commands, `/challenge/pwn` and `/challenge/college`, by placing them inside a shell script called `x.sh`. Once the shell script is created, you will execute it using `bash` to retrieve the flag.

### Info / Stuff We Should Know
- **Shell Script**: A shell script is a file containing a series of shell commands. Instead of typing each command manually, you can run the script to execute all the commands within it. The script is executed by invoking a shell (such as `bash`) and passing the script as an argument.
  - **Creating a Shell Script**: You can create a shell script using a text editor, like `nano`, and save it with a `.sh` extension (though this is not mandatory, it's a common convention).
  - **Executing a Shell Script**: After creating a shell script, it can be executed by running:
    ```bash
    bash scriptname.sh
    ```

### Step-by-Step Solution

1. **Create the Shell Script**:
   - Open the file using a text editor like `nano` or creates it:
     ```bash
     nano x.sh
     ```
   - Inside `x.sh`, write the following commands:
     ```bash
     /challenge/pwn
     /challenge/college
     ```

2. **Save and Exit the Script**:
   - After adding the commands, save the file and exit the editor.

3. **Run the Script**:
   - Execute the shell script using `bash`:
     ```bash
     bash x.sh
     ```
### Flag

> pwn.college{0dJAFjn157KCh1_pvRKq-wJB4je.dFzN4QDL4czN0czW}

![image](https://github.com/user-attachments/assets/b3d24007-8ce5-4424-b343-da200c93df31)
![image](https://github.com/user-attachments/assets/cafa9392-518a-4539-88a7-2ce8c1084bcc)
![image](https://github.com/user-attachments/assets/8981aec6-b033-4dd3-8418-6a899acb0927)

---

## Piping Output from Script

### Description of the Challenge
In this challenge, we need to create a script that calls two commands, `/challenge/pwn` and `/challenge/college`, and then pipe the output of the script into another program, `/challenge/solve`, using the pipe (`|`) operator.

### Info / Stuff We Should Know
- **Piping (`|`)**: Piping allows the output of one command to be sent directly as the input to another command. This technique is used frequently to chain operations.
  
  - **Example**:
    ```bash
    echo "Hello" | grep "H"
    ```
    This sends the output of `echo "Hello"` into the `grep` command, which filters lines that contain "H".

- **Shell Script**: A shell script is a text file that contains a series of commands for the shell to execute. In this case, we will create a script that runs two commands and pipes the combined output into another command.

### Step-by-Step Solution

1. **Create the Shell Script**:
   - First, create a shell script named `x.sh`:
     ```bash
     nano x.sh
     ```
   - Add the following commands to it:
     ```bash
     /challenge/pwn
     /challenge/college
     ```
   - These commands will be executed sequentially when the script is run.

2. **Save and Exit**:
   - Save the file and exit the editor.

3. **Run the Shell Script and Pipe Output**:
   - Execute the script and pipe its output into `/challenge/solve`:
     ```bash
     bash x.sh | /challenge/solve
     ```

   - The output from `/challenge/pwn` and `/challenge/college` will be passed into `/challenge/solve`.

The flag will hence be displayed 

### Flag

> oxky9OVm4iAweXK2dNUTmF7rli-.dhTM5QDL4czN0czW


![image](https://github.com/user-attachments/assets/b3d24007-8ce5-4424-b343-da200c93df31)
![image](https://github.com/user-attachments/assets/cafa9392-518a-4539-88a7-2ce8c1084bcc)
![image](https://github.com/user-attachments/assets/46421859-326e-442f-a3aa-18857137a094)

---

## Executable Shell Scripts

### Description of the Challenge
In this challenge, we need to create a shell script that executes `/challenge/solve` and make it executable. Instead of invoking the script with `bash script.sh`, we will directly execute it by setting the proper permissions.

### Info / Stuff We Should Know
- **File Permissions**: 
  - In Linux, a file can be made executable by modifying its permissions using the `chmod` command. This will allow the file to be run directly without specifying an interpreter like `bash`.
  
  - **Making a File Executable**:
    ```bash
    chmod +x filename.sh
    ```
    This command adds executable permissions to the file, allowing it to be run as a program.

- **Relative and Absolute Paths**:
  - A **relative path** refers to a file location relative to the current directory. For example, `./solve.sh` refers to the `solve.sh` script in the current directory.
  - An **absolute path** provides the complete path to a file, starting from the root directory, such as `/home/hacker/solve.sh`.

### Step-by-Step Solution

1. **Create the Shell Script**:
   - First, create a shell script named `solve.sh`:
     ```bash
     nano solve.sh
     ```
   - Add the following command to it:
     ```bash
     /challenge/solve
     ```

2. **Save and Exit**:
   - Save the file and exit the editor.

3. **Make the Script Executable**:
   - Use `chmod` to give the script execute permissions:
     ```bash
     chmod +x solve.sh
     ```

4. **Run the Script**:
   - Now, you can directly run the script without invoking `bash`:
     ```bash
     ./solve.sh
     ```

5. **Retrieve the Flag**:
   - After running the command, the flag will be displayed.

### Flag

> gma78JMeRwSYmOO1FwCwmwG6hum.dRzNyUDL4czN0czW

![image](https://github.com/user-attachments/assets/50f99905-f3dd-4c31-865d-1cbf47945b7f)
![image](https://github.com/user-attachments/assets/3b2af85c-563c-4e3f-81e8-399d4673fc50)

---
