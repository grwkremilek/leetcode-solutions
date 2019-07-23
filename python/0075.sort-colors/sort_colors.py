#https://leetcode.com/problems/sort-colors/


def sortColors(nums):
    nums.sort()


# BUBBLE SORT
def sortColors(nums):
    n = len(nums) 
    for i in range(n): 
        for j in range(0, n-i-1):  
            if nums[j] > nums[j+1]: 
                nums[j], nums[j+1] = nums[j+1], nums[j]


# RECURSIVE BUBBLE SORT
def sortColors(nums):
    for i, num in enumerate(nums): 
        try: 
            if nums[i+1] < num: 
                nums[i] = nums[i+1] 
                nums[i+1] = num 
                self.sortColors(nums)
        except IndexError:
            pass


# INSERION SORT
def sortColors(nums):
    for i in range(1, len(nums)): 
        key = nums[i] 
        j = i-1
        while j >= 0 and key < nums[j] : 
            nums[j + 1] = nums[j] 
            j -= 1
        nums[j + 1] = key 
     

# 2 pointer solutions
def sortColors(nums):
    pointer1 = 0
    pointer2 = 0
    while pointer1 != len(nums):
        if nums[pointer2]==0:
            nums.insert(0,nums.pop(pointer2))
            pointer2 += 1
        elif nums[pointer2]==2:
            nums.append(nums.pop(pointer2))
        else:
            pointer2 += 1
        pointer1 += 1


def sortColors(nums):
    left = 0
    right = len(nums) - 1
    current = 0
    while current <= right:
        if nums[current] == 0:
            nums[current], nums[left] = nums[left], nums[current]
            left += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
            current -= 1
        current += 1
 
