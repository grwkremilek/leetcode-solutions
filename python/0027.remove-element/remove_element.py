#https://leetcode.com/problems/remove-element

def removeElement(nums, val):
    try:
        while True:
            nums.remove(val)
    except:
        return len(nums)
			
			
