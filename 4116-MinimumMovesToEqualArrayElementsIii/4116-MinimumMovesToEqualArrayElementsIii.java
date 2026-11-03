// Last updated: 3/11/2026, 10:22:09 am
class Solution {
    public int minMoves(int[] nums) {
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            max = Math.max(max,nums[i]);
            sum += nums[i];
        }
        
        return max*nums.length-sum;
    }
}