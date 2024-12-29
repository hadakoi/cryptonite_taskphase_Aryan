# SRA

## Method

```
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...
Connect to the program on our server: nc saturn.picoctf.net 62923
```
File Provided: 
```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pride = "".join(choice(ascii_letters + digits) for _ in range(16))
gluttony = getPrime(128)
greed = getPrime(128)
lust = gluttony * greed
sloth = 65537
envy = inverse(sloth, (gluttony - 1) * (greed - 1))
anger = pow(bytes_to_long(pride.encode()), sloth, lust)

print(f"{anger = }")
print(f"{envy = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pride:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")
```

This seems to be similar to an RSA script where ``Lust = N = p*q``, Sloth is our ``e`` , Envy is our private key.

Anger seems to be our encrypted key of the form **pride^sloth % Lust**

We then get to print Anger and Envy which means it gives us our Cipher text and the Private Key.

Now from here we get to enter in a Input saved to vainglory which is then compared to our original string. If its the same we then get to open the file ``flag.txt``.

Ok so essentially we want to reverse this RSA encryption this can be done through this formula ``decrypted_message = pow(anger, envy, lust)``
Which is essentially **anger^envy % lust** and the code literally gives us anger and envy. From here ``decrypted_bytes = long_to_bytes(decrypted_message)`` and then ``decrypted_message = decrypted_bytes.decode()``

Now the only thing we are missing is the calculation for lust.

Now to make it easier for my self to understand 


``pride`` = plaintext
``gluttony`` = p
``greed`` = q
``Lust`` = n = p*q
``sloth`` = e = 65537
``envy`` = private key = d
``anger``= cipher text

Now from this We know that ``d = e^(-1) (mod φ(n))`` Now we can get this rearranged like this

```
# Rearrange some modular arithmetic
d = e^(-1) (mod φ(n))
ed = 1 (mod φ(n))
ed - 1 = 0 (mod φ(n))

# The `mod φ(n)` essentially means get the remainder dividing by φ(n)
# Thus, if the remainder is 0, `ed - 1` is a multiple of φ(n)
ed - 1 = φ(n) * k, where k is an integer

ed - 1 = (p - 1) * (q - 1) * k
```
Over here (p-1)(q-1) are unknown divisors which we need to figure out.
To do this we first find the prime factors of phi(n) which in this case is **ed-1**. Now these divisors will not directly give us p-1 and q-1 but rather they are potential factors for forming them because these are not prime numbers as p and q are. hence subtracting 1 almost always makes them divisible by other numbers. Once we have all of the divisors now from here we we use combinations to make combinations of all the divisors that can be multiplied together in whatever combination, hence we have to bruteforce this.

Steps to solve.
1. Now from this we can easily calculate a value for *ed - 1* with values given. 
2. Now we will then know that p-1, q-1, k are all factors of this ed. 
3. Now once we have the value of **ed-1** we find all the possible prime factors using a factor checker.  
4. We then get all possible subsets of the provided divisors. Each subset could represent p-1 or q-1
5. We then calculate the product of the subset, checks if its 128 bit and adds 1 to the product checking if it is prime.
6. We can then test all the prime pairs that satisified the last condition and it will print a plaintext message if it was successfull.

Starting challenge we get this.

```python
from itertools import combinations
from sympy import isprime
from Crypto.Util.number import long_to_bytes

ciphertext = int(input("Enter the ciphertext: "))
d = int(input("Enter the decryption key (d): "))

e = 65537

priv = d * e - 1
print("Provide the divisors of", priv)
factors = eval(input())

# Generate all subsets of the divisors
combos = []
for i in range(1, len(factors) + 1):
  combos += [list(j) for j in combinations(factors, i)]

primes = set()

for subset in combos:
    product = 1
    for k in subset:
        product *= k
    # Check if (p-1) is valid and (p-1) + 1 is a prime number
    if product.bit_length() == 128 and isprime(product + 1):
        primes.add(product + 1)

primelist = list(primes)

for p in primelist:
    for q in primelist:
        if p == q:
            continue
        n = p * q
        plain = pow(ciphertext, d, n)
        try:
            plaintext = long_to_bytes(plain).decode()
            print("Decoded plaintext:", plaintext)
        except Exception:
            continue
```

To find the possible divisors of the private key that are prime I used [Prime Factor Decomposition](https://www.dcode.fr/prime-factors-decomposition)

outPut from running the python file.
```
Enter the ciphertext: 30913208883090281692469301846906434564024235968267517573917245910606479980849
Enter the decryption key (d): 23113614010824248490241696406313804395271119028515797336091608198190513682401
Provide the divisors of 1514796921427388773304970057380587798652883327771839810015435726484811695203514336
2, 2, 2, 2, 2, 3, 3, 3, 11, 43, 43, 199, 1117, 11231699, 12239671, 54694015195892553427, 51576256624946381086258639643148019
Decoded plaintext: hnUPHXfcqxkCy1o6
```

```shell
anger = 30913208883090281692469301846906434564024235968267517573917245910606479980849
envy = 23113614010824248490241696406313804395271119028515797336091608198190513682401
vainglory?
> hnUPHXfcqxkCy1o6
hnUPHXfcqxkCy1o6
Conquered!
picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}
```


## Flag

> picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}