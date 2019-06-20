#https://leetcode.com/problems/height-checker

def heightChecker(heights):
    sort_heights = sorted(heights)
    count = 0
    for n1, n2 in zip(heights, sort_heights):
        if n1 != n2:
            count += 1
    return count
