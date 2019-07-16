#https://leetcode.com/problems/single-number/

def singleNumber(nums):
    s_nums = sorted(nums)
    for i,j in zip(s_nums[0::2], s_nums[1::2]):
        if i != j:
            return i
    return s_nums[-1]


def singleNumber(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n , 0) + 1
    return list(d.keys())[list(d.values()).index(1)]


def singleNumber(nums):  
    ans = []
    for n in nums:
        ans.remove(n) if n in ans else ans.append(n)
    return ans[0]


def singleNumber(nums):  
    d = {}
    for i in nums:
        try:
            d.pop(i)
        except:
            d[i] = 1
    return d.popitem()[0]
    

def singleNumber(nums):  
    xor = nums[0]
    for i in range(1, len(nums)):
        xor ^= nums[i]
    return xor
