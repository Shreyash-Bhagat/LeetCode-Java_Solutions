# Last updated: 25/10/2026, 10:19:36 pm
class Solution:
    

    def closedIsland(self, grid: list[list[int]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j] == 0):
                    if(self.checkk(grid,i,j)):
                        count+=1
        return count
    
    def checkk(self,grid,st,ed):
        if(st<0 or ed<0 or st>=len(grid) or ed >= len(grid[0])):
            return False
        if(grid[st][ed] == 1):
            return True
        grid[st][ed] = 1

        up = self.checkk(grid,st-1,ed)
        down = self.checkk(grid,st+1,ed)
        right = self.checkk(grid,st,ed+1)
        left = self.checkk(grid,st,ed-1)
        return up and down and right and left