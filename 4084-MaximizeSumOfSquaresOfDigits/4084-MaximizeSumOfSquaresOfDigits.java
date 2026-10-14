// Last updated: 14/10/2026, 8:58:17 am
class Solution {
    public String maxSumOfSquares(int num, int sum) {
        // if(num == 1){
        //     return sum.toString();
        // }
        if (sum > 9 * num) {
            return "";
        }
        int r = sum % 9;
        StringBuilder ans = new StringBuilder();
        int nines = sum / 9;
        for (int i = 0; i < nines; i++) {
            ans.append('9');
        }
        if (r > 0) {
            ans.append((char) ('0' + r));
        }
        int zeros = num - ans.length();
        for (int i = 0; i < zeros; i++) {
            ans.append('0');
        }
        return ans.toString();
        

    }
}