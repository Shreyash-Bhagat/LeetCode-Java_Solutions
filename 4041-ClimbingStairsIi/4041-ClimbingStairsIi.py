# Last updated: 10/11/2026, 6:03:06 pm
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = 0 
        b = 0
        c = 0
        for i in range(n):
            nxt = min(min(a+9,b+4),c+1) + costs[i]
            a = b
            b = c 
            c = nxt
        return c