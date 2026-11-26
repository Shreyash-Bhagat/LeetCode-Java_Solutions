# Last updated: 26/11/2026, 10:30:02 am
class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n-10<0:
            return False
        alice = 10
        bob = alice-1
        while(n>0):
            n-=alice
            if(n<0):
                return False
            elif(n==0):
                return True
            n-=bob
            if(n<0):
                return True
            elif(n==0):
                return False
            alice=bob-1
            bob=alice-1
        return True

            
            

        