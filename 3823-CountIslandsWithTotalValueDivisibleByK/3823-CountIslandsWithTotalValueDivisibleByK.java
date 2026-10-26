// Last updated: 26/10/2026, 9:36:34 am
class Solution {
    static long check(int grid[][] , int st ,int ed){
        if(st<0 || ed < 0 || st >= grid.length || ed >= grid[0].length){
            return 0;
        }

        if(grid[st][ed] == 0){
            return 0;
        } 
        long a = grid[st][ed];
        grid[st][ed] = 0;
        long up = check(grid , st-1,ed);
        long down = check(grid,st+1,ed);
        long right = check(grid,st,ed+1);
        long left = check(grid,st,ed-1);

        return a+up+down+right+left;
    }
    public int countIslands(int[][] grid, int k) {

        int count = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] != 0){
                    if((check(grid,i,j)%k) == 0){
                        count++;
                    }
                }
            }
        }
        return count;
        
    }
}