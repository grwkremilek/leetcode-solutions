#1221. Split a String in Balanced Strings

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
