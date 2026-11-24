# Last updated: 24/11/2026, 10:31:29 am
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxx = 0
        n = len(nums)
        for i in range(len(nums)):
            prod = 1 
            gcd = 0
            lcm = 1

            for j in range(i,n):
                val = nums[j]
                prod *= val
                gcd = math.gcd(gcd,val)
                lcm = math.lcm(lcm,val)

                if prod == gcd*lcm:
                    maxx = max(maxx,j-i+1)
        return maxx
