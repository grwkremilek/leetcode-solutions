#https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        A = list(map(lambda a: a - diff, A))
        b = (list(set(A) & set(B)))[0]
        return [b + diff, b]
