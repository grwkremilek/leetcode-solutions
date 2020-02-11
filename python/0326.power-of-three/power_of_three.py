#https://leetcode.com/problems/power-of-three/

def isPowerOfThree(n):
    if n < 1: return False
    while n % 3 == 0:        	
        n = n/3
    return n == 1
    
    
def isPowerOfThree(n):
    #check if log(n, 3) is an integer
    return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10


def isPowerOfThree(n):
     return n > 0 and 1162261467 % n == 0
