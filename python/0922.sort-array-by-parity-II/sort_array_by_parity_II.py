#https://leetcode.com/problems/sort-array-by-parity-ii/

def sortArrayByParityII(A):
    odd, even = [], []
    for a in A:
        (odd, even)[a % 2 == 0].append(a)   # divide to odd and even numbers 
    lst = list(zip(even, odd))              # zip to a list
    return[e for l in lst for e in l]       # flatten a list of tuples
