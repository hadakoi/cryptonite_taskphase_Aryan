# Practicing Piping

## Redirecting Output
```
In this challenge we are asked to redirect word PWN to the filename COLLEGE.

To do this we  echo PWN > college

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
Append mode is different from passing the outputs but similar using >>.

```

