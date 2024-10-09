# File Globbing

---

## Matching with *

### Description
This challenge requires us to change directories using globbing. Globbing expands identifiers like `*`, `?`, and `[]` into filenames and paths.  
In this challenge, we specifically use the `*` wildcard. The goal is to enter the challenge directory using globbing, where the argument passed should be at most 4 characters.  
This is achieved using **/ch***, which matches directories with 4 characters. Once inside the directory, we run **/challenge/run** to retrieve the flag.

### Info / Stuff We Should Know
- **Globbing** allows the shell to match files or directories using wildcards such as `*`, `?`, and `[]`.
- The wildcard `*` matches any characters after the prefix (in this case, **/ch***).

### Step-by-Step Solution

**Command to enter the directory using globbing:**
```bash
cd /ch*
```

**Command to run the challenge program:**
```bash
/challenge/run
```

### Flag
>  `8yjHPjQZzzISI56ncw6TIbLfULa.dFjM4QDL4czN0czW`


![image](https://github.com/user-attachments/assets/77d7dcc6-613f-4e84-845b-1b4c025197c6)

---

## Matching with ?

### Description
This challenge requires us to change directories using globbing, specifically with the `?` wildcard.  
Unlike the `*`, which matches any number of characters, the `?` matches exactly **one** character.  
In this challenge, we are supposed to replace certain characters in the directory name with `?` when navigating. Specifically, we reference `c` and `l` as `?` in the directory name.We can change directories using **cd /?ha??enge**, which matches the correct directory.
After entering the directory, running **/challenge/run** returns the flag

### Info / Stuff We Should Know
- The `?` wildcard in globbing matches exactly **one** character.
- In this case, we use `?` to match the characters `c` and `l` in the directory name.

### Step-by-Step Solution

**Command to change to the directory using the `?` wildcard:**
```bash
cd /?ha??enge
```

**Command to run the challenge program:**
```bash
/challenge/run
```

### Flag
>  `I2BaVpC3QzO41eGcyGUvCFM1Ljm.dJjM4QDL4czN0czW`\

![image](https://github.com/user-attachments/assets/8f74dae7-0ae3-4b23-ae16-c0999f6b961f)

---

## Matching with []

### Description
This challenge requires us to change directories using globbing, specifically using the `[]` wildcard.  
The `[]` in globbing matches exactly **one** character from a specific set of characters listed inside the brackets.  
In this challenge, we are tasked with accessing files identified as **file_b**, **file_a**, **file_s**, and **file_h**. We need to pass all these as arguments using the `[]` wildcard when running the command **/challenge/run**.
We first switch to the **/challenge/files** directory.
We then use the **/challenge/run file_[bash]** command, where `bash` represents the identifiers (`b`, `a`, `s`, `h`) for the respective files.

### Info / Stuff We Should Know
- The `[]` wildcard matches exactly **one** character from the set provided inside the brackets.
- The challenge hints that the files we are working with have identifiers **file_b**, **file_a**, **file_s**, and **file_h**.


### Step-by-Step Solution

**Command to change to the directory:**
```bash
cd /challenge/files
```

**Command to run the challenge program with file identifiers:**
```bash
/challenge/run file_[bash]
```

### Flag
>  `IdQQ-w7BWQ2cgaMnxL7OK38i4b4.dNjM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/df50c325-49be-440f-8597-b8b5c2cb8852)

---

## Matching paths with []

### Description
In this challenge, we are required to use bracket globs to search specific files and run the program with their absolute paths as arguments.  
The files we need to access are **file_b**, **file_a**, **file_s**, and **file_h**, located in the **/challenge/files** directory.  
We need to run **/challenge/run** with a single argument that includes these file names using the `[]` syntax.

### Info / Stuff We Should Know
- We are using the **[]** wildcard to match exactly one character from the set of characters `b`, `a`, `s`, and `h`.

### Step-by-Step Solution

**Command to run the challenge program with the file paths:**
```bash
/challenge/run /challenge/files/file_[bash]
```

### Flag
>  `ISHPrPswN5qCSFP7f08GLIFlp-x.dRjM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/d54c3470-c202-4580-bc48-d98520591d39)

---

## Mixing Globs

### Description
In this challenge, we need to create a glob that matches three file names: **challenging**, **educational**, and **pwning**. The glob must be 6 characters or less.  
We start by listing the files in the directory and then passing a glob argument to match all three files using a combination of the starting letters and the `*` wildcard.
This works as each file's name in the directory begins with a unique character.

### Info / Stuff We Should Know
- We need to match the file names **challenging**, **educational**, and **pwning**, which start with different letters.
- The **[CEP]** syntax is used to match files that start with **C**, **E**, or **P**.
- The `*` wildcard is used to match the rest of the characters in the file names.

### Step-by-Step Solution

**Command to change to the directory:**
```bash
cd /challenge/files
```

**Command to list all files in the directory:**
```bash
ls
```

**Command to run the challenge program with the glob pattern:**
```bash
/challenge/run [CEP]*
```

### Flag
>  `gVuDI-werY1rB1ugguyHnzcxfgI.dVjM4QDL4czN0czW`


![image](https://github.com/user-attachments/assets/ec44feb4-1b1a-4170-ab35-586f41079ed3)

---

## Exclusionary Globbing

### Description
In this challenge, we are required to use exclusionary globbing to filter out specific files.  
We need to exclude files that begin with the letters **p**, **w**, or **n**. This can be done by using the negation syntax **[!pwn]**, which matches files that do not start with these letters.

### Info / Stuff We Should Know
- The **[!...]** syntax in globbing negates a set of characters, meaning it matches files that do **not** start with any of the characters inside the brackets.
- We are excluding files that start with **p**, **w**, or **n** by using **[!pwn]**.
- After excluding, the `*` will match the rest of the files in the directory.

### Step-by-Step Solution

**Command to change to the directory:**
```bash
cd /challenge/files
```

**Command to run the challenge program with exclusionary globbing:**
```bash
/challenge/run [!pwn]*
```

### Flag
>  `8dapwwVqtNyvinBYf1BREKNjzNy.dZjM4QDL4czN0czW`

![image](https://github.com/user-attachments/assets/37985bf0-75fd-47f5-93d6-212e2c7ab303)

---






