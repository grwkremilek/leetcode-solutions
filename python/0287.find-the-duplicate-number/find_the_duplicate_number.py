#https://leetcode.com/problemset/all/


def findDuplicate(nums):
    seen = []
    for n in nums:
        if n in seen:
            return n
        seen.append(n)


def findDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)


def findDuplicate(nums):
    slow, fast, finder = nums[0], nums[nums[0]], 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    while slow != finder:
        slow = nums[slow]
        finder = nums[finder]
    return finder
