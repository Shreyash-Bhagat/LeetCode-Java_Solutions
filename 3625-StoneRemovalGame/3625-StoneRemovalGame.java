// Last updated: 26/11/2026, 10:36:36 am
class Solution {
    public boolean canAliceWin(int n) {
        int r = 10;

        while(n>=r){
            n -=r;
            r -= 1;
        }

        return r%2 ==1;
    }
}