# ARMssembly3

## method


```
What integer does this program print with argument 4012702611? File: chall_3.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```


```	asm
func1:
  stp     x29, x30, [sp, -48]!   // Push the frame pointer (x29) and return address (x30) to the stack.
  add     x29, sp, 0    // Set x29 as the current frame pointer.
  str     w0, [x29, 28]   // Store the input value (in w0) at (x29 + 28).
  str     wzr, [x29, 44]  // Initialize (x29 + 44) to 0.
  b       .L2   // Branch to label .L2 

.L4:                         
  ldr     w0, [x29, 28] // Load the current value from (x29 + 28) into w0.
  and     w0, w0, 1 // Perform a bitwise AND operation with 1 (check if the value is odd).
  cmp     w0, 0 // Compare the result of the AND operation with 0 (check parity).
  beq     .L3 // If the value is even, branch to label .L3.

  // If the value is odd:
  ldr     w0, [x29, 44] // Load the current accumulated value from (x29 + 44).
  bl      func2 // Call func2 with the current value.
  str     w0, [x29, 44] // Store the result of func2 back into (x29 + 44).

.L3:   .
  ldr     w0, [x29, 28] // Load the current value from (x29 + 28).
  lsr     w0, w0, 1 // Performs a logical shift right by 1 (divide the value by 2).
  str     w0, [x29, 28] // Store the updated value back at (x29 + 28).

.L2:  
  ldr     w0, [x29, 28] // Load the current value from (x29 + 28).
  cmp     w0, 0 // Compare the value with 0.
  bne     .L4 // If the value is not zero, branch back to .L4 (continue the loop).

  // Exit the loop:
  ldr     w0, [x29, 44]  // Load the final accumulated result from [x29 + 44].
  ldp     x29, x30, [sp], 48  // Restore the frame pointer and return address from the stack.
  ret  // Return to the caller.

func2:
  sub     sp, sp, #16  // Reserve 16 bytes on the stack for local variables.
  str     w0, [sp, 12] // Store the input value in [sp + 12].
  ldr     w0, [sp, 12] // Load the input value back into w0
  add     w0, w0, 3    // Add 3 to the value in w0
  add     sp, sp, 16   // Restore the memroy
  ret                  // Return to the caller with the result in w0.

```

func1 processes the input value (w0) in a loop It checks each bit of the input value to determine if it is odd or even
If it is odd (1) then it goes to func2
Whether odd or even, the value is shifted right by 1 (effectively dividing it by 2).
This process continues until the input value becomes 0 hence allowing us to test it.

From this we can understand that it is counting the number of `1s` of binary that are present in the number.

func2 simply adds 3 to the value passed to it.
The accumulated value is stored in [x29 + 44] and updated whenever func2 is called.
The result is returned in w0 at the end of func1


Now Looking at Main: 
```asm
main:
  stp     x29, x30, [sp, -48]!       
  add     x29, sp, 0        
  str     w0, [x29, 28] 
  str     x1, [x29, 16] 

  ldr     x0, [x29, 16] This loads our input from x29, 16
  add     x0, x0, 8 // increments address pointing by 8
  ldr     x0, [x0] // Load the value entered.

  bl      atoi  // Convert the string argument to an integer. Result in w0.
  bl      func1 // Call `func1` with the converted integer.
  str     w0, [x29, 44] // Store the result of `func1` into [x29 + 44].

  adrp    x0, .LC0 // Load the address of the format string ("Result: %ld\n") into x0.
  add     x0, x0, :lo12:.LC0
  ldr     w1, [x29, 44] // Load the result from [x29 + 44] into w1 (second argument to `printf`).
  bl      printf // Call `printf` to display the result.

  nop                            
  ldp     x29, x30, [sp], 48        
  ret
```

This first takes the input then loads it. next it converts it to integer format from string. 
After that we call func1 using it which goes throught the loops. afterwards its stored into [x29 + 44] next we load the tag with result and complete the address and then load the result into it. 
getting it printed.

All the work is being done in the functions so hence we can just count the number of 1s in the binary number of `4012702611` which is 21
Hence we can do 21 x 3 = 63 Then convert it to hex. Where we get 3F

## flag

> picoCTF{00003f}