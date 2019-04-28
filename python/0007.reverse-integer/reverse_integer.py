#https://leetcode.com/problems/reverse-integer/

def reverse(x):
    sign = cmp(x, 0)
    out = int(str(sign*x)[::-1])
    return (out < 1<<31)*out*sign
		
