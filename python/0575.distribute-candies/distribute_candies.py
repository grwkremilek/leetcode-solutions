#https://leetcode.com/problems/distribute-candies/

def distributeCandies(candies):
    d = {}
    for candy in candies:
        if candy not in d:
            d[candy] = 1
        else:
            d[candy] += 1
    if len(d) <= len(candies)//2:
        return len(d)
    return len(candies)//2

