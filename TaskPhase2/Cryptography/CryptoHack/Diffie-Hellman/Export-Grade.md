# Export Grade

### Challenge

Image

### Solving

Upon starting up the server and multiple testing we can realise multiple things:
1. Server sends a text ``Intercepted from Alice: {'supported': ['DH1536', 'DH1024', 'DH512', 'DH256', 'DH128', 'DH64']}`` This is essentially DH parameters that are used to understand the size of prime numbers especially for ``p``
2. We can then send a supposed list to Bob for what p should be.
3. The server then sends back what Bob had chosen, We can then just enter this to Alice
4. The server then provides us with all the parameters  such as g, p, A, B, iv and the encrypted flag.

Now essentially what they want us to do is send a smaller prime number possibility to be used in this protocall such as ``DH64``
This makes it easier to bruteforce and decrypt the flag, hence we make a similar script to last time using the same flag decoder excpt this time we will use the python function ``discrete logarithim`` to derive the Alice's private key. From there i can construct ``shared secrets`` to which we can then use the decryption technique for the flag as where provided in previous challs.


```python
from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Util.Padding import unpad
from json import loads, dumps
from Crypto.Cipher import AES
from hashlib import sha1 as hashlib_sha1 
from pwn import remote
import json


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):

    sha1_hash = hashlib_sha1() 
    sha1_hash.update(str(shared_secret).encode('ascii'))
    key = sha1_hash.digest()[:16]
    
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


conn = remote("socket.cryptohack.org", 13379)
conn.readline()
conn.sendline(dumps({"supported": ["DH64"]}).encode())
conn.readline()
conn.sendline(dumps({"chosen": "DH64"}).encode())
conn.readuntil(b"from Alice: ")
recv = loads(io.readline())

p = int(recv["p"], 16)
g = int(recv["g"], 16)
A = int(recv["A"], 16)
a = discrete_log(p, A, g) #since p is small due to the fact we set it to DH64 smallest prime

conn.readuntil(b"from Bob: ")
recv = loads(conn.readline())
B = int(recv["B"], 16)

conn.readuntil(b"from Alice: ")
recv = loads(conn.readline())
iv = recv["iv"]
ciphertext = recv["encrypted_flag"]

shared_secret = pow(B, a, p)
print(decrypt_flag(shared_secret, iv, ciphertext))
```
Running this returns the flag.

### Method

> crypto{d0wn6r4d35_4r3_d4n63r0u5}