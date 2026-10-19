// Last updated: 19/10/2026, 1:40:06 pm
class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        Arrays.sort(nums);
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(nums[i] == target){
                ans.add(i);
            }
        }
        return ans;
    }
}