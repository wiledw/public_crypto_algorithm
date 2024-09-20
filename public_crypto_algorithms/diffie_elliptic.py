import math
prime = 2503 # p
a = 4
b = 14

def elliptic_curve_addition(P: list, Q: list):
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]

    if x1 == x2 and y1 == y2:
        m = (3 * (x1**2) + a) * pow(2 * y1, -1, prime) % prime
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, prime) % prime
        
    newx = (m**2 - x1 - x2) % prime
    newy = (m * (x1 - newx) - y1) % prime

    return [newx, newy]

def elliptic_curve_multiplication(point: list, k: int):
    Q = point

    index = 2
    while True:
        Q =  elliptic_curve_addition(Q, point)
        if index == k:
            break
        index += 1
    return Q

def elliptic_getKpub(Kpriv): 
    Q = elliptic_curve_multiplication(P_init, Kpriv)
    print("Q: ", Q)
    return Q

def elliptic_getShared(public, private):
    Q = elliptic_curve_multiplication(public, private)
    print("Q: ", Q)
    return Q



#--------------------------------------------------------------------
# Example from slides
P_init = [1002, 493] # initial point on curve
KprivA = 1379
KprivB = 2011
k = 717

pubA = elliptic_getKpub(KprivA)
pubB = elliptic_getKpub(KprivB)

SharedKey = elliptic_getShared(pubA, KprivB)
SharedKey = elliptic_getShared(pubB, KprivA)
