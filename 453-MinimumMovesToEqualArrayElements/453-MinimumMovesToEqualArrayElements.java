// Last updated: 1/11/2026, 1:49:34 pm
class Solution {
    public int minMoves(int[] nums) {
        //Arrays.sort(nums);
        int min = nums[0];
        for(int i=1;i<nums.length;i++){
            if(min > nums[i]){
                min = nums[i];
            }
        }
        int count = 0;
        for(int i=0;i<nums.length;i++){
            count = nums[i] - min + count;
        }
        return count;
    }
}