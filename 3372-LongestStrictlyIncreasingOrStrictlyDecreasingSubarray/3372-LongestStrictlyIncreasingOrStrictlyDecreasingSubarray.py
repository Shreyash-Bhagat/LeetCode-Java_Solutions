# Last updated: 12/11/2026, 1:06:40 pm
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        countIn = 1
        countDe = 1
        count1 = 1
        count2 = 1
        for i in range(len(nums)-1):  
            if(nums[i] < nums[i+1]):
                count1 += 1
                countIn = max(count1,countIn) 
                count2 = 1
            if(nums[i] > nums[i+1]):
                count2 += 1
                countDe = max(count2,countDe)
                count1 = 1
            if(nums[i] == nums[i+1]):
                count1 = 1
                count2 = 1
        return max(countIn,countDe)