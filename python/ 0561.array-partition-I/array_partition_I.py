#https://leetcode.com/problems/array-partition-i/

def arrayPairSum(self, nums: List[int]) -> int:
    nums = sorted(nums)
    out = [nums[i:i + 2] for i in range(0, len(nums), 2)]
    return(sum(map(lambda x: min(x), out)))

def arrayPairSum(self, nums: List[int]) -> int:
    nums = sorted(nums)
    out = zip(*[iter(nums)]*2)
    return(sum(map(lambda x: min(x), out)))

def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
