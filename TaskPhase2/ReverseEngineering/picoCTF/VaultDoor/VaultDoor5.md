# vault-door-5

## Method

```
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! 
The source code for this vault is here: VaultDoor5.java
```

**Hint1:** You may find an encoder/decoder tool helpful, such as https://encoding.tools/
**Hint2:** Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

```java
import java.net.URLDecoder;
import java.util.*;

class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
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

    // Minion #7781 used base 8 and base 16, but this is base 64, which is
    // like... eight times stronger, right? Riiigghtt? Well that's what my twin
    // brother Minion #2415 says, anyway.
    //
    // -Minion #2414
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    // URL encoding is meant for web pages, so any double agent spies who steal
    // our source code will think this is a web site or something, defintely not
    // vault door! Oh wait, should I have not said that in a source code
    // comment?
    //
    // -Minion #2415
    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2";
        return base64Encoded.equals(expected);
    }
}
```

The password is first taken in by the URLEncode function where each character in the password is converted to there URL-encoded form. This is added to the buf string that was made and then returned. This is of the form ``XX`` which represents the hexadecimal Ascii of a char

From here the URL-encoded string is further encoded into a Base64 representation that transforms binary data into an ascii string. This is the final encrypted password.


Luckily they have already given the format URL encoded string. So we can just decrypt this
Remove the J prefix:
This is part of the encoding format. Each %XX is represented as JXXXX

Decrypting the Encrypted Password 
The expected format has strings in a state that looks like base 64 but currently isnt. This is due to the J prefix.

Essentially putting it through a base64 decoder we get ->

``%63%30%6e%76%33%72%74%31%6e%67%5f + %66%72%30%6d%5f%62%61%35%65%5f%36 + %34%5f%30%62%39%35%37%63%34%66``

Now we can see that it is in hexadecimal values of ascii. using a decrypter online for this we get the flag c0nv3rt1ng_fr0m_ba5e_64_0b957c4f


Notes:
Essentially Password is encoded with URL-encoding to become hexa ascii. Then its base64 encoded. Encryption done.
We know what the expected is hence we can decrypt it using base64 wich makes it hexa ascii for which we can then convert it into our original password

## Flag 

> picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}