#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(numbers,target):
    l, r = 0, len(numbers)-1
    while l < r:
        res = numbers[l] + numbers[r]
        if res == target:
            return [l+1,r+1]
        elif res < target:
            l += 1
        else:
            r -= 1


def twoSum(numbers, target):
    d = {}
    for i in range(len(numbers)):
        if target - numbers[i] in d:
            return [d[target-numbers[i]]+1, i+1]
        d[numbers[i]] = i
