#https://leetcode.com/problems/permutations/


# heap' s algorithm, divide and conquer

def permute(nums):
    return self.generate(len(nums), nums, [])

def generate(size, nums, result):
    if size == 1:
        result.append(nums + [])
    else:
        generate(size-1, nums, result)
        for i in range(size - 1):
            if size % 2:
                nums[0], nums[size - 1] = nums[size - 1], nums[0]
            else:
                nums[i], nums[size - 1] = nums[size - 1], nums[i]
            generate(size-1, nums, result)
    return result
        
        
#the basic idea is to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, in every possible position.
#For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>> (let's call it "answer").
#Then, 2 can be added in front or after 1. So we have to copy the List in answer (it's just {1}), add 2 in position 0 of {1}, then copy the original {1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}. There are 2 lists in the current answer.
#Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, and add 3 into position 1, then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.
def permute(nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms
        


def permute(nums):
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
