#https://leetcode.com/problems/intersection-of-two-arrays-ii/

def intersect(nums1, nums2):
    d = {}; out = []
    for n in nums1:
        d[n] = d.get(n, 0) + 1
    for n in nums2:
        if n in d and d[n] > 0:
            out.append(n)
            d[n] -= 1
    return out


