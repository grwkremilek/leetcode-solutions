#https://leetcode.com/problems/long-pressed-name/

def isLongPressedName(name, typed):
    n0, n1 = 0, len(name)
    t0, t1 = 0, len(typed)
    while n0 < n1 and t0 < t1:
        if name[n0] == typed[t0]:
            n0 += 1
            t0 += 1
        elif typed[t0] == typed[t0-1]:
            t0 += 1
        else:
            return False
    return True if n0==n1 else False
		
		
