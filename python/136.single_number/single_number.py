#https://leetcode.com/problems/single-number/

def singleNumber(nums):
    s_nums = sorted(nums)
    for i,j in zip(s_nums[0::2], s_nums[1::2]):
        if i != j:
            return i
    return s_nums[-1]
