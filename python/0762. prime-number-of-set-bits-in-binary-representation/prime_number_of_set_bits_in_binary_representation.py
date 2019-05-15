#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

def countPrimeSetBits(L, R):
    primes = {2, 3, 5, 7, 11, 13, 17, 19}  
    out = 0
    for i in range(L, R+1):
        counts = bin(i).count('1')
        if counts in primes:
            out +=1
    return out
