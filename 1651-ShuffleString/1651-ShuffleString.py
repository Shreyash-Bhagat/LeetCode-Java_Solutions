# Last updated: 24/11/2026, 12:49:29 pm
class Solution:
    def restoreString(self, s: str, indx: list[int]) -> str:
        strr = ""
        ct = 0 
        for i in range(len(indx)):
            # z = 
            strr+=s[indx.index(ct)]
            ct+=1
        return strr
            