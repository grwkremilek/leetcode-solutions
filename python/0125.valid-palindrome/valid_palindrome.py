#https://leetcode.com/problems/valid-palindrome/

import string

def isPalindrome(s):
    clean = ""
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator)
    s = s.replace(" ", "")
    for c in s.lower():
            clean += c
    return clean == clean[::-1]
