# Last updated: 2/11/2026, 10:14:37 am
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums)//2

        ans = 0
        ans_1 = 0
        for i in range(len(nums)):
            ans_1 += abs(nums[i] - nums[mid-1])
        for i in range(len(nums)):
            ans += abs(nums[i] - nums[mid])

        return min(ans_1,ans)