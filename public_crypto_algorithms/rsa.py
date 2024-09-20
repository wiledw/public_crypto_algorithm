import math

# Generate public key (e, n) using two large prime numbers p and q
def rsa_generate_Kpub(p, q):
    n = p*q
    print("n =", n)
    
    phi = (p-1)*(q-1)
    
    e = 2
    while(e<phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1
    print("e =", e)
    
    return e, n

# Generate private key using public key (e, n)
def rsa_generate_Kpriv(e, p, q):
    phi = (p-1)*(q-1)
    
    l = []
    tmp = 1
    while len(l) <= 5:
        if (tmp *e) % phi == 1:
            l.append(tmp)
        tmp += 1

    print("5 possible d values: ", l)
    return l

# Encrypt message m using public key (e, n)
def rsa_encrypt(m, e, n):
    C = (m**e) % n
    print(f'Encrypted message: {C}')
    return C
    
# Decrypt ciphertext C using private key d, and n
def rsa_decrypt(c, d, n):
    M = (c**d) % n
    print(f'Decrypted message: {M}')
    return M


# Example
p = 181
q = 1451

n = p*q # n = pq -> ALWAYS

e = 154993 # public key
d = 95857 # private key

msg = 152015
print(f'original message: {msg}')

C = rsa_encrypt(msg, e, n); # Get ciphertext C
M = rsa_decrypt(C, d, n); # Get decrypted message M

# privateKey = rsa_generate_Kpriv(e,p,q);