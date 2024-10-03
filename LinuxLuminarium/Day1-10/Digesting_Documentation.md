# Digesting Documentation

## Learning from Documentation
```
In this challenge we are required to pass the command /challenge/challenge with the argument --giveflag.
As a command this is /challenge/challenge --giveflag

Flag -> YMeDVM_1zGQ2C7-uO4a_kgH3NOB.dRjM5QDL4czN0czW

NOTE - Using - and -- are both arguments however - is followed by a letter hence
       condesned form or -- is followed by command name which is expanded for eg ls -a)
```
![image](https://github.com/user-attachments/assets/a8b7034d-ff09-46db-9447-fd6a353b7f18)

## Learning Complex Usage
```
In this challenge we are required to pass the argument --printfile with the path to the flag after it as shown in the example.
We can do this by /challenge/challenge --printfile /flag where /flag is our path to the flag.

Flag -> cepaK_5fTUgPpp0OrkFJ6DcNI9Z.dVjM5QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/452bb5cd-f278-4eca-9f27-567dac7e749b)

## Reading Manuals
```
In this challenge we are required to use the man command which displays the manual pages for other commands and concept.
Over here we are supposed to use the man command for the programme challenge.
Hence we do man challenge.
This presents us with the manual for the command /challenge/challenge
In the arguments section we see 3 options with the argument --gyjzaq NUM being the best as it returns the flag if we set NUM as 661

Hence when using the command it is /challenge/challenge --gyjzaq 661. This returns the flag.

Flag -> AgyjzME6TW6Ha1FPqxzwVtXOSfU.dRTM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/818a98a4-7eb2-48d7-8184-96f4ca489f23)

## Searching Manuals
```
In this challenge we are supposed to search through the manual to find the correct argument to return the flag.
We do man challenge to first open the manual

once opened we do /nameofitem. nameofitem is what we want to search for in this case flag.
so we do /flag hence allowing us to search for all instances of flag.
we move across these instances by pressing n.
We find that it is called --zzeg

Hence we run the command /challenge/challenge --zzeg this returns the flag.

Flag -> 4fMEyCn363egjI438iwi7PycnAq.dVTM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/f3dd5699-3ea5-40d7-8d7c-fda9ff0d2cd5)
![image](https://github.com/user-attachments/assets/ccf30060-5e24-4714-ad9a-8a3e769dbba8)
![image](https://github.com/user-attachments/assets/dfbc35b0-0fce-4c87-b339-6d3a350737e0)
![image](https://github.com/user-attachments/assets/9108d48c-d57c-4243-8e38-d9343fe1e330)

## Searching for Manuals
```
In this challenge we have to find the command argument for /challenge/challenge by. Sadly we do not know how to find the man challenge.
However there is no manual entry for challenge. so we first have to open up man man.
Upon opening it we can see the man -k command which is used for searching for man page names and descriptions for that specific word.
Hence doing man -k challenge.
We are given a name for a command called gofuewroff. Now we need to find what this command does so doing
man gofuewroff we find what the command does which is --gofuew NUM where it prints the flag if NUM is 824

Now our command is /challenge/challenge --gofuew 824

Flag -> EEgVWGoFfBu8ewrEoXffA2fCOvN.dZTM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/06b9c5a3-a143-4bbc-9303-6bfe0ac68a4b)
![image](https://github.com/user-attachments/assets/f7e105a6-4b8d-4244-a28a-ee73839bb855)

## Helpful Programmes
```
In this challenge we are given to assume /challenge/challenge does not have a man page.
So to find commands for this we can use commandname --help.
doing /challenge/challenge we see 4 commands but 2 mainly stand out.

-g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG
                        get the flag, if given the correct value
-p, --print-value
                       print the value that will cause the -g option to give you the flag

as such first we should find the value using /challenge/challenge --print-value or -p
this returns the value of 554

Now using the -g command we can do
/challenge/challenge -g 554

Flag -> YwY5pcQYniOGvRDQ5KPt-bsB_df.ddjM4QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/979914b9-fbb9-4af7-b043-110585d99c6b)

## Help for Builtins
```
In this challenge we are supposed to use the help command to identify and learn how to use the challenge command.
we do this by typing help challenge.

It first gives us how to use the command
challenge [--fortune] [--version] [--secret SECRET]
    This builtin command will read you the flag, given the right arguments!

next it gives 3 options for arguments however only 1 is valid for finding the flag
--secret VALUE	prints the flag, if VALUE is correct
    You must be sure to provide the right value to --secret. That value
    is "YP7mlzAu".

As such our command is now challenge --secret "YP7mlzAu"
THis returns the flag

Flag -> YP7mlzAuPLqRRIHnRZZcfA0hu9S.dRTM5QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/2ec22dbc-c8b1-4859-ac52-a198eef2adbb)









