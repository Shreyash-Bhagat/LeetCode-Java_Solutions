# Last updated: 28/10/2026, 10:44:09 am
class Solution:
    def minCost(self, A: List[List[int]]) -> int:
        s = set()
        res = inf

        def dfs(i: int, j: int, xor: int) -> None:
            nonlocal res
            if res == 0 or i < 0 or j < 0 or (i, j, xor) in s:
                return
            s.add((i, j, xor))
            xor ^= A[i][j]
            if i == 0 and j == 0:
                res = min(res, xor)
                return
                
            dfs(i - 1, j, xor)
            dfs(i, j - 1, xor)

        dfs(len(A) - 1, len(A[0]) - 1, 0)

        return res