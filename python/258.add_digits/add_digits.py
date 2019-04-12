#https://leetcode.com/problems/add-digits/

def addDigits(num):
    return (num-1) % 9 + 1 if num > 0 else 0


