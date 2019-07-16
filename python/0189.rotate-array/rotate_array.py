#https://leetcode.com/problems/rotate-array/


def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k] 


def rotate(nums, k):
    k = len(nums) - k
    nums[:] = nums[k:] + nums[:k]
