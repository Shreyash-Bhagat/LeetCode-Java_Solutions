# Last updated: 8/11/2026, 8:38:21 pm
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        row_count = [0]*row
        col_count = [0]*col

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_count[i] +=1
                    col_count[j] +=1
        
        count = 0
        for i in range(row):
            for j in range(col):
                if(grid[i][j] == 1):
                    if(row_count[i] > 1 or col_count[j] > 1):
                        count+=1
        return count