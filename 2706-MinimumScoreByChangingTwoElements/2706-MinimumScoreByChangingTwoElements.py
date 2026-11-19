# Last updated: 19/11/2026, 1:16:38 pm
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        s = sorted(nums)
        return min(
            (s[-1] - s[2]),
            (s[-2] -s[1]),
            (s[-3]- s[0])
        )
        # return a+2