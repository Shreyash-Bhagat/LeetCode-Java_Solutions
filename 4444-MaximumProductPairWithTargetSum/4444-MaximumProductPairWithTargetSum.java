// Last updated: 10/10/2026, 8:20:55 pm
class Solution {
    public int[] maxProductPair(int[] nums, int target) {
        
        int[] arr = new int[2];
        int maxx = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(i != j){
                    if(nums[i]>nums[j]){
                        int sum = 0;
                        sum = nums[i]+nums[j];
                        if(sum == target){
                            int mul = nums[i]*nums[j];
                            if(mul > maxx){
                                maxx = mul;
                                arr[0] = i;
                                arr[1] = j;
                            }
                        }
                    }
                }
            }
        }
        if(maxx == Integer.MIN_VALUE){
            arr[0] = -1;
            arr[1] = -1;
            return arr;
        }
        return arr;
    }
}