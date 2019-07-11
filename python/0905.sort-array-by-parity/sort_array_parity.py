
def sortArrayByParity(A):
    evens = []
    odds = []
    for a in A:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
    return evens + odds


def sortArrayByParity(A):
    odd, even = [], []
    for a in A:
        (odd, even)[a % 2 == 0].append(a) 
    return even+odd


def sortArrayByParity(A):
    A.sort(key = lambda x: x % 2)
    return A


def sortArrayByParity(A):
    sorted_A = []
    for a in A:
        if a % 2 == 0:
            sorted_A = [a] + sorted_A
        else:
            sorted_A.append(a)
    return sorted_A
    

def sortArrayByParity(A):
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]
        if A[i] % 2 == 0: i += 1
        if A[j] % 2 == 1: j -= 1
    return A
