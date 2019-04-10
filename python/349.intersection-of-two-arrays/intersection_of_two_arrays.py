#https://leetcode.com/problems/intersection-of-two-arrays/

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []; d = {}
        for i in nums1:
            d[i] = d[i]+1 if i in d else 1
        for j in nums2:
            if j in d and d[j] > 0:
                res.append(j)
                d[j] = 0
        return res
