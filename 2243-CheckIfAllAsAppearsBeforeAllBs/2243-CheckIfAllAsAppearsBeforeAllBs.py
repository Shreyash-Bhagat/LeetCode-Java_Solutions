# Last updated: 22/11/2026, 7:42:29 am
class Solution:
    def checkString(self, s: str) -> bool:
        ct = 0
        for i in range(len(s)):
            if(ct > 0  and s[i]=='a'):
                return False
            elif(s[i] == 'b'):
                ct+=1
            else:
                pass
        return True