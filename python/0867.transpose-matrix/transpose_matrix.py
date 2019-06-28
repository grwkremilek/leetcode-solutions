#https://leetcode.com/problems/transpose-matrix/

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    #return list(zip(*A))
