# Last updated: 16/11/2026, 2:29:15 pm
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        if len(s) == 1:
            return s
        while(len(s) > k):
            ans = ''
            ct = 0
            summ = 0
            for i in s:
                summ += int(i)
                ct+=1
                if(ct ==k):
                    ans += str(summ)
                    summ = 0
                    ct = 0
            if(ct > 0):
                ans += str(summ)
            # print(ans)
            s = ans
        return s
            
            
