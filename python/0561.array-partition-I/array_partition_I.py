#https://leetcode.com/problems/array-partition-i/

def arrayPairSum(nums):
    nums = sorted(nums)
    out = [nums[i:i + 2] for i in range(0, len(nums), 2)]
    return(sum(map(lambda x: min(x), out)))

def arrayPairSum(nums):
    nums = sorted(nums)
    out = zip(*[iter(nums)]*2)
    return(sum(map(lambda x: min(x), out)))

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])
