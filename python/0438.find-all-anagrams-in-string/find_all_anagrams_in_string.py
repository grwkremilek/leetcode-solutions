#https://leetcode.com/problems/find-all-anagrams-in-a-string/

def findAnagrams(s, p):
    ans = []
    n, m = len(s), len(p)
    phash, shash = [0]*123, [0]*123
    if n < m: 
        return ans
    for x in p:
        phash[ord(x)] += 1
    for x in s[:m-1]:
        shash[ord(x)] += 1
    for i in range(m-1, n):
        shash[ord(s[i])] += 1
        if i-m >= 0:
            shash[ord(s[i-m])] -= 1
        if shash == phash:
            ans.append(i - m + 1)
    return ans


def findAnagrams(s, p):
    result = []
    if len(p) > len(s): 
        return result
    d1, d2 = [0] * 26, [0] * 26
    for i in range(len(p)):
        d1[ord(s[i]) - 97] += 1
        d2[ord(p[i]) - 97] += 1
    if d1 == d2: 
        result.append(0)
    for i in range(1, len(s) - len(p) + 1):
        d1[ord(s[i + len(p) - 1]) - 97] += 1
        d1[ord(s[i - 1]) - 97] -= 1
        if d1 == d2: 
            result.append(i)
    return result


def findAnagrams(s, p):
    results = []
    pLen = len(p)
    sLen = len(s)
    if pLen > sLen:
        return results
    ps = [0] * 26
    ss = [0] * 26
    for i in range(pLen):
        ps[ord(p[i])-97] += 1
        ss[ord(s[i])-97] += 1
    if ps == ss:
        results.append(0)
    for i in range(pLen, sLen):
        ss[ord(s[i])-97] += 1
        ss[ord(s[i-pLen])-97] -= 1
        if ps == ss:
            results.append(i - pLen + 1)
    return results
