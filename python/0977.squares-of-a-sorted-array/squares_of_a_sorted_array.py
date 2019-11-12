#https://leetcode.com/problems/squares-of-a-sorted-array/


def sortedSquares(A):
    return sorted(list(map(lambda a: a**2, A)))


def sortedSquares(A):
        return sorted(x*x for x in A)


def sortedSquares(A):
        result = [None] * len(A)
        l, r = 0, len(A) - 1
        for i in range(len(A)-1, -1, -1):
            if abs(A[l]) > abs(A[r]):
                result[i] = A[l] ** 2
                l += 1
            else:
                result[i] = A[r] ** 2
                r -= 1
        return result
