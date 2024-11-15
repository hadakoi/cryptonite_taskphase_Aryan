# vault-door-6

## Method

```
This vault uses an XOR encryption scheme.
The source code for this vault is here: VaultDoor6.java
```

**Hint:**  If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.

```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
```

from the checkPassword function we can recognise that in the for loop that passBytes[i] is being ``XORed`` with 0x55 from this
and the hint we know that X ^ Y = Z, Z ^ Y = X. We already have the possible password which is myBytes. 

we can just exor each array element with ``0x55`` This then allows us to find the hex ascii equivalent of it all.

I made use of this script to get the flag.

```python
# Define the byte array
myBytes = [
    0x3b, 0x65, 0x21, 0x0a, 0x38, 0x00, 0x36, 0x1d,
    0x0a, 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0x0a,
    0x21, 0x1d, 0x61, 0x3b, 0x0a, 0x2d, 0x65, 0x27,
    0x0a, 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
]

# XOR key
xor_key = 0x55

# Perform XOR operation on each byte
result = [byte ^ xor_key for byte in myBytes]

# Convert XORed bytes to string
result_string = ''.join(chr(byte) for byte in result)

# Print the original and resulting strings
print("Original bytes:", [hex(byte) for byte in myBytes])
print("XORed bytes as string:", result_string)

```

## Flag 

> picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}