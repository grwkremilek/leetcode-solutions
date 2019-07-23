#https://leetcode.com/problems/house-robber/

def rob(nums):
    last, cur = 0, 0
    for n in nums: 
        last, cur = cur, max(last + n, cur)       
    return cur
