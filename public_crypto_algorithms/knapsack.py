import math

# Python3 program to calculate 
# Euler's Totient Function
# https://www.geeksforgeeks.org/eulers-totient-function/
def phi(n):
     
    # Initialize result as n
    result = n; 
 
    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2; 
    while(p * p <= n):
         
        # Check if p is a 
        # prime factor.
        if (n % p == 0): 
             
            # If yes, then 
            # update n and result
            while (n % p == 0):
                n = int(n / p);
            result -= int(result / p);
        p += 1;
 
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most 
    # one such prime factor)
    if (n > 1):
        result -= int(result / n);
    return result;

# Finds public key Kpub given private key Kpriv
# Note: n and m are secret numbers, will be generated according to the rules if not provided
def knapsack_getKpub(Kpriv, n=None, m=None):
    if n is None and m is None:
        m = sum(Kpriv) + 1 # m should be greater than sum of all numbers in private key
        while True:
            for i in range(2, m): # n and m should have no common factors
                if math.gcd(i, m) == 1:
                    n = i
                    break
            if n is not None:
                break
            m = m + 1
    elif m is None:
        m = sum(Kpriv) + 1 # m should be greater than sum of all numbers in private key
        while True: # n and m should have no common factors
            if math.gcd(n, m) == 1: 
                break
            m = m + 1
    elif n is None:
        n = 2
        while True:
            if math.gcd(n, m) == 1:
                break
            else:
                n += 1
    
    Kpub = [(k*n % m) for k in Kpriv] # Kpub[i] = (Kpriv[i] * n) mod m
    
    print("Kpriv: ", Kpriv)
    print("m: ", m)
    print("n: ", n)
    print("Kpub: ", Kpub)
    return Kpub
    
# Finds the private key Kpriv given public key Kpub
def knapsack_getKpriv(Kpub, n, m):
    Kpriv = [(((n**(phi(m)-1) % m) * k) % m) for k in Kpub] # Kpriv[i] = ((n**(phi(m)-1) mod m) * Kpub[i]) mod m)
    print("Kpriv: ", Kpriv)
    return Kpriv

# Encrypt message with public key
# Note: message should be a list of binary number strings
def knapsack_encrypt(Kpub, MsgList):
    cipherText = []
    for msg in MsgList:
        c = sum(map(lambda b,k : int(b)*k, msg, Kpub))
        cipherText.append(c)
    
    print("Ciphertext: ", cipherText)
    return cipherText

# Decrypt cipherText with private key
def knapsack_decrypt(Kpriv, cipherText, n, m):
    MsgList = []
    
    for c in cipherText:
        S = (c * (n**(phi(m)-1) % m)) % m 
        
        # Find S = b0*Kpriv[0] + b1*Kpriv[1] ... bn*Kpriv[n], where b0,b1,...,bn are either 0 or 1
        sum = 0
        msg = ""
        for k in reversed(Kpriv):
            if sum + k <= S:
                sum += k
                msg = "1" + msg
            else:
                msg = "0" + msg
        MsgList.append(msg)
    
    print("Message: ", MsgList)
    return MsgList


# Example usage    
# knapsack_getKpub(Kpriv=[1, 5, 9, 17, 39, 73], n=47, m=151)
knapsack_getKpriv(Kpub=[159, 98,143, 5, 124, 12], n=53, m=167)
# knapsack_encrypt(Kpub=[62, 93, 81, 88, 102, 37], MsgList=["011000", "110101"])
# knapsack_decrypt(Kpriv=[2, 3, 6, 13, 27, 52], cipherText=[174, 280], n=31, m=105)