#https://leetcode.com/problems/reverse-string/

def reverseString(s):
        s.reverse()


def reverseString(s):
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i +=1
        j -=1
        

def reverseString(s):
    s[:] = s[::-1]
