# Last updated: 3/11/2026, 10:15:58 am
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums)*len(nums)-sum(nums)
        