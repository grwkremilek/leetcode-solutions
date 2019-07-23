#https://leetcode.com/problems/subsets/


def subsets(nums):
    subsets = []
    for n in range(len(nums)+1):
        for subset in itertools.combinations(nums, n):
            subsets.append(subset)
    return subsets


def subsets(nums):
    L = []
    n = len(nums)
    size = 1 << n
    for i in range(size):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(nums[j])
        L.append(sub)
    return L
