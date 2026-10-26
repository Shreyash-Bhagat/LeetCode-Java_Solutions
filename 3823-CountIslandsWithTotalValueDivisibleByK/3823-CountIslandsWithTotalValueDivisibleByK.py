# Last updated: 26/10/2026, 3:25:08 pm
class Solution:
    def check(self,grid,st,ed):
        if(st<0 or ed < 0 or st >= len(grid) or ed >= len(grid[0])):
            return 0
        if grid[st][ed] == 0:
            return 0
        value = grid[st][ed]
        grid[st][ed] = 0
        up = self.check(grid,st-1,ed)
        down = self.check(grid,st+1,ed)
        right = self.check(grid,st,ed+1)
        left = self.check(grid,st,ed-1)

        return value+up+down+right+left

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((grid[i][j]) != 0):
                    if((self.check(grid,i,j))%k == 0 ):
                        count+=1
        return count