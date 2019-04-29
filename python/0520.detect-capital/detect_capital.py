#https://leetcode.com/problems/detect-capital/
 
def detectCapitalUse(word):
    if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
        return True
    return False
