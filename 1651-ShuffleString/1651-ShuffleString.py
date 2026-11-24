# Last updated: 24/11/2026, 12:54:58 pm
class Solution:
    def restoreString(self, s: str, indx: list[int]) -> str:
        strr = ""
        ct = 0 
        if(indx == sorted(indx)):
            return s
        for i in range(len(indx)):
            strr+=s[indx.index(ct)]
            ct+=1
        return strr
            