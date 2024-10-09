# Shell Variables 

---

## Printing Variables

### Description
The goal of this challenge is to retrieve and print the value of a variable called `FLAG`, which holds the flag. The program `/challenge/run` won't provide the flag directly, but since the flag is stored in the `FLAG` variable, we can solve the challenge by printing the variable's contents using basic shell commands.
The command `echo $FLAG` will print the contents of the `FLAG` variable, which is what we need to solve this challenge.

### Info / Stuff We should Know
In Linux, environment variables can be printed using the `echo` command. When you want to print a variable, you prepend its name with a `$`. For example:
- `echo Hello` prints "Hello" to the console.
- `echo $PWD` prints the current working directory stored in the `PWD` variable.

### Step-by-Step Solution
Command to print the flag variable:

```bash
echo $FLAG
```

### Flag
> 07R8UVOEhAaF6VXErnolYWrI9hG.ddTN1QDL4czN0czW

![image](https://github.com/user-attachments/assets/b557d52f-63a0-4302-85c8-0903c68ebd57)

---
