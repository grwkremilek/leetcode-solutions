#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from collections import OrderedDict

def removeDuplicates(nums):
    nums[:] =  OrderedDict.fromkeys(nums).keys()
    return len(nums)
		
	
