# Practicing Piping

## Redirecting Output
```
In this challenge we are asked to redirect word PWN to the filename COLLEGE.

To do this we  echo PWN > COLLEGE
PWN is passed to COLLEGE

This returns the flag.

Flag -> ETwqJ7hiwnEZBinH-X9hRIvEq47.dRjN1QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/5a5358bb-7304-4902-aa8b-95df677e7f83)

## Redirecting more Output
```
In this challenge we are asked to redirect output without the use of echo.
for this challenge we need to redirect the output from /challenge/run to a file called myflag

we can do this by doing /challenge/run > myflag
after having done this we are told that the redirection was successful hence
we can now do cat myflag to see the output. This returns the flag.

Flag -> kokZcFxqoxHnvmgZdZ6YPs4c08r.dVjN1QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/6b0e248f-a4d0-4a20-8cdf-200fbcde9720)

## Appending Output
```
In this challenge you need to redirect the output of /challenge/run in append mode.
THis so that the first and second halves of the flag are properly concatenated into the same file /home/hacker/the-flag
Append mode is different from passing the outputs but similar using >>

Over here we need to redirect the output of /challenge/run to the file /home/hacker/the-flag
This is done by /challenge/run >> /home/hacker/the-flag.
What basically happens is the first half of the flag directly written into the recieving file.
Whereas the second half is appended at the end of the recieving file.

As such after using the append command we can then cat /home/hacker/the-flag where we recieve the flag and an explanation.

Flag -> 0guvNn-TJoIsQCcmW9tuCDoLr0G.ddDM5QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/dbc10666-0517-474f-80c4-94dbb0224dbb)

## Redirecting Errors
```
Note -> In linux files there are file descriptions that are numbers that represent different channels for processes.
1. FD 0: Standard Input (stdin) - Input stream for taking user input.
2. FD 1: Standard Output (stdout) - Output stream for regular command output.
3. FD 2: Standard Error (stderr) - Output stream for error messages.
We can use these in our redirection as its already redirecting one of these types of files.
we can specify it by doing 1> or 2>.
We can also redirect both at the same time. command > output.log 2> errors.log

In this challenge we need to redirect the output of /challenge/run in two ways:
Redirect stdout (the flag) to a file called myflag.
Redirect stderr (the instructions) to a file called instructions

stdout stands for standard output or 1> and stderr is for 2>
We can do this mainly by
/challenge/run 1> myflag 2> instructions which can also be /challenge/run > myflag 2> instructions.
What happens here is the flag is put in myflag which is our basic output for the command.
While the other part >2 instructions passes feedback or any error message to the instructions file.

Flag -> 0GwdkQdwRw79WCFOIQEs1kN8l8I.ddjN1QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/3465b1aa-4aa6-4b36-ac03-4f4d20666c79)

## Redirecting input
```
In this challenge we are required to redirect the PWN file with the value of COLLEGE to the /challenge/run command.

We can enter COLLEGE into pwn using the echo command this is done by echo COLLEGE > PWN
When using a file is input we reverse the sign for redirecting which is <.
Hence our command becomes /challenge/run < PWN
This will Redirect the contents of the PWN file (which contains COLLEGE) as input to /challenge/run.

Flag -> kTFr660CcvTdRZPRxXiSiuC45Gj.dBzN1QDL4czN0czW
```
![image](https://github.com/user-attachments/assets/590c4272-c75e-44eb-b233-ee66acc1c0b7)


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

## Split Piping stderr and stdout
```
In this challenge we are supposed to redirect the output from /challenge/hack such that standard output (stdout) goes to /challenge/planet and standard error (stderr) goes to /challenge/the, while keeping them separate

We can do this with the command /challenge/hack > >( /challenge/planet ) 2> >( /challenge/the )
/challenge/hack: This command will run and produce output on both stdout and stderr.

>: This operator is used to redirect stdout.

>( /challenge/planet ): This is a process substitution. It creates a temporary named pipe and connects it to the stdin of /challenge/planet. The stdout of /challenge/hack will be sent through this pipe to /challenge/planet.

2>: This operator is used to redirect stderr.

>( /challenge/the ): Similar to the previous substitution, this creates another temporary named pipe that connects stderr from /challenge/hack to the stdin of /challenge/the.

When you execute /challenge/hack, it will generate both stdout and stderr.
The > operator redirects the stdout to /challenge/planet through the named pipe created by >( /challenge/planet ).
The 2> operator redirects stderr to /challenge/the through the named pipe created by >( /challenge/the ).

Flag -> IMyuQBRZyN0n1lc3rZnADDlvrla.dFDNwYDL4czN0czW
```
![image](https://github.com/user-attachments/assets/80885e0d-c2ed-4cf3-a6f5-a0f1c02af6f3)



