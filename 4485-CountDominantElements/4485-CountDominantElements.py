# Last updated: 22/11/2026, 8:22:06 am
class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        ct = 0
        n =len(nums)
        if(n == 1):
            return 1
        for i in range(n):
            if(i == 0):
                if(nums[i] >= nums[i+1]):
                    ct+=1
            elif(i == (n-1) ):
                if(nums[i] >= nums[i-1]):
                    ct+=1
            else:
                avg = (nums[i-1] + nums[i+1]) / 2
                if(nums[i] >= avg):
                    print(avg)
                    ct+=1
        return ct
            