// Last updated: 15/10/2026, 9:16:48 am
class Solution {
    public int sumCounts(List<Integer> nums) {
        int ans = 0;
        for(int i=0;i<nums.size();i++){
            for(int j=i;j<nums.size();j++){
                HashSet<Integer> hm = new HashSet<>();
                for(int k=i;k<=j;k++){
                    hm.add(nums.get(k));
                }
                ans += hm.size()*hm.size();
                
            }
        }
        return ans;
    }
}