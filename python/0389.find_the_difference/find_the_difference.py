#https://leetcode.com/problems/find-the-difference/

def findTheDifference(s, t):
    s = sorted(s); t = sorted(t)
    for index, (i,j) in enumerate(zip(s,t)):
        if i != j:
            return j if t[index+1] == i else i
    return t[-1]
