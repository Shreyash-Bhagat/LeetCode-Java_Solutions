// Last updated: 25/10/2026, 7:07:21 pm
class Solution {
    static boolean Check(int grid[][],int start,int end){
        if(start < 0 || end < 0 || start >= grid.length || end >= grid[0].length){
            return false;
        }
        if(grid[start][end] == 1){
            return true;
        }
        grid[start][end] =1;

        boolean up =Check(grid,start-1,end);
        boolean down = Check(grid,start+1,end);
        boolean right = Check(grid,start,end+1);
        boolean left = Check(grid,start,end-1);

        return up && down && right && left;
    }
    public int closedIsland(int[][] grid) {
        int count = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] == 0){
                    if(Check(grid,i,j)){
                        count++;
                    }
                }
            }
        }
        return count;
    }
    
}