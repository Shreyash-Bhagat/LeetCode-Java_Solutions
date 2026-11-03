# Last updated: 3/11/2026, 10:12:12 am
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx = max(nums)
        ans = 0
        for i in nums:
            ans += maxx - i
        return ans
        