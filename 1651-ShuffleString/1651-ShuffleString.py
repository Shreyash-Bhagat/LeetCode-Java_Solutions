# Last updated: 24/11/2026, 12:47:13 pm
class Solution:
    def restoreString(self, s: str, indx: list[int]) -> str:
        strr = ""
        ct = 0 
        for i in range(len(indx)):
            z = indx.index(ct)
            strr+=s[z]
            ct+=1
        return strr
            