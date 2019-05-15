#https://leetcode.com/problems/letter-case-permutation/

def letterCasePermutation(S):
    L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
    return [''.join(i) for i in itertools.product(*L)]
    
