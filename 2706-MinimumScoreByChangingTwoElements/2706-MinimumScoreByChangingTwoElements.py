# Last updated: 19/11/2026, 1:28:14 pm
class Solution:
    def minimizeSum(self, s: List[int]) -> int:
        if len(s) == 3:
            return 0
        # s = sorted(nums)
        s.sort()
        return min(
            (s[-1] - s[2]),
            (s[-2] -s[1]),
            (s[-3]- s[0])
        )
        # return a+2