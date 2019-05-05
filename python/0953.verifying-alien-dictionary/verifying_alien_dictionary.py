#https://leetcode.com/problems/verifying-an-alien-dictionary/

def isAlienSorted(words, order):
    return words == sorted(words, key=lambda w: list(map(order.index, w)))
