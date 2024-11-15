# vault-door-8

## Method

```
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! 
The result is a quite mess, but I trust that my best special agent will find a way to solve it. 
The source code for this vault is here: VaultDoor8.java
```

**Hint:**  Clean up the source code so that you can read it and understand what is going on.
**Hint:** Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.

```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*; import javax.crypto.Cipher; import javax.crypto.spec.SecretKeySpec;
import java.security.*; class VaultDoor8 {public static void main(String args[]) {
Scanner b = new Scanner(System.in); System.out.print("Enter vault password: ");
String c = b.next(); String f = c.substring(8,c.length()-1); VaultDoor8 a = new VaultDoor8(); if (a.checkPassword(f)) {System.out.println("Access granted."); }
else {System.out.println("Access denied!"); } } public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
char[] a = password.toCharArray(); for (int b=0; b<a.length; b++) {char c = a[b]; c = switchBits(c,1,2); c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ c = switchBits(c,5,6); c = switchBits(c,4,7);
c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ c = switchBits(c,3,4); c = switchBits(c,2,5); c = switchBits(c,6,7); a[b] = c; } return a;
} public char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit
that was in position p2 to position p1. Precondition: p1 < p2 */ char mask1 = (char)(1 << p1);
char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ char bit1 = (char)(c & mask1); char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ char rest = (char)(c & ~(mask1 | mask2)); char shift = (char)(p2 - p1); char result = (char)((bit1<<shift) | (bit2>>shift) | rest); return result;
} public boolean checkPassword(String password) {char[] scrambled = scramble(password); char[] expected = {
0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 }; return Arrays.equals(scrambled, expected); } }
```

This is a bit messy and like the hint says lets reformat it.

```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor8 {
    public static void main(String args[]) {
        Scanner b = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String c = b.next(); 
        String f = c.substring(8, c.length() - 1); // Remove "picoCTF{" from the input
        
        VaultDoor8 a = new VaultDoor8(); 
        if (a.checkPassword(f)) {
            System.out.println("Access granted."); 
        } else {
            System.out.println("Access denied!"); 
        } 
    }

    public char[] scramble(String password) {
        /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray(); 
        for (int b = 0; b < a.length; b++) {
            char c = a[b]; 
            c = switchBits(c, 1, 2); 
            c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ 
            c = switchBits(c, 5, 6); 
            c = switchBits(c, 4, 7);
            c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ 
            c = switchBits(c, 3, 4); 
            c = switchBits(c, 2, 5); 
            c = switchBits(c, 6, 7); 
            a[b] = c; 
        }
        return a;
    }

    public char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
           that was in position p2 to position p1. Precondition: p1 < p2 */
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ 
        char bit1 = (char)(c & mask1); 
        char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
                                       System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ 
        char rest = (char)(c & ~(mask1 | mask2)); 
        char shift = (char)(p2 - p1); 
        char result = (char)((bit1 << shift) | (bit2 >> shift) | rest); 
        return result;
    }

    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password); 
        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 
            0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 
            0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 
            0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
        }; 
        return Arrays.equals(scrambled, expected);
    }
}
```

Now that it is reformatted we can look at it properly.

This is not exactly and encryption upon further look but rather a scramble of sorts.
First the password entered is converted into characters.

After that it goes through every character and peforms bitswaps on them using the ``switchBits()`` function
we are inputting a character also known as c. Then we specify 2 locations p1 and p2 This function creates 2 masks.
if p1 = 1 and p2 = 2, mask1 will have a 1 at position 1 and mask2 will have a 1 at position 2.

It then extracts the bits at positions p1 and p2 by using bitwise AND (&) with the masks. These extracted bits are stored as bit1 and bit2

The remaining bits are isolated using the bitwise AND operations with the inverse of the masks: ``rest = c & ~(mask1 | mask2)``
The function then shift bit1 and bit2 to their new position combining them with the rest of the bits to create a final result.
Finally we get a new character with 2 bits swapped.

**Essentially ->** The function creates two masks to isolate bits at positions `p1` and `p2`, extracts these bits, isolates the rest of the bits, swaps the selected bits, and combines them back to form a new character.

for eg:
switchBits(c, 1, 2) — Swap bits 1 and 2.
so essentially each character undergoes around 8 bit swaps. The masks essentially just seperate the bits to swap from the rest.

To unscrable this password we can just apply the bit swaps but in the opposite order. while reusing the bitSwap function.

My script to solve it

```python
def switch_bits(c, p1, p2):
    """Reverses the bit switching by swapping the bits at positions p1 and p2."""
    # Create masks to isolate bits at positions p1 and p2
    mask1 = 1 << p1
    mask2 = 1 << p2

    # Extract bits at positions p1 and p2
    bit1 = c & mask1
    bit2 = c & mask2

    # Isolate the rest of the bits that are not being swapped
    rest = c & ~(mask1 | mask2)

    # Calculate the shift needed to swap bits
    shift = p2 - p1

    # Perform the bit swap: shift the bits and combine with the rest of the bits
    result = (bit1 << shift) | (bit2 >> shift) | rest

    return result

def unscramble(scrambled):
    
    unscrambled = []
    
    for byte in scrambled:

        byte = switch_bits(byte, 6, 7)
        byte = switch_bits(byte, 2, 5)
        byte = switch_bits(byte, 3, 4)
        byte = switch_bits(byte, 0, 1)
        byte = switch_bits(byte, 4, 7)
        byte = switch_bits(byte, 5, 6)
        byte = switch_bits(byte, 0, 3)
        byte = switch_bits(byte, 1, 2)
        unscrambled.append(byte)
    
    return unscrambled

scrambled_password = [
    0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 
    0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 
    0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 
    0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
]


unscrambled_password = unscramble(scrambled_password)

unscrambled_string = ''.join(chr(byte) for byte in unscrambled_password)
print(f"Unscrambled Password: {unscrambled_string}")

```

Upon running this we get the flag.

## Flag 

> picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}
