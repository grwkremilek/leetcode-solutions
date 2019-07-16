#https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    values = d.values()
    return sum(v & ~1 for v in values) + any(v & 1 for v in values)


def longestPalindrome(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    odds = sum(v & 1 for v in d.values())
    return len(s) - odds + bool(odds)
