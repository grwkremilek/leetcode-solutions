#https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    out = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            out -= roman[s[i]]
        else:
            out += roman[s[i]]
    return out + roman[s[-1]]



def romanToInt(s):
    d = { 'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9, 'X' : 10, 'XL' : 40,
         'L' : 50, 'XC' : 90, 'C' : 100, 'CD' : 400, 'D' : 500, 
         'CM' : 900, 'M' : 1000 }
    
    i = len(s)-1
    integers = 0
    while i >= 0:
        if s[i-1:i+1] in d:
            integers += d[s[i-1:i+1]]
            i -= 2
            continue
        else:
            integers += d[s[i]]
            i -=1
    return integers



def romanToInt(s):
    integers = 0 
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(s)): 
        if i != len(s) - 1 and d[s[i]] < d[s[i+1]]:
            integers -= d[s[i]]
        else:
            integers += d[s[i]]
    return integers
