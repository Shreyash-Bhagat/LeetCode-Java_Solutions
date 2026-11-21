# Last updated: 21/11/2026, 8:55:30 pm
class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        ans = []
        n = len(rain)
        # sunn = sum(rain)
        a_cnt = 0
        b_cnt = 0

        for i in range(len(rain)):
            a_need = i<n-1 and rain[i]==1 and rain[i+1] ==1
            b_need = rain[i] == 1
            if(a_need and b_need):
                if(a_cnt <= b_cnt):
                    ans.append("Alice")
                    a_cnt+=1
                else:
                    ans.append("Bob")
                    b_cnt+=1

            elif(a_need):
                ans.append("Alice")
                a_cnt+=1
            elif(b_need):
                ans.append("Bob")
                b_cnt+=1
            else:
                ans.append("None")
        return ans