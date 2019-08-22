#https://leetcode.com/problems/plus-one/


def plusOne(digits):
    integer = ''.join(map(str, digits))
    return list(map(int, str(int(integer) +1)))


def plusOne(digits):
    digits.reverse()
    remainder = True
    for i in range(len(digits)):
        if remainder:
            digits[i] += 1
            remainder = False
        if digits[i] > 9:
            digits[i] = 0
            remainder = True
        else:
            break
    if remainder:
        digits.append(1)
    digits.reverse()
    return digits


def plusOne(digits):
    integer = ''.join(map(str, digits))
    return list(map(int, str(int(integer) +1)))


def plusOne(digits):
    digits.reverse()
    remainder = True
    for i in range(len(digits)):
        if remainder:
            digits[i] += 1
            remainder = False
        if digits[i] > 9:
            digits[i] = 0
            remainder = True
        else:
            break
    if remainder:
        digits.append(1)
    digits.reverse()
    return digits
