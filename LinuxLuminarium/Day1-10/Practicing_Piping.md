# Practicing Piping
---

## Redirecting Output

### Description
In this challenge, we are tasked with redirecting the word **PWN** to a file named **COLLEGE**.  
To achieve this, we use the `echo` command, which outputs the specified text and redirects it to the desired file.

### Info / Stuff We Should Know
- The `>` operator is used to redirect the output from the `echo` command to a file.
- If the file does not exist, it will be created; if it does exist, its contents will be overwritten.

### Step-by-Step Solution

**Command to redirect the output:**
```bash
echo PWN > COLLEGE
```

### Flag
>  `ETwqJ7hiwnEZBinH-X9hRIvEq47.dRjN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/5a5358bb-7304-4902-aa8b-95df677e7f83)

---

## Redirecting more Output

### Description
In this challenge, we are required to redirect the output of the program **/challenge/run** to a file named **myflag** without using the `echo` command.  
This task involves running the command and redirecting its output to the specified file.
We can use the `cat` command to view the contents of the redirected file.


### Info / Stuff We Should Know
- The `>` operator is used to redirect the output from a command to a file.
- If the file does not exist, it will be created; if it does exist, its contents will be overwritten.

### Step-by-Step Solution

**Command to redirect the output:**
```bash
/challenge/run > myflag
```

**Command to view the contents of the redirected output:**
```bash
cat myflag
```

### Flag
>  `kokZcFxqoxHnvmgZdZ6YPs4c08r.dVjN1QDL4czN0czW`


![image](https://github.com/user-attachments/assets/6b0e248f-a4d0-4a20-8cdf-200fbcde9720)

---

## Appending Output

### Description
In this challenge, we are required to redirect the output of **/challenge/run** in append mode.  
This allows us to concatenate the first and second halves of the flag into the same file located at **/home/hacker/the-flag**.  

Appending output is similar to redirection but uses the `>>` operator, which adds content to the end of the specified file instead of overwriting it. We can then use the `cat` command to view the contents of the file after appending.

### Info / Stuff We Should Know
- The `>>` operator is used to append the output of a command to an existing file.
- If the file does not exist, it will be created; if it does exist, the new output will be added to the end of the file.

### Step-by-Step Solution

**Command to append the output:**
```bash
/challenge/run >> /home/hacker/the-flag
```

**Command to view the contents of the appended file:**
```bash
cat /home/hacker/the-flag
```

### Flag
>  `0guvNn-TJoIsQCcmW9tuCDoLr0G.ddDM5QDL4czN0czW`

![image](https://github.com/user-attachments/assets/dbc10666-0517-474f-80c4-94dbb0224dbb)

---
## Redirecting Errors

### Description
In this challenge, we need to redirect the output of **/challenge/run** in two ways: 
1. Redirect standard output (stdout), which contains the flag, to a file called **myflag**.
2. Redirect standard error (stderr), which contains any instructions or error messages, to a file called **instructions**.

### Info / Stuff We Should Know
- In Linux, file descriptors represent different channels for processes:
  - **FD 0:** Standard Input (stdin) - Input stream for user input.
  - **FD 1:** Standard Output (stdout) - Output stream for regular command output.
  - **FD 2:** Standard Error (stderr) - Output stream for error messages.
- Redirection can be specified using `1>` for stdout and `2>` for stderr.
- Both outputs can be redirected simultaneously using the format:
  ```bash
  command > output.log 2> errors.log
  ```

### Step-by-Step Solution

**Command to redirect stdout and stderr:**
```bash
/challenge/run 1> myflag 2> instructions
```
*Alternatively, you can use:*
```bash
/challenge/run > myflag 2> instructions
```

### Flag
>  `0GwdkQdwRw79WCFOIQEs1kN8l8I.ddjN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/3465b1aa-4aa6-4b36-ac03-4f4d20666c79)

---

## Redirecting Input

### Description
In this challenge, we are required to redirect the **PWN** file, which contains the value **COLLEGE**, as input to the **/challenge/run** command.

### Info / Stuff We Should Know
- To write the value **COLLEGE** into the **PWN** file, we use the `echo` command:
- When using a file as input, we reverse the redirection sign to `<`.

### Step-by-Step Solution

**To write the value **COLLEGE** into the **PWN** file, we use the `echo` command:**
  ```bash
  echo COLLEGE > PWN
  ```
**Command to redirect input:**
```bash
/challenge/run < PWN
```
This command redirects the contents of the **PWN** file (which contains **COLLEGE**) as input to **/challenge/run**.

### Flag
> `kTFr660CcvTdRZPRxXiSiuC45Gj.dBzN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/590c4272-c75e-44eb-b233-ee66acc1c0b7)

---

## Grepping stored results
```
In this challenge we are required to redirect the output of /challenge/run to /tmp/data.txt
Then we are required to search through this text file for the flag.

We can first redirect output by doing /challenge/run > /tmp/data.txt
Next we can do grep pwn.college /tmp/data.txt. this is because we know the flag begins with pwn.college.
Hence this returns the flag.


Flag -> AVTGh3SuaYy47qog6g4dBjzjJ6U.dhTM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/b5089535-9e7f-47a7-bb49-0334b810a386)


## Grepping live output
```
In this challenge we are to use the | operator to directly search the flag.
Basically using | after a command immediately executes the command thats written after it when the one before it is finished.
Hence our command will be /challenge/run | grep pwn.college. Hence this returns the flag.

Flag -> k0vF1_ixjw--uoSsMxtsBqAbL00.dlTM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/f7c7966e-e641-45eb-8f94-7f17cbbcc9e0)


## Grepping errors
```
In this challenge we need to To grep through the standard error output
which is redirect standard error (FD 2) to standard output (FD 1) using 2>&1

we can do this in one command again which is /challenge/run 2>&1 | grep pwn.college

Flag -> QvqT4fYY9M6tjS5f-Yej6L9PYd1.dVDM5QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/a6626100-c71c-41bc-a693-f24d209b121d)

## Duplicating piped data with tee
```
In this challenge we need to solve this challenge by intercepting data from the /challenge/pwn when passing it to /challenge/college
This is to see the data as it flows. We can accomplish this using the Tee command. It duplicates data flowing through my command line.

Hence we can use the command /challenge/pwn | tee intercepted_data | /challenge/college

We can then cat intercepted_data. this then shows us how to use the command with the following text
Usage: /challenge/pwn --secret [SECRET_ARG]

SECRET_ARG should be "47BeXUu0"

Hence we now do /challenge/pwn --secret "47BeXUu0"

This does not work as we can only view it through the intercepted_data hence we again pass it through tee or just pipelining

We now do /challenge/pwn --secret "47BeXUu0" | tee intercepted_data | /challenge/college
we can also do /challenge/pwn --secret "47BeXUu0" | /challenge/college as its stated we can use tee just for debugging this time.

Hence we get the flag

Flag -> 47BeXUu0VbkmSbYCyVteOtoUJgt.dFjM5QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/c741457a-c526-4a61-a0cb-84d70a402710)

## Writing to Multiple Programmes
```
In this challenge we can solve it using /challenge/hack, /challenge/the, and /challenge/planet, you’ll use tee along with process substitution. The goal is to take the output from /challenge/hack and pass it as input to both /challenge/the and /challenge/planet.

We can do this command /challenge/hack | tee >( /challenge/the ) >( /challenge/planet )
/challenge/hack: This command generates the output you want to duplicate.
|: The pipe operator sends the output of /challenge/hack to tee.
tee: This command will take the output from /challenge/hack and duplicate it.
>( /challenge/the ): This process substitution allows the output of tee to be passed as input to /challenge/the.
>( /challenge/planet ): Similarly, this allows the output to also be passed as input to /challenge/planet.

Flag -> kvgvRbZi1zsXve5bu_rkYuajnvD.dBDO0UDL4czN0czW
```
![image](https://github.com/user-attachments/assets/1b54d597-7f4a-4497-ac9d-252c558e16ec)

---

## Split Piping stderr and stdout

### Description
In this challenge, we are supposed to redirect the output from `/challenge/hack` such that standard output (stdout) goes to `/challenge/planet` and standard error (stderr) goes to `/challenge/the`, while keeping them separate.

We can do this with the following command:
```bash
/challenge/hack > >( /challenge/planet ) 2> >( /challenge/the )
```

### Info / Stuff We Should Know (Basically solving pattern this time)

- `/challenge/hack`: This command runs and produces output on both stdout and stderr.
- `>`: This operator is used to redirect stdout.
- `>( /challenge/planet )`: This is a process substitution. It creates a temporary named pipe and connects it to the stdin of `/challenge/planet`. The stdout of `/challenge/hack` will be sent through this pipe to `/challenge/planet`.
- `2>`: This operator is used to redirect stderr.
- `>( /challenge/the )`: Similar to the previous substitution, this creates another temporary named pipe that connects stderr from `/challenge/hack` to the stdin of `/challenge/the`.

### Step-by-Step Solution

**Command to run for redirecting stdout and stderr.**
```bash
/challenge/hack > >( /challenge/planet ) 2> >( /challenge/the )
```

When you execute `/challenge/hack`, it generates both stdout and stderr. 
- The `>` operator redirects stdout to `/challenge/planet` through the named pipe created by `>( /challenge/planet )`.
- The `2>` operator redirects stderr to `/challenge/the` through the named pipe created by `>( /challenge/the )`.

### Flag
> IMyuQBRZyN0n1lc3rZnADDlvrla.dFDNwYDL4czN0czW

![image](https://github.com/user-attachments/assets/80885e0d-c2ed-4cf3-a6f5-a0f1c02af6f3)

---




