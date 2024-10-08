# Digesting Documentation

---

## **Learning from Documentation**

### Description
In this challenge, we are required to pass the command `/challenge/challenge` with the argument `--giveflag`.

### Info / Stuff We Should Know
- The full command is `/challenge/challenge --giveflag`.
- Both `-` and `--` are used for arguments; however, `-` is followed by a letter (condensed form)
  while `--` is followed by the command name (expanded form).

### Step-by-Step Solution

**First basic command**
```bash
/challenge/challenge --giveflag
```
### Flag
> YMeDVM_1zGQ2C7-uO4a_kgH3NOB.dRjM5QDL4czN0czW 

![image](https://github.com/user-attachments/assets/a8b7034d-ff09-46db-9447-fd6a353b7f18)
---

## **Learning Complex Usage**

### Description
In this challenge, we are required to pass the argument `--printfile` 
with the path to the flag after it.

### Info / Stuff We Should Know
- The command structure is `/challenge/challenge --printfile <path_to_flag>`.
- In this case, we use `/flag` as the path to the flag.

### Step-by-Step Solution

**basic command**
```bash
/challenge/challenge --printfile /flag
```

### Flag
> 09S57AQLuUvJDJ0uxzJxleeW9Nz.dlTM5QDL4czNOCZW

![image](https://github.com/user-attachments/assets/452bb5cd-f278-4eca-9f27-567dac7e749b)

---
## Reading Manuals

### Description
In this challeng we are required to use the `man` command which displays the manual pages for other commands and concepts. Here we are supposed to use the `man` command for the program `challenge`. Hence
 we execute `man challenge`. This presents us with the manual for the command `/challenge/challenge`. In the arguments section we see 3 options with the argument `--gyjzaq NUM` being the best as it returns the flag if we set `NUM` as `661`.

### Info / Stuff We Should Know
- The `man` command shows the manual or documentation for a given command.
- To use the correct argument for the command you need to carefully read the manual's argument section.

### Step-by-Step Solution

**Read the manual and run the command**
```bash
man challenge

/challenge/challenge --gyjzaq 661
```

### Flag
> AgyjzME6TW6Ha1FPqxzwVtXOSfU.dRTM4QDL4czN0czW

![image](https://github.com/user-attachments/assets/818a98a4-7eb2-48d7-8184-96f4ca489f23)

---

## **Searching Manuals**

### Description
In this challenge, we are supposed to search through the manual to find the correct argument to return the flag. We do `man challenge` to first open the manual.
Once opened, we do `/nameofitem`. `nameofitem` is what we want to search for, in this case, "flag". So we do `/flag`, which allows us to search for all instances of "flag". We move across these instances by pressing `n`. We find that the argument is called `--zzeg`.

### Info / Stuff We Should Know
- Nothing to note.

### Step-by-Step Solution

**Command to run**
```bash
/challenge/challenge --zzeg
```

### Flag
> 4fMEyCn363egjI438iwi7PycnAq.dVTM4QDL4czN0czW

![image](https://github.com/user-attachments/assets/f3dd5699-3ea5-40d7-8d7c-fda9ff0d2cd5)
![image](https://github.com/user-attachments/assets/ccf30060-5e24-4714-ad9a-8a3e769dbba8)
![image](https://github.com/user-attachments/assets/dfbc35b0-0fce-4c87-b339-6d3a350737e0)
![image](https://github.com/user-attachments/assets/9108d48c-d57c-4243-8e38-d9343fe1e330)

---

## **Searching for Manuals**

### Description
In this challenge, we need to find the command argument for `/challenge/challenge`. Unfortunately, we cannot find a manual entry for "challenge," so we start by opening `man man`. We then see a description for a command that searches for man page names and descriptions related to a word 'man -k challenge'. This returns a command called gofuewroff.
To learn more about this command man gofuewroff we can do man for it. Here, we find that the command has the argument '--gofuew NUM', which prints the flag if NUM is 824.

### Info / Stuff We Should Know
- In the `man man` page, we discover the `man -k` command, which searches for man page names and descriptions related to a specific word.

### Step-by-Step Solution

**Finding the correct command.**
```bash
 man -k challenge
```
**Retrieve the flag**
```bash
/challenge/challenge --gofuew 824
```

### Flag
> EEgVWGoFfBu8ewrEoXffA2fCOvN.dZTM4QDL4czN0czW

![image](https://github.com/user-attachments/assets/06b9c5a3-a143-4bbc-9303-6bfe0ac68a4b)
![image](https://github.com/user-attachments/assets/f7e105a6-4b8d-4244-a28a-ee73839bb855)

---

## **Helpful Programmes**

### Description
In this challenge, we are tasked with assuming that `/challenge/challenge` does not have a man page. To find the available commands, we can use the `--help` option.
When doing this 2 commands stand out two stand out: *-g GIVE_THE_FLAG*, *--give-the-flag GIVE_THE_FLAG* get the flag, if given the correct value -p, --print-value print the value that will cause the -g option to give you the flag

### Info / Stuff We Should Know
- Running the command `/challenge/challenge --help` reveals several commands abd functions about the command /challenge/challenge.

### Step-by-Step Solution

**Returns the value.**
```bash
 /challenge/challenge --print-value 
```
**Retrieve the flag**
```bash
/challenge/challenge -g 554
```

### Flag
> YwY5pcQYniOGvRDQ5KPt-bsB_df.ddjM4QDL4czN0czW

![image](https://github.com/user-attachments/assets/979914b9-fbb9-4af7-b043-110585d99c6b)

---

## **Help for Builtins**

### Description
In this challenge, we are supposed to use the help command to identify and learn how to use the challenge command. We do this by typing `help challenge`.
The command structure provided is:

'challenge [--fortune] [--version] [--secret SECRET]'
Only the '--secret' option is valid for retrieving the flag, and the correct secret value to pass is "YP7mlzAu".

### Info / Stuff We Should Know
- The help command gives us information about the usage of the command

### Step-by-Step Solution

**Command to run**
```bash
challenge --secret "YP7mlzAu"
```

### Flag
> YP7mlzAuPLqRRIHnRZZcfA0hu9S.dRTM5QDL4czN0czW

![image](https://github.com/user-attachments/assets/2ec22dbc-c8b1-4859-ac52-a198eef2adbb)

---








