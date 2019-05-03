#https://leetcode.com/problems/minimum-index-sum-of-two-lists/

def findRestaurant(list1, list2):
    out = []
    d = {}
    for i, name in enumerate(list1):
        if name in list2:
            d[name] = i + list2.index(name)
    return [k for k, v in d.items() if v == min(d.values())]
