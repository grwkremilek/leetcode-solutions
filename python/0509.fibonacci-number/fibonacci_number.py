#https://leetcode.com/problems/fibonacci-number/
#https://leetcode.com/problems/fibonacci-number/discuss/308688/6-Python-solutions


def fib(N):
    if N > 1:
        return self.fib(N-1) + self.fib(N-2)
    elif N == 1:
        return 1
    return 0

def fib(N):
    a,b = 0,1
    for _ in range(N):
        a, b = b, a+b
    return a

def fib(N):
    g = (1 + 5 ** 0.5) / 2
    return int((g ** N + 1) / 5 ** 0.5)
