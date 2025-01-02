# Not Supported

## Solving

```
Straightforward challenge, the flag is written on running notepad process. 
```

Now in the challenge file we have been provided with a memdump file with the .mem extension.

What this essentially is, is a RAM moment capture at a specific moment in time. As such with the challenge description we understand that there was a running notepad process currently when the memdump was taken. Hence have to open the notepad process and find the flag in it.


Basedo on the name of the file we also know it is based on ``windows11`` hence we must use volatillity 3

``vol -q -f .\memdump.mem windows.pslist.PsList``

Essentially what this does is use volatillity in quiet mode specifying the memory dump tosee when uses ``windows.pslist.PsList`` which will extract all the list of processes that where running at the time

This essentially showcases the ``PID``, ``PPID``, process name and some other info.

This took some time to run and at the end of the  we see our process of ``Notepad.exe``

Now to get the memdump of this process I can specifically get the dump for it doing ``vol -q -f .\memdump.mem -o out windows.memmap.Memmap --pid 6028 --dump``


This is similar to our last command using the Memmap plugin of vol 
This plugin lists all memory-mapped regions for a given process, such as executable code, DLLs, and mapped files. hcne we can specify the PID for the ``Notepad`` process and make a dump for it 

Now trying to find allt he strings in a flag and piping it to a result.txt file only shows half the flag meaning the flag may be on multiple lines

```shell
hadakoi@Laptop:~/ctfsolve$ strings pid.6028.dmp | grep -i "BHFlagY{" > flag_results.txt
hadakoi@Laptop:~/ctfsolve$ cat flag_results.txt
BHflagY{d22a 3  e e
hadakoi@Laptop:~/ctfsolve$ strings pid.6028.dmp | grep -i "BHFlagY{"
BHflagY{d22a 3  e e
```

As such we just make a textfile of all the strings of ``.dmp`` and then open it in a text editor where we can then search for the flag.

Which we are able to find.


## Flag

> BHflagY{d22a 3  e e d 0  5 0  c 2  3 c  0 8  8 0  c c  9 1  2 3  6 8 9 0  5  c  9  d 2 5  2 7 a  4 1 c 3 2 8  f 8 1  e f  1 1  5 b  9  4 64 b  8 0  0f 7 42 5 33 3 edb7 1d5  7b4 40b  94 d c 7  6 6a 2d 4 9 61 1 d4  69 68 47  7b09dfa1  f246585d  8 7d 7b 5 a}