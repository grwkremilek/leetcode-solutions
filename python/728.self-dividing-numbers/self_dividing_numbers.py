#https://leetcode.com/problems/self-dividing-numbers/

def selfDividingNumbers(left, right):
    candidates = []
    for number in range(left, right+1):
        candidate = True
        for n in str(number):
            if n == '0' or number%int(n) != 0:
                candidate = False
                break
        if candidate:
            candidates.append(number)
    return candidates
