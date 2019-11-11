
def numJewelsInStones(J, S):
    count=0
    for s in S:
        if s in J:
            count += 1
    return count


def numJewelsInStones(J, S):
    return sum(s in J for s in S)


def numJewelsInStones(J, S):
    return(len([x for x in S if x in J]))


def numJewelsInStones(J, S):
    d = {}
    for c in S:
        if c in J:
            d[c] = d.get(c, 0) + 1
    return sum(d.values())


def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(J.count,S))
