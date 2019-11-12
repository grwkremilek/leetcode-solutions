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


def intersection(nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1
        return res
