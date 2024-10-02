# Hello Hackers Module

## Short Notes

```
make sure when connecting on linux terminal that you are in the file containing key. 

ssh -i key hacker@pwn.college

The ssh allows us access to a remote machine over the netowrk while passing our key.

The -i key specifies the file contaning the provate key to use for authentication.

The hacker@pwn.college specifies the username of the hacker and the hostname of the server which are respectively hacker and pwn.college 

this connects us to the server pwn.college as the user hacker

linux commands are sensitive.
when in the terminal it will show name@dojo.

```

## Challenges

### Intro to commands
```

For this level simply invoke the *hello* command in the linux terminal. Remembering its case sensitive.
We recieve the flag and to exit the SSH session we type *exit*

```
![image](https://github.com/user-attachments/assets/85b56ddb-0ed7-4c57-bb56-efc4b45c1f4e)
![image](https://github.com/user-attachments/assets/219853d3-33b4-42b8-a318-1b268e8af97e)

### Intro to Arguments
```

To find the Flag here we run the command *hello hackers* in the terminal.
This executes the *hello* command with *hackers* as its argument hence revealing the flag

```
![image](https://github.com/user-attachments/assets/60951bb6-0afb-4728-a5fb-0c8847e1c039)


