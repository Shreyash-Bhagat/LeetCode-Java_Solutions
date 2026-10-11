// Last updated: 11/10/2026, 10:05:20 am
class Solution {
    public int sumOfSquares(int[] nums) {
        int len = nums.length;
        int sum = 0;
        for(int i=0;i<len;i++){
            if(len%(i+1) ==0){
                sum += nums[i]*nums[i];
            }
        }
        return sum;
    }
}