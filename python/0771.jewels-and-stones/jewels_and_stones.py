# brute force (68ms)
def numJewelsInStones(J, S):
    count=0
    for s in S:
        if s in J:
            count += 1
    return count


#40ms
def numJewelsInStones(J, S):
    return sum(s in J for s in S)


#32ms
def numJewelsInStones(J, S):
    return(len([x for x in S if x in J]))

