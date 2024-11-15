# ARMssembly0

## Method


```
What integer does this program print with arguments 266134863 and 1592237099? 
File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
```

Upon opening the chall.S file. .S files are assembly language source code.

from the first line ``.arch armv8-a``

The challenging is dealing with arm64. We know this as 64 bits = 8 bytes.

These lines with it are the metadata or directive.
There's lines such as ``.file "chall.c"``, ``.text``, ``.align 2``, ``global	func1``, ``.type	func1, %function``

- "chall.c" suggests that this assembly file was generated by compiling a C source file
- ".align 2" aligns the code on a 4-byte boundary
- ".global func1" declares func1 as a global symbol. essentially like general programming the func1 can be accessed from other files or parts of the program
- ".type func1, %function" tells the assembler that func1 is not a variable but a function.

Below this we see sever `labels` some beginning with `.L`, `.LC0`

For `.L` labels we can understand that these are branches to the Lines of assembly under them and the lines of assembly are executed after the specific .L branch is gone through.


For `.LC` labels marks a unique location in memory where such data is kept. This is most likely for constant 

In this case we can see 2 branches .L2: and .L3:

We can also see data label .LC0 which is essentially used for constant data string "Result: %ld\n" referenced by a label.
It is simply a marker or pointer to a specific location in memory where data (like a string) is stored.

In this also we see the declarations for a main function refers to the entry point of the program.

so now we can look at the func1 later that means and start with the ``main`` function

```asm
.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
---

**Register Usage:** 

in ARM assembly x0 to x30 are 64-bit general registers used for holding data, function arguments etc 

``x0 -> x7`` are used for function arguments and return values 

``x19 -> x28`` is known as ``callee-saved registers`` <br>
They are like temporary storage. <br>
Its for function use where the value stored at the locations is used then if changed or not it is restored before returning to where it was called.

``x29`` is known as a ``frame pointer`` <br>
It’s like a bookmark that points to the start of the function's stack frame. We can understand from here that it is a section of memory that operates based on the stack protocals like push and pop for storing data etc.

It is like a pointer to the start of the function's local workspace

``x30`` is known as a ``Link register`` is like a pointer to where the program should go back to after the function finishes

``w0 to w30`` registers are 32 bit registers that hold the lower 32 bits of the corresponding x registers. for example w0 is the lower 32 bits of x0 

---

**Continuing with solve:**

- ``stp	x29, x30, [sp, -48]!`` 

stp stores 2 registers x29 and x30. 

x29 holds the start of the function’s stack frame and x30 holds the return address

sp is the stack pointer it points to the current top of the stack.

-48 means 48 bytes before the current position of the stack pointer. 

This is where the ! will move the sp to where we moved the pointer to and set it there and this will be stored in the x29 and x30 registers.

- ``add x29, sp, 0``

This equates to x29 = sp + 0. This means we are setting the starting register of the stack frame to sp.

- ``str	x19, [sp, 16]``

it stores the value from the x19 register at the memory address 16 bytes higher than the current stack pointer

- ``str	w0, [x29, 44]``

it stores the value from the w0 register (32 bit lower part of x0 register) into the memory location 44 bytes higher than the x29 register.

- ``str	x1, [x29, 32]``

it stores the value from the x1 register 32 bytes higher than the x29 register address.

- ``ldr	x0, [x29, 32]``

This is the load instruction which means we're loading data from memory into a register. x0 becomes the destination register and it is 32 bytes higher than x29

**ldr->** Loads memory into a registor <br>
**str->** Stores data from a register into a memory


**Code from here to discuss:**

```asm
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
```



This is essentially where the process starts.
hence we can call it `arg0` that signifies the first argument (value passed to a register) being loaded into x0 


- ``add	x0, x0, 8 ``

This is modifying the address pointed by x0. This adds 8 bytes to the address pointed to by x0 effectively moving it 8 bytes forward.
`arg1`


- ``ldr	x0, [x0]``

This instruction is is used to load value from the memory address pointed by x0 back into x0

from here we can understand that we have to load the value of our input "266134863"

- ``bl	atoi``

This instruction is branch with link for accessing the function ASCII to integer.
it takes the string in x0 as input converts it to an integer and returns the integer result to x0.

When a value is assigned to x0, both the 64-bit value of x0 and the lower 32 bits of it are updated.

so essentially when x0 is updated its also updated in w0

- ``mov	w19, w0``
 
This instruction means that the value in w0 is being copied into w19.
This is ->
w19 = int(266134863) <br>
w19 = 266134864

- ``ldr x0, [x29, 32]``

This instruction essentially loads the value of x29 + 32 into x0
This is intentionally clearing out the space.


- ``add x0, x0, 16``

This instruction essentially modifies the address. where we are moving it 16 bytes forward. This can be called `arg2`


- ``ldr	x0, [x0]``

This instruction is is used to load value from the memory address pointed by x0 back into x0

from here we can understand that we have to load the second value of our input "1592237099"

This will now look like x0 = (266134863) "1592237099"

- ``bl	atoi``

it takes the string in x0 as input converts it to an integer and returns the integer result to x0.

- ``mov w1, w0``

from before w1 = 1592237099 

- ``mov w0, w19``

Now as we had w19 = 266134864
w0 = 266134864


- ``b1 func1``<br>

Over here we we can see the use of the ``store`` instruction. The difference between store and load is that. Load is taking a value and putting it into a register and store is taking a register and putting it on the stack.

From here we can work out the function by annotating it.

```asm

func1:
	sub	sp, sp, #16 // Moves the stack pointer down by 16 bytes (essentially opening space.)

	str	w0, [sp, 12] // This stores the value of w0 at memory adress sp + 12 = 266134864

	str	w1, [sp, 8] // This stores value of w1 at address sp+8  = 1592237099

	ldr	w1, [sp, 12] // This loads the value of sp+12 into w1 = 266134864

	ldr	w0, [sp, 8] // This loads the value of sp+8 into w0 =  1592237099

	cmp	w1, w0 // Now we are comparing the two value of w1 and w0.subtracts w0 from w1 this will be negative (-ve)

	bls	.L2 // Branch if Less or Same instruction. it will jump to L2 if w1 <= w0 which is true.

	ldr	w0, [sp, 12]  // This is skipped as the bls statement was true.

	b	.L3 // unconditional jump to L3
  
.L2:
	ldr	w0, [sp, 8] // This keeps w0 as the same thing = 1592237099

.L3:
	add	sp, sp, 16 // (Closes the opened space)
	ret (returns)
	.size	func1, .-func1
	.section	.rodata
	.align	3
  

```

**Once we have returned:**

```
mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
```


- ``mov	w1, w0``

This sets w1 = 1592237099

- ``adrp x0, .LC0``

it loads the address of the 4KB-aligned page that contains .LC0 into x0. This is to print the result.


- ``add x0, x0, :lo12:.LC0``

This instruction adds the low 12 bits of the address of .LC0 to x0 to complete the address.

Now x0 holds the address of the 4KB page where .LC0 is located.

- ``bl printf``

This instruction performs a branch with link (bl) to the printf function.
This prints the string located at x0

- ``mov w0, 0``

This instruction sets the value of w0 to 0

0 is typically used to return values from functions. By setting it to 0, the program is preparing to return 0 as the return value for the current function. as this file was made from a c file we can assume it has successfully executed. When a function in ARM assembly finishes it typically places its return value in w0

Hence code after this we dont need to understand from here we can understand its just printing the larger integer which for us is 1592237099.

As the picoCTF flag format for this was picoCTF{XXXXXXXX} we need to convert it.

This essentially becomes 5EE79C2B Hence we have our flag


## Flag

> picoCTF{5EE79C2B}