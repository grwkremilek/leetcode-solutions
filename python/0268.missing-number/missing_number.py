#https://leetcode.com/problems/missing-number/

def missingNumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)
