# ARMssembly2

## method

```
What integer does this program print with argument 4189673334? File: chall_2.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

Looking at the main function first: 

``` 
main: 

	stp	x29, x30, [sp, -48]!

	add	x29, sp, 0
	str	w0, [x29, 28] 
	str	x1, [x29, 16]
	ldr	x0, [x29, 16] // this loads our value from x29, 16 into x0

	add	x0, x0, 8 // Shifting the poitner 8 bytes
	ldr	x0, [x0] // This instruction is is used to load value from the memory address pointed by x0 back into x0
	bl	atoi // converts ASCII to decimal.

	bl	func1 // calls the func1

	str	w0, [x29, 44] // Store the return value of func1 into [x29 + 44] from w0 which was changed in func1

	adrp	x0, .LC0 // Load the address of the string "Result: %ld\n".
	add	x0, x0, :lo12:.LC0 // Adjust address to point to the string.
	ldr	w1, [x29, 44]  // Load the result from func1 into w1.
	bl	printf // call printf function

	nop

	ldp	x29, x30, [sp], 48
	ret // returns back to normal
```


Now Looking at the functions: 
```
func1:
	sub	sp, sp, #32 // space for variables 
	str	w0, [sp, 12] // store the w0 into (sp + 12)
	str	wzr, [sp, 24] // Clear register wizard and store it at (sp + 24)
	str	wzr, [sp, 28] // Clear register wizard and store it at (sp + 28)
	b	.L2 // branch to L2

.L3:
	ldr	w0, [sp, 24] // Load the value at (sp + 24) into w0
	add	w0, w0, 3 // Increment the value in w0 by 3
	str	w0, [sp, 24] // Store the updated value back into (sp + 24).

	ldr	w0, [sp, 28] // Load the value of 0 from [sp + 28] int w0
	add	w0, w0, 1 // increment the value of w0 by 1 
	str	w0, [sp, 28] // 1 is then stored in (sp + 28)

.L2:
	ldr	w1, [sp, 28] // Load the value at [sp + 28] into w1
	ldr	w0, [sp, 12] // Load the value at [sp + 12] into w0
	cmp	w1, w0 // w0 - w1 if negative then label = negative hence allows loop to continuez
	bcc	.L3 // If w1 < w0, branch to label L3 (continue the loop) else continue

	ldr	w0, [sp, 24] // Load the value at [sp + 24] into w0 (this is the result)
	add	sp, sp, 32 // reallocate space.
	ret // Return from func1.

.LC0:
	.string	"Result: %ld\n"
```
wzr stands for **Zero Register** and is a special-purpose register. It is a read-only register that always holds the value 0.

From these functions we can see:


In the loop l3 w0 is always incremented by 3 in each iteration. which means that over multiple iterations this value is effectively being multiplied by 3.
Additionally, the loop uses w28 (stored at (sp + 28)) as a counter to track how many iterations have occurred, incrementing by 1 in each iteration

In the loop2: The loop continues as long as w28 (the iteration counter) is less than the value originally passed to the function (which is stored in w12 at (sp + 12)).
Once w28 reaches the value in w0 (the original input) the loop stops

The fact that it will continue until it reaches the original value we can assume it will be muliplited by 3 as it incremements by 3 each time.

so we do 4189673334 x 3 = 12,569,020,002 converting this to hex we get 2ED2C0662 and as no capitals allowed. we change it to our liking

## flag

> picoCTF{2ed2c0662}