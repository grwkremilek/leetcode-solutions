#https://leetcode.com/problems/number-complement/

def findComplement(num):
    lst = list(format(num, "b")) 
    swap = ['1' if l == '0' else '0' for l in lst]
    b =''.join(swap)
    return int(b, 2)
       
