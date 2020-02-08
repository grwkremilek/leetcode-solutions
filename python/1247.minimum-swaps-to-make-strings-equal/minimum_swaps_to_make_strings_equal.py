# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

def minimumSwap(s1, s2):
    x = 0
    y = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] == "x":
            x += 1
        if s1[i] != s2[i] and s1[i] == "y":
            y += 1
    if (x + y) % 2 != 0:
        return -1
    return x//2 + y//2 + 2*(x%2)
