#https://leetcode.com/problems/first-unique-character-in-a-string/

def firstUniqChar(s):
    if len(s) > 1:
        check = ''
        for i, c in enumerate(s):
            if c not in s[i+1:] and c not in check:
                return i
            check+= c
    if len(s) == 1:
        return 0
    return -1
