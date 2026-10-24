# Last updated: 24/10/2026, 10:45:04 am
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive_alice = arriveAlice.split('-')
        leave_alice = leaveAlice.split('-')
        arrive_bob = arriveBob.split('-')
        leave_bob = leaveBob.split('-')
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # print(arrive_alice,leave_alice,arrive_bob ,leave_bob)
        sumAliceA = sum(months[ : int(arrive_alice[0])-1] )+ int(arrive_alice[1]) 

        sumAliceE = sum(months[: int(leave_alice[0])-1]) + int(leave_alice[1]) 

        sumBobA = sum(months[: int(arrive_bob[0])-1] )+ int(arrive_bob[1]) 
        
        sumBobE = sum(months[: int(leave_bob[0])-1] )+ int(leave_bob[1]) 

        start = max(sumAliceA,sumBobA)
        end = min(sumAliceE,sumBobE)

        if(start<= end):
            return end-start+1
        return 0