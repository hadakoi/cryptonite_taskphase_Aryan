# Pondering Paths

---
## The Root

### Description
In this challenge we are tasked with invoking a program located in the root directory. 
This is done by executing **/pwn** where the `/` signifies that it is in the root directory and **pwn** is the executable program. 
By running this command we execute the pwn program, which returns the flag.

### Info / Stuff We Should Know
The command requires specifying the absolute path to the executable located in the root directory.

### Step-by-Step Solution

**Command to run for invoking the pwn program.**
```bash
/pwn
```

### Flag
>  `AhtgI2aIJwYv7p_Ye1_1EmmQz6c.dhzN5QDL4czN0czw`

![image](https://github.com/user-attachments/assets/4d5fcc1d-d6de-4297-9b23-4e881782d899)

---

## Program and absolute paths

### Description
In this challenge we will be accessing a directory called challenge which is located in the root directory (/). 
Inside this challenge directory there is an executable program named run. When invoked this program will automatically return the flag.

### Info / Stuff We Should Know
To execute the program we need to use its absolute path **/challenge/run**. It runs the executable file present in the challenge directory and hence returns the flag.

### Step-by-Step Solution

**Command to run for invoking the run program.**
```bash
/challenge/run
```

### Flag
> `wjv0fqhMGmPgZNJpA1vBE8UoeYq.dVDN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/efee2f36-d5c4-4421-a9ae-45b4dcb4058e)

---

## Position thy self

### Description
In this challenge we need to access the **/challenge/run** program. 
Initially we will be prompted to change to a specific directory before rerunning the **/challenge/run** program.

### Info / Stuff We Should Know
We must navigate to a different directory called **/usr/share/doc/fontconfig**. 
To do that we must use the command **cd /usr/share/doc/fontconfig** which allows us to enter the specific directory.
Once we have entered this directory we may finally run the program contained in challenge using **/challenge/run**.

### Step-by-Step Solution

**Command to change to the specific directory.**
```bash
cd /usr/share/doc/fontconfig
```

**Command to run the run program.**
```bash
/challenge/run
```

### Flag
>  `4CHtiNCVcDoa6Fzx88MSZegt8cN.dZDN1QDL4czN0czW`


![image](https://github.com/user-attachments/assets/c9083793-d2ae-457d-93c7-e645d6f1de16)

---

## Position Elsewhere

### Description
In this challenge we need to access the **/challenge/run** program.
Initially when we execute the command **/challenge/run** we encounter a prompt instructing us to change to a specific directory in this case **/usr/bin**.

### Info / Stuff We Should Know
To do that we use the command **cd /usr/bin** putting us in the bin directory. Afterwards we run the program using **/challenge/run**. Hence the key is returned to us.

### Step-by-Step Solution

**Command to change to the specific directory.**
```bash
cd /usr/bin
```

**Command to run the run program.**
```bash
/challenge/run
```

### Flag
>  `gvuIVp5frExfcmXOLIM064DL6la.ddDN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/35b1d138-5bd8-4da0-aacc-561a5bc3796b)

---

## Position yet Elsewhere

### Description
In this challenge we need to access the **/challenge/run** program. Initially when we execute the command **/challenge/run** we encounter a prompt instructing us to change to a specific directory. In this case, **/var**.

### Info / Stuff We Should Know
To do that we use the command **cd /var** which puts us in the **var** directory. Afterwards we run the command to execute the program **/challenge/run**. Hence the key is returned to us.

### Step-by-Step Solution

**Command to change to the /var directory.**
```bash
cd /var
```

**Command to run the run program.**
```bash
/challenge/run
```

### Flag
>  `IB-f4M_2InLhgHsdjqb0fAwM9db.dhDN1QDL4czN0czWj`

![image](https://github.com/user-attachments/assets/32332af0-11fa-4974-bd4d-c1251a35d95d)

---

## implicit relative paths, from /

### Description
In this challenge we need to access the **/challenge/run** program. Initially when we execute the command **/challenge/run** we encounter a prompt instructing us that we are not currently in the **/** directory. Please use the **cd** utility to change directory appropriately.

### Info / Stuff We Should Know
Hence we change to the **/** directory by **cd /**. This changes our current working directory to the root directory.

### Step-by-Step Solution
Running the program again using **/challenge/run** gives us an error message indicating that we invoked this challenge with an absolute path. This challenge needs a relative path. As an absolute path always begins with **/** and is referenced from the start of the root directory we need to use a relative path from the current directory we have switched to which is **challenge/run**.

**Command to change to the root directory.**
```bash
cd /
```

**Command to run the run program using a relative path.**
```bash
challenge/run
```

### Flag
>  `YVki8xoWpHfQOV7KгZI0P0mLN85.dlDN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/16476613-0866-4c83-aaae-995f8092c2e7)

---

## explicit relative paths, from /

### Description
In this challenge we need to access the **/challenge/run** program. Initially when we execute the command **/challenge/run** we encounter a prompt instructing us that we are not currently in the **/** directory. Please use the **cd** utility to change directory appropriately.

### Info / Stuff We Should Know
Hence we change to the **/** directory by **cd /**. This changes our current working directory to the root directory.

Running the program again using **/challenge/run** gives us an error message indicating that we invoked this challenge with an absolute path. This challenge needs a relative path. As an absolute path always begins with **/** as it is referenced from the start of the root directory we need to use a relative path from the current directory we have switched to which is **challenge/run**.

However we receive another error message indicating that this challenge must be called with a relative path that explicitly starts with a **.**.

### Step-by-Step Solution
To solve it we use the command **./challenge/run**. This tells the system to look for **challenge** in your current directory. This and the previous command ideally do the same thing but they reference the file differently.

**Command to change to the root directory.**
```bash
cd /
```

**Command to run the run program using a relative path.**
```bash
./challenge/run
```

### Flag
>  `8QuhNryEq9ycQKrjhL_QheiuC4u.dBTN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/bdae5bb8-0e4e-4982-b7dd-8eb7784f06c8)
![image](https://github.com/user-attachments/assets/ad778fae-6fbb-4d28-b2b4-1e2de2c2ab52)

---

## implicit relative path

### Description
In this challenge we are asked to execute the **run** program from the challenge directory. We enter the challenge directory by doing **cd /challenge**. We then run the program using **./run**. By using **./** we make it clear that the shell should look for **run** in **/challenge**.

### Info / Stuff We Should Know
Using **./** specifies that we want to execute a program in the current directory

### Step-by-Step Solution

**Command to change to the challenge directory.**
```bash
cd /challenge
```

**Command to run the run program.**
```bash
./run
```

### Flag
>  `kzLeDdJZQCIaHA59NnVwkfIVx4f.dFTN1QDL4czN0czW`

![image](https://github.com/user-attachments/assets/42a88925-5e7a-4911-8542-5c97e85d7aab)

---

## home sweet home

### Description
In this challenge we are asked to execute the **run** program present in the challenge directory. 
However this time it will return it to a file of our choice that we set as the argument.
As such when using an argument we can only make it 3 characters long. 
By considering **~** as our **/home/hacker** we can use the argument **~/x** which means the file or directory **x** inside your home directory. 
It is equivalent to **/home/hacker/x**.

### Info / Stuff We Should Know
Thus we use the command **/challenge/run ~/x** meaning **/challenge/run** to write the output (in this case the flag) to the file **x** located in your home directory **/home/hacker/x**. This automatically returns the flag.

In simple words
Command: **/challenge/run** (This is the main action: "Run the challenge!")
Argument: **~/x** (This tells the computer where to put the result in a file called **x** in your home folder). It gets expanded to **/home/hacker/x**. So the argument is essentially telling the command where to store the result.

### Step-by-Step Solution

**Command to run the run program with the argument.**
```bash
/challenge/run ~/x
```

### Flag
> `EM4F1PXVV5X2MHsBf5VpnCPNbs8.dNzM4QDL4czNcZW`

![image](https://github.com/user-attachments/assets/f1e8c511-6000-4d9a-b65a-7982d1fc0700)

---







