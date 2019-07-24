#https://leetcode.com/problems/reverse-integer/

def reverse(x):
    sign = cmp(x, 0)
    out = int(str(sign*x)[::-1])
    return (out < 1<<31)*out*sign


def reverse(x):
    sign = [-1,1][x>0]
    ans = sign * int(str(abs(x))[::-1])   
    return ans if -2**31<ans<2**31-1 else 0
