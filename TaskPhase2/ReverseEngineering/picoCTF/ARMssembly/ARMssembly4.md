# ARMssembly4

## method

```
What integer does this program print with argument 1151828495? File: chall_4.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

**Hint is: Switching things up**


```asm

func1:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 100
	bls	.L2
	ldr	w0, [x29, 28]
	add	w0, w0, 100
	bl	func2
	b	.L3

.L2:
	ldr	w0, [x29, 28]
	bl	func3

.L3:
	ldp	x29, x30, [sp], 32
	ret

func2:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 499
	bhi	.L5
	ldr	w0, [x29, 28]
	sub	w0, w0, #86
	bl	func4
	b	.L6

.L5:
	ldr	w0, [x29, 28]
	add	w0, w0, 13
	bl	func5

.L6:
	ldp	x29, x30, [sp], 32
	ret

func3:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	bl	func7
	ldp	x29, x30, [sp], 32
	ret

func4:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	mov	w0, 17
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func1
	str	w0, [x29, 44]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 48
	ret

func5:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	bl	func8
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 32
	ret

func6:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 314
	str	w0, [sp, 24]
	mov	w0, 1932
	str	w0, [sp, 28]
	str	wzr, [sp, 20]
	str	wzr, [sp, 20]
	b	.L14

.L15:
	ldr	w1, [sp, 28]
	mov	w0, 800
	mul	w0, w1, w0
	ldr	w1, [sp, 24]
	udiv	w2, w0, w1
	ldr	w1, [sp, 24]
	mul	w1, w2, w1
	sub	w0, w0, w1
	str	w0, [sp, 12]
	ldr	w0, [sp, 20]
	add	w0, w0, 1
	str	w0, [sp, 20]

.L14:
	ldr	w0, [sp, 20]
	cmp	w0, 899
	bls	.L15
	ldr	w0, [sp, 12]
	add	sp, sp, 32
	ret

func7:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	cmp	w0, 100
	bls	.L18
	ldr	w0, [sp, 12]
	b	.L19

.L18:
	mov	w0, 7

.L19:
	add	sp, sp, 16
	ret

func8:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 2
	add	sp, sp, 16
	ret

.LC0:
	.string	"Result: %ld\n"

main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret

```

Because main is alot smaller lets start with that D:

```asm
main:
  stp     x29, x30, [sp, -48]! 
  add     x29, sp, 0   
    
  str     w0, [x29, 28]  
  str     x1, [x29, 16]  
    
  ldr     x0, [x29, 16] 
  add  x0, x0, 8 // Increment the address pointer by 8
  ldr x0, [x0] // Load the string to be used

  bl atoi   // converts the string in x0 to integer
    
  str w0, [x29, 44] // Store the converted integer (result of `atoi`) in [x29 + 44].

  ldr w0, [x29, 44] // Load the converted integer stored at [x29, 44] into w0.
  bl func1 // function called

  mov w1, w0   // Move the result from `func1` (now in w0) into w1 for use as the second argument to `printf`.

  adrp  x0, .LC0  // Load the address of the format string (`"Result: %ld\n"`) into x0. The adrp instruction loads the page address.
  add x0, x0, :lo12:.LC0  // completes the address of the tag lo12

  bl printf // Call `printf` to print the result. The format string and the result are passed in x0 and w1, respectively.

  nop                              
  ldp  x29, x30, [sp], 48
  ret                              

```

Pretty standard function nothing special.
Now looking at functions ;,(

However i dont wanna do this again and the functions dont seem to special so how bout i run the file :) on linux with my suppposed input.
To compile ARMv8 as ARMv8 on a non-ARMv8 machine, we need a cross compiler. 

``sudo apt install binutils-aarch64-linux-gnu``
``sudo apt install gcc-aarch64-linux-gnu``
``sudo apt install qemu-user-static``
``sudo apt install qemu-user``

After installing them we can then run these commands for this terminal:  

```bash
hadakoi@Laptop:~/ctfsolve/ARMss$ aarch64-linux-gnu-as -o chall_4.o chall_4.S
hadakoi@Laptop:~/ctfsolve/ARMss$ aarch64-linux-gnu-gcc -static -o chall_4 chall_4.o
hadakoi@Laptop:~/ctfsolve/ARMss$ qemu-aarch64 ./chall_4 1151828495
Result: 1151828610
```
converting this to hex 44A78282
Hence this is our flag


~~Maybe i should have done this for all~~

## flag

> picoCTF{44a78282}