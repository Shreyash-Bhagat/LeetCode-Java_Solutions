// Last updated: 18/10/2026, 9:04:19 am
class Solution {
    public int[] lastVisitedCell(char[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        boolean[][] arr = new boolean[row][col];
        arr[0][0] = true;
        int r =0;
        int c =0;
        while(true){
            int rr = r;
            int cc = c;

            if(grid[rr][cc] == 'L'){
                cc--;
            }
            else if(grid[rr][cc] == 'R'){
                cc++;
            }
            else if(grid[rr][cc] == 'U'){
                rr--;
            }
            else{
                rr++;
            }

            if(rr < 0 || cc < 0 ||rr >= grid.length || cc >= grid[0].length || arr[rr][cc]){
                break;
            }
            r =rr;
            c =cc;
            arr[r][c] = true;
        }
        int[] a1 = {0,0};
        a1[0] = r;
        a1[1] = c;
            
        return a1;
    }
}