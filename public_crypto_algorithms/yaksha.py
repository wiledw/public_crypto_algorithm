def rsa_parameters_verbose(p, q, d_aa, d_ay, C_A):
    """
    Calculate RSA parameters and the session key with verbose print statements.
    
    Arguments:
    p -- Prime number 1 for RSA
    q -- Prime number 2 for RSA
    d_aa, d_ay -- Components of Alice's private key
    C_A -- Encrypted session key sent by Yaksha server
    """
    print(f"Given prime numbers: p = {p}, q = {q}")
    print(f"Components of Alice's private key: d_aa = {d_aa}, d_ay = {d_ay}")
    print(f"Encrypted session key sent by Yaksha server: C_A = {C_A}")

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print(f"Calculated RSA modulus n = {n} and Euler's totient function phi(n) = {phi_n}")

    # Calculate d (private key component)
    d = d_aa * d_ay
    print(f"Calculated private key component d = {d}")

    # Finding the public key component e
    e = None
    for i in range(2, phi_n):
        if (i * d) % phi_n == 1:
            e = i
            break
    print(f"Calculated public key component e = {e}")

    # Calculating the session key
    # k_session = pow(C_A, d, n)
    k_session = pow(C_A, d_aa, n)
    print(f"Decrypted session key k_session = {k_session}")

    return n, phi_n, d, e, k_session

# Given values
p = 997
q = 97
d_aa = 49
d_ay = 29
C_A = 62680

# Solving the problem with verbose output
rsa_parameters_verbose(p, q, d_aa, d_ay, C_A)
