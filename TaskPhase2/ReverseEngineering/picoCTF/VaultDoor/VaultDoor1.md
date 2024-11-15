# vault-door-1

## Method

```
This vault uses some complicated arrays! I hope you can make sense of it, special agent. 
The source code for this vault is here: VaultDoor1.java
```

**Hint:** Look up the charAt() method online.

```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
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

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '3' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == 'f' &&
               password.charAt(30) == 'b' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '6' &&
               password.charAt(26) == 'f' &&
               password.charAt(31) == '0';
    }
}

```

Now this issue with this code is that it firstly takes a password. again stripping the picoCTF{} from what we are entering then its manually checking the string through splicing it as an array for example password.charAt(0)  == 'd' checks if the ``text index[0] = d`` and it has multiple and statements to check all of the strings we can manually piece together this string then. We also Know its 32 characters long.

From this we can map each line 

```markdown
- **The first character** is 'd' (index 0): `password.charAt(0) == 'd'`
- **The 30th character** is '3' (index 29): `password.charAt(29) == '3'`
- **The 5th character** is 'r' (index 4): `password.charAt(4) == 'r'`
- **The 3rd character** is '5' (index 2): `password.charAt(2) == '5'`
- **The 24th character** is 'r' (index 23): `password.charAt(23) == 'r'`
- **The 4th character** is 'c' (index 3): `password.charAt(3) == 'c'`
- **The 18th character** is '4' (index 17): `password.charAt(17) == '4'`
- **The 2nd character** is '3' (index 1): `password.charAt(1) == '3'`
- **The 8th character** is 'b' (index 7): `password.charAt(7) == 'b'`
- **The 11th character** is '_' (index 10): `password.charAt(10) == '_'`
- **The 6th character** is '4' (index 5): `password.charAt(5) == '4'`
- **The 10th character** is '3' (index 9): `password.charAt(9) == '3'`
- **The 12th character** is 't' (index 11): `password.charAt(11) == 't'`
- **The 16th character** is 'c' (index 15): `password.charAt(15) == 'c'`
- **The 9th character** is 'l' (index 8): `password.charAt(8) == 'l'`
- **The 13th character** is 'H' (index 12): `password.charAt(12) == 'H'`
- **The 21st character** is 'c' (index 20): `password.charAt(20) == 'c'`
- **The 15th character** is '_' (index 14): `password.charAt(14) == '_'`
- **The 7th character** is 'm' (index 6): `password.charAt(6) == 'm'`
- **The 25th character** is '5' (index 24): `password.charAt(24) == '5'`
- **The 19th character** is 'r' (index 18): `password.charAt(18) == 'r'`
- **The 14th character** is '3' (index 13): `password.charAt(13) == '3'`
- **The 20th character** is '4' (index 19): `password.charAt(19) == '4'`
- **The 22nd character** is 'T' (index 21): `password.charAt(21) == 'T'`
- **The 17th character** is 'H' (index 16): `password.charAt(16) == 'H'`
- **The 28th character** is 'f' (index 27): `password.charAt(27) == 'f'`
- **The 31st character** is 'b' (index 30): `password.charAt(30) == 'b'`
- **The 26th character** is '_' (index 25): `password.charAt(25) == '_'`
- **The 23rd character** is '3' (index 22): `password.charAt(22) == '3'`
- **The 29th character** is '6' (index 28): `password.charAt(28) == '6'`
- **The 27th character** is 'f' (index 26): `password.charAt(26) == 'f'`
- **The 32nd character** is '0' (index 31): `password.charAt(31) == '0'`
```

Hence mapping this out we get d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0

## Flag 

> picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}