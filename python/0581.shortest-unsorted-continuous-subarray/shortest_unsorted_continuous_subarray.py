#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/


def findUnsortedSubarray(nums):
    ans = [i for (i, (n1, n2)) in enumerate(zip(nums, sorted(nums))) if n1 != n2]
    return 0 if not ans else ans[-1] - ans[0] + 1


def findUnsortedSubarray(nums):
    m = nums[0]
    end = 0
    for i in range(1, len(nums)):
        if nums[i] >= m:
            m = nums[i]
        else:
            end = i
    m = nums[-1]
    start = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] <= m:
            m = nums[i]
        else:
            start = i
    return 0 if start == end else max(end-start+1, 0)
