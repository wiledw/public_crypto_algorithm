# Curve is y^2 = X^3 + ax + b mod p
prime = 2503  # p
a = 4
b = 14


def elliptic_curve_addition(P: list, Q: list):
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]

    if x1 == x2 and y1 == y2:
        m = (3 * (x1 ** 2) + a) * pow(2 * y1, -1, prime) % prime
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, prime) % prime

    newx = (m ** 2 - x1 - x2) % prime
    newy = (m * (x1 - newx) - y1) % prime

    return [newx, newy]


def elliptic_curve_multiplication(point: list, k: int):
    Q = point

    index = 2
    while True:
        Q = elliptic_curve_addition(Q, point)
        if index == k:
            break
        index += 1
    return Q


###############################################################################################

# Get public key using private key
# Note: don't forget to change the curve values a, b, and p, at the top of this program
def elliptic_getKpub(Kpriv):
    Q = elliptic_curve_multiplication(P_init, Kpriv)
    print("Q: ", Q)
    return Q


# Encrypt using public key
# Note: don't forget to change the curve values a, b, and p, at the top of this program
#
# message - The message to be encrypted converted to a point on the curve
# k - random integer k
# P_init - starting point on the curve
# Q - public key
def elliptic_encrypt(message, k, P_init, Q):
    c1 = elliptic_curve_multiplication(P_init, k)
    kQ = elliptic_curve_multiplication(Q, k)
    c2 = elliptic_curve_addition(message, kQ)

    print("c1: ", c1)
    print("c2: ", c2)
    return c1, c2


# Decrypt using private key
# Note: don't forget to change the curve values a, b, and p, at the top of this program
#
# c1, c2 - the ciphertext to be decrypted
def elliptic_decrypt(Kpriv, c1, c2):
    kprivC1 = elliptic_curve_multiplication(c1, Kpriv)
    m = elliptic_curve_addition(c2, [kprivC1[0], -kprivC1[1]])

    print("decrypted message: ", m)
    return m

def shared_key(K_Alice_priv, K_Bob_priv, P_init):
    # Alice computes her part of the shared key using Bob's public key
    K_Bob = elliptic_curve_multiplication(P_init, K_Bob_priv)
    shared_key_Alice = elliptic_curve_multiplication(K_Bob, K_Alice_priv)

    # Bob computes his part of the shared key using Alice's public key
    K_Alice = elliptic_curve_multiplication(P_init, K_Alice_priv)
    shared_key_Bob = elliptic_curve_multiplication(K_Alice, K_Bob_priv)

    # The shared keys should be equal if the calculations are correct
    if shared_key_Alice != shared_key_Bob:
        print("Error: The computed shared keys do not match!")
        return None
    else:
        print("Shared key: ", shared_key_Alice)
        return shared_key_Alice


# Example from slides
P_init = [1002, 493]  # initial point on curve
Kpriv = 1379

P_init2 = [1002, 493]  # initial point on curve
BobPriv = 2011


message = [1659, 1919]
k = 717

print("original message: ", message)
Q = elliptic_getKpub(Kpriv)
Q = elliptic_getKpub(BobPriv)

print("Shared key: ", shared_key(Kpriv, BobPriv, P_init))


c1, c2 = elliptic_encrypt(message, k, P_init, Q)
m = elliptic_decrypt(Kpriv, c1, c2)


