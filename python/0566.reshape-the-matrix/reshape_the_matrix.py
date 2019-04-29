#https://leetcode.com/problems/reshape-the-matrix/

def matrixReshape(nums, r, c):
    if len(nums) * len(nums[0]) != r*c:
        return nums
    flat = [item for sublist in nums for item in sublist]
    return [flat[x:x+c] for x in range(0, len(flat), c)]
	
