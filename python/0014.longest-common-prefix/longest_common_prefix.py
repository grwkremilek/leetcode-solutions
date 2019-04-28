#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if strs:
        sorted_l = sorted(strs, key=len)
        pref = sorted_l[0]
        for word in sorted_l[1:]:
            for i, c in enumerate(word[:len(pref)]):
                if c == pref[i]:
                    continue
                else:
                    pref = pref[:i]
                    break
        return pref
    return ""
    

def longestCommonPrefix(strs):
    prefix = strs[0] if strs else ''
    while True:
        if all(s.startswith(prefix) for s in strs):
            return prefix
        prefix = prefix[:-1]
