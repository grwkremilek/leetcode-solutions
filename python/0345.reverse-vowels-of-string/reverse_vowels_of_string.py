#https://leetcode.com/problems/reverse-vowels-of-a-string/


def reverseVowels(s):
    s = list(s)
    vowels = 'aeiouAEIOU'
    l, r = 0,  len(s)-1
    while l < r:
        while s[l] not in vowels and l<r:
            l += 1
        while s[r] not in vowels and l<r:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1
    return ''.join(s)
