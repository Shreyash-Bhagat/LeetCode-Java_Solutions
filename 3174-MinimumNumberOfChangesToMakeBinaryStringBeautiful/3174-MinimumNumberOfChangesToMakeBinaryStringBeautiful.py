# Last updated: 18/11/2026, 2:18:24 pm
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(1,len(s),2):
            if s[i-1] != s[i]:
                count+=1
                
        return count