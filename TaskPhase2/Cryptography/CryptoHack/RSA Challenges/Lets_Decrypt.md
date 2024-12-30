# Let's Decrypt

## Challenge

![image](https://github.com/user-attachments/assets/3d3b5e40-c8eb-4559-ae2a-8a5342c4bba5)

13391.py

```python
#!/usr/bin/env python3

import re
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener
from pkcs1 import emsa_pkcs1_v15
# from params import N, E, D

FLAG = "crypto{?????????????????????????????????}"

MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)
SIGNATURE = pow(bytes_to_long(DIGEST), D, N)


class Challenge():
    def __init__(self):
        self.before_input = "This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_signature':
            return {
                "N": hex(N),
                "e": hex(E),
                "signature": hex(SIGNATURE)
            }

        elif your_input['option'] == 'verify':
            msg = your_input['msg']
            n = int(your_input['N'], 16)
            e = int(your_input['e'], 16)

            digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
            calculated_digest = pow(SIGNATURE, e, n)

            if bytes_to_long(digest) == calculated_digest:
                r = re.match(r'^I am Mallory.*own CryptoHack.org$', msg)
                if r:
                    return {"msg": f"Congratulations, here's a secret: {FLAG}"}
                else:
                    return {"msg": f"Ownership verified."}
            else:
                return {"error": "Invalid signature"}

        else:
            return {"error": "Invalid option"}


import builtins; builtins.Challenge = Challenge # hack to enable challenge to be run locally, see https://cryptohack.org/faq/#listener
listener.start_server(port=13391)

```

## Solving

The source code provided sets up a server that validates domain ownership using RSA signatures. It provides an RSA public key and signature for a specific message. The server then verifies signatures for incoming messages, and if the message matches a specific pattern, it returns a flag. Otherwise, it simply confirms ownership.

Now this message's plaintext is ``We are hyperreality and Jack and we own CryptoHack.org``. This plaintext is encoded into bytes then applying the ``EMSA-PKCS#1 v1.5 `` encoding scheme on to this. The 256 is the desired output length. 

This is then converted into long. It is then used signed using our private key which is done with ``M^d % N``.

Now upon looking further at the script we see that it provides -> N, e and the signature in hex when we enter the ``get_signature`` option.

Looking at the ``verify`` option it seems as though we pass our own **e, n and message** to be verified. and the text phrase should be "I am Mallory...own CryptoHack.org" Now from this we need to essentially get our own signature.

Now first off trying to just send ``get_signature`` does not work so we have to enter commands like this ``{option : get_signature}``.


**The actual solve:**

Now essentially we can solve this fairly easily. First by encoding it the message the same way:

```python
msg = "I am Mallory and I own CryptoHack.org"
Finaldigest =  bytes_to_long(emsa_pkcs1_v15.encode(msg.encode(), 256))
```
now essentially we want to make the signatures match. 

This verification is done like this ->

``Signature = (digest)^d % N`` -> DIGEST is the hashed message

During this process the servers use the public exponent e and modulus n to check if the ``signature^e mod n = digest`` <br>
If it matches the digest it is coming from the correct person.

Now they have given us a chance to enter our own e and n. This allows us to essentially make the decryption of Signature our own spoofing us to be correct.

From these lines the digest is made from our message and then checked with a signature that we calculate.

```python
digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
calculated_digest = pow(SIGNATURE, e, n)

calculated_digest
```

So because we know the digest before hand and the signature.

We can forcibly set e to 1 causing this check to just become ``Signature % n = Digest``

Now to make sure this 100% of the time equal the calculation equals digest we must set n to the difference between Signature and Digest.

This is done by doing ``Signature - Digest`` for the value of n. From this now we Understand how to possibly make it think we are the correct person.

the json request seems to be sent in the format ``{"option": "verify", "msg": msg, "N": hex(n), "e": hex(e)}``

hence we make a script using gpt

```python
from pwn import remote
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15
import json

p = remote("socket.cryptohack.org", 13391)
print(p.recvline().decode())

data = {"option": "get_signature"}
p.sendline(json.dumps(data).encode())
response = json.loads(p.recvline().decode())

signature = int(response['signature'], 16)

msg = "I am Mallory and I own CryptoHack.org"
Finaldigest = bytes_to_long(emsa_pkcs1_v15.encode(msg.encode(), 256))

e = 1 
n = signature - Finaldigest

data = {
    "option": "verify",
    "msg": msg,
    "N": hex(n),
    "e": hex(e)
}
p.sendline(json.dumps(data).encode())
response = json.loads(p.recvline().decode())

print(response['msg'])

p.close()
```

Running this will output the flag.

## Flag

> crypto{dupl1c4t3_s1gn4tur3_k3y_s3l3ct10n}
