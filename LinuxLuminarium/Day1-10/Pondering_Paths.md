# Pondering Paths

## The Root

```

In this challenge its asking us to enter a directory called pwn which automatically invokes a programme we can enter it by doing */pwn*. Upon entering this command it gives us back the flag.
This allows us to access the pwn directory contained in the root directory

```


## Program and absolute paths

```

In this challenge we are entering a directory challenge that is located in the root directory / inside this challenge directory there is another directory called run which like the previous challenge automatically runs a programme when entered returning the flag.

we just execute */challenge/run* and we get back the flag

```

## Position thy self

```

In this challenge we are asked to access the /challenge/run directory. After that it will prompt us where exactly we need to change the directory before rerunning the /challenge/run programme.

we do this with the following commands

*/challenge/run*

however then it prompts us with a message asking us to access the directory to /usr/share/doc/fontconfig

hence we use *cd /usr/share/doc/fontconfig*

which switches us to the fontconfig directory hence we rerun

*/challenge/run*
and have recieved our key

```

## Position yet Elsewhere

```

```