# Last updated: 24/11/2026, 10:32:45 am
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxx = 0
        # n = len(nums)
        for i in range(len(nums)):
            prod = 1 
            gcd = 0
            lcm = 1

            for j in range(i,len(nums)):
                # val = nums[j]
                prod *= nums[j]
                gcd = math.gcd(gcd,nums[j])
                lcm = math.lcm(lcm,nums[j])

                if prod == gcd*lcm:
                    maxx = max(maxx,j-i+1)
        return maxx
