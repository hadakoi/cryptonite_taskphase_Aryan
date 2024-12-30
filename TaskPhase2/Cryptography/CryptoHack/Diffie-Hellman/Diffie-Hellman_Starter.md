# Diffie-Hellman Starter

---

## Working with Fields

### Challenge

![image](https://github.com/user-attachments/assets/2eec6b47-fda2-48a8-a6b4-cac1d5facd27)

### Solving

We are given g, p and have to find d.

p = prime modulus = 991
g = 209 

``g * d % p = 1`` 

```
print(pow(209, -1, 991))
```

### Flag

> 569

---

## Generators of Groups

### Challenge

![image](https://github.com/user-attachments/assets/a4bade9f-51b4-4b3b-ae30-f62214b6a893)

### Solving

To find the smallest primitive element g we need to o find a primitive element, we need to check if an element
generates all elements of the field by confirming that the powers of g modulo p cover all non-zero elements of the field.

so we first do p-1 then find the prime factors for it.

Afterwards we know the formula for checking if g is correct if ``g^(p-1)/primefactorn`` is within the range of p. If all are then it is primitive. hence we can loop from numbers 1->N checking them against this formula. Then once we find all the primitives we can find the smallest one.

```python
def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def is_primitive(g, p):
    p_minus_1 = p - 1
    prime_factors = [2, 5, 7, 17] 

    for factor in prime_factors:
        if power_mod(g, p_minus_1 // factor, p) == 1:
            return False  
    
    return True  

def find_smallest_primitive(p):
    for g in range(2, p):
        if is_primitive(g, p):
            return g
    return None

p = 28151
g = find_smallest_primitive(p)
print(f"Smallest primitive element g = {g}")
```

### Flag

> 7

---

## Computing Public Values

### Challenge

![image](https://github.com/user-attachments/assets/9fdb8c8e-d692-429d-89d2-3705889711c5)

### Solving

To use this protocall prime P is established and some generator field g. The user then picks an integer ``a < p -1`` and calculates ``g^a mod p`` a is the secret value and when this is executed it forms A the public value

```python
g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
a = 972107443837033796245864316200458246846904598488981605856765890478853088246897345487328491037710219222038930943365848626194109830309179393018216763327572120124760140018038673999837643377590434413866611132403979547150659053897355593394492586978400044375465657296027592948349589216415363722668361328689588996541370097559090335137676411595949335857341797148926151694299575970292809805314431447043469447485957669949989090202320234337890323293401862304986599884732815
print(pow(g, a, p))
```

### Flag

> 1806857697840726523322586721820911358489420128129248078673933653533930681676181753849411715714173604352323556558783759252661061186320274214883104886050164368129191719707402291577330485499513522368289395359523901406138025022522412429238971591272160519144672389532393673832265070057319485399793101182682177465364396277424717543434017666343807276970864475830391776403957550678362368319776566025118492062196941451265638054400177248572271342548616103967411990437357924

---

## Computing Shared Secrets 

### Challenge

![image](https://github.com/user-attachments/assets/1f788f3c-ca10-40db-83be-8a936ba8a82a)

### Solving

In this challenge our friend has given her public key. We have our private key and we also have P. From this we can calculate our sharedsecret (the int we calculated last time) by doing ``A^b % p`` Btw we can also calculate our public value by doing B = ``g^b mod p`` 
we where also given g in this question not that it is needed...

```python
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
A = 70249943217595468278554541264975482909289174351516133994495821400710625291840101960595720462672604202133493023241393916394629829526272643847352371534839862030410331485087487331809285533195024369287293217083414424096866925845838641840923193480821332056735592483730921055532222505605661664236182285229504265881752580410194731633895345823963910901731715743835775619780738974844840425579683385344491015955892106904647602049559477279345982530488299847663103078045601
b = 12019233252903990344598522535774963020395770409445296724034378433497976840167805970589960962221948290951873387728102115996831454482299243226839490999713763440412177965861508773420532266484619126710566414914227560103715336696193210379850575047730388378348266180934946139100479831339835896583443691529372703954589071507717917136906770122077739814262298488662138085608736103418601750861698417340264213867753834679359191427098195887112064503104510489610448294420720
print(pow(A, b, p))
```

### Flag

> 1174130740413820656533832746034841985877302086316388380165984436672307692443711310285014138545204369495478725102882673427892104539120952393788961051992901649694063179853598311473820341215879965343136351436410522850717408445802043003164658348006577408558693502220285700893404674592567626297571222027902631157072143330043118418467094237965591198440803970726604537807146703763571606861448354607502654664700390453794493176794678917352634029713320615865940720837909466

---

## Deriving Symmetric Keys

### Challenge

![image](https://github.com/user-attachments/assets/9c9205d0-c346-40ad-bf91-cf5b45d90052)

source.py
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
from secret import shared_secret

FLAG = b'crypto{????????????????????????????}'


def encrypt_flag(shared_secret: int):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Encrypt flag
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    # Prepare data to send
    data = {}
    data['iv'] = iv.hex()
    data['encrypted_flag'] = ciphertext.hex()
    return data


print(encrypt_flag(shared_secret))
```
decrypt.py
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


shared_secret = ?
iv = ?
ciphertext = ?

print(decrypt_flag(shared_secret, iv, ciphertext))
```

### Solving

Using the decrypt script they gave us we can first calculate shared_secret hence using the format provided we can tweak it a little and solve our challenge :D

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


# Provided values
g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
A = 112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784
b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944

# Calculate the shared secret
shared_secret = pow(A, b, p)

# Provided IV and ciphertext
iv = "737561146ff8194f45290f5766ed6aba"
ciphertext = "39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c"

# Decrypt and print the flag
print(decrypt_flag(shared_secret, iv, ciphertext))
```

Running this we get the flag.

### Flag

> crypto{sh4r1ng_s3cret5_w1th_fr13nd5}

---

## **NOTES**

1. **Fields and Modular Arithmetic**: The Diffie-Hellman protocol uses fields (groups of numbers under modular arithmetic), where `g` is the generator and `p` is a prime modulus. The equation `g * d % p = 1` is used to find the modular inverse of `g` to compute shared secrets.

2. **Finding Primitive Elements**: A primitive element `g` in a field is one that generates all non-zero elements of the group. To check if `g` is primitive, we compute `g^(p-1)/factor % p` for each prime factor of `p-1` and verify that the result is not `1` to ensure it generates the entire field.

3. **Public Values and Exponentiation**: In Diffie-Hellman, users select a secret integer `a`, and compute the public value `A = g^a mod p`, where `g` is the generator and `p` is the prime modulus. This public value is shared with others, while keeping `a` secret.

4. **Computing Shared Secrets**: To compute a shared secret users use their friends public value `A` and their own secret key `b` to compute `shared_secret = A^b mod p`. This computation results in the same shared secret for both parties due to the properties of modular arithmetic.

5. **Symmetric Key Derivation**: After computing the shared secret a symmetric key for encryption (like AES) is derived using a hash function (e.g., SHA1) to generate a fixed-length key from the shared secret. This key is then used to encrypt or decrypt messages between parties.

6. **Encryption/Decryption**:  ``Key=SHA-1(shared_secret`` to create the key for encryption and decryption. 

