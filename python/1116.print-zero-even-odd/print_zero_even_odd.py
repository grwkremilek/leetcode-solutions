#https://leetcode.com/problems/print-zero-even-odd/

import threading

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n                              # 2n length divided to 3 loops
        self.count = 0
        
        self.lock_zero = threading.Lock()
        self.lock_odd = threading.Lock()
        self.lock_even = threading.Lock()
        
        self.lock_odd.acquire()
        self.lock_even.acquire()
        
    def zero(self, printNumber):
        for i in range(self.n):                 # print 0 n-times
            self.lock_zero.acquire()
            printNumber(0)
            self.count += 1
            if i % 2 == 0:
                self.lock_odd.release()
            else:
                self.lock_even.release()
        
    def even(self, printNumber):
        for _ in range(self.n//2):              # print even numbers n//2-times
            self.lock_even.acquire()
            printNumber(self.count)
            self.lock_zero.release()
        
    def odd(self, printNumber):
        for _ in range((self.n+1)//2):          # print odd numbers n//2-times
            self.lock_odd.acquire()
            printNumber(self.count)
            self.lock_zero.release()
