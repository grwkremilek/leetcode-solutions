#https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
    d = {}
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in d[:k]]
