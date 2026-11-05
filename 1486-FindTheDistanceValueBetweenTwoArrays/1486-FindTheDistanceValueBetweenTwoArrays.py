# Last updated: 5/11/2026, 6:16:57 am
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        # maxx = -inf
        ele = 0
        for i in arr1:
            # count = 0
            isValid = True
            for j in arr2:
                if(abs(i-j) <= d):
                    isValid = False
                    break
                    # count+=1
            if isValid:
                ele+=1

        return ele