# Last updated: 14/11/2026, 12:09:31 pm
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minn = inf
        # prefix = []
        count = l
        while (count <= r):
            for i in range(len(nums)):
                flag = False
                ss = 0
                for j in range(count):
                    if (i+count-1) < len(nums):
                        flag = True
                        ss += nums[i+j]
                if(flag):
                    if ss > 0:
                        minn = min(minn,ss)
                    # prefix.append(ss)
            count+=1
        # print(prefix)
        if minn == inf:
            return -1
        return minn