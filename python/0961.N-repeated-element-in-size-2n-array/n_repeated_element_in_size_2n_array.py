#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

def repeatedNTimes(A):
    d = {}
    n = len(A)//2
    for a in A:
        d[a] = d.get(a, 0) + 1
    for key, value in d.items():
        if value == n:
            return key

def repeatedNTimes(A):
    while 1:
        s = random.sample(A, 2)
        if s[0] == s[1]:
            return s[0]

def repeatedNTimes(A):
    return int((sum(A)-sum(set(A))) // (len(A)//2-1))
