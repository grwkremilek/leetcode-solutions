#https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    d = {}
    for s in strs:
        sort_s = ''.join(sorted(s))
        if sort_s in d:
            d[sort_s].append(s)
        else:
            d[sort_s] = [s]
    return [v for k,v in d.items()]
