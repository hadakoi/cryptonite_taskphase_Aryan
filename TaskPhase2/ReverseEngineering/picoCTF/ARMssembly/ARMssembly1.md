# ARMssembly1

## Method

```
For what argument does this program print `win` with variables 79, 7 and 3? File: chall_1.S

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

Our ASM file: 

```asm
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 79
	str	w0, [sp, 16]
	mov	w0, 7
	str	w0, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
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
	bl	func
	cmp	w0, 0
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

When solving now I am going to annotate it as the last file was way to messy D:


First understanding the function: 

### FUNC
 
```asm
func:
	sub	sp, sp, #32 // Declaring stack pointer and moving it 32 bytes allocating space

	str	w0, [sp, 12] // This stores the value in register w0 into memory at the address (sp + 12) = w0 from main.

	mov	w0, 79 // the value 79 is moved into register w0 = 79

	str	w0, [sp, 16] //  This stores the value in register w0 into the memory at the address (sp + 16) = 79

	mov	w0, 7 // the value 7 is moved into w0 = 7

	str	w0, [sp, 20] // This stores the value in register w0 into the memory at the address (sp + 20) = 7

	mov	w0, 3 // the value 3 is moved into w0 = 3

	str	w0, [sp, 24] // This stores the value in register w0 into the memory at the address (sp + 24) = 3

	ldr	w0, [sp, 20] // w0 = (sp+20) = 7

	ldr	w1, [sp, 16] // w1 = (sp + 16) = 79

	lsl	w0, w1, w0 // w0 = 79 << 7 = 10112

	str	w0, [sp, 28] // (sp + 28) = w0 = 10112

	ldr	w1, [sp, 28] // w1 = (sp + 28) = 10112

	ldr	w0, [sp, 24] // w0 = (sp + 24) = 3

	sdiv	w0, w1, w0 // w0 = w1 / w0 = 10112 / 3 = 3370

	str	w0, [sp, 28] // (sp + 28) = w0 = 3370

	ldr	w1, [sp, 28] // w1 = (sp + 28) = 3370

	ldr	w0, [sp, 12] // w0 = (sp + 12) = (value at sp + 12 which is from main)

	sub	w0, w1, w0 // w0 = w1 - w0 = 3370 - (sp + 12)

	str	w0, [sp, 28] // *(sp + 28) = w0 = <result of the subtraction>

	ldr	w0, [sp, 28] // w0 = (sp + 28) = <final result after subtraction>

	add	sp, sp, 32  //  readjust memory 

	ret // return from function
```
for the lsl i had to go into c and do it it is basically a left shfift
Any time im doing ``sp + int value`` it is the address as thought it was a pointer.

The function essentially does ``3370 - w0``
So now lets move onto main:


### MAIN

```asm

.LC0: // tag entered when we win
	.string	"You win!"
	.align	3

.LC1: // tag entered when we lose
	.string	"You Lose :("


.text
.align	2
.global	main
.type	main, %function
main:

	stp	x29, x30, [sp, -48]! // stores the link register (x30) and the frame pointer (x29) onto the stack. It also adjusts the stack pointer (sp) by -48 to allocate space for them

	add	x29, sp, 0 //  copies the current stack pointer (sp) into the frame pointer (x29)

	str	w0, [x29, 28] // First argument passed to Main stored in x29, 28
	str	x1, [x29, 16] // not really necessary

	ldr	x0, [x29, 16] // Loads the value stored at [x29 + 16] (the memory location where x1 was stored) into register x0.

	add	x0, x0, 8 // Moves the pointer 8 bytes in memory 
	ldr	x0, [x0] // This instruction is is used to load value from the memory address pointed by x0 back into x0


	bl	atoi // converts x0 to a integer
	str	w0, [x29, 44] // stored in x29 + 44 bytes
	ldr	w0, [x29, 44] // loads the integer value back from it as it prepares the integer for the next set.

	bl	func // Starts a function where w0 = 3370 - w0 (entered)

	cmp	w0, 0 
	bne	.L4 // if it is not equal to 0 go to .L4

	adrp	x0, .LC0 // if it returns 0 we get you win!
	add	x0, x0, :lo12:.LC0 // completes the address
	bl	puts // puts the string "You Win!"
	b	.L6 // skips to .L6

.L4: // if less than 0 
	adrp	x0, .LC1  // we get you lose :(
	add	x0, x0, :lo12:.LC1 // completes address
	bl	puts // that we have lost


.L6:
	nop // acts as placeholder
	ldp	x29, x30, [sp], 48 // does nothing
	ret

```

From this we can understand that if we want a win condition it should be equal to 0.

And we know in the function we are subtracting 3370 hence we can just convert 3370 to hex and make that our flag as that is the format -> ``D2A`` we then get our flag.


## Flag

> picoCTF{00000D2A}
