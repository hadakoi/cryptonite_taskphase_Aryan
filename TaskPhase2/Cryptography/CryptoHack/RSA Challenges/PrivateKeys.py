# d is used to decrypt ciphertexts created with the corresponding public key 

# pow = (base, exp, mod)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

phi_N = (p - 1) * (q - 1)

d = pow(e, -1, phi_N)

print(d)
