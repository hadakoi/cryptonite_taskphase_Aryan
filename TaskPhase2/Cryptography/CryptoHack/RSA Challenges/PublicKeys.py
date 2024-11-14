# Modular exponentiation of a message with an exponent e and a modulus N which is normally a product of two primes. N = p . q

# Here number = 12, N = p x q = 17 x 23, e = 65537
number = 12
N = 17*23
e = 65537

print(pow(number, e, N))