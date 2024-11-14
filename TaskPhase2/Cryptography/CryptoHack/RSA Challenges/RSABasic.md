

# RSA  

## 1. Modular Exponentiation

At the heart of RSA is **modular exponentiation**, which raises a base number to a given power (exponent) and then takes the result modulo some number. This operation is essential in RSA, ensuring that calculations remain manageable with large numbers, which is vital for the algorithm's security.

In RSA:
- **Encryption** of a message involves exponentiating it to a public exponent and then taking it modulo a large number, \(N\).
- **Decryption** reverses this transformation by exponentiating the encrypted message to the private key \(d\), modulo \(N\).

### Example Calculation

To illustrate modular exponentiation further, let's solve the specific problem of calculating \(10^1 \mod 22663\):

```python
base = 10
exponent = 1
modulus = 22663

# Calculate modular exponentiation
result = pow(base, exponent, modulus)
print("10^1 mod 22663 =", result)  # Output: 10
```

The result is `10`, which is the answer to the modular exponentiation problem.

## 2. Public Keys and the Modulus `N`

RSA encryption uses a pair of large prime numbers (p) and (q) to compute (N):

```
N = p * q
```

The product (N) forms part of the **public key** and is used in both encryption and decryption. The other part of the public key is the **public exponent**, usually denoted (e), which is commonly set to **65537** because it allows efficient computation while maintaining security.

Together, ((N, e)) constitutes the public key, which anyone can use to encrypt messages.

## 3. Euler’s Totient Function `φ(N)`

To generate the private key (d), we use **Euler's Totient Function** (φ(N)), defined for RSA as:

```
φ(N) = (p - 1) * (q - 1)
```

This value is critical for ensuring that the encryption and decryption operations work as inverses.

## 4. Private Key `d`

The private key (d) is calculated as the **modular inverse** of (e) with respect to (φ(N)):

```
d ≡ e^(-1) mod φ(N)
```

This means that (d) is chosen so that:

```
e * d ≡ 1 mod φ(N)
```

Only with this private key (d) can we reverse the encryption operation.

## 5. Encryption Process

To encrypt a message (m) using the public key ((N, e)):
1. Convert the message (m) into an integer.
2. Compute the ciphertext (c) using:

   ```c = m^e mod N```

3. Transmit (c) as the encrypted message.

### Example
Given:
- (N = 882564595536224140639625987659416029426239230804614613279163)
- (e = 65537)
- Message (m = 12)

Encryption:

```python
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
m = 12

# Encrypt the message
c = pow(m, e, N)
print("Ciphertext:", c)
```

## 6. Decryption Process

To decrypt a ciphertext (c) using the private key (d):
1. Compute the original message (m) with:

   ```m = c^d mod N```

2. The result (m) is the decrypted plaintext.

### Example
Given:
- Ciphertext (c = 77578995801157823671636298847186723593814843845525223303932)
- (N = 882564595536224140639625987659416029426239230804614613279163)
- Previously calculated (d = 121832886702415731577073962957377780195510499965398469843281)

Decryption:

```python
c = 77578995801157823671636298847186723593814843845525223303932
d = 121832886702415731577073962957377780195510499965398469843281
N = 882564595536224140639625987659416029426239230804614613279163

# Decrypt the ciphertext
m = pow(c, d, N)
print("Decrypted message:", m)
```

The output of (m) will be the original message before encryption.

## 7. RSA Signatures

RSA digital signatures authenticate the origin and integrity of a message. The process involves:

1. **Hashing the Message**: Use a cryptographic hash function like SHA-256 to create a fixed-size hash of the message.
2. **Signing the Hash**: The sender encrypts this hash using their private key (d), generating the signature:
   [
   s = text{hash}(m)^d mod N
   ]
3. **Verifying the Signature**: The recipient decrypts the signature with the sender's public key (e). If it matches the message’s hash, the signature is valid.

### Example of RSA Signature Verification

```python
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long

message = b'example message'
# Create a hash of the message
hash = SHA256.new(data=message)

# RSA Signature creation (sender side)
signature = pow(bytes_to_long(hash.digest()), d, n)

# RSA Signature verification (recipient side)
verified_hash = pow(signature, e, n)
if verified_hash == bytes_to_long(hash.digest()):
    print("Signature verified")
else:
    print("Signature verification failed")
```

This verifies that the message has not been altered, as any change in the message would produce a different hash, causing the signature verification to fail.

---

## Summary

RSA encryption allows for secure communication by using a **public key** for encryption and a **private key** for decryption. The strength of RSA lies in the difficulty of factoring large numbers and the reversible nature of modular exponentiation when the private key is known.

- **Public Key (N, e)**: Used for encrypting messages.
- **Private Key (d)**: Used for decrypting messages, calculated using Euler’s Totient.
- **Message (m)**: Represents the original message.
- **Modulo (N)**: (p * q).
- **Totient Function**: φ(N) = (p - 1) * (q - 1).
- **Private key formula**: d ≡ e^{-1} mod φ(N).
- **Encryption Formula**: c = m^e mod N.
- **Decryption Formula**: m = c^d mod N.
