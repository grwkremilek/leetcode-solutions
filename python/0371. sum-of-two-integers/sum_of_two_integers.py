#https://leetcode.com/problems/sum-of-two-integers/

def getSum(a, b):
    MAX = 0x7FFFFFFF        # 32 bits integer max
    mask = 0xFFFFFFFF       # mask to get last 32 bits
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask    # ^ get different bits and & gets double 1s, << moves carry
    return a if a <= MAX else ~(a ^ mask)
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
