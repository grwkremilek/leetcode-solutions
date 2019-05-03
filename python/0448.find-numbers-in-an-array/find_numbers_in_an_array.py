#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def findDisappearedNumbers(nums):
    if len(nums) > 0:
        new = set(list(range(1, len(nums)+1)))
        return list(new.difference(set(nums)))
    return []

