#https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balancedStringSplit(s):
        countL = 0
        countR = 0
        out = 0
        for i in s:
            if i == 'L':
                countL += 1
            else:
                countR += 1
            if countR == countL:
                out += 1
        return out
