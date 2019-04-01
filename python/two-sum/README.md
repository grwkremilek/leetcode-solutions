# Two sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].



## comments

* brute force (looping through each array once)

    time complexity:  O(n2)		: double array traversal
	
    space complexity:  O(1)



* double-pass with a hash table (trading time for space complexity)

    time complexity: O(n)		: double array traversal, but lookup in the table reduces time to O(1)

    space complexity: O(n)		: hash table stores max N elements

	
	
* single-pass with a hash table

    time complexity: O(n)

    space complexity: O(n)



#### Runtime: 44 ms (68.58%)
