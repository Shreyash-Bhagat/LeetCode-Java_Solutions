# Last updated: 24/11/2026, 1:19:59 pm
class Solution:
    def restoreString(self, s: str, indx: list[int]) -> str:
        strr = [""]*len(s)
        # ct = 0 
        # for i in range(len(indx)):
        #     strr+=s[indx.index(i)]
        #     # ct+=1
        for i in range(len(s)):
            strr[indx[i]] = s[i]
        return "".join(i for i in strr)
            