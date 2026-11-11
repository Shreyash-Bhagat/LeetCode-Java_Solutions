# Last updated: 11/11/2026, 1:35:09 pm
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if(need1 == 0):
            return min((need2*cost2),need2*costBoth)
        if(need2 == 0):
            return min((need1*cost1),need1*costBoth)

        if(cost1+cost2 < costBoth):
            return (need1*cost1 + need2*cost2)
        else:
            if(need1 > need2):
                a = need1 - need2
                b = need2*costBoth
                a *= cost1
                return min((a+b),need1*costBoth)
            elif need1 == need2:
                return need1*costBoth
            else:
                a = need2 - need1
                b = need1*costBoth
                a = a*cost2
                return min((a+b),need2*costBoth)
        return 0 
                
        