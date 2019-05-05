#https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False
	
