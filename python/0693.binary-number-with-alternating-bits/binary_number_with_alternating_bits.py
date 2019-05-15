#https://leetcode.com/problems/binary-number-with-alternating-bits/

def hasAlternatingBits(n):
    s = bin(n)
    return '00' not in s and '11' not in s
	
