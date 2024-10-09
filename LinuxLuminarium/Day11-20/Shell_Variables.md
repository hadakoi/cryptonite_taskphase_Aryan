# Shell Variables 

---

## Printing Variables

### Description
The goal of this challenge is to retrieve and print the value of a variable called `FLAG`  which holds the flag. The program `/challenge/run` won't provide the flag directly but since the flag is stored in the `FLAG` variable we can solve the challenge by printing the variables contents using basic shell commands.
The command `echo $FLAG` will print the contents of the `FLAG` variable which returns us the flag..

### Info / Stuff We should Know
In Linux  environment variables can be printed using the `echo` command. When you want to print a variable you prepend its name with a `$`. For example - 
- `echo Hello` prints "Hello" to the console.
- `echo $PWD` prints the current working directory stored in the `PWD` variable.

### Step-by-Step Solution

**Command to print Flag Variable**
```bash
echo $FLAG
```

### Flag
> 07R8UVOEhAaF6VXErnolYWrI9hG.ddTN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/b557d52f-63a0-4302-85c8-0903c68ebd57)

---

## Setting Variables

### Description
The goal of this challenge is to set the value of the `PWN` variable to `COLLEGE`.
We can use the `=` operator to assign values to variables.
This command is showcased as 'PWN=COLLEGE' which returns us the flag directly.

### Info / Stuff We should Know
In shell scripting variable assignment is done using the `=` operator with no spaces. To access a variable you prepend its name with a `$` symbol. For example:
- `VAR=1337` assigns the value `1337` to `VAR`
- `echo $VAR` prints the value of the `VAR` variable
Variables are case-sensitive meaning `PWN` is different from `pwn` and `COLLEGE` is different from `College`.

### Step-by-Step Solution

**Command to set PWN variable to COLLEGE**
```bash
PWN=COLLEGE
```
This ends up returning the flag.

### Flag
> QZ9BC0fZqnxrOQfB_4nWWx0NArC.dlTN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/759159d6-36b0-4af2-a9be-a85a05c8f37b)

---

## Multi Word Variables

### Description
The goal of this challenge is to set the `PWN` variable to the value `COLLEGE YEAH`. 
We can do this by 'PWN="COLLEGE YEAH"'

### Info / Stuff We should Know
To assign a multi-word value to a variable we must enclose the value in quotes. For eg : 

- `VAR="1337 SAUCE"` assigns `1337 SAUCE` to the variable `VAR`

In shell scripting spaces are significant and you need to use quotes to assign multi-word values to variables. Without quotes, the shell will interpret the space as the end of the assignment and treat the next word as a separate command.

### Step-by-Step Solution

**Command to set PWN variable to COLLEGE YEAH**
```bash
PWN="COLLEGE YEAH"
```
This returns the flag

### Flag
> wDDw5-MoIZxGdeQEkpNKQLFolpn.dBjN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/b4b892a4-d03a-4e91-b760-6e46222f7803)

---

## Exporting Variables

### Description
The goal of this challenge is to run `/challenge/run` with the `PWN` variable exported and set to `COLLEGE` while setting the `COLLEGE` variable to `PWN` without exporting it. To do this, we will use the following two commands:

- `export PWN=COLLEGE`
- `COLLEGE=PWN`

### Info / Stuff We should Know

- **Exported Variables**: When you export a variable it means that it can be used by other programs or commands that you start from your current shell. These programs are called *child processes*. For example if you run the command `export PWN=COLLEGE` you are telling the shell to make the `PWN` variable available to any program that you run afterward. So if you start a new program or shell it can see `PWN` and its value `COLLEGE`.

  **Example**:
  ```bash
  export PWN=COLLEGE
  sh
  echo "PWN is: $PWN"
  ```
In this example after exporting `PWN` we start a new shell with `sh`. Inside that new shell when we use `echo "PWN is: $PWN"`  it prints PWN is: COLLEGE` because `PWN` was exported.

- **Non-Exported Variables**: If a variable is not exported it only exists in the current shell and cannot be used by any programs started from it. This is useful when you want to keep some information private or only relevant to the current session. For example if you run `COLLEGE=PWN` this sets `COLLEGE` to `PWN` but since `COLLEGE` is not exported it cannot be accessed by any new programs or shells that you start.

  **Example**:
  ```bash
  COLLEGE=PWN
  sh
  echo "COLLEGE is: $COLLEGE"
  ```
In this example after setting `COLLEGE` we start a new shell with `sh`. Inside that new shell when we use `echo "COLLEGE is: $COLLEGE"` it will print `COLLEGE is:` without any value because `COLLEGE` was not exported and is not available in the new shell.

### Step-by-Step Solution

**Command to set and export PWN variable to COLLEGE**
```bash
export PWN=COLLEGE
```

**Command to set COLLEGE variable to PWN without exporting it**
```bash
COLLEGE=PWN
```

**Command to invoke the flag**
```bash
/challenge/run
```

### Flag
> k5GjUBqpkyMt_3__UiyAl7OSZpY.dJjN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/8fe7012e-582b-4933-9dd6-7ea19d6a0072)

---






