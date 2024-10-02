# Pondering Paths

## The Root

```

In this challenge we are tasked with invoking a program located in the root directory.
This is done by executing */pwn* where the / signifies that it is in the root directory and pwn is the executable program.
By running this commands we execute the pwn program which returns the flag.

Flag -> AhtgI2aIJwYv7p_Ye1_1EmmQz6c.dhzN5QDL4czN0czw

```
![image](https://github.com/user-attachments/assets/4d5fcc1d-d6de-4297-9b23-4e881782d899)

## Program and absolute paths

```

In this challenge we will be accessing a directory called challenge which is located in the root directory (/).
Inside this challenge directory there is an executable program named run.
When invoked this program will automatically return the flag.

To execute the program we need to use its absolute path: /challenge/run.
It runs the executable file present in the challenge directory and hence returns the flag.

Flag -> wjv0fqhMGmPgZNJpA1vBE8UoeYq.dVDN1QDL4czN0czW

```

![image](https://github.com/user-attachments/assets/efee2f36-d5c4-4421-a9ae-45b4dcb4058e)


## Position thy self

```

In this challenge we need to access the /challenge/run program.
Initially we will be prompted to change to a specific directory before rerunning the /challenge/run program.

Hence like before we use the /challenge/run command only to see it prompt us an error message and asking us to navigate to
a different directory called /usr/share/doc/fontconfig

to do that we must use this specific command *cd /usr/share/doc/fontconfig* which allows us to enter the specific directory which is fontconfig
once we have entred this specific directory we may finally run the programme contained in challenge using /challenge/run

Flag -> 4CHtiNCVcDoa6Fzx88MSZegt8cN.dZDN1QDL4czN0czW

```

![image](https://github.com/user-attachments/assets/c9083793-d2ae-457d-93c7-e645d6f1de16)


## Position Elsewhere

```
In this challenge we need to access the /challenge/run program. Initially when we execute the command /challenge/run
We encounter a prompt instructing us to change to a specific directory in this case /usr/bin

to do that we use this command *cd /usr/bin* putting us in the bin directory afterwards we put the command to run the programme /challenge/run
Hence the key is returned to us.

Flag -> gvuIVp5frExfcmXOLIM064DL6la.ddDN1QDL4czN0czW

```

![image](https://github.com/user-attachments/assets/35b1d138-5bd8-4da0-aacc-561a5bc3796b)

## Position yet Elsewhere

```
In this challenge we need to access the /challenge/run program. Initially when we execute the command /challenge/run
We encounter a prompt instructing us to change to a specific directory in this case /var

to do that we use this command *cd /var* putting us in the bin directory afterwards we put the command to run the programme /challenge/run
Hence the key is returned to us.

Flag -> IB-f4M_2InLhgHsdjqb0fAwM9db.dhDN1QDL4czN0czWj

```
![image](https://github.com/user-attachments/assets/32332af0-11fa-4974-bd4d-c1251a35d95d)

## implicit relative paths, from /

```
In this challenge we need to access the /challenge/run program. Initially when we execute the command /challenge/run
We encounter a prompt instructing
Incorrect...
You are not currently in the / directory.
Please use the `cd` utility to change directory appropriately.

Hence we change to the / directory by *cd /*

This changes our current working directory to the root directory.

Running the Program Again /challenge/run
I was given an error message of
Incorrect...
You invoked this challenge with an absolute path. This challenge needs a relative path!

As an absolute path always begins with / as its referenced from the start of the root directory we need
to use a relative path from the current directory we have switched to which is *challenge/run*
hence we get our flag.

Flag -> YVki8xoWpHfQOV7KгZI0P0mLN85.dlDN1QDL4czN0czW

```
![image](https://github.com/user-attachments/assets/16476613-0866-4c83-aaae-995f8092c2e7)

## explicit relative paths, from /

```
In this challenge we need to access the /challenge/run program. Initially when we execute the command /challenge/run
We encounter a prompt instructing
Incorrect...
You are not currently in the / directory.
Please use the `cd` utility to change directory appropriately.

Hence we change to the / directory by *cd /*

This changes our current working directory to the root directory.

Running the Program Again /challenge/run
I was given an error message of
Incorrect...
You invoked this challenge with an absolute path. This challenge needs a relative path!

As an absolute path always begins with / as its referenced from the start of the root directory we need
to use a relative path from the current directory we have switched to which is *challenge/run*
However we are given the error message of
Incorrect...
This challenge must be called with a relative path that explicitly starts with a `.`!

As such to solve it we use the command *./challenge/run*
./challenge/run tells the system to look for challenge in your current directory.
this and the previous command ideally do the same thing but they reference the file differently.
this returns the flag.

Flag -> 8QuhNryEq9ycQKrjhL_QheiuC4u.dBTN1QDL4czN0czW

```

![image](https://github.com/user-attachments/assets/bdae5bb8-0e4e-4982-b7dd-8eb7784f06c8)

![image](https://github.com/user-attachments/assets/ad778fae-6fbb-4d28-b2b4-1e2de2c2ab52)

## implicit relative path

```

In this challenge we are asked to execute the run programme from the challenge directory.

We enter the challenge directory by doing *cd /challenge*

We then run the programme using *./run*
By using ./ we make it clear that the shell should look for run in /challenge

this returns the flag

Flag -> kzLeDdJZQCIaHA59NnVwkfIVx4f.dFTN1QDL4czN0czW

```
![image](https://github.com/user-attachments/assets/42a88925-5e7a-4911-8542-5c97e85d7aab)

## home sweet home

```
In this challenge we are asked to execute hte run programme present in the challenge directory.
howver this time it will return it to a file of our choice that we set as the argument.
As such when using an argument we can only make it 3 characters long.
By considering ~ as our /home/hacker we can use the argument ~/x means the file or directory x inside your home directory. It is equivalent to /home/hacker/x.

Thus we use the command */challenge/run ~/x*
meaning /challenge/run to write the output (in this case, the flag) to the file x located in your home directory (/home/hacker/x)
This automatically returns the flag.

In simple words ->
Command: /challenge/run (This is the main action: "Run the challenge!")
Argument: ~/x (This tells the computer where to put the result, in a file called x in your home folder)
it gets expanded to /home/hacker/x. So the argument is essentially telling the command where to store the result.

Flag -> EM4F1PXVV5X2MHsBf5VpnCPNbs8.dNzM4QDL4czNcZW

```
![image](https://github.com/user-attachments/assets/f1e8c511-6000-4d9a-b65a-7982d1fc0700)







