# Last updated: 7/11/2026, 12:39:59 pm
class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        a=str(a)
        ans = a[::-1]
        # print(ans)
        ans = int(ans)
        if(ans > (2**31 - 1)):
            return 0
        if(x<0):
            return ans*-1
# 2147483647
        return ans