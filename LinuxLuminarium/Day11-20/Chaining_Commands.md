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


