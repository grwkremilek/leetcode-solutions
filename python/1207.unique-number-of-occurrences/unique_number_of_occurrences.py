#https://leetcode.com/problems/unique-number-of-occurrences/


def uniqueOccurrences(arr):
    d = {}
    for a in arr:
        d[a] = d.get(a, 0) + 1
    return len(list(d.values())) == len(set(list(d.values())))
