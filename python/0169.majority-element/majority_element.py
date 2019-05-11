#https://leetcode.com/problems/majority-element/

def majorityElement(snums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    return max(d.items(), key=operator.itemgetter(1))[0]
