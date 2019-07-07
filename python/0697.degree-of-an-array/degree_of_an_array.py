#https://leetcode.com/problems/degree-of-an-array/

def findShortestSubArray(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    keys = [k for k,v in d.items() if v == max(d.values())]
    outs = []
    for key in keys:
        outs.append(len(nums[nums.index(key):len(nums) - nums[::-1].index(key)]))
    return min(outs)
