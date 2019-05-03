#https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):

    def helper(i, j):
        while i >=0 and j < len(s) and s[i]==s[j]:
            i -= 1
            j += 1
        return s[i+1:j]  # s[i] != s[j]

    return s and max((a for i in range(len(s)) 
                  for a in (helper(i, i), helper(i, i+1))), key=len) or ''
