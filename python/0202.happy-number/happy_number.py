#https://leetcode.com/problems/happy-number/

def isHappy(n):        
    numbers = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in numbers:
            return False
        else:
            numbers.add(n)
    return True
