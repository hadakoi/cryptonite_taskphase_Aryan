# Parameter Injection

## Challenge

## Method

Upon starting up the server and multiple testing we can realise multiple things:

1. Alice first sends p, g, A values.
2. We then have to send p, g, A values to Bob, nothing really should be sent.
3. We then recieve a text from Bob with the B value.
4. Then we can send a text to Alice with a value of B
5. We then recieve the IV and the encrypted_flag values.

Remarks ->

1. p, g are our public parameters
2. A, B are our public keys.
3. Alice and bob prolly also have a, b for private keys
4. Initialization Vector And flag will be provided by Alice

Now essentially what they want us to do is change B to something that causes the ``shared_secret`` to become easily decryptable 

now the formula for shared_secret is calculated in this case by Alice using her private key ``B^a % p`` 

If we make B, 1 then it will just be ``1 % P`` and will be 1, hence we know the shared secret is a the private key.

We then recieve the IV and the Flag from alice and because we know what the shared secret is we can decrypt the flag using the previous decode script they had given us :D


Hence i made this script.
```python
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

# Send random info to Bob and ignore answer
p = remote("socket.cryptohack.org", 13371)
p.readline()

data = {"p":"0x01", "g":"0x01", "A":"0x01"}
p.sendline(json.dumps(data).encode())
p.readline()

# Send B = 1, so then shared secret = pow(B, a, p) = 1 for any a
data = {"B":"0x01"}
p.sendline(json.dumps(data).encode())
p.readuntil(b"from Alice: ")

rec = loads(p.readline())

iv, ciphertext = rec["iv"], rec["encrypted_flag"]

shared_secret = 1
print(decrypt_flag(shared_secret, iv, ciphertext))
```

## Flag

> crypto{n1c3_0n3_m4ll0ry!!!!!!!!}