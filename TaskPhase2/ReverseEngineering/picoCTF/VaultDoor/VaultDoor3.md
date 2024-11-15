# vault-door-3

## Method

```
This vault uses for-loops and byte arrays. 
The source code for this vault is here: VaultDoor3.java
```
**Hint:** Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}

```

Again like last 2 challenges they are splitting the string we enter from picoCTF{} where it then enters a checkpassword.

it basically creates a new buffer string which is supposed to become our new check

The first loop  where buffers 0->7 index will be the first 7 characters of the password.

Next it filled indices of the buffer from 8 to 15 but it takes them from the reversed position of the password starting at index 23 to 16.

The third loop fills the next set of characters (from index 16 to 31) by skipping every other index (i.e., 16, 18, 20, ...) in the buffer. However it also takes them from the reversed from indexes 46 44 etc...

The fourth loop fills the remaining characters from indices 17 to 31 (every other index in reverse order) with characters from the password string at the same index positions


Now it just compares this with ``jU5t_a_sna_3lpm18g947_u_4_m9r54f`` from this we can understand we have to jumble it based on the loops.

By using the original logic to scramble our inptut to become the ``jU5t_a_sna_3lpm18g947_u_4_m9r54f`` essentially we:

input string -> goes throguh 4 looping changers -> print the change string = jU5t_a_sna_3lpm18g947_u_4_m9r54f

So what we need to do is reverse the loops for jU5t_a_sna_3lpm18g947_u_4_m9r54f and we should be able to do it.

I made a script in python to do this. 

```python
def reverse_password(output):
    buffer = list(output)  
    password = [''] * 32
    
    # Reverse of loop 4: Copy every second character from buffer (indices 31 to 17) back to password
    for i in range(31, 16, -2):
      password[i] = buffer[i]
    
    
    # Reverse of loop 3: Copy characters from buffer (indices 16 to 31, every second position) to password
    for i in range(16, 32, 2):
      password[46 - i] = buffer[i]
    
    
    # Reverse of loop 2: Copy characters from buffer (indices 8 to 15) back to password (from 23-i)
    for i in range(8, 16):
      password[23 - i] = buffer[i]
    
    
    # Reverse of loop 1: Copy the first 8 characters directly from buffer to password
    for i in range(8):
      password[i] = buffer[i]
    
    
    finalpassword = ''.join(password)
    return finalpassword

output = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"

original_password = reverse_password(output)
print("Original password input:", original_password)

```

Running this gives us the flag.

## Flag 

> picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}