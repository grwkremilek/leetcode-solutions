#https://leetcode.com/problems/sqrtx/


def mySqrt(x):
    result = ''
    x_string = str(x)
    if len(x_string)% 2 != 0:
        x = '0' + x_string
        x = int(x)
    #solve A:
    a = 0
    while True:
        if a**2 > (int(x_string)/100):
            a -= 1
            break
        a += 1
    result += str(a)
    #solve B:
    b = 1
    while True:
        if b * ((20 * a) + b) > x - ((10*a)**2):
            b-= 1
            break
        b += 1
    result += str(b)
    return int(result)


#divide and conquer

def mySqrt(x):
    l,r = 1, x
    while l<=r:
        mid = l+int((r-l)/2)
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            r = mid-1
        else:
            l = mid+1
    return l-1
    
    
#Newton

def mySqrt(x):
    if x > 0:
        a = float(x)
        for i in range(100):
            x = 0.5 * (x + a / x)
    return int(x)



def mySqrt(x):
    if x == 0 : return 0
    if x < 4: return 1
    n = x // 2 
    left = 1
    right = n
    while left <= right:
        mid = (left + right)//2
        res = mid * mid
        if res == x:
            return mid
        elif res < x:    
            left = mid + 1
        else: 
            right = mid -1
    return right
