#https://leetcode.com/problems/number-of-1-bits/


def hammingWeight(n):
    string = "{0:b}".format(n)
    return string.count('1')


def hammingWeight(n):
    if n == 0: return 0
    count = 0
    while n != 1:
        count += n%2
        n = n // 2
    return count + n
