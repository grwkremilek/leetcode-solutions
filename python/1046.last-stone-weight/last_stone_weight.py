#https://leetcode.com/problems/last-stone-weight/

def lastStoneWeight(stones):
        stones = sorted(stones)
        for _ in range(len(stones)-1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))
        return stones.pop()
