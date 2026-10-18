// Last updated: 18/10/2026, 8:11:44 am
class Solution {
    public int minDeletions(int[] nums) {
        int count = 0;
        for(int i=1;i<nums.length;i++){
            if((nums[i-1]^nums[i]) == 0){
                count++;
            }
        }
        return count;
    }
}