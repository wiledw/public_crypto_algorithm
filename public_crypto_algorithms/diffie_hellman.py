# numbers chosen by Alice and Bob
p = 107 # prime number
g = 41 # integer, cannot be 0, 1, or p - 1

# private keys
Kalice_priv = 13 # alice's private key
Kbob_priv = 77 # bob's private key

def alice_pubkey():
    Kalice_pub = (g**Kalice_priv) % p
    print("Alice public key: ", Kalice_pub)
    return Kalice_pub

def bob_pubkey():
    Kbob_pub = (g**Kbob_priv) % p
    print("Bob public key: ", Kbob_pub)
    return Kbob_pub

# Shared key used in symmetric key encryption algorithm
# Produces same result as bob_sharedkey()
def alice_sharedkey(Kbob_pub):
    Kshared = (Kbob_pub**Kalice_priv) % p
    print("Alice shared key: ", Kshared)
    return Kshared

# Shared key used in symmetric key encryption algorithm
# Produces same result as alice_sharedkey()
def bob_sharedkey(Kalice_pub):
    Kshared = (Kalice_pub**Kbob_priv) % p
    print("Bob shared key: ", Kshared)
    return Kshared

# Example
Kalice_pub = alice_pubkey()
Kbob_pub = bob_pubkey()
alice_sharedkey(Kbob_pub)
bob_sharedkey(Kalice_pub)