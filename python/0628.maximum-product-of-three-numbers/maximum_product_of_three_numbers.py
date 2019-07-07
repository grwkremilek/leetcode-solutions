#https://leetcode.com/problems/maximum-product-of-three-numbers/

def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
