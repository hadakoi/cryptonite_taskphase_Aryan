# Pondering Paths

## The Root

```

In this challenge we are tasked with invoking a program located in the root directory.
This is done by executing */pwn* where the / signifies that it is in the root directory and pwn is the executable program.
By running this commands we execute the pwn program which returns the flag.

```
![image](https://github.com/user-attachments/assets/4d5fcc1d-d6de-4297-9b23-4e881782d899)

## Program and absolute paths

```

In this challenge we will be accessing a directory called challenge which is located in the root directory (/).
Inside this challenge directory, there is an executable program named run.
When invoked, this program will automatically return the flag.

To execute the program, we need to use its absolute path: /challenge/run.
It runs the executable file present in the challenge directory and hence returns the flag.

```

![image](https://github.com/user-attachments/assets/efee2f36-d5c4-4421-a9ae-45b4dcb4058e)


## Position thy self

```

In this challenge, we need to access the /challenge/run program.
Initially, we will be prompted to change to a specific directory before rerunning the /challenge/run program.

Hence like before we use the /challenge/run command only to see it prompt us an error message and asking us to navigate to
a different directory called /usr/share/doc/fontconfig

to do that we must use this specific command *cd /usr/share/doc/fontconfig* which allows us to enter the specific directory which is fontconfig
once we have entred this specific directory we may finally run the programme contained in challenge using /challenge/run

```

![image](https://github.com/user-attachments/assets/c9083793-d2ae-457d-93c7-e645d6f1de16)


## Position yet Elsewhere

```

```
