#brute force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


#two-pass with a hash table
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        d[nums[i]]=i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d and complement != i:
            return [i, d[complement]]


#single-pass with a hash table
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] not in d:
            d[nums[i]]=i
        else:
            return [d[target-nums[i]],i]
