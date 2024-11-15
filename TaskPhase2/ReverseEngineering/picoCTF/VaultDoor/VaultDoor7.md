# vault-door-7

## Method

```
This vault uses bit shifts to convert a password string into an array of integers.
Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java
```

**Hint:**  Use a decimal/hexadecimal converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
**Hint:**  You will also need to consult an ASCII table such as this one: https://www.asciitable.com/

```java
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor7 {
    public static void main(String args[]) {
        VaultDoor7 vaultDoor = new VaultDoor7();
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

    // Each character can be represented as a byte value using its
    // ASCII encoding. Each byte contains 8 bits, and an int contains
    // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
    // example: if the hex string is "01ab", then those can be
    // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
    // bytes are represented as binary, they are:
    //
    // 0x30: 00110000
    // 0x31: 00110001
    // 0x61: 01100001
    // 0x62: 01100010
    //
    // If we put those 4 binary numbers end to end, we end up with 32
    // bits that can be interpreted as an int.
    //
    // 00110000001100010110000101100010 -> 808542562
    //
    // Since 4 chars can be represented as 1 int, the 32 character password can
    // be represented as an array of 8 ints.
    //
    // - Minion #7816
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734304867
            && x[6] == 942695730
            && x[7] == 942748212;
    }
}
```
Passes string we enter to checkPassword. This first does converts the password using the function passwordToIntArray.

From the notes left by the minion above we can understand that each char from a string can be first converted into a hex value that represent a byte. Then each hex value can be converted into 8 bit binary. From here the bianry is grouped together than converted into decimal.

When he was encrypting the password each character in the password is converted into its ASCII byte value.
Then its packed together to form a single 32 bit integer. The full password then contains 32 characters is then split into 8 groups where each group represents an integer.

He has also mentioned that a 32 character password can be represented as 8 integers. we see 8 integer comparisons for each part of the array.
The way we can go back about this is first convert each integer back to its binary value. After that splice each one into 4. then convert each binary equivalent into its hex ascii. Then convert it directly to ascii

Hence i made a python script to do it : 

```python
def int_to_hex_ascii(num):
    # Convert the integer to a 32-bit binary string
    binary_str = f'{num:032b}'
    
    # Split the binary string into 4 bytes (each 8 bits)
    bytes_ = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each byte (binary) to its corresponding hexadecimal ASCII value
    hex_chars = [chr(int(byte, 2)) for byte in bytes_]
    
    # Join the hex characters into a string
    return ''.join(hex_chars)

def decode_password(integers):

    decoded_password = ""
    for num in integers:
        decoded_password += int_to_hex_ascii(num)
    return decoded_password

integers = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734304867,
    942695730,
    942748212
]

decoded_password = decode_password(integers)

flag = f"picoCTF{{{decoded_password}}}"

print("The flag is:", flag)

```

When running this i recieve the flag. Finally.


## Flag 

> picoCTF{A_b1t_0f_b1t_sh1fTiNg_dc80e28124}

