# Last updated: 21/11/2026, 9:06:52 pm
class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        min_ele = min(a,b,c)
        max_ele = max(a,b,c)
        sum_ele = a+b+c
        z = sum_ele-max_ele-min_ele
        if(min_ele == max_ele):
            return 0
        elif(z+min_ele > max_ele):
            return (max_ele - min_ele)

        else:
            return (z+min_ele - min_ele)