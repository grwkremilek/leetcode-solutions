#https://leetcode.com/problems/sort-characters-by-frequency/
 
def frequencySort(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return ''.join([k*v for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True)])
