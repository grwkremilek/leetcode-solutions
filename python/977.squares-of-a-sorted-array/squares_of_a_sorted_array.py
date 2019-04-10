#https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(A):
    return sorted(list(map(lambda a: a**2, A)))
