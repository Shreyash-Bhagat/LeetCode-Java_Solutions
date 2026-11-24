# Last updated: 24/11/2026, 1:16:02 pm
class Solution:
    def restoreString(self, s: str, indx: list[int]) -> str:
        strr = ""*len(indx)
        # ct = 0 
        for i in range(len(indx)):
            strr+=s[indx.index(i)]
            # ct+=1

        return strr
            