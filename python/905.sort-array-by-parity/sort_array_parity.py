#brute force
def sortArrayByParity(A):
    evens = []
    odds = []
    for a in A:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
    return evens + odds


#very slow solution
def sortArrayByParity(A):
    sorted_A = []
    for a in A:
        if a % 2 == 0:
            sorted_A = [a] + sorted_A
        else:
            sorted_A.append(a)
    return sorted_A
