#https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    d = sorted(d.items(), key=lambda n: -n[1])
    return [n[0] for n in d[:k]]
