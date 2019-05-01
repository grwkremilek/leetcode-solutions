#https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort(key = lambda x: 1 if x == 0 else 0)
    #nums.sort(key=bool, reverse=True)
